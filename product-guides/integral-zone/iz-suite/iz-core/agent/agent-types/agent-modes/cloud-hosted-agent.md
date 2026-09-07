# Cloud-Hosted Agent

{% hint style="warning" %}
Cloud hosted agents can be used when you do not want -

* To install the pre-requisite software required by the agent (i.e. Java)
* To run the agent on your own machines or if you do not have any servers
* The Agent / Workers to download and scan applications on cloud
* A default cloud agent will be created at part of the initial setup
{% endhint %}

## Configure Cloud Hosted Agent



1. Navigate to **`Global Settings`** -> **`Job Types`**
2. Edit **Anypoint Code Analysis Job** and set the Client Id and Secret of the [Connect Apps](https://docs.mulesoft.com/access-management/connected-apps-overview) which should be used to connect with the Anypoint Platform
3. Once the settings are saved, the Cloud Agent will be able to connect with the Anypoint Platform and execute the configured schedules
4. Once the credentials are configured, navigate to **`Global Settings`** -> **`Agents`** , and make sure the agent status is **RUNNING**
5. Re-log in, and start configuring the schedules

### Scaling Cloud Hosted Agents <a href="#scaling-cloud-hosted-agents" id="scaling-cloud-hosted-agents"></a>

Cloud agents that are started by a container platform can register themselves instead of being created in advance. Set **`AGENT_WRAPPER_SECRET`** on the IZ Server and start each agent with `--agentWrapperSecret` and an optional `--deploymentInstanceId`. Each new instance either reuses a stopped agent or is created as a new cloud-hosted agent with **`Default Workers Count`** workers.&#x20;

### See Also

* [Agent Job Types](../../agent-job-types.md)
* [Self-Hosted Agent](self-hosted-agent.md)
