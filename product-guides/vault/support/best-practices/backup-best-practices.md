# Backup Best Practices

This article illustrates many of the key best practices for the backup process on the Vault platform:

1. Configure full backup that includes all the objects (standard and custom) in [Salesforce Org](https://knowledgebase.autorabit.com/docs/salesforce-org). Recommended frequency is weekly, preferably on weekends.
2. Configure a backup for special objects like history, system, audit logs, and KAV objects on a weekly basis. Can be set to a daily basis, if needed.
3. Configure incremental backups to include all the objects in Salesforce. Recommended frequency for this backup is daily.
4. Configure the scheduled time of full and incremental backups with enough time the gap between them to avoid any bottlenecks in Salesforce, that may be caused due to queries being executed on the same objects in parallel.
5. Create backup schedules which are in sync with your production deployment schedules. Backup entire production instance or relevant instance data before deploying to a production instance
6. Identify a set of business-critical objects. Configure a backup specifically to include these objects to run at higher frequency levels (recommended frequency is multiple times a day) depending on RPO and RTO requirements.
7. Use the option to exclude formula fields in the case of objects with a large number of fields, without which it may result in Salesforce queries being errored out or giving results slowly.
8. Configure email addresses of users who need to be notified upon completion or failure of backups. (By default, the user who configured the backup will be notified automatically).
9. Go through logs and results of backups on a weekly basis to ensure that automated backups are happening as expected.
10. Adjust frequency and scheduled time of [backup](https://www.autorabit.com/blog/salesforce-essentials-backup-and-restore/) configurations based on API call limit and API calls consumption by other systems.
11. Salesforce user with which an org is registered on Vault should have admin-level permissions in the org. The recommendation is to create an admin user separately for Vault.
