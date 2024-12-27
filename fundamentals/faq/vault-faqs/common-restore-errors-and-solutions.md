# Frequently Asked Questions

## Vault FAQs

### Backup and Compare

#### **Can I delete specific, condition-based data from an existing backup?**

No, if the data is backed up in GCP and AWS, it is not possible to delete data from a field in Vault. If you want to delete it from the Org, you can archive the whole record but not the data for a single field.

#### **Is it possible to mask the existing field/record that is already backed up in GCP?**

It is impossible to mask existing data in a backup, as backups are kept immutable in compliance with General Data Protection Regulation (GDPR) requirements.

#### **If a Salesforce org is decommissioned, will its backup still be available and can it be restored (replicated) to another org?**

1. If the Backup snapshots are available in the storage, i.e., not expired, you can "**Replicate**" them to another org ("Restore" is for the same org, which is not possible if the org is decommissioned).
2. If the configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The Backup will be available in the storage, but it will be in Excel format. Restoring/Replicating, along with the relationships, will be a challenge and must be done manually, which is why we recommend users not delete any configurations unless they are certain they won't be needed in the future.

#### If you delete the backup configuration, will the backup still exist in Vault?

If the backup configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The backup will be available in the storage, but it'll be in Excel format. Restoring/Replicating along with the relationships will be a challenge and must be done manually. That's why we recommend that our customers do not delete any configurations unless they are certain they'll not need them in the future.

#### Where can I find my backup expiration date?

Users can verify the expiry date by reviewing the backup history in Vault. In our application, a column will display the backup's expiration date.

<figure><img src="../../../.gitbook/assets/image (1587).png" alt=""><figcaption></figcaption></figure>

#### Can I migrate data from other Salesforce backup solutions?

All backup solutions will ideally provide an option for users to download their data, which can be uploaded to our storage bucket and connected to our application to reinstate the backups/archives as if they were done through Vault. This is considered a professional service on our end, as there is significant effort involved from us to perform the migration.

#### Where in Vault can I view the attachments that were backed up?

File attachments cannot be viewed from the Vault user interface or in CSV format, as they are encrypted in our S3 storage. The customer must either restore those specific files in their Salesforce Org or Replicate them to another Salesforce Org.

***

### Restore and Replicate

#### Will the Restore operation create a duplicate if a record already exists in Salesforce?

A duplicate will not be created during a Restore operation because detection is achieved via Unique IDs. More details on Unique IDs can be found [here](https://knowledgebase.autorabit.com/product-guides/vault/configuring-vault/registering-salesforce-org/unique-identifier-uid).

#### Can I specify the order in which objects are restored, e.g., users first, then other objects?&#x20;

No, the order of a Restore operation is established by internal logic using data schema.&#x20;

#### Can I determine the number of API calls made during the Restore process, similar to a Backup?

API calls are not currently displayed on the user interface during the Restore process. &#x20;

#### How can I filter backup data by specific dates and use it as the source to Restore/Replicate?

To filter data based on specific dates from a backup using a CSV file and Excel, follow these steps:

1. **Download CSV File**: Download the CSV file corresponding to the object on which the date needs to be filtered from the backup.
2. **Filter Dates Using Excel**: Open the downloaded CSV file in Excel. Use Excel's filtering features to filter out the IDs for which the dates match the required criteria.
3. **Create Final CSV File**: Save the filtered data in a new CSV file. This file should contain only the filtered IDs.
4. **Upload and Filter Backup**: Use the final CSV file with the filtered IDs as the source. In the restore/replicate module, use the file upload option in the filters to filter the backup data accordingly.

### **Data Encryption**

#### **Does Vault encrypt data at rest by default?**

Yes, by default, Vault encrypts data at rest in **Amazon S3 buckets** using **AES-256 encryption**, a highly secure encryption standard.

#### **What is AES-256 encryption, and why is it used?**

AES-256 (Advanced Encryption Standard) is a **powerful encryption algorithm** that ensures data is stored in an unreadable format unless decrypted with the proper key. It is widely recognized for its security and compliance with regulations like GDPR, HIPAA, and PCI-DSS.

#### **Can I disable data encryption at rest?**

No, encryption at rest is enforced by default in Vault and cannot be disabled. This ensures all stored data remains secure, even in the unlikely event of unauthorized access to storage.

#### **Where is encrypted data stored?**

Encrypted data is stored in **Amazon S3 buckets**, part of Amazon Web Services (AWS), which provides secure, scalable, and reliable cloud storage.

***

### **Admin**

#### Does Vault support the Terafina managed packages?

Currently, Vault does not support the Terafina managed package.

#### Does Vault integrate with Salesforce Shield?

Salesforce Shield ensures that data is encrypted at rest within Salesforce. However, when data is queried through APIs, Salesforce returns it in a decrypted format. Since Vault leverages Salesforce APIs to retrieve data, our solution fully supports the backup and restoration of Salesforce orgs where Salesforce Shield is enabled.
