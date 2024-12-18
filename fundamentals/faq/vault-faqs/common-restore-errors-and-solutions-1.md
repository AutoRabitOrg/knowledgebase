# Frequently Asked Questions

## Vault FAQs

### Restore / Replicate

#### How can I filter backup data by specific dates and use it as the source to Restore/Replicate?

To filter data based on specific dates from a backup using a CSV file and Excel, follow these steps:

1. **Download CSV File**: Download the CSV file corresponding to the object on which the date needs to be filtered from the backup.
2. **Filter Dates Using Excel**: Open the downloaded CSV file in Excel. Use Excel's filtering features to filter out the IDs for which the dates match the required criteria.
3. **Create Final CSV File**: Save the filtered data in a new CSV file. This file should contain only the filtered IDs.
4. **Upload and Filter Backup**: Use the final CSV file with the filtered IDs as the source. In the restore/replicate module, use the file upload option in the filters to filter the backup data accordingly.

#### **Condition-Based Data Deletion from Existing Backup**

1. If the data is backed up in GCP and AWS, it is not possible to delete it with Vault.
2. If you want to delete from the Org, it is not possible to delete just a field from Vault—you can archive the whole record but not the data for a single field.

#### **Is it possible to mask the existing field/record that is already backed up in GCP?**

It is impossible to mask existing data in a backup, as backups are kept immutable in compliance with General Data Protection Regulation (GDPR) requirements.

#### **If a Salesforce org is decommissioned, will its backup still be available and can it be restored (replicated) to another org?**

1. If the Backup snapshots are available in the storage, i.e., not expired, you can "**Replicate**" them to another org ("Restore" is for the same org, which is not possible if the org is decommissioned).
2. If the configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The Backup will be available in the storage, but it will be in Excel format. Restoring/Replicating, along with the relationships, will be a challenge and must be done manually, which is why we recommend users not delete any configurations unless they are certain they won't be needed in the future.

#### If you delete the backup configuration, will the backup still exist in Vault?

If the backup configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The backup will be available in the storage, but it'll be in Excel format. Restoring/Replicating along with the relationships will be a challenge and must be done manually. That's why we recommend that our customers do not delete any configurations unless they are certain they'll not need them in the future.

***

### Backup + Compare

#### Where can I find my backup expiration date?

Users can verify the expiry date by reviewing the backup history in Vault. In our application, a column will display the backup's expiration date.

<figure><img src="../../../.gitbook/assets/image (1587).png" alt=""><figcaption></figcaption></figure>

***

### **Data Encryption**

#### **Does Vault encrypt data at rest by default?**

Yes, by default, Vault encrypts data at rest in **Amazon S3 buckets** using **AES-256 encryption**, a highly secure encryption standard.

#### **What is AES-256 encryption, and why is it used?**

AES-256 (Advanced Encryption Standard) is a **powerful encryption algorithm** that ensures data is stored in an unreadable format unless decrypted with the proper key. It is widely recognized for its security and compliance with regulations like GDPR, HIPAA, and PCI-DSS.

#### **Can I disable data encryption at rest?**

No, encryption at rest is enforced by default in Vault and cannot be disabled. This ensures all stored data remains secure, even in the unlikely event of unauthorized access to storage.

#### **Where is encrypted data stored?**

Encrypted data is stored in **Amazon S3 buckets**, part of Amazon Web Services (AWS), which provides secure, scalable, and reliable cloud storage.
