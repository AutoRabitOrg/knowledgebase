# Start the Backup

### Overview <a href="#overview" id="overview"></a>

Vault for Salesforce data security automatically performs backups for two kinds of structures:

* **Data:** Backup data in Salesforce is for records such as accounts, opportunities, contracts, leads, and cases. It also backs up Chatter, files, custom object records, and content.
* **Metadata:** Salesforce metadata backup refers to custom code like Apex and Visualforce and configuration settings like dashboards, reports, page layouts, and custom fields.

Vault suits the Salesforce environment and is built for our customers to protect their valuable data. Some features of our Salesforce backup tool include:

* **Dependable backups:** You can use Vault to back up your important content and recover it if the original file is compromised. Salesforce backup and recovery allows you to maintain the complete experience of Salesforce by preserving file attachments, knowledge feeds, and more.
* **Built-in archival:** Vault’s archival capabilities reduce storage costs for a more cost-effective solution. The archive tool is based on our scalable enterprise cloud infrastructure.
* **Metadata Mastery™:** Using Metadata Mastery™ with the AutoRABIT platform allows your company to back up and recover your Salesforce environment completely. This tool prevents Salesforce data loss by including metadata in its backups.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

1. A **Salesforce Org** registered inside Vault. To register a new org, navigate to **`Setup > Register New Org`**. \[[Learn More](../../configuring-vault/registering-salesforce-org/)]
2. A **backup configured** for your Salesforce Org. The backup configuration job creates a snapshot of the data/metadata from your Salesforce org and is also helpful in retrieving the data required to restore successfully. \[[Learn More](../../ncino/backup-configuration-for-your-salesforce-org.md)]
3. You have **permission** to create a backup job.

### Backing Up Your Data and Metadata <a href="#backing-up-your-data-and-metadata" id="backing-up-your-data-and-metadata"></a>

1. Login to your Vault account.
2. Go to the **`Backup`** module.
3. Select your **`Salesforce Org`**, **`Environment (Salesforce/nCino),`** and backup **`Configurations`** from the drop-down.Note:
   * A list of all scheduled and manual backups triggered to date will get displayed under the **`Backup Summary`** section.
   * To know more about the list of metadata and data being backed up or the configurations set for each backup, you can find it by clicking on the **`Backup Summary`** (<img src="../../../../.gitbook/assets/image (69) (1) (1) (1) (1) (1) (1).png" alt="" data-size="line">) icon under the **`Actions`** tab.
4. To initiate a new backup, click on **`Backup Now`**.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Backup Now</p></figcaption></figure>

5. On the next screen:
   * Enter the **`label`** of your choice or leave the auto-generated default label.
   * You'll be prompted to select your backup **configuration** again.
   * Select the **`Backup type`** for both metadata and data members. Vault recommends using the **Full-Backup** for metadata/data when performing a backup for the first time.
     1. **`Full-Backup`**: Full backup is a method of backup in which all the files and folders selected are backed up.
     2. **`Incremental-Backup`**: This method backs up only the data or metadata that has changed since the last backup operation. Vault allows incremental backups at intervals as short as every 5 minutes. Incremental backups identify changes by comparing file modification timestamps against the timestamp of the previous backup.
6. Select the **`Exclude Deleted Records`** checkbox to exclude the recently deleted records from your environment.
7. Click **`Backup`**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)  (14).png" alt="" width="491"><figcaption><p>Start Backup</p></figcaption></figure>

8. You'll be taken to the **`Backup Summary`** screen to display the status of the recently triggered backup activity.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Backup Summary</p></figcaption></figure>

### Backup Summary <a href="#backup-summary" id="backup-summary"></a>

For each backup performed inside Vault, you will find the details below on the **`Backup Summary`** screen.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Backup Summary Screen</p></figcaption></figure>

| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Label`              | The label name you assigned for your backup activity. Click on the label to find the list of successful/failed metadata and data members that are part of the backup operation. Also, you can **export** to save the restored metadata/data info in CSV format locally.                                                                                                         |
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

### Downloading Files

Having this feature to download the files from the backup will enable the user to download the files directly from the Vault backup of the actual Salesforce data.

Steps to download files:

1\. Open the backup summary and navigate to the ‘files’ tab to download the files from the backup.

2\. Click on the “Download” option to initiate the download of the files.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. A pop-up will be displayed with two options to choose from:

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**a. Download CSV:**

i. The following “Selecting this option will download the records without the actual files” can be observed in the info icon.

ii. On selecting this option, the CSV with records file will be downloaded.

**b. Download Files:**

i. The following “Selecting this option will download the actual files from the storage” can be observed in the info icon.

ii. On selecting “Download Files”, based on the size of the file, the progress icon will be displayed in the place of download option.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1).png" alt=""><figcaption><p>Download Files</p></figcaption></figure>

iii. Once the download is concluded, based on the actual state of the download, emails with different statues will be triggered to the registered emails in the vault environment.

7. Once “Download Files” is initiated, the progress of the files download is depicted through the progress icon. Following screenshot is for reference.
8. On hovering over the in-progress download, the count(downloaded files/total files count) of files can be observed.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>In Progress Downloads</p></figcaption></figure>

9. Once the download is concluded, based on the actual state of the download, emails with different statues will be triggered to the registered emails in the vault environment.
10. Using the “Download Files” column. The individual files related to the respective records can be downloaded.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Download Files</p></figcaption></figure>

## Filter & Download Records

The new provision is useful in filtering the “backed up” and archived records. The available records can be filtered through various options provisioned on the application.

**Step-By-Step Guide:**

Follow the following flow for the backup records download:

1. Go to the backup module of the Vault application
2. Click on the “Label Name” to open the backup details
3.  On landing on the backup details section, click on the “Records”

    <figure><img src="../../../../.gitbook/assets/image (1744).png" alt=""><figcaption></figcaption></figure>
4. On opening the backup “Records”, observe the “Downloads” option.
5.  The download has three values in the drop-down

    a.    Download All Records

    b.    Download Records On Screen

    c.     Download Filtered Results

    <figure><img src="../../../../.gitbook/assets/image (1745).png" alt=""><figcaption></figcaption></figure>
6. **Download All Records**: Selecting this option will download all the backed up records
7.  **Download Record On Screen**: Selecting this option will download all the records available on that current page

    <figure><img src="../../../../.gitbook/assets/image (1746).png" alt=""><figcaption></figcaption></figure>
8.  **Download Filtered Records**: Selecting this option will download the records filtered

    <figure><img src="../../../../.gitbook/assets/image (1747).png" alt=""><figcaption></figcaption></figure>

## Limitations

* Inconsistent File Download During GDPR Requests: When a GDPR request is initiated within an organization, file downloads may behave inconsistently. This issue will be resolved in the upcoming release.
* File Download Issues with Special Characters in File Names: Files with special characters in their names may not function properly in certain environments, particularly on macOS. This issue will be addressed in the upcoming release
