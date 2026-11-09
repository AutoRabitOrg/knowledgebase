# nCino Release Notes 25.3

## nCino + DataLoader 25.3.12

**Release date:** 28 September 2025

#### Multi-Bucket Support

Enhanced multi-bucket handling to ensure records are processed without creating duplicate entries.

#### Viewing Diff Count

Fixed an issue preventing users from viewing record differences when multiple templates were committed to the repository. Diff counts now display accurately.

#### Templates with Multi-Buckets

Resolved a deployment failure scenario where templates containing multiple buckets caused object deployment errors.

#### Build Failure Due to Null Entry

Fixed a defect where builds failed because of null entry objects. Builds now complete successfully.

#### Error Uploading to S3

Improved stability of data uploads to S3 to ensure seamless and reliable transfers.

#### Multi-Object Set Template

Implemented safeguards to prevent failures in multi-object set templates during execution.

***

## nCino + DataLoader 25.3.11

**Release date:** 21 September 2025

#### Multi-bucket Rollback

Enhanced rollback functionality to ensure that inserted records are deleted and updated records are accurately reverted to their previous state.

#### Multi-bucket – Duplicate Objects

Resolved an issue where duplicate objects were displayed when working with multiple buckets..

#### Single DataLoader – Attachments Processing

Fixed an issue where optional fields were incorrectly considered during delete operations — now only record IDs are considered for deleting the records.

#### Feature Deployment – Object Duplication

Addressed duplication issues when using the same branch with the VC Revision Range option including both commits. Objects are no longer duplicated.

#### Multi-bucket Support

Introduced support for multi-bucket functionality in templates, enabling better CI/CD data migration deployments and commits..

***

## nCino + DataLoader 25.3.10

**Release date:** 14 September 2025

#### Fix for Field Order in DataLoader Module Results

Resolved an issue where the ID and Status/Error fields were displayed in an incorrect order when viewing success or failure results in the Data Loader modules.

#### Optimized Log Display for Bulk Operations

Enhanced the log display for bulk operations to present users with optimized, clear, and relevant information for better troubleshooting and analysis.

***

## nCino + DataLoader 25.3.9.1

**Release date:** 10 September 2025

#### AuditLog – Null Pointer Exception Fix

A fix has been provided to address a null pointer exception occurring in instances with AuditLog enabled, ensuring stable and consistent execution.

***

## nCino + DataLoader 25.3.9

**Release date:** 7 September 2025

#### RBC Commit Data Merging Enhancements

Enhanced the nCino RBC commit workflow to intelligently merge record-based configuration changes (CSV and JSON) in version control. This ensures existing data is preserved while new changes are appended during commits, enabling seamless multi-version management and more reliable deployments across environments.

#### DL Test Configuration – Failure Count Logging Fix

Fixed an issue where the failed records count was not accurately reflected in the logs for Data Loader configuration jobs. The logs now display the correct failure count after job execution.

#### CI Jobs – Build Failure After Cloning

Fixed an issue where cloned CI Jobs failed during the build when executed against a different target branch. The build process now correctly handles scenarios where no data is found for the selected template by updating the appropriate status and response, ensuring stable job execution.

#### DataLoader Pro – Job Stuck in In-Progress State

Resolved an issue where DataLoader Pro jobs processing parent–child records could remain in an _In Progress_ state for an extended period. A fix has been applied to handle a null pointer exception and to ensure the overall job status is updated correctly upon completion.

#### Feature Commit – Log Step Update

Implemented a migration to correctly update the current log step in the Feature Commit Label table, ensuring accurate tracking of feature commit progress.

***

## nCino + DataLoader 25.3.8

**Release date:** 31 August 2025

#### Data Migration Flow Fix

Resolved an issue caused by an unwanted forward slash that disrupted the complete data migration flow in both nCino and Data Loader. Customers must re-run the affected jobs to process data successfully.

***

## nCino + DataLoader 25.3.7

**Release date:** 24 August 2025

#### Uber Jar Dependency

The dependency on the **uber jar** has been removed. Bulk data operations are now handled programmatically in the backend, improving efficiency, stability, and maintainability of the system.

#### Handling Source ID

A **Salesforce discrepancy** previously prevented source IDs from being fetched correctly. This issue has been resolved with a code fix, ensuring accurate retrieval and consistency of source IDs.

#### Org-Level Permissions

A code fix has been applied to enforce correct permission requirements:

* **Source ORGs** now only require **read access**.
* **Destination ORGs** require **write access**.

***

## nCino + DataLoader 25.3.6

**Release date:** 17 August 2025

#### Handling Record Types

A fix has been implemented to ensure that **Record Types are now correctly assigned to records** during processing. This resolves issues where records were previously created or updated without the appropriate Record Type association.

#### DataLoader Pro

A fix has been rolled out to ensure that, during data deployment, the **deployment status is fetched accurately**, resulting in a more reliable and successful deployment process.

***

## nCino + DataLoader 25.3.5

**Release date:** 10 August 2025

#### Logs Enhancements

Improved logging capabilities for enhanced tracking and traceability.

#### Cloning Data Loader Pro Jobs

Enhanced **Data Loader** Pro job cloning to ensure accurate replication with all settings retained.

#### Data Loader Clone Functionality

Improved cloning process for Data Loader jobs to maintain configuration integrity.

#### DL File Handling

Resolved issues to ensure reliable upload, insert, and delete operations for files.

***

## nCino + DataLoader 25.3.4

**Release date:** 3 August 2025

#### Commit Jobs

The processing of the commit jobs through the commit workspace has been streamlined.

#### DataLoader Pro – Stability Improvement

An issue affecting the reliability of Data Loader Pro job execution has been resolved, ensuring smoother performance under high-load conditions.

#### DataLoader Pro – Clone Issue

An issue that is occurring during the clone operation is rectified

#### DataLoader Pro – Clone Operation Fix

Resolved an issue where the clone functionality did not behave as expected, ensuring cloned jobs retain original configurations accurately.

***

## nCino + DataLoader 25.3.3

**Release date:** 27 July 2025

#### CI Job Execution

CI Job execution via the queue has been streamlined to ensure consistent and reliable processing.

#### nCino & DataLoader – Leading and Trailing Spaces

A fix has been implemented to ensure leading and trailing spaces are correctly handled during nCino and DataLoader job executions, improving data accuracy and consistency.

***

## nCino + DataLoader 25.3.2

**Release date:** 20 July 2025

#### Feature Template

Resolved an issue impacting feature template functionality to ensure seamless loading, selection, and execution across workflows.

#### Data Deployment via Migration Template

Implemented a fix to ensure reliable data deployment using migration templates, addressing inconsistencies during dataset migration.

***

## nCino + DataLoader 25.3.1

**Release date:** 13 July 2025

#### Pagination

A fix has been implemented to ensure that pagination functions reliably and transitions between pages occur seamlessly without disruptions.
