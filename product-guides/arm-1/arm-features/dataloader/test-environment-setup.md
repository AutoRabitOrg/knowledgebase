# Test Environment Setup

**Test Environment Setup: Overview**\
The ARM test environment enables efficient data transfer from CSV files into destination sandboxes, optimizing job execution times. This setup is particularly beneficial for validating data migration scenarios before performing a full-scale execution.

Step-By-Step Guide:

1.  Navigate to the "Dataloader - Test Environment" by logging into ARM application

    <figure><img src="../../../../.gitbook/assets/6 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
2.  Click on the "Create new job" button to initiate the job creation

    <figure><img src="../../../../.gitbook/assets/7 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
3.  Select the required  ORG and click on the "log and fetch objects" button to fetch the objects

    <figure><img src="../../../../.gitbook/assets/8 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/9 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
4.  Observe the object list fetched and select the required object

    <figure><img src="../../../../.gitbook/assets/10 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
5. Click "NExt" to continue to the "Source Data" section
6.  Either select the required file or drop the file onto the box, to continue with the data import

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
13. Auto-Map Fields – Ancestor Object (Screen 19)

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
19. #### Run the Test Environment Job (Screen 25)

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
22. #### Job Status – In Progress

    * The job displays an **In Progress** status in the list.
    * Monitor the status until completion.

    <figure><img src="../../../../.gitbook/assets/28 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
23. #### Abort Job Execution

    * If needed, click **Stop (Abort)** under Actions.
    * A confirmation displays to cancel the run.

    <figure><img src="../../../../.gitbook/assets/29 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
24. #### Run Job Completion (Screen 30)

    * Once completed, the job reflects a **final execution status** (e.g., Success/Failed).
    * Review status before proceeding with further validation or data checks.

    <figure><img src="../../../../.gitbook/assets/30 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
25. **Access Job Results (Screen 30.1)**

    * Under Actions for a job, select **Job Results**.

    <figure><img src="../../../../.gitbook/assets/30.1 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
26. **Open Validation / Workflow Rules (Screen 33)**

    * Click on the **VR/WFR** icon beside the object.

    <figure><img src="../../../../.gitbook/assets/33 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
27. **View Workflow/Validation Rules (Screen 34)**

    * The **Validation / Workflow Rules** panel opens.
    * Review Validation Rules under **Name, Previous State, Current State, Enable, Error (if any)**.
    * Switch to the **Workflow Rules** tab.
    * Validate existing Workflow Rules or confirm that none are displayed.

    <figure><img src="../../../../.gitbook/assets/34 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
28. **Edit Object Mapping (Screen 36)**

    * Select the **Mappings** icon to open **Edit Mapping**.
    * Review source and destination fields.
    * Use **Auto Map** to match fields automatically, or manually map unmapped fields.
    * Click **Save** to update mappings.

    <figure><img src="../../../../.gitbook/assets/35 - Test Environment Setup (1).png" alt=""><figcaption></figcaption></figure>
29. **View Job Run Results – Success (Screen 37)**

    * Under **Results of Last Run**, click the **Success count** icon.
    * A list of records with **Destination IDs** and **Status: Item Created** is displayed.

    <figure><img src="../../../../.gitbook/assets/35 - Test Environment Setup (2).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/36 - Test Environment Setup (2).png" alt=""><figcaption></figcaption></figure>
30. **View Job Run Results – Failure (Screen 38)**

    * Under **Results of Last Run**, click the **Failure count** icon.
    * A list of failed records with **Source IDs** and corresponding **Error Messages** is displayed.

    <figure><img src="../../../../.gitbook/assets/38 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/39 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
31. #### Search by Job Name (Screen 40)

    * Use the **Job name** field to locate specific jobs quickly.
    * Begin typing the job name to see filtered results update automatically.

    <figure><img src="../../../../.gitbook/assets/40 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
32. #### Filter by Status (Screen 41)

    * Open the **Status** dropdown to refine job listings.
    * Observe the available options to set the right filter criteria.

    <figure><img src="../../../../.gitbook/assets/41 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
33. #### Apply Advanced Filters (Screen 42)

    * Click **Filters** to apply additional criteria.
    * Choose filters such as:
      * **Category**
      * **Destination Org**
      * **Created Date Range**
    * Click **Apply** to filter or **Reset** to clear all selections.

    <figure><img src="../../../../.gitbook/assets/42 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
34. #### Manage Columns (Screen 43)

    * Click **Columns** to customize the table view.
    * Additional columns can be included in the view by selecting the desired options from the **Columns** menu. Columns that are not relevant can be deselected to keep the view focused on essential information.

    <figure><img src="../../../../.gitbook/assets/43 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
35. #### Job Actions – Menu Options (Screen 44)

    * Open the **⋮ (More)** menu next to any job to perform actions.
    * Available options include:
      * **Run**
      * **Edit**
      * **Clone**
      * **Delete**

    <figure><img src="../../../../.gitbook/assets/44 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
36. #### Running a Job
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
37. #### Monitoring Job Execution

    * During execution, the job’s _Status_ column updates to show the current progress.
    * Options available while the job is running:
      * **View** – Inspect job configuration or progress.
      * **Stop** – Terminate the execution if necessary.
    * Once completed, the status reflects success, failure, or warnings.

    <figure><img src="../../../../.gitbook/assets/47 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
38. #### Cloning a Job

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
39. Open Bulk Actions (Screen 49.1)

    * Click the **Bulk Actions** (three-line) icon at the top-right of the **Test Environment** list.

    <figure><img src="../../../../.gitbook/assets/49.1 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
40. Bulk Actions Menu (Screen 49.2)

    * Review available actions:
      * **Run** (disabled for bulk in this view)
      * **Edit** – bulk update job groups
      * **Clone** – clone multiple jobs at once
      * **Delete** – remove multiple jobs

    <figure><img src="../../../../.gitbook/assets/49.1.11 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
41. Start Bulk Edit (Screen 50)

    * From **Bulk Actions**, click **Edit** to open the bulk group editor.

    <figure><img src="../../../../.gitbook/assets/49.2 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/49.3 - Test Environment Setup.png" alt=""><figcaption></figcaption></figure>
42. Bulk Edit Job Groups (Screen 49.3)
    * Use the **Edit Job Group – All** dialog to update the **Category** (group) for many jobs at once.
    * Optional: use **Search** to filter the list; navigate with **Previous/Next** or the page size selector.
    * Click **Save** to apply group changes, or **Cancel** to discard.
43. Start Bulk Clone (Screen 51)
    * From **Bulk Actions**, click **Clone** to open the bulk clone setup.
44. Configure Bulk Clone (Screen 52)
    * In **Clone – All**:
      * **Group name** (required) – Enter the target group for the new copies.
      * **Destination Sandbox** (required) – Choose where all selected jobs will be cloned.
    * Click **Clone** to create the copies, or **Cancel** to exit.
45. Start Bulk Delete (Screen 53)
    * From **Bulk Actions**, click **Delete** to open the selection panel.
46. Select Jobs to Delete (Screen 54)
    * In **Category: All**, select individual jobs or use the header checkbox to select all.
    * Click **Delete** to permanently remove the selected jobs, or **Cancel** to keep them.





























### Test Environment Setup: Overview <a href="#test-environment-setup-overview" id="test-environment-setup-overview"></a>

The test environment in ARM supports convenient data transfer from CSV files to destination sandboxes and helps reduce job execution time. This is particularly useful for validating data migration scenarios prior to full execution.

***

### Create a New Test Environment Setup <a href="#create-a-new-test-environment-setup" id="create-a-new-test-environment-setup"></a>

1. Navigate to the **Dataloader** module and select **Data Loader Test Environment Setup**.

<figure><img src="../../../../.gitbook/assets/image (1116).png" alt="Navigation to Data Loader Test Environment Setup module" width="332"><figcaption></figcaption></figure>

2. Click on **Create New Job**.

<figure><img src="../../../../.gitbook/assets/image (1117).png" alt="Button to initiate a new test environment job"><figcaption></figcaption></figure>

3. Select your **Destination Org**.

<figure><img src="../../../../.gitbook/assets/image (1118).png" alt="Dropdown to select destination Salesforce org"><figcaption></figcaption></figure>

4. Click **Login and Fetch Objects** to display all objects from the destination org.
5. Choose a **Master Object** from the list.

<figure><img src="../../../../.gitbook/assets/image (1119).png" alt="Master object selection screen"><figcaption></figcaption></figure>

6. Click the **Show Dependencies** icon to view hierarchical relationships with parent objects.

<figure><img src="../../../../.gitbook/assets/image (1120).png" alt="Dependency analysis button for the selected object"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1121).png" alt="Text-based dependency relationship view" width="342"><figcaption></figcaption></figure>

7. Use **Switch to Graph View** to see a visual hierarchy.

<figure><img src="../../../../.gitbook/assets/image (1122).png" alt="Graphical representation of object dependencies" width="395"><figcaption></figcaption></figure>

8. Under **Source of Data**, upload a `.zip` file containing the object-specific `.csv` files.

<figure><img src="../../../../.gitbook/assets/image (1123).png" alt="Upload interface for CSV zip files"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** The `.csv` file name must match the object’s API name. Uploading CSVs for parent objects is optional, but required if you want their records migrated too.
{% endhint %}

9. Provide a **Name** for the job and choose a **Job Group** to categorize it.
10. The **Master Object** and **External ID** will auto-populate.
11. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (1124).png" alt="Test environment setup form with master object details"><figcaption></figcaption></figure>

12. You’ll be redirected to the **Test Environment Setup Summary** page.
13. Click **Run** to initiate the data migration job.

<figure><img src="../../../../.gitbook/assets/image (1126).png" alt="Job summary page showing list of configurations and run option"><figcaption></figcaption></figure>

***

### Deployment Criteria Options

| Configurations               | Descriptions                                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disable Workflows**        | Temporarily disables Salesforce workflows during migration, and re-enables them afterward.                                                                                                                                 |
| **Disable Validation Rules** | Turns off validation rules to allow data migration. Rules are restored once the migration is complete.                                                                                                                     |
| **Use Bulk API**             | Uses Salesforce Bulk API to increase performance for large data volumes. Jobs can be processed in **serial** (one after another) or **parallel** (simultaneously). For faster data throughput, parallel mode is preferred. |

<figure><img src="../../../../.gitbook/assets/image (1127).png" alt="UI for selecting workflow, validation, and Bulk API options" width="473"><figcaption></figcaption></figure>

14. Click **Run** to execute the job.

***

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (1128).png" alt="Action menu with edit, delete, clone, and log options"><figcaption></figcaption></figure>

1. **Edit:** Modify job settings.
2. **Delete:** Remove a job setup.
3. **Clone:** Create a duplicate of the configuration.
4. **Log:** View execution history and status.

***

### Schema (Grid View) <a href="#schema-grid-view" id="schema-grid-view"></a>

This section visualizes the master object schema and its dependencies. When validation or workflow rules are disabled, ARM displays these rules under the **VR/WFR** section. You can review and re-enable them manually if necessary.

<figure><img src="../../../../.gitbook/assets/image (1129).png" alt="Grid view showing object schema and relationship"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1130).png" alt="Section listing validation and workflow rules for review"><figcaption></figcaption></figure>
