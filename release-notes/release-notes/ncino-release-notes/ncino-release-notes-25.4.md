# nCino Release Notes 25.4

## nCino Release Notes 25.4.11 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** **14 December 2025**

#### **DataLoader Pro – Reference-Based Object Migration**

A fix has been implemented to ensure that objects with reference dependencies are no longer skipped during DataLoader Pro execution. The updated handling correctly processes referenced objects, ensuring complete and consistent data migration when reference relationships are involved.

#### **DataLoader Extract – Query Validation Performance**

Improved the DataLoader extract flow by optimizing query validation handling. This enhancement prevents long-running validation delays and ensures extract jobs proceed reliably even for large datasets.

#### **CI Jobs – Backup Snapshot Download**

Resolved an issue where backup snapshot downloads failed with a “File not found” error for CI jobs using a baseline source. Backup artifacts are now generated and retrieved correctly, ensuring reliable snapshot access after job execution.

#### **Feature Deployment – Deployment Status Handling**

Fixed an issue where redeployments using selective deployment remained stuck in the _In Progress_ state despite successful completion. Deployment iterations are now correctly finalized by saving only the selected objects, ensuring accurate status updates in Deployment History.

#### **DataLoader – Large File Download Handling**

Fixed an issue where large extract jobs produced invalid or incomplete CSV downloads. Extract results are now correctly packaged and downloaded in ZIP format, ensuring reliable access to full datasets for high-volume jobs.

#### **Feature Commit – CSV File Ordering**

Resolved an issue where object CSV files committed to version control were not consistently sorted. CSV files are now committed in a deterministic, sorted order, ensuring consistency across Feature Deployments and CI Jobs.

***

## nCino + DataLoader Release 25.4.10 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** **07 December 2025**

#### **nCino – Deployment History Action Button Fix** <a href="#ncino-deployment-history-action-button-fix" id="ncino-deployment-history-action-button-fix"></a>

A fix has been implemented to restore the functionality of the action button next to the download icon in Deployment History. The button now correctly expands the object set view, as intended.

#### **DataLoader Pro – UI Sync Issue After Bulk Delete** <a href="#dataloader-pro-ui-sync-issue-after-bulk-delete" id="dataloader-pro-ui-sync-issue-after-bulk-delete"></a>

A fix has been implemented to ensure that all jobs are immediately removed from the list after a bulk delete operation. Previously, one job continued to appear until the page was manually refreshed. The job list now updates correctly without requiring a browser refresh.

#### **Login Screen Loading Issue – Template Dependency Optimization** <a href="#login-screen-loading-issue-template-dependency-optimization" id="login-screen-loading-issue-template-dependency-optimization"></a>

A fix has been applied to prevent heap-space and restart issues caused by processing objects with complex parent dependencies during initial template creation. The system now skips non-selected standard and non-nCino package objects, ensuring the login screen loads reliably.

***

## nCino + DataLoader Release 25.4.9 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** **30 November 2025**

#### **DataLoader Pro – Multi-Level Parent Hierarchy Fix** <a href="#dl-pro-multi-level-parent-hierarchy-fix" id="dl-pro-multi-level-parent-hierarchy-fix"></a>

A fix was implemented to correctly handle multi-level parent relationships during DataLoader Pro migrations. An issue where ancestor object failures caused master and parent objects to fail has been resolved. The migration flow now isolates such failures and works reliably, including when Automatic Apply Filter is enabled.

#### **DataLoader Module – DB Optimization** <a href="#dl-module-db-optimization" id="dl-module-db-optimization"></a>

Redundant database calls across DataLoader Pro and Single DataLoader execution flows were removed, including unnecessary process, job, and object lookups. Job execution now fetches only relevant in-progress records, minimizing load. These enhancements significantly reduce DB usage and prevent connection pool shutdown issues.

#### **DataLoader Pro – Child Object Selection Fix** <a href="#dl-pro-child-object-selection-fix" id="dl-pro-child-object-selection-fix"></a>

A fix was implemented to ensure that, when editing a DL Pro job, the child object list correctly displays all available child objects rather than only the previously selected ones. This resolves inconsistencies in object visibility during job configuration.

#### **DataLoader Pro – Incorrect Parent Object Identification** <a href="#dl-pro-incorrect-parent-object-identification" id="dl-pro-incorrect-parent-object-identification"></a>

A fix was applied to ensure only the intended parent objects are included during job execution. The issue occurred when an object acted as both a parent and a child to the master object. The logic has been corrected to prevent additional, unintended parents from being identified and processed.

#### **DataLoader Pro – Job Redirect Issue Resolved** <a href="#dl-pro-job-redirect-issue-resolved" id="dl-pro-job-redirect-issue-resolved"></a>

A fix was implemented to ensure that, after running a DataLoader Pro job, the application correctly redirects back to the same job. Previously, it always loaded the first job in the list. The redirect logic on the DL Pro landing page has now been corrected.

#### **Corrected Error Message Handling** <a href="#corrected-error-message-handling" id="corrected-error-message-handling"></a>

Resolved an issue where an incorrect authentication error was shown for query-related failures. The system now displays the proper error message when a connection exception occurs.

***

## nCino + DataLoader Release 25.4.8 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** **23 November 2025**

### **Proxy Connectivity Issue – nCino & Data Loader** <a href="#proxy-connectivity-issue-ncino-and-data-loader" id="proxy-connectivity-issue-ncino-and-data-loader"></a>

A fix was implemented to resolve failures in nCino and Data Loader operations when Salesforce connectivity was routed through a proxy. Bulk API requests now establish connections reliably without timing out when the proxy is enabled.

### **Schema Synchronization for Feature Migration Templates** <a href="#schema-synchronization-for-feature-migration-templates" id="schema-synchronization-for-feature-migration-templates"></a>

A new option has been added to synchronize schema metadata directly within the Feature Migration Template. Triggering a sync refreshes the latest objects, fields, and attribute changes from Salesforce, ensuring templates remain up-to-date and reducing deployment failures caused by outdated schema definitions.

***

## nCino + DataLoader Release 25.4.7 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** 16 November 2025

**Handling User Data**

A fix was rolled out to make sure the user data such as jobs are handled properly once the user account is deleted from the Super Admin.

**Handling Object Relations**

A fix is provided to make sure the circular relations of objects in the buckets with multiple objects will be handled properly.

***

## nCino + DataLoader Release 25.4.6 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date:** 09 November 2025

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

***

## nCino + **DataLoader** Release 25.4.5

**Release Date:** 2 November 2025

#### Parent–Child Object Reference Handling

Implemented code changes to ensure parent object references in child records are correctly migrated when both parent and child objects are selected as child objects in a Data Loader Pro job.

#### Lookup Key Sorting Fix in Feature Commit

A fix was implemented to ensure the sorting field defaults to the lookup key during feature commit creation. The sorting field now switches to “Name” only when a lookup key field does not exist, preventing duplicate lookup keys in pull request file changes.

#### Dataset Loading Issue with Special Characters

Resolved an issue where datasets failed to load and got stuck at “Retrieving Iterations...” when the deployment label contained a “#” character. The label handling logic was updated to prevent URL truncation during dataset retrieval.

#### RBC Deployment – Invalid Field Error with Attachment Names

A fix was implemented to handle attachment names containing commas (`,`). Previously, deployments failed with an “Invalid Field” error when processing attachments with commas in their filenames.

***

## nCino + **DataLoader** Release 25.4.3

**Release Date:** 19 October 2025

#### **Connection Pool Shutdown Issue** <a href="#connection-pool-shutdown-issue" id="connection-pool-shutdown-issue"></a>

Optimized redundant database calls to prevent connection pool shutdown errors. This enhancement ensures stable and consistent connections during data processing, eliminating the “Connection Pool Issue” encountered by users.

***

## nCino + **DataLoader** Release 25.4.2

**Release Date:** 15 October 2025

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

***

## nCino + **DataLoader** Release 25.4.1

**Release Date**: 5 October 2025

#### **Person Account Org Handling** <a href="#person-account-org-handling" id="person-account-org-handling"></a>

Resolved an issue that caused record failures in environments with Person Account–enabled orgs. The process now supports these orgs seamlessly.

#### **DataLoader Extraction – Custom Query Handling** <a href="#data-loader-extraction-custom-query-handling" id="data-loader-extraction-custom-query-handling"></a>

Implemented a fix to ensure that custom queries in DataLoader extractions are parsed and executed correctly, preventing query-related failures.

#### **Attachment Processing** <a href="#attachment-processing" id="attachment-processing"></a>

Addressed an issue with attachment handling in form templates to ensure smooth and reliable processing during uploads and migrations.

#### **DataLoader Status Auto-Update** <a href="#dl-status-auto-update" id="dl-status-auto-update"></a>

Introduced an automatic refresh mechanism to keep job status updates in sync, ensuring that the latest execution status is always displayed in real time.
