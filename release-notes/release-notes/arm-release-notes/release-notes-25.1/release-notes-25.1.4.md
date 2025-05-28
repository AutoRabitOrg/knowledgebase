# Release Notes 25.1

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
