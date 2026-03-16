# Vault-FAQs

## Archival

### What determines whether a child record is mandatory for archival?

AutoRABIT Vault considers a child record mandatory for archival if it meets any of the following criteria:

* It is related to the parent via a [**Master-Detail Relationship**](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#q2-how-does-a-master-detail-relationship-affect-archival).
* It is linked through a [**Lookup Relationship**](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#q3-what-happens-in-a-lookup-relationship-where-the-field-is-required) that is marked as required.
* It is configured for [**Cascade Delete**](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#q4-what-is-cascade-delete-and-how-does-it-impact-archival), meaning it is deleted when the parent is deleted.
* The [**parent record cannot be deleted**](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#q5-what-does-it-mean-when-a-parent-record-is-restricted-from-deletion-due-to-a-child-record) unless the child is removed, necessitating their joint archival.

A Lookup Relationship can also be [configured like](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#q7-can-a-lookup-relationship-be-configured-to-act-like-a-master-detail-relationship) a Master-Detail Relationship.&#x20;

For more information, visit the page on [Parent-Child Archival](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival).

### Are email messages mandatory child records for objects they have a direct relationship with?

Yes, email messages are mandatory child records for those objects with which the email messages have a direct relationship through the fields 'RelatedTold' and 'ParentId'. Refer to the [Email Messages Relationships](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/archive/parent-child-record-archival#email-messages-relationships) section for a full list of objects with which email messages have a direct relationship.&#x20;

### How are backup and archival handled for objects with both parent and child references?

If an object has a reference from another object as both parent and a child record, then the parent will only be considered for a backup but not for archival. The child record will only be considered for archival.&#x20;

## PCI Compliance

### Does Vault adhere to the Payment Card Industry (PCI) Data Security Standards (DSS)?

**PCI DSS** is the global standard for protecting payment data. These security requirements and global access control measures are established by the Payment Card Industry Security Standards Council. Vault ensures the storage and transmission of cardholder data is kept private, safe, and secure.

### How does Vault ensure PCI compliance? <a href="#how-does-vault-ensure-pci-compliance" id="how-does-vault-ensure-pci-compliance"></a>

Vault firewalls, software, data encryption, secure passwords, transmission, and physical access to data storage all serve to protect data security. AutoRABIT performs continual software and security updates, testing to verify compliance. Data access logs are monitored regularly monitored to identify outliers.&#x20;

For more information, refer to our page on [PCI Compliance](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/compliance/pci-dss).&#x20;

***

## Sandbox Refresh vs. Backup and Restore Timing

### How long does it take to perform a sandbox refresh versus a backup and restore?&#x20;

**Sandbox Refresh:** A sandbox refresh creates a full replica of a Salesforce org, including data and metadata, in another sandbox environment. It can take **hours or days**, depending on the org's data and metadata size and complexity. Salesforce limits full-copy sandbox refreshes to once every 29 days.

**Backup and Restore:** Backup and restore processes involve creating backups and restoring specific or full data sets as needed. AutoRABIT Vault uses backups from AWS S3 or Azure Blob Storage for selective or full restoration. The time to perform a backup and restore is typically faster than a sandbox refresh. It also has no Salesforce-imposed frequency limits.

**Replicate RTO (Recovery Time Objective)** estimates depend on:

* Data volume
* Schema complexity
* API availability&#x20;

For specific estimates, contact the product team.

***

## Sandbox Refresh vs Sandbox Seeding

#### Understanding Salesforce Sandbox Refresh Limitations

#### 1.   Overview

In Salesforce environments, maintaining sandbox data aligned with production is critical for development, testing, QA, UAT, and training activities. There are two commonly discussed approaches:

* Sandbox Refresh (Native Salesforce Refresh)
* Data Seeding (Selective Data Replication using Vault)

While these terms are often used interchangeably, they serve very different purposes and operate in fundamentally different ways.

#### 2.   Sandbox Refresh vs Data Seeding

A sandbox refresh is a Salesforce-native process that completely rebuilds a sandbox from Production, overwriting all metadata and data to create a clean, production-aligned baseline. It resets the environment and removes any existing sandbox-specific configurations.

In contrast, data seeding selectively copies specific data (and sometimes metadata) from Production to a sandbox without recreating it. It updates targeted datasets without wiping the environment, making it ideal for keeping sandboxes test-ready between refresh cycles.

Sandbox Refresh = Full Environment Reset Data Seeding = Targeted Data Update

#### 3.   Challenges with Salesforce Sandbox Refresh

While effective for structural alignment, it is a full reset operation that introduces operational, administrative, and agility limitations.

* **Full Environment Overwrite** – Entire sandbox is rebuilt, wiping all existing configurations and test data.
* **Environment Downtime** – Sandbox becomes unavailable during refresh; Full Copy refresh may take hours or days.
* **Limited Refresh Frequency** – Developer (1 day), Partial (5 days), Full Copy (29 days).
* **No Incremental Capability** – Entire environment is replaced even when only minor updates are required.
* **Manual Post-Refresh Activities** – User reactivation, password resets, permission reassignment, integration endpoint updates.
* **Integration Disruption** – Outbound URLs and API integrations require reconfiguration.
* **Inflexible Data Control** – No selective or filtered object-level refresh capability.

These limitations make sandbox refresh suitable for baseline resets but less ideal for continuous DevOps-driven development and testing models.

#### 4.   Vault Replicate: Controlled Data Seeding

Vault’s Replicate module addresses the operational gaps of traditional sandbox refresh by enabling selective, controlled, and incremental data replication between Salesforce environments.

* **Selective Object-Level Replication** – Copy only required objects along with dependencies/ hierarchy.
* **Filtered Data Movement** – Replicate specific datasets (e.g., last 30 days of transactions).
* **Relationship-Aware Data Transfer** – Maintains referential integrity.
* **Incremental Data Updates** – Update sandbox data without full overwrite.
* **On-Demand or Scheduled Execution** – Support agile release cycles.
* **Selective Metadata Replication** – Support controlled configuration alignment.

Vault does not recreate the sandbox. Instead, it enhances sandbox usability by maintaining relevant, test-ready data without requiring a full refresh event.

#### 5.   Salesforce Refresh vs. Vault Replicate

<table><thead><tr><th valign="top">Criteria</th><th valign="top">Salesforce Sandbox Refresh</th><th valign="top">Vault Replicate (Data Seeding)</th></tr></thead><tbody><tr><td valign="top">Scope</td><td valign="top">Entire environment rebuild</td><td valign="top">Selective metadata and data replication</td></tr><tr><td valign="top">Frequency</td><td valign="top">Restricted (Full: 29 days)</td><td valign="top">On-demand / Scheduled</td></tr><tr><td valign="top">Downtime</td><td valign="top">Yes</td><td valign="top">No</td></tr><tr><td valign="top">Data Control</td><td valign="top">Limited</td><td valign="top">Highly granular</td></tr><tr><td valign="top">Incremental</td><td valign="top">No Incremental Updates - Entire</td><td valign="top">Vault Data Seeding</td></tr><tr><td valign="top">Updates</td><td valign="top">sandbox is replaced even for minor data updates.</td><td valign="top">capabilities supports granular incremental updates</td></tr><tr><td valign="top">User Reactivation Required</td><td valign="top">Yes</td><td valign="top">No</td></tr><tr><td valign="top">Integration Reconfiguration</td><td valign="top">Yes. Required (endpoints, APIs, tokens, middleware)</td><td valign="top">Not required</td></tr><tr><td valign="top">Best Use Case</td><td valign="top">Full baseline reset</td><td valign="top">Continuous data alignment</td></tr></tbody></table>

#### 6.   How Vault Overcomes Salesforce Refresh Limitations

* **Avoids Downtime** – Data replication occurs without sandbox recreation.
* **Eliminates 29-Day Dependency** – Data can be updated on demand. There is no need to wait for           the Full Copy refresh window.
* **Preserves In-Progress Testing** – No full environment reset required.
* **Reduces Administrative Overhead** – No need for user reactivation or endpoint reconfiguration.
* **Enables Incremental Testing** – Only required datasets are refreshed.
* **Supports DevOps Agility** – Continuous sandbox readiness.

#### 7.   The AutoRABIT Alternative: ARM + Vault

A traditional sandbox refresh performs two primary functions: metadata synchronization and data synchronization. AutoRABIT provides a modular alternative:

* ARM Org Synchronization - for metadata alignment

Compares metadata between environments, identifies differences, and enables controlled synchronization.

* Vault Replicate - for data alignment

Enables selective, filtered, and incremental data seeding from Production to sandbox environments.

Together, ARM and Vault allow organizations to align metadata and replicate necessary production data without executing a full sandbox refresh.

This approach avoids downtime, eliminates manual post-refresh activities, preserves integrations, and supports continuous DevOps practices.

#### 8.   Important Considerations for Data Seeding Activities

While Vault enables controlled and efficient data seeding, it is important to recognize that all data replication activities ultimately execute within the Salesforce platform. As such, Salesforce governor limits, validation rules, and platform constraints continue to apply during the replication process.

The success of a data seeding operation depends not only on Vault configuration but also on the data hygiene and structural integrity of the target sandbox. Issues such as inactive record owners, invalid IDs, broken relationships, active validation rules, or automation conflicts may result in Salesforce-generated errors during replication.

Organizations are advised to review sandbox data quality, user status, and platform limits prior to initiating large-scale data seeding activities.

#### Metadata Considerations in Vault Replication

Vault is designed to support selective metadata alignment, not full metadata restoration. Its purpose is to ensure that the necessary structural components required for data seeding are in place within the target environment.

For example, when performing a data seeding operation, the primary metadata components that must exist are:

* Object schema
* Field definitions

Vault supports the controlled replication of these required components to ensure that the target sandbox can properly receive and store the replicated data. It is important to note that Vault leverages Salesforce Metadata API capabilities. As a result, it operates within Salesforce platform constraints. Large-scale metadata restorations—such as deployments exceeding approximately 10,000 components or very large metadata package sizes (e.g., beyond platform-supported limits)—are subject to Salesforce API limitations.

In scenarios requiring full org-level metadata restoration or very large metadata deployments, a structured metadata deployment strategy (such as using ARM) is recommended.

#### 9.   Recommended Best Practice

The optimal approach is to start with a sandbox refresh to establish a clean production-aligned baseline. This ensures full metadata and structural consistency.

After the baseline is set, use Vault Replicate to perform periodic incremental data updates. Instead of repeatedly refreshing the sandbox, only new or modified records are synchronized.

This hybrid model reduces downtime, avoids refresh frequency constraints, preserves ongoing testing, and supports continuous DevOps practices.

_It is important to note: Vault is not a replacement for sandbox refresh. Instead, ARM (metadata alignment) combined with Vault (data seeding) provides a controlled alternative when alignment—not full structural reset—is the objective._

***

## Access and Refresh Token Handling

Salesforce automatically manages the life cycle of both **Access Tokens** and **Refresh Tokens**, ensuring secure and uninterrupted connectivity for Vault. Below are the scenarios you may encounter:

#### **Scenario 1: Access Token Expiry**

* The **Access Token** expires based on the duration configured in Salesforce.
* When this happens, Salesforce automatically refreshes the Access Token using the associated **Refresh Token**.
* This process is seamless and requires no user action. Vault operations continue without interruption.

#### **Scenario 2: Refresh Token Expiry**

A **Refresh Token** may expire in the following cases:

1. When the configured expiry period in Salesforce is reached.
2. When the Salesforce Org itself is refreshed.

**What happens next:**

* Once the Refresh Token expires, automatic renewal of Access Tokens is no longer possible.
* Vault prompts the user to **re-authenticate the connected org**.
* After successful re-authentication, Salesforce issues new tokens, and operations resume normally.

***

## Backup and Compare

### Can I delete specific, condition-based data from an existing backup?

No, if the data is backed up in GCP and AWS, it is not possible to delete data from a field in Vault. If you want to delete it from the Org, you can archive the whole record but not the data for a single field.

### Is it possible to mask an existing field/record already backed up in GCP?

It is impossible to mask existing data in a backup, as backups are kept immutable in compliance with General Data Protection Regulation (GDPR) requirements.

### Where can I find my backup expiration date?

Users can verify the expiry date by reviewing the backup history in Vault. In our application, a column will display the backup's expiration date.

<figure><img src="../../../.gitbook/assets/image (1587).png" alt=""><figcaption></figcaption></figure>

### Can I migrate data from other Salesforce backup solutions?

All backup solutions will ideally provide an option for users to download their data, which can be uploaded to our storage bucket and connected to our application to reinstate the backups/archives as if they were done through Vault. This is considered a professional service on our end, as there is significant effort involved from us to perform the migration.

### Where in Vault can I view the attachments that were backed up?

File attachments can be downloaded from the Vault user interface or in CSV format. Refer to [https://knowledgebase.autorabit.com/product-guides/vault/vault-features/backup/start-the-backup#downloading-files](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/backup/start-the-backup#downloading-files) for further details on download options.

### How can I filter backup data by specific dates and use it as the source to Restore/Replicate?

To filter data based on specific dates from a backup using a CSV file and Excel, follow these steps:

1. **Download CSV File**: Download the CSV file corresponding to the object on which the date needs to be filtered from the backup.
2. **Filter Dates Using Excel**: Open the downloaded CSV file in Excel. Use Excel's filtering features to filter out the IDs for which the dates match the required criteria.
3. **Create Final CSV File**: Save the filtered data in a new CSV file. This file should contain only the filtered IDs.
4. **Upload and Filter Backup**: Use the final CSV file with the filtered IDs as the source. In the restore/replicate module, use the file upload option in the filters to filter the backup data accordingly.

### If I delete the backup configuration, will the backup still exist in Vault?

If the backup configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The backup will be available in the storage, but it'll be in Excel format. Restoring/Replicating along with the relationships will be a challenge and must be done manually. That's why we recommend users do not delete any configurations unless they are certain they will not be needed in the future.

### If a Salesforce org is decommissioned, will its backup still be available and can I Replicate it to another org?

1. If the Backup snapshots are available in the storage, i.e., not expired, you can **Replicate** them to another org (Restore is for the same org, which is not possible if the org is decommissioned).
2. If the configuration is deleted, all its related backup snapshots are also deleted from the Vault UI. The Backup will be available in the storage, but it will be in Excel format. Restoring/Replicating, along with the relationships, will be a challenge and must be done manually, which is why we recommend users not delete any configurations unless they are certain they won't be needed in the future.

### How can I identify who triggered a specific backup?

1. Navigate to the backup section.
2. Select the relevant Salesforce org and configuration.
3. Navigate to the "Backup Label" which includes the required date.
4. Download the logs.

The logs will contain information about who initiated the backup (starting).

### How do I download backups?

1. Select the Backup mode and choose your Salesforce Org.&#x20;
2. Locate the backup you want.&#x20;
3. Upon clicking the “Download” icon, you will receive a confirmation email containing a download link.
4. By following this link, you can conveniently view the backup's data size in your browser and proceed to download it to your computer.

### Where can I find the backup after it expires in Vault?

Once a backup has reached its expiration, it will move to lower tier storage, such as Glacier. The backup will stay there for a month after this, and then it will be permanently deleted. During the time it stays in Glacier, we can retrieve it with the help of SRO and share to customer if required.

### Content Version Large File Processing

1. **What is the enhancement?**\
   Vault now supports processing **ContentVersion files up to 2 GB**, compared to the earlier limit of 10 MB.
2. **Is this feature enabled by default?**\
   No. This capability is **controlled by a feature flag** and must be explicitly enabled.
3. **Is there any performance impact?**\
   Yes. Large ContentVersion files are processed **one-by-one**, which may result in slower processing times. This is an expected trade-off to ensure reliable handling of large files.
4. **Who should enable this feature?**\
   This feature is recommended for customers who need to process large content files and can accommodate the additional processing time.

***

## Restore and Replicate

### Will the Restore operation create a duplicate if a record already exists in Salesforce?

A duplicate will not be created during a Restore operation because detection is achieved via Unique IDs. More details on Unique IDs can be found [here](https://knowledgebase.autorabit.com/product-guides/vault/configuring-vault/registering-salesforce-org/unique-identifier-uid).

### Can I specify the order in which objects are restored, e.g., users first, then other objects?&#x20;

No, the order of a Restore operation is established by internal logic using data schema.&#x20;

### Can I determine the number of API calls made during the Restore process, similar to a Backup?

API calls are not currently displayed on the user interface during the Restore process. &#x20;

### Handling Existing Parent Records

During **Restore** or **Replicate** operations, the system checks whether parent records already exist in the destination org. If a parent record is found to be already present, the system skips migrating that record to prevent duplicate creation.

The skipped parent record is recorded as an **error entry in the result file**, clearly indicating that the record was ignored because it already exists in the destination. All other eligible records continue to be processed without interruption, ensuring the overall operation completes as expected.

### Can AccountTeamMember Be Inserted with an Inactive User? (Vault Context)

**Q: Will Salesforce allow inserting AccountTeamMember records with an inactive user during Vault restore?**

**Answer:**\
No. Salesforce does **not** allow inserting an `AccountTeamMember` record if the referenced `UserId` is inactive.

#### Why?

The `AccountTeamMember` object requires:

* A valid **AccountId**
* An **active UserId**
* A Team Role

If the user referenced in the backup is:

* Deactivated, or
* No longer present in the org

Salesforce will reject the insert operation and throw an error (commonly `INVALID_CROSS_REFERENCE_KEY` or a user-related validation error).

***

## **Data Encryption**

### **Does Vault encrypt data at rest by default?**

Yes, by default, Vault encrypts data at rest in **Amazon S3 buckets** using **AES-256 encryption**, a highly secure encryption standard.

### **What is AES-256 encryption, and why is it used?**

AES-256 (Advanced Encryption Standard) is a **powerful encryption algorithm** that ensures data is stored in an unreadable format unless decrypted with the proper key. It is widely recognized for its security and compliance with regulations like GDPR, HIPAA, and PCI-DSS.

### **Can I disable data encryption at rest?**

No, encryption at rest is enforced by default in Vault and cannot be disabled. This ensures all stored data remains secure, even in the unlikely event of unauthorized access to storage.

### **Where is encrypted data stored?**

Encrypted data is stored in **Amazon S3 buckets**, part of Amazon Web Services (AWS), which provides secure, scalable, and reliable cloud storage.

***

## **Admin**

### Does Vault support the Terafina managed packages?

Currently, Vault does not support the Terafina managed package.

### Does Vault integrate with Salesforce Shield?

Salesforce Shield ensures that data is encrypted at rest within Salesforce. However, when data is queried through APIs, Salesforce returns it in a decrypted format. Since Vault leverages Salesforce APIs to retrieve data, our solution fully supports the backup and restoration of Salesforce orgs where Salesforce Shield is enabled.

***

## Data Migration to Vault

#### **1. Should I retain existing backup snapshots after moving to Vault?**

Yes. It is strongly recommended to retain your existing backup snapshots for at least **3 months**. This buffer allows for coverage in the event of immediate Salesforce failures or restoration needs.

#### **2. Why is the 3-month retention period suggested?**

The 3-month period provides sufficient time to:

* Capture multiple snapshots of both full and incremental changes in Vault.
* Ensure data reliability in Vault moving forward.
* Account for variations in data and file size across orgs.

#### **3. What happens if we were using an archival feature with our previous provider?**

If you previously used an **archival feature**, check whether you utilized any **"unarchive" functionality within Salesforce**:

* **If you did use unarchiving**: Vault currently does **not** support this functionality. A ticketing system or custom implementation may be necessary if unarchiving is a critical requirement.
* **If unarchiving wasn’t used**: You can rely on Vault's archival features and proceed to delete your old archival history after ensuring everything you need is archived properly in Vault.

#### **4. How long should I keep archival history with the previous provider?**

A **90-day period** is typically adequate. During this time:

* Vault can archive the required data.
* You can verify the completeness of archived information before decommissioning the older archive history.

#### **5. What precautions should I take before deleting old archives?**

Before removing archived data from your previous solution:

* Conduct a **thorough analysis** of your existing archive.
* Confirm whether any data within the legacy archive might require restoration.
* Any restoration needs during the 90-day transition must be handled via the legacy system.

#### **6. Is this a full migration of backups and snapshots into Vault?**

No. This process does **not** involve migrating historical snapshots into Vault. Instead:

* The focus is on setting up Vault to capture ongoing backups and archives.
* This reduces engineering effort and complexity while ensuring data continuity.

