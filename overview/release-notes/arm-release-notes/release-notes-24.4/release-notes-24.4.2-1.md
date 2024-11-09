# Copy of Release Notes 24.4.2

## ARM Release Notes 24.4.2

**Release Date: 10 November 2024**

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Salesforce API Version 62 Support**

ARM now supports Salesforce API Version 62 for all functions, allowing users to utilize the latest metadata types and capabilities introduced by Salesforce. This upgrade includes comprehensive integration across all ARM functions, including the Data Loader, ensuring alignment with Salesforce's Winter '25 release. ARM Admins can set the global API to version 62, ensuring consistent functionality across all features.

### Support <a href="#support" id="support"></a>

#### **Accurate Metadata Count for Repeated Deployments**

ARM now ensures accurate tracking of metadata counts across multiple deployments using previous deployment labels. The request node sent for deployment has been corrected in the front end, ensuring that when performing a follow-up deployment with a prior label, all specified components are included. This enhancement resolves issues in which subsequent deployments using previous labels reflected only a partial count of metadata components, providing a consistent and complete deployment experience across repeated operations. Support Case #123952

#### **Confirmation for Destructive-Only Deployments**

A new confirmation prompt has been added to notify users when a deployment includes only destructive changes and no constructive changes. This enhancement helps clarify deployment contents, reducing potential confusion for users who may expect other metadata components to be included. Support Case #122559

#### **Inclusion of Destructive Changes File in Deployment Backups**

The backup.zip file now includes the `destructiveChanges.xml` file, allowing users to access destructive change data for potential rollback scenarios. This enhancement provides a more comprehensive backup package to support safer and more flexible deployment management. Support Case #123767

#### **Improved Commit Label Search Functionality**

Enhancements have been made to the commit label search feature to address two user concerns:

1. **Accurate Filtering with Special Characters**: The search functionality on the Commit Labels screen now retains all special characters in commit labels, allowing for precise search results even with special characters.
2. **Consistent Label Retrieval Across Screens**: The commit label creation and retrieval processes have been standardized across the EZ-Commit and Commit Labels screens. This ensures accurate search results by aligning label keys, resolving prior issues with locating commit labels by revision.

These improvements enhance usability and consistency within the Version Control module, providing a more reliable experience for commit label management. Support Case #124254

#### **Corrected Revision Display in EZ-Merge Confirmation**

An update has been made to ensure proper display of revision numbers in EZ-Merge confirmations. Previously, certain revision formats containing the character "e" were misinterpreted as exponential values, causing them to display incorrectly as "Infinity" or scientific notation.

This issue has been resolved by adjusting the response handling, allowing revisions to appear as intended without conversion errors. This enhancement improves the accuracy and reliability of revision details displayed during merges, especially for branches with specific revision formats. Support Case #123820

#### **Quick Deploy Auto-Population for Deployment Label and Asynchronous ID**

An improvement has been made to the Quick Deploy feature to ensure the Deployment Label Name and Asynchronous ID fields auto-populate after a validated deployment. This update addresses issues in which these fields were previously blank, preventing users from completing Quick Deploy without manually re-entering data.

This enhancement improves efficiency and consistency for custom deployments, particularly for users working with single revision DX deployments. Support Case #123978, #123757

#### **Stable Permissions View for Newly Created Teams**

An update has been implemented to ensure stable loading of the Permissions View in the Admin module for newly created teams under Subscription Management. Previously, permissions were not displayed due to an incomplete setup for new users created via the "Create Team" option.

Now, the `releaseNotify` setting for new users defaults to "true," and additional checks have been added to handle null values during data conversion. This enhancement ensures permissions load reliably, enhancing usability for subscription-based team management. Support Case #124059

#### **Improved CI Job Editing with Null Check for Checkmarx Configuration**

A fix has been implemented to prevent blank pages from displaying when editing CI jobs. Previously, attempting to edit CI jobs with no rules configured for Checkmarx would result in an unresponsive, blank screen.

This enhancement includes a null check, ensuring CI jobs are editable even if no rules are set for Checkmarx configurations. This update improves stability and usability for managing CI jobs in ARM. Support Case #124555

#### **Improved Tag-Based Deployment**

An update has been made to ensure successful deployments when using tags in the deployment module. Previously, deployments initiated with tags would sometimes fail with a "No Changes are found in the package" error due to issues with file copying during tag-based deployments.

This enhancement ensures accurate file handling for tag-based deployments, providing stable and reliable performance for both DX and non-DX branches. Support Case #124672

#### **Accurate Error Messaging for CI Jobs and Deployments**

An update has been implemented to improve the accuracy of error messages displayed in CI job logs and deployments. Previously, CI jobs that encountered baseline revision failures or exceeded file limits displayed misleading error messages. Additionally, deployment failures were showing unrelated errors, such as "Invalid Login," instead of indicating the true cause, such as reaching Salesforce file limits or the need for reauthentication.

This enhancement ensures that CI job and deployment errors reflect the actual underlying issues, providing users with clearer, more actionable information for troubleshooting. Support Case #123816

#### **Direct Commit Support for Profiles and Permission Sets**

An update has been applied to the direct commit process to ensure that both profiles and permission sets are committed together when selected. Previously, when committing Field-Level Security (FLS) for profiles and permission sets in a single direct commit, only profile FLS was committed, while permission sets were excluded.

This enhancement aligns direct commit functionality with pre-validation commits, allowing selected metadata types—including profiles, permission sets, and custom fields—to be consistently committed as intended. This update improves accuracy and flexibility for version control management within ARM. Support Case #124622

#### **Improved Merge Conflict Resolution Status**

An update has been applied to ensure accurate status updates during merge conflict resolution in EZ-Merge. Previously, after resolving a conflict, the status was sometimes incorrectly set to "Commit," even when additional conflicts remained. This led to repeated merge conflict prompts after refreshing the page.

With this fix, the merge status will correctly display as "In Progress" when unresolved conflicts are pending, and actions will show as "Check Details" instead of "Commit." This enhancement ensures clearer guidance during conflict resolution, streamlining the merge process in EZ-Merge for better user experience. Support Case #123732

#### **Optimized Inline Comment Retrieval in Large File Diffs**

An improvement has been made to reduce "Network Connection Interrupted" errors when expanding large files under the "Files Changed" tab in EZ-Merge. Previously, each line in files exceeding 3,000 lines triggered an individual API call to fetch inline comments, leading to network interruptions and interface freezes, particularly for files with 15,000 lines or more.

With this enhancement, a single API call now retrieves all inline comments at the file level, significantly improving performance and stability when working with large files. This update prevents excessive network calls and enhances usability during merge and commit actions. Support Case #124893

#### **Accurate Component Inclusion for Reused Commit Labels**

An update has been made to the "Re-use Previously Validated Commit Labels" functionality to ensure that only selected components are included in the commit. Previously, when reusing a validated commit label, additional, unintended changes (such as Profiles and Permission Sets) could appear in the "Files Changed" tab during the approval stage, even if only specific components were selected initially.

This enhancement corrects the commit process so that only the selected components are retained and displayed in the commit, providing more reliable control and accuracy over component selection in EZ-Commit. This improvement applies to both DX and non-DX formats and supports all commit types, including manual selection, auto-draft, commit templates, and package uploads. Support Case #125341\








&#x20;

&#x20;

