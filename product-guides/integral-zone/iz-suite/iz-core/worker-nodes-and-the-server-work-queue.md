# Worker Nodes and the Server Work Queue

* Applies to IZ Suite Server **26.3.1** and later.
* A single-container installation (`FALCON_MODE=all`) needs no additional configuration: a worker runs inside the same container. This page is for administrators who want to scale background processing or understand how scheduled server tasks run

### Overview <a href="#overview" id="overview"></a>

Up to version 1.4.x, background server tasks such as notifications, archival and vulnerability matching ran as in-process schedulers on the IZ Suite server. From **26.3.1** these tasks are placed on a **server work queue** in the database and executed by **workers**:

1. One IZ Suite server node is elected **master**. On every schedule tick the master enqueues one work item per tenant for each background task.
2. **Workers** claim work items from the queue and run them. A worker can run inside a server container or in a dedicated worker container. Any number of workers can share the queue; an item is never claimed by two workers at once.
3. Every item records who claimed it, when it ran, its outcome and a full log transcript, visible under **`Audit`** → **`Scheduler Audit Logs`**.&#x20;



### Background Tasks Executed by Workers <a href="#background-tasks-executed-by-workers" id="background-tasks-executed-by-workers"></a>

| Handler                                      | Purpose                                                                                                                                                         | Frequency                                                                                   |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **`Allocate Agent Workers Handler`**         | Assigns pending job executions to free agent workers, round-robin across tenants. Tenants with an expired license are skipped.                                  | Every 10 seconds                                                                            |
| **`Notification Handler`**                   | Delivers pending Email, Slack and Web notifications.                                                                                                            | Every 15 seconds                                                                            |
| **`User Subscription Notification Handler`** | Matches new events to user subscriptions and creates the notifications to deliver.                                                                              | Every 30 seconds                                                                            |
| **`Health Check Category Status Handler`**   | Recomputes IZ Pulse category and status-page status and raises status-page notifications.                                                                       | Every 30 seconds                                                                            |
| **`Asset Deprecation Handler`**              | Re-evaluates IZ Lens deprecations against the latest scans when deprecation rules or scans changed.                                                             | Every 30 seconds                                                                            |
| **`Vulnerability Handler`**                  | Re-matches IZ Lens vulnerabilities against scanned dependencies when vulnerability data or scans changed.                                                       | Every 30 seconds                                                                            |
| **`Reset Stale Workers And Jobs Handler`**   | Resets agent workers and jobs that stopped reporting so their work can be re-dispatched.                                                                        | Every 5 minutes                                                                             |
| **`Maintenance Window Handler`**             | Opens and closes IZ Pulse maintenance windows and sends the related notifications.                                                                              | Hourly                                                                                      |
| **`Record Archival Handler`**                | Applies the **`Archival Policies`** setting. See [Records Archival](../../../iz-suite/iz-core/records-archival.md).                                             | Daily at 23:00 server time                                                                  |
| **`Seed Metadata Handler`**                  | Downloads the Integral Zone seed catalogue and applies new built-in rules, profiles, dashboards, vulnerabilities, deprecations, automation tasks and MCP tools. | Every 12 hours, at server start, and on demand from **`Global Settings`** → **`Seed Data`** |
| **`Compliance Validation Handler`**          | Recalculates IZ Compliance scores for tenants with the Compliance module.                                                                                       | 1st and 15th of each month at midnight                                                      |

If a task is still running when its next tick arrives, no second item is queued for that tenant. Work is therefore never duplicated by a slow run.



### Deployment Modes <a href="#deployment-modes" id="deployment-modes"></a>

The container image starts different components depending on **`FALCON_MODE`**:

| `FALCON_MODE` | Starts                                                   | Use                                                                           |
| ------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **`all`**     | Database migration, API, web UI (port 80) and one worker | Default. Single-container and small cluster installations.                    |
| **`api`**     | Database migration and API                               | Split deployments where the web UI is served by separate `web` containers.    |
| **`web`**     | Web UI only                                              | Split deployments.                                                            |
| **`worker`**  | One worker process only                                  | Dedicated background-processing node. Exposes no port and serves no requests. |

A worker container needs the same **`DATABASE_URL`** as the server containers, and the same `.env` values if you override any. It does not run database migrations, so start or upgrade the `all` or `api` container first; the API container refuses to start on a partially migrated schema and prints recovery instructions in its log.



### Worker Node Configuration <a href="#worker-node-configuration" id="worker-node-configuration"></a>

The behaviour of all workers is controlled by the global setting **`Worker Node Configuration`** on the **platform tenant**.

1. Navigate to **`Global Settings`** → **`Settings`**.
2. Search for **`Worker Node Configuration`** and click **`Edit`**.



| Key                                | Default | Description                                                                                                                                                                                                                                               |
| ---------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`WORKER_CONCURRENCY`**           | `10`    | Number of work items one worker process runs in parallel. Increase for throughput on large installations; decrease to reduce database load.                                                                                                               |
| **`WORKER_POLL_INTERVAL_MS`**      | `10000` | How long an idle worker waits before checking the queue again, in milliseconds.                                                                                                                                                                           |
| **`WORKER_CLAIM_TIMEOUT_SECONDS`** | `600`   | An item still marked **`Executing`** this long after it was claimed is considered abandoned (for example because the worker crashed) and is returned to **`Pending`**. Keep it longer than your slowest task, otherwise long-running tasks may run twice. |
| **`WORKER_RECLAIM_INTERVAL_MS`**   | `60000` | How often each worker checks for abandoned items, in milliseconds.                                                                                                                                                                                        |
| **`START_WORKERS_ON_MASTER`**      | `true`  | Whether worker loops are started inside server containers. Leave it at `true`. Setting it to `false` also prevents dedicated `worker` containers from starting their loops, and no background task runs.                                                  |

Changes to **`WORKER_CONCURRENCY`**, **`WORKER_POLL_INTERVAL_MS`** and the timeouts take effect when worker processes are restarted. Restart dedicated worker containers, and restart the server containers (or toggle **`START_WORKERS_ON_MASTER`** off, save, on, save) for in-process workers.



### Master Election <a href="#master-election" id="master-election"></a>



* Every server node (`all` or `api`) sends a heartbeat every 10 seconds. A node whose heartbeat is older than **`FALCON_SERVER_KEEP_ALIVE_SECONDS`** (default 25 seconds) is marked **`STOPPED`**.
* If the current master's heartbeat is stale, the next node to send a heartbeat becomes master. Election uses a database lock, so exactly one node is master at any time.
* Only the master enqueues work items and runs the bootstrap on start-up: applying data migrations, adding new built-in records to every tenant and queueing seed data.
* Workers do not take part in the election.

To see which node is master, open **`Audit`** → **`Server Audit Logs`** (platform tenant). The **`Is Master`** column shows `Yes` for the master, and **`View Execution Logs`** shows the election history of each node.



### Sizing Guidance <a href="#sizing-guidance" id="sizing-guidance"></a>

| Installation                                    | Recommendation                                                                                                                                                                                      |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single tenant, up to a few hundred applications | `FALCON_MODE=all`, defaults.                                                                                                                                                                        |
| Cluster of two or more server nodes             | Keep in-process workers on every node.                                                                                                                                                              |
| Multi-tenant platform with many tenants         | One or more dedicated `worker` containers per availability zone, `WORKER_CONCURRENCY` between 10 and 20, and `WORKER_CLAIM_TIMEOUT_SECONDS` raised if seed data or archival runs exceed 10 minutes. |

Note that agent job executions (scans, health checks, reports) are still executed by **agents**, not by server workers. Add agent workers to scale scanning; add server workers to scale notifications, archival and platform housekeeping. See [Agent](agent/).



