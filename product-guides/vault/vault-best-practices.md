# Vault Best Practices

## Understanding Salesforce Backup and Recovery: Challenges, Best Practices, and Effective Strategies <a href="#title-text" id="title-text"></a>

### **Introduction**

Salesforce, a highly customizable and dynamic CRM platform, presents unique challenges in data backup and recovery. Unlike traditional SQL databases, Salesforce does not offer straightforward methods to export and restore entire datasets, making full recovery of data nearly impossible under current constraints. This document aims to elucidate the challenges, best practices, and effective strategies for Salesforce data backup and recovery.

### **Shared Responsibility for Data Security**

Salesforce operates on a shared responsibility model, where users must take active steps to ensure data safety. The platform provides minimal tools to prevent data loss and facilitate restoration, requiring users to leverage external solutions and strategies to manage backups effectively.

### **Challenges in Salesforce Data Backup and Recovery**

1. **Governor Limits**: Salesforce imposes strict governor limits, including maximum API callouts and batch processing constraints. These limits significantly impact the ability to perform comprehensive backups and restores, often requiring careful planning and execution to avoid hitting these thresholds. For example, an enterprise attempting to back up or restore a large volume of data may find that they quickly exhaust their daily API call limits, leading to incomplete backups.
2. **Lack of Full Data Export Options**: Unlike traditional databases, Salesforce does not allow users to easily export and re-import entire datasets. This limitation complicates full data recovery, as incremental and selective backups become necessary. Organizations often need to develop custom scripts or use third-party tools to extract data, which can be both time-consuming and error-prone.
3. **Customization and Complexity**: Salesforce's flexibility allows extensive customization, resulting in unique environments for each organization. This diversity makes it challenging to implement a one-size-fits-all backup and recovery solution. Custom scripts and tailored approaches are often needed to accommodate specific organizational needs. For instance, a company with highly customized Salesforce objects and workflows may find that generic backup solutions fail to capture all necessary data and metadata.
4. **Triggers and Other Process Automation**: Salesforce allows many kinds of process automation to occur when records are inserted, deleted, or updated in Salesforce. This process automation takes time to run. That time may be insignificant for individual record updates but can cause substantial delays when writing large volumes of data. It is critical for customers to architect their applications in such a way that this automation **does not execute** when doing large data loads such as restores or replications.
5. **Constraints of Managed Packages**: Managed packages within Salesforce come with their own set of limitations, further complicating backup and recovery processes. Operations within these packages can be slow and cumbersome, adding another layer of complexity to data management. For example, attempting to back up data from a managed package that has stringent data access controls can lead to incomplete or failed backups.

## Best Practices for Salesforce Disaster Recovery Using Vault <a href="#title-text" id="title-text"></a>

Salesforce is a mission-critical system for many organizations, making disaster recovery a top priority. Establishing a clear Recovery Time Objective (RTO) and Recovery Point Objective (RPO) is essential to ensure business continuity in case of data corruption or system downtime. This guide outlines best practices for designing a disaster recovery strategy using AutoRABIT Vault, drawing on real-world experience with Salesforce environments.

### Challenges in Salesforce Restores <a href="#challenges-in-salesforce-restores" id="challenges-in-salesforce-restores"></a>

When organizations attempt a full restore of Salesforce data to assess RTO and RPO, they often face the following challenges:

* **Salesforce Validations**: Standard Salesforce validations may trigger errors during the restore, causing the process to fail.
* **Governor Limits**: Full restores can run into Salesforce’s governor limits or max API call restrictions, making it difficult to complete the operation.
* **Data Complexity**: The variety of data types in Salesforce adds complexity, as not all types can be restored easily or in the expected format.
* **Infrastructure Overload**: Excessive resource consumption on Vault’s infrastructure may slow down the process, causing jobs to stall or fail.

These challenges can hinder the success of a comprehensive disaster recovery strategy. However, by following a few key best practices, organizations can mitigate these risks and run smooth recovery exercises.

#### Best Practices for Salesforce Disaster Recovery <a href="#best-practices-for-salesforce-disaster-recovery" id="best-practices-for-salesforce-disaster-recovery"></a>

1.  **Identify Critical Salesforce Objects**\
    Start by identifying the Salesforce objects that are critical to maintaining business operations. Not all data needs to be restored immediately in a disaster scenario. Work with internal teams to prioritize objects based on their business impact.

    **Recommendation**: Collaborate with stakeholders to define which objects are crucial for "business-as-usual" operations in case Salesforce is unavailable or the data is corrupted.
2.  **Prioritize Data Within Objects**\
    Within each critical object, not all data carries the same importance. You can improve recovery efficiency by restoring high-priority data first. For instance, you may prioritize records based on when they were created, the accounts they are related to, or other business-specific factors.

    **Recommendation**: Establish a data hierarchy for each object, based on criteria like creation date or key relationships, to streamline the restore process.
3.  **Adopt a Phased Recovery Approach**\
    Rather than restoring all Salesforce data at once, which can lead to long-running jobs and infrastructure bottlenecks, consider a phased recovery approach. Begin by restoring essential data and then proceed with the rest, minimizing pressure on system resources.

    **Recommendation**: Plan for a staggered restoration where the most critical data is restored first, reducing the likelihood of job failures and governor limits.
4.  **Optimize Resource Usage**\
    To prevent Vault’s infrastructure from becoming overloaded during a restore, monitor the resources used by the restore process and adjust accordingly. This will help ensure that jobs complete successfully without stalling.

    **Recommendation**: Set resource usage thresholds and plan restores during off-peak hours when system load is lower.
5.  **Test Recovery Processes Regularly**\
    Regularly test your Salesforce recovery process to validate that RTO and RPO goals are being met. This ensures that your disaster recovery plan remains effective and that any new Salesforce changes are accounted for.

    **Recommendation**: Schedule quarterly recovery tests to stay prepared for disaster scenarios and ensure the RTO and RPO align with organizational requirements.

#### Conclusion <a href="#conclusion" id="conclusion"></a>

By adopting a strategic, phased approach to Salesforce restores and focusing on critical objects and high-priority data, organizations can reduce the risk of restore failures and minimize downtime. Following these best practices will help ensure that your organization’s disaster recovery process is efficient, reliable, and meets RTO and RPO targets.

AutoRABIT Vault, when paired with a thoughtful recovery strategy, can provide the confidence needed to handle Salesforce data recovery and ensure business continuity even during unexpected disruptions.

### **Techniques and Best Practices for Effective Backup and Recovery**

1. **Identify Critical Data and Objects**: AutoRABIT works with customers to determine the critical objects and data essential for business continuity. Establish Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) around these critical elements to ensure prioritized recovery in case of data loss. For example, a financial services company might prioritize backing up customer account data and transaction histories to ensure minimal disruption in case of data loss.
2. **Using Trigger Handlers or Other Means to Disable Automation**: It is important to prevent automated jobs from executing when you are performing restore and replication jobs. While Vault has the ability to disable Triggers and Workflow rules, this is not an efficient way to disable automation since it requires a deployment to the org, which can require test execution, and will disable this automation for ALL users. By contrast, Trigger handlers allow this automation to be disabled only for the user performing the restore jobs. See [this article](https://knowledgebase.autorabit.com/product-guides/vault/vault-best-practices#restore-replicate-best-practices) for more information.
3. **Incremental Testing**: For large datasets, test recovery processes using smaller data chunks before scaling up. This approach helps identify potential issues early and ensures a smoother recovery process when dealing with full datasets. A practical application might involve a retail company testing the recovery of sales data for a single store before attempting to recover data for all locations.
4. **Regular Customization Reviews**: Periodically review and assess the ongoing customizations in the Salesforce environment and their impact on the backup and recovery times. This practice helps identify changes that might complicate the 'restore' process, allowing for timely adjustments to recovery strategies and ensuring RTOs are met. For instance, a healthcare provider could regularly review custom patient data fields to ensure they are included in backup procedures and monitor for the inclusion of a rich text field in such objects, leading to increased time to recover.
5. **Leverage Automated Solutions**: Utilize automated backup and recovery strategies to minimize manual intervention and reduce the risk of human error. For example, scheduling automated daily backups and performing regular automated recovery tests can help ensure that backups are up-to-date and reliable.

## Best Practices for Salesforce Backup and Recovery Using Vault

### General Guidelines on Salesforce Limitations

Metadata API can deploy and retrieve up to 10,000 files or 400 MB at one time. If either of these limits is exceeded, the deployment or retrieval will fail.

See [Vault Archival Best Practices](vault-best-practices.md#archival-best-practices) below.

### **Email Messages Attachment Limitation**

Salesforce has a limitation where files can only be added to Email Messages in the draft state. This presents a challenge when replicating data between organizations (Orgs). We address this issue by implementing the following steps during the replication process:

1. **Draft State Conversion**
   * All Email Messages are replicated in a draft state in the destination Org.
   * This allows for file attachments to be added to the Email Messages.
2. **Email Messages Replication**
   * All existing Email Messages with attachments in the destination Org must be deleted if they are already available in the destination without attachments.
   * Email Messages from the source Org or backup are then replicated to the destination Org.
3. **File Attachment**
   * During the replication process, while the Email Messages are in the draft state, any available files are attached to the Email Messages.  &#x20;
   * Email Messages are changed to the same state as in the backup or source Org, ensuring the data replication is completed successfully.

This structured approach ensures files are properly attached to Email Messages during the data replication process between Orgs using AutoRABIT.

### Backup Best Practices

1. Configure your full backup, which includes all the Objects (standard and custom) in Salesforce org. The recommended frequency is weekly, preferably on the weekend.
2. Configure backup for Special objects like history, system, audit logs, and KAV objects every week. Can be set to a daily basis, if needed.
3. Configure incremental backups to include all the objects in Salesforce. The recommended frequency for this backup is daily.
4. Configure the scheduled time for full and incremental backups with enough of a time gap between them to avoid any bottlenecks in Salesforce, which may be caused due to queries being executed on the same objects in parallel.
5. Create backup schedules that are in sync with your production deployment schedules. Backup your entire production instance or relevant instance data before deploying to a production instance.
6. Identify a set of business-critical objects. Configure a backup specifically to include these objects to run at higher frequency levels (recommended frequency is multiple times a day) depending on RPO and RTO requirements.
7. Use the option to exclude formula fields in case of objects with a large number of fields, without which Salesforce queries may be errored out or give results slowly.
8. Configure email addresses of users who need to be notified upon completion or failure of backups. (By default, the user who configured the backup will be notified automatically).
9. Go through logs and results of backups every week to ensure that automated backups are happening as expected.
10. Adjust frequency and scheduled time of backup configurations based on API call limit and API call consumption by other systems.
11. A Salesforce user with which an org is registered on Vault should have admin-level permissions in the org. The recommendation is to create an admin user separately for Vault.
12. For handling Blob objects (such as attachments and content versions), note that:
    * These objects are typically backed up only once during the first full backup and linked to subsequent backups without requiring actual backup operations
    * Each Blob object requires one API call per file in worst case and five files in best case
    * Schedule the initial full backup over weekends to avoid business disruptions from API call spikes
    * This spike in API calls is expected only for the first full backup of a new org in Vault

### Configuration Best Practices

In this segment, we will go over some important points to note while configuring in Vault.

1. **First Incremental Backup:** It is crucial to note that the first incremental backup you perform will be a full backup. This means that during the initial incremental backup, the entire dataset will be backed up.
2. **Avoid Deleting Configurations:** It is highly recommended not to delete any configurations that you have set up. Deleting a configuration will result in the corresponding backup or archival jobs associated with it becoming inaccessible from Vault.
3. **Limit on Users and Salesforce Orgs:** By default, the total number of users and Salesforce Orgs that you can register in AutoRABIT Vault is set to 10.
4. **Number of Configurations:** AutoRABIT Vault allows you to create a maximum of 20 configurations, including both backup and archival configurations.
5. **Increasing Configuration Count:** If you require more than the default count of 20 configurations, you have the option to contact AutoRABIT. They can assist you in increasing the configuration count to accommodate your specific requirements.

### Restore/ Replicate Best Practices

1. Active validation rules, triggers, process builder, and workflow may lead to restore/replicate failures of certain data or metadata. Make sure to disable these before performing restore/replicate operations.
2. We strongly urge everyone to implement frameworks such as Trigger Handlers that allow you to disable automation (Triggers, Flows, Workflow Rules, etc.) for certain users or at certain times. Salesforce offers brief [guidance on this on Trailhead](https://trailhead.salesforce.com/content/learn/modules/success-cloud-coding-conventions/implement-frameworks-sc), and there are multiple Trigger Handler patterns available such as the [Apex Trigger Actions Framework](https://github.com/mitchspano/apex-trigger-actions-framework). Data restore jobs generally do not need to re-process that business automation. By bypassing this automation you can reduce time to write data to Salesforce by 10x or more.
3. Metadata API can deploy and retrieve up to 10,000 files or 400 MB at one time. If either of these limits is exceeded, the deployment or retrieval will fail. Make sure the metadata size is less than 400MB for a single job. You can split the metadata into multiple jobs to achieve restore/replicate if metadata is larger than 400 MB.
4. Define batch size based on the size of metadata or data you want to perform jobs on.
5. Make sure record owners are active on Salesforce, as Restore/Replicate will fail for inactive owners. If activating owners is not an option, you can enable [‘Set Audit](https://help.salesforce.com/articleView?id=000227663\&type=1) [Fields and Update Records with Inactive Owners’](https://help.salesforce.com/articleView?id=000227663\&type=1) on Salesforce.



### Archival Best Practices

* Archiving parent objects will result in the deletion of all the child objects related through mandatory lookups and master-detail relationships recursively as it is an expected behavior of Salesforce. For the children related through a lookup (which is not mandatory), the reference to the parent will be removed from the child object before performing deletion of the parent.
* Ensure that only one object is chosen for archival at a time in an org to avoid issues with row locks and interdependencies during the deletion of the records from Salesforce.
* Always select the option to ‘Notify before deleting data from Salesforce’ to avoid auto-deletion of the records without consent and review of the records that are going to be deleted as part of the job.
* Use limit and offset or an auto-increment field on the object to chunk the data for deletion into smaller batches to help understand the impact and strategize the deletion of subsequent batches based on the errors experienced in the initial batches.
* Provide a smaller Bulk API batch size when triggering the archival to avoid errors arising out of Salesforce processing capabilities.
* Run the archival job in serial mode to avoid errors like row locks or any other issues arising out of parallel processing in Salesforce. This is recommended only if you experience errors due to parallel mode as running the job in serial mode will impact the time it takes to execute the job.
* Ensure that options to disable workflows, validation rules, and triggers are enabled during the initiation of the archive job to ensure the deletion of records won’t result in reaching Salesforce processing limitations and allocations.

### Unsupported Components with Metadata API

The following components cannot be retrieved or deployed with Metadata API, and changes to them must be made manually in each of your organizations:

* Account Teams
* Activity Button Overrides
* Auto-number on Customizable Standard Fields
* Calendars
* Campaign Influences
* Case Contact Roles
* Case Feed Layouts
* Case Team Roles
* Console Layouts
* Currency Exchange Rates
* Data Category Visibility Settings
* Delegated Administration
* Divisions
* File Upload and Download Security Settings
* Mail Merge Templates
* Multiline layout fields for contract line items
* Multiline layout fields for opportunity teams
* Offline Briefcase Configurations
* Omni-Channel Queues and Omni-Channel Skills routing types for the LiveChatButton object
* Opportunity Big Deal Alerts
* Opportunity Update Reminders
* Organization Wide Email Addresses
* Partner Management
* Picklists: IdeaTheme.Categories, Opportunity.ForecastCategoryName, and Question.Origin. All other standard picklists are supported.
* Predefined Case Teams
* Quote Templates
* Salesforce to Salesforce
* Self-Service Portal Font and Colors
* Self-Service Portal Users
* Self-Service Public Solutions
* Self-Service Web-to-Case
* Service report templates
* Social Business Rules
* SoftPhone Layout
* Solution Categories
* Solution Settings
* Standard fields that are not customizable, such as auto-number fields or system fields
* Web Links on Person Account Page Layouts
* Web-to-Lead

Reference: [https://developer.salesforce.com/docs/atlas.en-](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_unsupported\_types.htm#%3A\~%3Atext%3DSome%20things%20you%20can%20customize%2CAccount%20Teams) [us.api\_meta.meta/api\_meta/meta\_unsupported\_types.htm#:\~:text=Some%20things%20yo](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_unsupported\_types.htm#%3A\~%3Atext%3DSome%20things%20you%20can%20customize%2CAccount%20Teams) [u%20can%20customize,Account%20Teams](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_unsupported\_types.htm#%3A\~%3Atext%3DSome%20things%20you%20can%20customize%2CAccount%20Teams)



### Managed Package Limitations

For any operation, the extent of a successful backup, restore, or replicate job depends on the permissions associated with the managed package. There is a possibility of failures of a few metadata components for which the package does not provide access. This is a limitation of the managed package and can be addressed by contacting the third-party vendor for required access.
