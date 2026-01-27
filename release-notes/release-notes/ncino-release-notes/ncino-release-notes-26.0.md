# nCino Release Notes 26.0

## nCino - Release 26.1.4

**Release Date:** 25 January 2026

#### Batch Size Support for Data Migration <a href="#batch-size-support-for-data-migration" id="batch-size-support-for-data-migration"></a>

Reintroduced the **Batch Size** option for data migration to process records in controlled batches, helping manage system load and ensure proper trigger execution during create or update operations in the target org.

#### Feature Deployment – Screens Template Batch Size Handling <a href="#feature-deployment-screens-template-batch-size-handling" id="feature-deployment-screens-template-batch-size-handling"></a>

Resolved an issue where enabling a batch size during the Screens template deployment caused failures by adding validation for CSV file size limits in bulk operations.

#### Forms Manager Template Deployment <a href="#forms-manager-template-deployment" id="forms-manager-template-deployment"></a>

Resolved an issue where Forms Manager template deployments remained stuck in an _In Progress_ state by correcting the handling of self-referenced records during entry object data retrieval.&#x20;

## nCino - Release 26.1.3

**Release Date:** **18 January 2026**

#### **Query Editor Validation Fix (nCino)** <a href="#query-editor-validation-fix-ncino" id="query-editor-validation-fix-ncino"></a>

Resolved an issue where valid queries entered in the **Query Editor** were incorrectly rejected with a validation error, preventing query execution during template configuration.

#### **nCino CI Job Deployment Consistency Fix**

Resolved an issue where the same **nCino template** produced inconsistent results between Deployment and CI Jobs. The fix ensures consistent behavior by correcting record type ID update logic during nCino CI job deployments.

***

## nCino + DataLoader - Release 26.1.2

**Release Date: 11 January 2026**

**Clone Version – Bucket Filter Retention**

Fixed an issue where filters applied to entry objects were not retained when switching between buckets in a cloned version, ensuring filter configurations persist consistently across buckets.

**Create Version – Entry Object Query Not Retained Across Object Sets**

Fixed an issue where entry object filter queries from the original version were not fully populated when creating a new version of a multi-bucket feature template. The filter queries are now consistently carried forward for all object sets during version creation.

***

## nCino + DataLoader - Release 26.1.1

**Release Date: 04 January 2026**

### **Version Control Source Reset in CI Jobs** <a href="#version-control-source-reset-in-ci-jobs" id="version-control-source-reset-in-ci-jobs"></a>

Resolved an issue where source details were not refreshed when changing the source type or repository during CI Job editing. The source configuration now resets correctly, ensuring accurate and consistent setup.

### **Single DataLoader – Limit Value Persistence Issue** <a href="#single-dataloader-limit-value-persistence-issue" id="single-dataloader-limit-value-persistence-issue"></a>

Fixed an issue where an unintended record limit was applied to subsequent Single DataLoader jobs. The system now correctly resets and applies record counts and limits when running jobs again or switching between extract, insert, and update operations with new CSV files.

### **DataLoader Extract – Download Performance Improvement** <a href="#dataloader-extract-download-performance-improvement" id="dataloader-extract-download-performance-improvement"></a>

Improved the performance of the DataLoader Extract file download process. The download now initiates promptly upon user action, reducing extended pending time and ensuring faster response and file availability compared to earlier behavior.

### **nCino Object Migration with Rollback – Stability Fix** <a href="#ncino-object-migration-with-rollback-stability-fix" id="ncino-object-migration-with-rollback-stability-fix"></a>

Resolved an issue where nCino object migrations failed during rollback-enabled feature deployments. The rollback process has been stabilized to prevent errors and ensure successful execution during rollback builds.



















