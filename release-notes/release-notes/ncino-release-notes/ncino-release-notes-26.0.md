# nCino Release Notes 26.0

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive nCino updates!" %}

## nCino - Release 26.1.5

**Release Date:** **01 February 2026**

#### Feature Deployment Status Handling <a href="#feature-deployment-status-handling" id="feature-deployment-status-handling"></a>

An issue was resolved where a feature deployment could remain stuck in an **IN PROGRESS** state even after successful execution, blocking subsequent deployments. The deployment status handling logic has been corrected to ensure the final state transitions properly, preventing further deployment or integration blocks.

#### Staging Deployment Data Scope <a href="#staging-deployment-data-scope" id="staging-deployment-data-scope"></a>

An issue was fixed where deployments triggered after staging would incorrectly process the entire dataset instead of only the staged data. The deployment logic has been updated to ensure the latest staging iteration is correctly used during deployment.

#### Selective Re-Deployment – External ID Mappings <a href="#selective-re-deployment-external-id-mappings" id="selective-re-deployment-external-id-mappings"></a>

An issue was resolved where External ID mappings were not loading during selective re-deployment iterations. The fix ensures External ID mappings are correctly stored and retrieved as part of the dataset, enabling accurate re-deployments.

***

## nCino - Release 26.1.4

**Release Date:** **25 January 2026**

#### Batch Size Support for Data Migration <a href="#batch-size-support-for-data-migration" id="batch-size-support-for-data-migration"></a>

Reintroduced the **Batch Size** option for data migration to process records in controlled batches, helping manage system load and ensure proper trigger execution during create or update operations in the target org.

#### Feature Deployment – Screens Template Batch Size Handling <a href="#feature-deployment-screens-template-batch-size-handling" id="feature-deployment-screens-template-batch-size-handling"></a>

Resolved an issue where enabling a batch size during the Screens template deployment caused failures by adding validation for CSV file size limits in bulk operations.

#### Forms Manager Template Deployment <a href="#forms-manager-template-deployment" id="forms-manager-template-deployment"></a>

Resolved an issue where Forms Manager template deployments remained stuck in an _In Progress_ state by correcting the handling of self-referenced records during entry object data retrieval.&#x20;

***

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



















