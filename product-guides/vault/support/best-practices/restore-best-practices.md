# Restore Best Practices

This article illustrates many of the key best practices for the restores process on the Vault platform:

#### For Metadata <a href="#for-metadata" id="for-metadata"></a>

1. Instead of executing _full metadata restoration_ at once, which would fail if metadata exceeds salesforce governor limits, identify the code components and opt for _selective restoration_.
2. If you try to restore full metadata in 2-3 cycles of selective restoration, you must understand the metadata's dependent components and include them in the selective restoration operations.Links to salesforce metadata limitation: [https://developer.salesforce.com/docs/atlas.en-us.salesforce\_app\_limits\_cheatsheet.meta/salesforce\_app\_limits\_cheatsheet/salesforce\_app\_limits\_platform\_metadata.htm](https://developer.salesforce.com/docs/atlas.en-us.salesforce\_app\_limits\_cheatsheet.meta/salesforce\_app\_limits\_cheatsheet/salesforce\_app\_limits\_platform\_metadata.htm)
3. Active validation rules, triggers, process builders, and workflow may result in data and metadata restoration failures. Make sure these are _turned off_ before you run the restore operation.
4. Metadata API can deploy and retrieve up to _10,000 files_ or _400 MB_ at one time. If either of these limits is exceeded, the deployment or retrieval fails. Make sure the metadata size is less than 400 MB for a single job. You can split the metadata into multiple jobs to achieve restoration/replication if metadata is larger than 400 MB.
5. Define batch size based depending on the size of metadata or data you want to perform jobs on.

#### For Data <a href="#for-data" id="for-data"></a>

1. If you're initiating a data restoration, make sure your production org has _full API limits_, else the process will take a long time (due to API availability limits)
2. If the triggers/validation rules are not properly configured, data restoration may fail.
3. Make sure the data you're restoring belongs to active users/owners; any failure caused by inactive owners/accounts/users should be considered a salesforce data error, not a vault restoration issue.
