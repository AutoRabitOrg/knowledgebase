# DataLoader Pro

**DataLoader Pro** is an advanced ARM capability that enables seamless transfer of data from a source sandbox to a destination sandbox. It automatically manages parent-child relationships, ensuring data integrity across related Salesforce objects. With support for multi-object hierarchies, DataLoader Pro simplifies the migration of complex Salesforce datasets, making the process faster, more reliable, and less prone to manual errors.

### Prerequisites for DataLoader Pro

When running **DataLoader Pro** on objects for the first time, ensure that **DataLoader Configuration** is completed between the same orgs for all objects included in the job. This configuration is a one-time requirement.

DataLoader Pro plays a crucial role in migrating data from a source sandbox to a destination sandbox. However, during this migration process, there is always a risk of creating duplicate records. To address this, ARM provides a synchronization feature that leverages the **ARM External ID** field (`AutorabitExtid__c`) to match and align records between orgs, helping prevent duplication.

#### &#x20;Step-By-Step Guide:

1. Log in to ARM application
2. Click on the PRO option in the left side navigation
3.  Open **DataLoader ▸ Pro** and click **Create new job**.

    <figure><img src="../../../../.gitbook/assets/1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
4.  In **Create DataLoader Job – Login and select object**, choose the **Source Org** and **Destination Org** from the dropdowns.<br>

    <figure><img src="../../../../.gitbook/assets/2 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
5.  Click **Login and fetch objects** to authenticate and load available objects from the source org.

    <figure><img src="../../../../.gitbook/assets/3 - DL PRO.png" alt=""><figcaption></figcaption></figure>
6.  Use the search box to filter objects, select the required object (radio button), then click **Next** to proceed.

    <figure><img src="../../../../.gitbook/assets/4 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
7. Open **Schema** and click the **Filters** icon
8.  In the **Master Object** tab, locate your object and select the funnel icon in the **Filters** column.

    <figure><img src="../../../../.gitbook/assets/5 - DL PRO.png" alt=""><figcaption></figcaption></figure>
9.  Configure the filter rule:

    In **Filter**, keep **Insert Value** (or switch as needed).

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
13. Format for CSV file to filter records:

    * ARM Data Loader Pro accepts CSV (comma-separated values) files. Use a spreadsheet program such as Microsoft Excel to create your CSV file.
    * Ensure you have a column header and rows of data populated for all system-required fields, such as **`Account Name`** or **`Contact Last Name`**.
    * There can be only one column header.&#x20;

    For more information, see [Preparing the CSV file for Data Loader](../../../arm/arm-features/dataloader/preparing-the-csv-file-for-arm-dataloader.md).
14. **Confirm the upload**

    1. After the CSV uploads, a success message will be displayed.

    <figure><img src="../../../../.gitbook/assets/13 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
15. **Auto-generate the filter**

    1. Click **Auto Populate** to build the SOQL filter from the uploaded CSV values.

    <figure><img src="../../../../.gitbook/assets/14 - DL PRO.png" alt=""><figcaption></figcaption></figure>
16. &#x20;**Validate and apply**

    1. Review the generated query in the editor (e.g., `… WHERE nFORCE__Look_Up_Key__c IN ('…')`).

    <figure><img src="../../../../.gitbook/assets/15 - DL PRO (3).png" alt=""><figcaption></figcaption></figure>
17. Click **Validate** to preview the fetch count, then click **Apply**.

    <figure><img src="../../../../.gitbook/assets/16 - DL PRO (3).png" alt=""><figcaption></figcaption></figure>
18. Back on **Schema**, verify the green **Success** toast and the active **Filters** icon.

    <figure><img src="../../../../.gitbook/assets/17 - DL PRO.png" alt=""><figcaption></figcaption></figure>
19. **Configure field mappings**

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
20. Click on the "Filters" and "Mappings" icons to open the respective windows on the "Ancestor Objects" section.

    <figure><img src="../../../../.gitbook/assets/21 - DL PRO.png" alt=""><figcaption></figcaption></figure>
21. Click on "Skip Records" to make sure the records from these objects were skipped from processing.

    <figure><img src="../../../../.gitbook/assets/22 - DL PRO.png" alt=""><figcaption></figcaption></figure>
22. **Select child object & open mappings**\
    In **Schema → Child Objects**, search and select the required child object (e.g., **ContentVersion**), then click the **Mappings** icon.

    <figure><img src="../../../../.gitbook/assets/23 - DL PRO.png" alt=""><figcaption></figcaption></figure>
23. **Map fields**\
    In **Create Mapping**, review source ↔ destination pairs.

    * Click **Auto Map** to map identical field names automatically.
    * Click **Clear Mapping** to reset if needed.\
      Finish by clicking **Save**.

    <figure><img src="../../../../.gitbook/assets/24 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
24. **Field Extraction**\
    Data Loader Pro retrieves only the fields explicitly mapped by the user, avoiding unnecessary data fetches. When checking for `AutorabitExtId__c`, the system validates that it is marked as both **External ID** and **Unique**; if not, these attributes are set automatically. Newly identified objects are saved to the database to improve processing efficiency.
25. **External ID Field Mapping**\
    This feature allows using an external ID instead of a Salesforce record ID to establish relationships between records during the Data Loader Pro operation. For example, if Object B has a lookup to Object A, the values in a field marked as an External ID on Object A can be used to relate the two.
    * **Source Field:** Select the source org containing the values to populate the destination external ID field.
    * **Destination Field:** Select the destination org where these values remain unique across all records.
26. **Open Masking**\
    Go to the **Masking** step and click **New** to add a masking rule.

    <figure><img src="../../../../.gitbook/assets/25 - DL PRO.png" alt=""><figcaption></figcaption></figure>
27. **Choose object & field type**\
    In **Create Masking Rule**, pick the **Object** (e.g., `nFORCE__Brand__c`) and **Field Type** (Text/Textarea). Provide a **Masking value** when required.

    <figure><img src="../../../../.gitbook/assets/26 - DL PRO.png" alt=""><figcaption></figcaption></figure>
28. **Select masking style**\
    Choose a **Masking style**: **Prefix**, **Suffix**, **Replace**, **Shuffle**, or **Generate Random**.

    <figure><img src="../../../../.gitbook/assets/27 - DL PRO.png" alt=""><figcaption></figcaption></figure>
29. **Choose the Masking Style**

    * **Prefix** – Adds a specified value before the original field value.\
      &#xNAN;_&#x45;xample:_ Source value `ABC` with prefix `123` → Deployed value `123.ABC`.
    * **Suffix** – Adds a specified value after the original field value.\
      &#xNAN;_&#x45;xample:_ Source value `ABC` with suffix `123` → Deployed value `ABC.123`.
    * **Replace** – Replaces the original field value entirely with the specified masking value.\
      &#xNAN;_&#x45;xample:_ Source value `ABC` replaced with `123` → Deployed value `123`.
    * **Shuffle** – Randomly rearranges characters in the field value while leaving other columns unaffected.\
      &#xNAN;_&#x45;xample:_ Source value `ABCDE` → Deployed value `DCBEA`.
    * **Generate Random** – Replaces the original value with a randomly generated value of a defined length.\
      &#xNAN;_&#x45;xample:_ Source value `ABC` with random length `7` → Deployed value `15d3aRG`.

    _**`Note:`**` ``Masking is not applied if the field value is empty.`_
30. **Select target fields & save**\
    Select the fields the rule should apply to (e.g., **Name**, lookup keys) and click **Save**.

    <figure><img src="../../../../.gitbook/assets/28 - DL PRO.png" alt=""><figcaption></figcaption></figure>
31. **Review rule in list**\
    The rule appears in the **Masking** grid with its value and style. Click the actions menu to **View Rule** or **Edit Rule**.

    <figure><img src="../../../../.gitbook/assets/29 - DL PRO.png" alt=""><figcaption></figcaption></figure>
32. **View rule details**\
    Use **View Rule** to see the full configuration: rule name, object, type, masking value/style, timestamps, and the fields impacted.

    <figure><img src="../../../../.gitbook/assets/30 - DL PRO.png" alt=""><figcaption></figcaption></figure>
33. **Edit if needed**\
    Choose **Edit Rule** from the actions menu to adjust the object, style, value, or field selection, then **Save**.

    <figure><img src="../../../../.gitbook/assets/30.1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
34. Observe the rule created for masking.

    <figure><img src="../../../../.gitbook/assets/31 - DL PRO.png" alt=""><figcaption></figcaption></figure>
35. Click "Delete" to delete the rule created

    <figure><img src="../../../../.gitbook/assets/32 - DL PRO.png" alt=""><figcaption></figcaption></figure>
36. Observe the rule deleted

    <figure><img src="../../../../.gitbook/assets/33 - DL PRO.png" alt=""><figcaption></figcaption></figure>
37. Open the Schedule step

    * The page defaults to **No Schedule**. This runs the job only when triggered manually. Click **Next** to continue without a schedule.

    <figure><img src="../../../../.gitbook/assets/35 - DL PRO.png" alt=""><figcaption></figcaption></figure>
38. Set a Daily schedule

    * Click **Daily**.
    * Choose **Scheduling Starts From** (start date).
    * Under **Repeats**, pick one:
      * **On specific time** and set the time, or
      * **At fixed interval of every** _N_ hours and select the starting hour.
    * Under **Scheduling Ends**, choose **Never**, **X Occurrences from creation**, or a specific end date.

    <figure><img src="../../../../.gitbook/assets/36 - DL PRO.png" alt=""><figcaption></figcaption></figure>
39. Set a Weekly schedule

    * Click **Weekly**.
    * Choose **Scheduling Starts From** (start date).
    * Select one or more days (Sun–Sat).
    * Set **On Specific Time**.
    * Choose when the schedule ends: **Never**, **X Occurrences from creation**, or a specific end date.

    <figure><img src="../../../../.gitbook/assets/37 - DL PRO.png" alt=""><figcaption></figcaption></figure>


40. Click **Next** to move to **Job Configuration**.

    The table below lists the configurations to choose from, along with their descriptions:

    |   |                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | - | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | 1 | **`Disable workflows`**                                                    | When this option is selected, all workflow rules associated with the relevant Salesforce objects are programmatically deactivated prior to initiating the migration process. This ensures that automation triggers do not interfere with the data transfer from the source to the destination sandbox. Upon successful migration completion, all workflow rules are reinstated to their original active state, preserving existing business logic.         |
    | 2 | **`Disable validation rules`**                                             | Validation rules enforce predefined data integrity constraints before a record can be saved. Selecting this option temporarily disables all validation rules on the associated Salesforce objects for the duration of the migration process. This ensures uninterrupted data transfer from the source to the destination sandbox. Upon successful migration completion, all validation rules are programmatically restored to their original active state. |
    | 3 | **`Use Bulk API`**                                                         | The Bulk API leverages REST architecture to efficiently handle large-scale data operations, including insert, update, and delete requests. Jobs may execute in **serial mode**, where batches are processed sequentially, or in **parallel mode**, where multiple batches are processed concurrently. Parallel processing increases the degree of parallelism, improving data throughput for high-volume workloads.                                        |
    | 4 | **`Insert/update with null values`**                                       | Insert/update with null values                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | 5 | **`Minimize multiple references between the same objects`**                | Eliminates redundant API calls in scenarios with multiple references between identical objects.                                                                                                                                                                                                                                                                                                                                                            |
    | 6 | **`Automatically apply master object filter on other dependency objects`** | All objects in the hierarchy are derived from the Master Object filters, preventing redundant record additions caused by self-references or multiple references.                                                                                                                                                                                                                                                                                           |
    | 7 | **`Data encryption for data files`**                                       | Data encryption for data files                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | 8 | **`Incremental data migration`**                                           | After the data load completes, only the newly created records are migrated to the destination sandbox, ensuring no duplicate or pre-existing data is transferred.                                                                                                                                                                                                                                                                                          |
41. Save the job (Process Details)

    1. **Fill in process details**
       * **Name**: Enter a clear job name (e.g., _Brands Migration Masking_).
       * **Job group**: Pick an existing group or click **+** to create one.
       * **User Name Suffix (Source Org)** and **(Destination Org)**: Enter the suffixes to avoid username conflicts.
       * (Optional) **Ignore Community Users**: Check if you don’t want to migrate community users.
       * Review the **Master Object** shown on the right.

    <figure><img src="../../../../.gitbook/assets/40 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
42. **Save**
    * Click **Save** (bottom-right).
43. **Confirmation**

    * You’ll return to the **Dataloader Pro** list and see a green **Success** toast: **“Job saved successfully.”**
    * Your new job now appears in the list.

    <figure><img src="../../../../.gitbook/assets/41 - DL PRO.png" alt=""><figcaption></figcaption></figure>
44. Click on the "Summary" to view the job summary

    <figure><img src="../../../../.gitbook/assets/42 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/43 - DL PRO.png" alt=""><figcaption></figcaption></figure>
45. Open Job Results

    * Go to **Dataloader Pro**.
    * For your job (e.g., _Brands Migration \* Masking_), click the **⋮** menu under **Actions** and choose **Job Results**.

    <figure><img src="../../../../.gitbook/assets/44 - DL PRO.png" alt=""><figcaption></figcaption></figure>
46. Review the Job Summary

    * You’ll land on **Summary** → **Master Object**.
    * The row shows quick actions: **VR/WFR** (validation/workflow), **Filters**, **Mappings**, plus **last run results**.

    <figure><img src="../../../../.gitbook/assets/45 - DL PRO.png" alt=""><figcaption></figcaption></figure>
47. Open Validation/Workflow controls

    * Click the **VR/WFR** icon (stacked lines) beside the object.

    <figure><img src="../../../../.gitbook/assets/46 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
48. Check Validation Rules:

    * In the **Validation Rules** tab, review the listed rules (Previous State, Current State).
    * Use **Enable** where applicable; click **Ok** when done (or continue to the next tab).

    <figure><img src="../../../../.gitbook/assets/47 - DL PRO.png" alt=""><figcaption></figcaption></figure>
49. Check Workflow Rules

    * Switch to the **Workflow Rules** tab and review similarly (enable/disable as needed).
    * Click **Ok** to close.

    <figure><img src="../../../../.gitbook/assets/48 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
50. Open and Review Filters

    * Back on **Summary**, click the **Filter** icon.

    <figure><img src="../../../../.gitbook/assets/49 - DL PRO.png" alt=""><figcaption></figcaption></figure>
51. Configure Filter criteria

    * Choose **Input Options: Upload CSV File**.
    * Set **Select Field** and **Operator** (e.g., _Id_ + _Equals_).
    * Paste or **Auto Populate** your SOQL/values (example shows a SELECT … IN (…) list).
    * Optional: click **Record Count**, **Validate**, then **Apply**.

    <figure><img src="../../../../.gitbook/assets/50 - DL PRO.png" alt=""><figcaption></figcaption></figure>
52. Review Field Mappings

    * From **Summary**, click **Mappings** to open the mapping dialog and verify/adjust source→destination field mappings.

    <figure><img src="../../../../.gitbook/assets/51 - DL PRO.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/52 - DL PRO.png" alt=""><figcaption></figcaption></figure>
53. View Success Results – Master Object

    1. From **Summary → Master Object**, locate **Results of last run**.
    2. Click the **Success:** 🔍 icon (**Click to View**) for the master object.

    <figure><img src="../../../../.gitbook/assets/52.1 - DL PRO (2).png" alt=""><figcaption></figcaption></figure>
54. See Success Details (CSV)

    1. Review the **Destination Id** and **Status** for each processed record.
    2. Use **Search** and pagination as needed, then close the dialog.

    <figure><img src="../../../../.gitbook/assets/52.2 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
55. Review Ancestor Object Results

    1. Open **Summary → Ancestor Objects**.
    2. For each ancestor object, click the **Success** 🔍 or **Failure** 🔍 icons to view details.
    3. Use the **download** icon to export results if required.
    4. The toggle **Skip Records** is in "inactive" state as the records are not choosen to be skipped while creating the job.

    <figure><img src="../../../../.gitbook/assets/53 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
56. Review Child Object Results

    1. Open **Summary → Child Objects**.
    2. Click the **Success** 🔍 or **Failure** 🔍 icons to view child-object run results.
    3. Use the **download** icon to export results if needed.

    <figure><img src="../../../../.gitbook/assets/54 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
57. Open Masking Rule Actions

    1. Go to **Summary → Masking Rules**.
    2. Click the **⋮** menu for a rule and choose **View Rule** (or **Edit Rule**).

    <figure><img src="../../../../.gitbook/assets/55 - DL PRO.png" alt=""><figcaption></figcaption></figure>
58. View Masking Rule Details

    1. In **Masking Object Info**, verify **Rule**, **Object**, **Type**, **Masking style/value**, and the **Fields** impacted.
    2. Use **Search** if the field list is long; click **Close** when done.

    <figure><img src="../../../../.gitbook/assets/56 - DL PRO.png" alt=""><figcaption></figcaption></figure>
59. Start Editing a Masking Rule

    1. From **Masking Rules**, open the **⋮** menu and select **Edit Rule**.

    <figure><img src="../../../../.gitbook/assets/57 - DL PRO.png" alt=""><figcaption></figcaption></figure>
60. Edit Masking Rule

    1. In **Edit Masking Rule**, confirm **Select Object**, **Field Type**, **Masking Style**, and **Masking value**.
    2. Check the **Fields** to apply the masking to.
    3. Click **Save** to apply changes.

    <figure><img src="../../../../.gitbook/assets/58 - DL PRO.png" alt=""><figcaption></figcaption></figure>
61. Confirm Rule List

    1. You return to **Masking Rules**.
    2. Verify the rule appears as expected (use **Modified date** to confirm updates).

    <figure><img src="../../../../.gitbook/assets/59 - DL PRO.png" alt=""><figcaption></figcaption></figure>
62. Create a New Masking Rule

    1. From **Masking Rules**, click **New** to open **Create Masking Rule**.
    2. Set **Select Object**, **Field Type**, **Masking Style**, **Masking value**, and select the **Fields**.
    3. Click **Save** to add the rule.

    <figure><img src="../../../../.gitbook/assets/60 - DL PRO.png" alt=""><figcaption></figcaption></figure>
63. **Open Edit**

    * From **Dataloader Pro**, find your job.
    * In **Actions**, click the **⋮** menu and choose **Edit**.

    <figure><img src="../../../../.gitbook/assets/61 - DL PRO.png" alt=""><figcaption></figcaption></figure>
64. **Edit Job – Login & Select Object**

    * On **Edit Dataloader Job**, choose **Source Org** and **Destination Org**.
    * Click **Login and fetch objects** to load metadata.
    * Click **Next** to continue through the setup steps as needed.

    <figure><img src="../../../../.gitbook/assets/62 - DL PRO.png" alt=""><figcaption></figcaption></figure>
65. **Open Schedule**

    * From **Dataloader Pro**, open the **⋮** menu for the job.
    * Select **Schedule**.

    <figure><img src="../../../../.gitbook/assets/63 - DL PRO.png" alt=""><figcaption></figcaption></figure>
66. **Set Scheduling Type**

    * In the **Schedule** panel, choose **No Schedule**, **Daily**, or **Weekly**.
    * Follow the [scheduling process](dataloader-pro.md#:~:text=Open%20the%20Schedule%20step) to set up a schedule.
    * Configure any timing options shown, then click **Schedule**.

    <figure><img src="../../../../.gitbook/assets/64 - DL PRO.png" alt=""><figcaption></figcaption></figure>
67. **Delete a Job**

    * From **Dataloader Pro**, open the job’s **⋮** menu.
    * Click **Delete**.

    <figure><img src="../../../../.gitbook/assets/65 - DL PRO.png" alt=""><figcaption></figcaption></figure>
68. **Confirm Deletion**

    * Review the job name in the confirmation dialog.
    * Click **Delete** to remove, or **Cancel** to keep the job.

    <figure><img src="../../../../.gitbook/assets/66 - DL PRO.png" alt=""><figcaption></figcaption></figure>
69. **Clone a Job**

    * From **Dataloader Pro**, open the job’s **⋮** menu.
    * Click **Clone**.

    <figure><img src="../../../../.gitbook/assets/67 - DL PRO.png" alt=""><figcaption></figcaption></figure>
70. **Configure Clone**

    * In the **Clone** panel, update **Name**, **Job Group**, **Source Sandbox**, **Destination Sandbox**, and any **User Suffixes**.
    * Click **Clone**.

    <figure><img src="../../../../.gitbook/assets/68 - DL PRO.png" alt=""><figcaption></figcaption></figure>
71. **Verify Cloned Job**

    * Back on **Dataloader Pro**, confirm the new job (e.g., _Brands Migration Masking-Copy_) appears in the list.

    <figure><img src="../../../../.gitbook/assets/69 - DL PRO.png" alt=""><figcaption></figcaption></figure>
72. Run Job

    * From Dataloader Pro, locate your job.
    * In **Actions**, click the **▶ Run** icon.

    <figure><img src="../../../../.gitbook/assets/70 - DL PRO.png" alt=""><figcaption></figcaption></figure>
73. Run Configuration

    * In **Run Configuration**, review/adjust options (e.g., Disable workflow rules, Use Bulk API, Parallel/Serial mode, Batch size, UTF-8, Encrypt data files).
    * Click **Run**.

    <figure><img src="../../../../.gitbook/assets/70.1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
74. Monitor Run Status

    * A toast confirms **Run Process Initiated Successfully**.
    * The **Status** shows **In Progress** until the job completes.

    <figure><img src="../../../../.gitbook/assets/71 - DL PRO.png" alt=""><figcaption></figcaption></figure>
75. Abort a Running Job

    * While the job is running, click the **⏹ Abort** icon in **Actions** to stop execution.

    <figure><img src="../../../../.gitbook/assets/72 - DL PRO.png" alt=""><figcaption></figcaption></figure>
76. Confirm Completion

    * When finished, verify the **Status** shows **Success** (or review failures if shown).

    <figure><img src="../../../../.gitbook/assets/73 - DL PRO.png" alt=""><figcaption></figcaption></figure>
77. Open Job Log

    * From Dataloader Pro, open the job’s **⋮** menu.
    * Select **Log**.

    <figure><img src="../../../../.gitbook/assets/74 - DL PRO.png" alt=""><figcaption></figcaption></figure>
78. Review Log Details

    * In **Log Details**, review each step, object counts, and success/error messages.
    * Use search as needed; close when done.

    <figure><img src="../../../../.gitbook/assets/75 - DL PRO.png" alt=""><figcaption></figcaption></figure>
79. Delete Data Encrypt Files

    * From the job’s **⋮** menu, choose **Delete Data Encrypt Files** to remove protected artifacts created during runs.

    <figure><img src="../../../../.gitbook/assets/76 - DL PRO.png" alt=""><figcaption></figcaption></figure>
80. Confirm Deletion

    * In the confirmation dialog, click **Delete** to permanently remove the encrypted files, or **Cancel** to keep them.

    <figure><img src="../../../../.gitbook/assets/77 - DL PRO.png" alt=""><figcaption></figcaption></figure>

