# Guard Release Notes 26.1

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive Guard updates!" fullWidth="true" %}

## Guard 26.1.3 Release Notes

**Release Date: 22 February 2026**&#x20;

### Enhancements&#x20;

#### External Connected App (ECA) Authentication Migration&#x20;

To align with Salesforce Spring ’26 security requirements, Guard has updated the authentication flow for External Connected Apps (ECA).&#x20;

What’s changed:&#x20;

* Guard now enforces Salesforce’s updated authentication standards for External Connected Apps.&#x20;
* Connectivity remains seamless once authentication is configured.&#x20;

Customer Action Required:&#x20;

* When adding new Salesforce orgs via External Connected Apps, the following to be provided:&#x20;
* Client ID&#x20;
* Client Secret&#x20;

What stays the same:&#x20;

* No changes to core Guard functionality.&#x20;
* No changes to user workflows after successful authentication.&#x20;

This update ensures continued secure and compliant integration with Salesforce orgs under updated platform security requirements. &#x20;

Learn more [here](https://knowledgebase.autorabit.com/fundamentals/announcements/salesforce-oauth-external-client-app-eca-transition).&#x20;

### Bug Fixes&#x20;

#### Duplicate Success Popups When Creating Real-Time Notifications&#x20;

Duplicate success messages when creating Real-Time Notifications are no longer shown. The system now displays a single, clear confirmation message.&#x20;

#### Session Token Expiration Error in Permission Explorer&#x20;

Fixed an intermittent issue that caused a “Session Token Expired” error when accessing Permission Explorer, ensuring uninterrupted usage.&#x20;

#### Permission Explorer Stuck on Org Switch&#x20;

Resolved loading issue when switching orgs with multiple permissions selected. Org switching complete successfully now (where applicable)&#x20;

#### Invalid ZIP when no Records found&#x20;

Exporting with no records was generating an invalid ZIP file. No-data exports are disabled now.&#x20;

***

## Guard 26.1.2 Release Notes&#x20;

**Release Date:  15 February 2026**&#x20;

### New features&#x20;

#### Public Links – Visibility into Exposed Salesforce Files&#x20;

Guard now provides visibility into Salesforce files that are publicly accessible via shared links, helping customers identify potential data exposure risks.&#x20;

A new Public File Exposure view under Risk lists files that have public links enabled, along with key details such as file name, public link, expiration date, and creator. This allows administrators to quickly identify links that may lack expiration controls or have been left active longer than intended.&#x20;

### Enhancements&#x20;

#### Access Controls – Multi-Selection Support&#x20;

Access Control criteria creation has been enhanced to provide greater flexibility and precision when defining access rules.&#x20;

Users can now select multiple Profiles, Roles, Company Names, and Domains when creating Access Control conditions, instead of being limited to a single value. &#x20;

Existing Access Controls continue to function without any behavior changes, and all violation detection, auto-revert, and notification workflows remain unchanged.&#x20;

#### Access Controls – Modification Tracking&#x20;

Access Control detail pages now include Last Modified Date and Modified By fields to improve visibility into configuration changes.&#x20;

This enhancement makes it easier for administrators to understand when an Access Control was last updated and by whom, supporting better governance and audit readiness. For newly created Access Controls, the creation date and creator are shown. For existing Access Controls, modification details are updated whenever changes are saved.&#x20;

This change is informational only and does not impact Access Control enforcement or performance.&#x20;

#### Permission Explorer – Multi-Selection Filters&#x20;

Permission Explorer now supports multi-selection across query filters, enabling more advanced and targeted permission analysis.&#x20;

Users can select multiple values for Profile, Role, Company Name, and Domain.&#x20;

Selected filters are clearly visible in the UI and can be individually removed, making complex queries easier to build and adjust.&#x20;

#### Persistent Filters Across Guard&#x20;

Guard now remembers user-applied filters during a session, improving usability when navigating across features.&#x20;

Once filters are applied, they remain active when users navigate away from a page, return later, or refresh the browser. Filter persistence is handled per feature and per user, ensuring that filters from one area do not affect another and that each user sees their own saved state.&#x20;

Default filters continue to apply on initial login, and users can modify or clear filters at any time, with changes saved immediately.&#x20;

#### Filter-Aware Export&#x20;

Exports now include only records that match the currently applied filters, ensuring consistency between the UI and exported files. This enhancement applies to:&#x20;

* Automated Data Classification&#x20;
* API Security&#x20;
* Change Monitoring&#x20;
* User Activity Monitoring&#x20;
* Risk Assessment&#x20;

When no filters are applied, export behavior remains unchanged and continues to include all records using the default format.&#x20;

#### Change Monitoring – Content Settings Tracking&#x20;

Change Monitoring has been enhanced to provide greater visibility into content-related configuration changes.&#x20;

Events related to content settings are now parsed and tracked, allowing administrators to better audit and understand changes made within Salesforce orgs.&#x20;

#### Change Monitoring – “Login as Any User” Event Tracking&#x20;

Change Monitoring now captures “Login as any user” events generated when administrators access user accounts using Salesforce’s delegated login capability.&#x20;

These events are parsed and displayed in Change Monitoring in the Other tab, providing improved visibility into elevated access activity and supporting stronger audit and compliance requirements.&#x20;

### Bug Fixes&#x20;

#### Risk Assessment – Risk Name Typo&#x20;

Corrected a typo in a risk name to “Anonymous user access is properly restricted”.&#x20;

#### User Activity Monitoring – User Count by Profile&#x20;

Fixed an issue where User Count by Profile displayed incomplete data. Profile-based user counts are now accurate and consistent with overall user and license data.&#x20;

#### Change Monitoring – Intermittent “Subscription Error”&#x20;

Resolved an intermittent “Subscription Error” pop-up that occurred when switching filters or orgs in the Change Monitoring module. Filter navigation now works smoothly without errors.&#x20;

***

## Guard Release Notes 26.1.1

**Release Date: 25 January 2026**

### New Features

#### Deep Data Scanning

Guard now goes beyond metadata analysis and can scan field data to identify sensitive or regulated information.

Sensitive data often resides in free-text or unstructured fields, such as comments or notes. With Deep Data Scanning, Guard can now detect regulated data patterns (such as emails, phone numbers, or other sensitive content) directly within field values.

Note: Deep Data Scanning is disabled by default and can only be enabled when explicitly allowing it.

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
