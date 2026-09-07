# Scheduler Audit Logs

* **`Scheduler Audit Logs`** can only be accessed by users with the **`View System Audit Log`** permission.
* In a multi-tenant installation every tenant sees the work items of its own tenant.

**`Scheduler Audit Logs`** lists the background server tasks (work items) that were queued for your tenant, who executed them, their outcome and their full log. Use it to verify that notifications, archival, seed data, vulnerability matching and compliance recalculation are running, and to read the error when one of them fails. For the list of tasks and how they are executed see [Worker Nodes and the Server Work Queue](worker-nodes-and-the-server-work-queue.md).



1. Navigate to **`Audit`** → **`Scheduler Audit Logs`**.
2. Each row is one execution of one task:

| Column            | Description                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **`Handler Key`** | Name of the task, for example `Notification Handler` or `Seed Metadata Handler`.                                                    |
| **`Status`**      | **`Pending`**, **`Executing`**, **`Completed`** or **`Failed`**. See below.                                                         |
| **`Claimed By`**  | Identifier of the worker that executed the item: hostname of the container, process id and worker loop number. Empty while Pending. |
| **`Created`**     | When the item was queued.                                                                                                           |
| **`Run After`**   | Earliest time the item may be executed. Normally equal to Created.                                                                  |
| **`Finished At`** | When execution finished. Empty while Pending or Executing.                                                                          |
| **`Tenant ID`**   | Hidden by default. Enable it from the column settings when reviewing the platform tenant.                                           |

3. Use **`Search Handler Key`** to filter by task name, for example `Archival`.
4. Rows are sorted by **`Created`** descending, 10 per page. Click **`Reload`** to refresh; the **`Download`** action exports the current page.

#### Status Values <a href="#status-values" id="status-values"></a>

| Status          | Meaning                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`Pending`**   | Queued and waiting for a worker. Items normally stay Pending for a few seconds. A growing number of Pending items indicates that no worker is running or that workers are saturated. |
| **`Executing`** | A worker has claimed the item and is running it.                                                                                                                                     |
| **`Completed`** | The task finished successfully.                                                                                                                                                      |
| **`Failed`**    | The task raised an error. Open the execution log to read it. The task will run again at its next scheduled time.                                                                     |

An item that remains **`Executing`** longer than the configured claim timeout (10 minutes by default) is treated as abandoned, for example because the worker container was restarted, and is returned to **`Pending`** to be picked up by another worker.

#### Execution Log <a href="#execution-log" id="execution-log"></a>

1. Click the **`View Execution Logs`** action on a row.
2. The **`Execution Log`** dialog shows the transcript written by the task, one line per event with a timestamp and a level (`INFO`, `WARN`, `ERROR`).
3. The last line reads `Completed "<task>" in <duration>` or `Failed "<task>" in <duration>` followed by the error. Click the reload icon in the dialog to refresh the log of a task that is still executing. While a task has not written anything yet the dialog shows _"Execution log seems to be empty. Please wait for the job to complete"_.



#### Typical Checks <a href="#typical-checks" id="typical-checks"></a>

| Question                                     | What to look for                                                                                                                                   |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Are email or Slack notifications being sent? | `Notification Handler` items should complete every 15 seconds. A Failed item lists the deliveries that failed and why.                             |
| Did the nightly archival run?                | One `Record Archival Handler` item per day around 23:00 server time.                                                                               |
| Was new seed data applied after an upgrade?  | `Seed Metadata Handler` items after server start; the log lists each seed key and version applied or skipped.                                      |
| Why is a compliance percentage not changing? | `Compliance Validation Handler` log shows the old and new percentage per standard, or a warning that the Compliance license module is not enabled. |
| Are jobs waiting for agents?                 | `Allocate Agent Workers Handler` items should complete every 10 seconds; the log shows how many jobs were assigned.                                |

#### Related Screens <a href="#related-screens" id="related-screens"></a>

* **`Audit`** → **`Server Audit Logs`** (platform tenant only) lists the server nodes, which node is master and each node's start-up and election log.
* **`Schedules`** → **`Jobs`** lists **agent** job executions (scans, health checks, reports). Those are not shown in Scheduler Audit Logs.
* **`Global Settings`** → **`Seed Data`** (platform tenant only) triggers a `Seed Metadata Handler` run for every tenant.
