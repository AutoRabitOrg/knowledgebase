# nCino Release Notes 25.4

## nCino + DL - Release 25.4.7 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** Nov 16, 2025

**Handling User Data**

A fix was rolled out to make sure the user data such as jobs are handled properly once the user account is deleted from the Super Admin.

**Handling Object Relations**

A fix is provided to make sure the circular relations of objects in the buckets with multiple objects will be handled properly.

## nCino + D - Release 25.4.6 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** Nov 09, 2025

#### **Delta Preparation Enhancement** <a href="#delta-preparation-enhancement" id="delta-preparation-enhancement"></a>

Enhanced delta preparation logic to ensure only relevant changes from the selected revisions are included when the source is Version Control (VC). This fix resolves migration failures caused by missing `.csv` files during deployment.

#### **CI Job – Validation Rules Handling** <a href="#ci-job-validation-rules-handling" id="ci-job-validation-rules-handling"></a>

Resolved an issue where the “Disable Validation Rules” setting was not honored during nCino CI job execution. The fix ensures that destination org details are correctly passed from the Agent to Rabbit, allowing validation rules to be accurately identified and disabled during deployment.

#### **Audit Fields Handling in Data Migration** <a href="#audit-fields-handling-in-data-migration" id="audit-fields-handling-in-data-migration"></a>

Resolved an issue where audit fields were incorrectly included during data migration, causing deployment failures for specific templates. The fix ensures audit fields are now processed only for objects that support them, preventing similar errors during deployment.

#### **RBC Feature Deployment – Authentication Error** <a href="#rbc-feature-deployment-authentication-error" id="rbc-feature-deployment-authentication-error"></a>

Resolved an issue where nCino RBC feature deployments intermittently failed with authentication errors despite valid credentials. The fix ensures record type data is properly saved during deployment, and additional loggers have been added to help trace any future occurrences.

#### **Salesforce SOAP Login Deprecation Notice**

Salesforce has deprecated the “username + password + security token” authentication method for integrations using the SOAP API starting with version 65. This legacy method will be completely disabled by Summer ’27 for API versions 31–64. Customers using this method in AutoRABIT connections (e.g., \{{ConnectionName\}}) must migrate to OAuth (JWT Bearer) authentication to ensure uninterrupted connectivity. The migration can be done through Connections → \{{ConnectionName\}} → Migrate to OAuth, followed by the on-screen steps to confirm the connection status as “OAuth (JWT)”.

## nCino + **DataLoader** - Release 25.4.5

**Release Date:** Nov2, 2025

#### Parent–Child Object Reference Handling

Implemented code changes to ensure parent object references in child records are correctly migrated when both parent and child objects are selected as child objects in a Data Loader Pro job.

#### Lookup Key Sorting Fix in Feature Commit

A fix was implemented to ensure the sorting field defaults to the lookup key during feature commit creation. The sorting field now switches to “Name” only when a lookup key field does not exist, preventing duplicate lookup keys in pull request file changes.

#### Dataset Loading Issue with Special Characters

Resolved an issue where datasets failed to load and got stuck at “Retrieving Iterations...” when the deployment label contained a “#” character. The label handling logic was updated to prevent URL truncation during dataset retrieval.

#### RBC Deployment – Invalid Field Error with Attachment Names

A fix was implemented to handle attachment names containing commas (`,`). Previously, deployments failed with an “Invalid Field” error when processing attachments with commas in their filenames.

## nCino + **DataLoader** - Release 25.4.3

**Release Date:** October 19, 2025

#### **Connection Pool Shutdown Issue** <a href="#connection-pool-shutdown-issue" id="connection-pool-shutdown-issue"></a>

Optimized redundant database calls to prevent connection pool shutdown errors. This enhancement ensures stable and consistent connections during data processing, eliminating the “Connection Pool Issue” encountered by users.

## nCino + **DataLoader** - Release 25.4.2

**Release Date:** October 15, 2025

#### **Person Account Org** <a href="#person-account-org" id="person-account-org"></a>

A fix has been implemented to ensure records are processed correctly in environments with Person Account–enabled orgs, preventing migration failures.

#### **Skipping Migration for Selected Parent Records** <a href="#skipping-migration-for-selected-parent-records" id="skipping-migration-for-selected-parent-records"></a>

Resolved an issue where parent records were incorrectly migrated even when the _Automatic Apply Filter_ option was selected. The system now skips parent records as intended.

#### **Cloning Single DataLoader Job** <a href="#cloning-single-data-loader-job" id="cloning-single-data-loader-job"></a>

Addressed an issue that prevented cloned DataLoader jobs from updating records properly. Cloned jobs now retain and update data accurately.

#### **Feature Management Versioning** <a href="#feature-management-versioning" id="feature-management-versioning"></a>

Implemented a UI enhancement to ensure versioning information displays correctly within the _Feature Management_ section.

#### **DataLoader Pro – Invalid Query Error** <a href="#dl-pro-invalid-query-error" id="dl-pro-invalid-query-error"></a>

Fixed an issue that occurred during job execution when no mappings were provided. The system now handles empty or null mapping values gracefully during job editing and saving.

#### **DataLoader Pro – Circular Reference Error** <a href="#dl-pro-circular-reference-error" id="dl-pro-circular-reference-error"></a>

Introduced a safeguard to handle empty source and destination external ID conditions, preventing circular reference errors during data processing.

## nCino + **DataLoader** - Release 25.4.1

**Release Date**: October 5, 2025

#### **Person Account Org Handling** <a href="#person-account-org-handling" id="person-account-org-handling"></a>

Resolved an issue that caused record failures in environments with Person Account–enabled orgs. The process now supports these orgs seamlessly.

#### **DataLoader Extraction – Custom Query Handling** <a href="#data-loader-extraction-custom-query-handling" id="data-loader-extraction-custom-query-handling"></a>

Implemented a fix to ensure that custom queries in DataLoader extractions are parsed and executed correctly, preventing query-related failures.

#### **Attachment Processing** <a href="#attachment-processing" id="attachment-processing"></a>

Addressed an issue with attachment handling in form templates to ensure smooth and reliable processing during uploads and migrations.

#### **DataLoader Status Auto-Update** <a href="#dl-status-auto-update" id="dl-status-auto-update"></a>

Introduced an automatic refresh mechanism to keep job status updates in sync, ensuring that the latest execution status is always displayed in real time.
