# Backup Support for Knowledge Articles

Vault introduced the ability to back up Salesforce Knowledge articles as part of the Vault Data backup feature.

During the backup process, these articles are saved under their respective Article Types, with the addition of a suffix **"\_\_kav,"** aligning with Salesforce's classification of Articles. Default Knowledge articles are saved as **knowledge\_\_kav** records.

### Point to Consider <a href="#point-to-consider" id="point-to-consider"></a>

* Ensure that the Knowledge Articles already exist in your Salesforce org.

### Process <a href="#process" id="process"></a>

1. Log in to your Vault account and navigate to the **Setup** module.
2. Select your **Salesforce org** from the list.
3. Go to the **Configs** tab.
4. Click on **Add Backup Config**.
5. Choose the Backup configuration type as **Metadata and data excluding special objects**.
6. Click **OK**.
7. By default, you will be directed to the **Metadata** tab, where the available metadata types in your Salesforce Org are listed. Since we are specifically backing up Knowledge Articles records, deselect all other metadata types by unchecking the **"Metadata Type"** field.
8. Click **Next** to proceed to the **Data** tab.
9. Uncheck the **Object Label Name** field to clear all objects selection.
10. Search for **knowledge** in the **Quick find** box, and select the **Knowledge** object.
11. Click **Next** to proceed to the final screen. On this screen, you need to:
    * Provide a **name** for the backup configuration and add a brief **description**.
    * Select the Backup type as **"None"** for _Metadata_ and choose between **"Full Backup"** or **"Incremental Backup"** for _Data_. The incremental backup option will copy only the data that has changed since the last backup operation.
    * To optimize data loading or delete extensive records asynchronously through parallel processing, enable the **bulk API** feature for your data objects. Click on the **Gear** icon next to the **Backup Type** field and turn on the **"Enable Bulk API"** option.
    * Keep the **"Allow multiple backups to run in parallel"** toggle set to **Yes**.
    * Choose the **frequency** of the backup: daily, weekly, monthly, or a specific interval.
    * Specify the period for retaining the backed-up data using the **Backup Retention period** field.
    * Click **Save Config**.
12. Next, go to the **Backup** module and select your **Salesforce org** configured with Knowledge Articles Versioning (KAV) objects. Click on **Backup Now.**
13. Choose the backup configuration you created earlier from the dropdown, if it's not already auto-selected. Click **Backup**.
14. You will be redirected back to the **Backup Summary** screen, which displays the status of the recently triggered backup.

***

For more details on how to restore or replicate Knowledge Articles, [check this article](restoring-knowledge-articles-with-vault.md).
