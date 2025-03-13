# Release Notes 21.0

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
