# nCino Release Notes 26.0

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive nCino release updates!" listId="a085e26e7e" %}

### Release Notes — nCino+DL 26.2.13 <a href="#release-notes-ncinodl-26.2.13" id="release-notes-ncinodl-26.2.13"></a>

**Release Date:** 2026-06-28

#### Latest Templates and Versions Sorting in CI Jobs Features Dropdown  <a href="#latest-templates-and-versions-sorting-in-ci-jobs-features-dropdown-dt-13172" id="latest-templates-and-versions-sorting-in-ci-jobs-features-dropdown-dt-13172"></a>

The **Features** template list and the related **Version/Versions** dropdown in CI Jobs and Feature Deployments now display the most recently changed items first. This allows users to quickly locate and select the latest updated template and version without scrolling through the entire list.

#### Consistent Deploy Destination Org Dropdown Across UIs <a href="#consistent-deploy-destination-org-dropdown-across-uis-dt-13458" id="consistent-deploy-destination-org-dropdown-across-uis-dt-13458"></a>

Fixed an inconsistency where the **Deploy – Dest Org** dropdown in the New UI listed the source org as a selectable target, while the Old UI did not. The behavior is now aligned across both UIs to prevent accidental same-org deployments and eliminate user confusion.

#### External Field Mappings Retained for Post-Approval Deployments <a href="#external-field-mappings-retained-for-post-approval-deployments-dt-13356" id="external-field-mappings-retained-for-post-approval-deployments-dt-13356"></a>

Fixed an issue where configured **external field mappings** were missing when deploying a dataset from **Deployment History** after it had passed the approval process. All mapped fields are now correctly applied during post-approval deployments.

#### Accurate Deployment Status for Dataset Retrieval in Deployment History <a href="#accurate-deployment-status-for-dataset-retrieval-in-deployment-history-dt-13476" id="accurate-deployment-status-for-dataset-retrieval-in-deployment-history-dt-13476"></a>

Fixed an issue where performing a **dataset retrieval** (without an actual deployment) incorrectly showed the status as **Success** in Deployment History. The status now accurately reflects that only retrieval was performed, preventing misleading audit and release validation records.

#### VC-to-VC Commit Deployment to Org Fix <a href="#vc-to-vc-commit-deployment-to-org-fix-dt-13459" id="vc-to-vc-commit-deployment-to-org-fix-dt-13459"></a>

Fixed an issue where a successful **VC-to-VC commit** was followed by a deployment failure with the error _"No objects were retrieved for label: {}"_. The deployment process now correctly retrieves committed components and completes successfully.

## nCino - Release 26.2.12

**Release Date:** **21 June 2026**

#### Custom Field Exclusion for Cleaner nCino Commits and Deployments <a href="#custom-field-exclusion-for-cleaner-ncino-commits-and-deployments" id="custom-field-exclusion-for-cleaner-ncino-commits-and-deployments"></a>

Users can now exclude unwanted Salesforce system fields during nCino commit and deployment review — reducing noise in pull requests and keeping change reviews focused on meaningful business changes.&#x20;

#### Rollback Enabled for Partially Successful Deployments <a href="#rollback-enabled-for-partially-successful-deployments" id="rollback-enabled-for-partially-successful-deployments"></a>

Rollback is now available when a deployment partially succeeds before hitting an error. Previously, any error incorrectly blocked rollback for components that deployed successfully.

#### Fixed Undefined Error When Opening CI Jobs in Old UI <a href="#fixed-undefined-error-when-opening-ci-jobs-in-old-ui" id="fixed-undefined-error-when-opening-ci-jobs-in-old-ui"></a>

Resolved a blocking `undefined` error that appeared when navigating to CI Jobs in the Old UI. CI Jobs now load correctly.

#### Improved Notification Email Visibility in Preview Screens <a href="#improved-notification-email-visibility-in-preview-screens" id="improved-notification-email-visibility-in-preview-screens"></a>

Long notification email addresses in the Deployment and CI Jobs Preview screens now wrap properly instead of being truncated, making it easier to verify notification recipients.&#x20;

***

## nCino - Release 26.2.10

**Release Date:** **7 June 2026**

#### Multi-Level Approvals for nCino Deployments and Commits <a href="#multi-level-approvals-for-ncino-deployments-and-commits" id="multi-level-approvals-for-ncino-deployments-and-commits"></a>

Introduced a configurable multi-level approval workflow for **nCino Data Deployments** and **nCino Commits**, enabling organizations to define **Level 1 (L1)** and **Level 2 (L2)** approvers for deployment and commit activities.

**Key Highlights:**

* Configure L1 and L2 approvers at the branch level.
*   CI JOBs Approver Selection

    <figure><img src="../../../.gitbook/assets/2 (6).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/3 (7).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/4 (7).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/5 (6).png" alt=""><figcaption></figcaption></figure>
*   **Feature Deployment Approver Selection**

    <figure><img src="../../../.gitbook/assets/3 (8).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/4 (8).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/5 (7).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/6 (6).png" alt=""><figcaption></figcaption></figure>
* Approval requests are automatically sent to designated approvers via email.
*   Supports one-approver completion logic, where approval from any configured approver completes the respective approval stage.

    **CI JOB Approvals Flow**

    <figure><img src="../../../.gitbook/assets/7 (6).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/8 (7).png" alt=""><figcaption></figcaption></figure>

    **Feature Deployment Flow**

    <figure><img src="../../../.gitbook/assets/13 (3).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/15 (3).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/16 (3).png" alt=""><figcaption></figcaption></figure>
* Provides approval status notifications, approval reports, and deployment progress updates.
* Includes approval history with approver details, approval status, and comments.
* Automatically rejects pending approval requests after 14 days of inactivity.
* Supports reminder notifications for pending approvals before expiration.
* Prevents users from approving deployments or commits that they created themselves.
* Provides end-to-end visibility into approval status through deployment and commit workflows.

#### RBC Deployment Label Name Auto-Population <a href="#rbc-deployment-label-name-auto-population" id="rbc-deployment-label-name-auto-population"></a>

Fixed an issue where the deployment label name was not auto-populating with the selected Feature/Template name during RBC deployments in the new UI. The label name now auto-fills as expected, matching the old UI behavior.

***

## nCino - Release 26.2.8

**Release Date:** **24 May 2026**

#### CI Job History Pagination Shows Stale Data on Back Navigation <a href="#ci-job-history-pagination-shows-stale-data-on-back-navigation" id="ci-job-history-pagination-shows-stale-data-on-back-navigation"></a>

The pagination now properly refreshes and displays the most up-to-date job data when navigating back and forth, including any newly completed jobs.

#### Removed Salesforce Org Persists in Post-Deployment Activities After Navigation <a href="#removed-salesforce-org-persists-in-post-deployment-activities-after-navigation" id="removed-salesforce-org-persists-in-post-deployment-activities-after-navigation"></a>

The removed org is now correctly cleared and no longer reappears after navigating back and forth during CI Job creation.

***

## nCino - Release 26.2.7

**Release Date:** **17 May 2026**

#### CI Job History Pagination Shows Stale Data on Back Navigation <a href="#ci-job-history-pagination-shows-stale-data-on-back-navigation" id="ci-job-history-pagination-shows-stale-data-on-back-navigation"></a>

Code refactoring for the Feature Commit History module in the New UI, improving maintainability and code quality.

#### Create Feature: New UI Code Refactoring

Code refactoring for the Create Feature module in the New UI, improving maintainability and code quality.

## nCino - Release 26.2.6

**Release Date:** **10 May 2026**

**Create Branch from Feature Deployment**&#x20;

Users can now create a new branch in Version Control directly from the Feature Deployment screen via a new "+" button next to the Branch field. This eliminates the need to navigate to Admin → VC Repos, reducing context switching.

**Null-Safety Fix for nCino Operations**

Fixed a null pointer exception with proper null-safety checks during nCino operations.

**New UI Deployment Screen Freeze Fix**

Fixed the New UI deployment screen freezing when encountering unsupported sObject types. The UI now correctly blocks deployment and stays responsive, matching Old UI behavior.

**CI Build Results Object Click Error Fix**

Fixed a "Request parameters are empty/null" error in the New UI when clicking on objects in successful CI Build Results, which was caused by incorrect API parameter passing.

**Build Trigger Dialog Auto-Close Fix**

Fixed the build trigger dialog not auto-closing after a build is successfully queued. The dialog now dismisses automatically.

***

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



















