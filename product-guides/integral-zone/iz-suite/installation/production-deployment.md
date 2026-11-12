---
description: >-
  The recommended production setup for IZ Suite on your own cloud account, with
  load-balanced servers, scaling workers and a managed database.
---

# Production Deployment

In production, run the IZ Suite components as separate services on a managed container platform, with a managed PostgreSQL database. This removes the single VM as a point of failure, lets the busy parts scale on their own and keeps backups out of your hands.

The setup below is the one AutoRABIT runs, described for Amazon Web Services.

## Recommended Layout

| Part                  | AWS service                                                               | Recommended setting                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Load balancer and TLS | Application Load Balancer with a certificate from AWS Certificate Manager | HTTPS on 443, HTTP redirected to HTTPS. Health check `GET /api/graphql/health`.                                                                    |
| Web firewall          | AWS WAF on the load balancer                                              | AWS managed rule sets.                                                                                                                             |
| Server                | ECS on Fargate, `iz-suite-server`, `FALCON_MODE=api`                      | At least **2 tasks**, in two Availability Zones.                                                                                                   |
| Worker                | ECS on Fargate, `iz-suite-server`, `FALCON_MODE=worker`                   | 1 task or more, scaling out with the load.                                                                                                         |
| Agent                 | ECS on Fargate, `iz-suite-agent`                                          | 1 task; add tasks for more scanning or monitoring capacity.                                                                                        |
| Database              | Amazon RDS for PostgreSQL 16                                              | Multi-AZ, storage encryption on, automated backups, an instance class sized by AutoRABIT.                                                          |
| Secrets               | AWS Secrets Manager                                                       | `DATABASE_URL`, `SECRETS_ENCRYPTION_KEY`, `AGENT_WRAPPER_SECRET`, `SESSION_JWT_PRIVATE_KEY` and `SESSION_JWT_PUBLIC_KEY`, injected into the tasks. |
| Logs and alarms       | Amazon CloudWatch                                                         | Container logs, and alarms on load balancer and target 5xx errors, no healthy targets, and database CPU and free storage.                          |

AutoRABIT sizes the tasks and the database with you; see [Requirements & Sizing](requirements-and-sizing.md).

{% hint style="info" %}
Run the database in private subnets, reachable only from the server and worker tasks. The agent reaches IZ Suite through the load balancer or the internal service address and never needs the database.
{% endhint %}

## Configuration

Every server and worker task uses the same values:

| Variable                                            | Required          | Description                                                                                                                                              |
| --------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DATABASE_URL`                                      | Yes               | `postgres://<user>:<password>@<host>:5432/<database>?sslmode=require`                                                                                    |
| `FALCON_MODE`                                       | Yes               | `api` for the server, `worker` for the worker.                                                                                                           |
| `SECRETS_ENCRYPTION_KEY`                            | Yes               | 64 hexadecimal characters, for example from `openssl rand -hex 32`. Encrypts stored credentials and secure settings.                                     |
| `AGENT_JOB_TYPE_VERSION`                            | Yes               | The agent and job-type version, normally the release, for example `26.4.2`. Set it on the server and the worker; the server refuses to start without it. |
| `AGENT_WRAPPER_SECRET`                              | Yes on the server | Shared secret that agents present when they register themselves.                                                                                         |
| `SESSION_JWT_PRIVATE_KEY`, `SESSION_JWT_PUBLIC_KEY` | Yes               | Base64-encoded PEM RSA key pair that signs sign-in sessions, set on the server and the worker. Replacing it signs everyone out.                          |
| `LOG_LEVEL`                                         | No                | `trace`, `debug`, `info`, `warn` (default), `error`, `fatal` or `silent`.                                                                                |

The agent needs:

| Variable               | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `FALCON_AGENT_OPTS`    | `--serviceUrl <IZ Suite address>`, for example `--serviceUrl https://izsuite.yourcompany.com`. |
| `AGENT_WRAPPER_SECRET` | The same value as on the server.                                                               |

{% hint style="danger" %}
Set `SECRETS_ENCRYPTION_KEY` once and never change it. Every server and worker task sharing the database needs the same value, and data encrypted with it cannot be read with another key.
{% endhint %}

## Roll Out a Release

1. Take a database snapshot.
2. Update the image tag of the server, worker and agent services, and `AGENT_JOB_TYPE_VERSION` of the server and worker.
3. Stop the old server tasks, then start the new server. A new server stops while a server of another release is still running, and it applies the release's database updates when it starts. Start the workers and agents once it is healthy.

See [Upgrades](upgrades.md) for what happens during an upgrade and how to roll back.

## Next Steps

* [First Start](first-start.md): apply the licence and sign in.
* [Upgrades](upgrades.md): back up, upgrade and roll back.
* [Agents](../administration/global-settings/agents.md): check that agents are connected and add more.
