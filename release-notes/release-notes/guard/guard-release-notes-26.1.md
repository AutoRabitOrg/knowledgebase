# Guard Release Notes 26.1

## Guard Release Notes 26.1.1

**Release Date: 21 January 2026**

### New Features

#### Deep Data Scanning

Guard now goes beyond metadata analysis and can scan field data to identify sensitive or regulated information.

Sensitive data often resides in free-text or unstructured fields, such as comments or notes. With Deep Data Scanning, Guard can now detect regulated data patterns (such as emails, phone numbers, or other sensitive content) directly within field values.

Note: Deep Data Scanning is disabled by default and can only be enabled when explicitly allowing for it.

Key capabilities include:

* Automatic Deep Data Scanning\
  Users can define common field name patterns (comments, notes, info). Guard automatically scans matching fields to identify potential regulatory exposure.
* Manual Deep Data Scanning\
  Users can manually trigger a one-time scan directly from a field’s detail page. Scan progress and results are clearly displayed for easy review.

User Benefits:

* Improved detection of sensitive data hidden in text-heavy fields.
* Stronger compliance visibility across Salesforce data.
* Full control over when and how data is scanned.

#### Custom Regulations Context

Guard now allows specifying custom regulations, enabling accurate classification of data against organization-specific, regional, or internal compliance requirements.

Users can provide Guard with additional context for custom regulations defined in their Salesforce organization, allowing classifications to reflect real-world compliance needs.

User Benefits:

* Centralized management of custom and default regulations in Data Classification settings.
* Editable regulation descriptions and sample field names to guide classification logic.
* Automatic use of custom definitions in future scans.
* Reduced manual validation and reclassification effort.

### Enhancements

* Access Controls – Support All Permissions\
  Access Controls now support all permissions available in a Salesforce org, including permissions outside predefined categories.
* Partial syncing of Data Classifications to Salesforce\
  Users can now choose which detected regulations to sync back to Salesforce on a per-field basis, with clear indicators for not synced classifications.
* Improved default view for Data Classification fields\
  The Data Classification table now shows only fields created in the past three months by default, helping to focus on recent changes.
* Additional filtering in Data Classification\
  New filters allow fields to be selected by Field Name and/or Sync status (Synced, Not Synced, Partially Synced).
* Visibility for unclassified fields\
  Fields that weren’t classified now appear in the Data Classification table and are clearly marked as “None Detected,” with optional manual data scan action available.
* Expanded email domain support for Support Login Access (autorabit.com, autorabit.us)\
  Support Login Access now allows authorized AutoRABIT support users from an additional approved email domain, while maintaining existing validation and audit.
* Improved stability of chatbot responses\
  Enhanced handling and validation ensure more consistent and reliable responses from Guard’s expert.
* Updated menu and refreshed logo\
  Minor UI updates improve visual consistency and overall user experience.

### Bug Fixes

* Tenant creation is no longer failing when a tenant's name starts with a number.
* Expiration dates for export download links generated during weekends are set properly now.
* Fixed an issue where administrators could not view activity history for support login users.
* Fixed a typo in the Data Classification UI (“Compliance Categorization”).
* Fixed swapped metrics on API Security Dashboard.
* Improved chatbot behavior as well as making responses more concise.
* Scenarios addressed in Permission Explorer:
  * Frozen users not appearing in matching profiles or permission sets.
  * Pagination not resetting when switching selections.
  * System Administrator profile incorrectly showing no assigned users.
  * Queries returning no users in large orgs.
* Table-view filters and search in Risk Assessment are working as expected.
* Added Risk Level to Change Monitoring export, so exported files match the UI.

&#x20;
