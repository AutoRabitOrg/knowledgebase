# Release Notes 24

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

See the recent updates to [nCino release 24.1](../../ncino-release-notes/release-notes-24.1.md) notes as well.&#x20;
