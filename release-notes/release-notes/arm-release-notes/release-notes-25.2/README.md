# Release Notes 25.2

## Release Notes 25.2.3

### Release Notes 25.2.3

**Release Date:** 04 May 2025

***

#### Overview

This release of **AutoRABIT ARM** introduces key bug fixes and stability improvements to deployment label handling, CI job webhook executions, and user management across regions. Notably, a critical internal issue affecting metadata filtering during full deployments has been addressed. Additionally, issues related to saving users for countries without state-level details and CI job webhook failures have been resolved.

#### Bug Fixes and Improvements

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

### Release Notes 25.2.2

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

Refer to the latest release notes published for nCino + Data Loader at [https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes](https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes).&#x20;

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
