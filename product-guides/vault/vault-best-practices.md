# Vault Best Practices

## Best Practices for Salesforce backup and recovery using Vault

### General Guidelines on Salesforce Limitations

Metadata API can deploy and retrieve up to 10,000 files or 400 MB at one time. If either of these limits is exceeded, the deployment or retrieval will fail.

See Vault Archival Best Practices

### Backup Best Practices

1. Configure your full backup, which includes all the Objects (standard and custom) in Salesforce org. Recommended frequency is weekly, preferably on the weekend.
2. Configure backup for Special objects like history, system, audit logs, and KAV objects on a weekly basis. Can be set to daily basis, if needed.
3. Configure incremental backups to include all the objects in Salesforce. Recommended frequency for this backup is daily.
4. Configure the scheduled time for full and incremental backups with enough of a time gap between them to avoid any bottlenecks in Salesforce, which may be caused due to queries being executed on same objects in parallel.
5. Create backup schedules that are in sync with your production deployment schedules. Backup your entire production instance or relevant instance data before deploying to a production instance.
6. Identify a set of business-critical objects. Configure a backup specifically to include these objects to run at higher frequency levels (recommended frequency is multiple times a day) depending on RPO and RTO requirements.
7. Use the option to exclude formula fields in case of objects with a large number of fields, without which Salesforce queries may be errored out or giving results slowly.
8. Configure email addresses of users who need to be notified upon completion or failure of backups. (By default, the user who configured the backup will be notified automatically).
9. Go through logs and results of backups on a weekly basis to ensure that automated backups are happening as expected.
10. Adjust frequency and scheduled time of backup configurations based on API call limit and API call consumption by other systems.
11. A Salesforce user with which an org is registered on Vault should have admin-level permissions in the org. Recommendation is to create an admin user separately for Vault.



### Restore/ Replicate Best Practices

1. Active validation rules, triggers, process builder and workflow may lead to restore/replicate failures of certain data or metadata. Make sure to disable these before restore/replicate operations.
2. Metadata API can deploy and retrieve up to 10,000 files or 400 MB at one time. If either of these limits is exceeded, the deployment or retrieval will fail. Make sure the metadata size is less than 400MB for a single job. You can split the metadata into multiple jobs to achieve restore/replicate if metadata is larger than 400 MB.
3. Define batch size based on the size of metadata or data you want to perform jobs on.
4. Make sure record owners are active on Salesforce, as Restore/Replicate will fail for inactive owners. If activating owners is not an option, you can enable [‘Set Audit](https://help.salesforce.com/articleView?id=000227663\&type=1) [Fields and Update Records with Inactive Owners’](https://help.salesforce.com/articleView?id=000227663\&type=1) on Salesforce.



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

&#x20;

1.

### Managed Package Limitations

For any operation, the extent of a successful backup, restore, or replicate job depends on the permissions associated with the managed package. There is a possibility of failures of a few metadata components for which the package does not provide access. This is a limitation from the managed package and can be addressed by contacting the third-party vendor for required access.
