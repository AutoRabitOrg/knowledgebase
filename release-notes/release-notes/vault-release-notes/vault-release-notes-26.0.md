# Vault Release Notes 26.0

## Vault Release Notes 26.1.1

**Release Date: 25 March 2026**

**Range-Based Date Masking for Sensitive Date Fields**\
Introduced range‑based date masking for sensitive date fields, enabling more flexible and realistic anonymization by shifting dates within configurable ranges.

<figure><img src="../../../.gitbook/assets/1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/2.png" alt=""><figcaption></figcaption></figure>

**Error while creating backup config with filter**\
Fixed an error occurring when creating backup configurations with filters, so filtered backup configs can now be created reliably.

**Intermittent archive job failure**\
Resolved intermittent archive job failures caused by “Failed to write backup to storage” errors, improving archive job reliability.

**Live Data Masking - Auto-delete of Local Masking Rules**\
Fixed an issue where local masking rules were not automatically deleted when their associated Live Data Masking configuration was removed, preventing leftover rules.

**Search bar missing in field selection during configuration creation**\
Added the missing search bar in the field selection section when creating Search & Compare configurations, making it easier to find and select fields.

**Order of latest snapshot records in compare screen**\
Adjusted snapshot ordering on the compare screen, so the latest snapshot records now display in the correct lower section, improving readability of comparisons.

**Backup download email content mismatch**\
Corrected the email template triggered for backup downloads so its content now accurately reflects the download action rather than showing backup summary text.

**Search & Compare | Improved Failure Messaging**\
Improved failure messaging by displaying a clearer message “Job failed. Please review the job logs for more details”, within the job details view, guiding users to review job logs for more information when a job fails.

**Case Sensitivity toggle in Search & Compare**\
Added a case sensitivity toggle in Search & Compare, allowing users to choose whether text comparisons are case‑sensitive or case‑insensitive.

**Metadata restore issues**\
Introduced a rollback capability for failed jobs, enabling recovery of missing files and resolution of metadata-related errors.

**Environment-based backup retention policy**\
Implemented environment‑based backup retention policies, allowing distinct retention behavior for Production versus Sandbox environments and correcting existing sandbox retention settings.

**Reports failing to replicate in target org**\
Fixed a problem that caused certain reports to fail replication to target orgs, improving reliability and coverage for report replication.

**Compare job stuck “In Progress” with lengthy Customer ID**\
Resolved an issue where compare jobs could remain stuck “In Progress” when the Customer ID was unusually long, improving job completion reliability.

**Boolean config field accepts uppercase value without validation**\
Improved validation for boolean configuration fields in Search & Compare so invalid uppercase values are no longer accepted without proper validation.

**Config updates not reflected in the generated query**\
Fixed an issue where updates to the selected object in Search & Compare configuration edits were not reflected in the generated query, ensuring configuration changes take effect correctly.

**Provided Retry option for Live Data Masking**\
Introduced a Retry option for Live Data Masking jobs, allowing users to quickly rerun failed masking operations without recreating the configuration.

**Unable to access/login to Vault**\
Fixed a login issue that prevented some users from accessing Vault, improving authentication stability and reducing access errors.

**Restore seems stuck**\
Resolved an issue where certain restore jobs are not retaining the partial selection of the records. After the fix is rolled-out the partial selection of the records is being retained.

**Unable to replicate files larger than 10MB**\
Fixed an issue that prevented replication of files larger than 10 MB, ensuring large files are now handled correctly during replication.

## Vault Release Notes 26.1.0

**Release Date: 4 March 2026**

**Search Across Backups and Archives**

Vault now enables advanced searches across Backups and Archives within a selectable six-month time span using an intuitive query builder. Users can define specific criteria, execute the search configuration, and identify data from Archives & Backups.

<figure><img src="../../../.gitbook/assets/1 (4).png" alt=""><figcaption></figcaption></figure>

The feature allows comparison of selected snapshots to pinpoint changes across Orgs based on the defined criteria. Once differences are identified, the **Review and Restore** capability enables targeted data restoration, ensuring precise recovery of required records.

<figure><img src="../../../.gitbook/assets/2 (4).png" alt=""><figcaption></figcaption></figure>

This enhancement streamlines historical data analysis and controlled restoration from backups and archives.

<figure><img src="../../../.gitbook/assets/3 (5).png" alt=""><figcaption></figcaption></figure>

**Salesforce Org Registration – Enhanced to Support External Client Apps**

Updated the Salesforce Org registration flow to use OAuth 2.0 aligned with Salesforce’s requirement to support OAuth flow through External Connected Apps. The enhanced guided setup enables secure onboarding of Production and Sandbox environments with real-time validation, encrypted credential storage, automatic token management, actionable error guidance, environment health visibility, and complete audit logging.

#### Multi-Factor Authentication – QR Code Display

Resolved an issue where the QR code was not displayed during the multi-factor authentication (MFA) setup process. This fix ensures that the QR code is properly generated and available during authentication setup, allowing users to complete MFA configuration successfully.

<figure><img src="../../../.gitbook/assets/image (2461).png" alt=""><figcaption></figcaption></figure>

**SSO Login – SAML Issuer Handling Fix**

Resolved an issue where users could encounter login failures when authenticating through SSO due to improper handling of the SAML issuer during validation. The authentication process has been updated to correctly process the issuer value, ensuring successful login when the required attributes are provided by the Identity Provider.
