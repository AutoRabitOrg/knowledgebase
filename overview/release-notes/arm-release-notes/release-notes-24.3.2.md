# Release Notes 24.3.2

## Release Notes 24.3.2

**22 September 2024**

The following release notes describe the enhancements featured in our next release.&#x20;

### Enhancements <a href="#enhancements" id="enhancements"></a>

**User Role Details in Export Report**\
The export report in the Admin section has been updated to include the assigned roles for each user. The "Role Name" column has been renamed to "Roles" to reflect the possibility of multiple roles assigned to a user. This allows administrators to download and analyze comprehensive user data, including their respective roles, directly from the My Admin → Permissions tab.

**Enforced Limits on Release and Commit Label Revisions**

The system now enforces a limit of 100 revisions per release label and 100 revisions per commit label to optimize performance. Additionally, users are restricted to creating a maximum of two concurrent release labels. Error messages are displayed when these limits are reached. If the revision threshold needs to be increased, please contact Support and the ARM team can adjust release label limits at the tenant level.

**New Repository Cloning Strategy to Optimize Commit and Merge Process**

ARM now creates a single mirror clone for each repository as a base workspace and uses local clones for user workspaces. This reduces clone time, minimizes storage usage, and accelerates branch registration, deletion, and revision listing. Additionally, workspaces are deleted automatically after single use, further enhancing resource management. This change will greatly improve the performance and resource utilization of commit and merge processes, particularly for large repositories.

**Optimized Workspace Updates**\
The workspace update process has been optimized to reduce unnecessary updates. Instead of updating all workspaces daily, the system will now update only those that have been used in the last three days, based on information from the branch table. Additionally, before updating remote branches, the system will verify if the branch still exists at the source, skipping updates for deleted branches. Workspace size calculations will now use a command-based approach instead of iterating through each file, improving overall efficiency.

**Support for New Metadata Types**

ARM now supports the following metadata types:

* MessagingChannel
* ConversationMessageDefinition
* channelobjectlinkingrule
* datasourcetenantdatasrcdatamodelfieldmap
* InternalDataConnector
* MlDataDefinition
* MlPredictionDefinition

These updates ensure that users can successfully migrate Enhanced Bots and related components through ARM, including the EZ-Commit process.

**XML Code Coverage Report Conversion**

The system now supports the conversion of XML code coverage reports into a structured database format. This feature allows users to efficiently store, manage, and analyze coverage data for improved insights and reporting.

* **XML Data Conversion:** The system parses XML code coverage reports and converts all relevant elements and attributes into a structured database format for accurate code coverage reporting.
* **Database Schema:** A newly designed database schema stores key metrics such as coverage percentage, covered lines, total lines, and relevant metadata, enabling more efficient management and analysis of code coverage data.

### Improvements <a href="#improvements" id="improvements"></a>

**Improve Azure SSO Login Experience**\
An issue was reported with logging into ARM using Azure SSO, where login attempts failed after clearing the browser cache. In this release, the Spring SAML 2 provider was customized to remove certain instance-specific validations. Support Case: #115307

**Resolved Stored XSS Vulnerability in User Inputs**

The vulnerability involves Stored Cross-Site Scripting (XSS) where user inputs like Credential Username, Search & Substitute, Template Name, and Token Name are not properly sanitized, allowing attackers to inject malicious scripts. To resolve this, ensure all user inputs are validated, sanitized, and HTML-escaped to prevent script execution, especially when handling data in HTML form for backend processes.

**Resolved Einstein Bot Deployment Erasing Unchanged Information**

The issue causing Einstein bot descriptions and connections to be erased during deployment has been resolved. Bots will now retain all unchanged information, including descriptions, after deployment. Support Case: #119658

**CI Job Package Processing Efficiency**

CI job processing has been improved to prevent full branch checkouts when "Trigger Build on Commit" and "Incremental Build" are enabled, ensuring only necessary changes are checked out, even with a baseline revision set. This enhancement speeds up CI job execution by reducing processing time and improving overall efficiency. Support Case: #116048

**SCA Refresh Functionality**

The SCA refresh process has been improved to correctly reflect changes made in CodeScan after updating issue statuses (e.g., "Resolved as false positive" or "Fixed") and marking the analysis as "Passes." Now, the SCA refresh accurately picks up changes from CodeScan, ensuring issue status updates are reflected in ARM as expected. Support Case: #118659

**Improved CI Job Deployment Accuracy**

The CI job has been improved to prevent unexpected metadata deletions. Previously, deleting a single JSON file caused the entire `leadImportUtility` member to be removed from the target Org. Now, the CI job ensures only the specific file deleted in the branch is removed, avoiding unintended changes during deployment. Support Case: #119321

**EZ-Merge Validation Accuracy**

The EZ-Merge process has been enhanced to prevent unrelated metadata changes from appearing during validation. Previously, even when the file diff did not show changes after a release label merge, the validation would incorrectly pick up record-type modifications. This update ensures that only relevant changes are reflected in the merge validation, improving accuracy and consistency in the EZ-Merge process. Support Case: #118669

**Resolved PMD SCA Report Download Issues**

Several improvements have been made to resolve issues with PMD SCA report downloads in the CI Job module:

1. The CSV file now correctly displays data when downloading the SCA report, addressing the issue of empty reports.
2. The download process has been updated to ensure only the PMD report is downloaded, instead of the entire zip folder.
3. The intermittent issue where the report did not download on the first attempt has been fixed, ensuring reports are successfully downloaded on the first try.

These updates enhance the reliability and accuracy of SCA report downloads. Support Case: #120621

**Repository Credentials Management**

The issue preventing users from changing repository credentials with only one registered repo has been fixed. Now, credentials can be updated even for a single repo. Additionally, sub-users can only update credentials for their own registered repositories, ensuring proper access control. Support Case: #120504

**Deployment Error Handling for Empty Folders**

A fix has been applied to prevent the "Index 0 out of bounds" error during Release Label deployments caused by empty folders in the repository. The system now ignores empty folders, ensuring smoother, uninterrupted deployments using version control. Support Case: #120987

**Admin User Privileges Stability**

An issue causing admin users to lose access to Orgs and Branches when modifying profiles has been resolved. Previously, changes to the "Skip Mappings" setting were unexpectedly reverting to false, leading to access issues. Now, profile modifications no longer affect the "Skip Mappings" setting, ensuring consistent user access to Orgs and Branches. This enhancement improves stability and reliability for admin privileges. Support Case: #121506

**CI Job 'Validate Only' Option**

An issue where the "Validate Only" option in CI jobs was not functioning correctly has been resolved. Previously, selecting this option during a manual build triggered a full deployment instead of a validation. Now, the "Validate Only" option works as expected, ensuring that the CI job only validates the build on the target org without deploying it. This fix enhances the accuracy of build validations. Support Case: #121541

**UI Display for "Include Custom Objects Child Profile Visibilities"**

An issue has been resolved where the "Include Custom Objects Child Profile Visibilities" button was incorrectly displayed in the UI when neither profile nor custom objects were selected. Now, the button only appears when both profile and custom objects are selected, ensuring the UI functions as intended during the EZ-commit process. Support Case: #121998

***

## nCino Improvements

**Release Date: 22 September 2024**

See the Release Notes for [nCino 24.3.2](https://knowledgebase.autorabit.com/overview/release-notes/ncino-release-notes/release-notes-24.3#ncino-release-notes-24.3.2) improvements published on the Knowledge Base.

&#x20;
