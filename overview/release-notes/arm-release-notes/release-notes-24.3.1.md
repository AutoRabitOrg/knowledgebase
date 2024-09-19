# Release Notes 24.3.1

## Release Notes 24.3.1

**Anticipated release date: 9 September 2024**

### Enhancements

#### **Version Information Display for Vlocity Metadata**

Users can now view detailed version information, including the modification date, modified by, and creation date, for metadata when selecting Vlocity Metadata for deployment. This enhancement gives users visibility into the most recent changes and helps ensure they select the correct version for deployment.

#### **Exclude Metadata in Branching Baseline**

Users can now exclude specific metadata directly within the Branching Baseline interface, removing the need to adjust settings globally under My Account > Salesforce Settings. The interface includes Salesforce and Vlocity dropdown options based on the selected retrieval type. Users can easily search, select, or deselect metadata items using the new "Check All" and "Uncheck All" features for both included and excluded metadata sections.

This functionality is also available when using the re-run option, reflecting the same metadata exclusions from the initial run. If no metadata is selected, the system will automatically apply the global settings.

#### **Date-Range Report Download for ARM Weekly Report**

Users can now download reports within a selected date range. After clicking on "Refresh Reports View" to generate the latest reports, users can select a customizable date range using the "From" and "To" date pickers. The date range can be anywhere from 7 days to 6 months. Once the date range is set, users can click "Download" to obtain the reports within the specified period. If the report generation is still in progress, the date selection and download options will be temporarily disabled until the reports are ready.

#### **Improved Profile Metadata Handling and Permissions Management on EZ-Commit**

Users can now more effectively manage profile metadata and permissions during commits with the introduction of new options and improved handling in the Review Artifact process.

**Key Features:**

1. **Child Fields and Permissions Checkbox:**
   * A new checkbox labeled "Custom Objects include all child fields and child field permissions" has been added. This is automatically selected by default, allowing users to include or exclude child field permissions when committing custom object profiles. If users prefer not to include any child field permissions, they can simply unselect this option.
   * This checkbox is visible only when custom objects and profiles are selected.
2. **Renamed Option for Clarity:**
   * The checkbox "Commit Options for Selected Profiles" has been renamed to "Commit Profile Metadata Only \[Includes Permissions for Selected Objects]" to more accurately reflect its function.

**Scenarios:**

* **Including All Permissions:**
  * When the user edits field permissions and selects the checkbox "Custom Objects include all child fields and child field permissions," all child permissions will be included in the commit.
* **Excluding Child Permissions:**
  * If the user edits object or field permissions and unchecks the checkbox, only object permissions will be committed, excluding all child permissions.
* **Commit Profiles Only:**
  * Selecting "Commit Profile Metadata Only" while unchecking the child permissions checkbox will result in committing only object permissions, excluding changes in child permissions and review artifact updates.
* **Full Profile Commit:**
  * When "Commit Full Profiles" is selected, the child permissions checkbox will be auto-checked and disabled, ensuring all permissions are included while excluding any review artifact changes.

This enhancement provides greater control over what is included in profile commits, ensuring more precise and targeted updates.

### Improvements

**UI Filter for InstalledEditable State in Deployments**

A new UI filter has been added for the "InstalledEditable" state in deployments. When the "Exclude Managed Packaged Components" option is selected in Admin (Salesforce Settings), the deployment filter will automatically have the "Installed" and "InstalledEditable" states unchecked by default. If the option is not selected, these states will be checked by default. This enhancement simplifies deployment filtering based on the chosen settings. Support case #118691

**Unified Icons Across UI**

The icons on the UI screen have been updated across all modules for better visibility. The updated icons are now consistent across the following modules: CI Jobs - Deploy Only, Modularization, Custom Deployment, Scratch Org, and Org Sync. This change does not introduce any new logic but ensures a more cohesive visual experience across the platform.

**Hiding the Auto Approve Option According to Merge Settings Response**

The 'Auto Approve on Merge Validation Success' option will now only be displayed during a merge if it has been enabled under the merge settings. If this option is not enabled by the user in the merge settings, it will no longer appear when performing a merge. Support case #119940

**Retention of SF Org Mappings During Sub-User Permission Updates**

Previously, when an Admin updated permissions for a sub-user—such as granting additional SF Org or branch access or revoking consent—the SF Org mappings for that sub-user were being removed. Now, SF Org usernames are retained when saving these updates. This ensures that sub-user profiles maintain their correct mappings after permission changes. Support case #120346

**Resolved Special Characters Issue with Re-Uploading Files After Merge Conflict**

A fix has been implemented to address an issue where users experienced a problem after resolving and re-uploading a conflicted file during a merge. Although the upload was successful, the verification process would not complete. This was caused by special characters in the label name or file name. The front end now uses an encoded URL for label names and file names containing special characters, ensuring the verification process completes successfully. Support case #120393

**Improved CI Job Build Stability**

An issue was identified where CI job builds were failing due to the use of identical variable names in both parent and child classes. This caused problems during JSON conversion in certain edge cases, leading to build failures. The underlying code has been updated to handle these scenarios more robustly, preventing conflicts and ensuring CI job builds proceed without errors. Support case #120527

**Improved Error Handling During Merge Conflicts**

An undefined error occurred when customers attempted to upload a merge-conflicted file. This issue has been addressed by making changes to the API payload and implementing minor UI adjustments. The impacted areas include the SCM Conflict Report and the SCM Merge Conflict and Review Artifact screen. Support case #120867

**Improved Ticket Detection in ALM CI Jobs**

A problem was identified where ALM CI Jobs stopped detecting tickets. This issue has been resolved by adding conditions to the database query to account for all types of completion values. Support case #120882

**Commit Template Component Limit Increased**

The commit template was limited to displaying 50 components, even when more components were selected. This limitation has been addressed by adding a data-table check for all metadata component members. The commit template can now handle and display 200 components. Support case #120095

**Report and Folder Deployment Stability**

An issue was identified during the package preparation process using Package.xml, metadata.zip, or Org-to-Org deployment for the Reports metadata type, leading to deployment failures. To address this, the logic has been corrected to ensure that -meta.xml is properly removed from components being added to Package.xml for reports and dashboards. This fix improves the reliability of report and folder deployments. Support case #121356

**Default Exclusion List**

Removed the messaging channel from the default exclusion list. Support case #119852

