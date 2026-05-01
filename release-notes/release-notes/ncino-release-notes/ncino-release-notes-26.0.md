# nCino Release Notes 26.0

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive nCino release updates!" listId="a085e26e7e" %}

## nCino - Release 26.2.5

**Release Date:** **03 May 2026**

**Selective Deployment Download Scope**\
Fixed an issue where downloading data from a selective deployment iteration exported the entire dataset instead of only the records belonging to that iteration. Downloads now correctly scope to the current iteration.

***

## nCino - Release 26.2.4

**Release Date:** **26 April 2026**

**Server start issue on data retention bucket update**\
Server failed to start when the data retention bucket was updated in the installation file. Fixed to handle bucket configuration changes gracefully.

**nCino Delta jobs failing**\
Delta-based CI Jobs were incorrectly migrating extra objects, causing upsert failures on parent field updates. Fixed delta logic to deploy only the intended object.

**Re-login prompt for sub-users without Commit History access**\
Sub-users without Commit History permission were shown commit-related actions and prompted to re-login on click. Fixed to hide these options for users lacking the required permission.

**Compare for sub-users**\
Sub-users with Feature Deployment and Deployment History access received a 401 Unauthorized error on Compare. Fixed authorization to allow Compare for users with correct permissions.

**Sub-user permission and roles issue in new UI**\
Feature Deployment module was visible to sub-users even without permission, and granting creation access didn't auto-grant history access. Fixed permission enforcement and default role assignment.

**Field Configuration RBC failures**\
Parent Route values were being cleared during deployment when multiple references to the same parent existed. Also fixed self-referencing parent Screen Sections not being picked up.

***

## nCino - Release 26.2.3

**Release Date:** **26 April 2026**

**Re-login prompt when going to nCino Deployment History tab in new UI**

* Non-admin users were prompted to re-login when accessing the Deployment History tab in the nCino module on the new UI. After re-login, they still could not view the module. This issue did not occur in the old UI. Fixed to allow proper access without re-login prompts.

**nCino Rollback not working**

* nCino CI Job rollback was failing because the agent could not locate the required backup directory from the previous build. The baseline revision was also incorrectly updating on failed/partial/rollback builds. Fixed rollback flow and ensured baseline revision only updates on successful deploy builds.

***

## nCino - Release 26.1.13

**Release Date: 29 March 2026**

**Streamlined Feature Migration Logging**

HTTP response bodies are no longer logged in standard logs. Logging now captures only essential details such as status, endpoint, request ID, and response time—reducing log noise and improving security.

***

## nCino - Release 26.1.11

**Release Date: 15 March 2026**

**View Dataset Pagination Improvement**

Pagination has been improved in the **View Dataset** functionality to ensure records are retrieved and displayed in paginated responses instead of loading the entire dataset at once. This enhancement improves performance and reduces response times when working with large datasets.

**Feature Management – Change Log Action Stability Fix**

An issue was resolved in the **Feature Management** module where clicking the **Change Log** action triggered a console error in the New UI. The issue occurred due to an undefined reference while accessing the change log data. This has been fixed, and the **Change Log** action now loads correctly without any console errors.

**Compare Module – Icon Update**

The icons for **Global Compare** and **Field-Level Compare** in the **Compare module** have been updated with new icons to improve visual clarity and consistency in the user interface.

***

## nCino - Release 26.1.8

**Release Date: 22 February 2026**

**CI Jobs & Feature Deployment – Version Control Merge Enhancement**

Enhanced version control behavior to ensure data from **CI Jobs & Feature Deployment** branches is seamlessly merged into the intended target branches. Merging into the same source branch is now restricted to prevent unintended updates.

**CI Jobs – “Features” Selection Improvement**

Resolved an issue with the select all **“Features”** functionality in CI Jobs to ensure accurate and seamless selection of all available features.

***

## nCino - Release 26.1.7

**Release Date:** **15 February 2026**

**Relational Compare – Select All Fix**

Resolved an issue where selecting **“All”** in Parent or Child relational compare was staging all object records instead of only the related records. The logic has been corrected to ensure only the relevant, user-selected records are included.

**Data Comparison Step Status Display Fix**

Fixed an issue where the **Data Comparison** step was not marked as completed. The correct current step is now updated in staging iteration details, and irrelevant steps are skipped in the UI.

***

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



















