# Setting Up a Test Environment

## **Test Environment Setup: Overview**

The ARM test environment enables efficient data transfer from CSV files into destination sandboxes, optimizing job execution times. This setup is particularly beneficial for validating data migration scenarios before performing a full-scale execution.

### Step-By-Step Guide: <a href="#test-environment-setup-overview" id="test-environment-setup-overview"></a>

1.  Navigate to the "DataLoader - Test Environment" by logging into ARM application.

    <figure><img src="../../../../.gitbook/assets/6 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
2.  Click on the "Create new job" button to initiate the job creation.

    <figure><img src="../../../../.gitbook/assets/7 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
3.  Select the required Org and click on the "Log and fetch objects" button to fetch the objects.

    <figure><img src="../../../../.gitbook/assets/8 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/9 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
4.  Observe the object list fetched and select the required object.

    <figure><img src="../../../../.gitbook/assets/10 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
5. Click "Next" to continue to the "Source Data" section.
6.  Either select the required file or drop the file onto the box to continue with the data import.

    <figure><img src="../../../../.gitbook/assets/11 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/12 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
7.  Drop the file

    <figure><img src="../../../../.gitbook/assets/13 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
8.  After adding the file, click upload file to upload the file

    <figure><img src="../../../../.gitbook/assets/14 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
9.  To indicate the progress of the upload, a progress bar will be displayed. On successfull upload, a success message will be displayed

    <figure><img src="../../../../.gitbook/assets/15 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
10. Auto-Map Fields – Master Object

    * Under **Master Object**, click the **Mappings** icon for **Account**.
    * In **Create Mapping: Account**, click **Auto Map** to match like-named fields.
    * Use **Search** to locate specific fields if needed.

    <figure><img src="../../../../.gitbook/assets/16 - Test Environment Setup (2).png" alt=""><figcaption></figcaption></figure>
11. Save Master Object Mapping

    * Review the mapped **Fields (Destination)** and complete any unmapped ones.
    * Click **Save**.

    <figure><img src="../../../../.gitbook/assets/17 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
12. Open Ancestor Object Mapping

    * Switch to the **Ancestor Objects** tab.
    * For each object (e.g., **Opportunity**), click the **Mappings** icon.

    <figure><img src="../../../../.gitbook/assets/18 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
13. Auto-Map Fields – Ancestor Object

    * In **Create Mapping: Opportunity**, click **Auto Map**.
    * Verify mappings and manually adjust where required.

    <figure><img src="../../../../.gitbook/assets/19 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
14. Save Ancestor Object Mapping

    * Confirm the field selections for the ancestor object.
    * Click **Save**.

    <figure><img src="../../../../.gitbook/assets/20 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
15. Proceed to Process Details

    * Ensure the **Success: Mappings saved successfully** message appears.
    * Click **Next** to continue to **Process Details**.

    <figure><img src="../../../../.gitbook/assets/21 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
16. Configure Job Details

    * In **Create Test Environment Job → Process Details**, provide a **Job Name**.
    * Select or enter a **Job Group Name**.
    * Click **Save**.

    <figure><img src="../../../../.gitbook/assets/22 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
17. #### View Job in Test Environment List

    * Clicking "Save" will redirect to the "Test Environment" dashboard..
    * The newly created job appears in the list under the configured group.
    * Under **Actions**, click the **eye icon** to view job summary.

    <figure><img src="../../../../.gitbook/assets/23 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
18. #### Review Job Summary

    * The **Summary panel** displays key job information:
      * Destination Org
      * Created Time & Created By
      * Uploaded Zipfile
      * Validation/Workflow Rules status
      * Batch Size
    * Review details and close the summary.

    <figure><img src="../../../../.gitbook/assets/24 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
19. #### Run the Test Environment Job

    * From the job list, click the **Run icon** under **Actions** for the created job.

    <figure><img src="../../../../.gitbook/assets/25 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
20. #### Run Configuration Settings

    * In the **Run Configuration** panel, set the following:
      * **Batch Size** (default 200, range 1–2000).
      * Toggle options if required:
        * _Disable workflow rules_
        * _Disable validation rules_
        * _Use Bulk API_
    * Click **Run** to initiate the process.

    <figure><img src="../../../../.gitbook/assets/26 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
21. #### Run Initiation Confirmation

    * A notification appears: **Run Process Initiated Successfully**.
    * The job status changes to a spinning icon (processing).
    * Action buttons become available: **View**, **Stop**.

    <figure><img src="../../../../.gitbook/assets/27 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
22. #### Run Configurations

    | **Disable Workflows**        | Temporarily deactivates Salesforce workflows during migration to prevent unintended triggers. Workflows are automatically re-enabled after migration completes.                                                                        |
    | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Disable Validation Rules** | Suspends validation rules to allow uninterrupted data migration. Rules are automatically restored once the migration is complete.                                                                                                      |
    | **Use Bulk API**             | Leverages Salesforce Bulk API for handling large data volumes efficiently. Jobs can be executed in **serial** (sequentially, one after another) or **parallel** (simultaneously). For higher throughput, parallel mode is recommended. |
23. #### Job Status – In Progress

    * The job displays an **In Progress** status in the list.
    * Monitor the status until completion.

    <figure><img src="../../../../.gitbook/assets/28 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
24. #### Abort Job Execution

    * If needed, click **Stop (Abort)** under Actions.
    * A confirmation displays to cancel the run.

    <figure><img src="../../../../.gitbook/assets/29 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
25. #### Run Job Completion

    * Once completed, the job reflects a **final execution status** (e.g., Success/Failed).
    * Review status before proceeding with further validation or data checks.

    <figure><img src="../../../../.gitbook/assets/30 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
26. **Access Job Results**

    * Under Actions for a job, select **Job Results**.

    <figure><img src="../../../../.gitbook/assets/30.1 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
27. **Open Validation / Workflow Rules**

    * Click on the **VR/WFR** icon beside the object.

    <figure><img src="../../../../.gitbook/assets/33 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
28. **View Workflow/Validation Rules**

    * The **Validation / Workflow Rules** panel opens.
    * Review Validation Rules under **Name, Previous State, Current State, Enable, Error (if any)**.
    * Switch to the **Workflow Rules** tab.
    * Validate existing Workflow Rules or confirm that none are displayed.

    <figure><img src="../../../../.gitbook/assets/34 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
29. **Edit Object Mapping**

    * Select the **Mappings** icon to open **Edit Mapping**.
    * Review source and destination fields.
    * Use **Auto Map** to match fields automatically, or manually map unmapped fields.
    * Click **Save** to update mappings.

    <figure><img src="../../../../.gitbook/assets/35 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
30. **View Job Run Results – Success**

    * Under **Results of Last Run**, click the **Success count** icon.
    * A list of records with **Destination IDs** and **Status: Item Created** is displayed.

    <figure><img src="../../../../.gitbook/assets/35 - Test Environment Setup (2).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/36 - Test Environment Setup (2).png" alt=""><figcaption></figcaption></figure>
31. **View Job Run Results – Failure**

    * Under **Results of Last Run**, click the **Failure count** icon.
    * A list of failed records with **Source IDs** and corresponding **Error Messages** is displayed.

    <figure><img src="../../../../.gitbook/assets/38 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/39 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
32. #### Search by Job Name

    * Use the **Job name** field to locate specific jobs quickly.
    * Begin typing the job name to see filtered results update automatically.

    <figure><img src="../../../../.gitbook/assets/40 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
33. #### Filter by Status

    * Open the **Status** dropdown to refine job listings.
    * Observe the available options to set the right filter criteria.

    <figure><img src="../../../../.gitbook/assets/41 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
34. #### Apply Advanced Filters

    * Click **Filters** to apply additional criteria.
    * Choose filters such as:
      * **Category**
      * **Destination Org**
      * **Created Date Range**
    * Click **Apply** to filter or **Reset** to clear all selections.

    <figure><img src="../../../../.gitbook/assets/42 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
35. #### Manage Columns

    * Click **Columns** to customize the table view.
    * Additional columns can be included in the view by selecting the desired options from the **Columns** menu. Columns that are not relevant can be deselected to keep the view focused on essential information.

    <figure><img src="../../../../.gitbook/assets/43 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
36. #### Job Actions – Menu Options

    * Open the **⋮ (More)** menu next to any job to perform actions.
    * Available options include:
      * **Run**
      * **Edit**
      * **Clone**
      * **Delete**

    <figure><img src="../../../../.gitbook/assets/44 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
37. #### Running a Job
    *   Identify the desired job in the job list.



        <figure><img src="../../../../.gitbook/assets/44 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
    * Click the **Run** button under the _Actions_ column.
    * A configuration panel opens with the following options:
      * **Disable workflow rules**
      * **Disable validation rules**
    *   Adjust the options if required, then click **Run**.



        <figure><img src="../../../../.gitbook/assets/46 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
    * A confirmation message _“Run Process Initiated Successfully”_ appears.
    * The job status updates to indicate that the process has started.
38. #### Monitoring Job Execution

    * During execution, the job’s _Status_ column updates to show the current progress.
    * Options available while the job is running:
      * **View** – Inspect job configuration or progress.
      * **Stop** – Terminate the execution if necessary.
    * Once completed, the status reflects success, failure, or warnings.

    <figure><img src="../../../../.gitbook/assets/47 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
39. #### Cloning a Job

    * From the job list, open the **Actions** menu (**⋮ -** three dots).
    * Select **Clone**.
    * A **Clone Job** panel appears where the following details can be updated:
      * **Name** – Defaults to original job name with _-Copy_ appended, but can be edited.
      * **Job Group** – Assign to an existing group or create a new one.
      * **Destination Sandbox** – Select the target sandbox.

    <figure><img src="../../../../.gitbook/assets/48 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    * Click **Clone** to create the duplicate job.
    * The cloned job appears in the job list.

    <figure><img src="../../../../.gitbook/assets/49 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
40. Open Bulk Actions

    * Click the **Bulk Actions** (three-line) icon at the top-right of the **Test Environment** list.

    <figure><img src="../../../../.gitbook/assets/49.1 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
41. Bulk Actions Menu

    * Review available actions:
      * **Run** (disabled for bulk in this view)
      * **Edit** – bulk update job groups
      * **Clone** – clone multiple jobs at once
      * **Delete** – remove multiple jobs

    <figure><img src="../../../../.gitbook/assets/49.1.11 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
42. Start Bulk Edit

    * From **Bulk Actions**, click **Edit** to open the bulk group editor.

    <figure><img src="../../../../.gitbook/assets/49.2 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
43. Bulk Edit Job Groups

    * Use the **Edit Job Group – All** dialog to update the **Category** (group) for many jobs at once.
    * Optional: use **Search** to filter the list; navigate with **Previous/Next** or the page size selector.
    * Click **Save** to apply group changes, or **Cancel** to discard.

    <figure><img src="../../../../.gitbook/assets/49.3 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
44. Start Bulk Clone

    * From **Bulk Actions**, click **Clone** to open the bulk clone setup.

    <figure><img src="../../../../.gitbook/assets/51 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
45. Configure Bulk Clone

    * In **Clone – All**:
      * **Group name** (required) – Enter the target group for the new copies.
      * **Destination Sandbox** (required) – Choose where all selected jobs will be cloned.
    * Click **Clone** to create the copies, or **Cancel** to exit.

    <figure><img src="../../../../.gitbook/assets/52 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
46. Start Bulk Delete

    * From **Bulk Actions**, click **Delete** to open the selection panel.

    <figure><img src="../../../../.gitbook/assets/53 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
47. Select Jobs to Delete

    * In **Category: All**, select individual jobs or use the header checkbox to select all.
    * Click **Delete** to permanently remove the selected jobs, or **Cancel** to keep them.

    <figure><img src="../../../../.gitbook/assets/54 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
