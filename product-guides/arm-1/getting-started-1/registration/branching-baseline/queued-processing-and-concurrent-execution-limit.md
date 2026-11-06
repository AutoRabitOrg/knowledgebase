# Queued Processing and Concurrent Execution Limit

**Product:** AutoRABIT ARM\
**Module:** Version Control – Branch Baseline\
**Availability:** Classic UI and New UI

### Overview

AutoRABIT ARM has enhanced the **Branch Baseline workflow** by introducing queued processing to improve application performance and prevent multiple baseline operations from running simultaneously.

With this enhancement, a maximum of **2 Branch Baseline operations can run concurrently per customer**. Any additional requests are automatically added to a queue and processed as execution slots become available.

### What's New?

#### 1. Concurrent Baseline Execution Limit

* Each customer(Org) can run up to **2 Branch Baseline operations simultaneously**.
* When two baselines are already running, additional requests are automatically placed in a queue.
* Queued requests start automatically when an execution slot becomes available.

#### 2. Queue Visibility and Management

* Users receive a **Queued** status when a baseline request is waiting for execution.
* Users can view their pending Branch Baseline requests in the queue.
* Queued requests can be cancelled before execution.
* Running baseline operations can also be cancelled.

#### 3. Automatic Queue Processing

* Queued requests are automatically picked up when execution capacity becomes available.
* Queue processing may take approximately **40–60 seconds** to start a pending request after a slot becomes available.
* Pending requests are retained during ARM restarts and resume processing afterward.

### How It Works

1. Navigate to **Version Control > Branch Baseline**.
2. Initiate a new Branch Baseline operation.
3. If fewer than two baselines are running for your account and execution capacity is available, the request can start processing.
4. If the concurrent execution limit has been reached, ARM places the request in the queue and displays a **Queued** message.
5. Users can monitor or cancel pending requests from the queue view.
6. ARM automatically starts queued requests as execution slots become available.

### Important Notes

* The default concurrent execution limit is **2 Branch Baselines per customer**.
* Additional requests are queued automatically; users do not need to resubmit them.
* Queued requests may take up to approximately one minute to begin processing after an execution slot becomes available.
* The concurrent execution limit can be adjusted through configuration when required.
* Existing restrictions on running duplicate baselines for the same repository and branch remain unchanged.
* This enhancement does not change the baseline content, metadata retrieval, or resulting branch configuration.
* The functionality is available in both **Classic UI and New UI**, subject to feature enablement.

### Benefits

* **Improved System Performance:** Prevents excessive simultaneous baseline operations.
* **Automatic Queue Management:** Processes additional requests without manual intervention.
* **Better Visibility:** Allows users to monitor and cancel queued baseline requests.
* **Improved Reliability:** Retains pending requests during system restarts.
* **Consistent Experience:** Provides the same queued processing behavior across Classic and New UI.
