# Using AWS Debian CIS Hardened Image

IZ Suite is available as an Amazon Machine Image (AMI) built on Debian and hardened to the CIS benchmark. The image comes with Docker installed. When the instance starts, it reads a short configuration you provide in the EC2 **User data** field, then pulls and runs the IZ Suite server and agent. You don't install anything by hand.

{% hint style="info" %}
Prefer containers on your own host? See Server Installation for running IZ Suite with Docker or Docker Compose.
{% endhint %}

### How It Works

1. You launch an EC2 instance from the **IZ Suite CIS** AMI.
2. The user data script writes your settings to `/etc/falcon-suite/config.env`.
3. On boot, the instance starts two containers on the host network:
   * **IZ Suite server**: the web application and API, at the version you set in `SERVER_VERSION`, exposed on `PORT`.
   * **IZ Suite agent**: runs scans and other jobs, at the version you set in `AGENT_VERSION`. It connects to the server on the same host.
4. The server connects to your PostgreSQL database through `DB_URL` and prepares it on first start.
5. Optionally, logs are sent to an Amazon CloudWatch log group.

<figure><img src="../../../../.gitbook/assets/ec2_launch_instance.png" alt=""><figcaption></figcaption></figure>

### Before You Begin

Make sure you have:

* A valid IZ Suite licence.
* An AWS account with permission to launch EC2 instances, and to manage security groups and IAM roles if you use CloudWatch.
* A PostgreSQL database, **version 12 or later**, that the instance can reach over the network (for example, Amazon RDS for PostgreSQL), plus its connection details.
* The IZ Suite **server** and **agent** versions you want to run.
* For HTTPS, a valid TLS certificate for the host name users will open.

{% hint style="warning" %}
The database must be reachable from the EC2 instance. With Amazon RDS, allow inbound PostgreSQL traffic (port `5432` by default) from the instance's security group.
{% endhint %}

### Step 1: Prepare the Database

1. Create an empty database for IZ Suite, for example `izsuite`.
2. Create a database user that owns this database (or has full rights on it).
3. Build the connection string:

```
postgres://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>
```

| Part       | Example                                   |
| ---------- | ----------------------------------------- |
| `USERNAME` | `izsuite_app`                             |
| `PASSWORD` | the database user's password              |
| `HOST`     | `mydb.abc123.eu-west-2.rds.amazonaws.com` |
| `PORT`     | `5432`                                    |
| `DB_NAME`  | `izsuite`                                 |

{% hint style="info" %}
If the password contains special characters such as `@`, `:`, `/` or `#`, URL-encode them. For example, `@` becomes `%40`.
{% endhint %}

### Step 2: Launch an Instance From the AMI

1. In the AWS console, go to **EC2 → AMIs**.
2. Select **IZ Suite CIS 1.x**, then choose **Launch instance from AMI**.
3. Enter a name, choose an instance type, and select a key pair if you want SSH access.
4. Under **Network settings**, choose the VPC and subnet that can reach your database.

### Step 3: Allow Network Access

Create or choose a security group for the instance:

| Direction | Port                     | Source / destination    | Why                                                                             |
| --------- | ------------------------ | ----------------------- | ------------------------------------------------------------------------------- |
| Inbound   | `PORT` (`80` or `443`)   | Your users' network     | Open IZ Suite in a browser                                                      |
| Inbound   | `22` (optional)          | Your admin network only | SSH for troubleshooting                                                         |
| Outbound  | `5432` (or your DB port) | The database            | Server to database                                                              |
| Outbound  | `443`                    | Internet                | Pull IZ Suite images from `public.ecr.aws`, and reach the platforms you analyse |

### Step 4: Add the Configuration

Expand **Advanced details** and paste your configuration into **User data**.

| Key                      | Description                                                                                        | Required |
| ------------------------ | -------------------------------------------------------------------------------------------------- | -------- |
| `SERVER_VERSION`         | IZ Suite server version to run.                                                                    | Yes      |
| `AGENT_VERSION`          | IZ Suite agent version to run.                                                                     | Yes      |
| `PORT`                   | Port that serves the IZ Suite web application. Use `80` for HTTP or `443` for HTTPS.               | Yes      |
| `PROTOCOL`               | `http` or `https`.                                                                                 | Yes      |
| `DB_URL`                 | PostgreSQL connection string from Step 1.                                                          | Yes      |
| `CLOUD_WATCH_LOGS_GROUP` | Name of an Amazon CloudWatch log group to send IZ Suite logs to. Requires an IAM role, see Step 5. | No       |

**Example**

```bash
#!/bin/bash

bash -c "cat > /etc/falcon-suite/config.env" <<EOF
SERVER_VERSION=1.3.3
AGENT_VERSION=1.0.8
PORT=443
PROTOCOL=https
DB_URL=postgres://dbuser:dbpass@dbhost:5432/dbname
EOF
```

<figure><img src="../../../../.gitbook/assets/ec2_launch_instance_2.png" alt=""><figcaption></figcaption></figure>

To send logs to CloudWatch, add one more line before `EOF`:

```bash
CLOUD_WATCH_LOGS_GROUP=/izsuite/production
```

{% hint style="danger" %}
User data is stored with the instance in plain text. Anyone who can view the instance's user data can read the database password in `DB_URL`. Limit who can view instance attributes in IAM, and use a database user that only has access to the IZ Suite database.
{% endhint %}

### Step 5 (Optional): Send Logs to CloudWatch

If you set `CLOUD_WATCH_LOGS_GROUP`, the instance needs permission to write logs:

1. In **IAM → Roles**, choose **Create role**.
2. Select **AWS service** as the trusted entity and **EC2** as the use case.
3. Attach the **CloudWatchAgentServerPolicy** policy, then create the role.
4. In **EC2 → Instances**, select the IZ Suite instance, then choose **Actions → Security → Modify IAM role**.
5. Select the new role and save.

Logs then appear in the log group you named.

### Step 6: Launch and Verify

1. Choose **Launch instance**.
2. Wait a few minutes while the instance starts, pulls the images and prepares the database. The first start takes the longest.
3. Open IZ Suite in a browser:
   * `http://<SERVER_IP>` when `PROTOCOL=http` and `PORT=80`
   * `https://<SERVER_HOST>` when `PROTOCOL=https` and `PORT=443`
   * Add `:<PORT>` for any other port.
4. Sign in and apply your licence.

You can also check the server's health from any machine that can reach it:

```bash
curl --fail http://<SERVER_IP>/api/graphql/health
```

{% hint style="success" %}
A successful response means the server is up and connected to the database.
{% endhint %}

### Upgrade to a New Version

The configuration is applied each time the instance starts. To move to a new version:

1. Stop the instance (**Instance state → Stop instance**).
2. Choose **Actions → Instance settings → Edit user data**.
3. Change `SERVER_VERSION` and `AGENT_VERSION`, then save.
4. Start the instance.

{% hint style="warning" %}
Take a snapshot or backup of the database before upgrading. The new server version may update the database schema on first start.
{% endhint %}

### Troubleshooting

| Symptom                                                    | What to check                                                                                                                                           |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The page doesn't load                                      | The security group allows inbound traffic on `PORT` from your network, and `PROTOCOL` and `PORT` match the address you opened.                          |
| The page loads but shows errors, or the health check fails | The database is reachable from the instance (security group and network ACLs), and `DB_URL` is correct, including URL-encoded special characters.       |
| Nothing seems to start                                     | Connect over SSH and run `sudo docker ps` to confirm the server and agent containers are running. `sudo docker logs <container-id>` shows their output. |
| The configuration didn't apply                             | Check `/etc/falcon-suite/config.env` on the instance, and review `/var/log/cloud-init-output.log` for errors from the user data script.                 |
| No logs in CloudWatch                                      | The IAM role with **CloudWatchAgentServerPolicy** is attached to the instance, and `CLOUD_WATCH_LOGS_GROUP` is set.                                     |

### Next Steps

* Prerequisites: system and database requirements.
