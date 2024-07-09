# Setup backup configuration for Salesforce Org

### Overview <a href="#overview" id="overview"></a>

Setting a backup configuration allows you to create a snapshot of the data/metadata from your Salesforce org and retrieves the data required to restore successfully. You can determine which backup method (full backup or Incremental backup) best suits the needs of your business. A _full backup_ is precisely what the name implies: A full copy of your entire data/metadata set. _Incremental backups_ only back up the data that has changed since the previous backup.&#x20;

In addition to choosing the right backup type, you can also **schedule the backup process** for _daily_, _weekly_, or _monthly intervals_.

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* A Salesforce Org registered successfully with Vault. \[[Learn More](https://knowledgebase.autorabit.com/vault/docs/registering-salesforce-org)]

### How to set up a backup configuration for your Salesforce Org? <a href="#how-to-set-up-a-backup-configuration-for-your-salesforce-org" id="how-to-set-up-a-backup-configuration-for-your-salesforce-org"></a>

When you register a new Salesforce Org with Vault, you will automatically navigate to the **`Configs`** tab, where you can add backup configuration(s) for your Salesforce Org. If not, navigate to **`Setup`**, select your Salesforce Org, go to the **`Configs`** tab, and select **`Add Backup Config`** box.

1.  A popup will be displayed asking you to choose the criteria for your configuration type:

    * **`Metadata and data excluding special objects:`** This will fetch the entire metadata/data objects from your Salesforce org excluding special objects. Special objects include system objects, history objects, audit logs, KAV objects, etc.
    * **`Special objects like history, system, audit logs, and KAV objects:`** This option will list only the special objects available in your Salesforce Org.

    <figure><img src="../../../../.gitbook/assets/image (202).png" alt=""><figcaption></figcaption></figure>
2. Based on the option you choose, the following screen will display the list of objects from your Salesforce Org.\
   **Example:** If you choose the first option, i.e., **`Metadata and data excluding special objects`**, the following screen (Metadata) will display the entire metadata types from your [Salesforce Org](https://knowledgebase.autorabit.com/docs/salesforce-org). You can select or deselect the metadata types that will be part of the backup configuration on this screen.&#x20;
3. Click **`Next`** to go to the **`Data`** tab.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt=""><figcaption></figcaption></figure>

4. For the **`Data`** objects, [Vault](https://www.autorabit.com/blog/whats-new-with-autorabit-vault-march-2021-release-21-1/) has a provision to filter the records to prevent unwanted objects from being backed up. You can either opt for including associated objects for your data objects or filter the data objects that are included with the timestamp.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

5. **Viewing Individual Data object:** Click on the individual object to view its related members on the next screen. Also, you can perform various operations on the members' fields, such as excluding them from getting back up. **For example**, if you want to exclude members for the **`Account`** data type, click on the **`Account`** object.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

6. On the next screen, select the **`Account`** object metadata members to include in the backup. Click **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="" width="563"><figcaption></figcaption></figure>

7. This will redirect you to the previous screen, where you can view the changes that have recently been made.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

8. You can even exclude the entire object's members by selecting the **`Excluded Formula Fields`** checkbox.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

9. To filter the label name for each data object, use the **`Filter`** icon. Based on the rule(s) assigned, the results are filtered.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="" width="563"><figcaption></figcaption></figure>

10. The **`Record Count Limit`** field will limit the number of records extracted from the data object. Click **`Validate`** to verify whether the filter applied is correct and view the total number of records to be retrieved.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321914149.png" alt="" width="563"><figcaption></figcaption></figure>

11. Click **`Apply`** to initiate the filter and close the filter dialog box.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt=""><figcaption></figcaption></figure>

12. Click **`Next`** to proceed to the **`Scheduling`** screen.&#x20;

#### Scheduling Backup <a href="#scheduling-backup" id="scheduling-backup"></a>

Once you are done with selecting metadata types and objects (and their fields), set up when you would like to carry out the **Org Backup** operation.

<figure><img src="../../../../.gitbook/assets/image (211).png" alt="" width="563"><figcaption></figcaption></figure>

1. Enter a **`name`** for the backup configuration.&#x20;
2. Give a short description in the **`Description`** field.
3.  Click on the gear icon (located after the _**`Backup Type`**_ text) to go to the **`Backup Settings`** page where you can configure how the backup is triggered.

    * For **`Data`** objects, you can **`enable Bulk API`** toggle box. The Bulk API is based on REST principles, and you can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. When you run a bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing better overall data throughput.&#x20;

    <figure><img src="../../../../.gitbook/assets/image (212).png" alt="" width="376"><figcaption></figcaption></figure>

    * For **`Metadata`** types, specify the batch size for both the profile and remaining components to retrieve records. The max batch is **10,000** records. This option helps run large jobs that exceed normal processing limits. Per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of **40MB**. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is your best solution.

    <figure><img src="../../../../.gitbook/assets/image (213).png" alt="" width="371"><figcaption></figcaption></figure>
4. Choose the **`Backup Type`** for both _metadata_ and _data_ members.
   * **`Full-Backup:`** Full backup is a method of backup in which all the files and folders selected are backed up.
   * **`Incremental-Backup:`** An incremental backup operation will copy only the data/metadata that has been changed since the last backup operation. The modified time stamp on files is typically used and compared to the timestamp of the previous backup.
5. Click on the **`email notification`**<img src="../../../../.gitbook/assets/image (68) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">icon to select users from the list who will receive an email notification whenever the objects are backed up from your Salesforce Org.

<figure><img src="../../../../.gitbook/assets/image (214).png" alt="" width="563"><figcaption></figcaption></figure>

6. Keep the **`"Allow multiple backups to run in parallel"`** toggle to **`Yes`**. If you turn it off, the backup jobs will run sequentially, meaning that only the subsequent scheduled job will be initiated after one is finished. Additionally, deactivating this option will prevent the scheduled jobs from running concurrently with earlier scheduled backups that haven't finished. The backup status will indicate the **`"stopped"`**status of the recently scheduled jobs if the previously scheduled jobs are not completed.

<figure><img src="../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

7. Next, choose the **`frequency`** for backup, i.e., _daily_, _weekly_, _monthly_, or any _specific interval_. If you want the schedule of the backup process to run every **4 hours**, select the **`Specific`** option and indicate the time frame as **4 hours**.

<figure><img src="../../../../.gitbook/assets/image (216).png" alt="" width="511"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (217).png" alt="" width="560"><figcaption></figcaption></figure>

8. You can specify until what period you want to retain the backed-up data under the **`Backup Retention period`** field.
9. Click **`Save Config`**.
10. The next screen will display the summary list of metadata and data members selected for your salesforce and how the backup will be carried out.

<figure><img src="../../../../.gitbook/assets/image (218).png" alt="" width="563"><figcaption></figcaption></figure>

11. Click **`Save`**. A confirmation message will display that the backup is successfully configured for your Salesforce org.
12. Next, you will be redirected to the **`Configs`** screen, where your newly added backup config will display on top of the backup config list.&#x20;
13. &#x20;**Additional options**:
    * **`Schedule`**: You can temporarily enable or disable the backup schedule of a Salesforce org by sliding the **`Schedule`** icon to either the right or left side.
    * **`Backup Config Details`**: View the list of metadata/data members of Salesforce org that will be backed up based on the process scheduled.
    * **`Actions (Edit/Delete)`**: Delete the backup scheduled using the **`Delete`** icon or update the metadata/data components from being backed up using the **`Edit`** icon.
    * **`Last Backup Status`**: Last backup activity status will be displayed in this section.
