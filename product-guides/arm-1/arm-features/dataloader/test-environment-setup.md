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
