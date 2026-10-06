# Release Notes 25

## ARM Release Notes 25.4.13

**Release Date: 28 December 2025**

**Support Case: #150240**

Resolved an issue where the Delta step was incorrectly marked as failed during commits despite successful completion. The fix improves delta handling for new repositories across Custom API and Non-Custom API (JGit) flows, impacting EZ-Commit, Merge, Release Label, Deployment, and CI Jobs.

**Support Case: #165779**

Fixed an issue where the validation deployment report was not visible for a failed CI job build due to a missing deployment Async ID. The backend logic has been updated to handle such exceptions gracefully, ensuring deployment reports are displayed correctly in CI Job deployment reports

**Support Case: #161304**

Resolved an issue where CI jobs did not detect picklist value name changes even when _Include Picklist Modifications_ was enabled. Backend logic has been updated to correctly track picklist value changes based on manageable states, ensuring CI jobs now pick up these updates reliabl**y.**\
\
**Support Case: #161295**

Fixed an issue where scheduled CI jobs for rebasing hotfix and pre-prod branches consistently failed due to a null pointer exception. The update improves CI job stability by correctly handling backup-to-VC flows with auto-switch to bulk retrieve service when metadata governor limits are hit, including support for Custom Objects and Custom Fields.

***

## ARM Release Notes 25.4.12

**Release Date: 21 December 2025**

**User Story:  Commit Retrieval Issue**

We’ve introduced a new **feature flag** that allows customers to continue using the **legacy “Select Manually” behavior** in EZ Commit.

When this feature is enabled, selecting **“Select Manually”** will retrieve **all detected changes across all authors**, regardless of the author selected in the user interface. This helps support existing workflows that depend on the earlier behavior for managing metadata dependencies.

If the feature is not enabled, EZ Commit will continue to behave as it does today, retrieving changes only for the selected author.

**Support Case: #172610**

Subject: EZ Commit – Package Manifest Selection Fix

We fixed an issue where component selections made using **“Select All”** in the Package Manifest flow were reset when navigating between pages. Selections now persist correctly across all pages, improving bulk commits for larger packages in both **Autodraft** and **Package Manifest** workflows.

**Support Case: #169831**

Subject: Deployment Logs Display Restored After Quick Deploy

We fixed an issue introduced after the instance upgrade where **deployment logs were not visible in the UI** following a **Quick Deploy**. Customers can now view both **validation and deployment logs** as expected, restoring full visibility into deployment activity.

**Support Case: #169858**

Vlocity Component Selection Warning Fixed

We fixed an issue where a misleading warning message, **“Please select at least one metadata type or member,”** was shown during Vlocity component deployments after users selected all members of a metadata type and then deselected a few. The selection logic has been improved to correctly reflect user choices and prevent this unnecessary warning.

***

## ARM Release Notes 25.4.11

**Release Date: 14 December 2025**

**Internal Ticket:**

**Fix for Duplicate Deployment Logs in Org Sync History:**\
Resolved an issue where performing actions like _Add to Destination Org_ or _Delete from Destination Org_ followed by _Synchronize Orgs_ with **Validate Deploy** enabled resulted in duplicate deployment logs for the same label. The system now correctly generates a single log per deployment.

**Internal Ticket:**

**Fix for Team Name Validation and Warning Message:**\
Addressed an issue where an empty warning message appeared and the feature did not work in both the old and new UI. Validation has been enhanced to ensure team names cannot contain spaces, and the warning message now displays correctly.

**Internal Ticket:**

**Fix for Merge Criteria Validation in Merge Settings**\
Resolved an issue where merge settings could be saved even when no merge criteria options were selected. The system now correctly prevents saving unless at least one option is chosen when merge criteria are enabled, ensuring proper validation.

\
**Support Ticket: #161454**

**Fix for Field Persistence Issues When Editing CI Jobs:**\
Resolved an issue where editing a CI Job with a configured Parallel Processor caused certain fields to clear unexpectedly and triggered validation errors. Additionally, updating the Baseline Revision previously cleared the Package Directory. The **Client ID**, **Client Secret**, and **Access Token URL** fields now persist correctly, and the editing workflow functions as expected.

\
**Support Ticket: #158630**

**Fix for Incorrect File Count and Missing Metadata in EZ Commit Code Scan**\
Addressed an issue where EZ Commit using **“Only Newly Added Supported Metadata Types”** produced inaccurate scan results. Some metadata types—such as Custom Fields and Permission Sets—were not included in the static code analysis, and the SCA logs always reported **“Total number of files identified for static analysis: 1”** regardless of the actual count. The logic has been updated to correctly include Custom Fields and Permission Sets during analysis and to display an accurate file count in the logs.

***

## ARM Release Notes 25.4.10

**Release Date: 7 December 2025**

* Resolved an issue where the **IgnoreWarnings** flag from the UI was not passed correctly, causing prevalidation to fail on warnings even when the checkbox was selected. Updated the UI request mapping so the correct value is stored and processed by the backend.\
  Support Case: #160228
* The issue preventing users from selecting the **Release Label** and other options in the **Change Label** module under VC has been resolved by updating the routing mechanism to `router.go`, restoring proper navigation from both the left menu and top bar.\
  Support Case: #172715

***

## ARM Release Notes 25.4.9

**Release Date: 30 November 2025**<br>

* Fixed an issue where scheduled jobs could not be deleted through Environment Provisioning. The system now correctly validates permissions and job eligibility, enabling successful scheduled job removals from target environments.\
  Support Case: #159287
* A performance optimization was implemented to improve how UserVersionControl details are retrieved. Instead of fetching data individually for each user, the system now retrieves the required information in a single bulk operation and processes it efficiently. This significantly reduces load time and restores a responsive user experience in EZ-Merge.\
  Support Case: #158633

***

## ARM Release Notes 25.4.8

**Release Date: 23 November 2025**<br>

* EZ-Merge report timestamps now adjust accurately to each user’s time-zone settings, ensuring Merge Submission, L1 Review, and L2 Review dates display consistently across regions.\
  Support Case: #156046
* CI Job validation behavior has been streamlined so that the Build Now option becomes available in the UI whenever the job’s deploy and overall status reach a completed state, providing a more consistent experience.\
  Support Case: #158357
* Backup-to-VC jobs now present the appropriate Git message during push scenarios, such as permission or hook restrictions, while clearly indicating “No modifications” only when no updates are present—offering more accurate visibility into job outcomes.\
  Support Case: #159296
* Delta commit results now reflect completion accurately, ensuring that the commit status aligns with the actual execution of the delta operation.\
  Support Case: #150240

***

## ARM Release Notes 25.4.7

**Release Date: 16 November 2025**\
\
**Highlights**: Improved downstream CI chaining, expanded Agentforce support, optimized EZ-Commit performance, and key platform upgrades.

\
**Downstream CI job chaining enhancement**\
AutoRABIT now allows downstream CI jobs to trigger even when a parent job completes without identifying artifacts during the delta build process. This removes unnecessary pipeline breaks, eliminates manual intervention, and ensures uninterrupted job chaining, especially for Vlocity and other metadata patterns where no-change builds are common. (This would be available basis only on feature flag).\
\
**Expanded Agentforce metadata support**\
ARM now supports a wider set of Agentforce metadata types across CI, Deployments, and Version Control flows.

| **Agentforce Metadata Type**                         | **Supported** |
| ---------------------------------------------------- | ------------- |
| GenAiPromptTemplate                                  | Yes           |
| GenAiPromptTemplateActv                              | Yes           |
| GenAiPlugin                                          | Yes           |
| GenAiFunction                                        | Yes           |
| GenAiPlanner (API 60 to 63)                          | Yes           |
| ​GenAiPlannerBundle (API 64 and Above)               | Yes           |
| Bot                                                  | Yes           |
| BotVersion                                           | Yes           |
| Custom Apex invoked by agents (ApexClass)            | Yes           |
| Flows used by agents (Flow)                          | Yes           |
| Permission Sets assigned to the Agent User           | Yes           |
| CustomSite                                           | Yes           |
| Network                                              | Yes           |
| DigitalExperienceBundle                              | Yes           |
| EmbeddedServiceConfig                                | Yes           |
| MessagingChannel                                     | Yes           |
| Flow (specifically the Omnichannel flow for routing) | Yes           |
| Queue                                                | Yes           |
| QueueRoutingConfig                                   | Yes           |

\
**Rollback failure fix for DX CI Jobs involving consecutive RecordTypes and StandardValueSets**\
A rollback issue caused DX CI Jobs to fail when only RecordTypes and StandardValueSets were selected but CustomLabels were excluded, resulting in a “not found in package.xml” error. The rollback logic has been updated to respect user-selected members, ensuring successful rollback operations even when other components are omitted. Destructive rollback continues to exclude RecordTypes due to Salesforce API limitations.\
(Support Case: 155931)

**EZ-Commit in-flight fetch optimization**\
Introduced an in-flight check to prevent repeated fetch calls during EZ-Commit table data loading. The update adds a fetch-state tracker, improves the loading indicator, stabilizes table rendering to occur only after a successful fetch, and resets state cleanly on errors resulting in faster UI responsiveness and reduced redundant API calls.\
(Support Case: 155994)

**Tomcat upgrade to version 11.0.13**\
ARM’s application runtime has been upgraded to Tomcat 11.0.13, delivering improved security, better performance, and alignment with the latest Java ecosystem standards.\
(Support Case: 158573)

***

## ARM Release notes 25.4.6&#x20;

**Release Date: 9 November 2025**\
\
**Highlights**

Salesforce is deprecating the **username + password + security token** method for SOAP API integrations. To ensure compatibility with **API version 65**, ARM now supports **OAuth (JWT) authentication**.

This release also includes:

* Support for **Salesforce Metadata API v65**
* A new **CodeScan Configuration Wizard** for simplified setup
* Enhanced audit visibility with **CEF login logs**
* Fix for **CaseTeamRole** handling of multi-word names in environment templates

**Limitation:** OAuth (JWT) is currently supported only for **Salesforce Dev Hub**. Regular Salesforce orgs continue to use **OAuth 2.0 Web Server Flow**. Other authentication methods are not supported in this release.\
\
**Salesforce SOAP Login Deprecation Notice**\
Salesforce has deprecated the “username + password + security token” authentication method for integrations using the SOAP API starting with version 65. This legacy method will be completely disabled by Summer ’27 for API versions 31–64. Customers using this method in AutoRABIT connections (e.g., \{{ConnectionName\}}) must migrate to OAuth authentication to ensure uninterrupted connectivity.

\
**Salesforce Metadata API Version 65 Support**\
ARM now supports Salesforce Metadata API version 65, ensuring full compatibility with the latest metadata structures introduced by Salesforce. As part of this release, ARM has validated several metadata types across both DX and Non-DX environments, enabling consistent retrieval, validation, deployment, and CI/CD operations.

| Metadata Type            | Supported | Verified |
| ------------------------ | --------- | -------- |
| LightningOutApp          | Yes       | Yes      |
| InvocableActionExtension | Yes       | Yes      |
| PresenceDeclineReason    | Yes       | Yes      |
| PresenceUserConfig       | Yes       | Yes      |
| QueueRoutingConfig       | Yes       | Yes      |
| DuplicateRule            | Yes       | Yes      |
| AnalyticsVisualization   | Yes       | No       |
| SrvcMgmtObjCollabAppCnfg | Yes       | No       |
| DgtAssetMgmtProvider     | Yes       | No       |
| DgtAssetMgmtPrvdLghtCpnt | Yes       | No       |

**CodeScan Configuration Wizard for Repository and Org Mapping**\
Introduced a guided configuration wizard for CodeScan integration to simplify project and branch mappings across ARM repositories and Salesforce orgs. The system now intelligently pre-matches existing CodeScan projects and branches, allows users to persist mappings, and ensures consistent baseline comparisons across Commit, Merge, CI Jobs, Custom Deployment, and SCA modules. This minimizes redundant project creation and improves scan relevance.\
\
**CEF Logger Added for Login Events**\
ARM now logs both successful and failed user login attempts through the Common Event Format (CEF) logger, improving traceability and compliance visibility for system administrators.\
(Support Case: 156220)

**Environment Provisioning Template – Multi-Word Case Team Role Names**\
ARM now handles the creation and execution of environment provisioning templates containing multi-word CaseTeamRole names (e.g., “VMI Specialist”, “Supply Chain Finance”). The template execution correctly supports full role names and ensures accurate reflection in the target Salesforce org.\
(Support Case: 154640, 152188)

***

## ARM Release Notes 25.4.5

**Release Date: 2 November 2025**\
\
**Highlights:** Improved validation visibility, enhanced deployment reliability, and Data Cloud DevOps support introduced.

### Enhancements <a href="#enhancements" id="enhancements"></a>

**Data Cloud DevOps Support**\
Introduced full support for Salesforce Data Cloud metadata deployment using DevOps Data Kits. Users can now commit, validate, and deploy Data Cloud components such as Data Streams, Data Model Objects, Calculated Insights, and Data Packages through EZ-Commit, Deployments, and CI Jobs.

Key highlights include:

* Deployment support for **DataPackageKitDefinition**, **DataSourceBundleDefinition**, **DataStreamTemplate**, and **DataKitObjectDependency**.
* Strict separation between Data Cloud and standard Salesforce metadata for packaging.
* Prerequisite checks for permissions and Data Cloud-specific access.
* Recommended DX repository usage and manifest-based commit flow for Package.xml-dependent metadata.
* Support for both constructive and destructive changes across DX and non-DX repositories.
* Validated Merge, Release Label, and Branching Baseline flows for all Data Cloud metadata types.\
  \
  _&#x4C;earn more_ [_https://knowledgebase.autorabit.com/product-guides/arm/salesforce-extensions/arm-for-salesforce-data-cloud_](https://knowledgebase.autorabit.com/product-guides/arm/salesforce-extensions/arm-for-salesforce-data-cloud)

### Bugs <a href="#bugs" id="bugs"></a>

**Partial FlexiPage Commit Handling**\
Fixed an issue where FlexiPage metadata was partially committed during Prevalidation Commits, resulting in missing content during CI Job deployment. Added schema validation checks to ensure full FlexiPage integrity and introduced detailed logging for file uploads on the Review Artifact screen.\
(Support Case: 155665)

**App Deployment Failure in Profile Manager**\
Addressed a “Malformed request detected” error encountered during “Apps” deployment using the Profile Manager process. Deployments now complete successfully, and changes are accurately reflected in the target Salesforce org.\
(Internal)

**Validation Circle Color Accuracy During Code Coverage Failure**\
Resolved an issue in EZ-Commit where both validation circles appeared green even when Salesforce validation failed due to insufficient code coverage. The circles now correctly turn red when code coverage fails, ensuring accurate validation feedback.\
(Support Case: 154962)\
\
**Caching Issue in EZ-Commit AutoDraft Flow**\
In version 25.4.4, a cache-related issue caused errors when expanding metadata components in the AutoDraft step of the EZ-Commit flow. Users encountered the message “Cannot invoke 'java.lang.Comparable.compareTo(Object)' because 'k1' is null.”This issue has been resolved in the current release. Metadata components now expand and display their contents correctly without any errors.

***

## ARM **Release Notes 25.4.4**

**Release Date: 26 October 2025**\
\
**Highlights**: Improvements in EZ-Commit author handling, EZ-Merge responsiveness, and CI Job error reporting.

* **EZ-Commit Author-Specific Retrieval**\
  Resolved an issue where EZ-Commit was not correctly filtering metadata changes by the selected Salesforce Org Author. The process now accurately fetches only Author-related changes when a specific Author is chosen in both “Select Manually” and “Re-Use Previously Validated Commit Labels” modes.\
  (Support Case: 151097)
* **EZ-Merge Screen Freeze After Target Branch Selection**\
  Fixed a delay where the EZ-Merge screen froze for 14–17 seconds after selecting the target branch (“To” branch). The merge approver validation API (`/mergerevieweremail`) has been optimized with asynchronous handling to improve responsiveness during branch selection.\
  (Support Case: 155279)
* **CI Job Failure with No Error Displayed**\
  Addressed an issue where CI Jobs failed silently when component names contained dots and were misclassified under different component types (e.g., Profiles) in DX environments. The fix ensures accurate component handling and consistent error reporting for both DX and Non-DX CI Jobs initiated from Version Control to Deploy Org.\
  (Support Case: 155649)

***

## ARM **Release Notes 25.4.3**

**Release Date**: **19 October 2025**\
\
**Highlights**: Enhancements to metadata handling for destructive commits, standard value set retrieval, CI Job status accuracy, and Quick Deploy validation behavior.

* **UserAccessPolicy Deletion in Destructive Commits**\
  Destructive commits containing the 'useraccesspolicy' metadata type failed during execution. The metadata type has now been added to the SfdxMetadataFolder to ensure it is recognized for deletion.\
  (Support Case: 153113)
* **ContactPointUsageType Standard Value Set Retrieval**\
  ARM was unable to retrieve the "ContactPointUsageType" standard value set, which is associated with the "Contact Point Email" object. Since standard value sets cannot be fetched using describe calls, the metadata was added to the internal static list to ensure successful retrieval.\
  (Support Case: 154150)
* **Quick Deploy Criteria Validation for PR-Triggered CI Jobs**\
  Quick Deploy was unavailable after a successful Pull Request–triggered validation due to incorrect variable binding of the "preventDeploy" setting. The logic has been corrected, ensuring Quick Deploy remains unavailable when "Prevent Deployment" is selected under "Validate Deployment," matching expected behavior.\
  (Support Case: 153792)
* **ManagedContentType Destructive Commit Failure**\
  Destructive commits for MANAGEDCONTENTTYPE metadata were failing due to unrecognized metadata classification. This metadata type has now been added to the SfdxMetadataFolder, ensuring it is properly recognized and deletable.\
  (Support Case: 154888)
* **CI Job Status Stuck in Progress After Completion**\
  Some CI Jobs continued showing as “In Progress” even after build and validation completion, blocking new runs on the same target org. A blocking wait mechanism was implemented to continuously check CIJobInfo until the deploy status updates to “Completed.”\
  (Support Case: 154818)

***

## ARM Release Notes 25.4.2 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date**: **15 October 2025**\
\
**Highlights**: Stability improvements across CI Jobs, Commit handling, and Scratch Org creation.

* **CI Job Email Notifications – Missing Error Details**\
  Fixed an issue where CI job email reports did not display deployment failure details for Apex Classes. The notification logic now correctly includes all error and failed test details in the email report.\
  (Support Case: 154005)
* **Backup CI Jobs – Git Push Pre-Receive Hook Error**\
  Addressed a problem causing Backup CI Jobs to fail with the error “GIT Push remote update Result: pre-receive hook declined.” The exception is now taken care and the UI displays a simplified message: “No modifications exist.”\
  (Support Case: 154837)
* **EZ-Commit Validation – File Copy Failure**\
  Resolved a FileNotFoundException that occurred during EZ-Commit validation when a metadata file was missing from the source folder. The updated logic now skips missing files and continues copying remaining files, allowing the commit process to complete successfully.\
  (Support Case: 154753)
* **Scratch Org Creation – Salesforce Org Validation**\
  Resolved an issue where users received a “Salesforce Org Doesn’t Exist” error while attempting to retrieve data for Scratch Org creation. The system now correctly validates the selected Salesforce org and proceeds with successful data retrieval.

***

## ARM Release Notes 25.4.1 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date**: **5 October 2025**\
\
**Highlights:** Fixes for Quick Deploy iteration visibility, CI post-deploy log accuracy with DataLoader Pro, and complete Jira sprint retrieval across ALM flows.

* **Quick Deploy iteration visibility**\
  A validated deployment could be quick-deployed from a later iteration while the Quick Deploy button remained visible and usable on earlier iterations, which diverged from Salesforce behavior; this affected deployment iteration handling in the Deployments UI. Quick Deploy is now correctly disabled for the current iteration and all previous iterations once an actual deployment is performed, matching Salesforce semantics and preventing accidental re-deploys of validated iterations.\
  (Support Case: 150463)
* **CI job post-deploy logs and DataLoader Pro status accuracy**\
  CI jobs that triggered a post-deploy DataLoader Pro process sometimes showed a null error or incorrect "not yet run" status in post-activity logs even though the DataLoader Pro job executed and made changes in the org. We handled the null pointer and corrected status mapping between the DL module and CI logs; CI jobs now complete without the null error and post-activity logs reflect accurate in-progress and final statuses. The system also ensures the DataLoader Pro job is triggered and its final status is shown correctly.\
  (Support Case: 153953)
* **Jira sprint pagination and ALM updates**\
  Fetching sprints in new EZ-Commit, EZ-Merge, and CI Job flows was stopping after the first page because Jira API maxResults was 50, so not all sprints were returned. We now page through all results and surface every sprint across the UI, restoring full sprint visibility. Additionally, Jira ALM integration updates for status and comments have been improved so status updates and comments propagate correctly from ARM flows.\
  (Support Case: 154690)

***

## ARM Release Notes 25.3.12

**Release Date**: **28 September 2025**

* **Wavedashboard deployment failure due to xmd conversion**\
  When customers uploaded a package.xml containing wavedashboard type and members, ARM converted them to wavexmd and the deployment failed because the wavexmd files were missing from the zip. Implemented backend logic to prune xmd metadata entries when corresponding xmd files are not retrieved from the source org, preventing missing-file deployment errors.\
  (Support Case: 151073)
* **Email approvals bypassing branch access**\
  Users who had branch access removed could still approve merge requests via the merge validation email notification. Added an enforcement check for email-based approvals that validates destination branch permissions against the merge approval role; users without permission on the destination branch will no longer be shown as eligible approvers or be able to approve via email.\
  (Support Case: 153126)
* **Jira Work Items Not Retrieved from Sprints**\
  Fixed an issue where customers were unable to select Jira work items during ALM flows in EZ-Commit and Merge, with the error “No work items found in this sprint.” Jira had deprecated the API (v2) used by ARM to fetch work items, causing sprint data retrieval failures.\
  ARM now uses Jira API v3 for work item retrieval, restoring functionality across EZ-Commit, EZ-Merge, Merge Requests, and CI Jobs.\
  _(Support Case: #150934 & #151385)_

***

## ARM Release Notes 25.3.11.1

**Release Date**: **24 September 2025**

* **Jira Work Items Not Retrieved from Sprints**\
  Fixed an issue where customers were unable to select Jira work items during ALM flows in EZ-Commit and Merge, with the error “No work items found in this sprint.”
  * Jira had deprecated the API (v2) used by ARM to fetch work items, causing sprint data retrieval failures.
  * ARM now uses Jira API v3 for work item retrieval, restoring functionality across EZ-Commit, EZ-Merge, Merge Requests, and CI Jobs.\
    _(Support Case: #150934 & #151385)_

***

## ARM Release Notes 25.3.11

**Release Date**: **21 September 2025**

**Highlights**: Fixes for EZ-Commit folder retrieval, branch registration, SCA validation, and webhook API token updates.<br>

* **EZ-Commit – Report and Dashboard Folder Retrieval**\
  Fixed an issue where report and dashboard folders were not being retrieved when using a package.xml. Now, folders and their members are correctly retrieved during EZ-Commit, covering scenarios for both DX and non-DX repos, with and without Autodraft.\
  _(Support Case: 150181)_
* **Branch Registration – Default Branch Change**\
  Resolved an issue where the main default branch was unintentionally updated when registering a new branch for the first time. The default branch is now updated only if the current default branch does not exist in the remote repository.\
  _(Support Case: 149845)_
* **SCA Validation with Special Characters**\
  Fixed an error where SCA analysis failed when branch names or paths contained "/" or special characters. The fix covers EZ-Commit, EZ-Merge (including Pre-validation and Release Label merges), CI Jobs (Package from Version Control), Deployment (Version Control & Release Label), and Report Module.\
  _(Support Case: 152825)_
* **Webhook API Token Status**\
  Corrected an issue where the webhook API token’s last status always showed as "Never Accessed," even after being used in CI Job triggers. The last access status now updates correctly when tokens are used.\
  _(Support Case: 153909)_

***

## ARM Release Notes 25.3.10.1&#x20;

**Release Date:** **20 September 2025**

* **SCA Validation with Special Characters**\
  Fixed an error where SCA analysis failed when branch names or paths contained "/" or special characters. The fix covers EZ-Commit, EZ-Merge (including Pre-validation and Release Label merges), CI Jobs (Package from Version Control), Deployment (Version Control & Release Label), and Report Module.\
  _(Support Case: 152825)_

***

## ARM Release Notes 25.3.10

**Release Date**: **14 September 2025**

**Highlights**: Stability improvements across Custom Deployment, Release Labels, EZ-Commit, CI Jobs, and Salesforce ALM integration.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **Custom Deployment – Full Profile Deployment Failure:** Fixed an issue where Full Profile Deployment using Version Control failed with a size limit error because the `.git` folder was unintentionally included in the build preparation. Now, hidden folders (starting with ".") are excluded from the build process.
* **Custom Deployment – Deployment Fails with Ignore Installed Components:** Resolved an issue where deployments failed silently on the UI when the **Ignore Installed Components** option was selected. The deployment now completes as expected.
* **Deployment Logs – UI Visibility Issue:** Customers reported deployment logs not consistently showing in the UI. While the root cause is still under review, additional logging has been added to capture scenarios when logs fail to display.
* **Release Label – Deployment with Apex Meta Files:** Fixed an issue where Release Label deployments failed when changes existed only in the Apex `-meta.xml` file and not in the corresponding `.cls` file. Such changes are now correctly included in the manifest.\
  _&#x43;ommunication_: For existing Release Labels, customers must re-run artifact preparation to apply this fix. New Release Labels will work as expected.
* **EZ Commit – Pre-Validation Error:** Addressed a parsing error ("XML document structures must start and end within the same entity") that caused pre-validation EZ-Commits to fail. A new file copy library has been implemented to resolve this in **EZ-Commit (Validate Deploy)**, **CI Jobs**, and **Deployments**.
* **Salesforce ALM Integration – Status Updates:** Fixed an issue where ALM work items failed to update if the **status field’s API name** differed from the picklist label. Updates now correctly use the API name for mapping.
* **CI Jobs – Missing Debug Information in Failed Builds:** Fixed an issue where failed builds did not display detailed error logs. The UI now shows schema validation errors with file and line details, helping users quickly identify and resolve issues.
* **File Upload Error in EZ-Merge Conflict Resolution**: Customers reported being unable to re-upload modified files after downloading the conflict resolution zip in EZ-Merge. The issue was caused by restrictive file size limits.  \
  Fix: Increased the maximum supported file upload size to 100MB, ensuring smoother conflict resolution workflows.

***

## ARM Release Notes 25.3.9 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date**: **7 September 2025**

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **Revision Retrieval Error During Deployment:** Fixed an error where retrieving revisions with a single revision or while creating a release label caused runtime exceptions from Git. Updated logic now ensures stable fetch during revision retrieval.
* **Intermittent Workspace Not Found Error in EZ-Merge:** Resolved an issue where merges intermittently failed with “Workspace not found with id….” Logic was updated to handle the scenario reliably.&#x20;
* **Sub-User Branch Visibility in Admin VC Repos:** Addressed a problem where sub-users couldn’t see newly created branches unless permissions were manually updated. Sub-user visibility is now automatically enabled when a new branch is created.
* **CI Job Stuck Issue in Abort Functionality:** Fixed a corner case where a CI job could get stuck, preventing new builds from being triggered. The abort functionality has been refined to avoid such blocking scenarios.
* **Deployment Trigger Date Accuracy:** The deployment date recorded in the Reports module and Audit Tab now reflects the exact trigger time instead of relying on package creation time. This ensures more accurate tracking for all new deployments.

### **Enhancements** <a href="#enhancements" id="enhancements"></a>

* **Webhook Security Update**\
  As part of our ongoing security improvements, webhook security has been strengthened in this release.
  * Support for old webhook URLs was retired earlier in ARM v23.1.15.
  * With this release, it is now **mandatory to use an API token** with all webhook endpoints.
  * This change ensures stronger protection and prevents unauthorized access to your integrations.\
    [https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks).

***

## ARM Release Notes 25.3.8 <a href="#title-text" id="title-text"></a>

**Release Date**: **31 August 2025**

**Highlights**: Fixes and improvements across permission sets, profile comparison, reports accuracy, and SSO configuration.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **Permission Set – Deleted Tags Displayed:** Resolved an issue where deleted tags appeared under Permission Sets when committing with ServicePresenceStatus. Support for ServicePresenceStatusAccess has been added to Permission Sets, and necessary code changes were made to ensure correct behavior.<br>
* **Profile Compare – Custom Permissions Not Visible:** Fixed an issue where the Profile Compare feature in the Deployment module did not show custom permissions for orgs. Updated UI logic ensures that deltas for custom permissions now display correctly.<br>
* **Reports – Discrepancy in Deployment Counts:** Addressed a mismatch where reports displayed an incorrect deployment count when using custom range filters. Deployment counts are now consistent with actual values.<br>
* **SSO Configuration – Empty Metadata File:** Corrected an issue where downloading the AutoRABIT SSO Metadata XML returned an empty file. The file now downloads with the correct default content.

***

## ARM Release Notes 25.3.7 <a href="#title-text" id="title-text"></a>

**Release Date: 24 August 2025**

**Highlights:** Fixes to EZ-Commit translations, webhook API token status, and rollback iterations.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

1. **EZ Commit – Case Values Removed from CustomObjectTranslation:** Resolved an issue where case values were being removed from the CustomObjectTranslation file when performing multiple EZ-Commits under Japanese language. The problem was caused by unmarshalling and marshalling logic comparing values incorrectly. The comparison logic has been updated to rely on additional fields to properly support translations for different languages.
2. **Webhooks – API Token Last Access Not Updating:** Fixed an issue where webhook API tokens continued to display “Never Accessed” even after recent runs triggered by CI jobs. The back-end logic has been corrected to update and display the last access time accurately.
3. **Rollback – Iteration and Components Not Available After Revert:** Addressed an issue where rolling back a previously deployed iteration caused both the iteration and its components to disappear. A change event has been added to ensure iterations and components are available after a revert rollback.

***

## ARM Release Notes 25.3.6

**Release Date: 17 August 2025**

**Highlights**: Stability improvements and fixes for CI Jobs and Admin functionalities.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **CI Jobs – Baseline Revision Update Issue**: Resolved an issue where CI jobs were stuck and queued after a specific build. The problem was traced to a scenario where the baseline revision was not updating. The back end has been updated to address this case and additional logging has been added for better diagnostics.<br>
* **Admin – Adding Released Users to Teams**: Fixed an issue where adding a delegated or released user to a team displayed a success message but did not actually add the user. The root cause was an error in fetching released user details. Logic has been corrected to ensure the released user is properly added to the team.<br>
* **CI Jobs – Rollback Failure for Selective Components**: Addressed a rollback failure during CI job deployments when rolling back selective components, resulting in a “Not in Package.xml” error. Back-end logic has been updated to handle the workflow metadata type correctly.

***

## ARM Release Notes 25.3.5

**Release date: 10 August 2025**

### Bug Fixes

* **Branching baseline now supports committing child metadata components for Sharing Rules, Workflow, and Managed Topics**: This enhancement ensures these metadata types are correctly captured and pushed to the remote repository, addressing gaps identified in earlier releases.

***

## ARM Release Notes 25.3.4

**Release Date: 3 August 2025**\
\
**Highlights**: Reliability and accuracy improvements across CI jobs, release labels, and EZ-Commit workflows.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **CI job cleanup for Provar executions**: Unused test-result folders in Provar job paths were not deleted after runs, slowly consuming disk space. A cleanup mechanism now removes temporary directories and report data immediately after each job completes.<br>
* **Destructive change detection in remote branches**: CI jobs missed destructive updates performed directly in GitHub, causing build failures. Backend logic has been corrected so that remote destructive changes are reliably detected and processed.<br>
* **Release label revision count displayed inaccurately**: When modifying an existing release label, the UI showed an incorrect number of selected revisions. Increment logic has been fixed so the description now reflects the true revision count.<br>
* **Static resources misidentified during destructive EZ-Commit**: Deleting one static resource while another with a similar name remained caused the diff view to include both files. Selection logic has been refined so only the intended destructive file is picked up, even when naming conventions overlap.

***

## ARM Release Notes 25.3.3

**Release Date: 27 July 2025**

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* **New ALM Support**: ARM now links to the SaaS Tool Kit so EZ-Commit can update Salesforce ALM records automatically. After a simple one-time setup, developers select the User Story or Defect during an EZ-Commit, add notes or effort, and ARM pushes the commit details to Salesforce while advancing the record’s status from Unit Complete → Ready For SIT and SIT Complete → Ready For UAT—no manual edits needed.

**Bug Fixes**

* **QuickAction metadata deployments fail due to package.xml exclusion**: Fixed the package-preparation logic so QuickAction files are included, allowing validation and deployment to succeed.<br>
* **Environment-provisioning flow errors not displayed**: Corrected run-time array handling so success and failure details are now shown when enabling flows via an environment-provisioning template.

***

## ARM Release Notes **25.3.2**

**Release Date**: **20 July 2025**\
\
**Highlights**: UI fixes in conflict resolution, improved destructive change handling in DX/Non-DX, and artifact preparation reliability enhancements.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **Merge Conflict Resolution – UI Handling:** Improved the reliability of conflict resolution in the Merge Conflict screen. Resolved a UI issue where repeated lines were unintentionally removed after resolving conflicts using "Block from Source/Destination", leading to incorrect merges.<br>
* **Destructive Changes in Commit (Non-DX):** Enhanced support for Report, Dashboard, Document, and EmailTemplate components in the Deleted tab under EZ-Commit for Non-DX repositories. These were previously not triggering the proper validation and error messaging during component selection.<br>
* **CI Job Deployment – Classic Manifest Support in DX:** Fixed a bug where CI Jobs using DX repositories and Classic Package Manifest settings only packaged destructive changes, ignoring constructive ones. Validations and deployments now correctly handle all combinations of destructive and constructive changes.<br>
* **Release Label Creation – Git SSH Response Handling:** Addressed an issue where release label creation failed due to invalid credentials. The system now properly handles Git responses when fetching branches via SSH, ensuring artifact preparation continues smoothly.

***

## Release Notes 25.3.1

**Release Date: 13 July 2025**

Highlights: Stability and accuracy improvements across EZ Commit, Branching Baseline, and CI Jobs.

* **EZ Commit** – Deployment-validation reports older than 30 days were missing in EZ Commit. It's now available.<br>
* **EZ Commit** – Malformed XML errors when committing permission-set files are resolved by refining the copy logic.<br>
* **Branching Baseline** – UNKNOWN\_EXCEPTION errors during batch processing eliminated by removing the parent Workflow entry and explicitly adding the child Workflow metadata types (WorkflowTask, WorkflowFieldUpdate, WorkflowAlert, WorkflowFlowAutomation, WorkflowKnowledgePublish, WorkflowOutboundMessage, WorkflowRule, WorkflowSend) to metadatatypes.json.<br>
* **CI Jobs** – Object-level permissions in permission sets were unintentionally wiped during CI Job deployments. Back-end logic now preserves object permissions while propagating FLS changes.

***

## ARM Release Notes 25.2.12

**Release Date**: **6 July 2025**\
\
**Highlights**: Key enhancements and fixes to CI jobs, VS Code integration, deployment modules, audit reports, and environment provisioning.

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* **Audit Reports – Deployment Label & Metadata Fixes**\
  Added the Deployment Label column in the Audit Reports section. Fixed issues with Invalid Date in the created/modified date columns and removed special characters from downloaded CSV headers.<br>
* **Env Provisioning – Apex Test Level Execution Support**\
  Improved the Enable/Disable Apex Trigger Migration Template by reintroducing the Test Level dropdown in the execution window. Now the execution status updates correctly based on test result outcomes.<br>
* **CI Jobs – Sharing Rules Not Deployed**\
  Resolved an issue where Sharing Rules were skipped during deployment when linked to custom objects from installed packages.<br>
* **VS Code Plugin – File Diff Undefined Error**\
  Fixed an undefined error in EZ Commit via VS Code when accessing file diffs post-commit. The file diff generation model is now available.<br>
* **Destructive Changes – Entitlement Process Commit Fail**\
  Addressed commit failures during the Entitlement Process, destructive changes by updating the logic for DX Repositories.<br>
* **Deployment – Missing Permissions in Profile Deployments**\
  Corrected permission deployment for profiles with “Ignore Missing Visibility” enabled. This included handling for PushTopic permissions.<br>
* **Audit Reports – Triggered Date Incorrect**\
  Fixed the mismatch in deployment-triggered date display under the Audit tab.<br>
* **CI Jobs – Abort Doesn’t Terminate Background Process**\
  Improved CI job abort handling to ensure background processes are completely stopped. Now, aborted jobs no longer get stuck, and subsequent jobs queue and execute as expected.

***

## ARM Release Notes 25.2.11

**Release Date: 29 June 2025**

**Highlights**: Git Performance Optimization, Accurate CI Deployments, and Enhanced Reporting Visibility

#### **Enhancements** <a href="#enhancements" id="enhancements"></a>

* **Faster Git-Based Version Control Validations**\
  We’ve improved how ARM validates Git branches and revisions.\
  These checks are now performed directly on the **remote Git repository**, eliminating the need for local workspace setup.\
  This significantly boosts performance and reduces processing time during operations.

#### **Bug Fixes** <a href="#bug-fixes" id="bug-fixes"></a>

* **Installed Components Now Properly Excluded in CI Jobs**\
  The **“Ignore Installed Components”** option in CI jobs was previously not functioning as expected—installed components were still being deployed.\
  This has been corrected. The selected option now effectively excludes these components from deployment.<br>
* **Resolved Validation Error During Permission Set Commit**\
  Users encountered commit validation errors when working with permission sets and specific metadata selections.\
  We've refined commit logic to ensure permission set files are filtered correctly based on selected options.<br>
* **Permissionset Deployments No Longer Drop Object Permissions**\
  Deploying a new permission set with **“Ignore Missing Visibility”** enabled previously removed `DataStreamDefinition` object permissions.\
  This issue is now resolved. Both `DataStream` and `DataStreamDefinition` object permissions are preserved regardless of the setting.<br>
* **Deployment Reports Display Accurate Results for All Years**\
  Reports for years like 2023 and 2024 were previously showing incorrect data due to a mismatch in attribute formatting.\
  We’ve added compatibility for both older and newer report formats, ensuring accurate data display on the dashboard.

***

## ARM Release Notes 25.2.10

**Release date: 22 June 2025**

### **Overview**

This release delivers targeted improvements to Vlocity deployments, CI job processing, sandbox provisioning, permission settings, and EZ-Commit behavior. Key internal issues have been resolved to enhance reliability, reduce metadata deployment anomalies, and streamline configuration workflows.

#### **Internal – Vlocity Calculation Matrix Fix**

**1. Issue: After a commit, comma-separated Calculation Matrix Components were not being correctly committed to the branch. Only the YAML file was pushed, and that too in an incorrect format.**

**Fix:** Introduced logic to backup the Calculation Matrix member name, fetch the correct member, and update the YAML file accordingly. Now, the Calculation Matrix Components are committed as expected, supporting direct commits, commit labels, and release labels.

* Vlocity Version Control Deployments (including release, commit label, and AutoRABIT build) now retrieve and deploy comma-separated Calculation Matrix Components accurately.
* Vlocity Org-to-Org Deployments are verified and working correctly.
* CI Jobs now correctly retrieve and deploy comma-separated Calculation Matrix Components from source to target Salesforce org.

**Module:** Vlocity Commit, Deployments, and CI Jobs



**2. Issue: Managed package components that were intended to be excluded were still being included during deployments.**

**Fix:** Implemented proper filtering logic to ignore installed (managed) components during deployments and CI job executions, ensuring expected exclusion behavior.

**Module:** CI Jobs and Deployments



**3. Issue: During a sandbox refresh, the template failed because the Sandbox Access field was missing for the production. Salesforce updates now require explicit configuration of access levels during the refresh process.**

**Fix:** Introduced a new Sandbox Access field to the environment provisioning template. Users can now define the appropriate access level, enabling complete control during sandbox refresh.

**Module:** Environment Provisioning<br>

<figure><img src="../../../../.gitbook/assets/image (1691).png" alt=""><figcaption></figcaption></figure>

**4. Issue: During an EZ-Commit, the Diff view did not correctly reflect profile permission changes (field/object permissions), despite being configured under My Account > Salesforce Settings.**

**Fix:** Applied backend logic to ensure that global profile and permission set rules apply only to the configured profiles/permissions. The Diff screen now accurately displays modifications relevant to the EZ-Commit context.

**Module:** EZ-Commit (Profile & Permission Set)



**5. Issue: In the "Apply Global Profile / PermissionSets Settings" screen under My Account, unnecessary permission selections were displayed. This contradicted the help text stating that all field/object permissions would be universally set to true (grant) or false (revoke), making the checkbox list appear redundant.**

**Fix:** Now, only explicitly granted or revoked object/field permissions are selected or deselected in the UI, making the configuration clearer and more accurate.

**Module:** Admin → My Account → Profile / Permission Set Configuration



**6. Issue: An internal CI Job history API call was failing. Customers were unable to retrieve data via Postman due to an invalid filter applied to the DB query.**

**Fix:** Corrected the filter logic in the DB query that powers the API. The API is now functioning as expected and can return CI job history details without failure.

**Module:** CI Job History API (Postman & DB Filter)

***

## ARM Release Notes 25.2.9

**Release Date: 15 June 2025**

#### **Overview** <a href="#overview" id="overview"></a>

This release introduces support for **Salesforce API 64 (Summer ‘24)** and adds compatibility for new metadata types. Key improvements include bug fixes for CI Job execution, Profile Compare deployments, permission retrieval, and DX-based destructive changes in EZ-Merge.

#### **Salesforce API 64 Support** <a href="#salesforce-api-64-support" id="salesforce-api-64-support"></a>

**Module:** Metadata Compatibility

* Added support for the following new metadata types:
  * `LightningTypeBundle` (supported for **Non-DX** only)
  * `ExtlClntAppMobileSettings`
  * `ExtlClntAppMobileConfigurablePolicies`
  * `ExtlClntAppNotificationSettings`
  * `ExtlClntAppPushSettings`
  * `ExtlClntAppPushConfigurablePolicies`
* Also validated existing metadata types (e.g., Objects, Fields, Profiles, Permission Sets) with API 64, and confirmed that they work as expected.



**Issue:** Newly created **CI Jobs** were not getting triggered upon pull request creation in a specific branch. CI jobs for other branches in the same repository were functioning correctly.

**Fix:** The logic was updated to properly retrieve the base branch name when fetching credentials from the database. This now ensures the correct CI job is triggered for all branches.

**Module:** CI Jobs



**Issue:** When updating object permissions using the Profile Compare feature, the changes appeared to reflect correctly in the UI but were not applied during deployment. The mismatch was due to inconsistent node names in the backend.

**Fix:** Standardized object permission node names across the UI and backend to align with Salesforce's profile XML structure, ensuring accurate deployment of user selections.

**Module:** Profile Compare



**Issue:** Profiles with special characters in their names were not being retrieved properly. This was due to URL decoding and formatting that altered the original profile name, preventing matching and retrieval.

**Fix:** Removed unnecessary decoding and now presents the profile name in the exact format received from Salesforce, ensuring such profiles are correctly processed.

**Module:** Admin → Salesforce Settings → Profiles and Permissions

#### **Internal Enhancement** <a href="#internal-enhancement" id="internal-enhancement"></a>

**Issue:** Destructive changes related to static resources were not working properly for DX-format deployments in EZ-Merge.

**Fix:** Destructive change logic for static resource metadata was implemented for **DX format**, making it consistent with non-DX behavior and ensuring successful validation and deployment.

**Module:** EZ-Merge

***

## ARM Release Notes 25.2.8 <a href="#title-text" id="title-text"></a>

**Release Date: 8 June 2025**

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

## Release Notes 25.2.7 <a href="#title-text" id="title-text"></a>

**Release Date: 24 August 2025**

Highlights: Fixes to EZ-Commit translations, webhook API token status, and rollback iterations.

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

1. **EZ Commit – Case Values Removed from CustomObjectTranslation**\
   Resolved an issue where case values were being removed from the CustomObjectTranslation file when performing multiple EZ-Commits under Japanese language. The problem was caused by unmarshalling and marshalling logic comparing values incorrectly. The comparison logic has been updated to rely on additional fields to properly support translations for different languages.\
   (Support Case: 142756)
2. **Webhooks – API Token Last Access Not Updating**\
   Fixed an issue where webhook API tokens continued to display “Never Accessed” even after recent runs triggered by CI jobs. The backend logic has been corrected to update and display the last access time accurately.\
   (Support Case: 149685)
3. **Rollback – Iteration and Components Not Available After Revert**\
   Addressed an issue where rolling back a previously deployed iteration caused both the iteration and its components to disappear. A change event has been added to ensure iterations and components are available after a revert rollback.\
   (Support Case: 150209)

***

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

**Release Date: 6 April 2025**<br>

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
