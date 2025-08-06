# Archive

## About Data Archive <a href="#about-data-archive" id="about-data-archive"></a>

Data archives can be thought of as a data repository for infrequently accessed, but still readily available data. In [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/), data archive is all about moving the unwanted data components from your Salesforce Org and freeing up the space for new data. This data is safely stored for future use. In a nutshell, Vault makes archiving [Salesforce data](https://www.autorabit.com/blog/how-to-backup-salesforce-data/) and backup simple, productive, and intuitive.

## Why Is Archival Important? <a href="#why-is-the-archival-important" id="why-is-the-archival-important"></a>

1. It's necessary for optimizing data storage in Salesforce.
2. For [Salesforce Org](../../configuring-vault/registering-salesforce-org/) with lots of data, searching for particular data is time-consuming and difficult.
3. Application building in the Salesforce platform tends to run slower if unwanted data is available in your org.

## Archival Job Status and Notification Settings

### **Overview**

This article explains how to understand an archival job’s **"Ready to Archive"** status and guides enabling notifications before deleting records in Salesforce. Ensuring these settings are correctly configured is essential to avoid accidental data loss and track your archival jobs' status.

### **Understanding the "Ready to Archive" Status**

The **"Ready to Archive"** status indicates that an archival job has been created but has not yet begun processing or archiving data from Salesforce. This means the job is **prepared** to archive the data, but no records have been moved or deleted.

#### Key Points:

* **"Ready to Archive"** means the job is queued for processing but hasn't started archiving any records.
* The job **waits** for the conditions to be met or manual intervention to begin archiving.

### **Notification Before Deleting Records**

To prevent accidental data loss, it is crucial to be notified before any records are deleted from Salesforce during the archival process. This can be controlled through the **"Notify before deleting records in Salesforce"** setting in the archival configuration.

### **How to Enable Archival Notifications**

1. Go to the **Salesforce Orgs list** in Setup.
2. Select the respective **Salesforce Org** where the archival configuration is created.
3. Navigate to the **Configs** > **Archive** tab to review the archival configurations.
4. Click the **Edit** button on any existing **Archival Configuration** to modify the settings.
5. Ensure the checkbox for the **“Notify before deleting records in Salesforce”** checkbox is checked.
6. When enabled, this setting will send notifications to users before any records are permanently deleted, ensuring that you have full awareness before data is removed.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Why This Matters:**

* This feature acts as a **safeguard** to prevent unintentional deletion of critical records.
* It allows you to review and confirm the actions being taken, helping ensure that essential data is not lost in the archival process.

By following these steps and ensuring proper configuration, you can safely manage your archival jobs and prevent accidental data loss.
