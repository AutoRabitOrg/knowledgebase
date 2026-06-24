# APIM Applications

## Azure API Management

{% hint style="warning" %}
* To start scanning the applications, a schedule has to be created to scan the deployed API Management Instances - [Configure Code Scan Schedules](../../code-scan-schedule-configuration.md)
{% endhint %}

### To view all the APIs

1.  Navigate to **`IZ Eye`** -> **`Azure API Management`**. Overview includes

    <figure><img src="../../../../../.gitbook/assets/azure_ais_apim_apps_1.png" alt=""><figcaption></figcaption></figure>

a. **`Name`** - Name of the API prefixed with Resource Group name

b. **`Organization`** - Subscription to which the API belongs to

c. **`Environment`** - Resource Group to which the API belongs to<br>

2.  Click on the **`Plus`** icon to view all the versions of the API <br>

    <figure><img src="../../../../../.gitbook/assets/azure_ais_apim_apps_2.png" alt=""><figcaption></figcaption></figure>
3. Summary details include -
   1. **`Total Issues`** - Indicates total number of issues once the application is scanned
   2. **`Status`** - Indicated the status of class / trigger in Salesforce
   3. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues with file names and line numbers.

### See Also

* [App Registration](../application-registration.md)
* [Configure Code Scan Schedules](../../../iz-pulse/about-iz-pulse/configure-schedule.md)
* [Logic Apps](logic-applications.md)
* [Function Apps](function-applications.md)
