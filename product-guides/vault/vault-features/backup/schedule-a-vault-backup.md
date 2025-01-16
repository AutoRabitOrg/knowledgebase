# Schedule a Vault Backup

### Overview <a href="#overview" id="overview"></a>

Vault gives you the possibility of a one-time backup configuration, setting frequency, e.g., every day at 03:00 PM for your Salesforce, and ... that is all you need to have your data/metadata backed up in Vault.&#x20;

### Before you Begin <a href="#before-you-begin" id="before-you-begin"></a>

1. Register your Salesforce Org in Vault. \[[Learn More](../../configuring-vault/registering-salesforce-org/)]

### How to do it? <a href="#how-to-do-it" id="how-to-do-it"></a>

When registering your Salesforce Org in Vault, you must configure the backup and set the backup schedule criteria. You will need to choose the metadata and data records as a part of the backup process before you schedule them. Head to the [Backup Configuration](../../configuring-vault/registering-salesforce-org/setup-backup-configuration-for-salesforce-org.md) article for detailed information on selecting metadata and data records for your Salesforce Org.

When you are done with the metadata/data selection, you will be navigated to the **`Scheduling`** screen, where you are required to fill in the details as follows:

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. Give a **`name`** for the scheduled backup configuration.
2.  Select the **`Backup Type`** for both metadata and data members.

    * **`Full-Backup`**: Full backup is a method of backup in which all the files and folders selected are backed up.
    * **`Incremental-Backup`**: An incremental backup operation will copy only the data/metadata that has been changed since the last backup operation. The modified time stamp on files is typically used and compared to the timestamp of the previous backup.

    <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Click on the <img src="../../../../.gitbook/assets/image (70) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line"> icon to go to the **`Backup Settings`** page.

    * For **`Data`** objects, you can **`enable Bulk API`**. Bulk API is optimized to load or delete extensive records asynchronously due to parallel processing.&#x20;

    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * For **`Metadata`** types, specify the batch size for both profile and remaining components to retrieve records. The max batch is **10,000** records. This option helps run large jobs that exceed normal processing limits. Per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of **40 MB**. You can process records in batches using the batch size to stay within platform limits. If you have a lot of records, processing records through batches is your best solution.

    <figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. Keep the **`"Allow multiple backups to run in parallel"`** toggle to **Yes**. If you turn it off, the backup jobs will run sequentially, meaning that only the next scheduled job will be initiated after one is finished. Additionally, deactivating this option will prevent the scheduled jobs from running concurrently with earlier scheduled backups that haven't finished. The backup status will indicate the **"Stopped"** status for the recently scheduled jobs if the previously scheduled jobs are not completed.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Select the **`email notification`** icon to receive an email notification whenever the objects are backed up from your Salesforce Org.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Next, choose the **`frequency`** for backup, i.e., daily, weekly, monthly, or at any specific interval. If you want the schedule of the backup process to run every 4 hours, select the **`Specific interval`** option and indicate the time frame as 4 hours.

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. You can specify until what period you want to retain the backed-up data under the **`Backup Retention period`** field.
8. Click **`Save Config`**.
9. The next screen will display the summary list of metadata and data members selected for your salesforce and how the backup will be carried out.
   * Click **`Save`**. A confirmation message stating the backup is successfully configured for your Salesforce org will be displayed.

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* You can find the backup configured for your Salesforce Org under the **`Setup > Configs`** tab.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Additional options**:
  1. **`Schedule`**: You can temporarily enable or disable the backup schedule of a Salesforce org by sliding the **`Schedule`** icon to either the right or left side.
  2. **`Backup Config Details`**: View the list of metadata/data members of Salesforce org that will be backed up based on the process scheduled.
  3. **`Actions (Edit/Delete)`**: Delete the backup scheduled using the **`Delete`** icon or update the metadata/data components from being backed up using the **`Edit`** icon.
  4. **`Last Backup Status`**: Last backup activity status will be displayed in this section.
