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
53. View Success Results – Master Object (Screen 52.1)

    1. From **Summary → Master Object**, locate **Results of last run**.
    2. Click the **Success:** 🔍 icon (**Click to View**) for the master object.

    <figure><img src="../../../../.gitbook/assets/52.1 - DL PRO (2).png" alt=""><figcaption></figcaption></figure>
54. See Success Details (CSV) (Screen 52.2)

    1. Review the **Destination Id** and **Status** for each processed record.
    2. Use **Search** and pagination as needed, then close the dialog.

    <figure><img src="../../../../.gitbook/assets/52.2 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
55. Review Ancestor Object Results (Screen 53)

    1. Open **Summary → Ancestor Objects**.
    2. For each ancestor object, click the **Success** 🔍 or **Failure** 🔍 icons to view details.
    3. Use the **download** icon to export results if required.
    4. The toggle **Skip Records** is in "inactive" state as the records are not choosen to be skipped while creating the job.

    <figure><img src="../../../../.gitbook/assets/53 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
56. Review Child Object Results (Screen 54)

    1. Open **Summary → Child Objects**.
    2. Click the **Success** 🔍 or **Failure** 🔍 icons to view child-object run results.
    3. Use the **download** icon to export results if needed.

    <figure><img src="../../../../.gitbook/assets/54 - DL PRO (1).png" alt=""><figcaption></figcaption></figure>
57. Open Masking Rule Actions (Screen 55)

    1. Go to **Summary → Masking Rules**.
    2. Click the **⋮** menu for a rule and choose **View Rule** (or **Edit Rule**).

    <figure><img src="../../../../.gitbook/assets/55 - DL PRO.png" alt=""><figcaption></figcaption></figure>
58. View Masking Rule Details (Screen 56)

    1. In **Masking Object Info**, verify **Rule**, **Object**, **Type**, **Masking style/value**, and the **Fields** impacted.
    2. Use **Search** if the field list is long; click **Close** when done.

    <figure><img src="../../../../.gitbook/assets/56 - DL PRO.png" alt=""><figcaption></figcaption></figure>
59. Start Editing a Masking Rule (Screen 57)

    1. From **Masking Rules**, open the **⋮** menu and select **Edit Rule**.

    <figure><img src="../../../../.gitbook/assets/57 - DL PRO.png" alt=""><figcaption></figcaption></figure>
60. Edit Masking Rule (Screen 58)

    1. In **Edit Masking Rule**, confirm **Select Object**, **Field Type**, **Masking Style**, and **Masking value**.
    2. Check the **Fields** to apply the masking to.
    3. Click **Save** to apply changes.

    <figure><img src="../../../../.gitbook/assets/58 - DL PRO.png" alt=""><figcaption></figcaption></figure>
61. Confirm Rule List (Screen 59)

    1. You return to **Masking Rules**.
    2. Verify the rule appears as expected (use **Modified date** to confirm updates).

    <figure><img src="../../../../.gitbook/assets/59 - DL PRO.png" alt=""><figcaption></figcaption></figure>
62. Create a New Masking Rule (Screen 60)

    1. From **Masking Rules**, click **New** to open **Create Masking Rule**.
    2. Set **Select Object**, **Field Type**, **Masking Style**, **Masking value**, and select the **Fields**.
    3. Click **Save** to add the rule.

    <figure><img src="../../../../.gitbook/assets/60 - DL PRO.png" alt=""><figcaption></figcaption></figure>
63. **Open Edit (Screen 61)**

    * From **Dataloader Pro**, find your job.
    * In **Actions**, click the **⋮** menu and choose **Edit**.

    <figure><img src="../../../../.gitbook/assets/61 - DL PRO.png" alt=""><figcaption></figcaption></figure>
64. **Edit Job – Login & Select Object (Screen 62)**

    * On **Edit Dataloader Job**, choose **Source Org** and **Destination Org**.
    * Click **Login and fetch objects** to load metadata.
    * Click **Next** to continue through the setup steps as needed.

    <figure><img src="../../../../.gitbook/assets/62 - DL PRO.png" alt=""><figcaption></figcaption></figure>
65. **Open Schedule (Screen 63)**

    * From **Dataloader Pro**, open the **⋮** menu for the job.
    * Select **Schedule**.

    <figure><img src="../../../../.gitbook/assets/63 - DL PRO.png" alt=""><figcaption></figcaption></figure>
66. **Set Scheduling Type (Screen 64)**

    * In the **Schedule** panel, choose **No Schedule**, **Daily**, or **Weekly**.
    * Follow the [scheduling process](dataloader-pro.md#:~:text=Open%20the%20Schedule%20step) to set up a schedule.
    * Configure any timing options shown, then click **Schedule**.

    <figure><img src="../../../../.gitbook/assets/64 - DL PRO.png" alt=""><figcaption></figcaption></figure>
67. **Delete a Job (Screen 65)**

    * From **Dataloader Pro**, open the job’s **⋮** menu.
    * Click **Delete**.

    <figure><img src="../../../../.gitbook/assets/65 - DL PRO.png" alt=""><figcaption></figcaption></figure>
68. **Confirm Deletion (Screen 66)**

    * Review the job name in the confirmation dialog.
    * Click **Delete** to remove, or **Cancel** to keep the job.

    <figure><img src="../../../../.gitbook/assets/66 - DL PRO.png" alt=""><figcaption></figcaption></figure>
69. **Clone a Job (Screen 67)**

    * From **Dataloader Pro**, open the job’s **⋮** menu.
    * Click **Clone**.

    <figure><img src="../../../../.gitbook/assets/67 - DL PRO.png" alt=""><figcaption></figcaption></figure>
70. **Configure Clone (Screen 68)**

    * In the **Clone** panel, update **Name**, **Job Group**, **Source Sandbox**, **Destination Sandbox**, and any **User Suffixes**.
    * Click **Clone**.

    <figure><img src="../../../../.gitbook/assets/68 - DL PRO.png" alt=""><figcaption></figcaption></figure>
71. **Verify Cloned Job (Screen 69)**

    * Back on **Dataloader Pro**, confirm the new job (e.g., _Brands Migration Masking-Copy_) appears in the list.

    <figure><img src="../../../../.gitbook/assets/69 - DL PRO.png" alt=""><figcaption></figcaption></figure>
72. Run Job (Screen 70)

    * From Dataloader Pro, locate your job.
    * In **Actions**, click the **▶ Run** icon.

    <figure><img src="../../../../.gitbook/assets/70 - DL PRO.png" alt=""><figcaption></figcaption></figure>
73. Run Configuration (Screen 70.1)

    * In **Run Configuration**, review/adjust options (e.g., Disable workflow rules, Use Bulk API, Parallel/Serial mode, Batch size, UTF-8, Encrypt data files).
    * Click **Run**.

    <figure><img src="../../../../.gitbook/assets/70.1 - DL PRO.png" alt=""><figcaption></figcaption></figure>
74. Monitor Run Status (Screen 71)

    * A toast confirms **Run Process Initiated Successfully**.
    * The **Status** shows **In Progress** until the job completes.

    <figure><img src="../../../../.gitbook/assets/71 - DL PRO.png" alt=""><figcaption></figcaption></figure>
75. Abort a Running Job (Screen 72)

    * While the job is running, click the **⏹ Abort** icon in **Actions** to stop execution.

    <figure><img src="../../../../.gitbook/assets/72 - DL PRO.png" alt=""><figcaption></figcaption></figure>
76. Confirm Completion (Screen 73)

    * When finished, verify the **Status** shows **Success** (or review failures if shown).

    <figure><img src="../../../../.gitbook/assets/73 - DL PRO.png" alt=""><figcaption></figcaption></figure>
77. Open Job Log (Screen 74)

    * From Dataloader Pro, open the job’s **⋮** menu.
    * Select **Log**.

    <figure><img src="../../../../.gitbook/assets/74 - DL PRO.png" alt=""><figcaption></figcaption></figure>
78. Review Log Details (Screen 75)

    * In **Log Details**, review each step, object counts, and success/error messages.
    * Use search as needed; close when done.

    <figure><img src="../../../../.gitbook/assets/75 - DL PRO.png" alt=""><figcaption></figcaption></figure>
79. Delete Data Encrypt Files (Screen 76)

    * From the job’s **⋮** menu, choose **Delete Data Encrypt Files** to remove protected artifacts created during runs.

    <figure><img src="../../../../.gitbook/assets/76 - DL PRO.png" alt=""><figcaption></figcaption></figure>
80. Confirm Deletion (Screen 77)

    * In the confirmation dialog, click **Delete** to permanently remove the encrypted files, or **Cancel** to keep them.

    <figure><img src="../../../../.gitbook/assets/77 - DL PRO.png" alt=""><figcaption></figcaption></figure>













































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
