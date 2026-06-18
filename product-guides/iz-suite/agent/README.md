# Agent

Every **`Agent`** has 2 main functionalities associated with it -

### As Schedulers

1. **`Agents`** are the main entities responsible for executing the job schedules.
2. Each agent can handle multiple job types. For example - Scanning Anypoint Runtime Applications, Performing health ckecks for configured endpoints
3. Multiple **`Agents`** can be started on different machines and one of the **`Agent`** will be chosen as a `master`

### As Workers

1. While Schedulers schedule the job at configured interval, workers execute the jobs
2. Workers can execute the jobs in parallel and it concurrency factor is determined by **`Total Workers`** parameter.
3. To view the workers status, navigate to **`Global Settings`** -> **`Agents`** and click on **`View Workers`**&#x20;
   1. **`Free`** status indicates that the worker is free and ready to pickup new job executions
   2. **`Executing`** status indicates that the worker is busy executing a job

### See Also

* Cloud Hosted Agent
* Self Hosted Agent
