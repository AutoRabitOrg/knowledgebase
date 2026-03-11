# Archiving Your Salesforce Data

1. Log in to your Vault account.
2. Go to the **Setup** module.
3.  Locate the Salesforce Org for which the data has to be archived. You can use the **Search** filter to easily find the required Salesforce Org.

    <figure><img src="../../../../.gitbook/assets/image (1610).png" alt=""><figcaption><p>Search for Salesforce Org</p></figcaption></figure>
4. Navigate to the **Configs** tab.
5.  Click on **Add Archive Config**. This will allow you to view all the components available in your Salesforce Org and choose the components for which you want to define the archive policy.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Add Archive Config</p></figcaption></figure>
6.  Select the components that you need to archive on the next screen.

    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1).png" alt=""><figcaption><p>Select components</p></figcaption></figure>
7.  Using **Filters,** you can define the criteria for which the records will get fetched. For example, you can define criteria to fetch **AccountBrand** records that are older than _1,000 days_ and _field Id_ is not empty.<br>

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>AccountBrand-Filter</p></figcaption></figure>

Validate your query to see whether the criteria set is correct and view the number of records that will be fetched. You can even set the record count limit for your data being fetched. Click on **Apply** to set the criteria and close the Filter dialog box. To easily identify the objects for which the filter is applied, the filter icon is highlighted.

<figure><img src="../../../../.gitbook/assets/image (232).png" alt="" width="563"><figcaption><p>Filter</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (233).png" alt=""><figcaption><p>Filters</p></figcaption></figure>

8.  #### **Schema Viewer**

    The schema viewer feature in Vault provides a structured view of parent and child relationships for Salesforce objects. This capability enables efficient navigation, selection, and dependency management while configuring data operations. Enhanced search controls, visual indicators, and guided navigation improve usability when working with complex object hierarchies.

    1. Accessing Account Hierarchy
       1. From the Edit Configuration screen, objects are displayed in a tabular list under the Data step.
       2.  Selecting the Hierarchy icon corresponding to an object opens the Account Hierarchy view.

           <figure><img src="../../../../.gitbook/assets/image (2345).png" alt=""><figcaption></figcaption></figure>
       3. The hierarchy view opens in a modal window, preserving the current configuration context.
    2. Hierarchy Layout and Navigation
       1. The selected object is displayed as the root node of the hierarchy.
       2.  Child objects are listed beneath the root, reflecting direct and indirect relationships.

           <figure><img src="../../../../.gitbook/assets/image (2346).png" alt=""><figcaption></figcaption></figure>
       3. Expand and collapse controls allow traversal across multiple hierarchy levels.
       4. Each object card displays:
          * Object name
          * Relationship type (Lookup or Master-Detail)
          * Selection checkbox
          * Visual hierarchy connector
    3. Search Functionality within Hierarchy
       1. The search bar is available at the top of the hierarchy view.
       2.  **As typing begins in the search bar:**

           1. Matching objects within the current hierarchy are highlighted.
           2. The info icon is automatically opened the first time typing is initiated.

           <figure><img src="../../../../.gitbook/assets/image (2347).png" alt=""><figcaption></figcaption></figure>
       3. The info icon can be manually reopened at any time by selecting the icon.
    4.  Search Help (Info Icon)

        The Search Help panel explains how search operates within the hierarchy:

        1.  **Typing**

            * Highlights matching objects only within the currently displayed hierarchy.
            * Does not change navigation or hierarchy depth.

            <figure><img src="../../../../.gitbook/assets/image (2349).png" alt=""><figcaption></figcaption></figure>
        2. **Selecting from results**
           * Performs a global hierarchy search.
           * Automatically navigates to the object’s location within the schema tree.
    5.  **Search Direction Options**

        The Search Direction dropdown controls how search results are evaluated:

        1. **Children Only**
           1. Searches only downstream child objects of the current root.
        2. **Parents Only**
           1. Searches only upstream parent objects.
        3.  **Both (Parents & Children)**

            1. Searches across the entire hierarchy path.

            <figure><img src="../../../../.gitbook/assets/image (2351).png" alt=""><figcaption></figcaption></figure>
    6.  If no valid path exists for the selected direction, a contextual message is displayed indicating that the object is not reachable from the current root.

        <figure><img src="../../../../.gitbook/assets/image (2352).png" alt=""><figcaption></figcaption></figure>
    7. **Search Results Feedback**
       1. **A result banner displays:**
          * Number of matches found on the current page.
          * Navigation arrows to move between matches.
       2. **When a match is located successfully:**
          * A confirmation message indicates the object has been found.
          * The hierarchy scrolls automatically to the object’s position.
    8. “Only Matches” Toggle
       1.  The Only Matches toggle is available alongside search results.

           <figure><img src="../../../../.gitbook/assets/image (2354).png" alt=""><figcaption></figcaption></figure>
       2. **When enabled:**
          1. Only objects matching the search criteria are displayed.
          2. Non-relevant hierarchy nodes are temporarily hidden.
       3. **When disabled:**
          1. The full hierarchy view is restored.
    9. Root Object Navigation
       1. The Root option is displayed at the top of the hierarchy view.
       2.  Clicking the Root option redirects the view back to the root object of the hierarchy.

           <figure><img src="../../../../.gitbook/assets/image (2355).png" alt=""><figcaption></figcaption></figure>
       3. This action resets the navigation context without clearing selected objects.
    10. Path and Navigation Indicators
        1.  A breadcrumb-style Path indicator displays the traversal route from the root object to the selected object.

            <figure><img src="../../../../.gitbook/assets/image (2356).png" alt=""><figcaption></figcaption></figure>
        2. A Go Back option allows navigation to the previous hierarchy level.
        3. A Returning to indicator clarifies the navigation context when moving back up the hierarchy.
    11. Object Selection Behaviour
        1. Selecting an object automatically selects dependent objects based on relationship rules.
        2. Objects selected due to dependency are visually marked.
        3. If cascading relationships exist:
           1. A **Cascade Delete** indicator is shown for impacted child objects.
        4. Deselection follows dependency rules to prevent inconsistent configurations.
    12. **Visual Indicators and States**
        1. Highlighted text indicates active search matches.
        2. Color-coded badges differentiate:
           1. Root objects
           2. Selected objects
    13. **Saving Hierarchy Configuration**
        1.  The Save button persists all selections made within the hierarchy view.

            <figure><img src="../../../../.gitbook/assets/image (2358).png" alt=""><figcaption></figcaption></figure>
        2. Validation is performed before saving to ensure dependency consistency.
        3. On successful save, the hierarchy modal closes and returns to the configuration screen.
    14. Key Functional Notes
        * Clicking the Root option always redirects to the root object.
        * The info icon auto-opens only on the first typing interaction and remains manually accessible thereafter.
        * Enabling Only Matches limits results strictly to relevant search outcomes without altering selection state.
    15. **Summary**

        The schema viewer feature in Vault enables precise object selection, dependency awareness, and efficient navigation across complex schemas. Enhanced search controls, guided feedback, and visual indicators ensure clarity, accuracy, and confidence while configuring data operations.
9. Click **Next.** On the next screen, do the following:
   * Give the process a **name**.
   * Select the **email notification** checkbox to receive an email notification whenever the objects are getting deleted from your Salesforce Org. If unchecked, data will be automatically deleted without any prior notification.
   * Select the date and time interval for the archive process to run under the **Schedule Archive** section. You can set the policy to run either daily, weekly, monthly, or input any duration manually.
   * You can specify till what time period you want to retain the archived data under the **Archive retention period** section.
   * Specify the **batch size** for components to retrieve records. 10K is the max batch size that you can set per batch. This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
   *   **Enable serial mode for Bulk API:** Serial mode processes batch one at a time, however, it can increase the processing time for a load.

       <figure><img src="../../../../.gitbook/assets/1.1 - Archive Automation Rules.png" alt=""><figcaption></figcaption></figure>
10. **Disable Automation Rules**
    1.  This provision to disable the automation rules is useful in making sure the automation rules created on various fields in Salesforce will not impact the Archival process midway.

        **Step-By-Step Guide:**

        1.  Set up the configuration for the automation rules at **“Scheduling”** while creating the “Archive Config”.

            <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        2. On selecting the required automation configurations, continue to **“Save Config”**.
        3.  Once saved, the set job configurations can be observed under the **“Archive Config Details”**.

            <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        4.  Clicking the information icon under the **"Archive Config Details"** column opens a pop-up displaying the configuration details associated with the respective archive job. This provides a quick view of the selected archive parameters without navigating away from the main screen.

            <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        5.  Run a job for the created configuration and observe the configuration details reflected on the job

            <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        6. The automation configurations selected during the creation of the _**Archive Config**_ will appear on the _**Start Archive**_ screen in the same state as they were initially defined.
        7. For archive configurations where the **"Notify before deleting records in Salesforce"** option is not selected, the automation settings will still appear on the **Start Archive** page..
        8.  On clicking the **“ARCHIVE NOW”** button, observe the automations to make sure they reflect in the same state of selection during the archive config creation.

            <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        9.  For "**Archive Configs"** with **"Notify before deleting records in Salesforce"** enabled, the automation rule settings will **not** be displayed on the **Start Archive** screen when the **ARCHIVE NOW** button is clicked.

            <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        10. Once the archive job is completed, observe the automation rules details on the _“Job Info”_ section.

            <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        11. Click on the information icon under the “Job Info” section to observe the job automation details configured.

            <figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
        12. Once the archive job is completed, any automations that were temporarily disabled during job creation will be restored to their original state as they were before the job was triggered.
11. Click **Save Config**.
12. A summary of all the objects, filters, and criteria selected or applied will get displayed before your archive policy gets configured. Click **Save**.

    <figure><img src="../../../../.gitbook/assets/image (1620).png" alt=""><figcaption><p>Save Config Details</p></figcaption></figure>
13. Now go to the **Archive** tab.
14. Select your [**Salesforce Org**](/broken/pages/9pLgfInGvztETx4cXCc2) for which you configured the archive recently.&#x20;
15. Select the **Environment**.
16. Select the archive configured recently under **Configurations** drop-down field.

    <figure><img src="../../../../.gitbook/assets/image (1616).png" alt=""><figcaption><p>Archive Settings</p></figcaption></figure>
17. Click on **Get Details** to fetch all the existing archive configured for your Salesforce Org. If you've initiated the archival process for the first time in Vault, you will not find any details on this page.
18. To run on-demand archive before the scheduled archive set, use **Archive Now** button.
19. On the **Start Archive** screen, the label name gets auto-populated; however, you have the option to edit the label name and enter the label you desire.
20. &#x20;Select your configuration and click **Archive**.

    <figure><img src="../../../../.gitbook/assets/image (1617).png" alt=""><figcaption><p>Start Archive</p></figcaption></figure>
21. You'll be redirected to the **Archive** page to view the status of the ongoing archive process being run.

    <figure><img src="../../../../.gitbook/assets/image (1618).png" alt=""><figcaption><p>View Status</p></figcaption></figure>
22. &#x20;For each archive job, the following information will be displayed:

    <figure><img src="../../../../.gitbook/assets/image (1619).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="226">Parameters</th><th>Description</th></tr></thead><tbody><tr><td>Label<br></td><td>An identification name for each archive performed in Vault<br></td></tr><tr><td>Configuration Name<br></td><td>Archive configuration name<br></td></tr><tr><td>Date/Time<br></td><td>The date and time stamp for the archive process took place<br></td></tr><tr><td>Expiry Date<br></td><td>Till which date the archive job will remain with Vault<br></td></tr><tr><td>Duration<br></td><td>Time-taken to complete the archive operation<br></td></tr><tr><td>Records<br></td><td>Total numbers of records archived<br></td></tr><tr><td>API Calls<br></td><td>API call duration (in seconds)<br></td></tr><tr><td>Query<br></td><td>Filter or query that have been used to fetch the records<br></td></tr><tr><td>Data Backup<br></td><td>Backup type for data components i.e., <em>Full backup</em> or <em>Incremental backup</em><br></td></tr><tr><td>Status<br></td><td>Status of the archive i.e., <em>completed, in progress, or failed</em><br></td></tr><tr><td>Actions<br></td><td><ol><li><strong>Summary Report</strong>: View the summary info for the archive performed. The report will contain the list of both success and failed components for the job triggered as shown below.</li><li><strong>View Log</strong>: View the log information for the archive job triggered.</li><li><strong>Download Archival Report</strong>: Specify the email address to receive the downloadable link to allow mentioned users to download the archive report on their local machine.</li></ol></td></tr></tbody></table>

## Filter & Download Records

This provision is useful in filtering the “backed up” and archived records. The available records can be filtered through various options provisioned on the application.

**Step-By-Step Guide:**

1. Follow the following flow for the backup records download:
2. Go to the backup module of the Vault application
3. Click on the “Label Name” to open the backup details
4.  On landing on the backup details section, click on the “Records”

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. On opening the backup “Records”, observe the “Downloads” option.
6.  The download has three values in the drop-down

    1. Download All Records
    2. Download Records On Screen
    3. Download Filtered Results

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. 6\.    Download All Records: Selecting this option will download all the backed up records
8.  7\.    Download Record On Screen: Selecting this option will download all the records available on that current page

    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
9.  Download Filtered Records: Selecting this option will download the records filtered

    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (1743).png" alt=""><figcaption></figcaption></figure>

## Limitations

* Inconsistent File Download During GDPR Requests: When a GDPR request is initiated within an organization, file downloads may behave inconsistently. This issue will be resolved in the upcoming release.
* File Download Issues with Special Characters in File Names: Files with special characters in their names may not function properly in certain environments, particularly on macOS. This issue will be addressed in the upcoming release.
