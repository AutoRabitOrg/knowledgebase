# Archival Configuration for your Salesforce Org

### Overview <a href="#overview" id="overview"></a>

Data archives can be thought of as a data repository for infrequently accessed, but still readily available data. In Vault, data archival is all about moving the unwanted data components from your Salesforce Org and freeing the space for new data. This data is safely stored for future use. In a nutshell, [Vault](https://www.autorabit.com/products/vault-enterprise-backup-and-recovery/) makes Salesforce data archiving and backup simple, productive, and a joy to use.&#x20;

### Procedure <a href="#procedure" id="procedure"></a>

1. Login to your Vault account.
2. Go to **Setup** and search for the [Salesforce Org](https://knowledgebase.autorabit.com/docs/salesforce-org-managements) from which the data has to be archived. You can use the **Search** filter to easily filter out the required Salesforce Org.

<figure><img src="../../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

3. Select the desired Salesforce Org.
4. The next step is to create Archival Config, navigate to the **Configs** tab, and click on **Add Archival Config**. This will allow you to view all the components available in your Salesforce Org and choose the components for which you want to define the archival policy.

<figure><img src="../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

5. Select the components that you need to archive on the next screen.

<figure><img src="../../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

6. Using **Filter** you can define the criteria on which the records will get fetched.\
   **For ex-** If you can define criteria to fetch Case records that are older than 1000 days and are in the closed state Validate your query to see whether the criteria set is correct and view the number of records that will be fetched. You can even set the record count limit for your data being fetched. Click on **Apply** to set the criteria and close the Filter dialog box. For easy identification of objects on which filter is applied, the filter icon is highlighted.

<figure><img src="../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

7. The **Hierarchy** option will allow you to view all the corresponding child objects for your selected object. These child objects will also get archived once you archive their parent object. Such a hierarchy schema view can be seen using the **Hierarchy** option.
   * You may notice in the schema view that some of the objects are auto-selected by default and cannot be unchecked. These are the child objects of its parent object which will be deleted for sure if its parent object is selected for archival policy. However, for other objects which are related to the selected object in some other way, you may have the option to choose them manually for archival.

<figure><img src="../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

8. Once done, click **Save** to close the hierarchy-schema screen. Similar to Filter criteria addition, the hierarchy icon gets highlighted corresponding to the object for which hierarchy is selected.

<figure><img src="../../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

9.  Click **Next.** On the next screen, do the following:

    * Give the process a **name**.
    * Select the **email notification** checkbox to receive an email notification whenever the objects are getting deleted from your Salesforce Org. If unchecked, data will be automatically deleted without any prior notification.
    * Select the date and time interval for the archival process to run under the **Schedule Archival** section. You can set the policy to run either daily, weekly, monthly, or input any duration manually.
    * You can specify to what time period you want to retain the archived data under the **Archival Retention period** section.
    * Specify the **batch size** for components to retrieve records. 10K is the max batch size that you can set per batch. This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
    * **Enable serial mode for Bulk API:** Serial mode processes batch one at a time, however, it can increase the processing time for a load.&#x20;

    <figure><img src="../../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>
10. Click **Save Config**.
11. A summary of all the objects, filters, and criteria selected or applied will get displayed before your archival policy gets configured. Click **Save**.

<figure><img src="../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

12. Now go to the **Archival** tab.
13. Select your [**Salesforce Org**](https://knowledgebase.autorabit.com/docs/org-synchronization) for which you configured the archival recently.&#x20;
14. Select the **Environment**.
15. Select the archival configured recently under **Configurations** drop-down field.

<figure><img src="../../.gitbook/assets/image (289).png" alt=""><figcaption></figcaption></figure>

16. Click on **Get Details** to etch all the existing archival configured for your Salesforce Org. If you've initiated the archival process for the first time in Vault, you will not find any details on this page.
17. To run on-demand archival before the scheduled archival set, use **Archive Now** button.

<figure><img src="../../.gitbook/assets/image (290).png" alt=""><figcaption></figcaption></figure>

18. On the **Start Archival** screen, the label name gets auto-populated, however, you have the option to edit the label name and enter the label you desire.
19. Select your configuration and click **Archive**.

<figure><img src="../../.gitbook/assets/image (291).png" alt=""><figcaption></figcaption></figure>

20. &#x20;You'll be redirected to the **Archival** screen to view the status of the ongoing archival process being run (under the In-progress tab).

<figure><img src="../../.gitbook/assets/image (292).png" alt=""><figcaption></figcaption></figure>

21. For each archival job, the following information will get displayed:
    * **Label**: An identification name for each archival performed in Vault
    * **Configuration Name**: Archival configuration name
    * **Date/Time**: The date and time stamp for the archival process took place
    * **Expiry Date**: Till which date the archival job will remain with Vault
    * **Duration**: Time-taken to complete the archival operation
    * **Records**: Total numbers of records archived
    * **API Calls**: Api call duration (in seconds)
    * **Query**: Filter or query that have been used to fetch the records
    * **Data Backup**: Backup type for data components i.e., _Full backup_ or _Incremental backup_
    * **Status**: Status of the archival i.e., completed, in progress or failed
    * **Actions:**
      1. **Summary Report**: View the summary info for the archive performed. The report will contain the list of both success and failed components for the job triggered as shown below.
      2. **View Log**: View the log information for the archival job triggered.
      3. **Download Archival Report**: Specify the email address to receive the downloadable link to allow mentioned users to download the archival report on their local machine.
