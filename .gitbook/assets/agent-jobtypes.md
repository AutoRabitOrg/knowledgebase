# Agent Job Types

{% hint style="warning" %}

* Each Agent is capable of running/handling multiple job types. For example - Scanning Anypoint Runtime Applications, Performing health ckecks for configured endpoints

{% endhint %}

The status of each **`Job Type`** supported by the Agent can administered by following the below steps -

1. Navigate to **`Global Settings`** -> **`Agents`**
   ![agents](../images/agents.png) 
2. Expand the details by clicking on the **`Plus`** icon 
   ![agent_jobtypes](../images/agent_jobtypes.png) 
3. Each Job Type can have different status assosiated with it -
   1. **`RUNNING`** - Running without any issues
   2. **`INVALID CREDENTIALS`** - Running, but with missing configurations. Eg: Client Id and Secret for a specific job type is not configured
   3. **`STOPPED`** - Not Running
4. The **`IS MASTER`** column indicates if the current instance is the **Master**
   1. **Master** instance is the once responsible for creating the jobs based on the configured schedules

## See Also

* [Creating an Agent](create-agent.md)
* [Updating an Agent](update-agent.md)
