# Agent

Every **`Agent`** has 2 main functionalities associated with it -

### As Schedulers

1. The **`IZ Server`** decides when each job schedule is due and places the schedule on a queue. **`Agents`** pick up due schedules from the queue and create the corresponding job executions.
2. Each agent can handle multiple job types. For example - Scanning Anypoint Runtime Applications, Performing health checks for configured endpoints
3. Multiple **`Agents`** can be started on different machines. Any agent that supports the job type can pick up a schedule, so no single agent is a point of failure. From IZ Suite 2.0.1 there is no longer a designated _master_ agent; scheduling is coordinated by the server.

#### As Workers <a href="#as-workers" id="as-workers"></a>

1. While the server schedules the jobs at the configured interval, workers execute the jobs
2. Workers can execute the jobs in parallel and its concurrency factor is determined by **`Total Workers`** parameter.
3. Pending job executions are allocated to free workers every 10 seconds. In a multi-tenant installation the allocation is fair across tenants: one tenant with a large backlog cannot prevent other tenants' jobs from running.
4. To view the workers status, navigate to **`Global Settings`** -> **`Agents`** and click on **`View Workers`**
   1. **`Free`** status indicates that the worker is free and ready to pickup new job executions
   2. **`Executing`** status indicates that the worker is busy executing a job

#### Default Number of Workers <a href="#default-number-of-workers" id="default-number-of-workers"></a>

New agents are created with the number of workers configured in **`Global Settings`** -> **`Settings`** -> **`Agent Settings`** -> **`Default Workers Count`** (12 by default). This applies to the cloud agent created when the license is applied and to agents that register themselves at start-up. The number of workers of an existing agent can be changed with the **`Edit`** action under **`Global Settings`** -> **`Agents`**.

### See Also

* [Cloud Hosted Agent](agent-types/agent-modes/cloud-hosted-agent.md)
* [Self Hosted Agent](agent-types/agent-modes/self-hosted-agent.md)
