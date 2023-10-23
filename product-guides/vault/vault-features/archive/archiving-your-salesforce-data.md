# Archiving your Salesforce Data

1. Login to your Vault account.
2. Go to the **SETUP** module.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656664649682.png" alt="" width="563"><figcaption></figcaption></figure>

3. Look for your Salesforce Org from which the data has to be archived. You can use the **Search** filter to easily filter out the required Salesforce Org.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656664742315.png" alt=""><figcaption></figcaption></figure>

4. Navigate to the **CONFIGS** tab.
5. Click on **ADD ARCHIVE CONFIG**. This will allow you to view all the components available in your Salesforce Org and choose the components for which you want to define the archive policy.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656664983943.png" alt=""><figcaption></figcaption></figure>

6. Select the components that you need to archive on the next screen.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665122391.png" alt=""><figcaption></figcaption></figure>

7. Using **Filters** you can define the criteria on which the records will get fetched.\
   For example, if you can define criteria to fetch **AccountBrand** records that are older than _1000 days_ and are _field Id_ are not empty.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665531839.png" alt="" width="563"><figcaption></figcaption></figure>

Validate your query to see whether the criteria set is correct and view the number of records that will be fetched. You can even set the record count limit for your data being fetched. Click on **Apply** to set the criteria and close the Filter dialog box. For easy identification of objects on which filter is applied, the filter icon is highlighted.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665586871.png" alt=""><figcaption></figcaption></figure>

8.  The **Hierarchy** option will allow you to view all the corresponding child objects for your selected object. These child objects will also get archived once you archive their parent object. Such a hierarchy schema view can be seen using the **Hierarchy** option.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665645256.png" alt=""><figcaption></figcaption></figure>

You may notice in the schema view that some of the objects are auto-selected by default and cannot be unchecked. These are the child objects of its parent object which will be deleted for sure if its parent object is selected for archive policy. However, for other objects which are related to the selected object in some other way, you may have the option to choose them manually for archive.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665706348.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665782294.png" alt="" width="563"><figcaption></figcaption></figure>

9. Once done, click **SAVE** to close the hierarchy-schema screen. Similar to **filter** criteria addition, the hierarchy icon gets highlighted corresponding to the object for which hierarchy is selected.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656665858852.png" alt=""><figcaption></figcaption></figure>

10. Click **NEXT.** On the next screen, do the following:

    1. Give the process a **name**.
    2. Select the **email notification** checkbox to receive an email notification whenever the objects are getting deleted from your Salesforce Org. If unchecked, data will be automatically deleted without any prior notification.
    3. Select the date and time interval for the archive process to run under the **Schedule Archive** section. You can set the policy to run either daily, weekly, monthly, or input any duration manually.
    4. You can specify till what time period you want to retain the archived data under the **Archive retention period** section.
    5. Specify the **batch size** for components to retrieve records. 10K is the max batch size that you can set per batch. This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
    6. **Enable serial mode for Bulk API:** Serial mode processes batch one at a time, however, it can increase the processing time for a load.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666170944.png" alt=""><figcaption></figcaption></figure>
11. Click **SAVE CONFIG**.
12. A summary of all the objects, filters, and criteria selected or applied will get displayed before your archive policy gets configured. Click **SAVE**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666308476.png" alt="" width="563"><figcaption></figcaption></figure>

13. Now go to the **ARCHIVE** tab.
14. Select your [**Salesforce Org**](../../../arm/arm-administration/registration/salesforce-org.md) for which you configured the archive recently.&#x20;
15. Select the **Environment**.
16. Select the archive configured recently under **Configurations** drop-down field.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666620229.png" alt=""><figcaption></figcaption></figure>
17. Click on **GET DETAILS** to fetch all the existing archive configured for your Salesforce Org. If you've initiated the archival process for the first time in Vault, you will not find any details on this page.
18. To run on-demand archive before the scheduled archive set, use **ARCHIVE NOW** button.
19. On the **Start Archive** screen, the label name gets auto-populated, however, you have the option to edit the label name and enter the label you desire.
20. Select your configuration and click **ARCHIVE**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666736135.png" alt="" width="563"><figcaption></figcaption></figure>

21. You'll be redirected to the **Archive** page to view the status of the ongoing archive process being run.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666853532.png" alt="" width="563"><figcaption></figcaption></figure>

22. &#x20;For each archive job, the following information will get displayed:

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656666969029.png" alt="" width="563"><figcaption></figcaption></figure>

| Parameters                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Label<br></p>              | <p>An identification name for each archive performed in Vault<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <p>Configuration Name<br></p> | <p>Archive configuration name<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <p>Date/Time<br></p>          | <p>The date and time stamp for the archive process took place<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <p>Expiry Date<br></p>        | <p>Till which date the archive job will remain with Vault<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <p>Duration<br></p>           | <p>Time-taken to complete the archive operation<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <p>Records<br></p>            | <p>Total numbers of records archived<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <p>API Calls<br></p>          | <p>API call duration (in seconds)<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <p>Query<br></p>              | <p>Filter or query that have been used to fetch the records<br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <p>Data Backup<br></p>        | <p>Backup type for data components i.e., <em>Full backup</em> or <em>Incremental backup</em><br></p>                                                                                                                                                                                                                                                                                                                                                                                                      |
| <p>Status<br></p>             | <p>Status of the archive i.e., <em>completed, in progress, or failed</em><br></p>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <p>Actions<br></p>            | <ol><li><strong>Summary Report</strong>: View the summary info for the archive performed. The report will contain the list of both success and failed components for the job triggered as shown below.</li><li><strong>View Log</strong>: View the log information for the archive job triggered.</li><li><strong>Download Archival Report</strong>: Specify the email address to receive the downloadable link to allow mentioned users to download the archive report on their local machine.</li></ol> |
