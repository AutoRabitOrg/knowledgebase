# Vault Release Notes

These release notes contain important information about **Vault® 23.2**.&#x20;

This release incorporates new featu

res, enhancements, and resolved issues from all previous significant releases. If you're upgrading from an earlier version of Vault, check the release notes for any interim versions for details about additional improvements in this release over your current release.

## Vault 23.2 Release Notes

**August 2023**

_**What's New?**_

#### View Archived Data through Vault Connect (Beta) <a href="#view-archived-data-through-vault-connect-beta" id="view-archived-data-through-vault-connect-beta"></a>

The archival capabilities of Vault are now enhanced further to create a connection between Salesforce and the storage environment (AWS S3 bucket), leveraging Salesforce Connect with OData 4.0 adapter to display the archived records directly within Salesforce without having to perform complex data loading operations.

#### **Prerequisites**

1. Salesforce Connect OData 4.0 adapter license
2. Reach out to support@autorabit.com to express your interest in participating in the beta program.

#### **Pricing**

Please reach out to your respective Customer Success Manager or Account Executive for more details on the pricing of this capability.

#### **Highlights**

1. OData protocol is an open and platform-independent protocol that can be integrated with the system of the user’s choice (along with Salesforce) as it exposes REST APIs for consuming and querying data from the underlying archives.
2. External objects support most of the capabilities that standard and custom objects have in Salesforce.
3. No need to install any managed packages or write custom scripts in Salesforce.

#### **Limitations**

1. Files and attachments are not supported for viewing through external objects in Salesforce. This will be supported in the upcoming version of Vault Connect scheduled for the end of Q4 ’23.
2. Salesforce OData 4.0 adapter has a limitation on the number of callouts per hour. This is going to be addressed with the support for the Salesforce OData 4.01 adapter in the subsequent versions of the capability.
3. Relationships between external objects and Salesforce objects need to be established manually (like if cases are archived and they are related to accounts that are not archived, the reference to accounts that are in the Salesforce object will be available in the external object but will not be reflected as a lookup relationship). The plan is to support the automated recreation of these references by the end of Q4 2023.
4. All the limitations of Salesforce external objects are applicable as mentioned in this article: [Help and Training Community](https://help.salesforce.com/s/articleView?language=en\_US\&id=sf.platform\_connect\_general\_limits.htm\&type=5).
5. The solution supports only the customers configured with AWS S3 as a storage option in Vault.
6. There is a max limit of 5GB of archived data per customer supported for connecting to Salesforce external data source as part of the beta program. This can be extended to a higher limit by raising a request with [support@autorabit.com](http://support@autorabit.com/).

For details on how to configure Vault Connect, please click here to access our [**Vault documentation**](../../product-guides/vault/vault-features/vault-connect/vault-connect-user-guide.md).

## Vault 23.1 Release Notes <a href="#vault-231" id="vault-231"></a>

**January 2023**

#### What's New <a href="#whats-new" id="whats-new"></a>

#### **Multi-Factor Authentication (MFA) support**

Currently, Vault allows _usernames_ and _passwords_ or _SSO-based_ authentication to grant users access to the Vault application; however, most of our customers requested the implementation of an additional layer of protection to prevent the misuse of their credentials if user credentials were compromised. With MFA now supported, it will allow our users to add Google, Salesforce, or other comparable authenticator apps to provide an authentication code at login.

[Read more →](../../product-guides/vault/getting-started/set-up-multifactor-authentication-in-vault.md)

#### **Unique Identifiers for Object**

With this update, we've added the capability to assign a unique identification to each object, preventing the generation of duplicate records.  The mapping between source and destination records was not previously available with Vault when records were available in a sandbox, making it impossible to uniquely identify the records in the destination.&#x20;

Thanks to this capability, every entity in the Salesforce org can now have a unique identifier configured. You can now restore or replicate data without recreating duplicate records.

#### **Enhanced schema representation in restore/replicate**

With the most recent Vault **23.1** release, we improved the schema representation by showing one level of the child/parent objects at a time. The tree can now be expanded based on your selection rather than the entire tree, which speeds up the download of the schema data and improves the UI.&#x20;

The significant improvements are:

* Shows the user one level of the child/parent objects at a time.&#x20;
* Expand the tree based on user selection instead of expanding the entire tree.
* The schema is easily searchable, and objects are easily selectable.

#### **Ability to search records in backup with partially matching values**

We have now made it possible to search backups for records selectively using a term that partially matches them. Users can now search backup records with partially matching values instead of using the whole value as the search keyword.

#### **Description field for backup and archive configurations**

Users need to understand the details of the config created, and it is helpful for any new member to understand the configs setup and why they were created. As a result, we included the **Description** box on the **Configuration** page so that you may describe why you created the backup and archiving configurations. This description field can also be seen on the **Config Summary** screen.&#x20;

#### Improvements <a href="#improvements" id="improvements"></a>

* Improved pagination to reduce page load times across the modules.
* Minor performance, bug fixes, and security improvements can also be observed in the Vault portal.&#x20;

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 7 June 2023 <a href="#id-7-june-2023" id="id-7-june-2023"></a>

_**Vault v23.1.11**_

This is a maintenance release. The following items were fixed and/or added:

1. An issue was resolved where users were experiencing a problem replicating records from production to a developer sandbox with the backup with hierarchy option. In this issue, when attempting to replicate over 1100 records, no records were being populated in the developer sandbox.
2. An issue has been resolved that affected manual backups. Users were unable to obtain all the objects in the backup, even when using the correct configuration settings.
3. An issue has been addressed where users were archiving jobs with a configuration set to limit to 1 million records, but more than 1 million records were being archived. This issue has been fixed.
4. An issue has been resolved where users encountered a problem while searching for a specific set of objects using the filter option during restoration or replication. Instead of selecting only those specific objects, all the objects were selected. This issue has been fixed.

#### 17 May 2023 <a href="#id-17-may-2023" id="id-17-may-2023"></a>

_**Vault v23.1.10**_

This is a maintenance release. The following items were fixed and/or added:

1. Vault now supports Single Sign-On (SSO) capability through its auto-login function.

#### 10 May 2023 <a href="#id-10-may-2023" id="id-10-may-2023"></a>

_**Vault v23.1.9**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue for the **Restore/Replicate** operation where the Person accounts restoration/replication failed when the backup got triggered with Person contacts.

#### 03 May 2023 <a href="#id-03-may-2023" id="id-03-may-2023"></a>

_**Vault v23.1.8**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue where the Vault archival failed with **`"No Records Archived"`** status in the Vault UI.
2. Fixed an issue where replicating the **Assest records** from the source to the destination org ran for a few hours, but no records were picked up.
3. Fixed an issue where the scheduled backups failed for production orgs.

#### 26 April 2023 <a href="#id-26-april-2023" id="id-26-april-2023"></a>

_**Vault v23.1.7**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue where the scheduled Archival jobs ran even after the **Config** was deleted.
2. Fixed a bug where users had issues downloading the **Label Names** report in the **Replicate** section.

#### 19 April 2023 <a href="#id-19-april-2023" id="id-19-april-2023"></a>

_**Vault v23.1.6**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue when replicating records from the production to a developer sandbox (1100+ records); no records were populated in the developer sandbox.
2. Fixed an issue where the archive job kept running after data were processed.
3. Fixed an issue with the Vault's data storage and management where the archive process failed as it could not write a backup to the Amazon S3 bucket.

#### 12 April 2023 <a href="#id-12-april-2023" id="id-12-april-2023"></a>

_**Vault v23.1.5**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue where the users could not archive the ContentDocument files ([#57707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093546014)).
2. Fixed an issue where the users could not edit or delete masking rules in the Replicate module (internal ticket).
3. Fixed an issue where the Archival jobs did not show all children's details in the **Archive config info** section (internal ticket).

#### 29 March 2023 <a href="#id-29-march-2023" id="id-29-march-2023"></a>

_**Vault v23.1.4**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue when the archive jobs got stuck, and the following error was thrown **`java.util.concurrent.ExecutionException: [UnexpectedErrorFault [ApiFault exceptionCode='TXN_SECURITY_RUNTIME_ERROR'`**. Additionally, when multiple archive jobs were initiated in the Salesforce environment, the count of the archive records fluctuated. Now that the issue has been rectified, everything works as it should.
2. Fixed an issue where the Salesforce API limit for the backup triggered using the Bulk API differed from the limit displayed inside the Vault application.
3. Fixed an issue that stopped the replication jobs from migrating the _Case and related objects_ to the production environment, including the _Content Document, ContentVersion, and ContentDocument link_.

#### 21 March 2023 <a href="#id-21-march-2023" id="id-21-march-2023"></a>

_**Vault v23.1.3**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue where users were trying to map case records which were eventually restored but not properly mapped.
2. Fixed an issue where the users could not use the SSO feature to log in to their Vault account.
3. Fixed an issue where users, while changing the password, the users were unable to see the `Save` button.

#### 15 March 2023 <a href="#id-15-march-2023" id="id-15-march-2023"></a>

_**Vault v23.1.2**_

This is a maintenance release. The following items were fixed and/or added:

1. Fixed an issue where the restore operation was stuck for hours, and in the end, the status threw as failed.
2. Fixed an issue where the replicate job failed with no error in the log.
3. Fixed an issue where the replicate Job is not replicating `ContentVersion` and `ContentDocumentLink` objects.
4. Fixed an issue where the hierarchical and archival-child objects were not processed using EZ-restore and EZ-replicate.
5. Fixed an issue for the EZ- Replicate, where the file upload count was incorrect.

#### 08 March 2023 <a href="#id-08-march-2023" id="id-08-march-2023"></a>

_**Vault v23.1.1**_

This is a maintenance release. The following items were fixed and/or added:

1.  Handling Salesforce session timeout in restore/replicate improved and performance improvement in the `updateOldIdsWithNewIds method.`

    ***



## Vault 22.2 Release Notes <a href="#vault-222" id="vault-222"></a>

#### What's New <a href="#whats-new1" id="whats-new1"></a>

**Support for Serial Backups**

With this release, we have added the flexibility to enable your backup configs to run in serial mode. This prevents overlap of backups triggered under the same config and helps reduce redundant data storage caused due to overlapping backups.

[Read more →](../../product-guides/vault/vault-features/backup/schedule-a-vault-backup.md)

**Access restriction through SSO for non-registered users**

We’ve added the capability to Vault administrator to prevent the auto-creation of new users in Vault from SSO ID providers like OKTA and Microsoft Azure AD.

[Read more →](../../product-guides/vault/configuring-vault/sso-configuration/sso-for-okta.md)

**Notifications for Restore/Replicate operations**

With this release, we have enhanced the capability of how the users get notified once an operation is performed inside Vault. You will now have a field to add multiple recipients who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be enabled to receive the notifications.

[Read more →](../../product-guides/vault/vault-features/restore/restoring-the-metadata-data-to-the-salesforce-org.md)

***

\


## Vault 21.4 Release Notes <a href="#vault-214" id="vault-214"></a>

**Release: 01 August 2021**

#### Enhancements <a href="#enhancements" id="enhancements"></a>

**nCino Template Sync:** Now that Vault is linked to nCino, whenever the nCino team changes or releases a template, Vault's [nCino features](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) will be updated as well.&#x20;

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* AutoRABIT’s help desk access via Vault had certain issues that have been rectified. Now you can see all of your support tickets when you access the helpdesk via Vault.&#x20;
* The combination of full and incremental [metadata backups](https://www.autorabit.com/blog/7-salesforce-security-concerns-relating-to-metadata/) was not picking up all metadata for restore. This has now been rectified and is working as it should.&#x20;
* Due to a certificate issue, SSO for Azure Blob storage was not working. This has been resolved. SSO now functions as intended.

## Vault 21.3 Release Notes <a href="#vault-213" id="vault-213"></a>

**Release: 06 June 2021**

#### Enhancements <a href="#enhancements1" id="enhancements1"></a>

* **Pre Restore/ Replicate Checklist:** Now you can achieve improved governance for restore/ replicate jobs by following a set of guidelines to maximize the success rate.
* **UI Improvement:** With this release, you will see all the jobs on a single summary page. The In-Progress tab under Backup, Restore, Replicate, Archival, GDPR module has been deprecated.&#x20;
* Vault now provides a capability to download backed-up metadata files for the on-premise offering&#x20;
* **Improved security:** We have worked on strengthening security by adding an additional layer of security.&#x20;

#### Bug Fixes <a href="#bug-fixes1" id="bug-fixes1"></a>

* **Field level restores fix for On-Premise offering:** The field level restore showed peculiar behavior for on-prem hosting this issue was identified and fixed. Now you can successfully restore at field level for the on-prem offering.&#x20;
* **Backup member count for Dashboard, Reports, and EmailTemplate:** There was an issue identified on backup count mismatch for incremental backups for metadata (Dashboard, Reports, and EmailTemplate). This is issue has been fixed, now you can see the exact count of the metadata that got changed and picked up in an incremental backup.

## Vault 21.2 Release Notes <a href="#vault-212" id="vault-212"></a>

**Release: 26 April 2021**

For our customers in regulated industries with extended needs to meet compliance and security auditing standards – Now Vault is fully available for on-premises or in-your-cloud deployment and use of on-premises storage (including SANs). These new deployment and storage options give you complete control of the environment where Vault is deployed and your data sets are stored.

#### New Features <a href="#new-features" id="new-features"></a>

**On-premises or “in-your-cloud” deployment**

Now Vault can be deployed where you need it to be. You can choose our AutoRABIT hosted and managed SaaS deployment within your premises or at a cloud location (Private or Public Cloud). Contact your sales representative if your organization would like to pursue this.

**On-premises storage from your AutoRABIT-hosted Vault**

We now support on-premises as well as cloud storage. Host your backups and archives within your premises, DR sites, or cloud environments. And get all the control you need to meet regulated industries' extended security, compliance, and risk reduction needs.

#### Enhancements <a href="#enhancements2" id="enhancements2"></a>

**Continued updates to the UI**

We’ve continued updates that we started in the UI with our March release. Again – there are no changes to where you’ll find content in the UI – just our updated look and feel with fonts, colors, buttons, and more.

**Email notifications with job status in the subject line**

Until now, when you received a Vault job status notification from us, you had to read the body of the email to find out what it would refer to. Now you’ll be able to quickly read the status line and select those that most need your attention for immediate reading.

**Some button naming changes: Full Restore to EZ Restore – Full Replicate to EZ Replicate**

1. EZ Restore (formerly Full Restore) enables restoration from a backup of all content from a selected backup. No functionality changes.
2. EZ Replicate (formerly Full Replicate) simplifies all the content from a backup set with just a few clicks. Again, no functionality changes.

**Support for additional FinancialForce Metadata types**

We’ve added support for some previously unsupported FinancialForce metadata types – (Layout, QuickAction, CustomObject, DuplicateRule).

## Vault 21.1 Release Notes <a href="#vault-211" id="vault-211"></a>

**Release: 25 March 2021**

The first thing you’ll notice with this new release is our updated look and feel.   All your familiar tools and features are available with updated fonts, colors, and logos.  We hope you’ll like it.

Elsewhere you’ll find new capabilities for using Google Cloud Platform (GCP) storage, enhanced support for Azure retention policies, and restore/replication functionality for non-required parents.

#### New Features <a href="#new-features1" id="new-features1"></a>

**Google Cloud Platform (GCP) storage support for Vault**

You can now use GCP storage for backups. Options available are to use either AutoRABIT’s hosted storage on GCP or your own GCP storage environment.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Fig_3_GCP(1).gif" alt=""><figcaption></figcaption></figure>

#### Enhancements <a href="#enhancements3" id="enhancements3"></a>

**Application Rebranding**&#x20;

Here’s a quick look at the product's updated UI and branding changes. Again – there are no changes to where you’ll find content in the UI (except for the new features below) – just our updated look and feel:

* Login/ Logout screens
* Logos
* Application fonts&#x20;
* Application colors

![Vault Data Backup Enhancements](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Fig\_1\_loginpage.gif)

**Restore/Replicate parents with relationship lookups**

We’ve now added the capability to restore or replicate any non-required parents. To do this, select them from the schema before running a restore/replicate job.

![Vault Data Restore/Replicate](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Fig\_2\_Schema.gif)

**Retention policy enhancements for Azure** &#x20;

With our January release, we added the capability to configure the Azure Blob Retention Policy for Azure-hosted backups from within the Vault UI to meet your retention requirements.

We’ve now enhanced this feature with the capability to define retention periods in previously existing Azure Blob-hosted backups or archives to start using retention periods.  Keep in mind that once you’ve applied a retention policy, your backups will no longer be available after the retention period has expired.

![Rentention Policy Enhancements for Azure](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Fig\_4\_Retention%20Policy.gif)

\
