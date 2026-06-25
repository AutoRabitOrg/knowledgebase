# Server Installation

## IZ Suite Server Installation

{% hint style="warning" %}
Before installing, make sure you have:

* Purchased a valid license.
* Installed Docker
* Installed PostgreSQL database and have the connection details handy. Supports v12 and higher
{% endhint %}

### Starting IZ Server - Using Docker

1. Run the following command
2. Replace **`FALCON_SERVER_VERSION`** with the latest version of the software. Latest version can be here. For example, if the latest version is v1.2.1, replace **`FALCON_SERVER_VERSION`** with **`1.2.1`**
3. Replace **`USERNAME`**,**`PASSWORD`**,**`HOST`**,**`PORT`**,**`DB_NAME`** with appropriate Database credentials and DB name SHELL> docker run -e DATABASE\_URL=postgres://:@:/\<DB\_NAME> -p80:80 public.ecr.aws/h0h7r7j4/falcon-suite:\<FALCON\_SERVER\_VERSION>
4. If there is any other process running on port 80, change the -p80:80 mapping. For example - to map to port 9000 change the -p80:80 to -p9000:80
5. Once the container is up and running navigate to **`SERVER_IP`** in the browser. For example - http://localhost

### Starting IZ Server - Using Docker Compose

6. Save the below docker compose script in a file. For example: iz-server-docker-compose.yml

```yaml
version: '3.8'
services:

  iz-server:
    image: public.ecr.aws/h0h7r7j4/falcon-suite:<FALCON_SERVER_VERSION>
    ports:
      - '80:80'
      - '443:443'
    environment:
      - FALCON_MODE=all
      - DATABASE_URL=postgres://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>
    healthcheck:
      test: curl --fail http://localhost/api/graphql/health || exit 1
      interval: 10s
      timeout: 20s
      retries: 3
```

7. Replace the value of **`FALCON_SERVER_VERSION`** with a valid server version
8. Replace **`USERNAME`**,**`PASSWORD`**,**`HOST`**,**`PORT`**,**`DB_NAME`** with appropriate Database credentials and DB name
9. Run the below command to start the server SHELL> docker compose -f iz-server-docker-compose.yml up
10. NOTE: Use option **`-d`** to start the instance in background
11. Once the container is up and running navigate to **`SERVER_IP`** in the browser. For example - http://localhost

### Starting IZ Instance - with SSL

1. Create a new directory called **`conf`** and file called **`server_ssl`** within the **`conf`** directory
2. Copy the below contents to **`server_ssl`** file

```json
    upstream iz-server {
      server localhost:8911 fail_timeout=0;
    }

    server {
        listen 80 default_server;
        server_name _;

          return 301 https://$host$request_uri;
    }

    server {

      access_log off;
      error_log /dev/stderr; # Redirect error logs to stderr

      listen 443 ssl default_server;
      listen [::]:443 ssl default_server;

      ssl_certificate    /var/falcon/ssl/tls.crt;
      ssl_certificate_key /var/falcon/ssl/tls.key;

      root /home/node/app/web/dist;

      index index.html index.htm index.nginx-debian.html;

      server_name iz_suite;

      gzip on;
      gzip_min_length 1000;
      gzip_types application/json text/css application/javascript application/x-javascript;

      sendfile on;

      keepalive_timeout 65;

      location ~* \.(?:css|js)$ {
          expires 1h;
          add_header Pragma public;
          add_header Cache-Control "public";
          access_log off;
      }

      location ~* \.(?:ico|gif|jpe?g|png)$ {
          expires 7d;
          add_header Pragma public;
          add_header Cache-Control "public";
          access_log off;
      }

      location /api/graphql {
          proxy_set_header Host $host;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_pass http://iz-server;
      }

      location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        try_files $uri $uri/ /index.html;
      }

    }
```

3. Make sure valid SSL certificates are copied to **`conf`** directory -
   1. **`tls.crt`** - CA signed certificated
   2. **`tls.key`** - Key used to generate the certificate
4. Replace the value of **`FALCON_SERVER_VERSION`** with a valid server version
5. Replace **`USERNAME`**,**`PASSWORD`**,**`HOST`**,**`PORT`**,**`DB_NAME`** with appropriate Database credentials and DB name
6. Run the below command to start the server SHELL> docker run -e DATABASE\_URL=postgres://:@:/\<DB\_NAME> -v $(pwd)/conf/server\_ssl:/etc/nginx/sites-enabled/default -v $(pwd)/conf/tls.crt:/var/falcon/ssl/tls.crt -v $(pwd)/conf/tls.key:/var/falcon/ssl/tls.key -p80:80 public.ecr.aws/h0h7r7j4/falcon-suite:\<FALCON\_SERVER\_VERSION>
7.  (Optional) Below is an example of running the same command using docker compose -

    1. Save the below docker compose script in a file. For example: iz-server-docker-compose.yml

    ```yaml
    version: '3.8'
    services:

      iz-server:
        image: public.ecr.aws/h0h7r7j4/falcon-suite:<FALCON_SERVER_VERSION>
        volumes:
          - ./conf/server_ssl:/etc/nginx/sites-enabled/default
          - ./conf/tls.crt:/var/falcon/ssl/tls.crt
          - ./conf/tls.key:/var/falcon/ssl/tls.key
        ports:
          - '80:80'
          - '443:443'
        environment:
          - FALCON_MODE=all
          - DATABASE_URL=postgres://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>
        healthcheck:
          test: curl --fail http://localhost/api/graphql/health || exit 1
          interval: 10s
          timeout: 20s
          retries: 3
    ```

    2. Run the below command to start the server SHELL> docker compose -f iz-server-docker-compose.yml up
    3. NOTE: Use option **`-d`** to start the instance in background

Once the container is up and running navigate to **`SERVER_IP`** in the browser. For example - https://localhost

### From AWS Debian CIS Hardened Image

1. Navigate to EC2 -> AMIs -> select **`IZ Suite CIS 1.x`** and click on **`Launch Instance from AMI`**&#x20;
2. Click on "Advanced details" and add the required configuration -

| Key                       | Description                                                                                                                                                                                                                                                                                                                                                               | Required? |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| SERVER\_VERSION           | The latest version of IZ Server can be found here                                                                                                                                                                                                                                                                                                                         | Yes       |
| AGENT\_VERSION            | The latest version of IZ Agent                                                                                                                                                                                                                                                                                                                                            | Yes       |
| PORT                      | Port on which the IZ Web should be exposed. Example 80 for http protocol and 443 for https protocol                                                                                                                                                                                                                                                                       | Yes       |
| PROTOCOL                  | Possible values **`http`** or **`https`**                                                                                                                                                                                                                                                                                                                                 | Yes       |
| CLOUD\_WATCH\_LOGS\_GROUP | Optional **`AWS Cloud Watch`** group name where the IZ Suite logs should be redirected to. If this option is configured, make sure a new IAM role is created with **`AWS Service`** type, **`EC2`** use case, **`CloudWatchAgentServerPolicy`** policy. Associate the same role to the EC2 Instance by navigating to **`Actions`**, **`Security`**, **`Modify IAM role`** | No        |
| DB\_URL                   | A valid **`Database`** url. Connection string example can be found below                                                                                                                                                                                                                                                                                                  | Yes       |

1. Example

```shell
#!/bin/bash

bash -c "cat > /etc/falcon-suite/config.env" &lt;&lt;EOF
SERVER_VERSION=1.3.3
AGENT_VERSION=1.0.8
PORT=443
PROTOCOL=https
DB_URL=postgres://dbuser:dbpass@dbhost:dbport/dbname
EOF
```

<figure><img src="../../../../.gitbook/assets/ec2_launch_instance_2.png" alt=""><figcaption></figcaption></figure>

### See Also

* [Prerequisites](installation-requirements.md)
* [Cluster Mode](cluster-installation.md)
