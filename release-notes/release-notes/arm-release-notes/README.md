# ARM Release Notes

## ARM 25.2.8 Release Notes <a href="#title-text" id="title-text"></a>

#### Release Date: 8 June 2025 <a href="#release-date-08th-june-2025" id="release-date-08th-june-2025"></a>

### **Overview** <a href="#overview" id="overview"></a>

This release brings critical improvements and feature enhancements across multiple modules, including Environment Provisioning, CI Jobs, Admin, EZ-Merge, and Metadata handling. The updates aim to improve system flexibility, performance, and metadata deployment consistency.

### Bug Fixes and Improvements

#### **1. Fix / Improvement** <a href="#support-ticket-123971" id="support-ticket-123971"></a>

**Issue:** In Environment Provisioning, the Remote Site Settings template was failing to update the URL in the destination org when the user applied alphabetical sorting. This caused deployment inconsistencies.

**Fix:** Now, the template can update remote site settings correctly regardless of alphabetical sorting. Sorting by Remote Site Name or Remote Site URL no longer blocks the update process. Validation has been completed in the integration branch.

**Module:** Environment Provisioning

#### **2. Fix / Improvement** <a href="#support-ticket-139461" id="support-ticket-139461"></a>

#### **Issue:** Customers could not edit SSO domain changes directly from the platform, leading to manual intervention. <a href="#support-ticket-139461" id="support-ticket-139461"></a>

**Fix:** Users can now update their SSO domain name via the **SSO Configuration** page. Once the domain name is changed, an automated email informing all users of the update is triggered.

**Module:** Admin → My Account → SSO Configuration

#### **3. Fix / Improvement** <a href="#support-ticket-140173" id="support-ticket-140173"></a>

**Issue:** While attempting to delete static resources and their `.meta` files through EZ-Merge, no destructive changes package was being generated, even when the "Run Destructive Changes" checkbox was selected. This caused validation failure during merge.

**Fix:** Destructive logic has been implemented in EZ-Merge for both DX and non-DX formats, ensuring static resource deletions are correctly handled and packaged.

**Module:** EZ-Merge

#### **4. Fix / Improvement** <a href="#support-ticket-141127" id="support-ticket-141127"></a>

**Issue:** CI Job deployments were failing with a **504 Gateway Timeout** error, blocking staging environment activities and causing delays in deployment pipelines.

**Fix:** Optimized the CI Job execution logic by improving how API timeouts are handled. This ensures better performance and avoids timeout-related failures during large or slow deployments.

**Module:** CI Jobs

#### **5. Fix / Improvement** <a href="#support-ticket-140243" id="support-ticket-140243"></a>

**Issue:** While running test classes in the Admin section, unrelated Apex test classes were being auto-populated.

**Fix:** The auto-population logic was revised to ensure only relevant Apex classes are retrieved and saved. Unrelated classes are now excluded from test jobs.

**Module:** Admin → My SF Org Management

#### **6. Fix / Improvement** <a href="#support-ticket-140384" id="support-ticket-140384"></a>

**Issue:** During CI Job deployments involving Search and Substitute rules, changes were not being applied to the destination org, even though the deployment was marked successful.

**Fix:** Provided Fix and also Extended support to apply substitution logic to the following metadata types:\
AutoResponseRule, CustomLabel, CustomMetadata, CustomObject, CustomSite, Dashboard, DashboardFolderShare, Network, NamedCredential, PermissionSet, Portal, Queue, RemoteSiteSetting, Report, ReportFolderShare, SamlSsoConfig, SharingCriteriaRule, SharingOwnerRule, and Workflow.

**Module:** Search and Substitute

#### **7. Fix / Improvement** <a href="#support-ticket-141464" id="support-ticket-141464"></a>

**Issue:** When performing a destructive change (e.g., deleting a ProfileSearchLayout) and deploying via Single Revision, the system failed to identify the change correctly, expecting the metadata to be present instead.

**Fix:** The Retrieve Metadata screen now correctly classifies added/modified ProfileSearchLayout changes under "ALL ITEMS" and does not falsely tag them as missing. For Non-DX Deployments and CI Jobs, ProfileSearchLayout changes now appear as constructive updates and deploy successfully.

**Behavior Limitation:** If a Custom Object contains only a single ProfileSearchLayout node and that node is deleted, the change will not be picked up during deployment, as ProfileSearchLayout is not a standalone metadata type.

**Module:** Deployment / CI Jobs

***

## Release Notes 25.2.7 <a href="#title-text" id="title-text"></a>

**Release date: 1 June 2025**

### **Overview** <a href="#overview" id="overview"></a>

This release improves metadata handling and deployment type consistency and enhances support for Vlocity and Permission Set delta deployments. Several critical fixes have been addressed across the Deployment, CI Jobs, and EZ-Commit modules to improve reliability and reduce deployment anomalies.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

#### **Fix/Improvement 1**

* **Issue:** When deploying a new profile search layout for the **Case object**, the deployment unintentionally removed all other existing profile search layouts in the org, causing a loss of metadata settings for other profiles.
* **Fix:** The logic in the deployment backend (`CustomObjectController.java`) has been **refactored**. It now compares layout differences in an **additive** manner, ensuring that new layouts are added without deleting existing ones.
* **Impacted Module:** Deployment

#### **Fix/Improvement 2**

* **Issue:** The “**Enable Delta on Permission Sets**” checkbox is designed to ensure only changed permissions are committed or deployed. While it did not work correctly for **CI Jobs**, object permissions were still getting removed even when the checkbox was enabled.
* **Fix:** The delta behavior is now **standardized** across both CI Jobs and Deployments. A back-end code fix ensures that object permissions are preserved in deployments sourced from version control (SCM) and delta logic is honored properly.
* **Impacted Modules:** CI Jobs, Deployment

#### **Fix/Improvement 3**

* **Issue:** During **Vlocity SF Org-to-Org** deployments, YAML files failed to handle **Calculation Matrix fields** with comma-separated values that included spaces. This broke deployments and made the downloaded DataPacks unusable.
* **Fix:** The YAML generation process was enhanced to support such field values. Now, comma-separated **Calculation Matrix components** are parsed and deployed correctly to the target org. YAML downloads are also displayed properly.
* **Note:** This fix currently applies **only to Org-to-Org Vlocity deployments**. Support for Vlocity deployments via **Version Control** is under R\&D.
* **Impacted Module:** Deployment (Vlocity SF Org-to-Org)

#### **Fix/Improvement 4**

* **Issue:** While configuring **ScheduleApexClassesMonthly** templates in the **Environment Provisioning** module, all default user fields were incorrectly set to **Analytics Cloud Integration User**, regardless of what the template intended.
* **Fix:** The back-end logic for template value assignment was fixed. It now correctly pulls in the **actual default values** specified in the template configuration.
* **Impacted Module:** Environment Provisioning

#### **Fix/Improvement 5**

* **Issue:** A customer was performing a merge using a commit that contained **only destructive changes**. Even though the **"Destructive Changes"** checkbox was enabled, the merge failed during the **Validate Deploy** stage.
* **Fix:** Salesforce expects both a `postdestructivechanges.xml` and an empty `package.xml` file for validation to pass. The fix ensures that an **empty** `package.xml` **file** is now automatically added to the package folder, along with destructive changes, making the validation step successful.
* **Impacted Module:** EZ-Merge with Validate Deploy

#### **Fix/Improvement 6**

* **Issue:** While using a previously validated commit label to perform a new **EZ-Commit**, customers were unable to see the **RecordType** component under the “All Metadata Components” tab.
* **Fix:** The component filtering logic was corrected to ensure that **RecordType** and similar metadata types are displayed when using commit templates, improving usability and completeness of the commit UI.
* **Impacted Module:** EZ-Commit

## Release Notes 25.2.6 <a href="#title-text" id="title-text"></a>

**Release Date: 25 May 2025**

### **Overview**

This release focuses on stability, reliability, and enhanced usability across core modules like CI Jobs, EZ-Commit, and Release Management. Key improvements address long-standing issues such as CI job queue blocks, premature status transitions during aborts, metadata filtering inconsistencies, and usability fixes in user management.

We’ve also added support for Provar v25.2.1, improved error handling and logging, and ensured a smoother experience for EZ-Commit users leveraging custom metadata and commit labels.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

#### **1. Release label Abort Stuck Status** <a href="#id-1.-release-abort-stuck-status" id="id-1.-release-abort-stuck-status"></a>

**Issue:**\
When a user aborts a release label, the system prematurely sets the release status to **"Failed"** while the abort request to the agent is still pending. If the abort request isn’t successfully sent, the status gets stuck, causing confusion in monitoring and troubleshooting.

**Fix:**\
The system now updates the release status to **“Failed”** only after the agent successfully triggers and acknowledges the abort request. Extra logging has been added to help trace abort scenarios and ensure proper state transitions.

**Impacted Module:** Release label Management

#### **2. EZ-Commit Metadata Filter with Reused Labels** <a href="#id-2.-ez-commit-metadata-filter-with-reused-labels" id="id-2.-ez-commit-metadata-filter-with-reused-labels"></a>

**Issue:**\
When performing an EZ-Commit using the **SCA > CodeScan** option and enabling **“Only newly added supported metadata types,”** the commit wasn’t functioning properly if the user reused a previously used commit label.

**Fix:**\
Metadata filtering logic has been updated to support commit label reuse, ensuring seamless functionality with **Auto Draft**.

**Impacted Module:** EZ-Commit

#### **3. CI Jobs Stuck in Queue** <a href="#id-3.-ci-jobs-stuck-in-queue" id="id-3.-ci-jobs-stuck-in-queue"></a>

**Issue:**\
Some CI jobs were getting stuck in the queue due to:

* Unhandled exceptions
* Git commit failures where no revision was generated

**Fixes:**

* Prevented downstream processes when Git fails to generate a revision
* Improved handling for null messages and unexpected errors
* Added enhanced logging to support better troubleshooting

**Impacted Module:** CI Jobs

#### **4. Admin User Creation Validation** <a href="#id-4.-admin-user-creation-validation" id="id-4.-admin-user-creation-validation"></a>

**Issue:**\
Fields like **Phone Number**, **Zip Code**, and **State** were mandatory during user creation, restricting onboarding in certain cases.

**Fix:**\
These fields are now optional in the Admin module, streamlining user creation.

**Impacted Module:** Admin (User Management)

#### **5. Fieldset Translation Removal During Commit** <a href="#id-5.-fieldset-translation-removal-during-commit" id="id-5.-fieldset-translation-removal-during-commit"></a>

**Issue:**\
When committing **CustomField** and **CustomObjectTranslations**, valid **Fieldset translation nodes** were unintentionally removed.

**Fix:**\
Translation node handling has been refined to preserve valid entries and prevent data loss in multilingual configurations.

**Impacted Module:** EZ-Commit

#### **6. Credential-Based CI Job Failures** <a href="#id-6.-credential-based-ci-job-failures" id="id-6.-credential-based-ci-job-failures"></a>

**Issue:**\
CI Jobs were failing inconsistently when using existing credentials, with causes difficult to trace.

**Fix:**\
Improved logging at credential validation points to isolate issues and aid future debugging.

**Impacted Module:** CI Jobs

#### **7. Provar v25.2.1 Compatibility Support** <a href="#id-7.-provar-v2521-compatibility-support" id="id-7.-provar-v2521-compatibility-support"></a>

**Request:**\
Compatibility needed for **Provar version 25.2.1** to support automated test execution.

**Update:**\
Provar v25.2.1 is now supported and available on demand for integration with ARM workflows.

#### **8. Branch Name Case Sensitivity in Release Labels** <a href="#id-8.-branch-name-case-sensitivity-in-release-labels" id="id-8.-branch-name-case-sensitivity-in-release-labels"></a>

**Issue:**\
Sub-users could not view their own release labels due to a mismatch in branch name casing logic.

**Fix:**\
The filtering logic now respects case sensitivity, ensuring correct visibility of release labels.

**Impacted Module:** Release Label Management

***

## Release Notes 25.2.5  <a href="#title-text" id="title-text"></a>

**Release Date: 18 May 2025**\
\
**Overview**

This release includes key bug fixes and improvements focused on enhancing CI Job stability, deployment reliability, and metadata diff accuracy. It addresses critical issues encountered in Salesforce-to-Salesforce deployments, destructive change logic, permission set handling, and package creation workflows. Additionally, customer-requested upgrades such as Provar support enhancements have been implemented.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

#### **1. CI Job: Destructive Changes Handling** <a href="#id-1.-ci-job-destructive-changes-handling" id="id-1.-ci-job-destructive-changes-handling"></a>

**Issue:**\
The **“Prepare Destructive Changes”** option was not selected during initial CI Job creation but was unexpectedly selected during re-runs.

**Impacted Modules:**

* Deploy a package from Salesforce to Salesforce
* Deploy a package from Salesforce to Salesforce and back up to Version Control

**Fix:**\
Resolved inconsistencies in destructive change logic. The system now retains the correct state of the “Prepare Destructive Changes” flag across CI Job executions.

#### **2. Permission Set FLS Diff Missing** <a href="#id-2.-permission-set-fls-diff-missing" id="id-2.-permission-set-fls-diff-missing"></a>

**Issue:**\
When attempting to commit FLS changes for a new field within a permission set, the changes were not captured in the diff report, resulting in missing commits.

**Fix:**\
Enhanced logic to correctly capture FLS changes by appending `Task` and `Event` objects for the `Activity` object when the **Global Permissions** option is selected in EZ-Commit.

#### **3. Deployment Abort Functionality** <a href="#id-3.-deployment-abort-functionality" id="id-3.-deployment-abort-functionality"></a>

**Issue:**\
When performing a **Single Revision Deployment**, even after aborting it (a confirmation popup showing a successful cancellation), the deployment continued and was marked as successful.

**Fix:**\
Fixed the abort logic within the deployment module to correctly halt execution and reflect the accurate status post-abortion.

#### **4. Unlocked Managed Package CI Job Failure** <a href="#id-4.-unlocked-managed-package-ci-job-failure" id="id-4.-unlocked-managed-package-ci-job-failure"></a>

**Issue:**\
Customer experienced failures when triggering a CI Job to **create and install an unlocked managed package** from a version control branch.

**Fix:**\
Improved JSON handling during CI Job execution, ensuring compatibility with both internal and customer-specific JSON structures. Now, even in case of exceptions during package creation, the system attempts fallback version creation instead of complete failure, similar to the existing SFDX module behavior.

#### **5. Provar Upgrade Request** <a href="#id-5.-provar-upgrade-request" id="id-5.-provar-upgrade-request"></a>

**Request:**\
Customer requested support for **Provar v25.2.1**

**Update:**\
Support for Provar version 25.2.1 has been added to ensure compatibility with automated test execution workflows. This version will be available on a demand basis.

***

## Release Notes 25.2.4

**Release Date: 11 May 2025**

### **Overview**

This release introduces feature enhancements and key bug fixes to improve deployment flexibility, metadata handling, CI job stability, and user experience. The update includes enhanced error handling for CI and Apex jobs, metadata recognition updates, and refined UI behavior in merge and licensing workflows.

### **Bug Fixes & Improvements**

**CI Job Includes Unsupported Metadata Despite Exclusion Configuration**\
A customer reported that certain metadata types (`CallCenterRoutingMap`, `CallCtrAgentFavTrfrDest`) were deployed despite being explicitly excluded in the deployment configuration.

Upon investigation, the data related to `CallCenterRoutingMap` was retrieved and verified successfully. However, data for `CallCtrAgentFavTrfrDest` could not be validated.

These metadata types are associated with Salesforce Service Voice features, which require full integration with a compatible telephone system. Currently, such an integration is unavailable in our environment, limiting our ability to validate the issue fully.

* **Fix:** Few metadata types are officially supported and recognized correctly in deployments.
* **Impacted Module:** CI Jobs

**Repository URL Migration**\
A customer-requested repository URL migration has been completed.

* **Fix:** Migration was successful, and no further issues were reported.
* **Impacted Module:** Repo Management

**Profile Comparison Error: “Salesforce Org Doesn’t Exist”**\
An error occurred when comparing profiles across 2 or 3 environments.

* **Fix:** UI logic for diff loading has been refined to handle multi-org comparisons.
* **Impacted Module:** Metadata Comparison

**CI Job Fails When All Standard Value Sets Are Excluded**\
CI Jobs failed to run if standard value sets were excluded from selection.

* **Fix:** Job logic updated to handle scenarios where standard value sets are excluded.
* **Impacted Module:** CI Jobs

**Failure in Scheduled Apex Test Runs for Production Orgs**\
Daily scheduled Apex test executions failed due to an issue handling multiple concurrent jobs.

* **Fix:** Logic in `ApexTestClassesSchedulerJob` refined to support multiple scheduled jobs.
* **Impacted Module:** Apex Test Scheduling

**Text Change in Merge Screen UI**\
The label was changed from “Skip all three prevalidation criteria” to “Skip all prevalidation criteria” for better clarity.

* **Impacted Module:** Merge UI

### **Known Issues** <a href="#known-issues" id="known-issues"></a>

**License Upload Not Visible for Expired On-Premise Servers**\
When the license expired, the option to upload a new key was not visible before login.

* **Fix:** The pop-up visibility issue was resolved; users can now upload the license before logging in.
* **Impacted Module:** Licensing (On-Prem)
* **Issue Type:** UI Bug

***

## Release Notes 25.2.3

**Release Date:** **4 May 2025**

#### Overview

This release of **AutoRABIT ARM** introduces key bug fixes and stability improvements to deployment label handling, CI job webhook executions, and user management across regions. Notably, a critical internal issue affecting metadata filtering during full deployments has been addressed. Additionally, issues related to saving users for countries without state-level details and CI job webhook failures have been resolved.

### Bug Fixes and Improvements

**Issue with Full Deployment - Previous Deployment Label Type**

A defect was identified when performing a full deployment using the “Previous Deployment Label” type, which inadvertently included all metadata members from the source organization, rather than only those associated with the selected label.

**Fix:** Updated deployment logic now ensures that only metadata within the selected label is included in the deployment.\
**Impacted Modules:** Deployments

**Webhook Execution Failures in CI Jobs**

Webhooks were not being executed during CI job runs due to limitations in DynamoDB.

**Fix:** Webhook invocation logic has been revamped to ensure reliable webhook execution in CI pipelines.\
**Impacted Modules:** CI Jobs

**User Creation Failure – Countries Without States**

An issue was reported where creating or editing users with countries that do not have states (e.g., Singapore, American Samoa, Andorra) failed to save the user details.

**Fix:** Validation logic has been updated to treat the state field as optional for applicable countries, ensuring successful user creation.\
**Impacted Modules:** User Management

***

## Release Notes 25.2.2

**Release Date:** **27 April 2025**

#### **Overview** <a href="#overview" id="overview"></a>

This release introduces significant enhancements to AutoRABIT’s ARM platform, focusing on enhanced metadata support, improved deployment accuracy, and optimized performance across CI workflows. Previously unsupported metadata types are now fully recognized in DX-based branching and deployment. Issues with redundant code coverage reports and performance bottlenecks in ALM item loading have been resolved. Significant improvements also include full profile permission coverage in EZ-Commit and enhanced metadata exclusion logic.

#### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

**Support for New Metadata Types in DX Repo CI Deployments**\
Previously unsupported metadata types are now included in deployments created through DX repo-based branching. These include: `ApplicationSubtypeDefinition`, `BusinessProcessTypeDefinition`, `ConvIntelligenceSignalRule`, `ExplainabilityActionDefinition`, `ExpressionSetDefinitionVersion`, `ForecastingGroup`, and `PathAssistant`.\
**Impacted Modules:** CI Jobs (DX Branching & Deployments)

**Code Coverage Report Duplication Fixed**\
Resolved an issue where multiple code coverage reports were generated for the same sandbox. The back-end logic has been updated to ensure that only one report is created per sandbox.\
**Impacted Modules:** Code Coverage Reports

**Improved ALM Item Load Time in Commit/Merge Modules**\
Addressed severe performance lag when loading Azure ALM items after sprint selection. Switched to batch API calls for fetching work item data and states, reducing calls from thousands to single digits. Load time dropped from \~6 minutes to \~4 seconds for large sprints.\
**Impacted Modules:** Commit/Merge (ALM Integration with Azure)

**Full Profile Commit – Object Permissions & Tab Visibility Fixes**\
Fixed missing object permissions (Documents, Push Topics) and tab visibilities (Reports, Dashboards) in full profile commits during EZ-Commit. The package.xml generation logic now correctly includes all necessary metadata members.\
**Impacted Modules:** EZ-Commit, Profiles

**Metadata Exclusion Logic Improved – ExpressionSetDefinitionVersion**\
Corrected behavior in which `ExpressionSetDefinitionVersion` metadata was included in deployments, even when excluded. This enhancement enables precise control over metadata exclusions, particularly for workflows that require separate deployment flows (e.g., OmniStudio jobs).\
**Impacted Modules:** CI Jobs, Deployment

***

### nCino + Data Loader Release Notes 25.1.4

**Release Date: 27 April 2025**

Refer to the latest release notes published for nCino + Data Loader at [https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes](https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes).

***

### ARM Release Notes 25.2.1 <a href="#arm-release-notes-25.2.1" id="arm-release-notes-25.2.1"></a>

**Release Date: 20 April 2025**

#### **Overview** <a href="#overview" id="overview"></a>

This release brings meaningful enhancements that improve reliability, accuracy, and visibility across ARM workflows. Backup CI jobs now consistently capture StandardValueSet changes, ensuring more complete metadata tracking. Improved metadata classification prevents deployment errors, while CustomObjectTranslation handling in EZ-Commit for DX repos is now more precise. Custom settings deploy smoothly through Environment Provisioning, reducing manual effort. File comparisons are clearer with restored full diff visibility, aiding better change reviews. Updates to Search and Substitute and managed package exclusions streamline CI deployments. Audit trails now display correct timestamps, enhancing reporting accuracy.

#### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

**StandardValueSet Metadata in Backup Jobs** Backup CI jobs now correctly detect and retrieve changes made to StandardValueSet metadata. Previously, these changes were not captured automatically, although manual commits through EZ-Commit functioned as expected. This enhancement ensures StandardValueSet changes are included in automated daily backups. _Impacted Modules: CI Jobs backup to VC. Support Case: #132829_

**Metadata Type Detection for Custom Metadata Labels** Improved handling of custom metadata with labels starting with "profile" or "permissionset" by validating based on their file paths instead of label names. The system now checks for `profiles/` and `permissionset/` in metadata paths to accurately categorize them during commit, merge CI jobs, and deployments. This resolves previous misclassification issues. _Impacted Modules: All Modules._

**CustomObjectTranslation Handling in DX Repositories** Improved the EZ-Commit process to correctly handle CustomObjectTranslation metadata in DX repositories. Previously, some nodes were unintentionally removed, and unrelated changes like validation rules appeared in the compare changes section. The commit process now includes only selected components, matching the behavior of non-DX repositories. _Impacted Modules: EZ-Commit while selecting 'customobjecttranslation' \[DX/NonDX]._

**Custom Settings Deployment in Environment Provisioning** Resolved an issue where custom settings were not being deployed through the Environment Provisioning module. Although no errors were shown on the history page, specified changes were not applied. This enhancement ensures that custom settings are now correctly deployed as part of the provisioning process. _Impacted Modules: Env Pro -> migrate custom settings._

**File Difference Display in Comparison Dialog** Fixed an issue where the comparison dialog box did not consistently display full file differences for all metadata types. Previously, the UI showed only a limited number of lines without offering a "Load More" option, while the downloaded file revealed additional differences. The "Load More" functionality has been restored, now loading up to 200 lines per click to ensure complete visibility of metadata changes. _Impacted Modules: Compare Metadata in Deployment Module._

**Search and Substitute for Workflow Alerts in CI Jobs** Resolved an issue where applying Search and Substitute rules on Workflow Alerts in SFDX repositories caused CI jobs to fail. The error was due to a logic fault, which has now been corrected. Common code has been refactored and moved to the pipeline to ensure consistent execution across jobs. _Impacted Modules: CI Jobs, Deployment, and Pre-Validation Commit._

**Exclusion of Managed Components in SFDX CI Job Deployments** Fixed an issue where managed components were not properly excluded during SFDX CI job deployments, despite selecting "Ignore installed packages" and configuring exclusions under the Skip Members section. The deployment logic has been corrected to ensure managed components are now accurately excluded as intended. _Impacted Modules: Deployments & CI Jobs._

**Date and Time Accuracy in Audit Trails** Corrected the logic used for date and time conversion in the UI of the Reports Audit Trail. Previously, the created and modified dates were displayed inaccurately. This enhancement ensures that audit timestamps now reflect the correct values. _Impacted Modules: Audit Report._

***

## ARM Release Notes 25.1.4

**Release Date: 17 April 2025**

### Overview <a href="#overview" id="overview"></a>

This release focuses on streamlining the deployment process and improving reliability across the platform. OmniStudio deployments now handle dependencies more intelligently with Max Depth -1, ensuring a smoother experience from retrieval to deployment. Conflict resolution has been made more precise, avoiding issues like content bleed between files, and users can now seamlessly retry failed merges without losing progress. Improvements to Org Sync and Admin settings make it easier to spot differences and manage roles in real time, while enhancements to file comparison and commit labeling bring greater clarity and control to the deployment workflow.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

* **Max Depth -1 Support for OmniStudio Deployment**\
  Deployments using Max Depth -1 now correctly retrieve and include all dependent components such as IntegrationProcedure, DataRaptor, Document, and VlocityUiTemplate. The retrieved dependencies are now properly reflected in the UI and included in the deployment to the target org. _Impacted Modules: Deployment (org → org)._&#x20;
* **Improved Conflict Resolution Accuracy**\
  Resolved an issue where content from previously resolved files was being incorrectly appended to other files during conflict resolution. This fix ensures each conflicted file is processed independently, preventing errors such as duplicate labels during deployment. _Impacted Modules: EZ-Merge → Conflicts._&#x20;
* **Retry Commit for EZ-Merge After Failure**\
  The "Retry Commit" option is now available when a merge fails due to incorrect or unmapped credentials. The system correctly updates the merge status to "CommitPending," enabling users to retry the commit. This fix applies to new merges created after this release. _Impacted Modules: EZ-Merge, Dry run merge._&#x20;
* **Enhancement: Accurate Filtering in Org Sync**\
  The 'Exists in Source Only' filter in Org Sync now accurately reflects the actual number of differing metadata groups. With this fix, both the group count and displayed results are consistent and reliable. _Impacted Modules: Org Sync._&#x20;
* **Immediate Visibility of 'Skip Org Mapping' Option**\
  The 'Skip Org Mapping' permission is now immediately visible in the Roles tab after enabling 'Skip Mappings' on a user’s profile. Previously, a page refresh was required for the option to appear. This enhancement ensures the setting is saved and reflected instantly without additional user actions. _Impacted Modules: Admin._&#x20;
* **Whitespace Differences in File Diff View**\
  The File Diff tab now displays whitespace-only changes when comparing Apex Class files. Previously undetected space differences are now identified and shown, ensuring accurate comparison between source and destination files. _Impacted Modules: Org Sync and Deployments._
* **Vlocity Commit Label Filtering**\
  Commit labels associated with Vlocity metadata can now be filtered correctly using the commit label name in the merge screen. Previously created labels without commit type are also supported following a back-end migration fix. _Impacted Modules: VC → Change labels → Commit labels._
* **Support for Initial Commit in Revision Range Deployment**\
  Salesforce metadata changes from the initial commit are now included in the retrieve metadata screen when selected as the "From Revision" in a revision range deployment. This ensures changes from both the initial and target revisions are accurately reflected and deployed. _Impacted Modules: Custom Deployments - Revision range, single revision._

***

## ARM Release Notes 25.1.3

**Release Date: 06 April 2025**\
\
This release introduces significant new capabilities and key enhancements across the ARM platform. A major new feature enables **multi-level deployment approvals by Org**, offering structured release governance with customizable approval groups. Architecture improvements include enhanced **global workspace management** to handle deleted or missing branches more gracefully. The release also strengthens security with **encrypted installation key** handling. Core functionality has been optimized, including improved **commit revision sorting** and **faster loading of standard value sets**.

#### **1. New Feature** <a href="#id-1.-new-feature" id="id-1.-new-feature"></a>

* **Multi-Level Deployment Approval by Org**\
  A two-level deployment approval process has been introduced to provide better control over releases. Each approval level supports group-based approval, allowing any member within the group to approve the deployment. Email notifications are sent to approvers with a link to ARM for approval actions. This approval process can be configured based on Org name. Admins can select applicable orgs and assign separate approvers or approver groups for each.\
  \
  **Note:** Approval Process support is now limited to **Direct Custom Deployment** only. It is **not supported** via **Org Sync** or **Profile Management**.

#### **2. Feature Enhancements** <a href="#id-2.-feature-enhancements" id="id-2.-feature-enhancements"></a>

* **Secure Handling of Installation Key in Unlocked Packages CI Job**\
  The installation key used in the Unlocked Packages CI Job is now masked and encrypted for improved security. Additionally, a view/hide eye icon has been introduced to toggle the visibility of the installation key.
* **Clear Status Indicators for Merge Pre-validation Outcomes**\
  The "Merge Prevalidation Process" logs now provide clearer visual indicators based on the outcome of the validation. A green checkmark ( <mark style="color:green;">✓</mark>) is shown only when the process completes successfully, while a red <mark style="color:red;">X</mark> clearly indicates when the pre-validation has failed or resulted in auto-rejection. This improvement ensures better visibility into validation outcomes for both merge and commit workflows.

#### 3. Architecture Improvements <a href="#id-3.-architecture-improvements" id="id-3.-architecture-improvements"></a>

* **3-Tier Architecture for ARM – Separate and Load the UI and Backend Services Individually**\
  The ARM UI can now be compiled and run independently from the backend. Based on configurable endpoints, the UI communicates with any designated backend server, defaulting to localhost. All UI components load locally, and API calls are routed according to the configured backend endpoint.
*   **Resilience in Global Workspace Management for Optimized Workspaces**\
    A backend fix has been implemented to ensure stability in global workspace creation when the default branch is missing or deleted in the repository. When the default branch no longer exists in AutoRABIT or the remote repository, the system will now automatically update the global workspace and repository configuration to use the last valid branch. This prevents version control operations—such as commit, merge, or revision listing—from being blocked due to a broken global workspace.

    A UI enhancement to allow users to change the default branch directly in the VC Repos module will be introduced in an upcoming release to fully resolve the issue.

#### **4. Bug Fixes and Improvements** <a href="#id-4.-bug-fixes-and-improvements" id="id-4.-bug-fixes-and-improvements"></a>

* **Reliable CI Job Queue Handling**\
  Resolved an issue where CI jobs were stuck in the queue due to mismatched build numbers between CIJobInfo and CIJobHistory tables. The system now handles these cases correctly, ensuring jobs progress without blocking subsequent builds. _Impacted Modules: CI Job abort and Queue flows, Release Label abort and Queue flows._&#x20;
* **CustomNotificationType Support in Destructive Commits**\
  Destructive commits now support the CustomNotificationType metadata. _Impacted Modules: Commits, Merges, Release Label Artifact execution, CI Jobs, Deployments while performing the Custom Notifications type destructive changes flow._&#x20;
* **Package Key Handling in Deployment Module**\
  Resolved an issue where deployments failed due to a null package key during package version installation. The key preparation logic for dependent packages has been corrected, and a migration has been implemented to fix existing invalid keys. _Impacted Modules: Unlocked packages, Deployments._&#x20;
* **LWC API Check Support in CodeScan Analysis**\
  Files with `.js-meta.xml` suffixes are now included in the CodeScan analysis, enabling proper API checks on Lightning Web Components (LWC) from ARM. This ensures more accurate validation during the scan process. _Impacted Modules: ARM CodeScan integration._&#x20;
* **Accurate File Name Display in Review Artifact**\
  The Review Artifact UI now correctly updates the file name when switching files, ensuring clarity while reviewing changes. _Impacted Modules: EZ Commit -> Review-Artifact -> Edit In IDE -> File Names in editor view._&#x20;
* **Commit Revisions Sorted by Committed Timestamp**\
  Commit revisions in the Commit module are now displayed based on the committed timestamp, aligning with GitHub's behavior. Previously, revisions were shown using the author timestamp, causing confusion. The backend logic has been updated to ensure commits are sorted and displayed consistently. _Impacted Modules: New Deployment, New CI Jobs, New Merge, VC Repositories, Release Labels._&#x20;
* **Support for Special Characters and Extended Name Lengths in User Profiles**\
  User profile fields now support special characters in first and last names. Additionally, the character limits have been extended—first names now allow 3 to 40 characters, and last names allow 1 to 80 characters. _Impacted Modules: Admin, My Profile._&#x20;
* **Support for Priority 4 Rules in Apex PMD Static Code Analysis**\
  Static Code Analysis now includes Priority 4 rule violations in Apex PMD reports. The minimum PMD priority has been updated from Medium (3) to Low (5), allowing visibility into lower-priority issues without affecting CI Job validations configured to fail only on higher priority errors. _Impacted Modules: All static code analysis running with Apex PMD._&#x20;
* **Optimized Loading of Standard Value Sets in Commit**\
  Improved performance and visibility of Standard Value Sets in the EZ-Commit module by minimizing repeated Salesforce API calls. The system now retrieves enabled services during org registration and stores the cloud org type in the database. For existing orgs, the cloud type is updated during retrieval and used for subsequent requests, significantly reducing load times and ensuring correct metadata visibility—especially for Financial Services Cloud orgs. _Impacted Modules: EZ-Commit, Commit Templates, Branching Baseline, Deployments, CI Jobs._&#x20;
* **Provar Plugin Name Edit Handling**\
  Editing the Provar name in the Admin module no longer triggers an invalid notification pop-up when a key file is already uploaded. A response check ensures smoother and more accurate user feedback. _Impacted Modules: My Account plugins (Provar)._

## **nCino + Data Loader 25.1.3 Release Notes**

**Release Date: 6 April 2025**\


See the [Release Notes](https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.3-release-notes) for nCino + Data Loader improvements.&#x20;

***

## ARM Release Notes 25.1.2

**Release Date: 09 March 2025**

This release introduces **Checkmarx One Integration**, enabling users to perform security scans within ARM using Checkmarx One alongside existing Static Code Analysis tools.

Additionally, we have addressed multiple bug fixes and enhancements, including improved support for **PLATFORMEVENTCHANNELMEMBER** in destructive commits, enhanced **merge conflict detection for layouts**, and more reliable **duplicate resolution for profiles**. Security and stability improvements include **fully hiding API tokens after creation**, ensuring **correct project mapping for CodeScan in CI jobs**, and providing **consistent permission set deployments in Commit Label deployments**.

### New Feature

*   **Checkmarx One Integration**

    Users can now integrate Checkmarx One as a Static Code Analysis tool within ARM. This allows security scans to be performed using Checkmarx One alongside other existing tools, providing a scalable and fully managed security solution for cloud-native and DevOps teams.

### Bug Fixes and Improvements

*   **Improved Support for PLATFORMEVENTCHANNELMEMBER in Destructive Commits**

    ARM supports the destructive commit of **PLATFORMEVENTCHANNELMEMBER** metadata, ensuring seamless deletion and replacement of platform events without file diff errors. _Impacted Modules: Destructive changes, VC, Deployments, CI Jobs._&#x20;
*   **Enhanced Merge Conflict Detection for Layouts**

    ARM reliably detects merge conflicts for layout metadata, including files with special characters in their names, ensuring a smoother and more accurate merge process. _Impacted Module: EZ-Merge._&#x20;
*   **Improved Duplicate Resolution for Profiles**

    ARM ensures stable conflict resolution for profiles by preventing errors caused by commented code on a new line. Users can click on files in the resolve duplicate screen without encountering IndexOutOfBounds exceptions. _Impacted Module: EZ-Merge duplicates resolution scenario._&#x20;
*   **Improved Security for API Tokens**

    API tokens are now fully hidden after their initial creation and display, ensuring they are no longer exposed in network requests. This enhances security by preventing unauthorized access through browser developer tools. _Impacted Module: API Token creation._&#x20;
*   **Correct Project Mapping for CodeScan in CI Jobs**

    ARM ensures that CodeScan projects are correctly linked to the scanned Salesforce org in CI jobs. The mapping issue causing a null project name has been resolved, ensuring accurate project creation and association. _Impacted Module: CI Job Build Logs._&#x20;
*   **Improved Commit Label Deployment for Permission Sets**

    ARM ensures consistent and accurate deployment of permission sets during Commit Label deployments. The **Ignore Missing Visibility** setting behaves as expected, and redeployments correctly generate a new deployment package instead of reusing the initial one. _Impacted Module: Commit Label._&#x20;

## nCino + Data Loader Improvements

**Release Date: 9 March 2025**

See the [Release Notes](https://knowledgebase.autorabit.com/overview/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.2-release-notes) for nCino + Data Loader improvements.

***

## ARM Release Notes 25.1.0

**Release Date: 23 February 2025**

The ARM Release 25.1.0 introduces key upgrades, new features, and critical fixes to enhance security, compatibility, and overall performance. This release includes updates to third-party libraries, improved error handling, and several bug fixes to ensure a seamless user experience.

#### Upgrades and Enhancements

* **Third-Party Library Updates:** OpenJDK, Tomcat, Salesforce CLI, Sonar Scanner, and Local DynamoDB have been updated to their latest versions for improved performance, security, and compatibility.
* **Salesforce API Version 63.0 Support:** ARM now fully supports Salesforce API version 63.0, ensuring compatibility with the latest Salesforce features and functionalities.

#### Deprecated Features

* **Picklist to ValueSet Migration:** The Picklist feature in the VC Repo section is now deprecated, as Salesforce has discontinued support for it starting from API version 39.

#### Bug Fixes and Improvements

* **Clearer Error Messages:** Improved UI messages provide more precise and actionable feedback, making troubleshooting easier.
* **Tag Deployment Fix:** Previously, deploying a tag would always result in the same changes, even when those changes were not present in the specified tag or branch. Tags now deploy the correct updates as expected. _Impacted Modules: Custom Deployments._&#x20;
* **Flow Access & LoginFlows Retrieval:** Users can now retrieve and compare Flow Access and LoginFlows seamlessly. Previously, LoginFlows were not visible during change comparisons. _Impacted Modules: EZ-Commit with validate deploy, Merge with validate deploy , Profile duplicates._&#x20;
* **EZ-Merge Report Accuracy:** The EZ-Merge report CSV now includes missing details, such as dates and L1/L2 review statuses, improving tracking and transparency. _Impacted Modules: Weekly Report, EZ-Merge report._&#x20;
* **CI Job Stability:** Resolved issues causing CI job failures and deployment errors for AccelQ tests. Test results now display the correct status and test counts in the Test Summary Report. &#x49;_&#x6D;pacted Modules: AccelQ CI Jobs._
* **Deployment Rules Visibility:** Deployment rules are now consistently displayed in the Deployment Submit popup window across all deployment types. _Impacted Modules: Custom Deployments._
* **Lightning Email Templates Retrieval:** Fixed an issue where Lightning Email Templates were not retrievable across multiple ARM modules, including EZ-Commit, EZ-Merge, Release Label Artifact Preparation, Org-to-Org Deployment, Org Sync, Auto-draft, Commit Template, and Branching Baseline. _Impacted Modules: EZ-Commit._&#x20;
* **Review Artifact Enhancement:** The "Review Artifact" option now correctly displays the package.xml and its corresponding data for commits, deployments, and merges. Additionally, SearchCustomization now functions as expected for both SFDX and non-DX environments, supporting merging, CI jobs, and deployments. _Impacted Modules: EZ-Commit, Merge._&#x20;
* **SFDX Package Naming Support:** Special characters such as @ and . can now be used in SFDX package version names, resolving previous naming limitations. _Impacted Modules: SFDX, Unlocked Packages._&#x20;

#### Upgrades and Enhancements

* **Third-Party Library Updates:** OpenJDK, Tomcat, Salesforce CLI, Sonar Scanner, and Local DynamoDB have been updated to their latest versions for improved performance, security, and compatibility.
* **Linux Upgrade:** The underlying Linux environment has been upgraded, strengthening security and optimizing system performance.

## nCino Improvements

**Release Date 23 February 2025**

See the [Release Notes](https://knowledgebase.autorabit.com/overview/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.0-release-notes) for nCino + Data Loader improvements.&#x20;

***

## ARM Release Notes 24.4.5

**Release Date: 19 January 2025**

With this release, we have implemented the following enhancements and support fixes to improve features and functionality and streamline the user experience.

### Security Improvements <a href="#enhancements" id="enhancements"></a>

**Email and Username Validation**

Registration processes now enforce unique email addresses and usernames, ensuring each email is linked to only one active account. Added email verification confirms ownership, enhancing security and preventing duplication. _Impacted Modules: Admin - User Registration, Subscription Management._

**Enhanced XSS Protection**

Implemented robust measures to prevent XSS risks, including validation of untrusted data, HTML sanitization, and Content Security Policy (CSP). These updates safeguard data and prevent script-based attacks. _Impacted Modules: All Modules._

### Support <a href="#support" id="support"></a>

**Improved Remote Site Settings Updates**

URL updates now run seamlessly in the destination org. A new mechanism ensures tests proceed smoothly, even if individual cases fail. _Impacted Modules: Environment Provisioning._&#x20;

**Consistent Merge Validation**

The merge validation process now handles internal folder references accurately. Files in helper folders are fully validated, ensuring consistent results across merges and deployments. _Impacted Modules: EZ-Merge with validate deployment._&#x20;

**SharingRules Metadata Visibility**

SharingRules metadata is now visible and selectable for deployment and commit operations. Child metadata exclusions were adjusted to ensure proper visibility. _Impacted Modules: All Modules._&#x20;

**Support for GenAiPromptTemplate**

ARM now supports the GenAiPromptTemplate component, ensuring compatibility with Salesforce updates and enhancing functionality. _Impacted Modules: VC, Deployment, CI Jobs._

**Aligned Branching Baseline Behavior**

Branching Baseline now matches EZ-commit behavior for Default manageable state metadata. Excluded Default metadata, such as Account.object-meta.xml, is no longer committed. _Impacted Modules: Branching Baseline._&#x20;

**Faster CI Job Assignment**

Agent assignment during CI jobs has been optimized, and a new feature flag allows streamlined verification using repository and username data, reducing delays. _Impacted Modules: CI Jobs using Version Control._

**Reliable Backup CI Jobs**

Backup CI jobs now handle DX metadata exclusions and dashboard queries correctly, ensuring successful scheduled backups. _Impacted Modules: CI Jobs, Deployments, EZ-Commits._&#x20;

**Merge Validation for Short Metadata Names**

Merge validation now properly handles metadata names shorter than 9 characters. Improved logic ensures accurate validations without failures. _Impacted Modules: EZ-Merge, EZ-Commit with validate deployment._&#x20;

**Commit Label Preservation**

Commit labels are now retained even when associated pre-validation labels are removed, ensuring labels remain accessible and visible. _Impacted Modules: EZ-Commit, Commit Label EZ-Merge, Commit Label Deployment._&#x20;

### Issue Resolution

**Optimized Merge File Processing**

The VALIDATINGSALESFORCEXML performs a single file check during branch-to-branch merges. Merged file data is stored uniquely, improving performance by preventing duplicate validations. _Impacted Modules: EZ-Merge._

***

## ARM Release Notes 24.4.4

**Release Date: 15 December 2024**

With this release, we have implemented the following enhancements and support fixes to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **TAF Sunset Feature Flag**

We introduced a feature flag to support the gradual phase-out of TAF functionality in AutoRABIT. This flag allows controlled activation or deactivation of TAF at the customer account level, enabling a seamless transition without disrupting existing workflows. Automated testing and monitoring have been implemented to ensure functionality operates correctly and customer environments remain stable during the transition. Affected customers will be notified with detailed timelines, guidance, and alternative solutions to support their migration. Impacted Modules: TAF, CI Jobs, Reporting

#### **Protection Against CSV Injection**

We strengthened protection against the potential for a security vulnerability related to CSV injection, where malicious formulas embedded in CSV files could execute commands when opened in spreadsheet applications. User-generated data is now thoroughly sanitized, and special characters are omitted to prevent formula execution. This enhancement ensures that exported CSV files are safe to open, enhancing security against attempted cyberattacks. Impacted Modules: Org Sync History, Users, CI Job History, Reports, CI Job List

#### **Unique Email Enforcement for User Registration**

We eliminated the possibility for users to register using multiple email accounts for the same email ID, preventing potential confusion and security risks. The registration process now includes strict validation checks to ensure each email address is linked to only one active account. Email verification has also been implemented to confirm ownership and prevent unauthorized registrations, improving data privacy and system integrity.

#### **Asynchronous Deployment Processing**

We implemented an update to the deployMetadata SOAP service within the Deployment module, which now enables the process to run asynchronously in the background when initiating a Full Deployment. Previously, the service remained in a "pending" state until the deployment job completed. With this enhancement, the deployment process is more efficient, allowing the service to proceed without blocking user actions while the deployment completes in the background. Impacted Module: Deployments

#### ARM API Integration with Supported SIEM Systems

AutoRABIT introduced a new API endpoint in the audit logs service to provide structured access to CEF audit logs. The API allows querying audit events based on a specified time range and maximum results, returning a detailed JSON response that includes event metadata, such as timestamps, event types, user actions, and outcomes. This enhancement replaces the previous plain-text log format with a structured system with query capabilities, enabling easier integration and analysis of audit data. Impacted Module: API Audit Log Event

#### **Fixed Redirect for Unsupported Types in Org Sync Report**

We corrected an issue in which clicking "Here" in the Org Sync Report failed to redirect to the Unsupported Types Salesforce screen. The href attribute spelling has been corrected, ensuring users are properly redirected to the relevant page for unsupported metadata types. This fix improves navigation and user experience within the Org Sync Report. Impacted Module: Org Sync

### Support <a href="#support" id="support"></a>

#### **Improved Stability for Commit and Merge Operations**

We resolved an issue causing failures in commit and merge operations due to corrupted global workspaces. The global workspace handling mechanism has been enhanced to ensure stability, even when the OPTIMIZED\_WORKSPACE feature flag is disabled. This fix eliminates runtime exceptions during clone operations, improving the reliability of EZ-Commit and EZ-Merge processes. Impacted Modules: EZ-Commit, EZ-Merge, Deployment & CI Jobs, Repo & Branch Registration.&#x20;

**Accurate Reporting for a CodeScan SCA with a Large Number of Violations**

We corrected an error occurring in which a CodeScan code analysis with more than 500 violations displayed incorrect results in the UI and incomplete data in downloaded reports. The fix ensures that all scanned violations are accurately reflected in the UI and included in the downloaded Excel files, providing a complete and reliable report for large code scans. Impacted Modules: CodeScan SCA Execution Reports, CI Jobs, Deployments, Commits, and Merges.&#x20;

#### **Improved Grouping for Salesforce Scanner Violations**

We resolved a mismatch issue between Apex PMD and Salesforce Scanner results. Violations in bundle or static resource subfolders are now correctly grouped under their respective metadata types instead of being displayed as separate components. This fix ensures accurate and consistent results, improving the clarity of scanned violations across all file types, including .JS files. Impacted Modules: SCA Execution for both DX and Non-DX.&#x20;

#### **ToRevision Included in Scheduled CI Jobs**

We fixed an issue in which the ToRevision parameter was missing in scheduled CI jobs. This issue caused jobs to fail by incorrectly using the baseline revision instead of the incremental revision. The fix ensures that ToRevision is consistently included, enabling accurate and reliable execution of CI jobs. Impacted Module: CI Jobs.&#x20;

#### **Accurate Metadata Selection in AutoRABIT Build Deployments**

We resolved an issue in which AutoRABIT Build deployments failed to pick all metadata components when certain components were excluded. The deployment process now ensures that all remaining metadata is correctly included, even after exclusions. This fix addresses issues with missing data-table rows, ensuring complete and accurate metadata deployment. Impacted Module: Deployments.&#x20;

**Accurate Revision Handling in Incremental CI Jobs**

We corrected an issue in which manually triggered incremental CI jobs were skipping the previous revision. The build process now ensures accurate handling of "From" and "To" revisions, preventing gaps in deployed commits. This enhancement guarantees that all relevant changes are included during incremental builds, maintaining consistency and reliability in deployment workflows. Impacted Module: CI Jobs.&#x20;

#### **Improved Handling of Managed Package Components in CI Jobs**

We have resolved an issue causing CI job deployments to fail by including managed package components in destructive changes, despite the "Ignore Installed (Managed) Components" setting being enabled. Logic has been added to exclude installed components from destructive changes in both custom deployments and CI jobs. This enhancement ensures successful deployments without errors related to managed package components. Impacted Modules: CI Jobs, Deployments \[DX, Non-DX, and Org-to-Org Deployments].&#x20;

#### **Resolved Deployment Error for DigitalExperienceBundle**

We corrected an issue during org-to-org deployments in which DigitalExperienceBundle components were not found in the zipped directory, resulting in deployment failure. The logic handling Digital Experience bundles has been corrected to account for scenarios where excluded components exceed 50. This enhancement ensures successful deployments are completed without errors related to missing DigitalExperienceBundle components. Impacted Module: Custom Deployments with Digital Experience bundles.&#x20;

#### **Accurate Package Version Updates in sfdx-project.json**

We resolved an issue where AutoRABIT failed to commit the latest package version to the `sfdx-project.json` file. When a new package version is created, it is now correctly updated and committed in the `sfdx-project.json` file, ensuring consistency between the project configuration and the deployed package versions. Impacted Module: CI Jobs.&#x20;

## ARM Release Notes 24.4.4.1

**Release Date: 22 December 2024**

Patch to fix bugs in the nCino Query Validation module.&#x20;

***

## ARM Release Notes 24.4.3

**Release Date: 24 November 2024**

The following enhancements and support fixes have been implemented with this release to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Special Character Support in Commit Comments**

The EZ-Commit workflow now supports special characters in commit comments, including German characters (ä, ö, ü) and punctuation marks (colon \[:], semicolon \[;], slash \[/]). These characters are correctly displayed in commit messages, and the commit process completes without errors when they are used. Impacted Module: EZ-Commit.

#### **Duplicate Detection for Layout Metadata Subnodes**

The system now supports duplicate detection for all subnodes in Layout metadata, ensuring consistent layout configurations and preventing errors during deployment. Duplicate detection functionality has been extended to include the following subnodes:

* **Header**
* **RelatedLists**
* **Sections**
* **QuickActionList**
* **RelatedContent**
* **EmailDefault**
* **MiniLayout**
* **PlatformActionList**

Users will be prompted with clear, actionable messages when duplicates are detected in any of these subnodes, allowing them to resolve issues efficiently. This enhancement builds on existing duplicate detection for `<layoutItems>`, `<layoutColumns>`, and `<layoutSections>`. Impacted Module: Back End.

### Support <a href="#support" id="support"></a>

#### **Digital Experience Metadata Type Improvements**

#### **Accurate Metadata Selection in Profile Deployment**

When deploying a profile via the CI Job build, only the selected profile is now included in the deployment. The issue in which Digital Experience metadata was incorrectly included has been resolved, ensuring that deployments contain only the metadata explicitly chosen by the user. Impacted Modules: Every module that uses Digital Experience Bundle Metadata type.&#x20;

#### **Delete Support for DigitalExperience Metadata**

Users can now delete DigitalExperience metadata in the EZ-Commit module. Additionally, support for managing DigitalExperience metadata has been extended across all modules. Impacted Modules: EZ-Merge, Custom Deployment, CI Jobs, Prevalidation Deployments, and Release Labels.&#x20;

#### **Subscription Extension via Super Admin**

Super Admin users can now successfully extend subscription counts for active accounts. The issue causing an empty notification pop-up when attempting to increase subscriptions has been resolved. Impacted Module: SuperAdmin - Extend Customer tab. Found in QA.

#### **Vlocity Deployment Visibility in Deployment History**

The Vlocity deployment process has been updated to address issues with visibility and interaction:

1. **Deployment History Display**:
   * Vlocity deployments now appear correctly in the deployment history, ensuring users can track and review their deployments without issues.
2. **UI Interaction Fix**:
   * Resolved the issue where Vlocity components failed to expand when toggled. Users can now expand and view Vlocity components seamlessly in the deployment history UI.

These improvements enhance the usability and reliability of Vlocity deployments in ARM. Impacted Module: Vlocity Deployments.&#x20;

#### **Accurate Notifications for Scheduled Code Coverage Report Changes**

The notification system for scheduled code coverage reports has been improved to accurately reflect changes in settings.

1. **Test-Level Changes**:
   * When the test level is altered for a scheduled code coverage report (e.g., weekly schedule), the notification now correctly indicates the change instead of displaying "no changes detected."
2. **Other Configuration Changes**:
   * Modifications to parameters such as test classes or email lists also trigger accurate and relevant notifications.

This enhancement eliminates misleading messages, ensuring that users receive correct feedback on configuration updates. Impacted Module: Admin-Code coverage report → Reports.&#x20;

#### **Automatic Mapping of JIRA Credentials**

The JIRA credentials mapping process has been improved to eliminate the need for manual workarounds. Credentials using application tokens are now automatically populated in the ALM Mapping section of the profile, without requiring modifications to the default credentials in the ALM Management admin section. This enhancement simplifies the mapping process and ensures seamless integration with JIRA. Impacted Modules: VC Repos, Modularization, EZ-Commit, My Account, SF Org Management.

#### **Improved Handling of Empty Metadata in Release Label Deployment**

The release label deployment process has been enhanced to prevent failures caused by empty metadata. When no deployable changes exist and the package.xml is empty, the system now accurately reflects the absence of metadata in both the UI and back end, ensuring consistency and preventing deployment errors. Impacted Module: Release Labels.&#x20;

#### **Notification Emails for New User Creation**

The issue in which notification emails were not being sent to new users upon creation in ARM has been resolved. New users now receive a notification email in their mailbox immediately after being created by an admin, ensuring consistent communication and a smoother onboarding process.&#x20;

## ARM Release Notes 24.4.2

**Release Date: 10 November 2024**

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Salesforce API Version 62 Support**

ARM now supports Salesforce API Version 62 for all functions, allowing users to utilize the latest metadata types and capabilities introduced by Salesforce. This upgrade includes comprehensive integration across all ARM functions, including the Data Loader, ensuring alignment with Salesforce's Winter '25 release. ARM Admins can set the global API to version 62, ensuring consistent functionality across all features.

### Support <a href="#support" id="support"></a>

#### **Accurate Metadata Count for Repeated Deployments**

ARM now ensures accurate tracking of metadata counts across multiple deployments using previous deployment labels. The request node sent for deployment has been corrected in the front end, ensuring that when performing a follow-up deployment with a prior label, all specified components are included. This enhancement resolves issues in which subsequent deployments using previous labels reflected only a partial count of metadata components, providing a consistent and complete deployment experience across repeated operations.&#x20;

#### **Confirmation for Destructive-Only Deployments**

A new confirmation prompt has been added to notify users when a deployment includes only destructive changes and no constructive changes. This enhancement helps clarify deployment contents, reducing potential confusion for users who may expect other metadata components to be included.&#x20;

#### **Inclusion of Destructive Changes File in Deployment Backups**

The backup.zip file now includes the `destructiveChanges.xml` file, allowing users to access destructive change data for potential rollback scenarios. This enhancement provides a more comprehensive backup package to support safer and more flexible deployment management.&#x20;

#### **Improved Commit Label Search Functionality**

Enhancements have been made to the commit label search feature to address two user concerns:

1. **Accurate Filtering with Special Characters**: The search functionality on the Commit Labels screen now retains all special characters in commit labels, allowing for precise search results even with special characters.
2. **Consistent Label Retrieval Across Screens**: The commit label creation and retrieval processes have been standardized across the EZ-Commit and Commit Labels screens. This ensures accurate search results by aligning label keys, resolving prior issues with locating commit labels by revision.

These improvements enhance usability and consistency within the Version Control module, providing a more reliable experience for commit label management.&#x20;

#### **Corrected Revision Display in EZ-Merge Confirmation**

An update has been made to ensure proper display of revision numbers in EZ-Merge confirmations. Previously, certain revision formats containing the character "e" were misinterpreted as exponential values, causing them to display incorrectly as "Infinity" or scientific notation.

This issue has been resolved by adjusting the response handling, allowing revisions to appear as intended without conversion errors. This enhancement improves the accuracy and reliability of revision details displayed during merges, especially for branches with specific revision formats.&#x20;

#### **Quick Deploy Auto-Population for Deployment Label and Asynchronous ID**

An improvement has been made to the Quick Deploy feature to ensure the Deployment Label Name and Asynchronous ID fields auto-populate after a validated deployment. This update addresses issues in which these fields were previously blank, preventing users from completing Quick Deploy without manually reentering data.

This enhancement improves efficiency and consistency for custom deployments, particularly for users working with single revision DX deployments.&#x20;

#### **Stable Permissions View for Newly Created Teams**

An update has been implemented to ensure stable loading of the Permissions View in the Admin module for newly created teams under Subscription Management. Previously, permissions were not displayed due to an incomplete setup for new users created via the "Create Team" option.

Now, the `releaseNotify` setting for new users defaults to "true," and additional checks have been added to handle null values during data conversion. This enhancement ensures permissions load reliably, enhancing usability for subscription-based team management.&#x20;

#### **Improved CI Job Editing with Null Check for Checkmarx Configuration**

A fix has been implemented to prevent blank pages from displaying when editing CI jobs. Previously, attempting to edit CI jobs with no rules configured for Checkmarx would result in an unresponsive, blank screen.

This enhancement includes a null check, ensuring CI jobs are editable even if no rules are set for Checkmarx configurations. This update improves stability and usability for managing CI jobs in ARM.

#### **Improved Tag-Based Deployment**

An update has been made to ensure successful deployments when using tags in the deployment module. Previously, deployments initiated with tags would sometimes fail with a "No Changes are found in the package" error due to issues with file copying during tag-based deployments.

This enhancement ensures accurate file handling for tag-based deployments, providing stable and reliable performance for both DX and non-DX branches.&#x20;

#### **Accurate Error Messaging for CI Jobs and Deployments**

An update has been implemented to improve the accuracy of error messages displayed in CI job logs and deployments. Previously, CI jobs that encountered baseline revision failures or exceeded file limits displayed misleading error messages. Additionally, deployment failures were showing unrelated errors, such as "Invalid Login," instead of indicating the true cause, such as reaching Salesforce file limits or the need for reauthentication.

This enhancement ensures that CI job and deployment errors reflect the actual underlying issues, providing users with clearer, more actionable information for troubleshooting.&#x20;

#### **Direct Commit Support for Profiles and Permission Sets**

An update has been applied to the direct commit process to ensure that both profiles and permission sets are committed together when selected. Previously, when committing Field-Level Security (FLS) for profiles and permission sets in a single direct commit, only profile FLS was committed, while permission sets were excluded.

This enhancement aligns direct commit functionality with pre-validation commits, allowing selected metadata types—including profiles, permission sets, and custom fields—to be consistently committed as intended. This update improves accuracy and flexibility for version control management within ARM.&#x20;

**Improved Merge Conflict Resolution Status**

An update has been applied to ensure accurate status updates during merge conflict resolution in EZ-Merge. Previously, after resolving a conflict, the status was sometimes incorrectly set to "Commit," even when additional conflicts remained. This led to repeated merge conflict prompts after refreshing the page.

With this fix, the merge status will correctly display as "In Progress" when unresolved conflicts are pending, and actions will show as "Check Details" instead of "Commit." This enhancement ensures clearer guidance during conflict resolution, streamlining the merge process in EZ-Merge for better user experience.&#x20;

#### **Optimized Inline Comment Retrieval in Large File Diffs**

An improvement has been made to reduce "Network Connection Interrupted" errors when expanding large files under the "Files Changed" tab in EZ-Merge. Previously, each line in files exceeding 3,000 lines triggered an individual API call to fetch inline comments, leading to network interruptions and interface freezes, particularly for files with 15,000 lines or more.

With this enhancement, a single API call now retrieves all inline comments at the file level, significantly improving performance and stability when working with large files. This update prevents excessive network calls and enhances usability during merge and commit actions.&#x20;

#### **Accurate Component Inclusion for Reused Commit Labels**

An update has been made to the "Re-use Previously Validated Commit Labels" functionality to ensure that only selected components are included in the commit. Previously, when reusing a validated commit label, additional, unintended changes (such as Profiles and Permission Sets) could appear in the "Files Changed" tab during the approval stage, even if only specific components were selected initially.

This enhancement corrects the commit process so that only the selected components are retained and displayed in the commit, providing more reliable control and accuracy over component selection in EZ-Commit. This improvement applies to both DX and non-DX formats and supports all commit types, including manual selection, auto-draft, commit templates, and package uploads.&#x20;

***

## ARM Release Notes 24.4.1

**Release Date: 27 October 2024**

### Enhancements <a href="#enhancements" id="enhancements"></a>

**Manageable-State Selection for Branching Baseline**\
A new option has been added to select the Salesforce org's manageable state when initiating or re-running a branching baseline. This option is available only when the retrieval type is set to Salesforce, ensuring greater control over the data types included in the process.

1. **Consistent Manageable-State Dropdown Across Modules**\
   The manageable-state dropdown is now consistently available across several modules, streamlining the user experience. It can be found in the following areas:
   * Branching Baseline
   * CI Job (Org to Org deployment)
   * EZ Commit
   * My Account (Save Global Settings for Admins)
   * Static Code Analysis
   * Org Synchronization History
2. **Global Settings Migration for Manageable State**\
   Global settings for manageable state, previously configured in the "My Account → Admin" section, are now automatically retrieved and applied across relevant modules, ensuring consistency across the platform.
3. **Database Support for Manageable State**\
   The database schema has been updated to support the manageable-state dropdown in CI Job, EZ-Commit, and Branching Baseline modules. This ensures that user selections are properly saved and retrieved, maintaining data integrity across sessions.

**Conditional Abort Functionality for Branching Baseline**\
The "Abort" button is now only clickable when the branching baseline process is actively in progress. The abort functionality behaves as follows:

* If the process is in the retrieval stage, clicking "Abort" will stop the operation.
* If the process is in the committing stage, clicking "Abort" will cancel the process.
* If the revision has already been generated or committed, the "Abort" button will be disabled to prevent unnecessary actions.

1. **Enhancement: Updated Actions in Branching Baseline**\
   The actions available for each branching baseline iteration now include "Run," "Abort," and "Delete," providing clear and accessible options based on the process state.
2. **Enhancement: Combined Revision and Info Section in Iterations**\
   The "Revision" and "Info" columns in the branching baseline iterations section have been merged into a single "Revision Info" column. This section is now a clickable hyperlink, allowing users to view detailed information for each specific revision easily.

**Improved Abort Functionality with Interrupt Method (Internal)**\
The abort functionality has been enhanced across the application by implementing the recommended interrupt method, significantly improving reliability and preventing potential thread-related crashes. This update ensures a smoother and more stable abort process.

The enhanced abort functionality has been applied to the following areas:

* Admin
* CI Jobs
* Version Control Release Labels

Thorough internal QA checks have been performed to ensure the stability of this new approach.

**Enable the “Trigger Build On Commit” option when creating a CI Job**\
Users can now enable the “Trigger Build On Commit” option when creating a CI Job, allowing automated builds triggered directly by commits. Upon selecting this option, a webhook setup will become available, ensuring that every new change in the version control system triggers an update to the CI Job. Builds will only initiate for commits made in the feature templates folder.

### Support <a href="#support" id="support"></a>

**Accurate Merge Status Display**

Customers reported receiving expiry email notifications with a misleading status of "MERGED," even though the merge was still pending approval or awaiting changes to be committed. This confusion has been addressed by updating the merge status in the expiry email. Now, the system retrieves the status from the SCM History table, ensuring the actual state of the merge is reflected. Users will no longer see "MERGED" unless the merge has been fully completed, providing clearer communication on the status of their merges.&#x20;

**Profile Comparison Layout and Behavior Fixes**

The following issues in profile comparison have been resolved by adding the "Person Account" column dynamically when person accounts are enabled:

1. **Record Type Column Fix**: The Record Type section in new profile comparisons now displays only two columns, as expected. The third column, "Person Account Default," will only appear in the downloadable report if person accounts are enabled.
2. **Layout Fix**: The layout issue where five columns were displayed instead of six during profile comparisons has been addressed.
3. **Default and Visible Field Fix**: The issue where users could check 'Default' without checking 'Visible' and could not uncheck 'Default' once selected has been fixed.

These changes ensure a more accurate and dynamic display in profile comparisons, improving the overall user experience.&#x20;

**Select All Behavior Correction in Deployment Tab**

A UI bug in the Deployment tab has been fixed where unchecking a metadata member under the "All Metadata" tab did not update the "Select All" option as expected. The condition for deselecting "Select All" has been corrected based on metadata types in the front end, ensuring that when individual metadata members are unchecked, the "Select All" option now responds accurately and reflects the correct selection status. This fix improves the consistency and usability of the deployment process.&#x20;

**Apex Test Class Live Status Fix**

The issue where the Live status for the Apex Test Class was not populating under the SF Org Management section has been resolved. The fix involved changing the response data type from text to JSON, allowing the Live status to be fetched and displayed correctly for Apex Test Classes. This update ensures accurate status reporting for users.&#x20;

**Vlocity Deployment Failure Fix**

A code fix has been implemented to resolve the issue where Vlocity deployments were failing during VC incremental deployments. The failure occurred because the CI job picked a different dependency, specifically the _contentVersion_ dependency, which was not included in the release label deployment. The fix removes non-Vlocity components during CI deployments, ensuring that only relevant dependencies are picked, resulting in consistent and successful Vlocity deployments.&#x20;

**Board Type Selection Fix in Release Label Merge**

An issue where the board type was automatically changing from Vlocity to Salesforce during release label merges has been resolved. The problem occurred because the board type was not being explicitly set to Vlocity during the merge operation, causing Salesforce to be selected by default. This fix ensures that the correct board type, Vlocity, is maintained during the merge process.&#x20;

**Unrelated Changes in EZ-Merges Fix**

A fix has been implemented to address the issue of unrelated changes being pulled into EZ-Merges. To prevent this, the system now cross-checks the remote head revision against the local revision before allocating the workspace, ensuring the workspace is properly synced with the remote repository.

Additionally, loggers have been added to track and identify the root cause should this issue recur in the future. These updates ensure a more reliable and controlled merge process, reducing the chance of unintended changes being included in EZ-Merges.&#x20;

**Manual Deployment Destructive Changes Fix**

An issue was identified during manual deployments using AutoRABIT Build, where clearing all pre-destructive changes did not exclude them as expected. This occurred when deploying via the _Metadata.zip_ option in non-DX custom deployments, where destructive changes were still included despite being deselected.

A code fix has been implemented to ensure that when pre-destructive changes are cleared during deployment, they are properly excluded from the process. This update ensures that all selected components are correctly deployed, without any unwanted destructive changes being included.&#x20;

**Review Artifact Screen Icon Display Fix**

An issue on the Review Artifact screen where icons were not displaying correctly during keyword searches (Ctrl + F) has been resolved. Users previously saw only box icons, leading to confusion about the functions of each icon.

The fix involved correcting the file path for font icons and updating the CSS to ensure proper loading. Icons now display correctly, providing clear visual guidance for each action on the screen. Support Case #123456

**NamedCredential Search and Substitute Fix**

An issue was identified where the "Search and Substitute" feature was not working for the _NamedCredential_ metadata type. The problem occurred because the metadata type was misspelled as "NamedCrendential" in the configuration file.

The root cause has been addressed by correcting the spelling of "NamedCredential" in the JSON file that maintains supported metadata types and their subnodes.&#x20;

**Deactivated User Deletion Error Fix**

An issue where an error pop-up appeared when attempting to delete deactivated users has been resolved. While the user was successfully deleted after a page refresh, the error caused confusion.

The fix involved correctly reading the JWT token during the deletion process, ensuring that inactive users can now be deleted without triggering an error message. This update streamlines the user deletion process and eliminates unnecessary pop-ups.&#x20;

**Validation Job NullPointerException Fix**

An issue causing validation CI jobs to fail with a `java.lang.NullPointerException` has been identified. The problem occurred intermittently when the customer changed the baseline revision, with the workaround only providing temporary relief.

A fix has been implemented to address the root cause of the null pointer error. This ensures that validation jobs now run consistently without failure, eliminating the need for manual interventions or workarounds.&#x20;

**Workspace Error in EZ-Commit Delete Tab Fix**

An issue where users encountered a "Workspace does not exist" error in the Delete tab of EZ-Commit has been resolved. The error occurred because the system did not check whether the workspace was optimized before throwing a custom exception when the workspace was not locked.

A fix has been implemented by adding a condition to ignore optimized workspaces when checking for locks. This ensures that users no longer see the error pop-up when navigating to the Delete tab in EZ-Commit, improving the overall functionality. Support Case #124537Improvements

**Optimized Selective Deployments**\
Selective deployments have been optimized to utilize pre-prepared artifacts, eliminating the need for additional Git operations. This enhancement allows users to perform component selection directly on the pre-prepared artifact, ensuring faster deployment times and reducing the risk of errors associated with manual Git interactions.

**Lazy Loading for EZ Commit Data Tables**\
The EZ Commit process now includes lazy loading for metadata components when using the Auto Draft functionality. Initially, only necessary data is loaded, with additional data fetched as the user scrolls or navigates through the table. This ensures a more efficient and responsive experience.

**Lazy Loading in Package Manifest and Commit Template** \
Lazy loading has also been implemented in the Package Manifest and Commit Template screens and the Selected and Deleted tabs, enhancing performance and responsiveness across these areas.

A visual indicator has been added during the loading process, ensuring users are informed while additional data loads, without any noticeable delays or interruptions to the user experience.

**Third-Party Library Upgrades** \
Third-party libraries have been upgraded to ensure the latest enhancements and fixes from external libraries, improving overall stability across the platform.

By streamlining the selective deployment process, this improvement enhances efficiency and contributes to a more reliable release management workflow.

***

## ARM Release Notes 24.2 <a href="#improved-reporting-features-and-enhancements" id="improved-reporting-features-and-enhancements"></a>

**Release Date: 25 August 2024**

**Improved Reporting Features and Enhancements**

### **New Features**

* The new merge report is now included in the downloaded reports.
* Failure/Auto-reject reasons have been added to the reports for merge, commits, deployment, and CI build jobs, ensuring that if any jobs fail, the reason is included in the reports.

### **Enhancements**

* Extra fields have been correctly added to the current report.
* The name of "Latest Reports" has been changed to "Refresh Reports View."
* Users are now restricted from downloading more than six months of data.
* Post-download, headers, alignment, and naming conventions in Excel have been checked for readability and usability.

1. **Exclude Metadata in the Branching Baseline**\
   Users can now customize their baselines by excluding specific metadata. When selecting the "New Branching Baseline" option, a pop-up appears with available fields. A new "Exclude Metadata" checkbox allows users to choose what metadata to include or exclude from a scrollable or searchable list, with individual checkboxes for each item. Options to "Check All" or "Uncheck All" are available in both sections. Once selections are made, users can click "OK" and then "Run" to execute the process.
2. **Detailed Status Messages for Branching Baseline Process**\
   To improve transparency and usability, the branching baseline process now provides specific status messages for different failure scenarios. If some metadata members fail to commit, the status will display as "Partial Success" or "Failed." Users can download the files of the failed batch metadata XML files for better feasibility and view failure reasons, reducing troubleshooting time and improving overall efficiency.
3. **Updated UI and Pagination**\
   The UI for EZ-commit, deployments, and commit template screens has been updated with pagination for metadata-type tables. Users can now adjust the number of entries displayed per page.

**Pagination Availability:**

* **VC Commit:** Components selection screen.
* **Commit Template:** Components selection screen.
* **Deployments:** Retrieval screen and "Additional Metadata" section.

### Improvements <a href="#improvements" id="improvements"></a>

1. In this release, we revolutionized the system by converting all JSP pages into a RESTful API, enhancing modularity, scalability, and interoperability.
2. SOAP to REST services were upgraded.
3. Third-party libraries were upgraded.

***

## ARM Release Notes 24.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**June 2024**

**Version 24.1 – Enhancements and Improvements**

### Enhancements

1. **Perform Validation Deployment for Multiple Orgs**\
   In this release, we're thrilled to introduce an enhanced **Validate Deployment** feature, responding to a key user request. Users can now choose multiple orgs simultaneously, enabling a forward-looking validation process as they promote from one sandbox to the next and eventually to production. This time-saving enhancement allows users to select up to three organizations from a convenient multi-picklist, and the subsequent summary screen provides a consolidated view of the deployment results for each selected organization. The implementation ensures a seamless experience by allowing users to toggle between different org validations. The introduction of this feature in the EZ-Merge and EZ-Commit options streamlines deployment validations, contributing to a more efficient and informed deployment workflow.\

2. **Incorporated Checkbox to Skip Prevalidation Criteria**\
   In this release, we're excited to introduce the ability for developers to **skip all prevalidation criteria** specifically for **back merges from designated branches**. This enhancement offers a streamlined approach to the back merge process, empowering developers to improve efficiency and simplify code migration upstream. To leverage this feature, developers can configure the branch type in VC Repos → Branch settings, where a new checkbox option allows you to enable skipping prevalidation criteria for a particular branch during back merges. This capability enhances flexibility and productivity, reducing unnecessary steps in the code migration workflow. With the skip option, developers have greater control over the back merge process, ensuring a smoother and more agile development experience.\

3. **Revamped Static Code Analysis View**\
   We’ve revamped our static code analysis UI to enhance the user experience. Now, errors are conveniently displayed under selected files, streamlining issue identification and resolution across various tools.\

4. **Streamlined EZ-Commit Editing**\
   This release significantly enhanced the EZ-Commit workflow to empower developers. The introduction of an integrated **Compare Changes** option in the **Review Artifact** screen allows for seamless viewing, editing, and visualizing of Salesforce metadata changes in a single, user-friendly interface. Developers can now effortlessly navigate and understand their code edits with color-coded differences, eliminating the need to toggle between multiple screens. This streamlined process enhances the user experience and addresses a crucial blocker in the journey towards CI/CD, providing a more efficient and intuitive path for developers.\

5. **Enhanced SCA Label Scheduling**\
   In this release, users can now enjoy enhanced control over SCA label scheduling with the introduction of the ability to edit/update schedules. This feature provides greater flexibility, allowing users to modify scheduled times for SCA labels, contributing to a more seamless and user-friendly experience in managing job schedules.\

6. **New Email Templates Implementation**\
   In this release, a significant enhancement has been made by implementing new email templates that align with current visualization standards. This update reflects our commitment to maintaining high standards in user interface design and enhancing overall user engagement.

### Improvements

This update improves the tool's efficiency and responsiveness and leverages new technologies, collectively resulting in a smoother, faster user experience.

1. In this release, we revolutionized the system by converting all JSP pages into a RESTful API, enhancing modularity, scalability, and interoperability.
2. SF CLI Version upgrade to 2.41.8
3. SOAP to REST services upgrade: Upgrading from SOAP to REST services improves performance by reducing overhead with lightweight JSON payloads and enhances security through stateless communication and simplified implementation of HTTPS.
4. By merging SalesforceDxHub into SalesforceOrg, it effectively reduces redundancy in data storage. Users can now register once from SalesforceOrg, with the added capability to specify a registered org as a Dev hub. When a production org is registered as a Dev hub, it appears on both screens, streamlining data management and enhancing user workflow. This release optimizes data storage, improves user experience, and simplifies registration processes, ultimately enhancing overall system efficiency.
5. Upgrade of third-party libraries
6. Salesforce integration credentials (Client ID & Secret) are now encrypted for improved security. Existing tokens are also migrated to the new format. This enhances protection against unauthorized access.
7. Log-leveling: Dynamically modify log levels for specific logger categories to enhance monitoring and troubleshooting.

### Changelogs

The following weekly fixes were implemented.

#### 31 July 2024

ARM 24.1.7

1. A code fix was applied to the CI Jobs module of version 24.1 related to a data error that caused a CI Job to be unable to be built manually. Support ticket #117587&#x20;
2. A code fix was applied to the Admin module of version 24.1 due to a data error that caused Salesforce orgs to not be displayed as mapped to the repository even after enabling them under the profile. Support ticket #117542&#x20;
3. A code fix was applied to the nCino module of version 24.1 due to a use-case error identified internally in which rollback failed for inserted records.
4. A code fix was applied to the nCino module of version 24.1 due to a use-case error in which Data Loader jobs were automatically being deleted. Support ticket #117577&#x20;
5. A code fix was applied to the CI Jobs module of versions 23.1 and 24.1 due to a use-case error causing the CI Job History report to not generate. #116943

#### 24 July 2024

**ARM 24.1.6**

1. A code fix was applied to the CI Jobs module of version 24.1 due to a typo in the ARM CI Jobs creation screen. Support ticket #116616
2. A code fix was applied to the Deployments module of version 24.1 due to a use-case error in which the 'add member' option was not working. Support tickets #116545, #117480
3. A code fix was applied to the Admin module of version 24.1 to correct a use-case error in which test class mappings were missing. Support tickets #116984, #117737&#x20;
4. A code fix was applied to the Admin module of version 24.1 to correct a use-case issue with log visibility in the branching baseline for admin users. Support ticket #117485&#x20;
5. A code fix was applied to the Admin module of version 24.1 from an internal ticket identifying a use case in which the user was getting an 'unauthorized 401' error during a new account signup registration.&#x20;
6. A code fix was applied to the Admin module of version 24.1 identified by internal ticket a use case in which the user was unable to log in via the default SSO login page; also, the build version and revsion information were not displaying.
7. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which an issue was occurring with the system administrator lite. Support ticket #117297
8. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which the user was not able to see the metadata through the single revision deployment. Support ticket #116919
9. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which the user was not able to deploy the Einstein Prediction builder. Support ticket #116909
10. A code fix was applied to the Admin module of versions 23.1 and 24.1 due to a use-case error with users losing access. Support ticket #111830
11. A code fix was applied to the Version Control module of versions 23.1 and 24.1 due to a use-case error requiring multiple revisions on an ALM work item. Support ticket #117810
12. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error with the new profile compare feature. Support ticket #117309&#x20;
13. A code fix was applied to the nCino module of version 24.1 due to a use-case error in which Data Loader jobs were being automatically deleted. Support ticket #117577&#x20;
14. A code fix was applied to the CI Jobs and Deployment modules of version 24.1 due to a use-case error causing the rollback functionality to not work properly. Support tickets #117512, #118316&#x20;
15. A code fix was applied to the CI Jobs module of version 24.1 due to a use-case error in which CI Jobs were experiencing a build issue, which is awaiting QA verification from the customer. Support ticket #118301&#x20;
16. A code fix was applied to the CI Jobs module of version 24.1 due to a use-case error identified by internal ticket in which a CI Unlocked package installed CI build failing with Hub connection failure, even though Hub connection was successful. &#x20;
17. An internal ticket identified an EBR change request required to the EBR module of version 24.1 to correct EBR plugins.

#### 17 July 2024

**ARM 24.1.5**

1. A code fix was applied to version 24.1 as a result of a data error encountered in the CI Jobs module related to CI Jobs not triggering. Support ticket #116677
2. A code fix was applied to the Version Control module in version 24.1 related to a data error causing the WebLink deletion feature to not work. Support ticket #115994
3. A code fix was applied to the CI Jobs module in version 24.1 due to a data error identified internally with the CI Edit edit mode where the "Do you want us to update the test classes" feature is not saving.
4. A code fix was applied to the nCino module in version 24.1 related to a use-case error in which Data Loader Pro was not fetching the child object. Support ticket #116928

#### 10 July 2024

**ARM 24.1.4**

1. A use-case error identified in version 23.1 required a code fix applied in versions 23.1 and 24.1 to the Deployment and Version Control modules, to correct a scenario in an org-to-org full-profile deployment in which package visibility and permissions were not captured. Support ticket #110760
2. A code fix was applied to versions 23.1 and 24.1 due to a use-case error identified in version 23.1 in which commits were failing with a 'no credentials mapped' error in the Version Control module. Support ticket #116704&#x20;
3. A code fix identified in version 24.1 was applied to the Admin module in version 24.1 due to a use-case error identified by internal ticket in which the on-premises server was not starting up after migrating from 23.1 to 24.1 build.&#x20;
4. A use-case error in the Version Control module identified in version 24.1 by internal ticket required a code fix to version 24.1 to correct an instance in which the user was unable to create a release label.

#### 3 & 7 July 2024

**ARM 24.1.3**

1. A use-case error identified in version 24.1 required a code fix to the CI Jobs module, applied in versions 23.1 and 24.1, to correct instances where configuration changes were not being saved to the CI job. Support ticket #116047&#x20;
2. A code fix identified in version 24.1 by an internal ticket was implemented in version 24.1 to correct a use-case error in which the Version Control module’s Validate and Merge button was not being reflected immediately after changing the EZ-Merge validation criteria in MyAccounts.
3. A code fix identified in version 24.1 by an internal ticket was applied to version 24.1 due to the minimization feature not working in the Version Control module.
4. A code fix identified by an internal ticket in version 24.1 was applied to the Version Control module in version 24.1 due a use-case error where ‘Path View’ section highlighting is occurring when toggling from the ‘File Changes’ screen to the ‘Path’ view, then back to the ‘File Changes Path’ view.
5. A code fix identified in version 24.1 by an internal ticket was initiated to the EBR Change module in version 24.1, prompted by a change to the EBR plugin info.
6. A use-case error identified in version 24.1 by an internal ticket required a code fix to the Version Control module in version 24.1 due to the commit history screen getting stuck loading when the repo name has a special character in it (e.g., plus sign \[+]).
7. A use-case scenario identified in version 24.1 by an internal ticket required a code fix to the CI Jobs module in version 24.1 for the time-frame window to be added for the ARM admin API to fetch data.
8. A use-case error identified in version 24.1 by an internal ticket required a code fix applied to the nCino module in version 24.1 to correct where the option "automap user/owner data" is disabled by default for CI jobs created in 23.1.x versions.
9. A use-case scenario identified in version 24.1 required a code fix to the Version Control module in version 24.1 due to release labels not showing. Support ticket #116413
10. A use-case error identified in version 24.1 required a code fix to the Version Control module in version 24.1 due to an issue with choosing the Level 1 approver when performing a merge. Support ticket #116417, #116692
11. A use-case error was identified in version 24.1 that required a code fix to the nCino module due to the RBC filters not working on commits. Support ticket #116291
12. A use-case scenario identified in version 24.1 via an internal ticket required a code fix to the nCino module to correct an error in which the Data Loader clone process is not identifying the new CSV file.&#x20;
13. A use-case error identified in version 24.1 required a code fix to the Version Control module to correct an error in which user is unable to create an EZ-Merge. Support ticket #116700
14. A code fix was applied to the Deployment and Version Control modules to correct a use-case error identified in version 24.1 in which the org comparison is not showing diff results. Support ticket #116039
15. A use-case scenario required a code fix to the version 24.1 Admin module to correct an error that caused the branching baseline to keep running for 24 hours. Support ticket #114734&#x20;
16. A code fix was applied to the Version Control module to correct a use-case error identified in version 24.1 that caused commits to be failing with an 'no credentials mapped' error. Support ticket #116704
17. A use-case error identified in version 23.1 required a code fix to the Deployment module, applied in versions 23.1 and 24.1, to correct the metadata retrieval in the repository from failing. Support ticket #115818&#x20;
18. A code fix identified in version 23.1 by an internal request ticket was applied to the Admin and CI jobs modules in versions 23.1 and 24.1 to upgrade v61 (Beta) to v61.

#### 26 June 2024

**ARM 24.1.2**

1. A data error reported in version 23.1 with the Version Control module that resulted in version control being deleted was resolved in both 23.1 and 24.1 through adding loggers. Support ticket #114503
2. A use-case error reported in version 23.1 with the Version Control module in which the user was unable to use an existing conflicted file, which resulted in reraising merge requests, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115084
3. &#x20;A use-case error reported in version 23.1, which resulted in an issue with the Data Loader module in which the software was not inserting the correct record type, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #114076
4. A use-case error reported in version 23.1 with the nCino module in which rollbacks were only partially being completed was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115204
5. A use-case error in version 24.1 with the Version Control module in which commits were remaining in progress was resolved through a code fix. Support ticket #115691
6. A use-case error in version 24.1 with the Version Control module with commit CI Job deployment errors was resolved in 24.1 through a code fix. Support ticket #115817
7. A use-case error reported in version 24.1 required an update to the Admin module to properly reflect X rather than Twitter along with revised copyright information, which was resolved through a code fix. Support ticket #115756

#### 23 June 2024

ARM 24.1.1

1. A code fix was applied to the Version Control module for a use-case error related to an EZ-Commit re-login issue identified. Support ticket #115664
2. A code fix was applied to the Version Control and Admin modules for a use-case error related to an issue in which Azure ADO connection and password were returning errors. Support tickets #115489, 115558
3. A code fix was applied to the Version Control module for a use-case error related to a validation org being requested when attempting to merge changes. Support ticket #115787
4. A code fix was applied to the Version Control module for a use-case error related to the create artifact button not being visible when attempting to create a release label.
5. A code fix was applied to the Reports module for a use-case error related to an alignment issue in the weekly reports filter for no deployments.&#x20;
6. A code fix was applied to the Admin module for a use-case error in which the user is unable to create a search and substitute rule.&#x20;
7. A code fix was applied to the Admin module for a use-case error related to being unable to register a branch.&#x20;

### nCino Improvements

See the recent updates to [nCino release 24.1](../ncino-release-notes/release-notes-24.1.md) notes as well.&#x20;

***

## ARM Release Notes 23.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**September 2023**

**Version 23.1 – New Features, Enhancements, and Improvements**

**Supports Provar** Current Version: 2.10.1&#x20;

**Supports Apex PMD** Current Version: 7.0.0

### New Features

**1. Automatic Merge after Successful CI Build**\
We know that understanding and managing version control can sometimes be a challenge. ARM offers the flexibility to cherry-pick branch revisions for merge or deployment. Now you can automate this process of cherry-picking the revisions in CI Jobs as a post-deployment step.

The '**Run Merge process on successful deployment**' feature keeps track of builds in source branches and merges them into a designated destination branch if they meet the configured criteria (for example, if the build is successful). Rather than requiring manual effort, upstream merges may now be automated by the **Salesforce Release Manager** using revision numbers that were determined as part of a build cycle in CI jobs.

Users will be notified via email of the success or failure of the automated merge process.

**2. Create and Install an Unlocked Package Version from a Version Control Branch**\
Use ARM CI intelligence to create a package version, build using the SFDX project structure in a Version Control branch, and install the same in the destination org of your choice—all from the same page.

You can now generate an unlocked package version automatically through the CI job, and as part of the deployment, it is deployed in the same build cycle. Until the 22.2 version, it picked the latest package version that was already successfully created in ARM.

When users create a CI job using this option, ARM checks the Version Control. If there is a change, it builds a new version on top of the packages. Once the package is created, then the deployment is triggered automatically.

**3. Create Connected Apps**\
ARM now gives access to users to create and maintain their OAuth credentials. Users can set up the **Connected Apps** for Jira OAuth and register the credentials with ARM.

You can add, edit, and delete your Jira login credentials instead of contacting AutoRABIT to manage the connected apps. Once created, simply provide us with the connected app details like **Client ID** and **Secret Keys**.

We use these details to connect as an ALM and test the connection.

**4. RESTricted Emails**\
The new **RESTricted Emails** section on the **Notifications** page of the Admin module helps ensure that ARM-related emails are not sent to deactivated users.

Admins can either add users to this list manually or deactivate the respective users from the **Users** page of the Admin module, and they will be automatically added to this list. These users will not receive ANY emails including deactivation, forgotten password, reset password, jobs executed in the application, etc. Admins can also use the same two methods to reactivate a user and remove them from this list.

There is also a provision for an Admin to remove all users from the **RESTricted Emails** list at once.

**5. Dependency Analyzer**\
Dependency Analyzer helps you understand the dependencies among various components in your Salesforce org. It allows you to analyze the relationships among objects, fields, classes, triggers, and other metadata components.

With Quality Gates, ARM helps Salesforce developers run multiple checks to understand if and how their commits can break a Salesforce org. Currently, we enforce the following gates:

* SAST, SSPM, and AST (Static Code Analysis, Salesforce Security Posture Management, and Application Security Testing)
* Deployment Validation
* File Change Footprint
* Peer-to-Peer Code Review

With the introduction of the Dependency Analyzer, we can offer a fourth gate, Dependency Check, which will allow users to see what they are missing due to Salesforce specificity.

We have introduced the Dependency Analyzer in CI Jobs for now, and this is just a start at bringing this functionality to the remaining modules soon.

Users now have the option to ‘**Run Metadata Dependency on Failed Deployments**’ to view the results of failed metadata components with their dependencies and download them in Manifest and XML formats.

**6. ServiceNow – ALM Management**\
The ARM–ServiceNow integration automatically posts updates to ServiceNow tickets. It makes tracking the status of your user stories and support tickets faster and easier. Tasks can be organized by project, allowing an organization to track issues within projects transparently.

ServiceNow will make information more easily accessible and workflows more streamlined, reducing the time and effort required to manage and resolve service requests. Additionally, the integration will allow teams to work more effectively, improving collaboration and communication.

### Enhancements

1. **Salesforce Spring (API 57.0) & Summer (API 58.0) Support**\
   AutoRABIT supports the most recent API 57.0 & API 58.0 versions in this release to keep our product updated with Salesforce updates. The most recent API version is intended for customizing and developing tools to manage the metadata model.
2. **Exporting Selected User Details**\
   Users with Admin access can now choose the fields they want to include while exporting users' details to a CSV file. While selecting the Export option, the list of available fields is displayed. Admins can select and deselect the required fields by clicking the corresponding checkbox. Some of the fields are selected by default for ease of use. Admins can always deselect these fields if they are not required. Thus, based on the teams with whom they will be shared, Admins can customize the fields in the list.
3. **More Info on CI Jobs and Info**\
   Users are now able to view the CI Jobs they created in the CI Job List screen to date inside ARM. The list is displayed in chronological order with the most recent jobs listed at the top.
4. **'Created and Requested by' in Deployment UI**\
   Users are now able to view the ‘Created by’ and ‘Triggered by’ fields in the Deployment home screen without scrolling through multiple screens for this info, enabling monitoring of the deployment’s real-time progress. [Read more](../../../product-guides/arm/arm-features/deployment/)
5. **Self-Service Connected App Setup for Jira OAuth in ARM**\
   We've introduced a self-service feature allowing users to set up Jira OAuth-connected apps in ARM autonomously. With guidance from our user manual's Connected App guide, users can effortlessly create and register their app credentials, eliminating the need for support team assistance. Users can quickly establish a robust connection by inputting the generated Client ID and Server Key into ARM's settings.
6. **Unified Admin Roles**\
   We’re excited to introduce a streamlined and more efficient Admin experience. We’ve consolidated the roles of Super Admin and Registered Admin into a single empowered Admin role. This change means Admins now have a unified set of tools and permissions, streamlining tasks and creating a more user-friendly Admin experience.
7. **CI Jobs List and Results: Filter and Export Option**\
   We've enhanced the platform with a user-friendly quick filter and export feature in response to user feedback. This functionality empowers administrators, release managers, and users to efficiently organize and analyze data by alphabet or date, facilitating faster insights and informed decision-making.
8. **Create Artifact: Release label more than 180 days**\
   In the Create Artifact section, users can now generate a Release Label and have the flexibility to choose an extended timeframe of over 180 days for retrieving comprehensive commit history data. This enhancement offers users a broader historical perspective, facilitating more in-depth analysis and tracking of commits for their projects.
9. <mark style="color:blue;">**Enhanced security and user experience. (NEW)**</mark>\
   The new features focus on enhancing security and user experience. They include a single-user session control to prevent multiple active sessions under the same username, automatic logout for inactivity to bolster security, and support for multiple tabs or pages in the same browser, improving user productivity and maintaining the environment's integrity.

### Improvements

This update has implemented significant performance upgrades to enhance the tool's efficiency and responsiveness. These enhancements encompass optimized queries and leverage new technologies, collectively resulting in a smoother, faster user experience.

#### 31 July 2024

**ARM 23.1.40**

1. A code fix was applied to the CI Jobs module of versions 23.1 and 24.1 related to a use-case error causing the CI Jobs History report to not generate. Support ticket #116943&#x20;

#### 24 July 2024

**ARM 23.1.39**

1. A code fix was applied to the Version Control module in version 23.1 related to a use-case error in which the merge completion was taking too long. Support ticket #113102
2. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which an issue was occurring with the system administrator lite. Support ticket #117297
3. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which the user was not able to see the metadata through the single revision deployment. Support ticket #116919
4. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error in which the user was not able to deploy the Einstein Prediction builder. Support ticket #116909
5. A code fix was applied to the Admin module of versions 23.1 and 24.1 due to a use-case error with users losing access. Support ticket #111830
6. A code fix was applied to the Version Control module of versions 23.1 and 24.1 due to a use-case error requiring multiple revisions on an ALM work item. Support ticket #117810
7. A code fix was applied to the Deployments module of versions 23.1 and 24.1 due to a use-case error with the new profile compare feature. Support ticket #117309
8. A code fix was applied to the Deployments module of version 23.1 due to a use-case error with 'add additional member' showing duplicates when expanding the toggle. Internal request.
9. A code fix was applied to the Version Control module of version 23.1 due to a use-case error with users getting an error for a commits tab external pull request using Bit bucket repo. Internal request.&#x20;

#### 17 July 2024

**ARM 23.1.38**

1. A code fix was applied to the nCino module in version 23.1 related to a use-case error in which Data Loader Pro was not fetching the child object. Support ticket #115313

#### 10 July 2024

**ARM 23.1.37**

1. A use-case error identified in version 23.1 required a code fix, which was applied in versions 23.1 and 24.1 to the Deployment and Version Control modules, to correct a scenario in an org-to-org full-profile deployment where it was not capturing package visibility and permissions. Support ticket #110760
2. A use-case error identified a code fix needed to the Reports module of version 23.1 to fix a product test class in which the weekly scheduled job failed. Support ticket #115654&#x20;
3. A code fix was applied to versions 23.1 and 24.1 due to a use-case error identified in version 23.1 where commits were failing with a 'no credentials mapped' error in the Version Control module. Support ticket #116704
4. A code fix was applied to the Admin module in version 23.1 related to a use-case scenario that required additional support to create the ARM instance from scratch. Support ticket #117015
5. A code fix was applied to the Deployment module in version 23.1 due to a use-case error in which the user was unable to get the popup while deploying using package.xml as the source. Support ticket #116967

#### **3 & 7 July 2024**

**ARM 23.1.36**

1. A use-case scenario identified an error in version 23.1 with metadata retrieval from the repository failing in the Deployment module, which was resolved in versions 23.1 and 24.1. Support ticket #115818
2. A code fix identified in version 23.1 was applied to correct a use-case error in the Version Control module of version 23.1 related to commit templates. Support tickets #116124, #116138
3. A code fix identified in version 23.1 by internal request ticket was applied to the Admin and CI jobs modules in versions 23.1 and 24.1 to upgrade v61 (Beta) to v61.
4. A use-case error in version 23.1 required a code fix to version 23.1 Deployment and Version Control modules due to an org comparison not showing diff results. Support tickets #112752, #116025&#x20;

#### 26 June 2024

**ARM 23.1.35**

1. A data error reported in version 23.1 with the Version Control module that resulted in version control being deleted was resolved in both 23.1 and 24.1 through adding loggers. Support ticket #114503
2. A use-case error reported in version 23.1 with the Version Control module in which the user was unable to use an existing conflicted file, which resulted in reraising merge requests, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115084
3. &#x20;A use-case error reported in version 23.1, which resulted in an issue with the Data Loader module in which the software was not inserting the correct record type, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #114076
4. A use-case error reported in version 23.1 with the nCino module in which rollbacks were only partially being completed was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115204

#### 12 June 2024

**ARM 23.1.34**

1. A code fix was performed due to a use-case error related to the CI Jobs module in which nCino CI Jobs were not triggered by metadata CI Jobs on success. Support ticket #113887
2. A code fix was performed due to a use-case error related to the Version Control module in which the API response from CodeScan returned a page not found (404) error in ARM. Support tickets #108895,  #115120, #114434
3. A code fix was performed due to a use-case error related to the Deployment module in which the Deployment button was not enabled in AutoRABIT after validation. Support ticket #107108
4. A code fix was performed due to a use-case error related to the Deployment module in which the user was unable to deploy a Bot from a Branch to a sandbox. Support ticket #11497&#x20;
5. A code fix was performed due to a use-case error related to the Version Control module in which an ALM work item was not displaying in the merge. Support ticket #113626
6. A code fix was performed due to a use-case error related to the Admin module in which a user was unable to implement ARM and Zoho desk integration with JWT.
7. A code fix was performed due to a use-case error related to the Version Control module in which a user was unable to perform EZ-Commits. Support ticket #114441
8. A code fix was performed due to a use-case error related to the Version Control module in which the previously validated commit label showed to add a date instead of the label dropdown. Support ticket #115249
9. A code fix was performed due to a use-case error related to the Reports module that required us to fix recursive errors.
10. A code fix was performed due to a use-case error related to the Data Loader module in which the master-child relationships were not being applied when loaded through Data Loader Pro. Support ticket #111780
11. A code fix was performed due to a use-case error related to the nCino module in which the CI job was not updating templated objects and object record count when the checkout was not taken from version control. Support ticket #112704
12. A code fix was performed due to a use-case error related to the nCino module wherein CI Jobs for nCino RBC feature migrations were failing. Support ticket #114991
13. A code fix was performed to the Admin module as a result of a change request related to users being unable to log in to AutoRABIT. Support tickets #115392, #113300

#### 5 June 2024

**ARM 23.1.33**

1. A code fix was applied to all modules prompted by an internal change request in preparation for support of the Salesforce Summer '24 release. This will require updates to internal documentation.
2. A code fix was applied to the Deployments module resulting from an internal request to correct a use-case error in which a deployment failure and document discrepancy were encountered, with subsequent deployment attempts unsuccessful.
3. &#x20;A code fix was applied to the Version Control module initiated by a use-case error in which the team encountered an ALM commit issue related to the label name when testing a user story. Support ticket #113308
4. A code fix was applied to the Version Control module related to a use-case error occurring when processing merge conflicts. Support ticket #113606
5. A code fix was applied to the Admin module related to a data error in which the branching baseline was not updating the LWCs in the branch. Support ticket #113174
6. A code fix was applied to the Data Loader module related to a configuration error causing Data Loader to not work as expected. Support ticket #113575&#x20;
7. A code fix was applied to the ARM module related to a use-case audit logging API error with start time and end time issues occurring when fetching logs. #113739



#### 29 May 2024

**ARM 23.1.32**

1. A code fix was applied to the Version Control module to resolve a use-case error in which the user cannot approve or reject a Merge Request when the label name contains a "+" symbol. When the merge label contains unsupported characters, the merge label is not submitted as expected and the validation message displays the supported characters. Support ticket #112715
2. A code fix was applied to the Admin module related to a use-case error occurring when modifying the Team Administrator, it created duplicate Teams, consuming existing licenses. Support ticket  #109457
3. A code fix was applied to the CI Jobs module due to a use-case error in which a Checkmarx scan was not matching up and breaking the build. Support ticket #105217
4. A code fix was applied to the CI Jobs module due to a use-case error occurring when multiple CI jobs run on GitHub PRs, AutoRABIT reports incorrectly that the jobs were successful. \* Issue requires updated documentation. Support ticket #111955
5. A code fix was applied to the Version Control module related to a use-case error in which Mock Deployment criteria check lines were not logged in the UI during the Prevalidation Deployment refresh, but they do appear after auto-rejection and subsequent refresh.&#x20;
6. A code fix was applied to the Deployment module to correct a use-case error occurring when selecting and deselecting ApexClass and CustomField metadata types, the Deploy pop-up incorrectly displayed "All components are selected" for ApexClass instead of the list of selected components.&#x20;
7. A code fix was applied to the Version Control module to correct a use-case error displaying unwanted characters, such as different language letters, like “â€” in the message: "Please waitâ€ when a compare and commit is in progress."
8. A code fix was applied to the Version Control module due to a use-case PrevalidationMerge error occurring when the user was trying to approve a Merge Label through an API with an auto-rejected label, the status changed from "Auto-reject" to "Commit."&#x20;
9. A code fix was applied to the Version Control module after a user observed three gaps/issues in Commit Templates: 1) Data Table Change in the Commit Template under the 'All Metadata' tab should also sync across all three places, like Deployments, VC Commit, and Commit Template under the 'All Metadata' tab for data table changes. 2) Folder-Related Members Visibility: Folder-related all members are not visible when selecting the folder. This does not sync with EZ Commit All Metadata, from new commit all members. When selecting the folder, all respective folder-related members are visible but not included in the Commit Template when selecting the same Salesforce org. 3) Input Search Dropdown Missing for selecting Folders.
10. A code fix was applied to the Data Loader module concerning a use-case error in which the user was unable to create a project journey with a BIC\_\_c field using "LookUp via" feature. Support ticket #110111

#### 22 May 2024

**(ARM 23.1.31)**

1. A code fix was applied to the Version Control module due to a use-case error related to EZ-Commits and EZ-Merges not taking the master branch, even when Baseline Branch "master" is selected. #107151
2. A code fix was applied to the Version Control module due to a use-case error in which reverting a commit failed. #112094
3. A code fix was applied to the Version Control module due to a use-case error related to the system failing to select multiple reports. #112381, #112812
4. A code fix was applied to the Deployment module due to a data error in which the org sync was not completing. #111545
5. A code fix was applied to the Deployment module due to a data error in which there was a problem in component selection during deployment. #111892&#x20;
6. A code fix was applied to the Deployment module due to a data error in which the selected items tab was now showing the selected components, as well as the search filter not always being visible. #112095

#### 15 May 2024

**(ARM 23.1.30)**

1. Code fix applied to Deployments module due to user receiving error message: INVALID\_LOGIN: Invalid username or password or security token or API version or user locked out. #111008
2. Code fix applied to Version Control module due to user not being able to see the merge request label name in BitBucket after merging. This required a feature flag, MERGE\_STRATEGY\_ENABLE\_NON\_FF, which is not enabled by default and must be enabled. #110541
3. Code fix applied to the Deployments module related to user experiencing Redeploy/Promote hanging if previous deployment used specified tests. This requires a feature flag, AR\_33697\_ENABLE\_APEX\_TEST\_GET\_CALL, which is not enabled by default and must be enabled. #110764
4. Code fix applied to Deployments module related to email templates of type Visualforce not being added to the package.xml when deploying. #110762
5. Internal - Code fix applied to Version Control module due to DX Package Directory Selection lists not being visible when configuration changes from Vlocity SF org and Vlocity repo to DX Repo.
6. Code fix applied to Version Control module related to an auto-rejected merge label being pushed to a remote repository. #112244

#### 7 May 2024

**(ARM 23.1.29)**

<table data-full-width="true"><thead><tr><th width="132">Module</th><th width="248">Summary</th><th width="137">Status</th><th width="89">Fix Version</th><th width="108">Resolution</th><th width="138">Cause</th></tr></thead><tbody><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Commits for Fields on Objects are Removing Lines from related Object XML</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Configuration</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Implemented an option to add Reviewers when Creating an External Pull Request</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Commit Issue with Custom Page Web Links Deletions</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Configure Gated Check-Ins Report for Deployment Validation</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Improve Performance of All Metadata Components Screen</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Administration</p><p> </p></td><td>EBR User Metrics </td><td><p> </p><p>Done</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td>EBR Change Request</td></tr><tr><td><p> </p><p>Data Loader</p><p> </p></td><td>Data Loader Pro jobs not picking up Records</td><td><p> </p><p>Customer Coordination</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Added Loggers</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr></tbody></table>

#### 29 April 2024

**(ARM 23.1.28)**

<table data-full-width="true"><thead><tr><th width="146">Module</th><th width="215">Summary</th><th width="173.3333740234375">Status</th><th width="85">Fix Version</th><th width="130">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployments</p><p> </p></td><td><p> </p><p>Getting error on deployments</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td><p> </p><p>Skip member is not working</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>EZ-Commits failing</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Static resources not identified by ARM SCA </p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Merge showing as no modifications</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Error occurred when the user attempted to upload the conflicted zip file from the local system after manual modifications</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Inquiries regarding report module</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Deployment from Dev Sandbox to B2C2 QA Org by using feature - New Deployment</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td><p> </p><p>Build did not include second revision</p><p> </p></td><td><p> </p><p>Requires Customer Coordination</p><p> </p></td><td> </td><td>Loggers added</td><td>Loggers added</td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td><p> </p><p>Run test based on changes, noticed issues</p><p> </p></td><td><p> </p><p>Requires Customer Coordination</p><p> </p></td><td></td><td>Loggers added</td><td>Loggers added</td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>IDs of parents/children and records not resolving</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr></tbody></table>

#### 24 April 2024

**(ARM 23.1.27)**

<table><thead><tr><th width="169">Module</th><th width="273">Summary</th><th width="122">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td><p> </p><p>Version Control</p><p> </p></td><td>EZ-merges: Successful validations were auto-rejected on 'validate deploy' step</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Release Label: Package is not preparing</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td><p> </p><p>Weekly Reports tab error</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Backups not being created for user</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Code Scan Analysis not showing in AR ARM tool - UI</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>setting default repository</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>ExternalCredentialPrincipalAccess (permissionSet) is ignored on a git revision deployment</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unknow error while merging site components</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>CI Job does not deploy all components</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>SSH connectivity issue</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>request_closure_duration_mins mismatch for the merges</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>B2C Prod Code Scan report</td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td><p> </p><p>AR issues</p><p> </p></td><td><p> </p><p>Added Loggers</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr><tr><td><p> </p><p>Dataloader</p><p> </p></td><td><p> </p><p>User Object Requiring ALL Fields for Uploads </p><p> </p></td><td><p> </p><p>Added Loggers</p><p> </p></td><td><p> </p><p>Use case</p><p> </p></td></tr></tbody></table>

#### 14 April 2024

**(ARM 23.1.26)**

<table data-full-width="true"><thead><tr><th width="152">Module</th><th width="188">Summary</th><th width="120">Status</th><th width="92">Version</th><th width="124">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Org Sync issue with case components</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Deployments</td><td>B2C Org sync diff mail notification issue</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>CI Jobs, Deployments</td><td>Einstein Chatbot Deployments Failing</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Admin</td><td>log files are not present</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Deployments</td><td>Deployments are not working</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>CI Jobs, Deployments</td><td>Failed to initiate the deployment</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Version control</td><td>Profile commit progress delay</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Admin</td><td>Team Administrator modifications creating duplicate Teams and consuming existing licenses</td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Version control</td><td>Issue Retrieving Components </td><td>QA Passed</td><td>23.1</td><td>Code fix</td><td>Use case</td></tr><tr><td>Version control</td><td>Release Label Stuck while building Artifact</td><td>Requires Customer Coordination</td><td></td><td>Loggers added</td><td></td></tr><tr><td>Deployments</td><td>utils.js was not deployed as part of package</td><td>Requires Customer Coordination</td><td></td><td>Loggers added</td><td></td></tr><tr><td>nCino</td><td>Version control record deployments to Salesforce Environments falling off</td><td>QA Passed</td><td>23.1</td><td>Code Fix</td><td>Use case</td></tr><tr><td>nCino</td><td>Lack of Consistency in Filter Functionality Across Feature Management, Deployment History, Commit History, and CI Jobs</td><td>QA Passed</td><td>23.1</td><td>Code Fix</td><td>Use case</td></tr><tr><td>Version control</td><td>Unable to view the Autodraft date and managed package changes dropdown</td><td>QA Passed</td><td>23.1</td><td>Code Fix</td><td>Use case</td></tr><tr><td>Admin</td><td>Super Admin EBR Token Security Enhancement </td><td>Done</td><td>23.1</td><td>Code fix</td><td>Internal change request</td></tr></tbody></table>

#### 3 April 2024

**(ARM 23.1.25)**

<table data-full-width="true"><thead><tr><th width="171">Module</th><th width="355">Summary</th><th width="130">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Reports, CI Jobs, Deployments, Version Control</td><td>ARM overwrites any exclusions set up in CodeScan UI * Requires documentation.</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td>Deployments</td><td>Single revision deployment taking longer time to retrieve revision</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Org registration issue – resolved by displaying in Logs the exact Salesforce error</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Getting empty revision when performing single revision merge with no modifications</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Unable to create branch with branch name containing "&#x26;" through EZ-commit and Modularization</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>nCino</td><td>Failure to Display Jobs in Deployment History for Version Control using Salesforce with Single Revision of initial commit</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>nCino</td><td>Feature Deployment issue with Salesforce Org Version Control when selecting initial commit as Revision</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>nCino</td><td>Version control record deployments to Salesforce environments dropping off</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 27 March 2024

**(ARM 23.1.24)**&#x20;

<table data-full-width="true"><thead><tr><th width="145">Module</th><th width="293">Summary</th><th width="92">Status</th><th width="67">Version Reported</th><th width="70">Fix Version(s)</th><th width="81">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Org Sync question on Moderation Rule difference</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to create EZ-Commit for the new user</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Problem with scheduled code coverage reports</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Profile Comparer - Taking too long to deploy</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Issue in Merging</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Incorrect merge status issue</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>The page is taking longer time to load the metadata when selecting to show metadata members.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Vlocity DataPacks not being baselined</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Getting stuck in loading when trying to Expand ALM mappings</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>CI Deploy job link throwing pop-up error message</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Loggers added in the SCA log to display whether the baseline branch was selected during the commit and merge process</td><td><p> </p><p>Customer Coordination</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>NA</p><p> </p></td><td>No Code Fix</td><td>Loggers Added</td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Data Loader Pro jobs failing for Lead</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>nCino Deployment History - search filter criteria is not working</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unnecessary select all checkbox is showing in added and modified tab</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to view created credentials</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Returns all CI Jobs History to EBR Data irrespective of active </td><td><p> </p><p>Done</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Internal change request in EBR Data Visibility</td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Feature Deployment Issue with Salesforce Org Version Control</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Data Loader Pro</p><p> </p></td><td>Issue with Audit Fields</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin, Version Control</td><td>Unable to register the same repository twice * <br><br><mark style="background-color:yellow;"><strong>REQUIRES FEATURE FLAG</strong></mark><strong>:</strong><br><strong>SKIP_DUPLICATE_REPOSITORY_REGISTRATION_CHECK</strong></td><td>QA Passed</td><td>23.1</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Error Message: Cannot invoke "String.startsWith(String)" because the return value of "com.autorabit.entity.admin.UserProject.getProjectType()" is null. Support ticket # 109042</td><td>QA Passed</td><td>23.1</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 20 March 2024

**(ARM v. 23.1.23)**

<table data-full-width="true"><thead><tr><th>Module</th><th width="252">Summary</th><th align="center">Status</th><th align="center">Fix Version</th><th align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>nCino CI jobs created are not visible for CI job on successful deployment</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Regarding unable to approve commit request</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Very slow commits</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to create branch with '&#x26;' character getting Exception Error</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Issues after Branching Baseline</td><td align="center"><p> </p><p>Requires Customer Coordination</p><p> </p></td><td align="center"><p> </p><p>Added Loggers</p><p> </p></td><td align="center">No Code Fix</td><td align="center"></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Static Code Analysis fails with timeout error</td><td align="center"><p> </p><p>Requires Customer Coordination</p><p> </p></td><td align="center"><p> </p><p>Post fix awaiting customer confirmation.</p><p> </p></td><td align="center">Code Fix for SF CL timeout configuration. </td><td align="center"></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Observing that after the 7th file, RabitCS and Agent logs are not being created or generated. From the 8th file, they are being overridden from Existing files 1 to 7.</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs, Deployments</p><p> </p></td><td>Identified below nCino CI Job "related to VC Source job type" displaying issue in CI jobs and Deployments</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Flow Center</p><p> </p></td><td>Enable SSL for the Kafka used to communicate with FlowCenter.</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"> Use Case </td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>nCino Feature deployment failed with a “malformed query” error, Feature deployment and Ci Job.<br>nCino CI jobs the customer has run failed with an exception, and the failed records column shows zero.</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Data Loader Pro</p><p> </p></td><td>[ARM-QAN5,7] The job is currently running in progress, but the Success Record Count is showing in the Failure Count.</td><td align="center"><p> </p><p>QA Passed</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### **13 March 2024**

**(ARM v. 23.1.22)**

<table data-full-width="true"><thead><tr><th>Module</th><th width="216.6666259765625">Summary</th><th align="center">Fix Version</th><th align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Profile Comparer was taking too long to deploy</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td>When the agent is external, DevHub authentication was not properly validated in CI Jobs for DX unlock and install-type CI job</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin</td><td>Signup account creation email not received by respective created-by owner</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Deployments</td><td>packExport is not failing when selecting data packs</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td>Status Check API working incorrectly on UI</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td>Issue when deploying the release to the master branch</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Issue when creating commit labels with dots (.) post upgrade * Feature Flag required (not enabled by default):  INCLUDE_DOT_IN_SFDX_COMMITLABEL_NAME</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Intermittent issue with the Merge screen</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Commit Labels within EZ-Merge no longer sorted by latest Commits</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Reports</td><td>CodeScan analysis discrepancies in APAC Prod * Requires documentation update</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Territory metadata type is not fetched as destructive changes during EZ-Commit.</td><td align="center">23.1</td><td align="center">Code Fix</td><td align="center">Use Case</td></tr><tr><td>Dataloader</td><td>Dataloader Pro was not copying over Contact fields when migrating data</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p></p></td></tr><tr><td>Dataloader</td><td>When updating the data using a CSV file, the update operation in Dataloader was failing with the error MISSING_ARGUMENT: ID is not specified</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Dataloader </td><td>The latest record was not being fetched in the single Dataloader</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>nCino </td><td>Deployment History - search filter criteria was not working</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Dataloader </td><td>Problem loading ContentVersion object</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td>Deployment stuck</td><td align="center">23.1</td><td align="center">Code Fix</td><td align="center">Use Case</td></tr></tbody></table>

#### 6 March 2024

**(ARM v. 23.1.21)**

<table data-full-width="true"><thead><tr><th>Module</th><th>Summary</th><th align="center">Version</th><th align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td><p> </p><p>ARM</p><p> </p></td><td>Not fetching merges when trying to create a release label for Vlocity components.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Org Sync issue</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Unable to Log in to AutoRABIT via Okta</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>EZ-Merge - User Approval Setting is not working as expected</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>EZ-Commit Salesforce Org Authors not completed</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Dashboards and reports were overwritten after the deployment to PROD</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Suggestion-SF org UI</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Suggestion to display a notification if a label has already been created for the same branch previously.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Expose API for Super Admin Token Authentication to Test Registered Agents' Connections</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Added metrics in ARM DB </td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Post Deployment Org Details need to be displayed on CI Job Info pop-up</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>CI Jobs Build Page - Pagination displayed as "undefined"</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>nCino CI jobs - Date Literals Value not being populated</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>When the Source Org is deleted, scheduled CI Job is not triggered from the queue</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>[API Upgrade v59.0] Attachments Object Failed due to "Index 1 out of bounds for length 1" error</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Dataloader</p><p> </p></td><td>Unable to migrate related EmailMessage records of Case</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix </p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td>Unable to view API 59 version in CI configuration under API version dropdown.</td><td align="center">23.1</td><td align="center">Code Fix</td><td align="center">Use Case</td></tr></tbody></table>

#### 28 February 2024

**(ARM v. 23.1.20)**

| Module                                 | Summary                                                                               | Resolution                       | Cause                                 | Feature Flag                              |
| -------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------- | ----------------------------------------- |
| <p> </p><p>Admin</p><p> </p>           |  Login Error                                                                          | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Ci Jobs</p><p> </p>         | CI Jobs build date sorting is not functioning as expected for non-Admin users         | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>ARM</p><p> </p>             | SF CLI version upgrade to 2.28.6 for ARM 23.1 instances                               | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Change Request</p><p> </p> | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Version Control</p><p> </p> | Able to approve auto-rejected merge from email                                        | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Version Control</p><p> </p> | PersonAccount AutoRABIT bug                                                           | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>CI Jobs</p><p> </p>         | It is not possible to run several CI Jobs in parallel when jobs are scheduled.        | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>SFDX</p><p> </p>            | Error on create package version and install type of job.                              | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | AR\_33235\_SKIP\_UPDATE\_PACKAGE\_COMMAND |
| <p> </p><p>Dataloader</p><p> </p>      | CPQ Dataload in Developer Sandbox - Errors                                            | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>nCino</p><p> </p>           | nCino CI Job issue                                                                    | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Dataloader</p><p> </p>      | Invalid CSV file. Please check for blank columns.                                     | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Dataloader</p><p> </p>      | CSV file does not reset when you go back to the previous step in a single data loader | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Version Control</p><p> </p> | Getting Undefined Error for target branch in External Pull request                    | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Version Control</p><p> </p> | Unable to resolve conflicts in release label merge.                                   | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |
| <p> </p><p>Flow Center</p><p> </p>     | Search & Substitute rules are not applied in the pipelines.                           | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p>       | <p> </p><p> </p><p> </p>                  |

#### 21 February 2024

**(ARM v. 23.1.19)**

| Module                                         | Summary                                                                                                                            |            Resolution           |              Cause              |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------: | :-----------------------------: |
| VS Code extension Version Control              | <p> </p><p>Cannot set up VS Code Extension</p><p> </p>                                                                             | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Ci Jobs</p><p> </p>                 | <p> </p><p>CI Job and code coverage not running at correct times</p><p> </p>                                                       | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | <p> </p><p>EZ-Commit &#x26; EZ-Merge SCA validation issue</p><p> </p>                                                              | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>All Modules</p><p> </p>             | <p> </p><p>Support for Salesforce Spring ‘24 * Requires Documentation</p><p> </p>                                                  | <p> </p><p>Code Fix</p><p> </p> |          Change Request         |
| <p> </p><p>Version Control</p><p> </p>         | Unable to commit the action overrides in service appointment object.                                                               | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Quick Merge shows below pop-up                                                                                                     | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | <p> </p><p>Unable to add the reviewer's name when using an external pull request</p><p> </p>                                       | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | EZ-Merge Validation Failing: "Metadata package is empty"                                                                           | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Admin</p><p> </p>                   | Branching baseline for main branch not bringing all components from production. \* Feature Flag: METADATA\_API\_TO\_DX\_CONVERSION | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Unable to commit a profile                                                                                                         | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Release label throwing InvalidFilterExpression error                                                                               | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>nCino </p><p> </p>                  | Error message when attempting to clone a feature template: ‘Request parameters are empty/null.'                                    | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Dataloader</p><p> </p>              | Dataloader Pro issue while triggering the job                                                                                      | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Add additional metrics in ARM DB.                                                                                                  | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>nCino &#x26; Dataloader</p><p> </p> | nCino - Support for Salesforce Spring ‘24                                                                                          | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>FC, Deployments</p><p> </p>         | Flow Center API: Create a metadata bundle from an org                                                                              | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Deployments</p><p> </p>             | "Experience container" metadata type component deployment is failed for org-to-org deployment                                      | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Unable to view the revision number when clicking on prevalidation merge details.                                                   | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Version Control</p><p> </p>         | Unable to fetch date from Auto-Draft when selecting DX branch in sub-user with no mappings.                                        | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>Deployments</p><p> </p>             | Deployment failed with error: ‘Cannot invoke "java.util.Map.clear()" because "this.relatedLayoutRecordTypeIdsMap" is null’         | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| <p> </p><p>nCino</p><p> </p>                   | CI Jobs: date filter not selectable or enter date value.                                                                           | <p> </p><p>Code Fix</p><p> </p> | <p> </p><p>Use Case</p><p> </p> |

#### 12 February 2024

**(ARM v. 23.1.18)**

<table data-full-width="true"><thead><tr><th width="133">Module</th><th width="139">Summary</th><th>Status</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th><th>Feature enabled by default</th><th>Feature Flag Name</th></tr></thead><tbody><tr><td><p> </p><p>Deployments</p><p> </p></td><td><p> </p><p>Upgrade to 23.1.16 + Ubuntu OS Upgrade</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Dashboards</p><p> </p></td><td>ARM dashboard</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td><p> </p><p>Org sync - Scheduler not working</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Commit failing without any logs</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Single-revision merge taking a long time</p><p> </p></td><td>Customer Coordination [Added Loggers]</td><td><p> </p><p>No Code Fix - Added Loggers</p><p> </p></td><td><p> </p><p>No Code Fix - Added Loggers<br></p></td><td>Data</td><td><p> </p><p>NO</p><p> </p></td><td>NO</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Package.xml fetching the Excluded components during Commit</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td><p> </p><p>Smart checkbox redeployment</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Change Request </p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>PG and ARM instances not working as expected</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td>FILE_SYNC_WITH_OPTIMISTIC_LOCK</td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Commit not getting detected</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td><p> </p><p>Error while trying to select the revision from branch</p><p> </p></td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td><td><p> </p><p>NO</p><p> </p></td></tr></tbody></table>

#### 7 February 2024

**(ARM v. 23.1.17)**

<table data-full-width="true"><thead><tr><th width="99">Module</th><th width="296">Summary</th><th>Status</th><th width="126">Fix Version(s)</th><th width="106">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Administration</p><p> </p></td><td>Jira On-prem SSO Cooperation</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Random Error Message</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Need a feature to save metadata selection before deployment</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Page unresponsive in new deployment using Previous Deployment as a source type</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Administration, CI Jobs</p><p> </p></td><td>Upgrade v59 (Beta) to v59</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Administration</p><p> </p></td><td>CI Job and Code Coverage Not Running at Correct Times</td><td>Customer Coordination </td><td>Customer Coordination </td><td></td><td></td></tr><tr><td><p> </p><p>Dataloader</p><p> </p></td><td>Configuration job failure</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>In the MergeRequest, CI Job View Screen under Build title, the Merge Request comment alignment is not displaying properly; it is not getting trimmed and appears larger than expected.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Administration</p><p> </p></td><td>Unable to view ‘Should pass validation criteria for Static Code Analysis’ checkbox under commit validation settings when Salesforce API version is not mapped</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Administration</p><p> </p></td><td>Release Label artifact execution is not working.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>nCino</td><td>Partial error on CI Job - nCino-Fee Template</td><td>QA Passed</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 28 January 2024

**(ARM v. 23.1.16)**

<table data-full-width="true"><thead><tr><th>Module</th><th width="287">Summary</th><th width="132">Status</th><th width="148">Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Email communication error in EZ-Commit * Requires documentation.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Finding WaveDataflow components for commit</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>‘Not a well-formed XML.' error when attempting org-to-org deployments in UAT</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Package CI Job Issue</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Vlocity Deployment issue</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Vlocity Release label issue </td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>EZ-Commit not creating a branch</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>ARM failed to auto-reject EZ-Merge request that has Apex class with less than 90% code coverage. Merge setting enforcing 90% code coverage in mock deployment.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>CodeScan – Delta scan</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td>Code Fix [Added Loggers for customer understanding,]</td><td></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Ignore warnings option in CI jobs is not working properly</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Commit failing without any logs</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Environment Provisioning</p><p> </p></td><td>Apex Anonymous Template not downloadable</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>‘File can't be loaded’ error</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>During Profile Manger Deployment, "NULL MSG: NULL" is displaying in the log</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Using Package XML: Document XML files are not being listed in the Org compare screen</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix  </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>CI Job build is failing without printing reason in logs for BY SELECTING LAST TILE: install unlock package/managed tile.</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix </p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Dataloader Pro</td><td>Multiple issues during data masking</td><td>Customer Coordination – Added Loggers</td><td>23.1</td><td>No Code Fix – Added Loggers</td><td>Data</td></tr></tbody></table>

#### 21 January 2024

**(ARM v. 23.1.15)**

<table data-full-width="true"><thead><tr><th width="151">Module</th><th width="206">Summary</th><th>Status</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Version Control</p><p> </p></td><td>EZ-Merge 'Reviewer Comments' section not displaying comments entered by reviewer.</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Profiles Sync Issue-CustomSettings issue</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Package.xml generated from release label is other components that are not in the commits</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Finding WaveDataflow components for commit</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Error: Access token as failed while doing a branching baseline</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Provar version upgrade</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td>No Code Fix – Only Configuration change for specific customer</td><td>Customer-specific</td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Initial commit failing</td><td>Customer Coordination</td><td></td><td>No Code Fix – Added Loggers</td><td>Data </td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Users’ permissions are being reset.</td><td>Customer Coordination</td><td></td><td>No Code Fix – Added Loggers</td><td><p></p><p>Data</p><p> </p></td></tr><tr><td>CI Jobs, Version Control, Admin, Deployments</td><td>Adding authentication check on web hook APIs</td><td>QA Passed</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Change Request</td></tr><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue while deploying promotions from QAT to PRD the rule set criteria is compressing the value while deploying it to RD<br><br></td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue on Feature Deployments</td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr></tbody></table>

#### 14 January 2024

**(ARM v. 23.1.14)**

<table data-header-hidden><thead><tr><th width="151">Module</th><th width="268">Summary</th><th width="115">Fix Version(s)</th><th width="138">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>MODULE</td><td>SUMMARY</td><td>FIX VERSION</td><td>RESOLUTION</td><td>CAUSE</td></tr><tr><td>Version Control </td><td>Internal - Default SCA branch not reflected while merging </td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p></p></td></tr><tr><td>Version Control</td><td>EZ-Merge request with apex class metadata files failed to identify related test classes and auto-rejected with validation failure</td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td><p>Missing Component in Package: PROD</p><p> </p></td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Deployments</td><td><p> </p><p>Release Label not appearing in Deployment tab</p><p> </p></td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td><p> </p><p>API broken for job history</p><p> </p></td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs</td><td><p> </p><p>Deploying Flow - Property 'customErrors' not valid in version 58.0</p><p> </p></td><td> 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> Deployments</td><td>Deployment status failed when deploying Vlocity components</td><td> 22.3, 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> Version Control</td><td>On Prevalidation Commit, the SonarQube SCA process is auto-rejected, even for unsupported metadata types.</td><td><p> </p><p>23.1</p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Deployments</td><td>Brazil Prod to UAT deployment issue</td><td><p> </p><p>23.1</p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> nCino</td><td> Metadata update is failing</td><td><p> </p><p>23.1</p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> Version Control</td><td>Commit not progressing</td><td><p> </p><p>23.1</p></td><td><p> </p><p>No Code Fix - Loggers Added</p><p> </p></td><td>Data</td></tr></tbody></table>

#### 7 January 2024

**(ARM v. 23.1.13)**

<table data-full-width="true"><thead><tr><th width="146">Module</th><th width="289">Summary</th><th width="112">Fix Version</th><th width="116">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Admin</p><p> </p></td><td>Client unable to create New Branching Baseline showing loading icon</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI jobs</p><p> </p></td><td>Request to increase the build label size to 150-200 characters</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI jobs</p><p> </p></td><td>Provar CI Job run takes a very long time and stops at status "Timed-Out"</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>ARM API to perform a deployment (or a validation, or a quick deploy)</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Issue with Regex on Feature Deployments</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI jobs</p><p> </p></td><td>Team/Slack in CI job post activity notification, users should not have email dependency in email notification. Suggestion.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI jobs</p><p> </p></td><td>Package creation CI job</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI jobs</p><p> </p></td><td>On both CI Results and CI Lists, user getting the “Invalid FilterExpression: Expression size has exceeded the maximum allowed size;(Service: DynamoDb“error) when selecting the “Ungrouped” value under “group by “ filter dropdown</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>CodeScan – EZ-Commit Auto Rejected</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Client login error</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Unable to edit and save changes for Exclude Baseline Managed Package Changes</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Deployment getting failed for queued jobs</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>



**17 December 2023**

**(ARM v. 23.1.12)**

<table data-full-width="true"><thead><tr><th width="148">Module</th><th width="284">Summary</th><th width="124">Fix Version</th><th width="132">Resolution</th><th width="200">Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Profile/Permission Set Manager Report not loading</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>ARM and CodeScan integration EZ- Commit validation issue. Feature Flag: USE_MASTER_ANALYSIS_PACKAGE_DIRECTORY</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>A non admin user cannot access the repository under the VC module.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Help investigating deployment errors</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Not receiving post activity notifications</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Feedback option change to message. Will require updated documentation.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>[On-premises – Signup for Demo] The registration screen opens when clicking on 'Signup for Demo,' even if the account is already registered.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>[On-premises] Service registration tab, alignment tab not visible properly and, when clicking on the tab, redirects to the logout page.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Unable to view ‘Credential already exists’ popup under ‘My profile.’</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Previously deleted log showing on other label if created Static Code Analysis label previously deleted SCA label name.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>SFDX</p><p> </p></td><td>When creating the package on a new module for the first time through modularization, Package creation failed with the error ["SaiJun19thprofile: An object 'SaiJun19thprofile' of type Profile was named in package.xml.'] Will require updated documentation.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to view committed files in direct EZ revert commit using DX repository.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>[On-Premises] Getting 'Malformed Id: Null' error displaying for a few seconds when performing a rollback operation for Org-to-Org deployment.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>[Org Synchronization] ‘SourceOrg,’ ‘Created date,’ and ‘Created by’ filters are not working properly.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>[On-Premise Testing] CI Job with template option failed due to "Data and Metadata retrieval Failed” error.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>ARM API to perform a deployment (or validation or quick deploy)</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>[ARM-SIT] Unable to view branches in SCM history screen</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

**10 December 2023**

**(ARM v. 23.1.11)**

<table data-full-width="true"><thead><tr><th width="142">Module</th><th width="276">Summary</th><th width="111" align="center">Version(s)</th><th width="130" align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td><p> </p><p>All Modules</p><p> </p></td><td><p> </p><p>SF CLI Version upgrade to 2.19.8</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>No Code Fix</p><p> </p></td><td align="center">Configuration Change request</td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Experience bundle not properly generated when deploying using release label</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>SFDX</p><p> </p></td><td><p> </p><p>Error creating unlocked package</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>CI Job report for Master-to-BackMerge Org Sync_13-Deployment Failed</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Merge shows no modification, but a CI job is triggered</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>* User is unable to do nCino Feature Deployments * Requires documentation</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Dataloader</p><p> </p></td><td>Getting error when clicking on Dataloader configured filter </td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs and Deployments</td><td>ARM API to perform a deployment (or validation or quick deploy)</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Enchancement</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to perform merge for sub-user, getting error to re-login</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>On-premise: ‘Proxy Configuration settings,’ ‘Audit logs’ section, and ‘Pool Mgnt" screen tab are missing.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>On-premise: When trying to save the ‘Audit Logs’ section in ‘My Account’ screen, the error “Uncaught TypeError: Cannot read properties of undefined (reading 'showMessage')” is encountered in the console.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>For the 'Create and Install Package' job, when selecting 'Deploy Using Create a Scratch Org and Install Package,' after successfully completing the build, an error is displayed in the log: “this.salesForceOrgDAO” is null.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin</td><td>Getting ‘null parameters’ error when clicking on save in the user’s section.</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Unable to perform merge request for sub-user getting error to re-login.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p>Version</p><p>Control</p></td><td>Unable to perform branching baseline on sub-user, getting error to re-login</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 3 December 2023

**(ARM v 23.1.10)**

| Module          | Summary                                                                                                                                   | Fix Version(s) | Resolution                  | Cause          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------- | -------------- |
| Admin           | Issue adding user mapping                                                                                                                 | 22.3, 23.1     | Code Fix                    | Use Case       |
| Deployments     | Full org:org deployment failing with no proper reason                                                                                     | 23.1           | Code Fix                    | Use Case       |
| Admin           | Issue with registering new branch in the repository                                                                                       | 23.1           | Code Fix                    | Use Case       |
| Reports         | ARM and CodeScan integration EZ-Commit validation issue                                                                                   | 23.1           | Code Fix                    | Change Request |
| Reports         | New branch created CodeScan issue                                                                                                         | 23.1           | Code Fix                    | Use Case       |
| Deployments     | Destructive package is not generated properly when deploying from git revisions                                                           | 23.1           | Code Fix                    | Use Case       |
| Admin           | nCino View Object Failing                                                                                                                 | NA             | No Code Fix - Added Loggers | Data           |
| Deployments     | Org sync not completing                                                                                                                   | NA             | No Code Fix - Added Loggers | Data           |
| Dataloader      | Corrected a spelling mistake in ARM steps.                                                                                                | 23.1, 22.3     | Code Fix                    | Use Case       |
| Dataloader      | Corrected data seeding error preventing upsert                                                                                            | 23.1, 22.3     | Code Fix                    | Use Case       |
| Reports         | Getting ‘cannot invoke "String.length()" because of "text" is “null”’ error when performing the ‘Get latest reports’ in Weekly reports    | 23.1           | Code Fix                    | Use Case       |
| Reports         | When navigating to Static Code Analysis screen from Reports module, getting the “comparison method violates its general contract!” error. | 23.1           | Code Fix                    | Data           |
| Version Control | On DX branch release label artifact execution, on deleted components, the destructive changes artifact preparation is not generated.      | 23.1           | Code Fix                    | Use Case       |
| nCino           | On-premise testing: CI Job with template option failed due to "data and metadata retrieval failed” error                                  | 23.1, 22.3     | Code Fix                    | Use Case       |
| CI Jobs         | Failed to deploy destructive changes though CI jobs.                                                                                      | 23.1           | Code Fix                    | Use Case       |

#### 26 November 2023

**(ARM v 23.1.9)**

<table data-full-width="true"><thead><tr><th width="122">Module</th><th width="310">Summary</th><th width="145">Fix Version(s)</th><th width="134">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Admin</td><td>Branching baseline issue</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>The new feature of merging only revision in the CI job build is not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>CI job filter not working properly</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Commit not getting detected</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Rejecting a commit is merging the changes</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Unable to save Pull Request Plugin config</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>AR commit File Diff process is failing with errors</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Merge auto-rejected but CI job triggered</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Changing role from Dev to Admin shows orgs and branches in New EZ- Commit without mapping under profile</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control and Deployment</td><td>Release Label Artifact not including code for a commit</td><td>23.1</td><td>Loggers Added</td><td>Data</td></tr><tr><td>Dataloader</td><td>Dataloader Pro jobs causing huge threads pileup</td><td>23.1</td><td>Enhancement</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Data Retention – CI Jobs - Observing 'java.lang.NumberFormatException' error in the CI Retention process log when processing the string '2023-08-26.' Please check the date formatting to ensure it is being treated as a string and not causing the exception.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>While submitting the ALM commit with these “&#x3C;ALM Issue ID>“, “{ALM Issue ID}” ALM patterns, unable to submit the commit</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Sub-user - Deployment History - While changing the date range filter, getting "Cannot invoke "String.equalsIgnoreCase(String)" because the return value of "com.autorabit.entity.deployment.DeploymentHistory.getCreatedBy()" is null" error</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>With Release label deployment, the flow-meta.xml retrieval issue both constructive and destructive</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 22 November 2023

<table data-full-width="true"><thead><tr><th width="126">Module</th><th width="290">Summary</th><th width="138">Fix Version(s)</th><th width="138">Resolution</th><th width="98">Cause</th><th width="158">Enabled by default?</th><th>Feature Flag Name</th></tr></thead><tbody><tr><td>Version Control</td><td>Branch Protection Policy enforced and behavior of EZ- merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td>NO</td><td>GIT_LOGGEDIN_USER_AS_COMMIT_USER</td></tr><tr><td>Version Control</td><td>Issue while creating feature branches in EZ - Commit screen</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td></td><td></td></tr><tr><td>Version Control</td><td>Upload File option not available during EZ- commit with Option package manifest</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td></td><td></td></tr></tbody></table>

#### 19 November 2023

**(ARM v. 23.1.8)**

<table><thead><tr><th width="121">Module</th><th width="283">Summary</th><th width="101">Fix Version</th><th width="105">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Deployment tab - Redeploy/Promote issue</td><td>22.3, 23.1</td><td>Added Loggers</td><td>Data</td></tr><tr><td>Dataloader</td><td>Optimize the Dataloader Pro job logs in the rabit cs log</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Unable to create Feature Migration Template on Debt Schedule object</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>All Modules</td><td>Invalid Email ID</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs, Deployments, Version Control, Admin</td><td>Org Sync diff report differs for the same source org compared to different orgs.</td><td>23.1</td><td>Code Fix</td><td>Use Case *</td></tr><tr><td>Dataloader</td><td>Urgent: AutoRABIT is down</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Issue with Block button during Merge Conflict</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>CI job deployment failing: Restriction rules deployed as moderation rule and made the deployment bugged</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Urgent: Rollback of specific components - Issue</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Unexpected behavior when disabling component category on rollback destructive changes.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>SFDX</td><td>Error while using Scratch Org Management tab</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>All Modules</td><td>ARM&#x3C;>ULP Integration Issues</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Auto-reject on commit validation for SCA &#x26; Auto-reject setting in Merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 15 November 2023

<table><thead><tr><th width="118">Module</th><th width="279">Summary</th><th width="107">Fix Version</th><th width="108">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>CI Jobs</td><td>CI Job is not picking up changes committed on the branch, indicating "No modifications made."</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Org Synchronization – constructive &#x26; destructive changes are not working together</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Sync error between ARM and GIT</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Deployment validation not working correctly during new EZ-Merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Merging only revision in the CI job build not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 12 November 2023

**(ARM v. 23.1.7)**

<table><thead><tr><th width="151">Module</th><th width="249">Summary</th><th width="138">Fix Version(s)</th><th width="119">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>During Org Sync, file names are being repeated as part of the deployment results.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>User is unable to see the Deployment History.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs &#x26; Deployments</td><td>User is unable to deploy static resource.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Reports</td><td>Scheduled Code Coverage Reports are running at the wrong time.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>User is unable to create Feature Migration Template on Debt Schedule object.</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Dataloader</td><td>User is unable to upload files and update records; system logs user out instead.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>User is getting timeouts in merge screen.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 5 November 2023

**(ARM v. 23.1.6)**

<table><thead><tr><th width="153">Module</th><th width="277.3333740234375">Summary</th><th width="121">Fix Version(s)</th><th width="108">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td>All Modules</td><td>SF CLI version upgrade to 2.14.6</td><td>23.1</td><td>Code Fix</td><td>Enhancement</td></tr><tr><td>Environment Provisioning</td><td>View environment provisioning templates</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Enhancement</td></tr><tr><td>Admin</td><td>Branching baseline is not picking all components from production</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Help with destructive change</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Merge request is failing due to validation credentials</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs, Deployments</td><td>Issues with a release – related to Feature Flag - not automatically deployed: STANDARD_VALUE_SET_DELTA</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Version Control</td><td>Approval button is not visible after successful merge validation</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Version Control</td><td>Create artifact: not completed</td><td>23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Admin</td><td>AutoRABIT login not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Error pop-up during merge type selection as Commit Label in EZ-Merge</td><td>23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>CI Jobs</td><td>AutoRABIT AccelQ Integration/ bhg-inc.com</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td><br>Developer API for CI Jobs History not returning latest results.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Ability to trigger nCino CI jobs using REST API</td><td>23.1</td><td>Code Fix</td><td>Customer Request</td></tr><tr><td>CI Jobs</td><td>For run test automation scripts job: More than one cycle is not displayed in the individual job history</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Unable to delete feature branch under merge request, getting internal server error</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Unable to view the entry of recently created merge request in the merge request history screen</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Criteria met ALM's not getting fetched under merge request</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Instead of POST methods need to change the GET</td><td>23.1</td><td>Code Fix</td><td>Customer Request</td></tr></tbody></table>

#### 27 October 2023

**(ARM v. 23.1.5)**

This was a maintenance release. The following items were enhanced, fixed, or added:

* <mark style="background-color:blue;">**Loggers**</mark> were added to **Reports** and **Dashboard** modules in versions 22.3 and 23.1 due to a data error in which users were unable to fetch a Salesforce **code coverage** report.
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Deployments** and **Org Synchronization** modules in versions 22.3 and 23.1 enabling users to **change deploy text for validations**.
* A code fix was applied to the **CI Jobs** module in version 23.1 identified by use case to **enable validation CI Job comments** to be visible on the **Bitbucket PR**.
* A code fix was applied to the **Admin** module of version 23.1 due to a use case in which modification logs were needed for **Version Control mapping setup**.
* A code fix was applied to the **Version Control** module of version 23.1 related to a use-case error in which **External Pull Requests, when expanding the files in the diff, content was not visible** and showing as undefined.
* A code fix was applied to the **Version Control** module of version 23.1 related to a use-case error in which **External Pull Requests, when expanding files in the diff,** show **duplicate** content.
* A code fix was applied to the **nCino** module of versions 22.3 and 23.1 due to a use-case scenario during dataset creation with saving only user info in **Json that is relevant to current dataset**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error with an **AR merge failing**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error in which the **incorrect removal of Custom Application type in package.xml on EZ-Commit** via AR occurred.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 in which two **external pull request** issues were occurring.

#### 25 October 2023

This was an interim maintenance release. The following items were enhanced, fixed, or added:

* A Code Fix was applied to the **Deployments** module due to the **Deployment initiated using Org Synchronization failing** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Version control** module due to a **Validation Error** requiring **Feature Flag:** **VALIDATE\_DEPLOY\_PICK\_FILECHANGES\_FROM\_DIFF** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Reports** module due to the **Weekly Code/ Test Coverage Report** taking a long time caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Admin** module due to an **SSO Error** as of Sept 25 caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Admin** module due to an AutoRABIT **Login Issue** caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Version Control** module due to **validation/merge errors** after latest release caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Dataloader** module due to the **download button not working** caused by a use case with a fix applied to versions 23.1.

**22 October 2023**

**(ARM v. 23.1.4)**

This is a maintenance release. The following items were enhanced, fixed, or added.

* Performed a code fix to version 23.1 affecting the **Reports** module resulting from a use-case error with **code coverage report emails missing test class errors in the subject.**
* Applied a code fix to version 23.1 for the **Deployments** module resulting from a use-case scenario with user **unable to see deployment history**.
* Instituted a code fix to version 23.1 for the **CI Jobs** module resulting from a use-case error with the **org management page**.
* Implemented a code fix to versions 22.3 and 23.1 affecting the **CI Jobs** module due to a use-case issue to **SFDX/CI jobs with package version installation key**.
* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue related to **custom label translation file**.
* Applied a code fix to versions 22.3 and 23.1 related to the **Deployments** module for a use-case error with previous **deployment label 'add members'** option not working.
* Performed a code fix to version 23.1 affecting the **Admin** module due to a use-case error with **MyProfile not redirecting properly** and showing the **profile icon** after clicking on the **'profile' button.**
* Implemented a **flow center change** to versions 22.3 and 23.1 for the **Dataloader** module due to a use-case error with the **download button not working**.

#### 18 October 2023

This interim release consisted of the following:

* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue with a **custom label translation file**.

#### 15 October 2023

**(ARM v23.1.3)**

**AutoRABIT provided the API 59.0 changes as part of its weekly fixes on both 22.3 and 23.1. This is available only for ARM modules, not for Dataloader or nCino. For DL and nCino, API 59.0 changes will be available next week as part of the Wednesday fixes deployment.**

This is a maintenance release. The following items were enhanced, fixed, or added.

* Instituted an <mark style="background-color:blue;">**enhancement**</mark> via code fix to versions 22.3 and 23.1 affecting **all ARM modules**, applying **Salesforce v.59 upgrade** for **Winter 2024**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **CI Jobs** module concerning a **package directory** issue.
* Applied a code fix to versions 22.3 and 23.1 due to a use-case scenario pertaining to the **Environmental Provisioning** module with **users not able to generate** a **migration template** using the **migrate custom setting data module**.
* Issued a code fix to versions 22.3 and 23.1 for a use-case error in the **Version Control** module with a **custom label translation file**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Deployments** module concerning **bugs in deployment** with **multi-packages** and **static resource**.
* Applied a code fix to version 22.3 resulting from a use-case error affecting **Dataloader** returning an '**invalid cross reference id**' error for **ProcessInput** and **ProcessingInputCondition** objects.
* Implemented a code fix to version 23.1 for a use-case error to the **Version Control** module, in which **duplicate commits** were being created.
* Performed a code fix to version 23.1 for a use-case error to the **Version Control** module pertaining to **Deployment history**, with the **deployment status not being visible**.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **nCino** module in which users are **unable to deploy nCino feature (RBC)**, instead returning a '**malformed query**' result.
* Performed a code fix to version 23.1 relating to a use-case error to the **Version Control** module with users **unable to perform new pull request commit** due to **commit template permission**.
* Executed a code fix to version 23.1 relating to a use-case error affecting the **Version Control** module with users continually **getting a login redirect error** when trying to **create a branc**h through an **EZ-Commit**.
* Performed a code fix to version 23.1 relating to a use-case error in the **Version Control** module with users **unable to create a commit label**, continually getting a **login redirect** error.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **Admin** module, particularly a **SuperAdmin** user, not getting any response to the **scheduler's service registration button** without **expanding** the selection.
* Initiated a code fix related to a use-case scenario in version 23.1 affecting the **Version Control** module with **release labels getting failed after restarting** the agent.
* Applied a code fix related to a use-case scenario affecting version 23.1 in the **nCino** module, when **parallel CI jobs limit** was reached, the **job** was **not added** to the **queu**e.
* Performed a code fix to correct a use-case error in version 23.1 related to the **nCino** module for a **merge missing changes**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the Version Control module, in which users were **unable to create/append a revision** to an **existing label** for a **sub-user**.
* Implemented a code fix to version 22.3 relating to a use-case error in the **Version Control** module in which the user was getting **empty error pop-ups** under the **ALM management screen** for a **sub-user**, not displaying the **ALM item**s.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **nCino** module with a **job deployment** issue.
* Applied a code fix to version 23.1 relating to a use-case error affecting the **nCino** module for a **CI job build getting failed**.
* Initiated a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **nCino** module for a '**no modifications status**' displayed for a **version control BR job**.

#### 11 October 2023

* Performed a code fix to versions 22.3 and 23.1 related to a use case scenario affecting the **Version Control** module related to **ALM tickets** being **bugged** after using the **ALM sync refresh**.
* Performed a code fix to version 23.1 related to the **Deployments** and **CI Jobs** modules affecting a use-case error being issued during **CI Deployment** for **property 'userLicense' not valid** in version 57.0.

#### 8 October 2023

#### (ARM v23.1.2)

This is a maintenance release. The following items were enhanced, fixed, or added.

* Performed a code fix to versions 22.3 and 23.1 for a use-case error affecting the **Admin** module relating to **code coverage issues**.
* Applied a code fix to versions 22.3 and 23.1 related to a use-case error in the **Deployments** module concerning a **flow component missed in the deployment**.
* Implemented a code fix to versions 22.3 and 23.1 for a use-case error related to a specific customer’s fields for **redeployment**.
* Applied a code fix to version 23.1 for a use-case error affecting the **Deployments** module related to **metadata production and a deployment issue**.
* Integrated a code fix to version 23.1 affecting the **Deployments** and **CI Jobs** modules for a **deployment issue running all test classes**.
* Performed a code fix to the **nCino** module in version 23.1 pertaining to **Salesforce Orgs not showing** as **source orgs** for **nCino feature management deployments**.
* Applied a code fix to the **nCino** module in versions 22.3 and 23.1 pertaining to **\[arm-qan] no modification status displayed for version control BR job**.
* Added **loggers** to versions 22.3 and 23.1 to correct a use-case error in the **Deployments** module pertaining to a **deployment bug** occurring with **multi packages** and **static resources**.

#### 1 October 2023

**(ARM v23.1.1)**

This is a maintenance release. The following items were enhanced, fixed, or added.

* A code fix was applied to the version control module in releases 22.3 and 23.1 due to a use-case error with a **user being unable to create a new commit**.
* A code fix was performed in the 23.1 release to the version control module for a use-case error when **merging destructive changes**.
* A code fix was instituted to the CI Jobs module in version 23.1 to address when **a CI job has two different package directories**. Changes were failing under one package when the analysis was completed in CodeScan.
* A code fix was performed for release versions 22.3 and 23.1 to the deployments module for a use-case error resulting in a **buggy deployment** with **multi packages** and the **static resources** being bugged as well.
* A code fix was applied to the version control module in releases 22.3 and 23.1 concerning a use-case error for an **EZ-Commit**, where the **user was unable to view the 'deleted components' tab** for the commit template when unchecking the '**skip mappings**' checkbox.
* A code fix was implemented to versions 22.3 and 23.1 to correct an error with the deployments module due to a **deployment** initiated using **org synchronization failing**.
* A code fix was applied to releases 22.3 and 23.1 due to a use-case error in which the **registration date** of the **repository** **was not correct** in the **version control repository** (**created date** in AutoRABIT).
* A code fix was performed to versions 22.3 and 23.1 due to a data error in the version control module **preventing ALM working items from loading**.
* A code fix was initiated for versions 22.3 and 23.1 due to a data error affecting the reports module, which occurred when executing a **static code analysis** (CodeScan) report.
* A code fix was performed to version 23.1 in the version control module resulting from a data error on the **commit history screen**.
* A code fix was implemented in versions 22.3 and 23.1 to the version control module related to a use-case error wherein the **baseline job** has **modified the Salesforce folder structure in GitHub**.
* **Loggers were added** in the version 23.1 release due to a data error in the version control module causing **duplicate commits** to be created.
* A code fix was implemented to the nCino module for versions 22.3 and 23.1 for a data error in which the **records count** was **not** being **updated** in the object sidebar for the version control baseline revision job.

#### 24 September 2023

**(ARM v23.1)**\
This is a maintenance release. The following items were enhanced, fixed, or added:

* A code fix was applied to the Deployment module due to a data error concerning an Org difference pulling changes from the managed packages.

***

## ARM Release Notes 22.3

We would like to inform you about the End of Life (EOL) for ARM version 22.3. Per our support agreement, this version is now more than 365 days old and is no longer supported. As part of our ongoing commitment to providing the best possible experience for our users and maintaining the highest standards of security and performance, we have made the decision to discontinue support for ARM 22.3.

**End of Life Date: April 1, 2024**

What Does This Mean?

* End of Support: As of April 1, 2024, we will no longer provide maintenance updates, bug fixes, or technical support for ARM 22.3. This includes both security and non-security updates.
* Security Risks: Continuing to use ARM 22.3 after the end of support date may expose your system to potential security vulnerabilities, as we will no longer release security patches.
* Upgrade Recommendations: We strongly recommend migrating to a supported version of ARM to ensure continued reliability, security, and performance. Our team is available to assist you with this transition process and provide guidance on your upgrade.
* Accessing Resources: While official support for ARM 22.3 will no longer be available, you can still access existing resources such as documentation, knowledge base articles, and the Knowledge Hub for reference purposes.

Action Required:

To mitigate any potential risks associated with the EOL of 22.3, we urge you to take proactive steps towards upgrade immediately. Our customer success and support team are here to assist you every step of the way. Please reach out to your CSM to plan this work.

We understand that this transition may present challenges, and we sincerely apologize for any inconvenience it may cause. However, we believe that focusing our efforts on our latest offerings will ultimately benefit you with enhanced features, improved performance, and better security.

Thank you for your understanding and continued support.



**December 2022 - Version 22.3 - New Features, Enhancements, Improvements and Changelogs**

**Date of release:** _18 December 2022_\
**Article last updated:** 31 _July 2023_

### New Features <a href="#new-features" id="new-features"></a>

#### 1. Retention Policy <a href="#id-1-retention-policy" id="id-1-retention-policy"></a>

You can now define a data **Retention Policy** and choose how much data should be stored for how long. ARM will now be considerably quicker by eliminating outdated data. Clearing out old and useless data from the database and moving it to the archives keeps the application from underperforming and improves speed across all modules.

A weekly clean-up will ensure that the application runs smoothly. The default data retention period is set as 12 months which will be implemented with the release of **ARM version 22.3**. Admins can specify the duration of data retention in the history tables from the My Account section and change the retention period from **12 months** to **6 months** or **3 months**.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings.md)

#### 2. Search, Group, and Filter CI Job List <a href="#id-2-search-group-and-filter-ci-job-list" id="id-2-search-group-and-filter-ci-job-list"></a>

Finding a **CI Job** has never been easier. Instead of scrolling through endless pages, you can search for a job or a group by simply typing the name in the new dropdown lists. You can further narrow the search results by combining these two options to look for a particular job within a group.

Additionally, the **filter** feature provides further options to narrow the search results by source type, date range, and more.\
[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-list.md)

#### 3. Ability to Abort a Vlocity Deployment <a href="#id-3-ability-to-abort-a-vlocity-deployment" id="id-3-ability-to-abort-a-vlocity-deployment"></a>

We just included new functionality to the **ARM 22.3 version** that allows users to terminate an ongoing Vlocity deployment process or abort it if get stuck. The **Deployment History** screen contains the **Abort** option, which allows you to terminate the deployment process.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-I1GT03M7.png)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Release Label Revamp <a href="#id-1-release-label-revamp" id="id-1-release-label-revamp"></a>

The revamp of the **Release Label** page is the feature of version 22.3 that stands out the most. This enhancement is actually a collection of multiple smaller enhancements, each of which is briefly discussed in this section.

* While creating a release label, you can choose the specific period for which you want to retrieve the **commit history** instead of loading the entire commit history, which could take a really long time.
* You can also create a release label while simultaneously creating a **package** simply by selecting a conveniently located checkbox on the same screen.
* The **selected revisions** are also displayed on the same screen and updated dynamically as you select/unselect revisions.
* Release labels are **color-coded** on the **Release Label Summary** screen for easier identification, and the search now provides leaner results.

[**Read more →**](../../../product-guides/arm/arm-features/version-control/change-labels/release-labels.md)

#### 2. Additional Metadata Support in Search and Substitute <a href="#id-2-additional-metadata-support-in-search-and-substitute" id="id-2-additional-metadata-support-in-search-and-substitute"></a>

Additional metadata types are now compatible with the **Search and Substitute** rule, allowing the application to use them for Deployments and Commits.

Until now, the Search and Substitute functionality only had the ability to select a metadata type and then perform the search for substrings across all members in that type. But now, you can select specific metadata members in a type and substitute values for that member(s).

This enhancement is also helpful when users want to add object permissions only to the production and not to the lower sandboxes.

It is also beneficial to have this feature so that the rules can be created and used in **CI Jobs** to do the replacements automatically, depending on the deployment settings in the CI Job.\
[**Read more →**](../../../product-guides/arm/arm-administration/search-and-substitute.md)

#### 3. Additional details in the Users Export List <a href="#id-3-additional-details-in-the-users-export-list" id="id-3-additional-details-in-the-users-export-list"></a>

**Export List** is a comprehensive list of all registered users with an organization. This list can be downloaded from the **Users** module. It includes details like the users' name, email, and title; and information about user accounts created, modified, deactivated, and deleted.

With the recent release, the **Export List** will include a few additional details related to the **last login** to ensure security and compliance. Details like the **location, login type, IP address, coordinates,** and the **browser** used.

The access level of users is not mentioned in the export list for security reasons, i.e., if any users are **Admin** or **Super Admin**, this will not be specified. The company can share this list, if required, with people both inside and outside their organization without jeopardizing the confidentiality of the access granted to the users.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/users-roles-and-permissions.md)

#### 4. Dataloader Clone process <a href="#id-4-dataloader-clone-process" id="id-4-dataloader-clone-process"></a>

In addition to providing a new name, **Dataloader users** can now specify a different Salesforce org as a source or destination for the operation while cloning an existing job. This helps the users to reuse the same job configuration with a different Salesforce org without going through the entire process again.

For the **Extract** operation, users have the option to edit the query corresponding to the new org selected. For **Insert/Update/Upsert/Delete** operations, users have the option to upload a different **.CSV** file instead of the original one. Validation is done to verify whether the object is available in the new org and also if the user edits the query for the cloned process.\
[**Read more →**](./#4-dataloader-clone-process)

***

### Improvements <a href="#improvements" id="improvements"></a>

* The `/syncbranchcommits` service is no longer supported. The users will no longer require **Auto-sync** functionality to create a release label. This simplifies the function's use and gets rid of unnecessary steps.
* For improved user experience, the **metadata.zip** file upload option has been added to the **New Deployment** page itself. When uploading large files, this is extremely useful.
* The **password policy** is reduced from **13** previously used passwords not being allowed to **5** previously used passwords. This gives users more options while resetting their passwords after the **three months** period or if they forget their password.
* Improvements have been made to **VC Repo flow** as well as to **Salesforce Org flow**. You can now run scans on a repo or an org to be tagged to the same project and run comparisons so that you have traceability across the scans. The comparison feature allows for every delta scanned to be compared with the baseline. Scans are run on the source, and the results are available in the **Reports** module. Users can trace the jobs run using the unique identifier.\
  Click [HERE](../../../product-guides/arm/static-code-analysis.md) to see a few points to note about these improvements.
* **Super Admin** and the user currently logged in are disabled for ALL actions. They cannot be added, deleted, suspended, activated, deactivated, edited, or their roles delegated to other users. Super Admin is displayed at the top of the users' list for easy identification.
* The **Users** module now displays the last login date and time of the users instead of the phone number, and the first and last names appear under the single **Name** column for better monitoring and tracking.
* **Super Admin** can now enter the desired thread pool count while registering an ARM agent.
* Customers can now request for **Pendo** and **Full Story** to be enabled or disabled for their instance. Simple toggle buttons to do this are added under the **Product Analytics** section on the **Super User Accounts** page. Only **Super Admin** will have access to this section.
* In **DataLoader**,
  * The number of records that are going to be impacted by the specific operation (Extract, Insert, Update, Upsert, or Delete) is displayed as a message before the operation begins and also on the **Summary** screen as **Records**.
  * **Filters** have been added to differentiate between the mapped and unmapped fields when auto-map is selected.
  * **Success** and **error count** of records is displayed while the job is still in progress.\
    Click [HERE](https://knowledgebase.autorabit.com/docs/single-dataloader) to read more about these improvements for each of the operations.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 28 February 2024

**(ARM v. 22.3.55)**

| Module                                 | Summary                                                                                    | Fix Version                 | Resolution                       | Cause                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------- | -------------------------------- | ------------------------------- |
| <p> </p><p>Version Control</p><p> </p> | Merges are not being fetched when trying to create a release label for Vlocity components. | <p> </p><p>22.3</p><p> </p> | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| Version Control                        | Unable to Commit the Action Overrides in Service Appointment Object                        | 22.3                        | Code Fix                         | Use Case                        |

#### 28 January 2024

**(ARM v. 22.3.54)**

<table data-full-width="false"><thead><tr><th width="130">Module</th><th width="247">Summary</th><th width="113">Status</th><th width="77">Fix Version(s)</th><th width="93">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Vlocity Deployment issue</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Not fetching merges when trying to create a release label for Vlocity components</td><td>QA Passed</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 21 January 2024

**(ARM v. 22.3.53)**

<table data-full-width="true"><thead><tr><th width="151">Module</th><th width="206">Summary</th><th>Status</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue while deploying promotions from QAT to PRD the rule set criteria is compressing the value while deploying it to RD<br><br></td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue on Feature Deployments</td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr></tbody></table>

#### 14 January 2024

**(ARM v. 22.3.52)**

<table data-header-hidden><thead><tr><th width="128">Module</th><th width="313">Summary</th><th width="90">Fix Version(s)</th><th width="111">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>MODULE</td><td>SUMMARY</td><td>FIXVERSION</td><td>RESOLUTION</td><td>CAUSE</td></tr><tr><td> Admin</td><td><p> </p><p>After baselining the branch, it did not pull all metadata for development.</p><p> </p></td><td>22.3</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> Deployments</td><td>Deployment status failed when deploying Vlocity components</td><td>22.3 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

**10 December 2023**

**(ARM 22.3.51)**

<table data-full-width="true"><thead><tr><th width="118">Module</th><th width="263">Summary</th><th width="111" align="center">Version(s)</th><th width="130" align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td> nCino</td><td>User is unable to do nCino Feature Deployments <br>* Requires documentation</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin</td><td>Getting ‘null parameters’ error when clicking on save in the user’s section.</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 3 December 2023

**(ARM v. 22.3.50)**

| Module      | Summary                                                                                                  | Fix Version(s) | Resolution                  | Cause    |
| ----------- | -------------------------------------------------------------------------------------------------------- | -------------- | --------------------------- | -------- |
| Admin       | Issue adding user mapping                                                                                | 22.3, 23.1     | Code Fix                    | Use Case |
| Admin       | nCino View Object Failing                                                                                | NA             | No Code Fix - Added Loggers | Data     |
| Deployments | Org sync not completing                                                                                  | NA             | No Code Fix - Added Loggers | Data     |
| Dataloader  | Corrected a spelling mistake in ARM steps.                                                               | 23.1, 22.3     | Code Fix                    | Use Case |
| Dataloader  | Corrected data seeding error preventing upsert                                                           | 23.1, 22.3     | Code Fix                    | Use Case |
| nCino       | On-premise testing: CI Job with template option failed due to "data and metadata retrieval failed” error | 23.1, 22.3     | Code Fix                    | Use Case |

#### 26 November 2023

**(ARM v. 22.3.49)**

<table data-full-width="true"><thead><tr><th width="120">Module</th><th width="327">Summary</th><th width="140">Fix Version(s)</th><th width="124">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Post activities, particular job status showing as FAILED in ARM even job execution completed with succeed</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Getting empty Configuration under "Configure Default SCA Baseline Branches"</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Able to view empty role under permissions</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 19 November 2023

**(ARM v. 22.3.48)**

<table><thead><tr><th width="121">Module</th><th width="283">Summary</th><th width="101">Fix Version</th><th width="105">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployments</p><p> </p></td><td>In sub-user, unable to get the branch in Salesforce Org Mappings section in SF Org Management screen if Admin user given only admin module permission.</td><td><p> </p><p>22.3</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Deployment tab - Redeploy/Promote issue</td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td>Added Loggers</td><td><p> </p><p>Data</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Unable to create Feature Migration Template on Debt Schedule object</td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>All Modules</p><p> </p></td><td>Invalid Email ID</td><td>22.3, 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 15 November 2023

<table><thead><tr><th width="118">Module</th><th width="279">Summary</th><th width="107">Fix Version</th><th width="108">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Page unresponsive in new deployment for "previous deployment" as source type</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 12 November 2023

**(ARM v. 22.3.47)**

<table><thead><tr><th width="109">Module</th><th width="240">Summary</th><th width="136">Fix Version(s)</th><th width="120">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td>nCino</td><td><p> </p><p>User is unable to create Feature Migration Template on Debt Schedule object.</p><p> </p></td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 5 November 2023

**(ARM v. 22.3.46)**

<table data-full-width="true"><thead><tr><th width="145">Module</th><th width="218">Summary</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>All Modules</td><td>New User Creation</td><td>22.3</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td>Environment Provisioning</td><td>View environment provisioning templates</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Enhancement</p><p> </p></td></tr><tr><td>Admin</td><td>Branching baseline is not picking all components from production</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Deployments</td><td>Help with destructive change</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Merge request is failing due to validation credentials</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs, Deployments</td><td>Issues with a release – related to Feature Flag not automatically set: STANDARD_VALUE_SET_DELTA </td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Data</p><p> </p></td></tr><tr><td>Version Control</td><td>Approval button is not visible after successful merge validation</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Data</p><p> </p></td></tr></tbody></table>

#### 27 October 2023

**(ARM v. 22.3.45)**

This was a maintenance release. The following items were enhanced, fixed, or added:

* <mark style="background-color:blue;">**Loggers**</mark> were added to **Reports** and **Dashboard** modules in versions 22.3 and 23.1 due to a data error in which users were unable to fetch a Salesforce **code coverage** report.&#x20;
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Environment Provisioning** module in version 22.3 to enable users to **view Environment Provisioning** templates.
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Deployments** and **Org Synchronization** modules in versions 22.3 and 23.1 enabling users to **change deploy text for validations**.
* A code fix was applied to the **nCino** module of versions 22.3 and 23.1 due to a use-case scenario during dataset creation with saving only user info in **Json that is relevant to current dataset**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error with an **AR merge failing**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error in which the **incorrect removal of Custom Application type in package.xml on EZ-Commit** via AR occurred.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 in which two **external pull request** issues were occurring.

#### 25 October 2023

This was a maintenance release. The following items were enhanced, fixed, or added by code fixes resulting from use-case scenarios:

* A Code Fix was applied to the **Deployments** module due to the **Deployment initiated using Org Synchronization failing** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Version control** module due to a **Validation Error** requiring **Feature Flag:** **VALIDATE\_DEPLOY\_PICK\_FILECHANGES\_FROM\_DIFF** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Reports** module due to the **Weekly Code/ Test Coverage Report** taking a long time caused by a use case with a fix applied to versions 22.3 and 23.1.

**22 October 2023**

**(ARM v. 22.3.44)**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Implemented an <mark style="background-color:blue;">**enhancement**</mark> to version 22.3 identified as part of a use-case issue affecting the **Deployments** and **Org Synchronization** modules requiring changing deploy text for validations.&#x20;
* Implemented a code fix to versions 22.3 and 23.1 affecting the **CI Jobs** module due to a use-case issue to **SFDX/CI jobs with package version installation key**.
* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue related to **custom label translation file**.&#x20;
* Applied a code fix to versions 22.3 and 23.1 related to the **Deployments** module for a use-case error with previous **deployment label 'add members'** option not working.
* Added **loggers** to version 22.3 affecting the **Version Control** module due to a use-case error with **user roles missing**.
* Added **loggers** to version 22.3 affecting the **CI Jobs** module resulting from a use-case with **automated package generation CI job AR server exception error**.
* Implemented a **flow center change** to versions 22.3 and 23.1 for the **Dataloader** module due to a use-case error with the **download button not working**.

#### 18 October 2023

This interim release consisted of the following:

* Performed a code fix to versions 22.3 and 23.1 affecting the Version Control module for a use-case issue with a custom label translation file.

#### 15 October 2023

**(ARM v22.3.43)**

**AutoRABIT provided the API 59.0 changes as part of its weekly fixes on both 22.3 and 23.1. This is available only for ARM modules, not for Dataloader or nCino. For DL and nCino, API 59.0 changes will be available next week as part of the Wednesday fixes deployment.**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Instituted an <mark style="background-color:blue;">**enhancement**</mark> via code fix to versions 22.3 and 23.1 affecting **all ARM modules**, applying **Salesforce v.59 upgrade for Winter 2024**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **CI Jobs** module concerning a **package directory** issue.
* Applied a code fix to versions 22.3 and 23.1 due to a use-case scenario pertaining to the **Environmental Provisioning** module with users **not able to generate a migration template** using the **migrate custom setting** data module.&#x20;
* Issued a code fix to versions 22.3 and 23.1 for a use-case error in the **Version Control** module with a **custom label translation file**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Deployments** module concerning **bugs in deployment with multi-packages and static resource**.
* Applied a code fix to version 22.3 resulting from a use-case error affecting **Dataloader** returning an '**invalid cross reference id**' error for **ProcessInpu**t and **ProcessingInputCondition** objects.
* Performed a code fix to version 23.1 relating to a use-case error to the **Version Control** module with users **unable to perform new pull request commit** due to **commit template permission**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Version Control** module, in which users were **unable to create/append a revision** to an **existing label** for a **sub-user**.
* Implemented a code fix to version 22.3 relating to a use-case error in the **Version Control** module in which the user was getting **empty error pop-ups** under the **ALM management screen for a sub-user**, not displaying the **ALM items**.
* Initiated a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **nCino** module for a '**no modifications status**' displayed for a version control BR job.

#### 11 October 2023

* Performed a code fix to versions 22.3 and 23.1 related to a use case scenario affecting the **Version Control** module related to **ALM tickets being bugged** after **using the ALM sync refresh**.

#### 8 October 2023

#### (ARM v22.3.42)

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Performed a code fix to versions 22.3 and 23.1 for a use-case error affecting the **Admin** module relating to **code coverage issues**.
* Applied a code fix to versions 22.3 and 23.1 related to a use-case error in the **Deployments** module concerning a **flow component missed in the deployment**.   &#x20;
* Implemented a code fix to versions 22.3 and 23.1 for a use-case error related to a specific customer’s fields for **redeployment**.
* Applied a code fix to the **nCino** module in versions 22.3 and 23.1 pertaining to **\[arm-qan] no modification status displayed for version control BR job**. &#x20;
* Added **loggers** to versions 22.3 and 23.1 to correct a use-case error in the **Deployments** module pertaining to a **deployment bug** occurring with **multi packages** and **static resources**.

#### 1 October 2023

**(ARM v22.3.41)**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* A code fix was applied to the version control module in releases 22.3 and 23.1 due to a use-case error with a **user being unable to create a new commit**.&#x20;
* A code fix was performed for release versions 22.3 and 23.1 to the Deployments module for a use-case error resulting in a **buggy deployment** with **multi packages** and the **static resources** being bugged as well.&#x20;
* A code fix was applied to the version control module in releases 22.3 and 23.1 concerning a use-case error for an **EZ-Commit**, where the **user was unable to view the 'deleted components' tab** for the commit template when unchecking the '**skip mappings**' checkbox.&#x20;
* A code fix was implemented to versions 22.3 and 23.1 to correct an error with the Deployments module due to a **deployment** initiated using **Org Synchronization failing**.
* A code fix was applied to releases 22.3 and 23.1 due to a use-case error in which the **registration date** of the **repository** **was not correct** in the **version control repository** (**created date** in AutoRABIT).&#x20;
* A code fix was performed to versions 22.3 and 23.1 due to a data error in the version control module **preventing ALM working items from loading**.&#x20;
* A code fix was initiated to versions 22.3 and 23.1 due to a data error affecting the reports module, in which a user was getting an error message when executing a **static code analysis** (CodeScan) report.&#x20;
* A code fix was applied to version 22.3 in the version control module pertaining to a use-case error with **changes not** getting **fetched via autodraft after reverting a commit**.&#x20;
* A code fix was implemented in versions 22.3 and 23.1 to the version control module related to a use-case error wherein the **baseline job** has **modified the Salesforce folder structure in GitHub**.&#x20;
* A code fix was integrated to the version control module in version 22.3 after a data error caused by a **feature template migration** issue. The feature flag is **MERGE\_SKIP\_AUTORESOLVE\_CONFIGURATION\_FILES**.&#x20;
* A code fix to version 22.3 was implemented affecting all modules from a data error when **setting up SFDX deployment**.&#x20;
* A code fix was applied to the version control module in version 22.3 resulting from a use-case error with an **ARM commit comment label error**.&#x20;
* A code fix was implemented to the nCino module for versions 22.3 and 23.1 for a data error in which the **records count** was **not** being **updated** in the **object sidebar** for the version control baseline revision job.&#x20;

#### 24 September 2023

**(ARM v22.3.40)**\
This is a maintenance release. The following items were enhanced, fixed, or added:

* A code fix was implemented due to a use-case error to the Version Control module regarding an issue with merging destructive changes.&#x20;
* A code fix was applied to the Deployment module due to a data error concerning an Org difference pulling changes from the managed packages.&#x20;
* A code fix was applied due to a use-case error relating to the Deployments module with a user unable to deploy components via Org Sync.&#x20;
* A code fix was applied pertaining to the CI Jobs module relating to a use-case error in which the CI Job has two different package directories and changes fall under one package when an analysis is completed on CodeScan&#x20;
* Performed a code fix relating to a use-case error in on the Deployments module in which a deployment bug with multi packags and static resource was bugged.&#x20;

#### 17 September 2023

**(ARM v22.3.39)**\
This is a maintenance release. The following items were enhanced, fixed, or added.

* A code fix was implemented to the **Deployment** module related to a use-case error encountered when **deploying Vlocity components** from a **Git branch**.&#x20;
* A code fix was implemented related to the **CI Jobs** module to institute **best practices** following a user session.
* A code fix was implemented to the **Version Control** module related to a use-case error pertaining to **\[integration\_EZ-commit]**. User was getting a **"no package .xml found to retrieve the members"** through **package manifest** when selecting **'all users or the respective SF org user.'**&#x20;

#### 10 September 2023

**(ARM v22.3.38)**

This is a maintenance release. The following items were enhanced, fixed, or added:

1. As part of this fix deployment, one of the feature flags, '**RUN\_PACKAGE\_JOB\_ENTIRE\_BRANCH\_78757**,' has been provided. Enabling this feature flag only applies to one specific customer.&#x20;
2. Implemented a code fix associated with the **version control** module for a use-case error in which **ALM working items were not loading**.&#x20;
3. Implemented a code fix for a use-case error pertaining to the **version control** module for an **approval email notification error**.&#x20;
4. As a result of a use-case error relating to a **feature template migration** issue, a new **feature flag** has been provided, '**MERGE\_CONFLICTS\_AUTORESOLVE\_CONFIGFILES\_USINGSOURCE,'** which must be enabled for one specific customer only: More details are provided in the ticket itself.&#x20;
5. Implemented a code fix related to a use-case error where the **AutoRABIT deployment** **initiated using Org Synchronization fails**. This error pertains to the **Version Control** module.&#x20;
6.  Implemented a code fix related to the **CI Jobs** module related to setting up **SFDX deployment, with the Feature Flag:**&#x20;

    | **RUN\_PACKAGE\_JOB\_ENTIRE\_BRANCH\_78757** |
    | -------------------------------------------- |

    Regarding one ticket, '**Setting up SFDX Deployment'**: \
    Only for the '**Create and Install an Unlocked/Managed Package Version from a Version Control Branch'** CI, type in the CI Job configuration. When selecting the 'Trigger build on commit' option, we have hidden the '**Process commit revision received via hook only**' sub-option. This change will be incorporated into our documentation. Further details are available in the ticket itself.&#x20;
7.  Implemented a code fix related to the **nCino** module error: &#x20;

    | **LLC\_BI\_\_Schedule\_Section\_\_c migration issue#1** |
    | ------------------------------------------------------- |
8. Implemented a code fix related to an internal ticket in ARM, in which the user was **not able to migrate related data** using the **Dataloader test environment setup** module.&#x20;
9. Implemented a code fix related to the **Deployment** module for an **EBR Manual Asyncid XML Copy Automation** error.&#x20;

#### 3 September 2023

**(ARM v22.3.37)**

This is a maintenance release. The following items were enhanced, fixed, or added:

* Implemented a **code fix** associated with the **version control** module related to a use-case scenario in which a **review artifact was not working**.&#x20;
* Implemented a **code fix** to the **nCino** module resulting from a user product suggestion to the **deployment history filter**.&#x20;
* Implemented a **code fix** to the **nCino** module related to an instance in which the **org name** was **not displayed** for the **destination org value field**.&#x20;

#### 27 August 2023

**(ARM v22.3.36)**

This is a maintenance release. The following items were enhanced, fixed, or added:

* **Error: "Merging from Devint branch to Developer branch (Back merge) is getting Auto Rejected":** Code fix to Version Control module on user merging from **Devint branch to Developer branch (Back merge) getting Auto Rejected**.&#x20;
* Implemented a **UI change** to include the **“Ignore Warnings”** option in both the **prevalidation commit** and **merge flows**. This requires a documentation change. See ticket for more details.&#x20;
* **Error: “\[Client] getting frequent page unresponsive errors in ARM":** \
  Introduced a UI change to support Salesforce orgs and the **previous label deployment type** in the deployment module.&#x20;
* Performed a code fix affecting the Deployments module related to a use-case error with the client **getting frequent page unresponsive errors** in ARM. This also requires an update in our documentation. Further information is in the ticket.&#x20;
* **Error: “Branching baseline is not picking all components from production":** Based on the customer-confirmed downtime window, it was necessary to enable the "**METADATA\_API\_TO\_DX\_CONVERSION**" **feature flag** for this fix deployment.&#x20;
* Performed a code fix concerning the Admin module due to an error with a branching baseline not picking all components from production with feature flag error: **‘METADATA\_API\_TO\_DX\_CONVERSION’**.&#x20;
* Error in **CodeScan Plugin pop-up window** where the user was **unable to type text in Org key drop-down selection field**, which required a code fix to the Admin module. (Internal ticket)
* Performed a code fix related to a use-case error during **Vlocity deployments showing "NoOrgFoung" after activation** of **LWC components**. Fix applied to the CI Jobs and Deployment modules.&#x20;
* Code fix applied to SFDX module for the user receiving an error message showing **login failed**. Also related to CI Jobs, **scratch org creation was being struck in progress** and **not able to be deleted**.&#x20;
* Applied a code fix for the Version Control module related to a user being **unable to select the ALM side, getting a JAVA error**.&#x20;
* Initiated a code fix to the **Deployments** module related to an error during an **EZ deployment from a single revision with profiles and comp-specific changes pulling all comps**. &#x20;
* Executed a code fix to the Deployments module on a use-case error affecting an **AR deployment initiated using Org Synchronization failing**.&#x20;
* Applied a code fix related to the following use-case error: **\[Cijobs-DXModulePckagecreation] facing the "\["An unexpected error occurred while preparing endpoint: null. Please contact Salesforce Support and provide the following error code: 795089467-5806 (-1215335089)"]**.&#x20;
* Initiated a code fix to the **nCino** module for a client use-case error concerning **spread template issues**.&#x20;
* Performed a code fix for a customer use-case scenario regarding an error related to an **nCino CI job deployment issue**.&#x20;

#### 20 August 2023

**(ARM v22.3.35)**\
This is a maintenance release. The following items were fixed and/or added:

* Performed a code fix impacting the Deployments and CI Jobs modules related to use cases in which **selected test classes for production were not running** and users were having **code coverage issues**.&#x20;
* Performed a code fix for the Admin module related to a specific user having difficulty with **PWD policy**.&#x20;
* Performed a code fix to the CI Jobs and Deployment modules relating to users **unable to deploy changes to production orgs** due to a **CI Jobs coding issue**.&#x20;
* Performed a code fix to the CI Jobs module related to an **error message as login failed**.&#x20;
* Performed a code fix on the CI Jobs module pertaining to **Vlocity SFI components not compiling LWC on destination orgs when deploying via CI Jobs**.&#x20;
* Performed a code fix related to the CI Jobs module for **CI Job not starting according to schedule**.&#x20;
* Performed a code fix related to the CI Jobs module to resolve an error related to **setting up SFDX deployment and CI Job configuration**.&#x20;
* Performed a code fix to the **nCino** module for an error in which the **screen template failed** with a **malformed query exception**.&#x20;

#### 13 August 2023

**(ARM v22.3.34)**

This is a maintenance release. The following items were fixed and/or added:

* Performed a code fix pertaining to all modules relating to an **SFDX to SF CLI Hotfix**.&#x20;
* Performed a code fix relating to **version control, CI jobs, and deployment modules initiated via change request due to ALM working items not loading**, resolved by enabling the customer domain name.&#x20;
* Performed a code fix for a data error with **feature flag name, ‘Disable\_Merge\_Rename\_Detection’** after a merge was failing and took hours to complete.&#x20;
* Performed a code fix for the version control, CI jobs, and deployment modules pertaining to a data error, **validation failing for the LWC component despite no error message being displayed in the logs**.&#x20;
* Performed a code fix related to a use-case error in the version control module pertaining to a **commit showing a “no modification” error**.&#x20;
* Performed a code fix related to a use-case error affecting the version control, CI jobs, and deployment modules caused by an **error merging a commit from the dev environment to the INT environment**.&#x20;
* Performed a code fix to the version control module resulting from a use-case error where the **commit was incorrectly showing “no modification”**.&#x20;
* Performed a code fix related to a data error pertaining to the version control module, when **Jira integration stories redeploy post sandbox refresh**.&#x20;
* Performed a code fix for a use-case error in the deployment module related to **filter-based retrievals not working when applying the ‘created by,’ ‘modified by,’ ‘created date,’ and ‘modified date’ filters**.&#x20;
* Performed a code fix related to a performance issue in the nCino module pertaining to **Spread Template** issues.
* Fixed an error in the deployment module when ‘**Run Specified Tests**’ is selected from the Apex Test Level dropdown.&#x20;
* Rather than a code fix, a **customer-specific utility** was provided to address **SSO login issues** in the admin module. This particular utility only works in **versions 22.3.9** or lower for one individual customer.&#x20;

#### 06 August 2023

**(ARM v22.3.33)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an error under reports where **code coverage emails** were **missing information**.&#x20;
* Fixed an error related to a **second deployment** starting in the middle of a deployment.&#x20;
* Fixed an error in version control module related to **not being able to commit or Repush changes** in the **Training Branch**.&#x20;
* Fixed an error in version control module related to a feature flag: **USE\_PATCH\_LOGIC\_IN\_EZCOMMIT** for\
  **Code overwritten** (feature not enabled by default).
* Fixed an error for CI Job module where **ALM-enabled failed due to Unparsable date error**.&#x20;
* Fixed an error concerning **multiple CI Jobs failing due to data error**.&#x20;
* Fixed an error related to the Deployment, CI Jobs, and Version Control modules occurring when **merging a commit from dev environment to INT environment**.&#x20;
* Fixed an error related to deployments getting **frequent page unresponsive errors** in ARM.&#x20;
* Fixed an error under the Admin module relating to being **unable to select the revision number while creating the Tag**.&#x20;
* Fixed an error for **Create and Install Package** CI job deployment failing if having multiple package directories on the branch.&#x20;
* Fixed an error under the Admin module, **My Account >> Merge Settings: Not visible Border for "Notify All Criteria Overwrites To"** field.&#x20;
* Fixed an error under the Admin module, which enabled **Domain names to be visible in the inspect mode**.&#x20;
* Fixed an error in the nCino module related to **\[ARM-QAN] attachments’** deployment Failed with Bulk API.&#x20;
* Fixed an error in the nCino module related to a **Pricebook** entry.&#x20;
* Fixed an error related to the nCino module with **scheduled Job not showing up in UI** after completion due to **Deploy Status Not Updated**.&#x20;
* Fixed an error related to the nCino module with a **CI Job Edit not populating with scheduled time details**.&#x20;

#### 30 July 2023 <a href="#id-23-july-2023" id="id-23-july-2023"></a>

**(ARM v22.3.32)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **duplicate** not working on **EZ-merge** requests related to **version control**.&#x20;
* Fixed EZ deployments from a single revision with profiles **comp-specific changes pulling all comps** during deployments.&#x20;
* Fixed an error related to **CI Jobs** not running the pipeline.&#x20;
* Fixed situations with both **version control prevalidation commit and merge** where static code analysis processes are stuck in an **In-progress** state when VNC is not started.&#x20;
* Helped generate the reports for CI/CD pipelines for **nCino reports**.&#x20;
* Performed Jira integration story’s redeploy **post-sandbox refresh** in version control.&#x20;
* Fixed a specified metadata type is unsupported: **\[processflowmigration]** error in CI Jobs.&#x20;
* Set up the **SFDX Deployment** in CI Jobs.&#x20;
* Fixed an error with a **CI Job** not identifying changes.
* Fixed an error related to BHG with **CI Job webhooks** failing to trigger.&#x20;
* Performed **nCino AR template** updates.&#x20;

#### 23 July 2023 <a href="#id-23-july-2023" id="id-23-july-2023"></a>

**(ARM v22.3.31)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with a merge use case of handling **deleted files** in both source and target branches by using **git rm** command.
* Fixed an issue where screen redirects to login page on clicking on **User activation email**.
* Fixed an issue where **Commit stuck in InProgress**.
* Fixed an issue where we receive **“JAXB marshall/unmarshall exception”** while getting directed to CI results screen.
* Fixed an issue where **Release labels are taking 30 minutes** or more to be available for repository in Version control.
* Fixed an issue where **Merges are taking a long time** to complete in version control.
* Fixed an issue where components selected on review component pages were being repeated in the next category in **Version Control**.
* Fixed an issue where same name should be reflected instead of **Commit showing a different name in Bitbucket** in Version Control.
* Fixed an issue where **JIRA ALM Filter mappings not working** in My profile & Version Control.
* Fixed an issue where the **Login rate exceeded error** on the Salesforce Integration user.
* Fixed an issue where **Backup to Version Control** is not backing up **Matching Rules** in Salesforce in CI jobs.
* Fixed an issue where the shared server with common DB creates another customer weekly report in another server.
* Fixed an issue where **Custom field property** didn’t deploy in CI Jobs and Deployment.
* Fixed an issue where **Diff report** is not generated in New Deployment Module.
* Fixed an issue where **Unsupported metadata template** execution is failing in **Sandbox Refresh** in **Environment Provisioning** module.
* Enhanced **DataLoader uber jar upgrade to 58.0.3**.
* Fixed an issue where we are facing **Record Configuration** Time Out in nCino.
* Enhanced UI in **Post Deployment** activities result page in CI Job – nCino.
* Enhanced the **View details page** not being visible unless post-deployment activities are completed – nCino.

#### 18 June 2023 <a href="#id-18-june-2023" id="id-18-june-2023"></a>

**(ARM v22.3.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced ARM by allowing **PAT Authentication** for **Jira**.
* Fixed an issue where user ran an **Org Synchronization** history job and tried to access the **Diff** report to see the metadata difference, but the page kept loading indefinitely without the required diff.
* Upgraded **Provar** to **version 2.10.1**.
* Fixed an issue where the **Approval** option wasn't functional for **L1 Approvers**, and the **Org Admin** couldn't bypass the approval gate on EZ-Merge.
* Fixed an issue with **nCino** where user created a **Feature** deployment task, but the jobs were stuck the queue.
* Introduced a new feature in **DataLoader** called **Hard Delete** which can be used to delete the data completely and permanently instead of sending it to the **Recycle Bin** of the org.
* Fixed an issue where **CI Job build** history was not displaying the results and throwing a blank page instead.
* Fixed a UI bug where **Abort** option for CI job was displaying even after the build was successful.
* Fixed an issue where duplicate ALM Commit entries were Displaying while performing ALM Commit with Vlocity repository.
* Fixed an issue where the CI edit configuration screen was taking longer to load than expected before throwing `Page Unresponsive` alert.
* Fixed an issue with **DataLoader Pro** where user created a new job and applied filter, but the source and destination orgs are taken from history page.
* Fixed an issue with **DataLoader** where **Insert** operation bulk API selection was resulting in console error message `serializeToString`.
* Fixed an issue where **Vlocity** metadata components were getting expanded on the **Finish** page.

#### 11 June 2023 <a href="#id-11-june-2023" id="id-11-june-2023"></a>

**(ARM v22.3.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where deployment failed with the error message `File cannot be loaded`.
* Fixed an issue where the **SharingCriteriaRule** component was not deployed to Production even though the user had selected it ([#73824](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000114206402)).
* Fixed an issue where the **SharingReasons** component was ignored when the deployment/validation was done using **Commit Label** as source, but the same component was processed using **Single Revision** deployment or **CI Job** deployment ([#72073](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112029001)).
* Fixed an issue where user was trying to create an connect an **Active Directory** but it kept failing ([#73582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113941053)).
* Fixed an issue where user was migrating a field value with **Rich Text Area Field** type but it was not reflecting in the target org as expected. Hyperlinks, font size, etc., were not migrated as present in the source Salesforce org ([#73371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113607033) and [#56084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091215009)).
* Fixed a UI bug where **Deployment Failed** line was displayed twice in the logs for failed deployments (internal ticket).
* Fixed an issue where admin was unable to release a user from a team (internal ticket).
* Fixed an issue where **Null Values** were displayed on the **ALM Labels** screen as well as the **ALM Details** tab on the respective **ALM Commit Label Details** screen (internal ticket).
* Fixed an issue where selected files for DX Commits were not displayed in the **File Changes** tab, and after the commit it was showing as **No Modifications** (internal ticket).

#### 04 June 2023 <a href="#id-04-june-2023" id="id-04-june-2023"></a>

**(ARM v22.3.24)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where a **CI job** failed to pick the external commit revision which was added to an ALM Label as part of **Smart Commits** sync ([#71444](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111273077)).
* Fixed an issue where **Class Coverage Report** generated was empty for one of the Salesforce orgs, and it was intermittent.\
  The same behavior was observed for **RunSpecified** and **RunLocal** test levels ([#71367](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111185001)).
* Fixed an issue where deploying test classes from manual deployment was throwing an out of memory error ([#71872](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111679026)).
* Fixed an issue where **BackUp to Version Control CI Job** was failing due to too many retrieval error messages even though the **Bulk API** option was enabled ([#72181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112197081)).
* Fixed an issue where while performing any commit, **Pull Request** enabled **CI Job** was triggering as expected; but its **Build** and **Deployment** status was not added in the **Comments** in **Bitbucket** ([#72811](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112765004)).
* Fixed an issue where **EZ-Commits** were stuck with **In-progress** status for a few hours before failing. But the commit revisions were generated at the repository level and updated in ARM database ([#72817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112807012)).
* Fixed an issue where the **Git author** was overridden by ARM ([#71393](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111202442)).
* Fixed an issue with **DataLoader** where user was unable to create an **Update** job because the functionality prompoted user to select the **Required field** within the **Mapping Fields** ([#73515](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113850003)).
* Fixed an issue with DataLoader where user was getting a **script error** in the console while editing an existing old job (internal ticket).
* Fixed an issue where **Destructive** commit for DX was not working as expected for **Documents**, **Reports**, and **Dashboards** types (internal ticket).
* Fixed an issue where the **Layout** file was not displayed in the **Review Artifact** screen after resolving the layout **duplicates** (internal ticket).
* Fixed an issue where **4 CI jobs** were running parallelly even though the **parallel process limit** was **1** on the e**xternal agent** (internal ticket).

#### 28 May 2023 <a href="#id-28-may-2023" id="id-28-may-2023"></a>

**(ARM v22.3.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a compliance issue with **Apache Commons** by removing the text dependency ([#71947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111886005)).
* Fixed an issue where **CI Jobs** were failing due to empty **JSON** file(s) in the remote repository, and throwing the following error: `Failed to initiate deployment. Unexpected end of JSON input` ([#72217](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112229003)).
* Improved the UI by removing the **Validate Deployment** option if **Vlocity** is selected, and hiding the whole **Board Type** option if Vlocity is not enabled ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Fixed an issue where user was performing CI jobs for **Validate and Deploy** for a successful commit, but only validation was performed but not the deployment ([#72751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112682583)).
* Fixed an issue where CI job deployment was failing because the build was picking duplicate **Layout** values ([#71214](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110698400)).
* Fixed an issue where unwanted metadata changes were observed in the **package.xml** file while performing a commit ([#72089](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112054140) and [#71820](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111655842)).
* Fixed an issue where **Branching Baseline** was not picking all the components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Enhanced **DataLoader** by adding related objects and the fields of those objects displayed, so you can select the required fields of the related objects in the filter criteria and edit the query through SOQL editor ([#58549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095408144) and [#38339](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064118003)).
* Fixed an issue with **nCino** where CI jobs that used a **Deployment** from **Version Control** were failing when the build was triggered ([#71914](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111840343)).
* Improved the **New Merge** screen by adding **Layouts** text in the **Skip Flow /Profile/ Perm.Set Access-Setting Duplicity Check** option (internal ticket).
* Fixed a UI bug where **SF Org Test Connection** notification message was displayed on an unrelated module (internal ticket).
* Removed the option to sign up for a 30-day Salesforce trial while registering a DevHub as the trial offer is no longer applicable (internal ticket).

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

**(ARM v22.3.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where wrong **timezone** region was displaying for users ([#71553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111412006)).
* Fixed an issue where the **EZ-Commits report file** displayed the file count but not the components count ([#71538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111479094)).
* Fixed an issue where clone build jobs were taking between 10 and 25 minutes, which is much longer than expected ([#70227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109182447)).
* Fixed an issue where CI job build failed to show changes in the org after deployment ([#70791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110120443) and [#71956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111861212)).
* Fixed an issue where CI job to generate **Code Coverage Report** was not reflected in the org or in the e-mail notification ([#72042](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111983230)).
* Fixed an issue where merge status is displayed as completed but no revision is generated, and the merge is not available in the UAT branch ([#71266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110960210)).
* Enhanced **DataLoader** by adding the ability to **field mapping** through the lookup fields ([#58480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095290579)).
* Fixed an issue with **DataLoader** where while running an **Extract** job on the **PUBLISHER** object, the job was failing with the following error `Publisher: column id is not supported in ORDER BY clause` ([#71303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111030174)).
* Enhanced the **nCino filter criteria** by adding the ability to search and filter labels using the whole or partial name ([#71826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111666181)).
* Enhanced ARM by using known vulnerable components through the **DataTables 1.10.12** plugin for advanced data table functionalities such as sorting, filtering, pagination, and more. This allows users to easily display and manipulate large sets of data on their web pages in a user-friendly manner (internal ticket).
* Fixed an issue with **Prevalidation Merge** where users were unable to deploy the **ApexClass Tests** related to ApexClasses and Apex Triggers (internal ticket).
* Fixed a UI bug where the **date column** in the **EZ-Commit Weekly report** was displaying incorrect values (internal ticket).

#### 14 May 2023 <a href="#id-14-may-2023" id="id-14-may-2023"></a>

**(ARM v22.3.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was having trouble while deploying **LighteningMessageChannel** components ([#70787](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110191524)).
* Fixed an issue where **Destructive Changes** wasn't working as expected while performing an **Entire Branch** merge ([#68882](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107824070)).
* Enhanced the ALM management feature by adding an option to sync **Smart Commits** ([#58904](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095643142)).
* Fixed an issue with **CI Jobs** **Destructive Sharing Rule** was not deploying to the Salesforce org ([#71183](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110703254)).
* Fixed an issue where user could not disable the **Smart Commits-Sync** option for a repository branch in the **VC repos section** ([#70854](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110258586)).
* Improved the **New Merge** screen by removing the **Validate Deployment** option from the UI if **Vlocity** is selected ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Enhanced the **Credentials** module by adding **SSH Cetificate** option for **Git Authentication** ([#67725](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106632579)).
* Improved **Release label** creation by requiring at least **two revisions** to be selected (internal ticket).
* Fixed an issue where **Classic SF Org URL** with a slash at the end of the URL redirects to the `400` error page, and for a **Lightning SF Org URL** without a slash gives an `OAuth Authentication Failed` error message (internal ticket).
* Fixed an issue with **nCino** where user was getting a `NullPointerException` on **Saving Permissions** using **Bulk Assignment** (internal ticket).
* Fixed an issue with **CI Jobs** where all the scheduled timings were not displayed in the **Preview & Save** page (internal ticket).
* Fixed an issue with **Dataloader** where user was able to upload a 900 MB file despite the limit being 100 MB, causing the process to hang (internal ticket).
* Fixed an issue with **Dataloader** where sever crashed after user performed an **Extract** operation from an SF org which had **Account Object** with 2 million records (internal ticket).

#### 07 May 2023 <a href="#id-07-may-2023" id="id-07-may-2023"></a>

**(ARM v22.3.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was getting a validation deployment error while performing release label deployment ([#70400](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109643126)).
* Fixed an issue where **Branching Baseline** was taking longer than expected ([#67814](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777192)).
* Fixed an issue where using the **AutoDraft** functionality in **EZ-Commit** was resulting in a malformed exception in the UI ([#70458](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109706018)).
* Fixed an issue where **Branching baseline** was not picking all components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Fixed an issue where **prevalidation merge** failed with empty metadata package even though there were changes in **File Diff** ([#32256](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000049822310)).
* Fixed an issue where entire **ARM** application was down temporarily ([#70658](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110024189)).
* Fixed an issue where **Merge** was **auto-rejected** due to an empty package because the **metadata folder path** not being specified under branch settings ([#69788](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108851098)).
* Fixed an issue where user was using the **Bulk Assignment** feature to assign **Sandbox** permissions on the **Permissions** page but encountered the following error: `Java.lang.NullPointerException` ([#70868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110350003)).
* Fixed an issue where users weren't receiving **SCA reports** by email even though the reports were running ([#70751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110137323)).
* Fixed an issue where while performing new **EZ-Commit**, user edited one line using review artifact option but **Diff** did not capture the same ([#70270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109345141)).
* Fixed an issue where if **CI Jobs** were added in a queue with **Scheduled jobs**, then not all jobs were displayed in the queue (internal ticket).
* Fixed an issue where existing revision file related delta still existed in agent even after uploading to rabitserver (internal ticket).
* Fixed an issue where release label creation was failing when user tried to create package manifest and aborted and refreshed the label for DX repo (internal ticket).
* Fixed an issue where **Super admin user** was getting a blank popup screen while trying to click on the **Register Agent** button from the **Pool Mgmt** screen (internal ticket).

#### 30 April 2023 <a href="#id-30-april-2023" id="id-30-april-2023"></a>

**(ARM v22.3.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced the **Version Control** module by adding **SSH Certificate** for Git authentication while creating user credentials ([#67725](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106632579)).
* Fixed an issue where CI Job was picking changes one build but not for the other, and the logs weren't capturing this ([#69164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108123319)).
* Fixed an issue where **Ignore missing visibility settings** function was not working as expected and **Record type visibility** on the profile was not getting deployed using CI Job ([#67654](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106594374)).
* Fixed an issue where user merged a new component using a single revision merge but the merge missed to perform a CodeScan analysis ([#70391](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109502039)).
* Fixed an issue where user was unable to commit the destructive **Email Template** files as part of commit in SFDX format and getting auto failure ([#70351](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109465295)).
* Fixed a UI issue where **OK** button to reject an EZ-Merge was not working ([#70041](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108965683)).
* Fixed an issue where a field was available in the package but still Validation was throwing error that the field was missing ([#69831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108972528)).
* Fixed an issue with **DataLoader** where multiple jobs were not processing parallelly when user loaded a large number of jobs to the queue ([#62559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100372446)).
* Fixed an issue with **nCino** where user created more than 100 jobs with sub-user but was still getting the following error: `No jobs exist to load` ([#69831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108972528)).
* Fixed an issue where **Release Label artifact** was not displaying metadata types in the Destructive changes tab for DX repos, but was working as expected for non-DX repos (internal ticket).
* Fixed an issue where new jobs are getting added to the queue but not getting triggered, and later throwing `NullPointer Exception` (internal ticket).
* Fixed an issue where **Rollback** button was not enabled for the first job if that job is came from a queued list (internal ticket).
* Fixed an issue where **ALM CI Job** and **Release artifact** execution was happening at the same time, and the CI Job build was failing (internal ticket).
* Fixed an issue where an empty pop-up was displayed when user tried to edit the existing CI jobs label for **Sub-User** (internal ticket).
* Fixed an issue where if **Validate only** CI job came from the queue, then direct deployment was executing for that job instead of **validate deployment** (internal ticket).
* Fixed an issue where duplicates revisions were being added to the list while creating the release label when user unselected and reselected the same revisions. (internal ticket).
* Fixed an issue where **Vlocity** revisions were not displaying while user was trying to edit a release label (internal ticket).
* Enhanced the **Release Label** creation page by adding options to the **Vlocity** label type which were only available for Salesforce revisions before (internal ticket).

#### 23 April 2023 <a href="#id-23-april-2023" id="id-23-april-2023"></a>

**(ARM v22.3.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **SCA Report** failed to run using **Codescan** plugin with the below Salesforce error: `UNKNOWN_EXCEPTION: An unexpected error occurred`. ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Enhanced the **VC Repos** page by introducing a feature that allows users to **sync external smart commits** ([#58904](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095643142)).
* Updated the UI on the **External pull request** creation page to reflect the **Source** and **Target** fields clearly so users can trace which one is the source and destination branches ([#69772](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108841212)).
* Fixed an issue where duplicate entries were created in different lines during the Merge process and user wasn't able to remove the duplicate field without clearing the layout tag as well ([#68012](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107136001)).
* Fixed an issue where the baseline branch is not displayed during Static Code Analysis job creation if the branch name contains spaces in the Reports module ([#69614](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108583086)).
* Enhanced deployment in ARM by providing a new option **Rollback on error** in merge pre-validation. This checkbox allows users to choose if deployment should proceed with remaining components in case of errors ([#47794](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081201667)).
* Fixed an issue with nCino where CI job filter changes on templates were not taking effect after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue where user created a baseline revision job with the **Automation Sanity** repo and triggered the build but it failed without any error (internal ticket).
* Fixed an issue where user could not fetch the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** as an option (internal ticket).
* Fixed an issue where error `405` in the build and deployment logs didn't display further details in the UI log (internal ticket).
* Fixed a UI bug where dropdown selection in **Reports > CodeCoverage Reports** was not working after refreshing the page (internal ticket).
* Fixed an issue where **Release Label artifact** was not displaying metadata types in the Destructive changes tab for DX repos, but was working as expected for non-DX repos (internal ticket).
* Fixed an issue where user was unable to revert the commit if a previously reverted commit was deleted while in **Conflict** state (internal ticket).

#### 16 April 2023 <a href="#id-16-april-2023" id="id-16-april-2023"></a>

**(ARM v22.3.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced the **SCA report** options by removing the **10,000** limit for exporting issues using **CodeScan** ([#48644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082753293)).
* Enhanced **Vlocity CI jobs** by allowing **Local Compilation** for **Omniscript** and **Flexcard** objects ([#55641](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090230148) and [#50301](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084720103)).
* Fixed an issue where user was unable to use the **Redeploy/Promote** option after ten iterations of an existing **Deployment** label ([#69084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108041156)).
* Fixed an issue where user was trying to commit **System Permissions** which were enabled in Salesforce org, but while performing **EZ-Commit**, file **Diff** is not getting generated and the **system permissions** are not getting committed ([#67826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777838)).
* Fixed an issue where **ALM label** merge option was not working in **EZ-Merge** feature. This happened only when the **ALM Label** contained **`/`** in it ([#67818](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777588)).
* Fixed an issue where **EZ-Merge** was failing with `NullPointerException` ([#67502](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106282031)).
* Fixed a recurring issue of ARM overwriting the **Salesforce Org - Default Apex Test Class Configuration** by adding a checkbox **`Do you want us to update the test classes?`** ([#65565](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104611176)).
* Fixed an issue where **Revert** commits were failing without any error messages ([#68771](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107671065)).
* Fixed an issue where user created a **Release label** with multiple commit revisions, each with dependency components, but the revisions were not displaying in the right order in UI ([#68939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107912007)).
* Fixed a UI bug where when user unchecked **Validate deployment** option in **EZ-Merge**, the **Run destructive changes** checkbox was hidden ([#68750](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107699066)).
* Fixed an issue where when user had files in conflicted state, selecting the **ALL** checkbox was not working and user had to click on each file to resolve conflicts ([#65680](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104849001)).
* Fixed an issue where the **NPM repository Access Key** wasn't saving after clicking **Save**, causing the **Local Compilation** to fail (internal ticket).
* Fixed an issue where comments lines were not executed in **Metadata** when there were spaces in the comment line in merge flow (internal ticket).
* Fixed an issue where an empty popup screen is displayed while resolving conflicts in case of malformed file (internal ticket).
* Fixed an issue where improper validation message is displayed after clicking on **Resolve Duplicates** without selecting any files to resolve (internal ticket).
* Fixed an issue where SSO user's org was not deleted from the **Security-Context XML** (internal ticket).
* Fixed an issue where the **API Token** status was marked as **Never Accessed**, despite the API being in use already (internal ticket).

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

**(ARM v22.3.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **validation jobs** on **Pull Requests** weren't getting triggered ([#67538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106410313), [#67494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106382311), and [#67448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106353830)).
* Fixed an issue where Salesforce components were showing under the **Apex Test Success** tab in the **Deployment** module, which is not expected behavior ([#67537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253424)).
* Enhanced the **Branching Baseline** feature by allowing admin to define default baseline branches, making it easier for developers to choose the default branch for each project ([#63571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102024066)).
* Fixed an issue where user was unable to register a branch even though **Test Connection** was successful ([#67023](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105968682)).
* Fixed an issue where ARM wasn't fetching the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** option ([#67503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106378846)).
* Fixed an issue where **SCA Report** failed to run using **Codescan** plugin with the following Salesforce error: `An unexpected error occurred. Please include this ErrorId if you contact support: 384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Fixed an issue where triggered **CI jobs** were either failing due to an error **No Such File or Directory found**, or getting aborted automatically after some time and logs weren't printing at the back end ([#67549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253579), [#66910](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106035058), [#67724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106597223), [#67720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106570720), [#66881](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936162), and [#67667](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604150)).
* Fixed an issue where triggered **CI jobs** were taking too long to build, and also slowing down ARM altogether ([#66846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105989569)).
* Fixed an issue where if the file name contained spaces, **Commit Validation** via **VS Code** plugin was unable to detect the file ([#63518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101868754)).
* Fixed an issue where **Search & Substitute** was not updating the value for a **custom label** in the SF org ([#66809](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936001)).
* Fixed an issue where there was a discrepancy between the changes captured in the ARM **Diff** and the repos in **BitBucket** ([#60596](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097396243)).
* Fixed an issue where the SF org **URL** is not displaying the updated one under **Profile** ([#67718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106581101)).
* Fixed an issue with **nCino** where CI job filter changes on templates are not reflecting after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue with **Dataloader Pro** where user tried to migrate **Account Object Data** with **Attachments Object**, but the logs verify that there is a **Null Pointer Exception**. (internal ticket).
* Improved **nCino** by adding additional loggers for **Branching baseline** for user to view the status in the UI (internal ticket).
* Fixed an issue where user was unable to filter while trying to select a job which had spaces in the job name (internal ticket).

#### 02 April 2023 <a href="#id-02-april-2023" id="id-02-april-2023"></a>

**(ARM v22.3.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Custom Metadata** type access changes were not detected in version control **Diff**. There was no diff generated even there were changes in metadata access ([#59458](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096457374)).
* Fixed an issue where user performed a **CI job deployment** that had 8 destructive change items in the **merge PR**, but ARM is displaying only 2 destructive changes ([#66587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105697158)).
* Fixed an issue where **Git backup job** was failing due to unsupported metadata ([#66536](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105610003)).
* Fixed an issue where scheduled CI jobs were getting queued or not getting triggered as per schedule ([#57749](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093607144)).
* Fixed an issue where **Quick action** was not picked for destructive changes ([#65058](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104091725)).
* Fixed an issue where while running the scan from ARM for the version control branches are failing because **.java** files were present in the current repository ([#63234](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101513612)).
* Fixed an issue where user using **non-SFDX** repo with **Custom API** enabled failed to pick the changes in the CI job ([#64497](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103321171)).
* Fixed an issue where **Release label** displayed **commit revisions** older than 30 days even when the **No. of days** filter was set as **30** ([#63845](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102526769)).
* Fixed an issue where a user had trouble creating **artifact** for a **release label** ([#65557](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104667180)).
* Fixed an issue where there are **Vlocity** components in **Merge Validation**, and the validation deployment should bypass and process the merge; instead it is **Auto-rejecting** as criteria were not met ([#65625](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104812001)).
* Fixed an issue with **Dataloader** where a job completes with **No records** status whenever attachment and content version are selected as child objects in the parent cccount object ([#66655](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105749754)).
* Fixed an issue with **nCino** where CI job build status is displayed as **Completed** for a failed job ([#64479](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103318168)).
* Fixed an issue with **nCino** where attachements to `nFORMS__Form_Template__c` failed to get deployed ([#65242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104379896)).
* Fixed an issue where user was unable to initiate **static code analysis** on a Salesforce Org ([#51559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085951433)).
* Fixed an issue with **New EZ- Commit** where while using **Custom YAML** file the page was taking much longer to load than usual ([#65742](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104883025)).
* Fixed an issue where **Merge** was happening on incorrect files ([#64485](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103318553)).
* Fixed an issue where for DX repo, **Custom field** destructive **Deployment** was failing with the error `Package generation without a valid package directory cannot be processed` (internal ticket).
* Fixed an issue from the **VS Code** where **Static Code Analysis** report was not getting executed on the selected files and report generated (internal ticket).
* Fixed an issue where **Release Label** creation with **SVN Repo** was not successful, and throwing the following errors (internal ticket):
  * `Supplied AttributeValue is empty, must contain exactly one of the supported datatypes (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ValidationException; Request ID: a59c77cb-67ad-4a58-80b4-364feb5a4d6c; Proxy: null)`
  * `No Version Control Mappings found for Repo: {} and Branch: {}. Please update it in My Profile`
* Fixed an issue where **Merge** was not **Auto-rejected** after UI logs displayed `Mock deployment is failed, so auto rejecting the merge` (internal ticket).
* Fixed an issue where **Revision** in **Vlocity** release label was not getting selected after you clicked save (internal ticket).
* Fixed an issue with **nCino** where user was getting an exception while creating a CI job, and user was selecting the same **VC Repo**/**Branch** for multiple times (internal ticket).

#### 26 March 2023 <a href="#id-26-march-2023" id="id-26-march-2023"></a>

**(ARM v22.3.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Quick action** was not picked for destructive changes ([#65058](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104091725)).
* Fixed an issue where **CI job** deployment was failing due to the following error:\
  `Error: Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field (line 0, column 0)` ([#60914](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097801217) and [#65855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105051054)).
* Fixed an issue where **WebStoreTemplates** object was not available for deployment ([#65854](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104921177)).
* Fixed an issue where **Merge Request XML** file was conflicting with an error `No conflict data found for this block` ([#65164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104169938)).
* Fixed an issue where **Release label** failed while creating the artifact ([#64491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103297164)).
* Fixed an issue where **Prevalidation EZ-Commit** shows that **Diff** does not exist even when there are changes. If user tries multiple times, then Diff is displayed sometimes ([#64612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103417610)).
* Fixed an issue where user was unable to merge the code from one branch to another branch. ([#65570](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104676278)).
* Fixed an issue where **Ignore Missing Visibility** settings not working on **EZ-Merge** validation ([#65162](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104186080)).
* Fixed an issue where user was loading multiple **DataLoader** jobs but it was not processing parallelly ([#62559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100372446)).
* Fixed a UI bug in **nCino** where the header in **template details** section was missing in **Feature Deployment** (internal ticket).
* Fixed an issue with **nCino** where **Deployment Logs** were not displayed when the **CI Job** failed (internal ticket).

#### 19 March 2023 <a href="#id-19-march-2023" id="id-19-march-2023"></a>

**(ARM v22.3.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where CI job deployments were failing with the error, `Error 405 Only POST allowed` ([#64228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103003760)).
* Fixed an issue where multiple deployment requests were being generated while performing **Org Sync** if the user selected all components instead of a few ([#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where **Rollback API** threw a **200** response but the Rollback immediately failed in the ARM UI ([#65146](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104115380)).
* Fixed an issue where SCA report Failed to run using the **Codescan Plugin** with the following Salesforce error `384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151)).
* Fixed an issue where users were having trouble logging in to ARM due to an error `Session Invalid` ([#64965](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103959064), [#65052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104090509), and [#64969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104016027)).
* Fixed an issue where after upgrading to ARM version **22.3** user was unable to approve **EZ-Commits** that were pending approval in the **22.2** ([#64094](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102809037)).
* Fixed an issue where **Auto-draft** was taking much longer than expected to retrieve the metadata in **EZ-Commit** ([#65109](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104022403), [#65007](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104076001), [#64950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103943001), [#64510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103338015), [#64645](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103513158), [#64161](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102852098), and [#64523](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103361369)).
* Fixed an issue where user was trying to resolve a conflict in EZ-Merge but was getting a message on the UI that there are no conflicts ([#64185](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102875003)).
* Fixed an issue where **Branching Baseline** job does not delete files in **static resources sub directories** even though the user has selected the **Delete existing metadata and commit new changes** option ([#64150](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102831529)).
* Fixed an issue where user was unable to retrieve **MutingPermissionSet** using the **SFDX** repository ([#64141](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102573686)).
* Fixed an issue where the **Release Label** failed while creating the artifact ([#64491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103297164)).
* Fixed an issue where **Sharing Rule Set** metadata type was found in the **Deployment** module but not in the **Version Control** module ([#65060](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104102165)).
* Fixed an issue where the user performed a merge and approved both level 1 and level 2 reviews but was unable to approve the merge ([#65091](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104040481)).
* Fixed an issue where errors were occuring while performing **Delete Org** (internal ticket).
* Fixed an issue where for **Build only** job source from VC with DX repo, if **Master Details Object Change** is included in the build, we're getting **No Modifications** even if changes exist (internal ticket).

#### 12 March 2023 <a href="#id-12-march-2023" id="id-12-march-2023"></a>

**(ARM v22.3.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Static Code Anaysis** was failing due to missing property tag in **Apex PMD** rules file, but the UI log wasn't displaying this error ([#63554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101980029)).
* Fixed an issue where when there was no results generated, the report displayed an error that there are zero metrics instead of displaying the results as zero in all the places when there is no change ([#63272](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101591692)).
* Fixed an issue where user was unable to deploy a CI job with the **RelationshipGraphDefinition** components ([#64145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102836208)).
* Fixed an issue where **Validate** deployment was displayed as **failed** in UI and the database, but was successful as per the logs ([#63868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102596005)).
* Fixed an issue with **Review Artifact** where similar custom fields from different objects were not populating correctly and switching to other fields ([#63676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102181836)).
* Fixed an issue where multiple fields of the respective custom objects were getting selected parallelly while performing **edit** or **save** or **exit** operations on the **Review Artifact** screen (internal ticket).
* Enhanced ARM by adding an option for **multiple ARM instances** to share a **single database cluster** (internal ticket).

#### 05 March 2023 <a href="#id-05-march-2023" id="id-05-march-2023"></a>

**(ARM v22.3.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where ARM was displaying incorrect installation settings and package version information in the deployment log while installing the package version from a CI job ([#63544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101947159)).
* Fixed an issue where user chose **Exclude Metadata Type** for a particular metadata type during a **CI Job**, but it was still deployed ([#62966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101046005)).
* Fixed an issue where user was unable to perform **Destructive Commit** with **PermissionSetGroups** metadata type ([#63172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101463001)).
* Fixed an issue where users weren't receiving emails after setting up **Mail Settings** ([#55070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089394047)).
* Fixed an issue where there was a discrepancy between **EZ-Commit** and **Commit templates** while retrieving **Email Template** metadata members ([#61696](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099121314)).
* Fixed an issue where **Merge Labels** were taking much longer than expected ([#62625](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100474287)).
* Fixed an issue where user tried to commit the changes without validation and UI displayed an error `Another commit is in progress` ([#61930](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099562127)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed a UI bug where there was a discrepancy in the timestamp displayed for a commit in the **Commits History** page ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Fixed an issue where **Merge** was not auto-rejected when validation criteria was not met ([#62287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100008338)).
* Enhanced **nCino** by adding an option to specify **Baseline Revision** in **Continuous Integration** for **Version Control** to perform feature deployments ([#43642](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073759034) and [#44506](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074950579)).
* Enhanced **nCino** by allowing users to deploy nCino **CI build** to multiple target sandboxes ([#41763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070674305)).
* Fixed a UI bug where incorrect notification was displayed in certain components pages when template was created using one org and was used by another org (internal ticket).
* Fixed an issue where **Baseline Managed Package Changes** option was not displayed on the UI when navigating from **Package xml** to select manually (internal ticket).
* Fixed an issue where there was a discrepancy between the **Attachments Records Success/Failure Count** and the **Retrieved Count** when **BULK API** was enabled for **Deployment** (internal ticket).

#### 26 February 2023 <a href="#id-26-february-2023" id="id-26-february-2023"></a>

**(ARM v22.3.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a UI bug in **Profile Manager** where **User Permissions** differences are shown in the report but not in the UI ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Enhanced the **Release Label** creation by increasing the range of retrievable commit history ([#61714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099129934)).
* Fixed an issue where user was unable to use **Release Labels** to perform **Deployment**, and it failed while trying to **Create Artifact** ([#59429](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096450140)).
* Fixed an issue where users with non-admin access were unable to register branches in **EZ-Commit** since upgrading to version 22.3 ([#62723](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100650673), [#62949](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101016055), [#62979](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010456), and [#62969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010302)).
* Fixed an issue where **Release Artifact** execution was failing when **rabit home** did not exist with an external agent (internal ticket).
* Fixed a UI bug on the **Profile** screen where the expand option for the **My Projects** and **My Roles** sections was not working (internal ticket).
* Fixed an issue where triggering **Data Retention** for **Audit Tables** was throwing the following error: `Unable to execute HTTP request: Read timed out` (internal ticket).
* Fixed an issue where extra characters are seen in the **Fetch Commit History** results while creating a **Release Label** with **Vlocity** label type (internal ticket).
* Fixed an issue where user was unable to delete Apex test class on the SF Org Management page (internal ticket).
* Enhanced **nCino** by introducing **New Spreads Schedule** tile in the **Feature Creation** screen (internal ticket).
* Fixed an issue where if the fields did not load for **Applied Mappings** during deployment, no error was thrown by the application (internal ticket).

#### 19 February 2023 <a href="#id-19-february-2023" id="id-19-february-2023"></a>

**(ARM v22.3.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was deploying single revision deployment with only report folder but sub-reports were also getting fetched, and the deployment was failing due to field dependency error ([#61403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098537015)).
* Fixed an issue where after deployment with single revision merge, user permission appears to be removed in target org but in the Salesforce target org the user permission is not removed, and an incorrect layout is displayed in UI ([#60531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097360001)).
* Fixed an issue where user performed a pre-validation commit and each process like file diff, validate deploy happened thrice as per the logs ([#61079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097987087)).
* Fixed an issue where user was unable to select master branch as the parent branch while creating a new branch in **EZ-Commit** ([#56188](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091240174)).
* Fixed an issue where user was customer trying to register a **Salesforce Org** with **Custom URL** but it was failing with an error ([#62192](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099509581)).
* Fixed an issue where user was unable to remove **Revisions**/**Commit Labels** from a **Release label** ([#59152](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096005470) and [#61578](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098950203)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed an issue where user user uploaded a **YAML file** to retrieve the **Vlocity components** but ALL metadata types were retrieved and displayed ([#61181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248158)).
* Fixed an issue where the same merge could be approved and rejected by different users simultaneously ([#60859](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097787146)).
* Fixed an issue where branch creation was faileing for sub-users in the **EZ-Commit** screen for **Non-DX Repo** (internal ticket).
* Fixed an issue where **Null Pointer** was seen in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where all credentials were listed twice in the **Credentials** dropdown in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where **branch creation** was failing for sub-users in **VC repos** when the credential scope was private while Admin credentials were fetched (internal ticket).
* Fixed an issue where user was unable to delete the **Apex Test class** under the SF org Apex **default config** (internal ticket).
* Fixed an issue where the **Add manually** checkbox under Apex class config was selected by default (internal ticket).
* Fixed an issue with nCino where user created a feature Deployment for **Credit memo** template with attachments, but **Attachments Objects Data** was not fetched, and the deployment failed with the following error: `Data file not fetched for object: Attachment` (internal ticket).
* Fixed an issue with nCino where **Standard Features** were not loaded in the **Feature Management** page (internal ticket).

#### 12 February 2023 <a href="#id-12-february-2023" id="id-12-february-2023"></a>

**(ARM v22.3.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was unable to download success/failure reports in **Single Dataloader** ([#61551](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098913200)).
* Fixed an issue where when multiple **CI Jobs** are triggered, jobs are moved into the queue as expected, but new jobs are not starting automatically getting processed once the existing jobs is cleared from the **CI Job results** page ([#59082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096042290)).
* Fixed an issue where **Dependency** order defined in **json** file was being changed on every commit but it was not supposed to ([#57731](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556797)).
* Fixed an issue where **Create Artifact** was not working as expected while using **Release Label** ([#61607](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098932152)).
* Fixed an issue where user was performing an **EZ-Commit** with **Review Artifact** option and download the .zip file to make some changes, but was unable to upload it afterwards ([#61751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248378)).
* Fixed an issue where meta.xml file was not deleted from the repository after committing the destructive changes ([#61736](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099207347)).
* Fixed an issue where **File Diff** was empty in case of modified **Uploaded** via **Review Artifact** in **PV Commit Flow** (internal ticket).
* Fixed an issue where **Review Artifact Tree** was not responding after uploading the modified file in **Commit Flow** (internal ticket).
* Fixed an issue where **User Permissions** and **Ip Ranges** are completly removed from the branch after commiting the **Permission Sets** and **Profiles** (internal ticket).
* Fixed an issue where **Super Admin** was getting an error while trying to activate newly signed up users (internal ticket).

#### 05 February 2023 <a href="#id-05-february-2023" id="id-05-february-2023"></a>

**(ARM v22.3.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where SFDX module creation log shows that deployment is successful but the module creation had failed ([#57318](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092768029)).
* Fixed an issue with **Backup from Org CI Jobs** where **PermissionSet User Permissions** were being deleted ([#59674](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096685144)).
* Fixed an issue where **Org to Org Deployment** for **Profiles** including **Deploy Profile Access Settings for selected components only** was not working as expected ([#60559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097375154)).
* Fixed an issue where **Post Destruct** fields were also added to **Pre Destruct** despite the user setting it to post ([#61162](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248005)).
* Fixed an issue where user set the **Max depth** value as '0' under **Vlocity Configuration Settings** but it was retrieving all level dependancy components ([#57501](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093212471)).
* Fixed an issue with DataLoader where the **Credit Memo Template** migration was not deploying after user upgraded their instance ([#57676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093470003)).
* Fixed an issue where user selected **Custom Metadata** members (records), but **EZ-Commit** was failing to generate **File Diff** with `Null` error ([#59709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096706005)).
* Fixed an issue where **Merge** was taking longer than usual, and then failing with `Null Exception` ([#60757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097574427)).
* Fixed an issue where **EZ-Commits** and **EZ-Merges** were taking much longer than usual ([#58098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094302292)).

#### 29 January 2023 <a href="#id-29-january-2023" id="id-29-january-2023"></a>

**(ARM v22.3.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment was failing with the following error when user was deploying **Permissionset** with a user-permission **Manage Public Documents**: `Permission Manage Public Documents depends on permission(s): Create Document, Delete Document, Edit Document, Read Document` ([#60597](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097399881)).
* Fixed an issue where CI jobs were failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#59050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095999076)).
* Fixed an issue where **Reports** deployment validation failed in **EZ-Merge** but was successful in **EZ-Commit** and **Deployment** modules ([#57714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093587003)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Fixed an issue where user initiated the prevalidation commit by enabling the destructive type but the deployment failed with an error `null` at **Diff** ([#59919](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096907001)).
* Fixed an issue where **Validate Deploy** failed in **QuickMerge** and displayed the following message: `This folder unique name already exists for this folder type or has been previously used. Please choose a different name` (internal ticket).
* Fixed an issue where CI job wasn't considering the metadata changes, so the destructive changes were not being prepared or displayed on the build. (internal ticket).

#### 22 January 2022 <a href="#id-22-january-2022" id="id-22-january-2022"></a>

**(ARM v22.3.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user changed the permissions to **list view** from **visible to all users** to **visible only for me** while using the previous commit label, it is added under the **Deleted** tab ([#59359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096219627)).
* Fixed an issue where commit was running for longer and remained **in-progress** and **validation check log** is also in progress ([#59199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096003630)).
* Fixed an issue where commits with SFDX metadata structure are **failing** in metadata **retrieval stage** ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed an issue where user couldn't create a managed package with the selected ancestor ([#59044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095985421)).
* Fixed an issue where **CI Job** was occasionally failing with the error `BUILD FAILED` ([#57647](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093370172)).
* Fixed an issue where CI job was taking the last modified user name if trigger through API instated of taking API token user ([#55438](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089958034)).
* Salesforce **API version 57** (Beta support) is upgraded. The label is modified throughout ARM application including DataLoader and nCino (internal ticket).
* Fixed an issue where nCino CI job was stuck in **Build Success** status for more than a week ([#59040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095982206)).
* Fixed an issue where user was trying to deploy RBC (nCino Screens) and the deployment was failing for some of the objects, but there were no error messages shown on the UI ([#58044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094164003)).
* Fixed an issue where user was using SSH credential in AutoRABIT but it was throwing the following error: `Invalid Private Key` ([#59244](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096134293)).
* Fixed an issue where user has created a Commit label but it was not available while trying to perform an **EZ-Merge** ([#55176](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089550097)).
* Fixed an issue where user was not getting file Diff to commit the previously validated commit label and getting an error in the Diff ([#59114](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096048883)).
* Fixed an issue where user was getting an error while trying to create a new branch in GitHub ([#59193](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096138920)). For more information, click [here](https://knowledgebase.autorabit.com/docs/faqs-version-control?highlight=$%20ssh-keygen%20-t%20rsa%20-b%204096%20-C#why-am-i-getting-an-error-while-trying-to-register-github-repository-with-ssh).
* Fixed an issue where user could not create an **xml package** for deployment because artifact creation and package manifest preparation were failing with an `invalid credentials` error ([#59402](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096425001)).
* Fixed an issue where user was trying to perform single revision merge but validation deployment was failing with the following error `Metadata package is empty` ([#59028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095867179)).
* Fixed an issue where when there are special characters in **Layout metadata** then the user was not able to add it manually in **Skip Members** section ([#58998](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095876003)).
* Fixed an issue where user wanted to choose commit revision in a release label based on its comment but if the comment was not in text, it was not completely visible in the UI ([#59014](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095898340)).
* Fixed a UI bug where an incorrect validation message was seen while adding **Skip Members** manually (internal ticket).
* Fixed an issue where the selected tab checkbox in the **metadata components** page in the EZ-Commit was not functioning as expected (internal ticket).
* Fixed an issue where the **EZ-Commit** validation screen was displaying incorrect notification when name of the template was empty (internal ticket).

#### 15 January 2022 <a href="#id-15-january-2022" id="id-15-january-2022"></a>

**(ARM v22.3.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556)).
* Fixed an issue with user received 6 notifications for a failed **CI Job** instead of 1 ([#58436](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095199003)).
* Fixed an issue where user was trying to register branches to AutoRABIT through GitHub, but was getting the following error: `Lower Region` ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed a recurring issue where **Commits** and **Merges** were slowing down at a particular step, and **EZ-Merge** was failing with an error at commit phase ([#51268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085726862)).
* Fixed an issue where while performing destructive changes in **EZ-Commit**, it was creating **package.xml** in root path folder in **SFDX** structure ([#57868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093790001)).
* Fixed a UI bug on **CI List** and **CI Results** pages where when pagination was changed, the first 25 records were repeated (internal ticket).
* Fixed an UI bug where the **LastUsedDate** column was not displayed in the **Branch Table** (internal ticket).

#### 8 January 2022 <a href="#id-8-january-2022" id="id-8-january-2022"></a>

**(ARM v22.3.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189)).
* Fixed a build bug where **CI Job Build** was failing during package preparation **step 5** failing while commiting **DecisionMatrixDefinition** and throwing an error ([#58376](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095049142)).
* Fixed an issue with **Branching Baseline** where the developers were migrating the changes from dev branch to INT, but **Diff** was showing 100% addition which is incorrect\
  ([#58478](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095251543)).
* Fixed an issue where generating **Diff** for a **Commit Label** was taking much longer than expected ([#55220](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591780)).
* Fixed an issue where **Code coverage** job was running **4 hours** earlier than scheduled every time services were restarted ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed an issue where **SFDX scratch org** was failing during data deployment but without any errors on UI, and the logs did not capture the failure either ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58244](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094983001), [#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556), and [#58438](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095210005)).
* Fixed an issue where **CheckMarx** is executed successfully, but when trying to open the file user is the following error popup: `Result file not exists` (internal ticket).
* Fixed an issue where **ActionCall** and **Decision Nodes** were not shown in the **Duplicate Resolving** screen (internal ticket).

#### 1 January 2022 <a href="#id-1-january-2022" id="id-1-january-2022"></a>

**(ARM v22.3.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was unable to create **Environment Provisioning** templates for multiple component types ([#57898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093797903)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).
* Fixed an issue where AutoRABIT **SSH credentials** were failing with an error `Auth failed` while trying to connect with **AWS CodeCommit** ([#53694](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087714369)).
* Fixed an issue where **EZ-Commit Diff** was taking approximately 4 hours while **Refactoring CustomField**, which is much longer than expected ([#56650](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091636348)).
* Fixed an issue where **ExternalCredential** metadata type was not getting excluded even when user added it in the **excluded lists** in **CI Configuration** (internal ticket).
* Fixed an issue where after triggering **Branching baseline**, standard value set metadata type was getting displayed under the **deleted components** through **Autodraft** for **Non-DX repo** (internal ticket).
* Fixed an issue where **Destructive Components** are not seen in case of **PV-DX-Destructive Merge** for **Report** metadata type. Instead, it displaying a message: `Package is empty` (internal ticket).
* Fixed an issue where **Deployment** was failing with certain **Permission set metadatatypes** that were not selected (internal ticket).

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

**(ARM v22.3.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where non-admin users were unable to select **Branch Type** while trying to create a **new branch** from **New EZ-Commit Branch** ([#57732](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556923)).
* Fixed an issue where **CI jobs** are failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#57371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880162)).
* Fixed an issue where user was trying to deploy only the **Documents** from the branch to Org, but deployment failed and **Asynch ID** is not generating ([#57263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092661381)).
* Fixed an issue where user was trying to deploy **login hours**. First they merged it to target branch, then once CI job triggers login hours are not getting deployed to target org ([#57359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880015)).
* Fixed multiple issues where user was having trouble creating **new package version** from **previous ancestor** version ([#55707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090251366)).
* Fixed an issue where **Merge** is **failing** with the following error: `failed to push some refs to 'https://github.com/salesforce-align/SFDX.git'` ([#55939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090999346)).
* Fixed an issue where the **Standard Field Account.name** is displayed in the deleted components list ([#57396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092927781)).
* Fixed an issue where the **prevalidation commit** failed at **delta** stage ([#55763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090435979)).
* Fixed an issue where user was unable to create **commit label** for the same repository second time, and branches were not displayed (internal ticket).

#### 18 December 2022 <a href="#id-18-december-2022" id="id-18-december-2022"></a>

**(ARM v22.3.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DataLoader Pro** where jobs executed in the last 6 months were not showing in the database process table and in the **Reports** module ([#53980](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087981132)).
* Fixed an issue with **Deploy SFDX Source With ALM Mapping** where CI job with ALM Mapping was not working as expected for Team which is not default ([#55995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091129007)).
* Fixed an issue where **Profile Diff** is working as expected for **Selective Deployment**, but not while using the same profile in the profile manager ([#52868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087005140)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189), [#55754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090487029)).
* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).

***

## **ARM Release Notes 22.2**

**Date of release:** _9 October 2022_\
**Article last updated:** _15 May 2023_

### New Features <a href="#new-features" id="new-features"></a>

#### 1. Teams/Slack Notifications <a href="#id-1-teamsslack-notifications" id="id-1-teamsslack-notifications"></a>

**Mail Settings** module in the **Admin** section is relabeled as **Notifications**. Through this module, you can choose to send notifications about specific events triggered in ARM to specific groups or channels within your organization through **Teams** or **Slack**. For whichever messaging app you use, you can configure a webhook connection for each of the groups or channels, and then integrate them with ARM. You can customize and select which group(s) to notify when events like build failure, build success, deployment failure, merge reports, etc. are triggered.

[**Read more →**](../../../product-guides/arm/troubleshoot/how-tos/notifications-mail-server-settings.md)

#### 2. Salesforce Scanner plugin <a href="#id-2-salesforce-scanner-plugin" id="id-2-salesforce-scanner-plugin"></a>

In addition to the existing static code analysis tools, ARM now provides the ability to choose the **Salesforce Scanner CLI** plugin.

Most static code analysis tools specialize in one language or a set of languages. Many applications (including typical Salesforce packages), however, contain an assortment of components created using different languages. A single static analyzer is insufficient to address all aspects of such applications, and managing multiple static analyzer tools could prove unfeasible.

This is where the **Salesforce CLI Scanner** plugin shines. This plugin aggregates the results of static analyzers that are most relevant to Salesforce developers while providing a unified experience.

With the Salesforce CLI Scanner plugin, you can look forward to a:

* Single installation process
* A single set of commands to interact with multiple rule engines
* A unified set of rules that are checked by their respective rule engines
* Unified rule violation report that includes all issues identified by the engines.

#### 3. AutoRABIT for nCino <a href="#id-3-autorabit-for-ncino" id="id-3-autorabit-for-ncino"></a>

We’ve added the ability to view and review datasets corresponding to each version of the nCino feature template before using it for deployment. Prior to this release, the capability was available only for the latest version of the template.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. ApexPMD Upgrade to 6.49 version <a href="#id-1-apexpmd-upgrade-to-649-version" id="id-1-apexpmd-upgrade-to-649-version"></a>

With this release, PMD has been upgraded to version **6.49**. If you have not uploaded a rules file, ARM will use the default Apex PMD rules file. However, you can add new rules to the default ruleset.

Click [HERE](https://pmd.github.io/latest/pmd_next_major_development.html#list-of-currently-deprecated-rules) to view the list of currently deprecated rules available on GitHub.

#### 2. Auto-approve on validation success <a href="#id-2-autoapprove-on-validation-success" id="id-2-autoapprove-on-validation-success"></a>

We have moved one step closer to automating the flow by adding an option to choose if an **EZ-Commit** or an **EZ-Merge** should be approved automatically if the SCA validation is successful. Combined with the existing option to auto-commit on approval, this leads to a true CI/CD experience.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings.md)

#### 3. HashiCorp Vault Integration <a href="#id-3-hashicorp-vault-integration" id="id-3-hashicorp-vault-integration"></a>

While adding HashiCorp credentials to ARM, you can now choose the **AWS Authentication** method so that the Vault Token will be generated automatically whenever the existing token expires. Now the user will not have to update the token manually from the application when it expires.

[**Read more →**](./#3-hashicorp-vault-integration)

#### 4. SFDX CLI Upgrade <a href="#id-4-sfdx-cli-upgrade" id="id-4-sfdx-cli-upgrade"></a>

The SFDX CLI has been upgraded to the latest stable **7.169** version.

Key characteristics to look for:

* Support for the **quick deploy** functionality for SFDX jobs.
* Use CLI commands to generate the package manifest and rollbacks.

#### 5. Salesforce Winter (API 56.0) Support <a href="#id-5-salesforce-winter-api-560-support" id="id-5-salesforce-winter-api-560-support"></a>

To keep our product up to date with the most recent Salesforce updates, AutoRABIT supports the most recent **API 56.0** version in this release. The most recent API version is intended for customizing the metadata model and developing tools to manage it.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/salesforce-api-version.md)

#### 6. Merge to multiple branches <a href="#id-6-merge-to-multiple-branches" id="id-6-merge-to-multiple-branches"></a>

With this release, you can choose to **merge** from one **source branch** to multiple **destination branches** upon successful deployment.

[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/create-a-new-ci-job/deploy-from-sfdx-branch-to-a-salesforce-org.md)

#### 7. OAuth for Jira <a href="#id-7-oauth-for-jira" id="id-7-oauth-for-jira"></a>

In addition to the **Standard** access type, users can now set up **SSO** as authentication for **Jira** using the OAuth access type while registering an ALM. You can also switch between **Standard** and **OAuth** access types for already registered ALMs.

[**Read more →**](../../../product-guides/arm/arm-administration/alm-management.md)

### Improvements <a href="#improvements" id="improvements"></a>

* Users with Admin access can now turn off the Jira comments and notifications created by AR. This ensures a cleaner workspace. These comments and notifications are very development centric, so the end users who use Jira cannot make sense of our technical comments from AR, and this may create confusion for them.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 28 May 2023 <a href="#id-28-may-2023" id="id-28-may-2023"></a>

**(ARM v22.2.28)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a compliance issue with **Apache Commons** by removing the text dependency ([#71947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111886005)).
* Fixed an issue where **CI Jobs** were failing due to empty **JSON** file(s) in the remote repository, and throwing the following error: `Failed to initiate deployment. Unexpected end of JSON input` ([#72217](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112229003)).
* Improved the UI by removing the **Validate Deployment** option if **Vlocity** is selected, and hiding the whole **Board Type** option if Vlocity is not enabled ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Fixed an issue where user was performing CI jobs for **Validate and Deploy** for a successful commit, but only validation was performed but not the deployment ([#72751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112682583)).
* Fixed an issue where CI job deployment was failing because the build was picking duplicate **Layout** values ([#71214](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110698400)).
* Fixed an issue where unwanted metadata changes were observed in the **package.xml** file while performing a commit ([#72089](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112054140) and [#71820](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111655842)).
* Fixed an issue where **Branching Baseline** was not picking all the components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Enhanced **DataLoader** by adding related objects and the fields of those objects displayed, so you can select the required fields of the related objects in the filter criteria and edit the query through SOQL editor ([#58549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095408144) and [#38339](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064118003)).
* Fixed an issue with **nCino** where CI jobs that used a **Deployment** from **Version Control** were failing when the build was triggered ([#71914](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111840343)).
* Improved the **New Merge** screen by adding **Layouts** text in the **Skip Flow /Profile/ Perm.Set Access-Setting Duplicity Check** option (internal ticket).
* Fixed a UI bug where **SF Org Test Connection** notification message was displayed on an unrelated module (internal ticket).
* Removed the option to sign up for a 30-day Salesforce trial while registering a DevHub as the trial offer is no longer applicable (internal ticket).

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

**(ARM v22.2.27)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where wrong **timezone** region was displaying for users ([#71553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111412006)).
* Fixed an issue where the **EZ-Commits report file** displayed the file count but not the components count ([#71538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111479094)).
* Fixed an issue where clone build jobs were taking between 10 and 25 minutes, which is much longer than expected ([#70227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109182447)).
* Fixed an issue where CI job build failed to show changes in the org after deployment ([#70791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110120443) and [#71956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111861212)).
* Fixed an issue where CI job to generate **Code Coverage Report** was not reflected in the org or in the e-mail notification ([#72042](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111983230)).
* Fixed an issue where merge status is displayed as completed but no revision is generated, and the merge is not available in the UAT branch ([#71266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110960210)).
* Enhanced **DataLoader** by adding the ability to **field mapping** through the lookup fields ([#58480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095290579)).
* Fixed an issue with **DataLoader** where while running an **Extract** job on the **PUBLISHER** object, the job was failing with the following error `Publisher: column id is not supported in ORDER BY clause` ([#71303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111030174)).
* Enhanced the **nCino filter criteria** by adding the ability to search and filter labels using the whole or partial name ([#71826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111666181)).
* Enhanced ARM by using known vulnerable components through the **DataTables 1.10.12** plugin for advanced data table functionalities such as sorting, filtering, pagination, and more. This allows users to easily display and manipulate large sets of data on their web pages in a user-friendly manner (internal ticket).
* Fixed an issue with **Prevalidation Merge** where users were unable to deploy the **ApexClass Tests** related to ApexClasses and Apex Triggers (internal ticket).
* Fixed a UI bug where the **date column** in the **EZ-Commit Weekly report** was displaying incorrect values (internal ticket).

#### 14 May 2023 <a href="#id-14-may-2023" id="id-14-may-2023"></a>

**(ARM v22.2.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was having trouble while deploying **LighteningMessageChannel** components ([#70787](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110191524)).
* Fixed an issue where **Destructive Changes** wasn't working as expected while performing an **Entire Branch** merge ([#68882](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107824070)).
* Enhanced the ALM management feature by adding an option to sync **Smart Commits** ([#58904](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095643142)).
* Fixed an issue with **CI Jobs** **Destructive Sharing Rule** was not deploying to the Salesforce org ([#71183](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110703254)).
* Fixed an issue where user could not disable the **Smart Commits-Sync** option for a repository branch in the **VC repos section** ([#70854](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110258586)).
* Improved the **New Merge** screen by removing the **Validate Deployment** option from the UI if **Vlocity** is selected ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Enhanced the **Credentials** module by adding **SSH Cetificate** option for **Git Authentication** ([#67725](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106632579)).
* Improved **Release label** creation by requiring at least **two revisions** to be selected (internal ticket).
* Fixed an issue where **Classic SF Org URL** with a slash at the end of the URL redirects to the `400` error page, and for a **Lightning SF Org URL** without a slash gives an `OAuth Authentication Failed` error message (internal ticket).
* Fixed an issue with **nCino** where user was getting a `NullPointerException` on **Saving Permissions** using **Bulk Assignment** (internal ticket).
* Fixed an issue with **CI Jobs** where all the scheduled timings were not displayed in the **Preview & Save** page (internal ticket).
* Fixed an issue with **Dataloader** where user was able to upload a 900 MB file despite the limit being 100 MB, causing the process to hang (internal ticket).
* Fixed an issue with **Dataloader** where sever crashed after user performed an **Extract** operation from an SF org which had **Account Object** with 2 million records (internal ticket).

#### 07 May 2023 <a href="#id-07-may-2023" id="id-07-may-2023"></a>

**(ARM v22.2.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was getting a validation deployment error while performing release label deployment ([#70400](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109643126)).
* Fixed an issue where **Branching Baseline** was taking longer than expected ([#67814](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777192)).
* Fixed an issue where using the **AutoDraft** functionality in **EZ-Commit** was resulting in a malformed exception in the UI ([#70458](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109706018)).
* Fixed an issue where **Branching baseline** was not picking all components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Fixed an issue where **prevalidation merge** failed with empty metadata package even though there were changes in **File Diff** ([#32256](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000049822310)).
* Fixed an issue where entire **ARM** application was down temporarily ([#70658](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110024189)).
* Fixed an issue where **Merge** was **auto-rejected** due to an empty package because the **metadata folder path** not being specified under branch settings ([#69788](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108851098)).
* Fixed an issue where user was using the **Bulk Assignment** feature to assign **Sandbox** permissions on the **Permissions** page but encountered the following error: `Java.lang.NullPointerException` ([#70868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110350003)).
* Fixed an issue where users weren't receiving **SCA reports** by email even though the reports were running ([#70751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110137323)).
* Fixed an issue where while performing new **EZ-Commit**, user edited one line using review artifact option but **Diff** did not capture the same ([#70270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109345141)).
* Fixed an issue where if **CI Jobs** were added in a queue with **Scheduled jobs**, then not all jobs were displayed in the queue (internal ticket).
* Fixed an issue where existing revision file related delta still existed in agent even after uploading to rabitserver (internal ticket).
* Fixed an issue where release label creation was failing when user tried to create package manifest and aborted and refreshed the label for DX repo (internal ticket).
* Fixed an issue where **Super admin user** was getting a blank popup screen while trying to click on the **Register Agent** button from the **Pool Mgmt** screen (internal ticket).

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

**(ARM v22.2.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **validation jobs** on **Pull Requests** weren't getting triggered ([#67538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106410313), [#67494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106382311), and [#67448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106353830)).
* Fixed an issue where Salesforce components were showing under the **Apex Test Success** tab in the **Deployment** module, which is not expected behavior ([#67537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253424)).
* Enhanced the **Branching Baseline** feature by allowing admin to define default baseline branches, making it easier for developers to choose the default branch for each project ([#63571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102024066)).
* Fixed an issue where user was unable to register a branch even though **Test Connection** was successful ([#67023](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105968682)).
* Fixed an issue where ARM wasn't fetching the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** option ([#67503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106378846)).
* Fixed an issue where **SCA Report** failed to run using **Codescan** plugin with the following Salesforce error: `An unexpected error occurred. Please include this ErrorId if you contact support: 384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Fixed an issue where triggered **CI jobs** were either failing due to an error **No Such File or Directory found**, or getting aborted automatically after some time and logs weren't printing at the back end ([#67549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253579), [#66910](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106035058), [#67724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106597223), [#67720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106570720), [#66881](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936162), and [#67667](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604150)).
* Fixed an issue where triggered **CI jobs** were taking too long to build, and also slowing down ARM altogether ([#66846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105989569)).
* Fixed an issue where if the file name contained spaces, **Commit Validation** via **VS Code** plugin was unable to detect the file ([#63518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101868754)).
* Fixed an issue where **Search & Substitute** was not updating the value for a **custom label** in the SF org ([#66809](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936001)).
* Fixed an issue where there was a discrepancy between the changes captured in the ARM **Diff** and the repos in **BitBucket** ([#60596](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097396243)).
* Fixed an issue where the SF org **URL** is not displaying the updated one under **Profile** ([#67718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106581101)).
* Fixed an issue with **nCino** where CI job filter changes on templates are not reflecting after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue with **Dataloader Pro** where user tried to migrate **Account Object Data** with **Attachments Object**, but the logs verify that there is a **Null Pointer Exception**. (internal ticket).
* Improved **nCino** by adding additional loggers for **Branching baseline** for user to view the status in the UI (internal ticket).
* Fixed an issue where user was unable to filter while trying to select a job which had spaces in the job name (internal ticket).

#### 19 March 2023 <a href="#id-19-march-2023" id="id-19-march-2023"></a>

**(ARM v22.2.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where CI job deployments were failing with the error, `Error 405 Only POST allowed` ([#64228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103003760)).
* Fixed an issue where multiple deployment requests were being generated while performing **Org Sync** if the user selected all components instead of a few ([#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where **Rollback API** threw a **200** response but the Rollback immediately failed in the ARM UI ([#65146](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104115380)).
* Fixed an issue where SCA report Failed to run using the **Codescan Plugin** with the following Salesforce error `384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151)).
* Fixed an issue where users were having trouble logging in to ARM due to an error `Session Invalid` ([#64965](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103959064), [#65052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104090509), and [#64969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104016027)).
* Fixed an issue where after upgrading to ARM version **22.3** user was unable to approve **EZ-Commits** that were pending approval in the **22.2** ([#64094](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102809037)).
* Fixed an issue where **Auto-draft** was taking much longer than expected to retrieve the metadata in **EZ-Commit** ([#65109](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104022403), [#65007](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104076001), [#64950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103943001), [#64510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103338015), [#64645](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103513158), [#64161](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102852098), and [#64523](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103361369)).
* Fixed an issue where user was trying to resolve a conflict in EZ-Merge but was getting a message on the UI that there are no conflicts ([#64185](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102875003)).
* Fixed an issue where **Branching Baseline** job does not delete files in **static resources sub directories** even though the user has selected the **Delete existing metadata and commit new changes** option ([#64150](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102831529)).
* Fixed an issue where user was unable to retrieve **MutingPermissionSet** using the **SFDX** repository ([#64141](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102573686)).
* Fixed an issue where the **Release Label** failed while creating the artifact ([#64491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103297164)).
* Fixed an issue where **Sharing Rule Set** metadata type was found in the **Deployment** module but not in the **Version Control** module ([#65060](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104102165)).
* Fixed an issue where the user performed a merge and approved both level 1 and level 2 reviews but was unable to approve the merge ([#65091](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104040481)).
* Fixed an issue where errors were occuring while performing **Delete Org** (internal ticket).
* Fixed an issue where for **Build only** job source from VC with DX repo, if **Master Details Object Change** is included in the build, we're getting **No Modifications** even if changes exist (internal ticket).

#### 12 March 2023 <a href="#id-12-march-2023" id="id-12-march-2023"></a>

**(ARM v22.2.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Static Code Anaysis** was failing due to missing property tag in **Apex PMD** rules file, but the UI log wasn't displaying this error ([#63554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101980029)).
* Fixed an issue where when there was no results generated, the report displayed an error that there are zero metrics instead of displaying the results as zero in all the places when there is no change ([#63272](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101591692)).
* Fixed an issue where user was unable to deploy a CI job with the **RelationshipGraphDefinition** components ([#64145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102836208)).
* Fixed an issue where **Validate** deployment was displayed as **failed** in UI and the database, but was successful as per the logs ([#63868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102596005)).
* Fixed an issue with **Review Artifact** where similar custom fields from different objects were not populating correctly and switching to other fields ([#63676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102181836)).
* Fixed an issue where multiple fields of the respective custom objects were getting selected parallelly while performing **edit** or **save** or **exit** operations on the **Review Artifact** screen (internal ticket).
* Enhanced ARM by adding an option for **multiple ARM instances** to share a **single database cluster** (internal ticket).

#### 05 March 2023 <a href="#id-05-march-2023" id="id-05-march-2023"></a>

**(ARM v22.2.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where ARM was displaying incorrect installation settings and package version information in the deployment log while installing the package version from a CI job ([#63544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101947159)).
* Fixed an issue where user chose **Exclude Metadata Type** for a particular metadata type during a **CI Job**, but it was still deployed ([#62966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101046005)).
* Fixed an issue where user was unable to perform **Destructive Commit** with **PermissionSetGroups** metadata type ([#63172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101463001)).
* Fixed an issue where users weren't receiving emails after setting up **Mail Settings** ([#55070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089394047)).
* Fixed an issue where there was a discrepancy between **EZ-Commit** and **Commit templates** while retrieving **Email Template** metadata members ([#61696](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099121314)).
* Fixed an issue where **Merge Labels** were taking much longer than expected ([#62625](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100474287)).
* Fixed an issue where user tried to commit the changes without validation and UI displayed an error `Another commit is in progress` ([#61930](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099562127)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed a UI bug where there was a discrepancy in the timestamp displayed for a commit in the **Commits History** page ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Fixed an issue where **Merge** was not auto-rejected when validation criteria was not met ([#62287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100008338)).
* Enhanced **nCino** by adding an option to specify **Baseline Revision** in **Continuous Integration** for **Version Control** to perform feature deployments ([#43642](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073759034) and [#44506](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074950579)).
* Enhanced **nCino** by allowing users to deploy nCino **CI build** to multiple target sandboxes ([#41763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070674305)).
* Fixed a UI bug where incorrect notification was displayed in certain components pages when template was created using one org and was used by another org (internal ticket).
* Fixed an issue where **Baseline Managed Package Changes** option was not displayed on the UI when navigating from **Package xml** to select manually (internal ticket).
* Fixed an issue where there was a discrepancy between the **Attachments Records Success/Failure Count** and the **Retrieved Count** when **BULK API** was enabled for **Deployment** (internal ticket).

#### 26 February 2023 <a href="#id-26-february-2023" id="id-26-february-2023"></a>

**(ARM v22.2.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a UI bug in **Profile Manager** where **User Permissions** differences are shown in the report but not in the UI ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Enhanced the **Release Label** creation by increasing the range of retrievable commit history ([#61714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099129934)).
* Fixed an issue where user was unable to use **Release Labels** to perform **Deployment**, and it failed while trying to **Create Artifact** ([#59429](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096450140)).
* Fixed an issue where users with non-admin access were unable to register branches in **EZ-Commit** since upgrading to version 22.3 ([#62723](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100650673), [#62949](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101016055), [#62979](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010456), and [#62969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010302)).
* Fixed an issue where **Release Artifact** execution was failing when **rabit home** did not exist with an external agent (internal ticket).
* Fixed a UI bug on the **Profile** screen where the expand option for the **My Projects** and **My Roles** sections was not working (internal ticket).
* Fixed an issue where triggering **Data Retention** for **Audit Tables** was throwing the following error: `Unable to execute HTTP request: Read timed out` (internal ticket).
* Fixed an issue where extra characters are seen in the **Fetch Commit History** results while creating a **Release Label** with **Vlocity** label type (internal ticket).
* Fixed an issue where user was unable to delete Apex test class on the SF Org Management page (internal ticket).
* Enhanced **nCino** by introducing **New Spreads Schedule** tile in the **Feature Creation** screen (internal ticket).
* Fixed an issue where if the fields did not load for **Applied Mappings** during deployment, no error was thrown by the application (internal ticket).

#### 19 February 2023 <a href="#id-19-february-2023" id="id-19-february-2023"></a>

**(ARM v22.2.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was deploying single revision deployment with only report folder but sub-reports were also getting fetched, and the deployment was failing due to field dependency error ([#61403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098537015)).
* Fixed an issue where after deployment with single revision merge, user permission appears to be removed in target org but in the Salesforce target org the user permission is not removed, and an incorrect layout is displayed in UI ([#60531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097360001)).
* Fixed an issue where user performed a pre-validation commit and each process like file diff, validate deploy happened thrice as per the logs ([#61079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097987087)).
* Fixed an issue where user was unable to select master branch as the parent branch while creating a new branch in **EZ-Commit** ([#56188](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091240174)).
* Fixed an issue where user was customer trying to register a **Salesforce Org** with **Custom URL** but it was failing with an error ([#62192](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099509581)).
* Fixed an issue where user was unable to remove **Revisions**/**Commit Labels** from a **Release label** ([#59152](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096005470) and [#61578](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098950203)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed an issue where user user uploaded a **YAML file** to retrieve the **Vlocity components** but ALL metadata types were retrieved and displayed ([#61181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248158)).
* Fixed an issue where the same merge could be approved and rejected by different users simultaneously ([#60859](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097787146)).
* Fixed an issue where branch creation was faileing for sub-users in the **EZ-Commit** screen for **Non-DX Repo** (internal ticket).
* Fixed an issue where **Null Pointer** was seen in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where all credentials were listed twice in the **Credentials** dropdown in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where **branch creation** was failing for sub-users in **VC repos** when the credential scope was private while Admin credentials were fetched (internal ticket).
* Fixed an issue where user was unable to delete the **Apex Test class** under the SF org Apex **default config** (internal ticket).
* Fixed an issue where the **Add manually** checkbox under Apex class config was selected by default (internal ticket).
* Fixed an issue with nCino where user created a feature Deployment for **Credit memo** template with attachments, but **Attachments Objects Data** was not fetched, and the deployment failed with the following error: `Data file not fetched for object: Attachment` (internal ticket).
* Fixed an issue with nCino where **Standard Features** were not loaded in the **Feature Management** page (internal ticket).

#### 12 February 2023 <a href="#id-12-february-2023" id="id-12-february-2023"></a>

**(ARM v22.2.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was unable to download success/failure reports in **Single Dataloader** ([#61551](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098913200)).
* Fixed an issue where when multiple **CI Jobs** are triggered, jobs are moved into the queue as expected, but new jobs are not starting automatically getting processed once the existing jobs is cleared from the **CI Job results** page ([#59082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096042290)).
* Fixed an issue where **Dependency** order defined in **json** file was being changed on every commit but it was not supposed to ([#57731](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556797)).
* Fixed an issue where **Create Artifact** was not working as expected while using **Release Label** ([#61607](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098932152)).
* Fixed an issue where user was performing an **EZ-Commit** with **Review Artifact** option and download the .zip file to make some changes, but was unable to upload it afterwards ([#61751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248378)).
* Fixed an issue where meta.xml file was not deleted from the repository after committing the destructive changes ([#61736](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099207347)).
* Fixed an issue where **File Diff** was empty in case of modified **Uploaded** via **Review Artifact** in **PV Commit Flow** (internal ticket).
* Fixed an issue where **Review Artifact Tree** was not responding after uploading the modified file in **Commit Flow** (internal ticket).
* Fixed an issue where **User Permissions** and **Ip Ranges** are completly removed from the branch after commiting the **Permission Sets** and **Profiles** (internal ticket).
* Fixed an issue where **Super Admin** was getting an error while trying to activate newly signed up users (internal ticket).

#### 05 February 2023 <a href="#id-05-february-2023" id="id-05-february-2023"></a>

**(ARM v22.2.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where SFDX module creation log shows that deployment is successful but the module creation had failed ([#57318](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092768029)).
* Fixed an issue with **Backup from Org CI Jobs** where **PermissionSet User Permissions** were being deleted ([#59674](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096685144)).
* Fixed an issue where **Org to Org Deployment** for **Profiles** including **Deploy Profile Access Settings for selected components only** was not working as expected ([#60559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097375154)).
* Fixed an issue where **Post Destruct** fields were also added to **Pre Destruct** despite the user setting it to post ([#61162](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248005)).
* Fixed an issue where user set the **Max depth** value as '0' under **Vlocity Configuration Settings** but it was retrieving all level dependancy components ([#57501](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093212471)).
* Fixed an issue with DataLoader where the **Credit Memo Template** migration was not deploying after user upgraded their instance ([#57676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093470003)).
* Fixed an issue where user selected **Custom Metadata** members (records), but **EZ-Commit** was failing to generate **File Diff** with `Null` error ([#59709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096706005)).
* Fixed an issue where **Merge** was taking longer than usual, and then failing with `Null Exception` ([#60757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097574427)).
* Fixed an issue where **EZ-Commits** and **EZ-Merges** were taking much longer than usual ([#58098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094302292)).

#### 29 January 2023 <a href="#id-29-january-2023" id="id-29-january-2023"></a>

**(ARM v22.2.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment was failing with the following error when user was deploying **Permissionset** with a user-permission **Manage Public Documents**: `Permission Manage Public Documents depends on permission(s): Create Document, Delete Document, Edit Document, Read Document` ([#60597](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097399881)).
* Fixed an issue where CI jobs were failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#59050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095999076)).
* Fixed an issue where **Reports** deployment validation failed in **EZ-Merge** but was successful in **EZ-Commit** and **Deployment** modules ([#57714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093587003)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Fixed an issue where user initiated the prevalidation commit by enabling the destructive type but the deployment failed with an error `null` at **Diff** ([#59919](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096907001)).
* Fixed an issue where **Validate Deploy** failed in **QuickMerge** and displayed the following message: `This folder unique name already exists for this folder type or has been previously used. Please choose a different name` (internal ticket).
* Fixed an issue where CI job wasn't considering the metadata changes, so the destructive changes were not being prepared or displayed on the build. (internal ticket).

#### 22 January 2022 <a href="#id-22-january-2022" id="id-22-january-2022"></a>

**(ARM v22.2.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user changed the permissions to **list view** from **visible to all users** to **visible only for me** while using the previous commit label, it is added under the **Deleted** tab ([#59359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096219627)).
* Fixed an issue where commit was running for longer and remained **in-progress** and **validation check log** is also in progress ([#59199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096003630)).
* Fixed an issue where commits with SFDX metadata structure are **failing** in metadata **retrieval stage** ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed an issue where user couldn't create a managed package with the selected ancestor ([#59044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095985421)).
* Fixed an issue where **CI Job** was occasionally failing with the error `BUILD FAILED` ([#57647](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093370172)).
* Fixed an issue where CI job was taking the last modified user name if trigger through API instated of taking API token user ([#55438](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089958034)).
* Salesforce **API version 57** (Beta support) is upgraded. The label is modified throughout ARM application including DataLoader and nCino (internal ticket).
* Fixed an issue where nCino CI job was stuck in **Build Success** status for more than a week ([#59040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095982206)).
* Fixed an issue where user was trying to deploy RBC (nCino Screens) and the deployment was failing for some of the objects, but there were no error messages shown on the UI ([#58044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094164003)).
* Fixed an issue where user was using SSH credential in AutoRABIT but it was throwing the following error: `Invalid Private Key` ([#59244](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096134293)).
* Fixed an issue where user has created a Commit label but it was not available while trying to perform an **EZ-Merge** ([#55176](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089550097)).
* Fixed an issue where user was not getting file Diff to commit the previously validated commit label and getting an error in the Diff ([#59114](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096048883)).
* Fixed an issue where user was getting an error while trying to create a new branch in GitHub ([#59193](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096138920)). For more information, click [here](https://knowledgebase.autorabit.com/docs/faqs-version-control?highlight=$%20ssh-keygen%20-t%20rsa%20-b%204096%20-C#why-am-i-getting-an-error-while-trying-to-register-github-repository-with-ssh).
* Fixed an issue where user could not create an **xml package** for deployment because artifact creation and package manifest preparation were failing with an `invalid credentials` error ([#59402](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096425001)).
* Fixed an issue where user was trying to perform single revision merge but validation deployment was failing with the following error `Metadata package is empty` ([#59028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095867179)).
* Fixed an issue where when there are special characters in **Layout metadata** then the user was not able to add it manually in **Skip Members** section ([#58998](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095876003)).
* Fixed an issue where user wanted to choose commit revision in a release label based on its comment but if the comment was not in text, it was not completely visible in the UI ([#59014](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095898340)).
* Fixed a UI bug where an incorrect validation message was seen while adding **Skip Members** manually (internal ticket).
* Fixed an issue where the selected tab checkbox in the **metadata components** page in the EZ-Commit was not functioning as expected (internal ticket).
* Fixed an issue where the **EZ-Commit** validation screen was displaying incorrect notification when name of the template was empty (internal ticket).

#### 15 January 2022 <a href="#id-15-january-2022" id="id-15-january-2022"></a>

**(ARM v22.2.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556)).
* Fixed an issue with user received 6 notifications for a failed **CI Job** instead of 1 ([#58436](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095199003)).
* Fixed an issue where user was trying to register branches to AutoRABIT through GitHub, but was getting the following error: `Lower Region` ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed a recurring issue where **Commits** and **Merges** were slowing down at a particular step, and **EZ-Merge** was failing with an error at commit phase ([#51268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085726862)).
* Fixed an issue where while performing destructive changes in **EZ-Commit**, it was creating **package.xml** in root path folder in **SFDX** structure ([#57868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093790001)).
* Fixed a UI bug on **CI List** and **CI Results** pages where when pagination was changed, the first 25 records were repeated (internal ticket).
* Fixed an UI bug where the **LastUsedDate** column was not displayed in the **Branch Table** (internal ticket).

#### 8 January 2022 <a href="#id-8-january-2022" id="id-8-january-2022"></a>

**(ARM v22.2.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189)).
* Fixed a build bug where **CI Job Build** was failing during package preparation **step 5** failing while commiting **DecisionMatrixDefinition** and throwing an error ([#58376](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095049142)).
* Fixed an issue with **Branching Baseline** where the developers were migrating the changes from dev branch to INT, but **Diff** was showing 100% addition which is incorrect\
  ([#58478](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095251543)).
* Fixed an issue where generating **Diff** for a **Commit Label** was taking much longer than expected ([#55220](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591780)).
* Fixed an issue where **Code coverage** job was running **4 hours** earlier than scheduled every time services were restarted ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed a UI bug where scrollbar and pagination were not visible on the **Org Sync History** page (internal ticket).

#### 01 January 2022 <a href="#id-01-january-2022" id="id-01-january-2022"></a>

**(ARM v22.2.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Deployment** was failing with **no changes** in the package (internal ticket).
* Fixed an issue where user was unable to create **Environment Provisioning** templates for multiple component types ([#57898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093797903)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).
* Fixed an issue where AutoRABIT **SSH credentials** were failing with an error `Auth failed` while trying to connect with **AWS CodeCommit** ([#53694](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087714369)).
* Fixed an issue where **EZ-Commit Diff** was taking approximately 4 hours while **Refactoring CustomField**, which is much longer than expected ([#56650](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091636348)).
* Fixed an issue where **ExternalCredential** metadata type was not getting excluded even when user added it in the **excluded lists** in **CI Configuration** (internal ticket).
* Fixed an issue where after triggering **Branching baseline**, standard value set metadata type was getting displayed under the **deleted components** through **Autodraft** for **Non-DX repo** (internal ticket).
* Fixed an issue where **Destructive Components** are not seen in case of **PV-DX-Destructive Merge** for **Report** metadata type. Instead, it displaying a message: `Package is empty` (internal ticket).

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

**(ARM v22.2.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where non-admin users were unable to select **Branch Type** while trying to create a **new branch** from **New EZ-Commit Branch** ([#57732](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556923)).
* Fixed an issue where **CI jobs** are failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#57371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880162)).
* Fixed an issue where user was trying to deploy only the **Documents** from the branch to Org, but deployment failed and **Asynch ID** is not generating ([#57263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092661381)).
* Fixed an issue where user was trying to deploy **login hours**. First they merged it to target branch, then once CI job triggers login hours are not getting deployed to target org ([#57359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880015)).
* Fixed multiple issues where user was having trouble creating **new package version** from **previous ancestor** version ([#55707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090251366)).
* Fixed an issue where **Merge** is **failing** with the following error: `failed to push some refs to 'https://github.com/salesforce-align/SFDX.git'` ([#55939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090999346)).
* Fixed an issue where the **Standard Field Account.name** is displayed in the deleted components list ([#57396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092927781)).
* Fixed an issue where the **prevalidation commit** failed at **delta** stage ([#55763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090435979)).
* Fixed an issue where user was unable to create **commit label** for the same repository second time, and branches were not displayed (internal ticket).

#### 18 December 2022 <a href="#id-18-december-2022" id="id-18-december-2022"></a>

**(ARM v22.2.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DataLoader Pro** where jobs executed in the last 6 months were not showing in the database process table and in the **Reports** module ([#53980](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087981132)).
* Fixed an issue with **Deploy SFDX Source With ALM Mapping** where CI job with ALM Mapping was not working as expected for Team which is not default ([#55995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091129007)).
* Fixed an issue where **Profile Diff** is working as expected for **Selective Deployment**, but not while using the same profile in the profile manager ([#52868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087005140)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189), [#55754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090487029)).
* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).

#### 11 December 2022 <a href="#id-11-december-2022" id="id-11-december-2022"></a>

**(ARM v22.2.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where multiple metadata types where not able to retrieve ([#56668](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091694003)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was creating the **feature template** for some of the **nCino** objects but it was taking too long to **retrieve** the objects from **Source Org** ([#53915](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087934809)).
* Enhanced **nCino** to:
  * Modify **notification** messages for null checks on request parameters (internal ticket).
  * Display only **nCino** revisions for Version Control in nCino feature **deployment** (internal ticket).

#### 04 December 2022 <a href="#id-04-december-2022" id="id-04-december-2022"></a>

**(ARM v22.2.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Flexi pages** were not picked up in a **CI Job** even after the commit with same set of metadata was excluded by user ([#54518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088461033)).
* Fixed an issue where **Abort** function to stop **Provar** jobs was not working as expected ([#55511](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090032787)).
* Fixed an issue where production backup **CI Job** was not picking all the changes, and when user modified the job configuration and retriggered the job, the application was throwing the following error `java.lang.NullPointerException: null` ([#55213](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591408)).
* Fixed an issue where all **Slack Notifications** were selected by default and user was unable to unselect all at once ([#55817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090727146)).
* Fixed an issue where **SFI components** were not being fetched both in **Commit** and **Deployment** modules ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue with **DataLoader Pro** where user selected a field as **External ID** in a job and saved it, but the saved entry was lost and user was unable to map it ([#55011](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089299148)).
* Fixed an issue where **Deployment validation** in **Prevalidation Commit** fails because profile validation automatically picks **User Permissions** even though **Remove User Permissions** option is selected ([#54941](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088985107)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where **Release Label Merge** was failing and throwing the following error: `fatal: bad revision` ([#55000](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089278434)).
* Fixed an issue with **EZ-Commit** where user was unable to upload a **Custom YAML** file ([#55826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090770005)).
* Fixed an issue where the **Vlocity Component** option under **Fetch Changes** is not populating for sub-users with roles that have all permissions and access ([#54962](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089032619)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was performing a merge operation and validating the package on the **target org** but the validation was failing with multiple errors ([#55541](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090145025)).

#### 27 November 2022 <a href="#id-27-november-2022" id="id-27-november-2022"></a>

**(ARM v22.2.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was trying to migrate **Products**, **Pricebooks**, and its entries but the **Deploy** was failing for **Pricebook** and throwing the following error: `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY: insufficient access rights on cross-reference id:--` ([#55263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089652641)).
* Fixed an issue with **nCino** where user was trying to create a custom feature template including **product objects** as well as **product line** but the deployment was failing with the following error: `Required fields are missing: [LLC_BI_Product_Line_c]` ([#51209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085641324)).
* Fixed an issue with **nCino** where **CI Job** was stuck in **Build Success** status ([#53605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087564091)).
* Fixed an issue where **CI Job** build was failing with a **NullPointerException** ([#55204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089616148)).
* Fixed an issue where the **Repository Branch** was unavailable to select to run the **Merge** process after selecting **On successful deployment** option ([#55537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090158003)).
* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue with **EZ-Commit** where user was trying to perform a **destructive commit** using **Autodraft** option, but was unable to select **deleted components** under the **Deleted** tab ([#55507](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089979335) and [#55651](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090293003)).
* Fixed an issue where user was getting a **NullPointerException** when trying to resolve a **Merge conflict** ([#55137](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089410195)).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was able to create a **Delegated Group** but was unable to add a **Delegated Admin** user to the group using **Environment Provisioning** ([#55266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089705014)).

#### 20 November 2022 <a href="#id-20-november-2022" id="id-20-november-2022"></a>

**(ARM v22.2.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing **Prevalidation Commit** but commits in the repository have different components than the ones shown in **Diff** before the commit ([#52307](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086491044)).
* Fixed an issue with **Install an Unlocked or Managed Package from a Version Control Branch** where CI job getting an exception and the build status was showing as successful but the **Scratch Org** was not being created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **CI Job** shows that the ALM status has been updated successfully but on **Azure ALM** it is not updated ([#54669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088657005)).
* Fixed an issue where **Test Automation CI Jobs** were failing due to **InitializeDriver** & **quit methods** ([#45878](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077372830)).
* Fixed a bug where user was able to access certain branches in the **Deployment** module to which he did not have access under **Profile Settings** ([#54879](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089011291)).
* Fixed an issue with **CI Jobs** where the build failed with **Checkout** conflict for an **.svg file** ([#54172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088252005)).
* Fixed an issue with **nCino** where **Record Classification** and **Classification Objects** were missing in the template (internal ticket).
* Fixed an issue with **nCino** where user was creating a CI Job and observed that `Use UTF-8 file encoding for the file read and write operations` flag was displayed at the bottom below the **Commit Details** section (internal ticket).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was unable to add another branch to **Azure** in the **ALM MGMT Repository mappings** ([#55133](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089433593)).
* Fixed an issue where the **Destructive** commit **Diff** was including more components than selected ([#54795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088780309)).
* Fixed an issue where a merge got stuck for a long time and the **Commit ID** was reflected in **BitBucket** but unavailable to select for release label deployment ([#52964](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087060140)).

#### 13 November 2022 <a href="#id-13-november-2022" id="id-13-november-2022"></a>

**(ARM v22.2.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was trying to create an **Extract** process in **DataLoader** but after validating the query the application was throwing an error: `not supported; requires @DynamoDBTyped or @DynamoDBTypeConverted` ([#54648](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088630160)).
* Fixed an issue with **CI Jobs** where **External Credential** metadata was not identified during **Deployment** ([#53939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087955144)).
* Fixed a UI bug where user was performing an **org to org deployment** using **package.xml** file and the components were successfully deployed and also verified on Salesforce target, but the status on ARM was still **In-Progress** ([#50459 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375)and [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue with **DX CI Jobs** where user is not getting details of faulty commit revisions in the notification ([#54063](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088015242)).
* Fixed an issue with **Profile Manager** where the deployment is not showing any progress in the logger detail in front end. It was updated only after completion of the deployment job at backend ([#53706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704963)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed a bug where **Merge Commit** validation was not considering special characters like %,#, etc. as a value and throwing the following error: `Merge comment should not contain an empty space` ([#54512](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088479003)).
* Fixed an issue where ARM was slowing at different phases in the **EZ-Commit** module ([#50503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084910726)).
* Fixed an issue where Git check response was not delivered for validation **CI Job** even though user has added the comment for a **Pull request** in the remote repository ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).

#### 06 November 2022 <a href="#id-06-november-2022" id="id-06-november-2022"></a>

**(ARM v22.2.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DX CI Job** where user selected **Do Not Include Skip Members** but the respective mapper reports were not skipped (internal ticket).
* Fixed an issue where the **Deployment** module page was loading very slowly and then throwing an error: `Page Unresponsive` ([#53675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704191)).
* Fixed the following issues in **CI** and **Reports** modules (internal ticket):
  * Build With **NULL ERROR** (issue exists both with Proxy and without Proxy)
  * SF Org Code coverage Execution is failing (issue exists both with Proxy and without Proxy)
  * Jenkins Build is updated with **FAILED** status even after it is successfully completed (issue exists only without Proxy)
  * Checkmarx text is not displaying the **Proxy Configuration** note (Only With Proxy)
* Fixed an issue with **QA Environments** where user was unable to create and delete the **SFDX module** because of the **Apache config CACHE** settings (internal ticket).
* Fixed an issue with the **Deployment** module where user initiated a **Deployment** without selecting the **Do not Include Skip Members** option, but this option was auto-enabled and skipped the member at the time of deployment ([#53747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087811296)).
* Fixed an issue with **Modularization** where user creating a module and selected the **Ignore installed components** check box but the installed components were not ignored causing the deployment to fail ([#53703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087755311)).
* Fixed an issue with **AccelQ Test Automation** where test case fails but the error details pop-up is not showing the details of the error that caused the failure ([#54224](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088281589)).
* Fixed an issue where user is setting up the **Apex PMD rules** as **Priority 1** & **Priority 2** in the **CI Job** but the SCA Report is showing the **Priority 3, P4 & P5** which wasn't selected ([#54017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087969396)).
* Fixed an issue where the **Git** check response was not delivered for a validation **CI Job** ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).
* Fixed an issue where the **Deleted Report** metadata components were not found in the **EZ-Commit** ([#53119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087247293)).
* Fixed an issue where user was trying to perform a **Quick Merge** but was getting an **Undefined** error for all labels (internal ticket).

#### 30 October 2022 <a href="#id-30-october-2022" id="id-30-october-2022"></a>

**(ARM v22.2.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where triggering a **CI Job** in **Objects** was resulting in an ambiguous error in the **CI Job Build** ([#53066](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087190013), [#52955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087099268), [#53631](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087579265)).
* Fixed an issue where all **CI Jobs** were failing and throwing the error: `Validation Checking failed Version Control Mappings not found for Repo: SA Repo and Branch: bugfix/Bugfix_PQT_Rel_Validation` ([#52945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087098136), [#52950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087101272), [#52757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086925007)).
* Fixed a UI bug on the **CI Jobs** page for **Install an Unlocked or Managed Package from a Version Control Branch** type where old **Dev Hub**dropdown list was displayed in the **Deploy** section (internal ticket).
* Fixed an issue with **AccelQ** where running a test execution was successful even before the jobs were completed in AccelQ, but the status was always showing as **Not Run** instead of **Success** or **Failure** even if the jobs have been successfully completed ([#50181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084509148)).
* Fixed a **Page Unresponsive** issue while creating a new **Release Label** by adding a feature to list limited results on each page ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where a merge got auto-approved and was in **Merged Not Commit** status ([#52398](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086586845), [#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed an issue where user created a **Release Label**, performed a **Merge** operation, committed changes to the target branch, and created two revisions in the **Github** branch.\
  But ARM was throwing an error while applying merge stage and only on the revision generated ([#51364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085859319)).
* Fixed an issue where **EZ-Commit** initiation was stuck with the error: `Unable to fetch Salesforce Org users. Reason: Invalid login: invalid user name or password or security token or api version or user locked out` ([#52550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086834002)).
* Fixed an issue where user was not able to select the orgs in the **EZ-Commit** drop down ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001), [#51219](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085620605)).
* Fixed an issue where **Page Size** value on the **Edit Release Label** screen is defaulting to the previous value instead of the set value (internal ticket).
* Fixed a UI bug where **OK Button** in **Automation** is not visible in the **Create Release Label** pop-up when opened in 100% zoom (internal ticket).

#### 23 October 2022 <a href="#id-23-october-2022" id="id-23-october-2022"></a>

**(ARM v22.2.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **CI Job** was successful but was including components from **GIT revisions** from old deleted branches ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a production deployment using CI job for an object, but it failed with the following error: `Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field` ([#48626](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082749181)).
* Fixed an issue where **CI Job** was getting an exception, **Build** status was showing as _successful_, but **Scratch Org** not getting created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **Managed Package** was picking the wrong ancestor by adding a feature to manually select the preferred ancestor while creating a package version ([#48311](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223305)).
* Fixed an issue where user was adding **URLs** to the **Proxy Configuration Settings** but the **URL List** was not reflecting the same (internal ticket).
* Fixed an issue where **Custom Template Creation** failed and the **Logs** did not record the reason for failure ([#52147](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086277150)).
* Fixed an issue where the **Created By** value was not visible in **Dataloader**, **Dataloader Pro DL Config**, and the **TestEnv History** page (internal ticket).
* Fixed an issue where the **Comment Box** was not accepting more than **100 characters** while rejecting a **Commit**, but was working as expected while approving a commit ([#51384](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085891476)).
* Fixed an issue with **Apex Test Class Config.** in **SF MGMT ORG** where the **Fetch Current Set**, **Add Manually**, and **Auto Populate** options were throwing an error: `Error 200` ([#52408](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086578687), [#52328](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086485900)).
* Fixed an issue where user set **Commit validation Criteria** to **Auto reject after 7 days** but the older Pre-validation commits are not auto rejected after 7 days ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user cannot add **Skip** members manually and it is failing due to **special characters** being included ([#53139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087266642)).

#### 16 October 2022 <a href="#id-16-october-2022" id="id-16-october-2022"></a>

**(ARM v22.2.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where skipped members were present in many components but only **Report Metadata** was failing during **Deployment** ([#51040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085433814)).
* Fixed an issue where **CI Job** was getting stuck in **In Progress** status but the log showed that the deployment was successful ([#51140](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085583019)).
* Fixed an issue where GitHub login credentials were not working when user triggered a CI Job for the second time ([#50630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085136003)).
* Fixed an issue where CI Job has failed in the Salesforce org, but still stuck in **In Progress** status in ARM ([#50435](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084823763)).
* Fixed an issue where user raised a **Pull request** on a branch and was getting a webhook response, but CI Job build was not triggered ([#51592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085996953)).
* Fixed a UI bug where **Add to dashboard** button was unavailable for widgets ([#52333](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086514169)).
* Fixed an issue where a new database file is created and overwritten with an existing database file whenever the server was restarted (internal ticket).
* Fixed an issue where user was trying to resolve conflicts on **Merge Request Labels** created more than 7 days ago, but application was throwing an error: `undefined` (internal ticket).
* Fixed an issue where **Custom Email Template** was not working for **Email notifications** ([#47484](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080506162)).
* Fixed an issue where user was testing **SSH Connection** but the application was throwing an error: `invalid privateKey` ([#50940](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371198)).
* Fixed an issue with **nCino** where **UI Log** was not generated for failed CI Jobs ([#50442](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084795478)).
* Fixed an issue where **New EZ-Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue where **Audit Logs** were not generating via **Postman Services** ([#50221](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084545179)).
* Fixed an issue where **Commits** were getting stuck and throwing the following error: `No credential have been found with Name:git`, but was not reflecting in the UI log ([#51713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086127001)).
* Fixed an issue with **Workspace Settings** where unused workspaces were not being cleared despite selecting **Clear all workspaces which are not used in last 7 days** ([#50164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084481079)).
* Fixed an issue where user was performing a **Prevalidation EZ-Commit** and found that some **Layout Assignments** were deleted though those layouts were not part of the commit ([#50945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371456)).
* Fixed an issue with **nCino** where migration was failing due to errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).

***

## **ARM Release Notes 22.1**

**Date of release:** _20 March 2022_\
**Article last updated:** _23 October 2022_

### New features <a href="#new-features" id="new-features"></a>

#### 1. Squash and merge <a href="#id-1-squash-and-merge" id="id-1-squash-and-merge"></a>

We have added the **Squash and Merge** feature in this release. Sometimes, when merging a long list of changes from a development branch into the master, it's helpful to squash those commits into one change for ease of review and declutter the repo's commit history. AutoRABIT offers an option to squash all commits in a merge request into one commit after the merge is approved and completed.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/squash%20and%20merge.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/ez-merge/squash-and-merge.md)

#### 2. SFDX- Import packages <a href="#id-2-sfdx-import-packages" id="id-2-sfdx-import-packages"></a>

**Packages**

The users could previously build a new package (unlocked or managed) and update the package's version in Salesforce DX. With this release, you may now import packages and update the version of packages created outside of AutoRABIT.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/import%20packages.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/import-an-unlocked-managed-package.md)

**Dev Hub management**

With this update, users will see all of the packages in their dev hub in the record view. You may expand each package to show the package's versions in order and package data such as version name, version number, ancestor version, ancestor dependencies, etc.

![Dev hub.gif](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Dev%20hub.gif)

[**Read more →**](../../../product-guides/arm/registering-a-devhub.md)

#### 3. Step-based rollback <a href="#id-3-stepbased-rollback" id="id-3-stepbased-rollback"></a>

The option to list the API-supported and unsupported API components is added to the CI job/deployment rollback. If such components may be deployed to the target environment but do not have API support to delete them, ARM will display them individually as unsupported API types. Take, for example, **RecordType**.

The **RecordType** component may be deployed to the target environment, but it cannot be removed; instead, we need to connect to the target Salesforce environment to deactivate the component.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/step%20based%20rollback.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-rollback.md)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Checkmarx upgrade to v9.4.1 <a href="#id-1-checkmarx-upgrade-to-v941" id="id-1-checkmarx-upgrade-to-v941"></a>

Checkmarx has been updated to version **9.4.1**. Earlier, Checkmarx used a username/password-based authentication method. Now, the user will be able to use token-based authentication with the Checkmarx upgrade.

#### 2. Export all users <a href="#id-2-export-all-users" id="id-2-export-all-users"></a>

The **Export All Users** feature allows the org admins to export a CSV file of all the users currently in their account. We now have added the following fields to the existing CSV file:

* CreatedDate
* CreatedByName
* DeativatedDate
* LastLoginDate
* DeactivatedByName
* LastModifiedDate
*   LastModifiedByName.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/export%20all%20users.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/users-roles-and-permissions.md)

#### 3. Pull request support for Azure cloud repositories <a href="#id-3-pull-request-support-for-azure-cloud-repositories" id="id-3-pull-request-support-for-azure-cloud-repositories"></a>

We have extended the support of having the pull request support in the CI Job for the Azure repository. This feature was previously available for Github cloud/Enterprise and Bitbucket cloud/Enterprise; however, we've added support for Azure cloud repositories (DX and non-DX repositories) with this release.

#### 4. Merge/commit approval eligibility <a href="#id-4-mergecommit-approval-eligibility" id="id-4-mergecommit-approval-eligibility"></a>

If you want to make sure one or more people approve every commit or merge, you can enforce this workflow by using merge/commit approvals. These approvals allow you to set the number of necessary approvals to approve every commit/ merge in a project.

The org admins' eligibility level has been enhanced with the ARM 22.1 version. If you're an administrator, you will have the privilege to approve self-merge even if the criteria to self-approve a merge is set to FALSE. This permission will be denied to all members of your team except the org admin. To put it another way, no criteria can restrict an org administrator from approving any EZ-commit/ EZ-Merge.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/commit-merge%20approval.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/merge-approvals.md)

#### 5. CodeScan additional metadata support <a href="#id-5-codescan-additional-metadata-support" id="id-5-codescan-additional-metadata-support"></a>

We have enhanced the scope for analysis of what CodeScan does by adding support for additional metadata and rules. For our ARM users who want to incorporate the SCA tool into their subscriptions, CodeScan would be their first choice as it now supports more robust integrations.

Below is the list of CodeScan supported metadata types:

|                                   |                         |                         |
| --------------------------------- | ----------------------- | ----------------------- |
| Apex Triggers                     | Apex Classes            | Aura Definition Bundles |
| Lightning Component Bundles (LWC) | Visualforce Pages       | Custom Object           |
| Settings                          | Flows                   | Workflows               |
| Profiles                          | Sharing Rules           | Sharing Criteria Rules  |
| Sharing Owner Rules               | Sharing Territory Rules | Permission Sets         |

#### 6. SFDX CLI update <a href="#id-6-sfdx-cli-update" id="id-6-sfdx-cli-update"></a>

The SFDX CLI has been upgraded to the latest stable **7.134** version.

Key characteristics to look for:

* Single deployment request for constructive and destructive changes
* Quick deploy and rollbacks work for both constructive and destructive changes
* Package preparation has been improved.

***

### Improvements <a href="#improvements" id="improvements"></a>

* The jquery-UI version has been upgraded to **v1.13.0** to fix security issues. Upgrading to the most recent version of jquery makes our application more secure and potentially faster in script execution and loading.
* Minor performance, bug fixes, and security improvements can also be observed in the ARM portal.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

**(ARM v22.1.48)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where wrong **timezone** region was displaying for users ([#71553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111412006)).
* Fixed an issue where the **EZ-Commits report file** displayed the file count but not the components count ([#71538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111479094)).
* Fixed an issue where clone build jobs were taking between 10 and 25 minutes, which is much longer than expected ([#70227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109182447)).
* Fixed an issue where CI job build failed to show changes in the org after deployment ([#70791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110120443) and [#71956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111861212)).
* Fixed an issue where CI job to generate **Code Coverage Report** was not reflected in the org or in the e-mail notification ([#72042](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111983230)).
* Fixed an issue where merge status is displayed as completed but no revision is generated, and the merge is not available in the UAT branch ([#71266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110960210)).
* Enhanced **DataLoader** by adding the ability to **field mapping** through the lookup fields ([#58480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095290579)).
* Fixed an issue with **DataLoader** where while running an **Extract** job on the **PUBLISHER** object, the job was failing with the following error `Publisher: column id is not supported in ORDER BY clause` ([#71303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111030174)).
* Enhanced the **nCino filter criteria** by adding the ability to search and filter labels using the whole or partial name ([#71826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111666181)).
* Enhanced ARM by using known vulnerable components through the **DataTables 1.10.12** plugin for advanced data table functionalities such as sorting, filtering, pagination, and more. This allows users to easily display and manipulate large sets of data on their web pages in a user-friendly manner (internal ticket).
* Fixed an issue with **Prevalidation Merge** where users were unable to deploy the **ApexClass Tests** related to ApexClasses and Apex Triggers (internal ticket).
* Fixed a UI bug where the **date column** in the **EZ-Commit Weekly report** was displaying incorrect values (internal ticket).

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

**(ARM v22.1.46)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **validation jobs** on **Pull Requests** weren't getting triggered ([#67538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106410313), [#67494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106382311), and [#67448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106353830)).
* Fixed an issue where Salesforce components were showing under the **Apex Test Success** tab in the **Deployment** module, which is not expected behavior ([#67537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253424)).
* Enhanced the **Branching Baseline** feature by allowing admin to define default baseline branches, making it easier for developers to choose the default branch for each project ([#63571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102024066)).
* Fixed an issue where user was unable to register a branch even though **Test Connection** was successful ([#67023](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105968682)).
* Fixed an issue where ARM wasn't fetching the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** option ([#67503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106378846)).
* Fixed an issue where **SCA Report** failed to run using **Codescan** plugin with the following Salesforce error: `An unexpected error occurred. Please include this ErrorId if you contact support: 384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Fixed an issue where triggered **CI jobs** were either failing due to an error **No Such File or Directory found**, or getting aborted automatically after some time and logs weren't printing at the back end ([#67549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253579), [#66910](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106035058), [#67724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106597223), [#67720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106570720), [#66881](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936162), and [#67667](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604150)).
* Fixed an issue where triggered **CI jobs** were taking too long to build, and also slowing down ARM altogether ([#66846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105989569)).
* Fixed an issue where if the file name contained spaces, **Commit Validation** via **VS Code** plugin was unable to detect the file ([#63518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101868754)).
* Fixed an issue where **Search & Substitute** was not updating the value for a **custom label** in the SF org ([#66809](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936001)).
* Fixed an issue where there was a discrepancy between the changes captured in the ARM **Diff** and the repos in **BitBucket** ([#60596](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097396243)).
* Fixed an issue where the SF org **URL** is not displaying the updated one under **Profile** ([#67718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106581101)).
* Fixed an issue with **nCino** where CI job filter changes on templates are not reflecting after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue with **Dataloader Pro** where user tried to migrate **Account Object Data** with **Attachments Object**, but the logs verify that there is a **Null Pointer Exception**. (internal ticket).
* Improved **nCino** by adding additional loggers for **Branching baseline** for user to view the status in the UI (internal ticket).
* Fixed an issue where user was unable to filter while trying to select a job which had spaces in the job name (internal ticket).

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

**(ARM v22.1.38)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where non-admin users were unable to select **Branch Type** while trying to create a **new branch** from **New EZ-Commit Branch** ([#57732](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556923)).
* Fixed an issue where **CI jobs** are failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#57371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880162)).
* Fixed an issue where user was trying to deploy only the **Documents** from the branch to Org, but deployment failed and **Asynch ID** is not generating ([#57263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092661381)).
* Fixed an issue where user was trying to deploy **login hours**. First they merged it to target branch, then once CI job triggers login hours are not getting deployed to target org ([#57359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880015)).
* Fixed multiple issues where user was having trouble creating **new package version** from **previous ancestor** version ([#55707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090251366)).
* Fixed an issue where **Merge** is **failing** with the following error: `failed to push some refs to 'https://github.com/salesforce-align/SFDX.git'` ([#55939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090999346)).
* Fixed an issue where the **Standard Field Account.name** is displayed in the deleted components list ([#57396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092927781)).
* Fixed an issue where the **prevalidation commit** failed at **delta** stage ([#55763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090435979)).
* Fixed an issue where user was unable to create **commit label** for the same repository second time, and branches were not displayed (internal ticket).

#### 11 December 2022 <a href="#id-11-december-2022" id="id-11-december-2022"></a>

**(ARM v22.1.37)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where multiple metadata types where not able to retrieve ([#56668](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091694003)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was creating the **feature template** for some of the **nCino** objects but it was taking too long to **retrieve** the objects from **Source Org** ([#53915](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087934809)).
* Enhanced **nCino** to:
  * Modify **notification** messages for null checks on request parameters (internal ticket).
  * Display only **nCino** revisions for Version Control in nCino feature **deployment** (internal ticket).

#### 04 December 2022 <a href="#id-04-december-2022" id="id-04-december-2022"></a>

**(ARM v22.1.36)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Flexi pages** were not picked up in a **CI Job** even after the commit with same set of metadata was excluded by user ([#54518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088461033)).
* Fixed an issue where **Abort** function to stop **Provar** jobs was not working as expected ([#55511](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090032787)).
* Fixed an issue where production backup **CI Job** was not picking all the changes, and when user modified the job configuration and retriggered the job, the application was throwing the following error `java.lang.NullPointerException: null` ([#55213](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591408)).
* Fixed an issue where all **Slack Notifications** were selected by default and user was unable to unselect all at once ([#55817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090727146)).
* Fixed an issue where **SFI components** were not being fetched both in **Commit** and **Deployment** modules ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue with **DataLoader Pro** where user selected a field as **External ID** in a job and saved it, but the saved entry was lost and user was unable to map it ([#55011](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089299148)).
* Fixed an issue where **Deployment validation** in **Prevalidation Commit** fails because profile validation automatically picks **User Permissions** even though **Remove User Permissions** option is selected ([#54941](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088985107)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where **Release Label Merge** was failing and throwing the following error: `fatal: bad revision` ([#55000](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089278434)).
* Fixed an issue with **EZ-Commit** where user was unable to upload a **Custom YAML** file ([#55826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090770005)).
* Fixed an issue where the **Vlocity Component** option under **Fetch Changes** is not populating for sub-users with roles that have all permissions and access ([#54962](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089032619)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was performing a merge operation and validating the package on the **target org** but the validation was failing with multiple errors ([#55541](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090145025)).

#### 27 November 2022 <a href="#id-27-november-2022" id="id-27-november-2022"></a>

**(ARM v22.1.35)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was trying to migrate **Products**, **Pricebooks**, and its entries but the **Deploy** was failing for **Pricebook** and throwing the following error: `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY: insufficient access rights on cross-reference id:--` ([#55263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089652641)).
* Fixed an issue with **nCino** where user was trying to create a custom feature template including **product objects** as well as **product line** but the deployment was failing with the following error: `Required fields are missing: [LLC_BI_Product_Line_c]` ([#51209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085641324)).
* Fixed an issue with **nCino** where **CI Job** was stuck in **Build Success** status ([#53605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087564091)).
* Fixed an issue where **CI Job** build was failing with a **NullPointerException** ([#55204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089616148)).
* Fixed an issue where the **Repository Branch** was unavailable to select to run the **Merge** process after selecting **On successful deployment** option ([#55537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090158003)).
* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue with **EZ-Commit** where user was trying to perform a **destructive commit** using **Autodraft** option, but was unable to select **deleted components** under the **Deleted** tab ([#55507](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089979335) and [#55651](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090293003)).
* Fixed an issue where user was getting a **NullPointerException** when trying to resolve a **Merge conflict** ([#55137](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089410195)).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was able to create a **Delegated Group** but was unable to add a **Delegated Admin** user to the group using **Environment Provisioning** ([#55266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089705014)).

#### 20 November 2022 <a href="#id-20-november-2022" id="id-20-november-2022"></a>

**(ARM v22.1.34)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing **Prevalidation Commit** but commits in the repository have different components than the ones shown in **Diff** before the commit ([#52307](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086491044)).
* Fixed an issue with **Install an Unlocked or Managed Package from a Version Control Branch** where CI job getting an exception and the build status was showing as successful but the **Scratch Org** was not being created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **CI Job** shows that the ALM status has been updated successfully but on **Azure ALM** it is not updated ([#54669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088657005)).
* Fixed an issue where **Test Automation CI Jobs** were failing due to **InitializeDriver** & **quit methods** ([#45878](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077372830)).
* Fixed a bug where user was able to access certain branches in the **Deployment** module to which he did not have access under **Profile Settings** ([#54879](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089011291)).
* Fixed an issue with **CI Jobs** where the build failed with **Checkout** conflict for an **.svg file** ([#54172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088252005)).
* Fixed an issue with **nCino** where **Record Classification** and **Classification Objects** were missing in the template (internal ticket).
* Fixed an issue with **nCino** where user was creating a CI Job and observed that `Use UTF-8 file encoding for the file read and write operations` flag was displayed at the bottom below the **Commit Details** section (internal ticket).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was unable to add another branch to **Azure** in the **ALM MGMT Repository mappings** ([#55133](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089433593)).
* Fixed an issue where the **Destructive** commit **Diff** was including more components than selected ([#54795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088780309)).
* Fixed an issue where a merge got stuck for a long time and the **Commit ID** was reflected in **BitBucket** but unavailable to select for release label deployment ([#52964](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087060140)).

#### 13 November 2022 <a href="#id-13-november-2022" id="id-13-november-2022"></a>

**(ARM v22.1.33)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was trying to create an **Extract** process in **DataLoader** but after validating the query the application was throwing an error: `not supported; requires @DynamoDBTyped or @DynamoDBTypeConverted` ([#54648](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088630160)).
* Fixed an issue with **CI Jobs** where **External Credential** metadata was not identified during **Deployment** ([#53939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087955144)).
* Fixed a UI bug where user was performing an **org to org deployment** using **package.xml** file and the components were successfully deployed and also verified on Salesforce target, but the status on ARM was still **In-Progress** ([#50459 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375)and [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue with **DX CI Jobs** where user is not getting details of faulty commit revisions in the notification ([#54063](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088015242)).
* Fixed an issue with **Profile Manager** where the deployment is not showing any progress in the logger detail in front end. It was updated only after completion of the deployment job at backend ([#53706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704963)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed a bug where **Merge Commit** validation was not considering special characters like %,#, etc. as a value and throwing the following error: `Merge comment should not contain an empty space` ([#54512](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088479003)).
* Fixed an issue where ARM was slowing at different phases in the **EZ-Commit** module ([#50503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084910726)).
* Fixed an issue where Git check response was not delivered for validation **CI Job** even though user has added the comment for a **Pull request** in the remote repository ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).

#### 06 November 2022 <a href="#id-06-november-2022" id="id-06-november-2022"></a>

**(ARM v22.1.32)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DX CI Job** where user selected **Do Not Include Skip Members** but the respective mapper reports were not skipped (internal ticket).
* Fixed an issue where the **Deployment** module page was loading very slowly and then thrwing an error: `Page Unresponsive` ([#53675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704191)).
* Fixed the following issues in **CI** and **Reports** modules (internal ticket):
  * Build With **NULL ERROR** (issue exists both with Proxy and without Proxy)
  * SF Org Code coverage Execution is failing (issue exists both with Proxy and without Proxy)
  * Jenkins Build is updated with **FAILED** status even after it is successfully completed (issue exists only without Proxy)
  * Checkmarx text is not displaying the **Proxy Configuration** note (Only With Proxy)
* Fixed an issue with **QA Environments** where user was unable to create and delete the **SFDX module** because of the **Apache config CACHE** settings (internal ticket).
* Fixed an issue with the **Deployment** module where user initiated a **Deployment** without selecting the **Do not Include Skip Members** option, but this option was auto-enabled and skipped the member at the time of deployment ([#53747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087811296)).
* Fixed an issue with **Modularization** where user creating a module and selected the **Ignore installed components** check box but the installed components were not ignored causing the deployment to fail ([#53703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087755311)).
* Fixed an issue with **AccelQ Test Automation** where test case fails but the error details pop-up is not showing the details of the error that caused the failure ([#54224](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088281589)).
* Fixed an issue where user is setting up the **Apex PMD rules** as **Priority 1** & **Priority 2** in the **CI Job** but the SCA Report is showing the **Priority 3, P4 & P5** which wasn't selected ([#54017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087969396)).
* Fixed an issue where the **Git** check response was not delivered for a validation **CI Job** ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).
* Fixed an issue where the **Deleted Report** metadata components were not found in the **EZ-Commit** ([#53119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087247293)).
* Fixed an issue where user was trying to perform a **Quick Merge** but was getting an **Undefined** error for all labels (internal ticket).

#### 30 October 2022 <a href="#id-30-october-2022" id="id-30-october-2022"></a>

**(ARM v22.1.31)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where triggering a **CI Job** in **Objects** was resulting in an ambiguous error in the **CI Job Build** ([#53066](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087190013), [#52955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087099268), [#53631](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087579265)).
* Fixed an issue where all **CI Jobs** were failing and throwing the error: `Validation Checking failed Version Control Mappings not found for Repo: SA Repo and Branch: bugfix/Bugfix_PQT_Rel_Validation` ([#52945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087098136), [#52950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087101272), [#52757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086925007)).
* Fixed a UI bug on the **CI Jobs** page for **Install an Unlocked or Managed Package from a Version Control Branch** type where old **Dev Hub**dropdown list was displayed in the **Deploy** section (internal ticket).
* Fixed an issue with **AccelQ** where running a test execution was successful even before the jobs were completed in AccelQ, but the status was always showing as **Not Run** instead of **Success** or **Failure** even if the jobs have been successfully completed ([#50181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084509148)).
* Fixed a **Page Unresponsive** issue while creating a new **Release Label** by adding a feature to list limited results on each page ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where a merge got auto-approved and was in **Merged Not Commit** status ([#52398](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086586845), [#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed an issue where user created a **Release Label**, performed a **Merge** operation, committed changes to the target branch, and created two revisions in the **Github** branch.\
  But ARM was throwing an error while applying merge stage and only on the revision generated ([#51364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085859319)).
* Fixed an issue where **EZ-Commit** initiation was stuck with the error: `Unable to fetch Salesforce Org users. Reason: Invalid login: invalid user name or password or security token or api version or user locked out` ([#52550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086834002)).
* Fixed an issue where user was not able to select the orgs in the **EZ-Commit** drop down ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001), [#51219](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085620605)).
* Fixed an issue where **Page Size** value on the **Edit Release Label** screen is defaulting to the previous value instead of the set value (internal ticket).
* Fixed a UI bug where **OK Button** in **Automation** is not visible in the **Create Release Label** pop-up when opened in 100% zoom (internal ticket).

#### 23 October 2022 <a href="#id-23-october-2022" id="id-23-october-2022"></a>

**(ARM v22.1.30)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **CI Job** was successful but was including components from **GIT revisions** from old deleted branches ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a production deployment using CI job for an object, but it failed with the following error: `Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field` ([#48626](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082749181)).
* Fixed an issue where **CI Job** was getting an exception, **Build** status was showing as _successful_, but **Scratch Org** not getting created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **Managed Package** was picking the wrong ancestor by adding a feature to manually select the preferred ancestor while creating a package version ([#48311](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223305)).
* Fixed an issue where user was adding **URLs** to the **Proxy Configuration Settings** but the **URL List** was not reflecting the same (internal ticket).
* Fixed an issue where **Custom Template Creation** failed and the **Logs** did not record the reason for failure ([#52147](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086277150)).
* Fixed an issue where the **Created By** value was not visible in **Dataloader**, **Dataloader Pro DL Config**, and the **TestEnv History** page (internal ticket).
* Fixed an issue where the **Comment Box** was not accepting more than **100 characters** while rejecting a **Commit**, but was working as expected while approving a commit ([#51384](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085891476)).
* Fixed an issue with **Apex Test Class Config.** in **SF MGMT ORG** where the **Fetch Current Set**, **Add Manually**, and **Auto Populate** options were throwing an error: `Error 200` ([#52408](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086578687), [#52328](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086485900)).
* Fixed an issue where user set **Commit validation Criteria** to **Auto reject after 7 days** but the older Pre-validation commits are not auto rejected after 7 days ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user cannot add **Skip** members manually and it is failing due to **special characters** being included ([#53139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087266642)).

#### 16 October 2022 <a href="#id-16-october-2022" id="id-16-october-2022"></a>

**(ARM v22.1.29)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where skipped members were present in many components but only **Report Metadata** was failing during **Deployment** ([#51040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085433814)).
* Fixed an issue where **CI Job** was getting stuck in **In Progress** status but the log showed that the deployment was successful ([#51140](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085583019)).
* Fixed an issue where GitHub login credentials were not working when user triggered a CI Job for the second time ([#50630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085136003)).
* Fixed an issue where CI Job has failed in the Salesforce org, but still stuck in **In Progress** status in ARM ([#50435](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084823763)).
* Fixed an issue where user raised a **Pull request** on a branch and was getting a webhook response, but CI Job build was not triggered ([#51592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085996953)).
* Fixed a UI bug where **Add to dashboard** button was unavailable for widgets ([#52333](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086514169)).
* Fixed an issue where a new database file is created and overwritten with an existing database file whenever the server was restarted (internal ticket).
* Fixed an issue where user was trying to resolve conflicts on **Merge Request Labels** created more than 7 days ago, but application was throwing an error: `undefined` (internal ticket).
* Fixed an issue where **Custom Email Template** was not working for **Email notifications** ([#47484](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080506162)).
* Fixed an issue where user was testing **SSH Connection** but the application was throwing an error: `invalid privateKey` ([#50940](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371198)).
* Fixed an issue with **nCino** where **UI Log** was not generated for failed CI Jobs ([#50442](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084795478)).
* Fixed an issue where **New EZ-Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue where **Audit Logs** were not generating via **Postman Services** ([#50221](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084545179)).
* Fixed an issue where **Commits** were getting stuck and throwing the following error: `No credential have been found with Name:git`, but was not reflecting in the UI log ([#51713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086127001)).
* Fixed an issue with **Workspace Settings** where unused workspaces were not being cleared despite selecting **Clear all workspaces which are not used in last 7 days** ([#50164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084481079)).
* Fixed an issue where user was performing a **Prevalidation EZ-Commit** and found that some **Layout Assignments** were deleted though those layouts were not part of the commit ([#50945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371456)).
* Fixed an issue with **nCino** where migration was failing due to errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).

#### 09 October 2022 <a href="#id-09-october-2022" id="id-09-october-2022"></a>

**(ARM v22.1.28)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **nCino** where user was getting errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).
* Fixed an issue where user noticed discrepancy in the **Conflict Resolution Log** ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).

#### 02 October 2022 <a href="#id-02-october-2022" id="id-02-october-2022"></a>

**(ARM v22.1.27)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where components were successfully deployed, but deployment status was still showing **In-Progress** in ARM ([#50459](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375), [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where CI Jobs were getting stuck and throwing the following error: `Too many open files` ([#44319](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001), [#49273](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001)).
* Fixed an issue where **email notification** wasn't sent for some of the **CI Jobs** ([#48028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081639899)).
* Fixed an issue where the Custom label and remote site setting URLs were not getting updated by ARM through **Environmental Provisioning** ([#49612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083684001)).
* Fixed an issue with **Vlocity** where selecting one component from a GIT repository was causing all the components from the category to get selected ([#49806](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084007005)).
* Fixed an issue with **ALM Mgmt.** where item status was not retrieved properly for **Merge Request**, but was working as expected for **EZ-Merge** ([#50628](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085133005)).
* Fixed a UI bug where **Release Labels** were showing duplicate **Time Stamps** ([#51205](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085689003)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected after 7 days as the user had configured under **Commit Validation Criteria** ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user was getting an error pop-up on the **Permissions** and the **SF ORG MGMNT** pages, and the SF org and VC repo mappings were lost in the profile section of a role ([#49108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083164265)).

#### 26 September 2022 <a href="#id-26-september-2022" id="id-26-september-2022"></a>

**(ARM v22.1.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** test job was throwing an error while in queue ([#49797](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083986945)).
* Fixed an issue where scheduled auto-sync of external commits was not working (internal ticket).
* Fixed an issue with the **New EZ-Commit** screen where **ALM Types** are changing to old ALM type names after resaving details on the **ALM Management** screen (internal ticket).
* Fixed an issue with **Pre-validation merge** where the **Object** file content was empty in the **CodeScan Analysis SCA** report (internal ticket).
* Fixed an issue with **Branching Baseline** where some of the custom object metadata nodes were deleted from the repository ([#47239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080102001), [#47270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080113166)).
* Fixed an issue with **EZ-Merge** where **Diff** was not being generated even though there were file changes between the source branch and the destination branch ([#50323](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084689471)).
* Fixed a UI bug in **DataLoader** where user was switching from **Graphical View** to **Grid View** but **Graphical View** options were still being displayed ([#50431](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084822478)).
* Fixed an issue with **nCino** where the **Insert/Update With Null Values** option was not getting updated for CI jobs ([#50259](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084641005)).
* Fixed an issue where users were unable to **re-authenticate** the **Salesforce Org** after refreshing their personal sandboxes ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001)).
* Fixed an issue where **Environment Provisioning Template** was not functioning as expected for **Custom Labels** containing URL ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue with **EZ-Commit** where user was trying to deploy **Permission Sets** and **Profiles** together, and the pre-validation process was stuck in **In-Progress** status ([#49340](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083456001)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected as configured ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).

#### 19 September 2022 <a href="#id-19-september-2022" id="id-19-september-2022"></a>

**(ARM v22.1.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed multiple issues with **CodeScan<>ARM** Integration (internal ticket).
* Fixed an issue where **CI Jobs** and **Deployments** were both failing for **Reports** and **Dashboards** because the folder could not be found (internal ticket).
* Fixed an issue with **New Commit** screen where the **Select All** checkbox was getting unselected when navigating from the **DELETED** tab to the **ADDED/MODIFIED METADATA COMPONENTS** tab and back to the **DELETED** tab (internal ticket).
* Fixed an issue with **Version Control Prevalidation Commit** where for the selected **Custom Metadata** and **Permission Set**, **Diff** was being generated as expected but the **Deployment** was failing (internal ticket).
* Fixed an issue with **Version Control Prevalidation Merge** where SCA report was empty, and throwing the following error in the console: `Uncaught TypeError: Cannot read properties of undefined (reading 'length')` (internal ticket).
* Fixed an issue where user was unable to reset the AutoRABIT password, and was getting an error: `getAttribute: Session already invalidated` ([#50145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084391472)).
* Fixed an issue where **CI Jobs** was not picking the right number of components unless the user cancelled the build and retriggered it ([#47164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921675)),([#46981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079504156)).
* Fixed an issue where the user tried to merge to the Dev branch but the **CI Job** failed and was throwing a **Duplicate** error ([#49661](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083729177)).
* Fixed an issue where user was trying to install **Unlocked Package** via **CI Job** but it was failing and throwing the following error: `ERROR 178928269770891:275 - For input string: "0-2" java.lang.NumberFormatException: For input string: "0-2"` ([#50093](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084341003)).
* Enhanced **Vlocity** loggers for **Branching Baseline** by displaying to the user **Status Count** of **Remaining**, **Success**, **Error** and **Ignored** (internal ticket).
* Fixed an issue where **Test Connection** was failing on the **Version Control Summary** page under the **Admin** module ([#49299](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083372346)).
* Fixed an issue with **Prevalidation Merge** by increasing the **SCA Response timeout** from **50 minutes** to **5 hours** ([#48613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082720068)).
* Fixed an issue where merging **Master Branch** with the **Production** branch was throwing the following error: `No merge head specified` ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed a bug where **New A-Z Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue with **Autorabit Commit Label** related to **Permission Sets Deployment** ([#48709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082892203)).

#### 11 September 2022 <a href="#id-11-september-2022" id="id-11-september-2022"></a>

**(ARM v22.1.24)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was selecting a single package to import, but all available package versions were being imported ([#49426](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083542359)).
* Fixed an issue with **Profile Manager** where user was comparing a profile but the deployment was not starting ([#48620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082696017)).
* Fixed an issue where deploying components with profiles was not working as expected and throws the following error: `Duplicate layoutAssignment:PersonAccount (PersonAccount.Person_Prospect)` ([#49021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083082001)).
* Fixed an issue where custom metadata records were not being selected during deployment ([#49167](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083203846)).
* Fixed an issue in **Version Control Commit Labels** history where **Created By** and **Created Date** values were exchanged (internal ticket).
* Fixed an issue where user was getting an error while trying to deploy **Vlocity Metadata** using **CI Jobs** ([#47568](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080830005)).
* Fixed an issue where **Branching Baseline** was not retrieving **Workflow Metadata types** ([#49403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083447017)).
* Fixed an issue where **Release Label** failed to load revisions from a particular branch and the browser was hanging and throwing an _Out of memory_ error ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where **EZ-Commit** was not getting auto-rejected when **CodeScan** analysis failed, even though user select the option to run **Static Code Analysis** ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).
* Fixed an issue where merge was failing at the **Validate Deploy** step even before selecting the org to validate ([#49724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083898393)).
* Fixed an issue where **Layout** was being removed from the **Diff** while deploying **Profile** changes with related **Layouts** and **RecordTypes** ([#48268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082045983)).
* Fixed multiple issues with **CodeScan<>ARM** Integration ([#49605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083671017)).

#### 04 September 2022 <a href="#id-04-september-2022" id="id-04-september-2022"></a>

**(ARM v22.1.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing a new deployment but getting an error when using the **Compare Orgs & Deploy** button ([#48707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860460), [#48676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860003), [#48737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082918005), [#48734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082914003)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.NullPointerException: null` ([#48706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860315)).
* Fixed an issue where few fields were not being analyzed in CodeScan SFDX. User was selecting Custom Fields, Apex Classes, and Record Types in E-Z Commit, but Static Code Analysis was only Apex Classes ([#48547](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082584398)).
* Fixed an issue where dashboards and reports were changing to **Destructive** and getting deleted ([#48119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081915009)).
* Fixed an issue where discrepancies for **Document**, **Assignment Rule** and **AutoResponseRule** metadata types content was observed in **package.xml** for SFDX and non-SFDX CI Jobs ([#47017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079534439)).
* Fixed an issue where the Dataloader Pro Jobsfailing and throws the following error: `java.lang.NullPointerException: null` ([#49170](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182317), [#49283](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083331025), [#49331](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083407003), [#49199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182597)).
* Fixed an issue where nCino CI Jobs via RBC were failing during parallel deployment. Instead of falling in queue, the first job was failing while the other succeeded, and the user had to retrigger the failed job ([#47335](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080272507)).
* Fixed an issue where creating multiple deployment jobs from the same source org to the same destination org for different templates, the jobs were failing with **Null Pointer Exception** error (internal ticket).
* Fixed an issue with **DX Pre-validation merge** where **Destructive Deployment** for custom labels failed without any errors (internal ticket).

#### 28 August 2022 <a href="#id-28-august-2022" id="id-28-august-2022"></a>

**(ARM v22.1.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Unpackaged Packages Directory** folder was being created in the **Deployment Promotion** zip package when deploying **Static Resource Metadata type** using **Single revision DX Deployment** (internal ticket).
* Fixed an issue where after upgrading the AR instance, deployment jobs kept removing the custom metadata access on the **Permission Sets** ([#48296](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082147005)).
* Fixed an issue where **Org difference** jobs were running for more than 24 hours ([#48324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223730)).
* Fixed an issue where Environment provisioning template was not working when trying to update custom label values that contain URL, and the incorrect value was being updated in the org ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue where choosing the **Select Manually** option while doing a commit was resulting in a blank screen for the **Deleted** tab (internal ticket).
* Fixed an issue where while doing Prevalidation commit in AR, **Commit Only Permissionsets For The Selected Metadata** functionality was not working properly for both DX and Non-DX cases (internal ticket).
* Fixed an issue in Dataloader where an **Undefined Error** was displayed when user was trying to create and save the **Screens Template** (internal ticket).
* Fixed an issue where user was trying to validate the commit using single revision, but was getting an **Empty Package** error even though there were changed files in the commit ([#47530](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080730150)).
* Fixed an issue where DataLoader Pro jobs were failing with an error **duplicate value found: SetupOwnerId duplicates value on record with id** for the custom setting **Multichannel\_Settings\_vod\_\_c**, even though there is no field mapped with name **SetupOwnerId** ([#48230](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081981779)).
* Fixed an issue where the **search** functionality was not working in Dataloader Configuration as well as Dataloader Test Environment Setup (internal ticket).
* Fixed an issue where EZ Commit Logs and Change Labels were not displaying for some of the commit labels ([#45364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076464250)).
* Fixed an issue where the user was not able to see the deployment report because the build was failing when only custom fields were being selected without the related object ([#45663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077048275)).
* Fixed an issue where merge request was being auto rejected if the selected approver was no longer with AR ([#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed a bug where user had enabled Squash and Merge while performing a new merge, but the Squash and Merge option was not displayed after the Merge Request was approved ([#48246](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082046388)).
* Fixed an issue in CI Jobs deployments where Bulk API option for **Attachments** was throwing an error (internal ticket).
* Fixed an issue where **nCino CI Jobs** were failing the first time and completing the second time successfully ([#46545](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644141)).

#### 21 August 2022 <a href="#id-21-august-2022" id="id-21-august-2022"></a>

**(ARM v22.1.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI job build was getting stuck in **In-progress** status ([#47934](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081483565)).
* Fixed an issue where **RunSpecifiedTest** level execution was failing with Test classes dependency errors ([#47666](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081029378)).
* Fixed an issue where DX CI Job build failed if document metaxml change commit revision includes in the build \[Including Email templates and Static Resources types] (internal ticket).
* Fixed an issue where entire branch merge was failing with multiple common ancestor errors ([#47334](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080237436)).
* Enhanced the Dataloader history screen (internal ticket):
  * Column mover added to table column alignment for text view.
  * Moved **Last Run** details to the **Date/Time** column.
* Fixed an issue where Standard fields are not retreiving when included in **package.xml**, and retrieving through **E-Z Commit (Package Manifest)** option ([#47961](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081505333)).
* Fixed an issue for the **nCino CI Jobs** were failing due to default selection of **AutorabitExtId\_\_c** in **Mappings** (internal ticket).
* Fixed an issue for the nCino Deployments where even if **LookupKey** is available, by default **Name** is selected in **External ID Mapping** (internal ticket).
* Fixed an issue for the nCino CI Jobs where **Attachments** were failing due to **External Mappings** not being set to the **NAME** field (internal ticket).
* Added the feature to dynamically handle the respective nCino Prefix rather than depending on the JSON file to identify the External Id field

#### 14 August 2022 <a href="#id-14-august-2022" id="id-14-august-2022"></a>

**(ARM v22.1.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushed with special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).

#### 07 August 2022 <a href="#id-07-august-2022" id="id-07-august-2022"></a>

**(ARM v22.1.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the package URL was not visible for the SFDX modules successfully configured in ARM (internal ticket).
* Fixed an issue where our internal team members got the undefined error while creating a new scratch org and selecting the module (internal ticket).
* Fixed an issue where after triggering the CI job, the **File Changes** and **Check-ins** results mismatched ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue where the package created to deploy ExperienceBundle misses some of the folder and metadata files contained in it ([#46692](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079024001)).
* Fixed the below deployment-related issues:
  * Unable to find commits that are part of a Release Label while performing a new deployment ([#47337](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080246444))
  * Unable to retrieve components from a Release Label during deployment ([#47534](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080713440))
  * Changes are not deployed to the destination org which are part of a Release Label ([#46908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079358877))
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).
* Fixed an issue where the deployment failed to initiate when search and substitute rules are selected ([#47802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081320007)).
* Fixed an issue where the status log .csv files are inconsistent for deployment via CI jobs (internal ticket).
* Fixed an issue where the users were unable to process the migration of RBC object (nForce\_\_Views\_\_c) using the nCino CI jobs, feature template migration, or the Dataloader Pro jobs ([#47098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079761055)).
* Fixed an issue where while deploying a **nCino-User Interface** template, only partial records are deployed and no deployment logs are generated ([#47494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080488668)).
* Fixed an issue where the users, while performing an EZ-Commit by enabling the run SCA option, the CodeScan analysis is getting failed, but EZ-Commit is not getting auto-rejected ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).

#### 31 July 2022 <a href="#id-31-july-2022" id="id-31-july-2022"></a>

**(ARM v22.1.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Upgraded the Spring and AWS libraries on ARM for addressing the Spring vulnerability ([#46970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079471289)).
* Fixed an issue where the users were unable to login to ARM via SSO (internal ticket).
* Fixed an issue where the ARM is not able to fetch any component using the release label ([#46662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078894834)).
* Fixed an issue where the baselining of branches has wiped out the records types for many records, and the users were forced to do manual changes to the Record types ([#42719](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072309163)).
* Fixed an issue where the ARM allows to associate only one branch to one package, and not able to build beta package versions from various branches. This is now fixed ([#46841](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262193)).
* Fixed an issue where the CI job, while deploying manage packages, is installing all the manage packages instead of installing a single package ([#46832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262054)).
* Fixed an issue where the links on the **CI Job log** screen are redirected to the user's login page instead of redirecting to user's Salesforce org screen ([#47151](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079912283)).
* Salesforce API version 55 (Beta support) is upgraded. The label is modified throughout ARM application to Salesforce API version 55.0 ([#47404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080386152)).
* Duplicate classes from the ARM repo has been removed (internal ticket).
* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushedwith special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the merge was getting failed with the following error: `Fetch operation is failed due to some runtime exceptions from Git` ([#46773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079094055)).
* Fixed an issue where the username and passwords fields were not editable for users registered in ARM with basic authentication ([#47099](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079788018)).

#### 24 July 2022 <a href="#id-24-july-2022" id="id-24-july-2022"></a>

**(ARM v22.1.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when user triggers a code coverage run in the production environment, the action takes more time than expected. Also, the total time taken for the task completion is shown inaccurate in the log report ([#44544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040590), [#43527](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073512143)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.OutOfMemoryError: Java heap space` ([#47182](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988001), [#47190](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988142), [#47209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080017264), [#47191](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079950166)).
* Fixed an issue where the **Rollback settings** were not getting saved in the **My Account** page (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue with the permissionsets where instead of delta changes, the Permissionset retrieving entire file from the branch and causing dependency issues ([#46846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262334)).
* Fixed an UI bug where the ARM application displays unwanted scrollbar when **"Exclude Installed (Managed) components"** is selected in the **My Account** page (internal ticket).
* Enhanced the ARM workspace feature to automatically unlock the workspace after sufficient time to run the workspace operations.
* Added the feature to set **Limit 0** option for the Dataloader Pro jobs. This limit will allow users to skip migrating child or Ancestors objects.
* Fixed an issue where while editing an existing nCino CI Job, the version control is not automatically choosing the previous repository set. This is causing the selected nCino Templates to reset ([#46952](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079432380)).
* Fixed an issue where the ALM labels were missing from the ALM Label lists page ([#44410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074860453)).
* Fixed an issue where the settings related with user permissions were erased ([#46472](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078507457)).
* Fixed an issue where the users when performed EZ-Commit using a package manifest file, doesn't include managed components that are in the **package.xml** file ([#47083](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079769291)).

#### 17 July 2022 <a href="#id-17-july-2022" id="id-17-july-2022"></a>

**(ARM v22.1.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the Execute Anonymous Apex metadata is not working as expected when configured as Environment Provisioning template ([#46817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079248146)).
* Fixed a bug where our internal team were able to use the perform the prevalidation commit and direct commit without giving the prevalidation commit label name and without commit comment, which are mandatory fields (internal ticket).
* Fixed an issue where the ALM workitems are not retrieved in CI job through merge (internal ticket).
* Fixed a bug where our internal team were able to save the **Install an Unlocked or Managed Package from a Version Control Branch** CI job even though Installation key were not uploaded which is a mandatory field (internal ticket).
* **\[Enhancement]** Added the Salesforce versions information in the logs for all Dataloader related jobs activities.
* **\[Enhancement]** Added the ability to delete a commit before it is pushed to your remote repository so that you have a choice to redo incorrect commits/ merges.
* Fixed an issue where the merge prevalidations were auto rejected with status as **Approval Pending** ([#46665](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078888152), [#46864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079289063)).
* Fixed an issue where the **Delete Commit** button was not seen after approving an EZ-Commit label (internal ticket).
* Fixed an issue where the toggle button for the dashboard metadata type in the commit label screen is not working as expected (internal ticket).
* Fixed an issue for the nCino Feature Deployments where the users were getting audit field issue when trying to deploy with `Insert/Update with Null Values` option (internal ticket).
* Fixed an issue for the nCino CI jobs using Spreads Templates where the users were getting `NullPointerException` error when trying to deploy with `Insert/Update with Null Values` option (internal ticket).

#### 10 July 2022 <a href="#id-10-july-2022" id="id-10-july-2022"></a>

**(ARM v22.1.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users failed to enable the pull request support for their version control repositories ([#46336](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078290172)).
* Fixed an issue where the re-use previously validated commit label takes more time to load ([#46171](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077992017)).
* Fixed an issue where the constructive changes are picked in the CI build, although no constructive changes are in-between _From_ and _To_ revisions (internal ticket).
* Fixed a bug marked deployment as failed, whereas the log report says successful ([#46737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079038631)).
* Fixed an issue with the SFDX job, where for the Report metadata type, the rollback feature was working weirdly (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue where entering the package installation key in `Install an Unlocked or Managed Package from Version Control Branch` CI Job gets altered when manually entered or pasted ([#46836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079265163)).
* Fixed an issue where the user could not run the static code scan report on GitHub with APEX PMD Lint Scanner metadata type ([#46781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079122007)).
* Fixed an issue with the CodeScan analysis report that failed when running from ARM ([#44404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074862389)).
* Fixed an issue where the user could not fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Enhanced the Dataloader Pro, where the attachments are now supported ([#41077](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299001)).
* Fixed a bug where editing the Dataloader job shows **"Job Group"** as _null_ or _empty_ (internal ticket).
* Vlocity has been upgraded to v1.15.5.
* Fixed an issue with the CI job where the version control using Salesforce with attachments was not picking the attachments during CI build (internal ticket).
* Fixed an issue with the EZ-Merge, where merging the main branch to the dev branch failed with a `No merge head specified` error ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed an issue that throws `Schema as invalid` error while running the branching baseline operation ([#46593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078805109)).
* Fixed an issue where the merge failed using a single revision ([#46491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644005), [#45764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077211038)).
* Fixed an issue where our internal team members could not create a new role from the **Admin** section (internal ticket).
* Fixed a bug where the `Invalid Schema` error is seen for non-SFDX prevalidation merge (internal ticket).
* Fixed an EZ-Commit issue where additional permissions were removed from Profiles metadata type, which is not a part of the commit ([#44543](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040441)).

#### 03 July 2022 <a href="#id-03-july-2022" id="id-03-july-2022"></a>

**(ARM v22.1.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment via CI job picked unnecessary components for deletion ([#44204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074533873)).
* Fixed the issue where the user when trying to delete a component in **Community** metadata type, deletes the whole Community rather than its components ([#43698](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073869007)).
* Fixed an issue where DevHub registration in ARM was failing ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed a bug where our internal team members were not able to view the Salesforce Org URLs in the **My Profile** section (internal ticket).
* Fixed an issue where the deployment using **Commit/Release Label** was not working ([#46419](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078496053)).
* Fixed an issue where the mapping more than one class to same test class is not recognized by ARM during commit/merge operation ([#46396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078430859), [#45159](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076223139)).
* Fixed an issue where the CI job builds were failing because of missing revisions ([#45532](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076855001), [#46352](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078378003)).
* Fixed an issue where the **Compact Layout** were not getting deployed and throws undefined error([#46592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078798022)).
* Fixed an issue where the ALM statuses were not updated/rolled back post CI job rollback completion ([#45945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077581145)).
* Fixed an issue where the destructive changes were not working as expected for the CI jobs ([#46216](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049311)).
* Fixed an issue where the ARM failed to update the Audit fields when trying to run nCino feature deployment ([#46356](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078401001)).
* Fixed an issue where our internal team were not able to register their credentials on one of the ARM SAAS instances ([#46315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078239277)).
* Fixed an issue where prevalidation commits were getting failed due to credential issues. The following error was thrown `No credentials found` ([#46274](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078213003), [#46098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077754153)).
* Fixed a bug where the deleted components were tagged as **UC (UnChanged)** instead of **D (Deleted)** in the EZ-Commit ([#46087](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077760173)).
* Fixed an issue where the metaXML file were not retrieved for the ContentAsset metadata type for the **SFDX "Entire Branch"** merge case (internal ticket).
* Fixed an issue where the deployment validation were failing for the prevaildation merge with the error: `No source backed components present in the package` (internal ticket).
* Fixed an issue where the merge using single revision (baseline revision) receives the metadata schema error ([#46570](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078699087)).
* Fixed an issue where the merges were getting failed and throws the `Schema is invalid for the file` error ([#45768](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077202614)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).

#### 26 June 2022 <a href="#id-26-june-2022" id="id-26-june-2022"></a>

**(ARM v22.1.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Spread Template** in the **nCino** module was not working as expected ([#45078](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076003188)).
* Fixed an issue where the user was getting `"field integrity exception: unknown (CreatedByID(0051X00000BbMIR) is not in org"` for the records that were available in the destination org.
* Fixed the issue where the **Disable Workflow** template in the **Environment Provisioning** module was not working as expected ([#46195](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049157)).
* Fixed an issue where the creation of a scratch org were getting failed. The fix has been deployed to in this weekly release ([#46021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690007)).
* Fixed an issue where the users were unable to use the **release label** for deployment ([#45415](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076584626)).
* Fixed an issue where the users were not able to register same DevHub with two different usernames ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed an issue where the CI Job was picking the deleted components from GitHub branch although the **Prepare Destructive Changes** checkbox was not selected. This caused the deployment to fail ([#42553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the users were not able to view their GitHub branches in the ARM application ([#46044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690473), [#46353](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078386013)).
* Fixed an issue where the CI Job for backing up from org to the version control branch was failing with null pointer exception error ([#45646](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the **EZ-Commits**, when included **Profile**, was not working as expected ([#45902](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077441170)).
* Fixed an issue where the commits were getting stuck at the delta stage ([#45101](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076070023)).
* Fixed an issue where the Git tags were being added to the queue but not being processed (internal ticket).
* Fixed an isse where the delta was getting failed in the **EZ-Commit** flow (internal ticket).
* Fixed an issue where the Dalaloader Pro job is failing with `Required field missing on "nCino_Screen__c" object`, however the user were able to view the `Screen__c` object has a value in their source org ([#45139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076158018)).
* Fixed an issue where the user were not able to save the Dataloader Pro jobs and throws the `JAVA.NullPointerException` error ([#46385](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078393786)).
* Fixed a bug where the users were not able to view the log reports after registering **Tags** via ARM (internal ticket).
* Fixed an issue where the tags creation got failed when the tag name contains **'error'** with custom API flow (internal ticket).

#### 19 June 2022 <a href="#id-19-june-2022" id="id-19-june-2022"></a>

**(ARM v22.1.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a minor bug where the child members checkboxes remained checked even when the parent metadata type was unchecked (internal ticket).
* Fixed an issue where CI job build **ToRevision** number was mismatched in the **CI Job Results** and the **CI Build Info** page ([#45580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076910037)).
* Fixed an issue where the request parameters were empty in the **nCino Feature Commit History** screen ([#45855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077344165)).
* Fixed an issue where the users while accessing the commits older than 30 days, ARM throws `Request parameters are empty/null` error (internal ticket).
* Fixed an issue where the users when accessing the **Commit History** page throws `Invalid FilterExpression` error (internal ticket).
* Fixed an issue where the user were unable to fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Fixed an issue where the **Diff report** in the **Merge Request** was not working as expected ([#45315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076389550)).
* Fixed an issue where the user ran the branching baseline operation by excluding the Managed package components, however, the **Package.xml** file still had all the managed package components listed in it ([#45125](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076117289)).
* Fixed an issue where the code coverage report was being generated at a different time than what was scheduled ([#45703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077145009)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).
* Fixed an issue where the TAF execution were getting failed (internal ticket).
* Fixed an issue where the **From Revision** was not visible when user access their CI job from **CI Job History** page (internal ticket).
* Fixed an issue that caused **Chrome** to crash anytime a user attempted to view the functional test results for the task of running a Selenium Maven test. The functional test results screen enters a continuous cycle of requests, which crashes the browser (internal ticket).
* Fixed an issue where the **skip members** feature of ARM was not working as expected (internal ticket).
* Fixed an issue where the user while performing **EZ-Commit** with SonarQube code analysis was getting failed with `Failed to run the sonar-scanner: null` error ([#46070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077717988)).

#### 12 June 2022 <a href="#id-12-june-2022" id="id-12-june-2022"></a>

**(ARM v22.1.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 05 June 2022 <a href="#id-05-june-2022" id="id-05-june-2022"></a>

**(ARM v22.1.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).

#### 29 May 2022 <a href="#id-29-may-2022" id="id-29-may-2022"></a>

**(ARM v22.1.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 22 May 2022 <a href="#id-22-may-2022" id="id-22-may-2022"></a>

**(ARM v22.1.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 15 May 2022 <a href="#id-15-may-2022" id="id-15-may-2022"></a>

**(ARM v22.1.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).

#### 08 May 2022 <a href="#id-08-may-2022" id="id-08-may-2022"></a>

**(ARM v22.1.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 01 May 2022 <a href="#id-01-may-2022" id="id-01-may-2022"></a>

**(ARM v22.1.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).
* Fixed an issue where the commits triggered in ARM shows a different author in Azure DevOps ([#44225](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074591143), [#43503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073518014)).
* Fixed a bug where selecting the "**Deployment**" icon after signing in to the ARM application caused the user to log off and on and return to the home page ([#44040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301863)).
* Fixed a bug where the check-ins display the wrong number of files changed during commit ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue in the TAF module where nothing pops up when you click on the "**View Log**" button ([#42020](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071114057), [#40284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067992205)).
* Fixed an issue where the users while accessing the help center from ARM application, receiving the **({"result":"failure","cause":"E105 - Request Delayed"})** error ([#43579](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652168)).
* Fixed a bug where the commits was getting failed due to SCM (Software Configuration Management) authentication failure ([#42276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071577005)).
* Fixed a bug where the merge operations ran for more than 12 hours and later failed ([#38755](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065037173), [#42874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072544001), [#38913](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065383003)).
* Fixed an issue where extra metadata members are picked up for the profile component during the EZ-Commit process ([#41361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069919263)).
* Fixed an issue where the users could not use commit template for the deployment ([#43995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074325045), [#43586](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073635324), [#43905](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074163310), [#43407](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073339003)).

#### 24 April 2022 <a href="#id-24-april-2022" id="id-24-april-2022"></a>

**(ARM v22.1.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 17 April 2022 <a href="#id-17-april-2022" id="id-17-april-2022"></a>

**(ARM v22.1.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue for the Chrome browser where the ApexPMD ruleset was not uploading incorrectly (under the **Plugins** section). For other browsers, it was working as expected ([#42954](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072670003)).
* Fixed the issue with the merge where the changes present in the source branches were not picked up, and therefore latest changes did not reflect on the destination branch ([#43553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073610001), [#43598](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073662177), [#43595](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073653614), [#43593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652863), [#43591](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073629096), [#43580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652300), [#43574](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073651134)).
* Fixed an issue where the Salesforce-DX deployment and rollback mismatches ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040))
* Added the criteria to trigger the callout URL post-deployment. If you set it to _success_, the callout URL is activated if the salesforce deployment is successful ([#38990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065571472)).
* Enabled feature flag settings to select between classic ARM and Salesforce CLI process to generate package manifest.
* Fixed an issue where the commit validation is successful for an empty field, whereas the CI job fails ([#43324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073218067)).
* Fixed an issue where the deleted metadata components were showing under the **"File Changes"** tab but did not appear under the **"Destructive Changes"** column while carrying out a manual deployment ([#41670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070494027)).
* Fixed Dataloader Pro job issue where the job is completed successfully without loading all ancestors/master objects data to the destination environment ([#43276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073123039)).
* Fixed branching baseline issue where all metadata from the production org were not copied to the version control repo/branch ([#42938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072633029), [#42685](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072244001), [#42955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072644308), [#42445](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071818001), [#43038](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072780490), [#42753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072314347), [#42242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071424143), [#42766](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072375048), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed the below nCino issues:
  * Unable to proceed with feature deployment using an existing community feature migration template due to the following error: **"No External Id field exist in source org."** This is now fixed and working as expected ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
  * Non-template records were being picked up during nCino deployment.
  * Non-template records are fetched in the dataset.
  * Spread Statement Record failing with the error **“Missing Statement Types.”** This is now fixed.

#### 10 April 2022 <a href="#id-10-april-2022" id="id-10-april-2022"></a>

**(ARM v22.1.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Abort** option was showing for completed CI jobs ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463), [#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed the issue where the SFDX deployment is getting failed even though the user uploaded the correct file.
* Fixed a bug where the static code analysis (SCA) status shows as **in progress** for a failed execution.
* Fixed an issue where deleting a custom field was affecting other custom objects where the globalpicklistvalue is shared by multiple objects ([#42782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072370556)).
* Fixed a bug where the users were not able to view specific values under the standard value sets in the **New EZ-Commit** screen ([#41773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070686445)).
* Fixed a bug where the **New EZ-Commit > Deleted Component** tab throws a null error on expanding the metadata types.
* Fixed a bug where the deploying records via record based configurations (RBC) was throwing error: **"No external Id field exists in the source org"** ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
* Fixed an issue where creating a new nCino feature migration template takes longer than expected ([#41855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070869289)).
* Addressed out of memory (OOM) and other performance issues in this weekly release.

#### 03 April 2022 <a href="#id-03-april-2022" id="id-03-april-2022"></a>

**(ARM v22.1.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option where not working when users use the EZ commit/ Merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 March 2022 <a href="#id-27-march-2022" id="id-27-march-2022"></a>

**(ARM v22.1.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** in the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the exclude metadata types in the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).

***

## ARM Release Notes **21.6**

**Date of Release:** _**21 November 2021**_

**On this page:**

1. [New Features](./#new-features)
2. [Enhancements](./#enhancements)
3. [Improvements](./#improvements)
4. [Changelogs](./#changelogs)

### New Features <a href="#new-features" id="new-features"></a>

#### Pull Request Support for Azure DevOps <a href="#pull-request-support-for-azure-devops" id="pull-request-support-for-azure-devops"></a>

Pull request is a feature that allows you to review code and provide feedback before merging it into the master branch. Previously, we had GitHub and Bitbucket support. We've included support for Azure DevOps in this release. ([Learn More](../../../product-guides/arm/arm-features/version-control/external-pull-request/pull-request-support-for-azure-cloud.md))

* During **Ez-Commit** and new **Pull Requests**, you can now create a Pull Request in Azure with the assignee.
* You should be able to choose the repository, the base branch, and another branch to compare during the creation of a pull request.
* A link to the Azure DevOps application will be included in each pull request created in AutoRABIT. The pull request can also be approved directly from the AutoRABIT application.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### Audit Log Report <a href="#audit-log-report" id="audit-log-report"></a>

AutoRABIT had an audit report feature that gave you a comprehensive view of your business operations by fostering a collaborative operational audit environment. In this release, we've made some enhancements and added a button called **"Audit Log Report"** on the CI job page, which allows you to generate a report in PDF format for a specific period.

* We've improved the **CI Job Result** screen by giving users the option to generate an Audit log report for internal auditing purposes. This is a report of CI jobs deployments and the commits associated with each deployment, including commit details such as Author, Commit Time Stamp, and so on.
* We changed the timestamp in the Audit log report from **12-Hour** format to **24-hour UTC** format by default to comply with ISO 8601 notation, which is a commonly recommended format for representing date and time.
* Added support for custom _“keynames”_, _“Salesforce Org type“_ and _“AR SF Org type”_ in the Audit trail report wherever Salesforce org name details are applicable.

#### **Salesforce CLI Upgrade** <a href="#salesforce-cli-upgrade" id="salesforce-cli-upgrade"></a>

Salesforce CLI is a command-line interface for working with your Salesforce org that makes development and build automation easier. It can be used to create and manage organizations, synchronize sources to and from organizations, create and install packages, and more. In this version of ARM, Salesforce-DX CLI is upgraded to the latest **7.129** version.

#### **Salesforce Winter (API 53) Support** <a href="#salesforce-winter-api-53-support" id="salesforce-winter-api-53-support"></a>

In order to keep our product up to date with the most recent Salesforce updates. AutoRABIT now supports the most recent **API version 53** in this release. Now our Salesforce developers will begin using API 53 on their Sandboxes for development. The most recent API version is intended for customizing the metadata model and developing tools to manage it.

### Improvements <a href="#improvements" id="improvements"></a>

#### Platform Improvements <a href="#platform-improvements" id="platform-improvements"></a>

* We've been working hard over the last few weeks to improve our platform's stability, performance, query optimizations, code smells, security vulnerabilities, and reliability. With this release, you will notice significant improvements in our application, such as faster page load times, improved performance, and faster search functionality, among other things.
* **JQuery Upgrade**: JQuery was updated from version **1.8.3** to version **3.6**. Upgrading to the most recent version of jQuery makes our application more secure, as well as potentially faster in terms of script execution and loading.

#### **UI Improvement** <a href="#ui-improvement" id="ui-improvement"></a>

Across the CI Job module, **"Load More"** buttons have been replaced with **"Previous"** and **"Next"** buttons. This new feature will allow our users to display 25, 50, 75, or 100 records on a single page and navigate between pages using the Previous and Next buttons. This feature was previously limited to the Version Control module, but it has recently been expanded to include the CI Job module as well.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 11 Mar 2022 <a href="#id-11-mar-2022" id="id-11-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to deploy release labels ([#40600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068395530)).
* Fixed the following SSO errors:
  * Unable to use SSO for AutoRABIT authentication ([#37767](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062637173)).
  * Unable to log in via SSO in the chrome and the firefox browser.
  * Fixed "**domain name does not exist**" error ([#41853](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070865403)).
* Fixed a bug where users were getting an undefined error for the standard templates while editing the CI job.
* Fixed an issue where the status of the AutoRABIT ExternalId field was showing as processing, but it was marked as completed in the log report ([#40669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068569430)).
* Fixed a bug that restricted users from using Dataloader Pro's **Auditable Standard** field feature ([#40794](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068711163)).
* Fixed an issue where the users were unable to replace attachment records in the destination org.
* Fixed an issue where the attachments were not completely deployed in the target environment ([#41208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069667003)).
* Fixed an issue where users were unable to deploy the nCino feature from org to org using the **nCino-Forms** **standard template** ([#38764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065055277)).
* Fixed an issue where the users were unable to **stop/delete** the data loader running jobs ([#39556](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066791149)).
* Fixed an issue where the users when attempting to initiate the deployment, were failing with the **"Failed to initiate deployment request"** error ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to perform the branching baseline operation ([#41622](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070417055)).
* Fixed an issue where the users were not able to configure the approver's lists on the **New Merge Request** screen ([#41844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070874003)).
* Fixed an issue where the users trying to revert a commit for a commit label was getting failed ([#39613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066805855)).

#### 06 Mar 2022 <a href="#id-06-mar-2022" id="id-06-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option was not working when users use the EZ-Commit/merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for the EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 Feb 2022 <a href="#id-27-feb-2022" id="id-27-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** on the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the excluded metadata types on the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for the Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).
* Fixed an issue where the users when trying to start a deployment, it was getting failed with the "**Failed to start deployment request** error" ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to revert the commits using AutoRABIT ([#39957](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067378384)).
* Fixed an issue where the users were not able to use the "**Files Changed**" functionality on the **Merge Request History** page ([#41456](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070069155)).
* Fixed an issue where the users were unable to delete the changes made in the version control branch via AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed a bug that prevented users from performing commit and merge operations in AutoRABIT ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where the external objects with lookup relationships were not getting displayed under the child objects in the Dataloader Pro ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed an issue where the users were unable to update the "**Validation checks**" status from the in-progress state to the completed state.
* Fixed an issue where changes from multiple package directories were not being retrieved without selecting a package directory.
* Fixed an issue where the users were unable to attach the CSV file while carrying out the CI deployment.
* Fixed an issue that caused users to receive an invalid session error when changing their password.

#### 20 Feb 2022 <a href="#id-20-feb-2022" id="id-20-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to see the commits ID in the release label ([#41284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069797001)).
* Fixed an issue where the users were unable to view their permission details in the Users and Roles tab ([#41043](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069219179)).
* Fixed an issue where users were not able to delete the changes made in the source branch using AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed an issue where the branching baseline for a profile and branch to branch merge was not working ([#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* There was an AutoRABIT performance issue that caused searching for revisions, validations, and commits to taking a long time. It has now been fixed ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where users were not able to commit their changes to the branch ([#39269](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066103022)).
* When users attempted to update changes in the target org using the profile manager, the deployment getting failed. It has now been fixed ([#40599](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068421379)).
* Fixed an issue where users were unable to switch from a credential-based login to an SSO-based login ([#40871](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068784190)).
* AutoRABIT instances were not supporting the Salesforce API 54 version. It has now been fixed. ([#40921](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068957023)).
* When a user performs a pre-validation commit on the Azure repository branches, it creates a duplicate external commit with the same revision ID. This issue has now been fixed ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).

#### 13 Feb 2022 <a href="#id-13-feb-2022" id="id-13-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **"Group By"** functionality was not fetching the correct CI job results ([#38870](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069460109)).
* Fixed an issue where the deployment status of CI Job has failed in logs but the process is still in-progress stage ([#40805](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068697958)).
* Fixed an issue where the users were unable to use the SCA for LWC components unlike apex class, triggers, and aura bundle ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* When a pull request is in progress, the job is not triggered for additional changes committed before the work is completed. This is now fixed ([#38877](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065276358)).
* Fixed a bug where the users were facing challenges while merging the entire branch changes to the target environment ([#39451](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066611145)).
* Fixed an issue where the File Diff shows full component (especially Aura, LWC components) as a change instead of delta changes ([#39351](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066320276)).
* Fixed a bug where the sub-users without admin privileges were able to export and download the org users' data from **Admin > Users** section.
* Fixed an issue where the data loader pro throws the error **"Error creating output directory: configs"** while uploading data from one environment to another ([#40832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068736307)).
* Fixed an issue where the external object-related lookups were unable to verify the relationship associated with the external objects in the destination org ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed a minor user-interface bug where the users were unable to find the **Resolve Conflict button** to resolve the merges conflict. This is now resolved.

Limitations identified in this release:**RestrictionRule** metadata type is not supported for the SFDX deployment.

#### 06 Feb 2022 <a href="#id-06-feb-2022" id="id-06-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed the below UI issues:
  * The **"Commit"** button was not available for the merge request label job. ([#38876](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065275014)).
  * For the entire deployment, the **"To Revision"** radio button was disabled, and users were unable to select revisions from the list provided.
  * Although the field **"Timezone"** was mandatory upon signup, the users were able to proceed without picking a timezone.
* Fixed an issue where the admin was unable to assign permissions to its sub-users. This is now working as expected ([#40017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067565003)).
* Fixed an issue where the validation rule automation was not working for the **Environment Provisioning** module ([#41035](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069198519), ([#40991](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069108736)).
* Fixed an issue where the data loader pro job is not able to load data for objects with fields exceeding limits([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the users were unable to register the existing branches to AutoRABIT ([#40894](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068809067)).
* Fixed an issue where the EZ-Merge was showing status as failed in the AutoRABIT application however, in the Salesforce environment the status shows as success ([#40673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068536502)).
* Fixed a bug where the users were unable to register a dev hub on the **SDFX > Hub Management** page.

#### 30 Jan 2022 <a href="#id-30-jan-2022" id="id-30-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 29 Jan 2022 <a href="#id-29-jan-2022" id="id-29-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 23 Jan 2022 <a href="#id-23-jan-2022" id="id-23-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to generate the code coverage log report from the **Report** Module ([#38717](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939344)).
* Fixed an issue where the users were unable to upload the package.xml file to resolve the merge conflict ([#39960](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067372236)).
* Fixed an issue where the users were able to commit the changes although the validation got failed. ([#38228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775343)).
* Fixed an issue where the user was unable to perform the **Enable/Disable validation rule** on the Managed package object using the environment provisioning functionality ([#40297](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068017532)).
* Fixed a bug where the user was unable to deploy the **Email Template** on their target environment ([#40241](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067922013)).
* Fixed an issue where users were unable to upload/migrate the knowledge articles from one sandbox to another sandbox ([#37922](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063030291)).
* Fixed an issue where the users were facing the **"Null Pointer Exception"** error during the merge prevalidation process.
* Fixed an issue where If the users picked all the conflicted files during a merge request, they would receive an error message saying **"Please click on any conflicted file."**
* Fixed an issue where the users were unable to find the log report for the newly created branch in AutoRABIT.
* Fixed an issue where the users were unable to find out the work item statuses during the deployment process for the unlocked packages.
* **ALM Enhancements:**
  * Added a new section called **"ALM Management"** to the **Admin** module for merge requests
  * Detailed information on all of your ALM's active and inactive sprints.
  * Smart commits to reading the comment in a revision associated with your ALM story.
  * We have introduced the **ALM Details** section that lists the work items linked with the commits along with the existing and post-merge status.
  * Ability to keep the work item status without a change or update it during EZ-Commit.
  * You may now configure the job to pick up revisions based on your work item status while deploying from version control to a Salesforce org, allowing you to adjust the status even after a successful rollback.

#### 16 Jan 2022 <a href="#id-16-jan-2022" id="id-16-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 09 Jan 2022 <a href="#id-09-jan-2022" id="id-09-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 02 Jan 2022 <a href="#id-02-jan-2022" id="id-02-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI Job builds are getting stuck and no log information was displayed ([#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed an issue where the conflicted files downloaded were incorrect during the merge process ([#39364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066317317)).
* Fixed an issue where the aura components were not getting retrieved while carrying out the branching baseline operation ([#38610](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064710558)).
* Fixed a bug that restricted users from entering the credential name on the **"Create Credential"** screen because the field was disabled.
* Fixed a bug where the super administrator was getting an empty popup screen when navigating to the **Process Summary** page.
* Fixed an issue where the users were able to find the **Abort** option even when the CI Job had been completed successfully ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463)).

#### 26 Dec 2021 <a href="#id-26-dec-2021" id="id-26-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as the parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 19 Dec 2021 <a href="#id-19-dec-2021" id="id-19-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 12 Dec 2021 <a href="#id-12-dec-2021" id="id-12-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when the user is trying to perform pre-validation commit for report metadata, it is getting added under emailservice functions in diff report ([#37925](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063067009), [#38581](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064666105), [#38880](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065272149), [#38734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064981980)).
* Fixed an issue where the case _entitlementProcess-meta.xml_ files were not picked up during deployment ([#39069](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065734191), [#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed an issue where the deployment report is getting failed while doing prevalidation merge with the report folder.
* Fixed an issue where users were unable to retrieve a package which has more than 1000 components ([#38737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064985007)).
* Fixed a bug where a null pointer exception was thrown while loading in Dataloader Pro ([#38286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063928003)).
* Fixed an issue where the entitlement process is getting removed from Package.xml ([#39097](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065777009)).
* Fixed an issue where the external commits did not show up on the release label ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed a bug that displays the wrong statuses in the test reports ([#39008](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065572975), [#38986](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564303)).
* Fixed an issue where the code coverage percent is not available in the case of SFDX merge operation.
* Fixed an issue where the data loader pro jobs were not able to load data for objects with fields exceeding 800 ([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the code coverage percentage shows as 0 in the UI logs even after deployment validation is passed.
* Fixed a bug where the changes are being committed even after a failed validation.
* Fixed an issue where the package directory filter in the release labels is not working as expected.

#### 05 Dec 2021 <a href="#id-05-dec-2021" id="id-05-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when pre- and post-destructive changes were added to the process, it caused the deployment to fail ([#38330](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064040175), [#38721](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064967175)).
* Fixed a bug where for fewer CI jobs, the **Older** button was disabled. This has now been enabled and is working as expected ([#39050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065702042)).
* Fixed an issue in the SFDX module that prevented commits from being executed using scratch org ([#38789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076258)).
* Fixed an issue where the external commits were not displayed when creating release labels or merging single revisions. This is now working as it should ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed an issue where users were unable to run SCA within the reports module due to an error stating **"Invalid mapping credentials."** In addition, the number of issues indicated in the Ez-commit process does not match the CodeScan analysis ([#38917](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065373386)).
* Fixed a bug where single data loader jobs couldn't be edited and there was a mapped field cache issue ([#38753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065026084)).
* Fixed an issue where the alm mapping details for the scratch org with alm configuration could not be found.
* While executing scratch org alm commit with skip mapping set to false, the current ALM work item status was reporting _"empty"_ results. This is now fixed.
* Fixed a bug that allowed users to save multiple criteria rows with the same priorities for ApexPMD.
* Fixed an issue where the repository filter on the _Commit History_ screen was reset to default after resolving a conflict.
* Fixed a bug where the failed component count position is wrong when the window is scrolled.

#### 28 Nov 2021 <a href="#id-28-nov-2021" id="id-28-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed nCino objects deployment issue during using nCino CI Jobs ([#39375](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058591003)).
* Fixed an issue where the custom object is being listed during CI Job operation but not during Ez-commit ([#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed Ez-merge issue which shows different results in AutoRABIT when compared to the production environment ([#38831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065181230)).
* Fixed an issue where the users were unable to extract deleted records and threw **"Malformed Query Fault"** error ([#38448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064441154)).
* Fixed an issue where the pull request support with BitBucket was not working properly. This is now fixed ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed a bug in the merge request and pull request validation builds which were unable to list the changed components whereas the CI Job build was able to pick them up ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017), [38713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064936484)).
* Fixed an issue where the org administrator was unable to assign hub level permissions to its sub-users ([#38898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065336005)).
* Fixed wrong metadata identification for deletion issue ([#37703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062453147)).
* Fixed an issue where the user was unable to update **"Configuration For recordTypes picklistValues"** ([#38901](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065355005)).
* Fixed API version error in the CI Job screen ([#36550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059178003)).
* Fixed CI build failing issue ([#38630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064788278)).
* Fixed EZ-Commit issue where the file diff was throwing an error due to credential scope issue ([#38950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065446001), [38795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065077341)).
* Fixed an issue where duplicate entries were seen while creating release labels ([#37300](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061440253)).
* Fixed a bug where the user was unable to click on the **OK** button on the **Merge Request History** screen ([#38781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085003)).
* Fixed an issue where the **"include delete records"** checkbox is de-selected automatically during editing the data loader extract job.
* Fixed an issue where the scratch org permissions are not visible on **"hub level permissions"** and _"_**scratch org permissions"** screens.
* Fixed Ez-commit issue where a sub user with only one repository registered with AutoRABIT, is not able to find/select his repository in the **EZ-Commit** screen.
* Fixed an issue where the repository filter is reset to default during the conflict resolve flow.
* Fixed registering the branch issue when the branch registration crossed 100 limits in AutoRABIT.
* Fixed a bug where the parent checkbox in the download zip for CI Job is not working as expected.
* Fixed wave-dependent missing files from the package during the prevalidation merge operation.
* Fixed an issue where the non-SFDX CI job for WaveTemplates is showing no modifications when triggered.
* Fixed single data loader and data loader pro filter issues while carrying out the edit functionality.

#### 21 Nov 2021 <a href="#id-21-nov-2021" id="id-21-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the quick deployment feature was not working as expected and was throwing **"Invalid Login"** error ([#37802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062709159)).
* Fixed a bug where the merge request validation was getting failed ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017)).
* Fixed an issue where the commit search was not working as expected in the **Version Control** module ([#36548](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059165111)).
* Fixed an issue where the users were facing invalid credentials issue while updating the src as metadata folder path in-branch settings **(Admin > VC' Repos)** ([#38727](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939824)).
* Fixed an issue where the pull request support for BitBucket was not working properly as expected ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed an issue where the deployment shows failed status although there are no failures and the items did get moved to the destination org. This is now working as expected ([#37774](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062644015), [#38363](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064201151)).
* Fixed an issue where the user was not able to retrieve the metadata to deploy the changes using AutoRABIT's deployment feature.
* Fixed data loader pro issue which was throwing unknown error while migrating the data objects ([#38566](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064649001)).

***

## **ARM Release Notes 21.5**

**Date of Release:&#x20;**_**29 August 2021**_

**On this page:**

1. [Enhancements](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#enhancements)
2. [Changelogs](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#changelogs)

In keeping with our dedication to continual improvement, the **August-21 (AR 21.5)** release delivers a plethora of exciting upgrades and improvements to our AutoRABIT application.

### Enhancements <a href="#enhancements" id="enhancements"></a>

* **UI/UX Improvements:** Focused on application performance and user experience. Try it out for yourself and let us know how to feel:
  * **Page Navigation:** When working with several records, breaking data into multiple pages is always a good idea. You can now view 25, 50, 75, or 100 records on a single page, and use the **Previous** and **Next** buttons to switch to the previous or next page. This feature is now only available in the Version Control module, but it will be expanded to other modules in future releases.
  * **Never miss a required field:** You will be prompted to fill in all the required fields before you proceed. Follow the UI highlights to minimize rework.
* **Customize CI jobs for desired Salesforce API versions:** To support different Salesforce API versions for distinct Salesforce orgs instead of a global setup, we've added a new checkbox named **Salesforce API version** across the CI Job module. This will offer a granular facility in a CI job to select the required Salesforce API version.
* **Improved Audit Trail Report:** Additional data was added to the reports to support improved report analysis.
* **Performance Improvement:** Waiting is always boring- we have reduced that wait for you.
* **Salesforce CLI Upgrade-** Salesforce CLI upgraded to the latest stable **7.112** version.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 14 November 2021 <a href="#id-14-november-2021" id="id-14-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed deployment issues
  * Fixed an issue where no metadata was found while validating the components from the master branch to the production environment ([#38612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064709627), [#38587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064645657), [#38571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639413), [#38537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064517581), [#38552](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064584042), [#38549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064544537))
  * Fixed revision based deployment issue ([#38386](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064283007))
  * Fixed an issue where the commit labels changes are not reflected in the release label ([#38569](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064646158))
  * Fixed an issue where the salesforce deployment from GIT to SFDC was not working ([#38558](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639001))
  * Fixed deployment issue where no components were being retrieved via _Single Revision_ or _Revision Range_ ([#38550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064581003), [#38546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064558188))
* Fixed a bug where the deployment CI Job occurs multiple times ([#37454](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061960003)).
* Fixed the search and substitute deletion rule issue ([#38410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064291165)).
* Fixed SFDX parent and child job triggered the issue.
* Fixed an issue where the review artifact with AutoDraft functionality was not working properly in the EZ-commit screen.

#### 07 November 2021 <a href="#id-07-november-2021" id="id-07-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141))
* Fixed SFDX deployment and rollback mismatches issue ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040)).
* Fixed a bug where when attempting to commit the deletion of 19 profiles, a Diff Report listing of 20 profiles was generated. ([#38303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063932311)).
* Fixed code coverage report discrepancy issue ([#36282](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058168335)).
* Fixed an issue where the wave template related dependent files were missing from the package \[CI, Deployment, VC].
* Fixed an issue where all existing credentials for version control mappings that were created using the **Profile** screen were reset.

#### 31 October 2021 <a href="#id-31-october-2021" id="id-31-october-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* The deleted sharing rules were not showing up in the EZ-Commit Deleted tab, which was fixed ([#37747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062586019))
* Fixed a bug where the older commits were not accessible for merge ([#38242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063785008)).
* Fixed an issue where when deploying a new custom object, an error _"Profile Search Layout: - System Administrator - not appropriate for object XXXXXX"_ was thrown ([#37897](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062972201)).
* Fixed a merge conflict issue([#37950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063128003)).
* Fixed a commit label issue ([#38275](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063874030)).
* Fixed an issue with SSO where users had to log in twice before being able to use the AutoRABIT application ([#36634](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059319963)).
* The issue with the SSO domain has been fixed ([#37232](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061168477)).
* Fixed data loader audit logs issue ([#37688](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062385762)).
* Fixed an issue where the users were unable to exclude _EmbeddedServiceLiveAgent_ from CI Job ([#38261](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063818321)).
* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141)).
* Fixed an issue where users were unable to compare profiles using the _Profile Manager_ feature in the _Deployment_ module ([#36978](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060367023)).
* In CI Jobs, a bug with the _"Group By"_ filter was fixed ([#38132](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063522197)).
* Fixed an issue where the community site was not getting deployed ([#38226](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775199)).
* Fixed a bug that caused metadata retrieval to fail with a **Null** error during revision range deployment.
* \[Profile Manager] Fixed an issue where the org compare feature would not work when three orgs were configured, resulting in a "Empty screen" error.
* \[Profile manager] Fixed an issue where after comparison, duplicate metadata entries and empty popups were displayed.
* \[nCino CI Jobs] Fixed an issue where the unwanted objects are displayed on editing the cloned CI Job.
