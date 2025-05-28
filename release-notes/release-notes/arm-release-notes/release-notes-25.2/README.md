# Release Notes 25.2

## Release Notes 25.2.6 <a href="#title-text" id="title-text"></a>

**Release Date: 25 May 2025**

**Overview**

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
