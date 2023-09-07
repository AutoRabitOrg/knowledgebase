# Replicating Objects between Two Salesforce Orgs

### Overview <a href="#overview" id="overview"></a>

The Replication functionality enables you to replicate objects between two Salesforce org capable of replication. During the replication session, Vault reads the object from the replicated session and initiates the replication from the source to the target org.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

1. Salesforce Org registered with Vault.&#x20;
2. Backup configured for your Salesforce Org. \[[Learn More](../../configuring-vault/registering-salesforce-org/setup-backup-configuration-for-salesforce-org.md)]
3. At least one backup operation is triggered for your Salesforce Org in Vault.

### How to do it? <a href="#how-to-do-it" id="how-to-do-it"></a>

1. Login to your Vault account.
2.  Click on **`Replicate`** from the Vault dashboard page and click on **Replicate Now**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622385859844.png" alt=""><figcaption></figcaption></figure>
3. On the next screen, select your **`Salesforce Org`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622386291490.png" alt=""><figcaption></figcaption></figure>

4. Next, select the **`Destination Org`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622386572891.png" alt=""><figcaption></figcaption></figure>

5.  Next, select the **`Replicate Source`** and its **`configuration`** from the drop-down.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622386708320.png" alt=""><figcaption></figcaption></figure>
6. Based on the **replicate source** and **configuration** selection, the configured list will get displayed.
7.  For **`backup`** as the replicate source, you can select multiple backups for replication. However for **`archival/hierarchical backup`**, you can choose only one from the list.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622389597500.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622389682157.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622389753111.png" alt=""><figcaption></figcaption></figure>

8. Click on either **`EZ Replicate`** or **`Selective Replicate`**.

#### EZ Replicate <a href="#ez-replicate" id="ez-replicate"></a>

Full replication copies everything from the source to the destination, including new, updated, and existing data.

1. Select the **`backups/hierarchical/archival`** to replicate and click on the **`EZ Replicate`** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644319328339.png" alt=""><figcaption></figcaption></figure>

2.  The replicate checklists are displayed on the next pop-up screen, which must be considered before we proceed with the replicate operation. Click **`Got It`** to close the popup.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644319360366.png" alt=""><figcaption></figcaption></figure>
3. On the next screen, you will need to:
   1. Enter the **`Replicate label`** of your choice or leave the auto-generated default label.
   2. Specify the **`Batch Size`** for components to retrieve records. 10K is the max batch size that you can set per batch. This option helps run large jobs exceeding normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40 MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
   3. Choose the recipients from the **`Email notification`** dropdown who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be checked by default.
   4. Next, you can select the criteria for the replicate to get performed:
      * **`Disable Workflows:`** On selection, all the workflows of the Salesforce objects will be deactivated, and the data will be transferred from the source to the destination sandbox. Once the replication is completed, workflows will get activated.
      * **`Disable Validation rules:`** Validation rules verify that the data a user enters in a record meets your specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects will be deactivated, and the data will be transferred from the source to the destination sandbox. Once the replicate is done, validation rules will get activated.
      * **`Enable Serial Mode for Bulk API:`** Serial mode processes batch one at a time; however, it can increase the processing time for a load.
      * **`Disable Triggers:`** When working with data and metadata, you may want to disable triggers you have in place to guarantee a successful replicate operation. _This feature disables Salesforce triggers only.  Any managed package triggers will not be disabled._
4. The list of metadata and data objects replicated will be displayed for the last time before the replicate process begins. You will not have options to select individual objects as it is an entire replicate process.
5. Click **`Replicate Now`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664788732654.png" alt="" width="563"><figcaption></figcaption></figure>

#### Selective Replicate <a href="#selective-replicate" id="selective-replicate"></a>

This option allows you to select specific metadata/data that gets replicated only to the target org.

1.  Select the **backups/archival** to replicate and click the **`Selective Replicate`** button.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644319518069.png" alt=""><figcaption></figcaption></figure>
2. The next screen displays the metadata and data objects that will be replicated. From the list of **Metadata** and **Data** type components, the user needs to select the components (along with their member) that will get replicated.
3.  Under the **`Metadata`** tab, you can choose the metadata members for each metadata type.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644319699635.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644317604473.png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644319768301.png" alt=""><figcaption></figcaption></figure>

4.  On the **`Data`** tab, you additionally have the below configurations:

    1.  **`Schema:`** The **Schema** will allow you to view your selected object's corresponding child objects. With the most recent **Vault 23.1** release, we improved the schema representation by showing one level of the child/parent objects at a time. The tree can now be expanded based on your selection rather than the entire tree, which speeds up the download of the schema data and improves the UI.\


        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1650393728235.png" alt="" width="563"><figcaption></figcaption></figure>



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1650393767769.png" alt="" width="563"><figcaption></figcaption></figure>
5.  You may notice in the schema view that some objects are auto-selected by default and cannot be unchecked. These are the child objects of its parent object, which will be replicated if its parent object is selected. However, for other objects which are related to the selected object in some other way, you may have the option to choose them manually for replication. A warning popup appears when you click the **`Save`** button, stating you must select the appropriate hierarchy for the replicate procedure, or the process will fail. Click **`OK`** to dismiss the popup notification and return to the previous screen.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1650393819383.png" alt=""><figcaption></figcaption></figure>
6.  **`Mappings:`** Map your source fields to your destination fields. Any matching headers from your source fields and your destination fields map automatically.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623319335838.png" alt="" width="563"><figcaption></figcaption></figure>
7. **`Records:`** View the list of records for the object selected. Here, you can choose the records you wish to replicate to the destination org. You also have the option of importing records from a CSV file. To upload the CSV, click the **`Choose File`** button in the top right corner of the screen.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644406975485.png" alt=""><figcaption></figcaption></figure>

8. Next, click on either the **`Next`** or **`Replicate`** button. If you choose **`Next`**, you will be navigated to a new screen where you can add a new masking rule. Data masking refers to changing certain data elements within a data store so that the structure remains similar while the information is changed to protect sensitive information. It ensures that sensitive customer information is unavailable beyond the permitted production environment.&#x20;
9.  However, if you want to skip the masking steps, click **`Replicate`**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644320077236.png" alt=""><figcaption></figcaption></figure>
10. Let's create a masking rule before we conclude the replicate process. To do so, click on **`Next`**. Now, click on the **`New Masking Rule`** button available in the top right corner.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644320249277.png)
11. In the **`Masking Form`** screen, do the following:
    * Select the **`object`** for masking and choose the **`field type`** (string, date, phone, etc.).
    *   Choose the **`Masking Style`**:

        * **`Prefix:`** This option will add the character before the selected field name. For example, if the field value in source org is ABC, and the prefix masking value is kept as 123, then the final field value being deployed will be **123.ABC**
        * **`Suffix:`** This option will add the character after the selected field name. For example, if the field value in source org is ABC, and the suffix masking value is kept as 123, then the final field value being deployed will be **ABC.123**
        * **`Substitution:`** This option will substitute the selected field name with the character you enter in the **Masking Value** field. For example, if the field value in source org is ABC, and the replace masking value is kept as 123, then the final field value being deployed will be **123**
        * **`Random:`** This option helps mask the original value with a random value within a specified range. For example, if the field value in source org is ABC, and the random string length value is set to 7, then the deployed field value would be similar to **15d3aRG.**



        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644320348536.png" alt=""><figcaption></figcaption></figure>
    * Choose the fields for which the masking will be applicable.&#x20;
    * Once done, click on the **`Add`** button.
12. Now, click on the **`Replicate`** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644320927495.png" alt=""><figcaption></figcaption></figure>

13. The following popup screen displays the restore checklists, which must be considered before we continue with the replicate operation. Click on **`Got It`** button to close the popup. &#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644320993651.png" alt=""><figcaption></figcaption></figure>

8. On the next screen, you will need to:
   1. On the next screen, enter the **`Replicate label`** of your choice or leave the auto-generated default label.
   2. Specify the **`batch size`** for components to retrieve records. **10K** is the max batch size that you can set per batch. This option helps run large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to **10,000 files** at once or a max size of **40 MB**. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
   3. Choose the recipients from the **`Email notification`** dropdown who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be checked by default.
   4. Next, you can select the criteria for the replicate to get performed:
      * **`Disable Workflows:`** On selection, all the workflows of the Salesforce objects will be deactivated, and the data will be transferred from the source to the destination sandbox. Once the replication is completed, workflows will get activated.
      * **`Disable Validation rules:`** Validation rules verify that the data a user enters in a record meets your specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects will be deactivated, and the data will be transferred from the source to the destination sandbox. Once the replicate is done, validation rules will get activated.
      * **`Enable Serial Mode for Bulk API:`** Serial mode processes batch one at a time; however, it can increase the processing time for a load.
      * **`Disable Triggers:`** When working with data and metadata, you may want to disable triggers you have in place to guarantee a successful replicate operation. _This feature disables Salesforce triggers only.  Any managed package triggers will not be disabled._
9. Click **`Replicate Now`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664788676131.png" alt="" width="375"><figcaption></figcaption></figure>

16. You will be redirected to the **`Replicate Summary`** homepage, which will show you the progress of the replicate operation recently triggered.
17. Click on the **`Replicate Label`** to view the list of metadata/data being replicated to the org. Click on **`Export`** to locally save the restored metadata/data info in CSV format.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623319458008.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623319471018.png" alt=""><figcaption></figcaption></figure>

### Replicate Summary <a href="#replicate-summary" id="replicate-summary"></a>

For each Replicate activity triggered in Vault, you will find the below details:\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622390757130.png" alt=""><figcaption></figcaption></figure>

| Attribute        | Description                                                                                                                                                                                                                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Label`          | <p>The label name that you have assigned for your restore activity.<br>Click on the label to find the list of successful/failed metadata and data members that are part of the restore operation. Also, you can <strong>export</strong> to save the restored metadata/data info in CSV format locally. </p> |
| `Backup Info`    | Get a snapshot of your restore operation                                                                                                                                                                                                                                                                    |
| `Date/Time`      | Date and time stamp for your restore operation                                                                                                                                                                                                                                                              |
| `Duration`       | Total time taken to complete the restore operation                                                                                                                                                                                                                                                          |
| `MetaSuccess`    | Total count of metadata objects that were successfully restored                                                                                                                                                                                                                                             |
| `MetaFailure`    | Total count of metadata objects that failed to restore                                                                                                                                                                                                                                                      |
| `SuccessRecords` | Total count of data objects that were successfully restored                                                                                                                                                                                                                                                 |
| `FailedRecords`  | Total count of data objects that failed to restore                                                                                                                                                                                                                                                          |
| `Status`         | Restore status (success or failed)                                                                                                                                                                                                                                                                          |
| `Actions`        | Additional actions:**`Restore summary:`** View the restore summary report**`Log:`** Find the log details for your restore operation**`Abort:`** For an ongoing replicate operation, you can abort the process in between using the **`Abort`** icon.                                                        |
