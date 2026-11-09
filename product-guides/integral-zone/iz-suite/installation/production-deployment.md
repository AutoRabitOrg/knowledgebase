---
description: >-
  The recommended production setup for IZ Suite on your own cloud account, with
  load-balanced servers, scaling workers and a managed database.
---

# Production Deployment

In production, run the IZ Suite components as separate services on a managed container platform, with a managed PostgreSQL database. This removes the single VM as a point of failure, lets the busy parts scale on their own and keeps backups out of your hands.

The setup below is the one AutoRABIT runs, described for Amazon Web Services. The same layout works on Azure (Container Apps and Azure Database for PostgreSQL) or Google Cloud (GKE and Cloud SQL).

### Recommended Layout

| Part                  | AWS service                                                               | Recommended setting                                                                                                          |
| --------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Load balancer and TLS | Application Load Balancer with a certificate from AWS Certificate Manager | HTTPS on 443, HTTP redirected to HTTPS. Health check `GET /api/graphql/health`.                                              |
| Web firewall          | AWS WAF on the load balancer                                              | AWS managed rule sets, in blocking mode once tested.                                                                         |
| Server                | ECS on Fargate, `iz-suite-server`, `FALCON_MODE=api`                      | At least **2 tasks** of 2 vCPU and 4 GB, in two Availability Zones.                                                          |
| Worker                | ECS on Fargate, `iz-suite-server`, `FALCON_MODE=worker`                   | 1 task of 2 vCPU and 4 GB with `NODE_OPTIONS=--max-old-space-size=3072`, scaling out to 4.                                   |
| Agent                 | ECS on Fargate, `iz-suite-agent`                                          | 1 task of 2 vCPU and 4 GB; add tasks for more scanning or monitoring capacity.                                               |
| Database              | Amazon RDS for PostgreSQL 16                                              | Multi-AZ, storage encryption on, automated backups kept for 14 days, a `db.t4g.large` class or larger as sized by AutoRABIT. |
| Secrets               | AWS Secrets Manager                                                       | `DATABASE_URL`, `SECRETS_ENCRYPTION_KEY` and `AGENT_WRAPPER_SECRET`, injected into the tasks.                                |
| Logs and alarms       | Amazon CloudWatch                                                         | Container logs, and alarms on unhealthy targets, task restarts and database CPU and storage.                                 |

Size the tasks and the database from your inputs; see [Requirements & Sizing](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/requirements-and-sizing).

{% hint style="warning" %}
**HINT (info):** Run the database in private subnets, reachable only from the server and worker tasks. The agent reaches IZ Suite through the load balancer or the internal service address and never needs the database.
{% endhint %}

### Configuration

Every server and worker task uses the same values:

| Variable                 | Required          | Description                                                                                                                   |
| ------------------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `DATABASE_URL`           | Yes               | `postgres://<user>:<password>@<host>:5432/<database>?sslmode=require`                                                         |
| `FALCON_MODE`            | Yes               | `api` for the server, `worker` for the worker.                                                                                |
| `SECRETS_ENCRYPTION_KEY` | Yes               | 64 hexadecimal characters, for example from `openssl rand -hex 32`. Encrypts stored credentials and secure settings.          |
| `AGENT_JOB_TYPE_VERSION` | Yes               | The agent and job-type version, normally the release, for example `26.4.2`. The server and worker refuse to start without it. |
| `AGENT_WRAPPER_SECRET`   | Yes on the server | Shared secret that agents present when they register themselves.                                                              |
| `LOG_LEVEL`              | No                | `error`, `warn`, `info` (default) or `debug`.                                                                                 |

The agent needs:

| Variable               | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `FALCON_AGENT_OPTS`    | `--serviceUrl <IZ Suite address>`, for example `--serviceUrl https://izsuite.yourcompany.com`. |
| `AGENT_WRAPPER_SECRET` | The same value as on the server.                                                               |

> **HINT (danger):** Set `SECRETS_ENCRYPTION_KEY` once and never change it. Every server and worker task sharing the database needs the same value, and data encrypted with it cannot be read with another key.

### Roll Out a Release

1. Take a database snapshot.
2. Update the image tag and `AGENT_JOB_TYPE_VERSION` of the server, worker and agent services.
3. Deploy the server first. It applies the release's database updates when it starts; workers and agents follow once it is healthy.

See [Upgrades](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/upgrades) for what happens during an upgrade and how to roll back.

### Next steps

* [First Start](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/first-start): apply the licence and sign in.
* [Upgrades](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/upgrades): back up, upgrade and roll back.
* [Agents](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/administration/global-settings/agents): check that agents are connected and add more.
