# Mule Applications

{% hint style="warning" %}
* To start scanning the applications, a schedule has to be created to scan the applications deployed in Anypoint **`Runtime Manager`**
* To create a schedule follow the steps mentioned at [Configure Schedule](../azure-ai-services/schedule-configuration.md)
* All applications deployed in **`CLOUD HUB`** and **`CLOUD HUB 2.0`** targets will be scanned.
{% endhint %}

### Configuring Schedule

1. While configuring the schedule select `Anypoint Mule Runtime Analysis` job type
2. In the next step, select the required `Organizations` and `Environments`
3. Choose the appropriate schedule

### To view all the applications

1. Navigate to **`IZ Eye`** -> **`Mule Projects`**&#x20;
2. The **`Status`** column indicates whether the application is running in Anypoint Platform **`Runtime Manager`**
3. Summary details include -
   1. **`Target`** - Indicates the deployment target E.g. CloudHub or CloudHub 2.0
   2. **`Total Issues`** - Indicates total number of issues once the application is scanned
   3. **`App Size`** - Total size of the deployed artifact
   4. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues. [View Dashboard](../dashboard.md)
   2. **`View Issues`** - Detailed report of the issues with file names and line numbers. [View Issues](application-issues.md)
5. Click on the settings icon to view additional columns like total worker, worker size, domain, etc.&#x20;

### See Also

* [API Applications](api-applications.md)
* [Application Issues](application-issues.md)
* [Application Dashboard](application-dashboard.md)
