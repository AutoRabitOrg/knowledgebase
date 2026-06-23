# Apex Classes and Triggers

## Apex Applications

{% hint style="warning" %}
* Create Organization and Environment with appropriate external client app credentials - Configure External Client App
* To start scanning the applications, a schedule has to be created to scan the Classes and Triggers deployed in Salesforce Instance - Configure Code Scan Schedule
{% endhint %}

### To view all the applications

1. Navigate to **`IZ Eye`** -> **`Salesforce Apex`**. Overview includes -&#x20;
   1. **`Name`** - Name of the Apex Class or Trigger
   2. **`Organization`** - Organization to which the app belongs to
   3. **`Environment`** - Environment to which the app belongs to
2. Click on the **`Plus`** icon to view the details&#x20;
3. Summary details include -
   1. **`Total Issues`** - Indicates total number of issues once the application is scanned
   2. **`Status`** - Indicated the status of class / trigger in Salesforce
   3. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues with file names and line numbers.

### To view only Apex Classes or Triggers

1. To filter either Classes or Triggers locate the **`Source`** filter from the filtering options and choose the appropriate value -&#x20;
   1. **`Apex Class`** - To filter only Apex Classes
   2. **`Apex Trigger`** - To filter only Apex Triggers

### See Also

* Configure External Client App
* Configure Code Scan Schedule
