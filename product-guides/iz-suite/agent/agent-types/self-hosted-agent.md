# Self Hosted Agent

{% hint style="warning" %}
Self hosted agents can be used when you do not want -

1. To share the Anypoint Connected App’s Client Id and Secret
2. The Agent / Workers to download and scan applications on cloud
{% endhint %}

### Configure Self Hosted Agent

1. Navigate to **`Global Settings`** -> **`Agents`** and click on **`Configure Agent`**
   1. Specify the agent name. For example: On-prem Agent
   2. Specify number of worker. For example, a value of 3 indicates that the agent can perform 3 parallel scans/jobs at a time.
   3. Specify tge Agent type as **`SELF HOSTED`**
   4. Select the Job Types handled by agent. If you are not sure, all the available job types can be selected
   5. Click on Submit
2. Once the agent is created, click on the **`Download Agent`** action and follow the instructions&#x20;
3. After starting the agent, make sure the agent status is **RUNNING**
4. Relogin, and start configuring the schedules

### See Also

* Cloud Hosted Agent
* Agent Job Types
