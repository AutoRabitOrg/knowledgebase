# nCino Release Notes 25.3

## nCino + **DataLoader** - Release 25.3.12

**Release Date:** September 28, 2025

#### **Multi-Bucket Support** <a href="#multi-bucket-support" id="multi-bucket-support"></a>

Enhanced multi-bucket handling to ensure records are processed without creating duplicate entries.

#### **Viewing Diff Count** <a href="#viewing-diff-count" id="viewing-diff-count"></a>

Fixed an issue preventing users from viewing record differences when multiple templates were committed to the repository. Diff counts now display accurately.

#### **Templates with Multi-Buckets** <a href="#templates-with-multi-buckets" id="templates-with-multi-buckets"></a>

Resolved a deployment failure scenario where templates containing multiple buckets caused object deployment errors.

#### **Build Failure Due to Null Entry** <a href="#build-failure-due-to-null-entry" id="build-failure-due-to-null-entry"></a>

Fixed a defect where builds failed because of null entry objects. Builds now complete successfully.

#### **Error Uploading to S3** <a href="#error-uploading-to-s3" id="error-uploading-to-s3"></a>

Improved stability of data uploads to S3 to ensure seamless and reliable transfers.

#### **Multi-Object Set Template** <a href="#multi-object-set-template" id="multi-object-set-template"></a>

Implemented safeguards to prevent failures in multi-object set templates during execution.

***

## nCino + **DataLoader** - Release 25.3.11

**Release Date:** September 21, 2025

#### **Multi-bucket Rollback**

Enhanced rollback functionality to ensure that inserted records are deleted and updated records are accurately reverted to their previous state.

#### **Multi-bucket – Duplicate Objects**

Resolved an issue where duplicate objects were displayed when working with multiple buckets..

#### **Single DataLoader – Attachments Processing**

Fixed an issue where optional fields were incorrectly considered during delete operations — now only record IDs are considered for deleting the records.

#### **Feature Deployment – Object Duplication**

Addressed duplication issues when using the same branch with the VC Revision Range option including both commits. Objects are no longer duplicated.

#### **Multi-bucket Support**

Introduced support for multi-bucket functionality in templates, enabling better CI/CD data migration deployments and commits..

***

## nCino + **DataLoader** - Release 25.3.10

**Release Date:** September 14, 2025

#### **Fix for Field Order in DataLoader Module Results**

Resolved an issue where the ID and Status/Error fields were displayed in an incorrect order when viewing success or failure results in the Data Loader modules.

#### **Optimized Log Display for Bulk Operations**

Enhanced the log display for bulk operations to present users with optimized, clear, and relevant information for better troubleshooting and analysis.

***

## nCino + **DataLoader** - Release 25.3.9.1

**Release Date:** September 10, 2025

#### **AuditLog – Null Pointer Exception Fix**

A fix has been provided to address a null pointer exception occurring in instances with AuditLog enabled, ensuring stable and consistent execution.

***

## nCino + **DataLoader** - Release 25.3.9

**Release Date:** September 07, 2025

#### RBC Commit Data Merging Enhancements <a href="#rbc-commit-data-merging-enhancements" id="rbc-commit-data-merging-enhancements"></a>

Enhanced the nCino RBC commit workflow to intelligently merge record-based configuration changes (CSV and JSON) in version control. This ensures existing data is preserved while new changes are appended during commits, enabling seamless multi-version management and more reliable deployments across environments.

#### DL Test Configuration – Failure Count Logging Fix <a href="#dl-test-configuration-failure-count-logging-fix" id="dl-test-configuration-failure-count-logging-fix"></a>

Fixed an issue where the failed records count was not accurately reflected in the logs for Data Loader configuration jobs. The logs now display the correct failure count after job execution.

#### CI Jobs – Build Failure After Cloning <a href="#ci-jobs-build-failure-after-cloning" id="ci-jobs-build-failure-after-cloning"></a>

Fixed an issue where cloned CI Jobs failed during the build when executed against a different target branch. The build process now correctly handles scenarios where no data is found for the selected template by updating the appropriate status and response, ensuring stable job execution.

#### DataLoader Pro – Job Stuck in In-Progress State <a href="#dataloader-pro-job-stuck-in-in-progress-state" id="dataloader-pro-job-stuck-in-in-progress-state"></a>

Resolved an issue where DataLoader Pro jobs processing parent–child records could remain in an _In Progress_ state for an extended period. A fix has been applied to handle a null pointer exception and to ensure the overall job status is updated correctly upon completion.

#### Feature Commit – Log Step Update <a href="#feature-commit-log-step-update" id="feature-commit-log-step-update"></a>

Implemented a migration to correctly update the current log step in the Feature Commit Label table, ensuring accurate tracking of feature commit progress.

***

## nCino + **DataLoader** - Release 25.3.8

**Release Date:** August 31, 2025

#### Data Migration Flow Fix <a href="#data-migration-flow-fix" id="data-migration-flow-fix"></a>

Resolved an issue caused by an unwanted forward slash that disrupted the complete data migration flow in both nCino and Data Loader. Customers must re-run the affected jobs to process data successfully.

***

## nCino + **DataLoader** - Release 25.3.7

**Release Date:** August 24, 2025

#### Uber Jar Dependency <a href="#uber-jar-dependency" id="uber-jar-dependency"></a>

The dependency on the **uber jar** has been removed. Bulk data operations are now handled programmatically in the backend, improving efficiency, stability, and maintainability of the system.

#### Handling Source ID <a href="#handling-source-id" id="handling-source-id"></a>

A **Salesforce discrepancy** previously prevented source IDs from being fetched correctly. This issue has been resolved with a code fix, ensuring accurate retrieval and consistency of source IDs.

#### Org-Level Permissions <a href="#org-level-permissions" id="org-level-permissions"></a>

A code fix has been applied to enforce correct permission requirements:

* **Source ORGs** now only require **read access**.
* **Destination ORGs** require **write access**.

***

## nCino + **DataLoader** - Release 25.3.6 <a href="#title-text" id="title-text"></a>

**Release Date:** August 17, 2025

#### Handling Record Types <a href="#handling-record-types" id="handling-record-types"></a>

A fix has been implemented to ensure that **Record Types are now correctly assigned to records** during processing. This resolves issues where records were previously created or updated without the appropriate Record Type association.

#### **DataLoader Pro**

A fix has been rolled out to ensure that, during data deployment, the **deployment status is fetched accurately**, resulting in a more reliable and successful deployment process.

***

## nCino + **DataLoader** - Release 25.3.5 <a href="#title-text" id="title-text"></a>

**Release Date:** Aug 10, 2025

#### **Logs Enhancements**

Improved logging capabilities for enhanced tracking and traceability.

#### **Cloning Data Loader Pro Jobs**

Enhanced **Data Loader** Pro job cloning to ensure accurate replication with all settings retained.

#### **Data Loader Clone Functionality**

Improved cloning process for Data Loader jobs to maintain configuration integrity.

#### **DL File Handling**

Resolved issues to ensure reliable upload, insert, and delete operations for files.

***

## nCino + **DataLoader** - Release 25.3.4 <a href="#title-text" id="title-text"></a>

**Release Date:** August 03, 2025

#### **Commit Jobs**

The processing of the commit jobs through the commit workspace has been streamlined.

#### **DataLoader Pro – Stability Improvement**

An issue affecting the reliability of Data Loader Pro job execution has been resolved, ensuring smoother performance under high-load conditions.

#### **DataLoader Pro – Clone Issue**

An issue that is occurring during the clone operation is rectified

#### **DataLoader Pro – Clone Operation Fix**

Resolved an issue where the clone functionality did not behave as expected, ensuring cloned jobs retain original configurations accurately.

***

## nCino + **DataLoader** - Release 25.3.3

**Release Date:** July 27, 2025

#### **CI Job Execution**

CI Job execution via the queue has been streamlined to ensure consistent and reliable processing.

#### **nCino & DataLoader – Leading and Trailing Spaces**

A fix has been implemented to ensure leading and trailing spaces are correctly handled during nCino and DataLoader job executions, improving data accuracy and consistency.

***

## nCino + **DataLoader** - Release 25.3.2

**Release Date:** July 20, 2025

#### **Feature Template**

Resolved an issue impacting feature template functionality to ensure seamless loading, selection, and execution across workflows.

#### **Data Deployment via Migration Template**

Implemented a fix to ensure reliable data deployment using migration templates, addressing inconsistencies during dataset migration.

***

## nCino + **DataLoader** - 25.3.1 Release Notes

**Release Date:** July 13, 2025

#### Pagination <a href="#pagination" id="pagination"></a>

A fix has been implemented to ensure that pagination functions reliably and transitions between pages occur seamlessly without disruptions.
