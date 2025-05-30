# Archiving Your Salesforce Data

1. Log in to your Vault account.
2.  Go to the **Setup** module.\


    <figure><img src="../../../../.gitbook/assets/image (1624).png" alt=""><figcaption><p>Records</p></figcaption></figure>
3.  Locate the Salesforce Org for which the data has to be archived. You can use the **Search** filter to easily find the required Salesforce Org.

    <figure><img src="../../../../.gitbook/assets/image (1610).png" alt=""><figcaption><p>Search for Salesforce Org</p></figcaption></figure>
4. Navigate to the **Configs** tab.
5.  Click on **Add Archive Config**. This will allow you to view all the components available in your Salesforce Org and choose the components for which you want to define the archive policy.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1).png" alt=""><figcaption><p>Add Archive Config</p></figcaption></figure>
6.  Select the components that you need to archive on the next screen.

    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>Select components</p></figcaption></figure>
7.  Using **Filters,** you can define the criteria for which the records will get fetched. For example, you can define criteria to fetch **AccountBrand** records that are older than _1,000 days_ and _field Id_ is not empty.\


    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1).png" alt=""><figcaption><p>AccountBrand-Filter</p></figcaption></figure>

Validate your query to see whether the criteria set is correct and view the number of records that will be fetched. You can even set the record count limit for your data being fetched. Click on **Apply** to set the criteria and close the Filter dialog box. To easily identify the objects for which the filter is applied, the filter icon is highlighted.

<figure><img src="../../../../.gitbook/assets/image (232).png" alt="" width="563"><figcaption><p>Filter</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (233).png" alt=""><figcaption><p>Filters</p></figcaption></figure>

8.  The **Hierarchy** option will allow you to view all the corresponding child objects for your selected object. These child objects will also get archived once you archive their parent object. Such a hierarchy schema view can be seen using the **Hierarchy** option.

    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption><p>Hierarchy</p></figcaption></figure>

    You may notice in the schema view that some of the objects are auto-selected by default and cannot be unchecked. These are the child objects of its parent object, which will be deleted if the parent object is selected for archival per policy. However, for other objects that are related to the selected object in some other way, you may have the option to choose them manually for archival. Visit the Mandatory Child Archival page for more information.

    <figure><img src="../../../../.gitbook/assets/image (1612).png" alt=""><figcaption><p>Schema</p></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (1613).png" alt=""><figcaption><p>Child Schema</p></figcaption></figure>
9.  Once done, click **Save** to close the hierarchy-schema screen. Similar to **filter** criteria addition, the hierarchy icon gets highlighted corresponding to the object for which hierarchy is selected.\


    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
10. Click **Next.** On the next screen, do the following:
    * Give the process a **name**.
    * Select the **email notification** checkbox to receive an email notification whenever the objects are getting deleted from your Salesforce Org. If unchecked, data will be automatically deleted without any prior notification.
    * Select the date and time interval for the archive process to run under the **Schedule Archive** section. You can set the policy to run either daily, weekly, monthly, or input any duration manually.
    * You can specify till what time period you want to retain the archived data under the **Archive retention period** section.
    * Specify the **batch size** for components to retrieve records. 10K is the max batch size that you can set per batch. This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
    *   **Enable serial mode for Bulk API:** Serial mode processes batch one at a time, however, it can increase the processing time for a load.

        <figure><img src="../../../../.gitbook/assets/image (1614).png" alt=""><figcaption><p>Enable serial mode for bulk API</p></figcaption></figure>
11. Click **Save Config**.
12. A summary of all the objects, filters, and criteria selected or applied will get displayed before your archive policy gets configured. Click **Save**.

    <figure><img src="../../../../.gitbook/assets/image (1620).png" alt=""><figcaption><p>Save Config Details</p></figcaption></figure>
13. Now go to the **Archive** tab.
14. Select your [**Salesforce Org**](../../../arm/arm-administration/registration/salesforce-org/) for which you configured the archive recently.&#x20;
15. Select the **Environment**.
16. Select the archive configured recently under **Configurations** drop-down field.

    <figure><img src="../../../../.gitbook/assets/image (1616).png" alt=""><figcaption><p>Archive Settings</p></figcaption></figure>
17. Click on **Get Details** to fetch all the existing archive configured for your Salesforce Org. If you've initiated the archival process for the first time in Vault, you will not find any details on this page.
18. To run on-demand archive before the scheduled archive set, use **Archive Now** button.
19. On the **Start Archive** screen, the label name gets auto-populated, however, you have the option to edit the label name and enter the label you desire.
20. &#x20;Select your configuration and click **Archive**.

    <figure><img src="../../../../.gitbook/assets/image (1617).png" alt=""><figcaption><p>Start Archive</p></figcaption></figure>
21. You'll be redirected to the **Archive** page to view the status of the ongoing archive process being run.

    <figure><img src="../../../../.gitbook/assets/image (1618).png" alt=""><figcaption><p>View Status</p></figcaption></figure>
22. &#x20;For each archive job, the following information will be displayed:

    <figure><img src="../../../../.gitbook/assets/image (1619).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="226">Parameters</th><th>Description</th></tr></thead><tbody><tr><td>Label<br></td><td>An identification name for each archive performed in Vault<br></td></tr><tr><td>Configuration Name<br></td><td>Archive configuration name<br></td></tr><tr><td>Date/Time<br></td><td>The date and time stamp for the archive process took place<br></td></tr><tr><td>Expiry Date<br></td><td>Till which date the archive job will remain with Vault<br></td></tr><tr><td>Duration<br></td><td>Time-taken to complete the archive operation<br></td></tr><tr><td>Records<br></td><td>Total numbers of records archived<br></td></tr><tr><td>API Calls<br></td><td>API call duration (in seconds)<br></td></tr><tr><td>Query<br></td><td>Filter or query that have been used to fetch the records<br></td></tr><tr><td>Data Backup<br></td><td>Backup type for data components i.e., <em>Full backup</em> or <em>Incremental backup</em><br></td></tr><tr><td>Status<br></td><td>Status of the archive i.e., <em>completed, in progress, or failed</em><br></td></tr><tr><td>Actions<br></td><td><ol><li><strong>Summary Report</strong>: View the summary info for the archive performed. The report will contain the list of both success and failed components for the job triggered as shown below.</li><li><strong>View Log</strong>: View the log information for the archive job triggered.</li><li><strong>Download Archival Report</strong>: Specify the email address to receive the downloadable link to allow mentioned users to download the archive report on their local machine.</li></ol></td></tr></tbody></table>

## Downloading Files

**Steps to download files:**

1. Go to the “Files” tab of any archive summary.
2.  Click to open the “Records” icon on the files tab to download the files.\


    <figure><img src="../../../../.gitbook/assets/image (1625).png" alt=""><figcaption><p>Records</p></figcaption></figure>
3.  The records window will have the “Download” and “Download Files” options to initiate the download of files.

    <figure><img src="../../../../.gitbook/assets/image (1621).png" alt=""><figcaption><p>Downloads</p></figcaption></figure>
4.  On clicking download, the following pop-up will be displayed with two options to download.

    <figure><img src="../../../../.gitbook/assets/image (1623).png" alt=""><figcaption><p>Download Options</p></figcaption></figure>

    * Selecting "Download CSV" will download a CSV file with all the records.
    * Selecting "Download Files" allows you to download the file from the Vault backup.
5. &#x20;As soon as "Download Files" is initiated:
   1.  A message will be displayed. Click "Ok" to continue.

       <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (2).png" alt=""><figcaption><p>User Message</p></figcaption></figure>
   2.  The download progress can be observed with the progress bar that replaces the “Download” button.

       <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption><p>Download</p></figcaption></figure>
   3. Once the download is completed, an email based on the actual state of the download will be triggered to the registered emails in Vault.
   4. For downloading individual files, click on the download icon under the "Download Files" column.

## Limitations

* Inconsistent File Download During GDPR Requests: When a GDPR request is initiated within an organization, file downloads may behave inconsistently. This issue will be resolved in the upcoming release.
* File Download Issues with Special Characters in File Names: Files with special characters in their names may not function properly in certain environments, particularly on macOS. This issue will be addressed in the upcoming release.
