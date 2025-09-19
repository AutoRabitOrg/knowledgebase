# nCino Release Notes 25.3

## nCino + DL - Release 25.3.11

**Release Date:** September 21, 2025

**Multibucket Rollback**\
Enhanced rollback functionality to ensure that inserted records are deleted and updated records are accurately reverted to their previous state.

**Multi-Bucket – Duplicate Objects**\
Resolved an issue where duplicate objects were displayed when working with multiple buckets..

**Single DataLoader – Attachments Processing**\
Fixed an issue where optional fields were incorrectly considered during delete operations — now only record IDs are considered for deleting the records.

**Feature Deployment – Object Duplication**\
Addressed duplication issues when using the same branch with the VC Revision Range option including both commits. Objects are no longer duplicated.

**Multibucket Support**\
Introduced support for multi-bucket functionality in templates, enabling better CI/CD data migration deployments and commits..

## nCino + DL - Release 25.3.10

**Release Date:** September 14, 2025

**Fix for Field Order in DL Module Results**\
Resolved an issue where the ID and Status/Error fields were displayed in an incorrect order when viewing success or failure results in the Data Loader modules.

**Optimized Log Display for Bulk Operations**\
Enhanced the log display for bulk operations to present users with optimized, clear, and relevant information for better troubleshooting and analysis.

## nCino + DL - Release 25.3.9.1

**Release Date:** September 10, 2025

**AuditLog – Null Pointer Exception Fix**\
A fix has been provided to address a null pointer exception occurring in instances with AuditLog enabled, ensuring stable and consistent execution.

## nCino + DL - Release 25.3.8

**Release Date:** August 31, 2025

#### Data Migration Flow Fix <a href="#data-migration-flow-fix" id="data-migration-flow-fix"></a>

Resolved an issue caused by an unwanted forward slash that disrupted the complete data migration flow in both nCino and DataLoader. Customers must re-run the affected jobs to process data successfully.

## nCino + DL - Release 25.3.7

**Release Date:** August 24, 2025

#### Uber Jar Dependency <a href="#uber-jar-dependency" id="uber-jar-dependency"></a>

The dependency on the **uber jar** has been removed. Bulk data operations are now handled programmatically in the backend, improving efficiency, stability, and maintainability of the system.

#### Handling Source ID <a href="#handling-source-id" id="handling-source-id"></a>

A **Salesforce discrepancy** previously prevented source IDs from being fetched correctly. This issue has been resolved with a code fix, ensuring accurate retrieval and consistency of source IDs.

#### ORG-Level Permissions <a href="#org-level-permissions" id="org-level-permissions"></a>

A code fix has been applied to enforce correct permission requirements:

* **Source ORGs** now only require **read access**.
* **Destination ORGs** require **write access**.

## nCino + DL - Release 25.3.6 <a href="#title-text" id="title-text"></a>

**Release Date:** Aug 17, 2025

#### Handling Record Types <a href="#handling-record-types" id="handling-record-types"></a>

A fix has been implemented to ensure that **Record Types are now correctly assigned to records** during processing. This resolves issues where records were previously created or updated without the appropriate Record Type association.

#### DL Pro <a href="#dl-pro" id="dl-pro"></a>

A fix has been rolled out to ensure that, during data deployment, the **deployment status is fetched accurately**, resulting in a more reliable and successful deployment process.

## nCino + DL - Release 25.3.5 <a href="#title-text" id="title-text"></a>

**Release Date:** Aug 10, 2025

#### **Logs Enhancements** Improved logging capabilities for enhanced tracking and traceability.

#### **Cloning DL PRO Jobs** Enhanced DL PRO job cloning to ensure accurate replication with all settings retained.

**DataLoader Clone Functionality**\
Improved cloning process for DataLoader jobs to maintain configuration integrity.

**DL File Handling**\
Resolved issues to ensure reliable upload, insert, and delete operations for files.

## nCino + DL - Release 25.3.4 <a href="#title-text" id="title-text"></a>

**Release Date:** August 03, 2025

**Commit Jobs**

The processing of the commit jobs through the commit workspace has been streamlined.

**Dataloader Pro – Stability Improvement**\
An issue affecting the reliability of Dataloader Pro job execution has been resolved, ensuring smoother performance under high-load conditions.

**DL PRO - Clone Issue**

An issue that is occurring during the clone operation is rectified

**Dataloader Pro – Clone Operation Fix**\
Resolved an issue where the clone functionality did not behave as expected, ensuring cloned jobs retain original configurations accurately.

### nCino + DL - Release 25.3.3

**Release Date:** July 27, 2025

**CI Job Execution**\
CI Job execution via the queue has been streamlined to ensure consistent and reliable processing.

**nCino & Dataloader – Leading and Trailing Spaces**\
A fix has been implemented to ensure leading and trailing spaces are correctly handled during nCino and Dataloader job executions, improving data accuracy and consistency.

### nCino + DL - Release 25.3.2

**Release Date:** July20, 2025

**Feature Template**\
Resolved an issue impacting feature template functionality to ensure seamless loading, selection, and execution across workflows.

**Data Deployment via Migration Template**\
Implemented a fix to ensure reliable data deployment using migration templates, addressing inconsistencies during dataset migration.

### nCino + DL - 25.3.1 Release Notes

**Release Date:** July 13, 2025

### Pagination <a href="#pagination" id="pagination"></a>

A fix has been implemented to ensure that pagination functions reliably and transitions between pages occur seamlessly without disruptions.
