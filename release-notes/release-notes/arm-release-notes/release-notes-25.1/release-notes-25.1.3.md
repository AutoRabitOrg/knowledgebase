# Release Notes 25.1.3

## ARM Release Notes 25.1.3

**Release Date: 06 April 2025**\
\
This release introduces significant new capabilities and key enhancements across the ARM platform. A major new feature enables **multi-level deployment approvals by Org**, offering structured release governance with customizable approval groups. Architecture improvements include enhanced **global workspace management** to handle deleted or missing branches more gracefully. The release also strengthens security with **API token usage audit logging** and encrypted installation key handling. Core functionality has been optimized, including improved **commit revision sorting** and **faster loading of standard value sets**.

#### **1. New Feature** <a href="#id-1.-new-feature" id="id-1.-new-feature"></a>

* **Multi-Level Deployment Approval by Org**\
  A two-level deployment approval process has been introduced to provide better control over releases. Each approval level supports group-based approval, where any member within the group can approve the deployment. Email notifications are sent to approvers with a link to ARM for approval actions. This approval process can be configured based on Org name. Admins can select applicable orgs and assign separate approvers or approver groups for each.

#### **2. Feature Enhancements** <a href="#id-2.-feature-enhancements" id="id-2.-feature-enhancements"></a>

* **Secure Handling of Installation Key in Unlocked Packages CI Job**\
  The installation key used in the Unlocked Packages CI Job is now masked and encrypted for improved security. Additionally, a view/hide eye icon has been introduced to toggle the visibility of the installation key.
* **Clear Status Indicators for Merge Pre-validation Outcomes**\
  The 'Merge Prevalidation Process' logs now provide clearer visual indicators based on the outcome of the validation. A green checkmark is shown only when the process completes successfully, while a red X clearly indicates when the pre-validation has failed or resulted in auto-rejection. This improvement ensures better visibility into validation outcomes for both merge and commit workflows.

#### 3. Architecture Improvements <a href="#id-3.-architecture-improvements" id="id-3.-architecture-improvements"></a>

*   **Resilience in Global Workspace Management for Optimized Workspaces**\
    A backend fix has been implemented to ensure stability in global workspace creation when the default branch is missing or deleted in the repository. When the default branch no longer exists in AutoRABIT or the remote, the system will now automatically update the global workspace and repository configuration to use the last valid branch. This prevents version control operations—such as commit, merge, or revision listing—from being blocked due to a broken global workspace.

    A UI enhancement to allow users to change the default branch directly in the VC Repos module will be introduced in an upcoming release to fully resolve the issue.

#### **4. Bug Fixes and Improvements** <a href="#id-4.-bug-fixes-and-improvements" id="id-4.-bug-fixes-and-improvements"></a>

* **Reliable CI Job Queue Handling**\
  Resolved an issue where CI jobs were stuck in the queue due to mismatched build numbers between CIJobInfo and CIJobHistory tables. The system now handles these cases correctly, ensuring jobs progress without blocking subsequent builds. _Impacted Modules: CI Job Abort and Queue flows Release label abort and Queue flows. Support Case #134965_
* **CustomNotificationType Support in Destructive Commits**\
  Destructive commits now support the CustomNotificationType metadata. _Impacted Modules: Commits, Merges , Release label Artifact execution ,CI Jobs, Deployments while performing the Custom Notifications type destructive changes flow. Support Case: #133054_
* **Package Key Handling in Deployment Module**\
  Resolved an issue where deployments failed due to a null package key during package version installation. The key preparation logic for dependent packages has been corrected, and a migration has been implemented to fix existing invalid keys. _Impacted Modules: Unlocked packages, Deployments. Support Case: #132661_
* **LWC API Check Support in CodeScan Analysis**\
  Files with `.js-meta.xml` suffixes are now included in the CodeScan analysis, enabling proper API checks on Lightning Web Components (LWC) from ARM. This ensures more accurate validation during the scan process. _Impacted Modules: ARM CodeScan integration. Support Case: ##132042_
* **Accurate File Name Display in Review Artifact**\
  The Review Artifact UI now correctly updates the file name when switching files, ensuring clarity while reviewing changes. _Impacted Modules: EZ Commit -> Review-Artifact -> Edit In IDE -> File Names in editor view. Support Case: ##133904_
* **Commit Revisions Sorted by Committed Timestamp**\
  Commit revisions in the Commit module are now displayed based on the committed timestamp, aligning with GitHub's behavior. Previously, revisions were shown using the author timestamp, causing confusion. The backend logic has been updated to ensure commits are sorted and displayed consistently. _Impacted Modules: New Deployment, New CI Jobs, New Merge, VC Repositories, Release Labels. Support Case: #132721_
* **Support for Special Characters and Extended Name Lengths in User Profiles**\
  User profile fields now support special characters in first and last names. Additionally, the character limits have been extended—first names now allow 3 to 40 characters, and last names allow 1 to 80 characters. _Impacted Modules: Admin, My Profile. Support Case: #133923_
* **Support for Priority 4 Rules in Apex PMD Static Code Analysis**\
  Static Code Analysis now includes Priority 4 rule violations in Apex PMD reports. The minimum PMD priority has been updated from Medium (3) to Low (5), allowing visibility into lower-priority issues without affecting CI Job validations configured to fail only on higher-priority errors. _Impacted Modules: All static code analysis running with apexPMD. Support Case: #132749_
* **Optimized Loading of Standard Value Sets in Commit**\
  Improved performance and visibility of Standard Value Sets in the EZ-Commit module by minimizing repeated Salesforce API calls. The system now retrieves enabled services during org registration and stores the cloud org type in the database. For existing orgs, the cloud type is updated during retrieval and used for subsequent requests, significantly reducing load times and ensuring correct metadata visibility—especially for Financial Services Cloud orgs. _Impacted Modules: EZ-Commit, Commit Templates, Branching baseline, Deployments, CI-Jobs. Support Case: #133958_
* **Provar Plugin Name Edit Handling**\
  Editing the Provar name in the Admin module no longer triggers an invalid notification pop-up when a key file is already uploaded. A response check ensures smoother and more accurate user feedback. _Impacted Modules: My Account plugins (Provar)._

\
