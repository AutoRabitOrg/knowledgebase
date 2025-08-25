---
hidden: true
---

# Release Notes 25

## Release Notes 25.2.7 <a href="#title-text" id="title-text"></a>

**Release Date: 24th Aug 2025**

Highlights: Fixes to EZ-Commit translations, webhook API token status, and rollback iterations.

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

1. EZ Commit – Case Values Removed from CustomObjectTranslation\
   Resolved an issue where case values were being removed from the CustomObjectTranslation file when performing multiple EZ-Commits under Japanese language. The problem was caused by unmarshalling and marshalling logic comparing values incorrectly. The comparison logic has been updated to rely on additional fields to properly support translations for different languages.\
   (Support Case: 142756)
2. Webhooks – API Token Last Access Not Updating\
   Fixed an issue where webhook API tokens continued to display “Never Accessed” even after recent runs triggered by CI jobs. The backend logic has been corrected to update and display the last access time accurately.\
   (Support Case: 149685)
3. Rollback – Iteration and Components Not Available After Revert\
   Addressed an issue where rolling back a previously deployed iteration caused both the iteration and its components to disappear. A change event has been added to ensure iterations and components are available after a revert rollback.\
   (Support Case: 150209)

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
