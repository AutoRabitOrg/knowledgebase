# Release Notes 23.0

This release incorporates new features, enhancements, and resolved issues from all previous significant releases. If you're upgrading from an earlier version of Vault, check the release notes for any interim versions or details about additional improvements in this release over your current release.

### Vault 23.2.13 Release Notes

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

For details on how to configure Vault Connect, please click here to access our [**Vault documentation**](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/vault-connect).

## Vault 23.1.12 Release Notes <a href="#vault-231" id="vault-231"></a>

**January 2023**

#### What's New <a href="#whats-new" id="whats-new"></a>

#### **Multi-Factor Authentication (MFA) support**

Currently, Vault allows _usernames_ and _passwords_ or _SSO-based_ authentication to grant users access to the Vault application; however, most of our customers requested the implementation of an additional layer of protection to prevent the misuse of their credentials if user credentials were compromised. With MFA now supported, it will allow our users to add Google, Salesforce, or other comparable authenticator apps to provide an authentication code at login.

[Read more →](../../../product-guides/vault/getting-started/set-up-multifactor-authentication-in-vault.md)

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

_**3 Jan 2024**_

_**Vault v23.2.14**_&#x20;

1. Backup Delay: The backup is taking longer because FeedItem and EmailMessages are processing for over an hour.
2. Suggested Workaround: A workaround was suggested to exclude Total Price and Unit Price to resolve the issue.
3. Policy Level Verification: Verification revealed issues with multiple policies when selecting policy-level changes.

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

