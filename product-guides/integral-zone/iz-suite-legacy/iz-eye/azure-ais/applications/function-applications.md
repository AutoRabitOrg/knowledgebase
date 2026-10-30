---
description: Azure Function Apps
---

# Function Applications



{% hint style="warning" %}
* To start scanning the applications, a schedule has to be created to scan the deployed API Management Instances - [Configure Code Scan Schedules](../../anypoint-platform/code-scan-schedule-configuration.md)
{% endhint %}

### What Is Scanned



For every Function App discovered in the selected resource groups, the **`Azure Function App Analysis`** job reads the following documents and evaluates them against the active **Function App** quality profile:

| File reported in issues        | Description                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------- |
| `function-app-definition.json` | The Function App resource: runtime, HTTPS, identity, networking and other site properties   |
| `function-app-web-config.json` | The site configuration: TLS version, FTP state, CORS, remote debugging and similar settings |
| `functions.json`               | The functions of the app and their bindings                                                 |

When the app's runtime is **Python** and IZ Suite can read the app's host keys, the deployed code is also downloaded and scanned with the Python rules, so the same scan reports configuration and code issues.

* Function Apps on other runtimes (.NET, Node.js, Java, PowerShell) are configuration-scanned only. Java Function Apps deploy compiled bytecode; scan Java from the source repository with IZ Scan instead.
* Logic App (Standard) sites are not listed here; they are listed under **`Azure Logic Apps`**.

#### To view all the Function Apps <a href="#to-view-all-the-function-apps" id="to-view-all-the-function-apps"></a>



1. Navigate to **`IZ Eye`** -> **`Azure`** -> **`Azure Function Apps`**. Overview includes -
   1. **`Name`** - Name of the Function App
   2. **`Organization`** - Subscription to which the Function App belongs to
   3. **`Environment`** - Resource Group to which the Function App belongs to
2. Click on the **`Plus`** icon to view the details
3. Summary details include -
   1. **`Total Issues`** - Indicates total number of issues once the application is scanned
   2. **`Status`** - State of the Function App in Azure, for example **`Running`**
   3. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues with file names and line numbers.

### See Also

* [App Registration](../app-registration.md)
* [Configure Code Scan Schedules](../../anypoint-platform/code-scan-schedule-configuration.md)
* [Logic Apps](logic-applications.md)
* [Function Apps](function-applications.md)
