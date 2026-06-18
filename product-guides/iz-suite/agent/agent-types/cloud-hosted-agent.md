# Cloud-Hosted Agent

{% hint style="warning" %}
Cloud hosted agents can be used when you do not want -

* To install the pre-requisite softwares required by the agent (i.e. Java)
* To run the agent on your own machines or if you do not have any servers
* The Agent / Workers to download and scan applications on cloud
* A default cloud agent will be created at part of the initial setup
{% endhint %}

## Configure Cloud Hosted Agent

1. Navigate to **`Global Settings`** -> **`Job Types`**
2. Edit \<b>Anypoint Code Analysis Job\</b> and set the Client Id and Secret of the [Connect Apps](https://docs.mulesoft.com/access-management/connected-apps-overview) which should be used to connect with the Anypoint Platform
3. Once the settings are saved, the Cloud Agent will be able to connect with the Anypoint Platform and execute the configured schedules
4. Once the credentials are configured, navigate to **`Global Settings`** -> **`Agents`** , and make sure the agent status is **RUNNING**
5. Re-log in, and start configuring the schedules

### See Also

* [Agent Job Types](../agent-job-types.md)
* [Self-Hosted Agent](self-hosted-agent.md)
