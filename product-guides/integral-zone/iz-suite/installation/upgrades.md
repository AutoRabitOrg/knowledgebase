---
description: >-
  Back up, upgrade an IZ Suite installation to a newer release, and roll back if
  you need to.
---

# Upgrades

Upgrading replaces the containers with the new release. The database is kept: the new server applies the release's database updates when it starts.

{% hint style="warning" %}
Always back up the database before an upgrade, and keep the secrets (`SECRETS_ENCRYPTION_KEY` and the rest of your configuration) with the backup.
{% endhint %}

## How Upgrades Work

* **Database updates run on start-up.** They only add what the database does not have yet; they never reset or drop data.
* **A failed update stops the server.** If an update fails, the server stops. Restore the database backup or contact AutoRABIT support.
* **Upgrades only go forward.** The database records the release that last started on it, and an older server refuses to start on it. Going back to an earlier release needs the database backup.
* **Start the server first.** Workers and agents follow once the server is healthy. On the proof-of-concept setup, the start script does this for you.

## Upgrade a Proof of Concept Installation

From the installation folder:

```sh
cp .env .env.backup
docker compose exec -T postgres pg_dump -U izsuite -Fc izsuite > izsuite-before-upgrade.dump
./up.sh 26.4.2
docker compose logs -f iz-suite-server
```

When the logs show the new release and `docker compose ps` shows every service healthy, the upgrade is done.

To go back: stop the stack, put `.env.backup` back as `.env`, restore the dump and start the previous release:

```sh
docker compose up -d postgres
docker compose exec -T postgres pg_restore -U izsuite -d izsuite --clean --if-exists < izsuite-before-upgrade.dump
./up.sh <previous release>
```

## Upgrade a Production Deployment

1. Take a snapshot of the database.
2. Set the new image tag on the server, worker and agent services, and `AGENT_JOB_TYPE_VERSION` on the server and worker.
3. Stop the old server, deploy the new one and wait until it is healthy, then deploy the worker and the agents. A new server stops while a server of another release is still running.

To go back, restore the snapshot to a new database and deploy the previous release against it.

## Upgrading to 26.4.2

* Set **`AGENT_JOB_TYPE_VERSION`** (for example `26.4.2`) on every server and worker. The 26.4.2 server does not start without it. The proof-of-concept start script sets it for you.
* Set **`SESSION_JWT_PRIVATE_KEY`** and **`SESSION_JWT_PUBLIC_KEY`** (a base64-encoded PEM RSA key pair) on the server and worker, and **`AGENT_WRAPPER_SECRET`** on the server and every agent. The server and worker do not start without the session keys. The proof-of-concept start script creates them for you.
* Content such as rule packs, standards and starter dashboards is added after start-up. Your licence decides which of it is used.
* See the release notes for changes that affect existing data, such as quality gate results.

## Next Steps

* [Proof of Concept Installation](proof-of-concept-installation.md): the single-VM setup and its commands.
* [Production Deployment](production-deployment.md): the recommended production setup.
