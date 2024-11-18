# Start the Backup

### Overview <a href="#overview" id="overview"></a>

Vault for Salesforce data security automatically performs backups for two kinds of structures:&#x20;

* **Data:** Backup data in Salesforce is for records such as accounts, opportunities, contracts, leads, and cases. It also backs up Chatter, files, custom object records, and content.&#x20;
* **Metadata:** Salesforce metadata backup refers to custom code like Apex and Visualforce and configuration settings like dashboards, reports, page layouts, and custom fields.&#x20;

Vault suits the Salesforce environment and is built for our customers to protect their valuable data. Some features of our Salesforce backup tool include:&#x20;

* **Dependable backups:** You can use Vault to back up your important content and recover it if the original file is compromised. Salesforce backup and recovery allows you to maintain the complete experience of Salesforce by preserving file attachments, knowledge feeds, and more.&#x20;
* **Built-in archival:** Vault’s archival capabilities reduce storage costs for a more cost-effective solution. The archive tool is based on our scalable enterprise cloud infrastructure.&#x20;
* **Metadata Mastery™:** Using Metadata Mastery™ with the AutoRABIT platform allows your company to back up and recover your Salesforce environment completely. This tool prevents Salesforce data loss by including metadata in its backups.

### Before you Begin <a href="#before-you-begin" id="before-you-begin"></a>

1. A **Salesforce Org** registered inside Vault. To register a new org, navigate to **`Setup > Register New Org`**. \[[Learn More](../../configuring-vault/registering-salesforce-org/)]
2. A **backup configured** for your Salesforce Org. The backup configuration job creates a snapshot of the data/metadata from your Salesforce org and is also helpful in retrieving the data required to restore successfully. \[[Learn More](../knowledge-articles/ncino/backup-configuration-for-your-salesforce-org.md)]
3. You have **permission** to create a backup job.

### Backing up your Data and Metadata <a href="#backing-up-your-data-and-metadata" id="backing-up-your-data-and-metadata"></a>

1. Login to your Vault account.
2. Go to the **`Backup`** module.
3. Select your **`Salesforce Org`**, **`Environment (Salesforce/nCino),`** and backup **`Configurations`** from the drop-down.Note:
   * A list of all scheduled and manual backups triggered to date will get displayed under the **`Backup Summary`** section.&#x20;
   * To know more about the list of metadata and data being backed up or the configurations set for each backup, you can find it by clicking on the **`Backup Summary`** (<img src="../../../../.gitbook/assets/image (69) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">) icon under the **`Actions`** tab.
4. To initiate a new backup, click on **`Backup Now`**.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. On the next screen:
   * Enter the **`label`** of your choice or leave the auto-generated default label.
   * You'll be prompted to select your backup **configuration** again.
   * Select the **`Backup type`** for both metadata and data members. Vault recommends using the **Full-Backup** for metadata/data when performing a backup for the first time.
     1. **`Full-Backup`**: Full backup is a method of backup in which all the files and folders selected are backed up.
     2. **`Incremental-Backup`**: An incremental backup operation will copy only the data/metadata that has been changed since the last backup operation. The modified time stamp on files is typically used and compared to the timestamp of the previous backup.
6. Select the **`Exclude Deleted Records`** checkbox to exclude the recently deleted records from your environment.
7. Click **`Backup`**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="491"><figcaption></figcaption></figure>

8. You'll be taken to the **`Backup Summary`** screen to display the status of the recently triggered backup activity.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Backup Summary  <a href="#backup-summary" id="backup-summary"></a>

For each backup performed inside Vault, you will find the details below on the **`Backup Summary`** screen.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Label`              | The label name you assigned for your backup activity.Click on the label to find the list of successful/failed metadata and data members that are part of the backup operation. Also, you can **export** to save the restored metadata/data info in CSV format locally.                                                                                                          |
| `Configuration Name` | The configuration name you choose for the backup operation                                                                                                                                                                                                                                                                                                                      |
| `Date/Time`          | Date and time stamp for your backup operation                                                                                                                                                                                                                                                                                                                                   |
| `Expiry Date`        | Backup retention period                                                                                                                                                                                                                                                                                                                                                         |
|                      |                                                                                                                                                                                                                                                                                                                                                                                 |
| `Duration`           | Total time to complete the backup operation                                                                                                                                                                                                                                                                                                                                     |
| `Metadata`           | Total count of metadata objects successfully backed up                                                                                                                                                                                                                                                                                                                          |
| `Records`            | Total count of records successfully backed up                                                                                                                                                                                                                                                                                                                                   |
| `API calls`          | API call duration (in seconds)                                                                                                                                                                                                                                                                                                                                                  |
| `Metadata Backup`    | The backup type you chose for metadata members                                                                                                                                                                                                                                                                                                                                  |
| `Data Backup`        | The backup type you selected for data records                                                                                                                                                                                                                                                                                                                                   |
| `Status`             | Backup status (success, failure, or in progress)                                                                                                                                                                                                                                                                                                                                |
| `Actions`            | <p>Additional actions:</p><ul><li><strong><code>Backup summary</code></strong>: View the backup summary report</li><li><strong><code>Log</code></strong>: Find the log details for your backup operation</li><li><strong><code>Abort</code></strong>: For an ongoing backup, you can abort the process in between using the <strong><code>Abort</code></strong> icon.</li></ul> |
