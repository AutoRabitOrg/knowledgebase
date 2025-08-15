# Data Loader Pro

**Data Loader Pro** is an advanced ARM capability that enables seamless transfer of data from a source sandbox to a destination sandbox. It automatically manages parent-child relationships, ensuring data integrity across related Salesforce objects. With support for multi-object hierarchies, Data Loader Pro simplifies the migration of complex Salesforce datasets, making the process faster, more reliable, and less prone to manual errors.

### Prerequisites for Data Loader Pro

When running **Data Loader Pro** on objects for the first time, ensure that **Data Loader Configuration** is completed between the same orgs for all objects included in the job. This configuration is a one-time requirement.

Data Loader Pro plays a crucial role in migrating data from a source sandbox to a destination sandbox. However, during this migration process, there is always a risk of creating duplicate records. To address this, ARM provides a synchronization feature that leverages the **ARM External ID** field (`AutorabitExtid__c`) to match and align records between orgs, helping prevent duplication.

#### &#x20;Step-By-Step Guide:

1. Log in to ARM application
2. Click on the PRO option in the left side navigation
3.  Open **Dataloader ▸ Pro** and click **Create new job**.

    <figure><img src="../../../../.gitbook/assets/1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
4.  In **Create Dataloader Job – Login and select object**, choose the **Source Org** and **Destination Org** from the dropdowns.\


    <figure><img src="../../../../.gitbook/assets/2 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
5.  Click **Login and fetch objects** to authenticate and load available objects from the source org.

    <figure><img src="../../../../.gitbook/assets/3 - DL PRO.png" alt=""><figcaption></figcaption></figure>
6.  Use the search box to filter objects, select the required object (radio button), then click **Next** to proceed.

    <figure><img src="../../../../.gitbook/assets/4 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
7. Open **Schema** and click the **Filters** icon
8.  In the **Master Object** tab, locate your object and select the funnel icon in the **Filters** column.

    <figure><img src="../../../../.gitbook/assets/5 - DL PRO.png" alt=""><figcaption></figcaption></figure>
9.  Configure the filter rule

    -In **Filter**, keep **Insert Value** (or switch as needed).

    <figure><img src="../../../../.gitbook/assets/6 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    Pick the field in **Select Field** (e.g., `nFORCE__Look_Up_Key__c`).

    <figure><img src="../../../../.gitbook/assets/7 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    Choose the **Operator** (e.g., **Is not empty**) and enter a **Value** if the operator requires one.
10. (Optional) Build complex logic\
    – Use **+** to add more conditions, the **OR** button for alternate clauses, and the refresh icon to reset.

    <figure><img src="../../../../.gitbook/assets/7.1 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>

    – Click **Validate** to check the rule and see an estimated record count. _(Success toast confirms the count.)_

    <figure><img src="../../../../.gitbook/assets/8 - DL PRO.png" alt=""><figcaption></figcaption></figure>
11. Apply the filter\
    – Click **Apply** to save the rule to the object.

    <figure><img src="../../../../.gitbook/assets/9 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>

    – A success message will be displayed on the screen, on clicking the "Apply" button.

    <figure><img src="../../../../.gitbook/assets/10 - DL PRO.png" alt=""><figcaption></figcaption></figure>
12. **Open Filters and choose CSV input**

    – In **Schema → Master Object**, click the **Filters** icon for the object.

    <figure><img src="../../../../.gitbook/assets/11 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    – Pick the **Select Field** (e.g., `Id`) and **Select Operator** (e.g., **Equals**).

    <figure><img src="../../../../.gitbook/assets/12 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    – In the **Filter** dialog, select **Upload CSV File** (Input Options).

    1. From **Select Field**, choose a field (e.g., `nFORCE__Look_Up_Key__c`). Select an operator.

    <figure><img src="../../../../.gitbook/assets/13 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    – Click **Upload File**.
13. **Confirm the upload**

    1. After the CSV uploads, a success message will be displayed.

    <figure><img src="../../../../.gitbook/assets/13 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
14. **Auto-generate the filter**

    1. Click **Auto Populate** to build the SOQL filter from the uploaded CSV values.

    <figure><img src="../../../../.gitbook/assets/14 - DL PRO.png" alt=""><figcaption></figcaption></figure>
15. &#x20;**Validate and apply**

    1. Review the generated query in the editor (e.g., `… WHERE nFORCE__Look_Up_Key__c IN ('…')`).

    <figure><img src="../../../../.gitbook/assets/15 - DL PRO (3).png" alt=""><figcaption></figcaption></figure>
16. Click **Validate** to preview the fetch count, then click **Apply**.

    <figure><img src="../../../../.gitbook/assets/16 - DL PRO (3).png" alt=""><figcaption></figcaption></figure>
17. Back on **Schema**, verify the green **Success** toast and the active **Filters** icon.

    <figure><img src="../../../../.gitbook/assets/17 - DL PRO.png" alt=""><figcaption></figcaption></figure>
18. **Configure field mappings**

    1. Click the **Mappings** icon for the same object.

    <figure><img src="../../../../.gitbook/assets/18 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    1. In **Create Mapping**, use **Auto Map** to map identical field names or **Clear Mapping** to reset.

    <figure><img src="../../../../.gitbook/assets/18 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>

    1. Click "Clear" to clear the mappings

    <figure><img src="../../../../.gitbook/assets/19.1 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>

    1. Click on "Automap" to map the similar fields

    <figure><img src="../../../../.gitbook/assets/20 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    1. Review and adjust any mappings as needed, then click **Save**.

    <figure><img src="../../../../.gitbook/assets/20 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
19. Click on the "Filters" and "Mappings" icons to open the respective windows on the "Ancestor Objects" section.

    <figure><img src="../../../../.gitbook/assets/21 - DL PRO.png" alt=""><figcaption></figcaption></figure>
20. Click on "Skip Records" to make sure the records from these objects were skipped from processing.

    <figure><img src="../../../../.gitbook/assets/22 - DL PRO.png" alt=""><figcaption></figcaption></figure>
21. **Select child object & open mappings**\
    In **Schema → Child Objects**, search and select the required child object (e.g., **ContentVersion**), then click the **Mappings** icon.

    <figure><img src="../../../../.gitbook/assets/23 - DL PRO.png" alt=""><figcaption></figcaption></figure>
22. **Map fields**\
    In **Create Mapping**, review source ↔ destination pairs.

    * Click **Auto Map** to map identical field names automatically.
    * Click **Clear Mapping** to reset if needed.\
      Finish by clicking **Save**.

    <figure><img src="../../../../.gitbook/assets/24 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
23. **Open Masking**\
    Go to the **Masking** step and click **New** to add a masking rule.

    <figure><img src="../../../../.gitbook/assets/25 - DL PRO.png" alt=""><figcaption></figcaption></figure>
24. **Choose object & field type**\
    In **Create Masking Rule**, pick the **Object** (e.g., `nFORCE__Brand__c`) and **Field Type** (Text/Textarea). Provide a **Masking value** when required.

    <figure><img src="../../../../.gitbook/assets/26 - DL PRO.png" alt=""><figcaption></figcaption></figure>
25. **Select masking style**\
    Choose a **Masking style**: **Prefix**, **Suffix**, **Replace**, **Shuffle**, or **Generate Random**.

    <figure><img src="../../../../.gitbook/assets/27 - DL PRO.png" alt=""><figcaption></figcaption></figure>
26. **Select target fields & save**\
    Select the fields the rule should apply to (e.g., **Name**, lookup keys) and click **Save**. _(img 28)_

    <figure><img src="../../../../.gitbook/assets/28 - DL PRO.png" alt=""><figcaption></figcaption></figure>
27. **Review rule in list**\
    The rule appears in the **Masking** grid with its value and style. Click the actions menu to **View Rule** or **Edit Rule**. _(img 29)_

    <figure><img src="../../../../.gitbook/assets/29 - DL PRO.png" alt=""><figcaption></figcaption></figure>
28. **View rule details**\
    Use **View Rule** to see the full configuration: rule name, object, type, masking value/style, timestamps, and the fields impacted.

    <figure><img src="../../../../.gitbook/assets/30 - DL PRO.png" alt=""><figcaption></figcaption></figure>
29. **Edit if needed**\
    Choose **Edit Rule** from the actions menu to adjust the object, style, value, or field selection, then **Save**. _(img 31)_

    <figure><img src="../../../../.gitbook/assets/30.1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
30. Observe the rule created for masking.

    <figure><img src="../../../../.gitbook/assets/31 - DL PRO.png" alt=""><figcaption></figcaption></figure>
31. Click "Delete" to delete the rule created

    <figure><img src="../../../../.gitbook/assets/32 - DL PRO.png" alt=""><figcaption></figcaption></figure>
32. Observe the rule deleted

    <figure><img src="../../../../.gitbook/assets/33 - DL PRO.png" alt=""><figcaption></figcaption></figure>
33. Open the Schedule step

    * The page defaults to **No Schedule**. This runs the job only when triggered manually. Click **Next** to continue without a schedule. _(35)_

    <figure><img src="../../../../.gitbook/assets/35 - DL PRO.png" alt=""><figcaption></figcaption></figure>
34. Set a Daily schedule _(36)_

    * Click **Daily**.
    * Choose **Scheduling Starts From** (start date).
    * Under **Repeats**, pick one:
      * **On specific time** and set the time, or
      * **At fixed interval of every** _N_ hours and select the starting hour.
    * Under **Scheduling Ends**, choose **Never**, **X Occurrences from creation**, or a specific end date.

    <figure><img src="../../../../.gitbook/assets/36 - DL PRO.png" alt=""><figcaption></figcaption></figure>
35. Set a Weekly schedule _(37)_

    * Click **Weekly**.
    * Choose **Scheduling Starts From** (start date).
    * Select one or more days (Sun–Sat).
    * Set **On Specific Time**.
    * Choose when the schedule ends: **Never**, **X Occurrences from creation**, or a specific end date.

    <figure><img src="../../../../.gitbook/assets/37 - DL PRO.png" alt=""><figcaption></figcaption></figure>
36. Continue
    * Review the summary banner at the top (it describes the schedule in plain text).
    * Click **Next** to move to **Job Configuration**.
37.





































### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

While performing **Data Loader Pro** on the objects for the first time, ensure you perform [Data Loader Configuration](../../../arm/arm-features/dataloader/dataloader-configuration.md) among the same orgs on all the objects included in your Data Loader Pro job. This is a one-time operation.

Data Loader plays an essential role in data migration from source sandbox to destination sandbox. However, in this data migration process, the chances of duplicate records being created always exist. To avoid this, ARM has developed a new feature that allows synchronizing between the orgs with the help of the ARM external ID **AutorabitExtid\_\_c** field.

### How to Perform a Data Loader Pro Operation <a href="#how-to-perform-a-dataloader-pro-operation" id="how-to-perform-a-dataloader-pro-operation"></a>

1. Log in to your ARM account.
2. Hover your mouse over the **`Data Loader`** module and select **`Data Loader Pro`**.
3. Click on **`Create New Job.`**

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, choose the **`Source Org`** and the **`Destination Org`** that automatically populate the selected sandbox's details.
5. Click **`Login and Fetch Objects`**.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Next, **`Select Master Object`**.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="353"><figcaption></figcaption></figure>

7. View the relationship between child objects/ancestor objects and the master object in the **`Schema (Grid View)`** section.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Change the grid view to a graph view by clicking the **`Switch to Graph View`** button. Click on the![](<../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>) icon to view the graphical representation on full screen.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Filters and Mappings <a href="#filters-and-mappings" id="filters-and-mappings"></a>

For each object displayed, users can view the list of fields related to the corresponding object.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Filters**

You can extract records within a specified limit using specifying criteria in the **`Filters`** section. You can even filter the details via **`Date`** or **`Date Literals`**. A date literal is a fixed expression representing a relative range of time, such as last month, this week, or next year. (Refer [here](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm) for the list of data literals supported).

Upload the **`CSV`** file (if required) if there is a large amount of data and it requires the filter for those records. The max file size supported is **10 MB**. Once the CSV is uploaded, click **`Auto-Populate`**. The filters are autopopulated for the selected field and operator based on the values of the chosen field in the uploaded CSV file.

Format for CSV file to filter records:

* ARM Data Loader Pro accepts CSV (comma-separated values) files. Use a spreadsheet program such as Microsoft Excel to create your CSV file.
* Ensure you have a column header and rows of data populated for all system-required fields, such as **`Account Name`** or **`Contact Last Name`**.
* There can be only one column header.&#x20;

For more information, see [Preparing the CSV file for Data Loader](../../../arm/arm-features/dataloader/preparing-the-csv-file-for-arm-dataloader.md).

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

The **`Record Count Limit`** box limits the number of records extracted from the source, giving a value in this field.

Click **`Validate`** to fetch the number of records transferred from the source sandbox to the destination sandbox. Finally, click **`Apply`**.

### Skip Records

‘Skip Records’ can be enabled by entering a ‘0’ on the record count section under the filters or by selecting the ‘checkbox’ under the ‘Skip Records’ section.

To ‘Skip Records' using the filters, click on 'Filters.' ‘Skip Records’ will omit migrating an object to the destination.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Enter ‘0’ on the ‘Record Count’ field of the ‘Apply Filters’ page pop-up and click on ‘Validate’ to validate the query.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Upon completing the validation, click on ‘Apply’ to apply the inputs.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Select the checkbox to 'Skip Records' from migrating to the destination.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;Upon selecting the checkbox, a pop-up will ask for confirmation.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Upon confirming, the checkbox will be selected to skip migrating those records to the destination with the following notification on filters applied.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Click on the filters section of the object on which the 'Skip Records' is applied to observe the query builder and the Record Count.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

When ‘Skip Records’ is selected, the record count is set to ‘0’ and the records from the selected object will not be migrated to the destination.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

When unchecking the ‘checkbox’, skip records will be disabled on the object. The following message will ask for confirmation.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Upon clicking 'confirm,' the records from that particular object will be migrated to the destination. The following notification will be displayed when unchecking the checkbox.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

When ‘Skip Records’ is disabled, the record count that was set to ‘0’ in the filters and the query will be reset to blank and the records will be migrated to the destination.

### **Mappings**

Map the object fields between the source and destination sandboxes.

Using the **`Automap`** feature, you can map the fields automatically based on fetched object fields with destination fields. To set up manual mappings, automapping needs to be disabled. Click on **`Clear Mappings`** to remove the automapping and set up the desired manual mappings.

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt=""><figcaption><p>Edit Mappings - Auto-Map</p></figcaption></figure>

### **Field Extraction**

Data Loader Pro allows users to fetch only the fields explicitly mapped by the user, rather than retrieving all available fields in an object.&#x20;

* When checking for the existence of `AutorabitExtId__c`, if it exists, the system verifies whether it is marked as "External Id" and "Unique." If not, it is set to `true` as required.
* Any new objects are saved to the database, reducing processing time.

### **External ID Field Mapping**

In this section, you can use an external ID instead of a related record's Salesforce record ID to relate or associate records to each other as you process the Data Loader Pro operation. For example, if Object B has a lookup field to another Object A, you can use the values in a field marked as an **`External ID`** on Object A to relate the two (Object B to Object A records).

In the **`Source`** field, select the source whose values will be populated in the destination external ID field.

In the **`Destination`** field, select the required destination org whose values will remain unique for all the records.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** ARM does not support the automatic creation of an ExternalUniqueID. The user has to create this manually on both the Source Org and Destination Org.
{% endhint %}

### Process Details <a href="#process-details" id="process-details"></a>

Here in this section, fill in the process details listed below:&#x20;

1. Enter a **`Name`**  for the job.
2. Select the category in the **`Job Group`** field. This is important if you'd like to group related jobs into a single category. You can also create a new group and assign your job to this group.
3. **`Master Object`** and **`External ID`** are auto-populated.
4. Enter the **`User Name Suffix`** for the **`Source Org`** and the **`Destination Org`**. Below are some examples of usernames and the corresponding suffixes:

| Case 1      | User Name                                       | User Name Suffix |
| ----------- | ----------------------------------------------- | ---------------- |
| Source      | [jsmith@ar.com.src](mailto:jsmith@ar.com.src)   | src              |
| Destination | [jsmith@ar.com.dest](mailto:jsmith@ar.com.dest) | <p>dest<br></p>  |

| Case 2      | User Name                                     | User Name Suffix |
| ----------- | --------------------------------------------- | ---------------- |
| Source      | [jsmith@ar.qan.com](mailto:jsmith@ar.qan.com) | qan.com          |
| Destination | [jsmith@ar.aws.com](mailto:jsmith@ar.aws.com) | aws.com          |

| Case 3      | User Name                                       | User Name Suffix       |
| ----------- | ----------------------------------------------- | ---------------------- |
| Source      | [jsmith@ar.com](mailto:jsmith@ar.com)           | Empty (leave it blank) |
| Destination | [jsmith@ar.com.dest](mailto:jsmith@ar.com.dest) | dest                   |

| Case 4      | User Name                                     | User Name Suffix       |
| ----------- | --------------------------------------------- | ---------------------- |
| Source      | [jsmith@ar.com.src](mailto:jsmith@ar.com.src) | src                    |
| Destination | [jsmith@ar.com](mailto:jsmith@ar.com)         | Empty (leave it blank) |

5. Additionally, users can ignore certain records related to community users by selecting the **`Ignore Community Users`** checkbox.

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Masking Wizard <a href="#masking-wizard" id="masking-wizard"></a>

Data masking refers to changing certain data elements within a data store so the structure remains similar while the information is altered to protect sensitive information. It ensures sensitive customer information is unavailable beyond the permitted production environment.

Under the **`Masking Wizard`** section, click on **`New`** to add a masking rule.

<figure><img src="../../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

In the **`Masking Form`** screen, do the following:

<figure><img src="../../../../.gitbook/assets/image (19) (1).png" alt="" width="426"><figcaption></figcaption></figure>

1. **`Select Object`** for masking and choose the **`Field Type`**.
2. Choose the **`Masking Style`**:
   * **`Prefix`**: This option adds the character before the selected field name. For example, if the field value in source org is ABC, and the prefix masking value is kept as 123, then the final field value being deployed will be 123.ABC.
   * **`Suffix`**: This option adds the character after the selected field name. For example, if the field value in source org is ABC, and the suffix masking value is kept as 123, then the final field value being deployed will be ABC.123.
   * **`Replace`**: This option replaces the selected field name with the character you enter in the **`Masking Value`** field. For example, if the field value in source org is ABC, and the replace masking value is kept as 123, then the final field value being deployed will be 123.
   * **`Shuffle`**: Shuffles the data in the column (like a deck of cards) and leaves the other columns untouched. For example, if the field value in source org is ABCDE, then the final field value being deployed will be DCBEA.
   * **`Generate Random`**: This option helps mask the original value with a random value within a specified range. For example, if the field value in source org is ABC, and the random string length value is set to 7, then the deployed field value would be similar to 15d3aRG.

{% hint style="info" %}
**Important Note:** Masking is not applicable if the field value for the record is empty.
{% endhint %}

#### Process Schedule <a href="#process-schedule" id="process-schedule"></a>

In the Scheduling procedure, the user can schedule the process it must run.

1. **`Daily:`** The process will run every day at the scheduled or set time interval.
2. **`Weekly:`** The process will run weekly on the scheduled day and time.
3. **`No schedule:`** The process is only saved; you can run it when required.

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

Finally, click on **`Save`** to complete the initial process. You will be redirected to the **`Dataloader Pro Summary`** page, where the Data Loader process initiated can be seen at the top of the list.

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

### Job Configuration Settings

1. This feature will allow the user to select the required job settings to disable workflow rules, disable validation rules etc., as required during the job creation.

<figure><img src="../../../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

2. Once the job is saved the selected job configuration settings will be saved.
3. On running the job, the retained job settings will be displayed on the pop-up, “Run Configuration”.

<figure><img src="../../../../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

4. Any changes made during the run of the job will only affect that individual job run.
5. To permanently change the configured settings during the job creation, the user has to edit the created job and change the settings and save the job.

### Running the Data Loader Pro Job

Select your job from the **`Data Loader Pro Summary`** screen and click on **`Run`**. This option allows you to run the processes created in the selected category.

<figure><img src="../../../../.gitbook/assets/image (24) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (25) (1).png" alt="" width="533"><figcaption></figcaption></figure>

The table below lists the configurations to choose from, along with their descriptions:

| Serial Number | Configurations                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1             | **`Disable workflows`**                                                    | The workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                   |
| 2             | **`Disable validation rules`**                                             | Validation rules verify that the data a user enters in a record meets the criteria you specify before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                               |
| 3             | **`Use Bulk API`**                                                         | <p>The Bulk API is based on REST principles and optimized for inserting, updating, and deleting large data sets.</p><p>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. </p><p><strong>Note</strong>: When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing your overall run better data throughput.</p> |
| 4             | **`Insert/update with null values`**                                       | Insert/update with null values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 5             | **`Minimize multiple references between the same objects`**                | When there are multiple references between the same objects, unnecessary API calls are not triggered upon selecting this option.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 6             | **`Automatically apply master object filter on other dependency objects`** | All objects in the hierarchy are calculated based on the Master Object filters; this option avoids extra records addition due to self-references and multiple references.                                                                                                                                                                                                                                                                                                                                                                                     |
| 7             | **`Data encryption for data files`**                                       | Data encryption for data files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 8             | **`Incremental data migration`**                                           | After a data-loading process is done, only the newly added records are transferred into the destination sandbox.                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### More Options <a href="#more-options" id="more-options"></a>

1. **`Edit:`** Edits the processes in the selected category to rerun them.
2. **`Abort:`** Aborts the process.
3. **`Schedule:`** Schedules the data-loading process for the selected category.
4. **`Clone:`** Clones the respective Data Loader Pro job.
5. **`Log:`** Provides information about the process execution.

<figure><img src="../../../../.gitbook/assets/image (26) (1).png" alt=""><figcaption></figcaption></figure>

#### Schema (Grid View) <a href="#schema-grid-view" id="schema-grid-view"></a>

This section lets you view the master object and its related information for the test environment setup job. For the setup run with disabled validation/workflow rules, ARM lists all the validation rules set under **`VR/WFR`** section. The UI lists all the workflow/validation rules; users must enable them for the disabled rules (if required).

<figure><img src="../../../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>
