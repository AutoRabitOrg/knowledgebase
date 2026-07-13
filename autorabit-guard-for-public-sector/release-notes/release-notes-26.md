# Release Notes 26

## AutoRABIT Guard PubSec 26.1.1 Release Notes

**Release Date: 12 July 2026**

### New features <a href="#new-features" id="new-features"></a>

#### **AI Interfaces for AutoRABIT Guard**

Guard now includes new AI interfaces that allow users and AI assistants to interact with Guard through natural language workflows.

A built-in MCP server enables compatible AI clients to securely query Guard data, run supported tools, and access Guard capabilities through authenticated requests. The MCP server uses the existing Guard backend, security model, tenant isolation, and service layer.

For more detailed information on the MCP setup, please see the User Guide and Technical Specification in the Knowledge Base.

#### **User Activity Monitoring – Historical Tracking**

User Activity Monitoring now captures historical user activity data through daily snapshots.

Guard stores daily per-user snapshots and org-level aggregate counts, allowing customers to review how user access and activity change over time. The UAM dashboard now includes historical aggregate data, and user detail pages include daily history for individual Salesforce users.

#### **API Security – Historical Tracking**

API Security now supports historical tracking through daily posture snapshots.

Guard stores daily API Security summary data for connected orgs, including unverified apps, over-permissive apps, verified apps, total usage, and last used time. A new read-only history view allows users to review past API Security posture over time.

#### **Permissions Explorer – Agentforce Visibility**

Guard now has Agentforce coverage in Permissions Explorer to help teams understand what Salesforce AI agents can access and the actions they can take within your Salesforce orgs.

There is now a dedicated Agentforce permission category that makes it easier to investigate users with Agentforce-related capabilities, including permissions tied to managing agents, prompt templates, and Agentforce-specific features. Users can select one or multiple Agentforce permissions and trace how access is granted across profiles, permission sets, and permission set groups.

In addition, a new “Explore Agentforce” experience from the Permissions Explorer home page allows users to identify Agentforce-related users and review the profiles, permission sets, and permission set groups assigned to them. Results also show the source of each permission, making it easier to audit AI agent access and support least-privilege reviews.

#### **Risk Assessment – Historical Tracking**

Risk Assessment now includes historical tracking to provide visibility into how an org’s security posture changes over time.

Guard captures daily snapshots for each connected org and makes them available in a new History view. The history table includes a timestamp and a count of the org’s auto-resolvable risks, manual risks, and compliant settings, helping teams review past states and establish a foundation for future trend analysis.

#### **User Security Overview**

AutoRABIT Guard introduces the **User Security Overview**, a centralized dashboard that provides administrators with a comprehensive, per-user view of security and access within a connected Salesforce org. This feature allows users to select an org and a specific Salesforce user, then review their security posture across multiple dimensions in a single place.

The User Security Overview makes it easier to understand what a user can access, why they have that access, and how their account is being used. It brings together key information such as user profile details, effective permissions, connected applications, and login activity into a unified, tabbed interface.

Key capabilities:

* **User Details**: View profile information, role, status, and last login details.
* **Object-Level Access**: Analyze effective CRUD permissions across all Salesforce objects.
* **Permission Source Transparency**: Understand which profiles and permission sets grant access.
* **Field-Level Security**: Review Read/Edit access at the field level with drill-down visibility.
* **Permission Sets**: Audit assigned permission sets and identify expired or unnecessary access.
* **Connected Applications**: View active OAuth-connected apps and their usage.
* **Login Activity Monitoring**: Analyze login history, including IP, location, and device details.

This feature helps security teams quickly investigate access, identify over-permissioned users, detect suspicious activity, and improve overall governance. The feature is read-only and does not impact existing permissions, configurations, or system performance.

#### **Public Links – Visibility into Exposed Salesforce Files**

Guard now provides visibility into Salesforce files that are publicly accessible via shared links, helping customers identify potential data exposure risks.

A new Public File Exposure view under Risk lists files that have public links enabled, along with key details such as file name, public link, expiration date, and creator. This allows administrators to quickly identify links that may lack expiration controls or have been left active longer than intended.

#### **Deep Data Scanning**

Guard now goes beyond metadata analysis and can scan field data to identify sensitive or regulated information.

Sensitive data often resides in free-text or unstructured fields, such as comments or notes. With Deep Data Scanning, Guard can now detect regulated data patterns (such as emails, phone numbers, or other sensitive content) directly within field values.

Note: Deep Data Scanning is disabled by default and can only be enabled when explicitly allowing it.

Key capabilities include:

* Automatic Deep Data Scanning Users can define common field name patterns (comments, notes, info). Guard automatically scans matching fields to identify potential regulatory exposure.
* Manual Deep Data Scanning Users can manually trigger a one-time scan directly from a field’s detail page. Scan progress and results are clearly displayed for easy review.

User Benefits:

* Improved detection of sensitive data hidden in text-heavy fields.
* Stronger compliance visibility across Salesforce data.
* Full control over when and how data is scanned.

#### **Custom Regulations Context**

Guard now allows specifying custom regulations, enabling accurate classification of data against organization-specific, regional, or internal compliance requirements.

Users can provide Guard with additional context for custom regulations defined in their Salesforce organization, allowing classifications to reflect real-world compliance needs.

User Benefits:

* Centralized management of custom and default regulations in Data Classification settings.
* Editable regulation descriptions and sample field names to guide classification logic.
* Automatic use of custom definitions in future scans.
* Reduced manual validation and reclassification effort.

### **Enhancements** <a href="#enhancements" id="enhancements"></a>

#### **Risk Assessment – New Salesforce Security Check Details**

Risk Assessment now includes curated Overview and Impact descriptions for additional Salesforce security checks, including MFA, SAML, external client application metadata access, session settings, trusted IP ranges, and administrator access levels.

These descriptions help users understand what each check means and why it matters, rather than relying only on raw Salesforce labels.

#### **Risk Assessment – Auto Resolve Configuration**

Risk Assessment now supports tenant-level configuration for Auto Resolve.

When Auto Resolve is disabled for a tenant, the Auto Resolve button is unavailable in Risk Assessment and displays a tooltip explaining that auto-resolve is disabled for the instance. When enabled, Auto Resolve continues to behave as before.

#### **AutoRABIT Guard™ Naming Updates**

Customer-facing product naming has been updated across Guard for consistency.

UI copy, browser title, help areas, notification email templates, chatbot prompts, CLI help text, MCP references, and skill references now use AutoRABIT Guard™ consistently where product naming appears.

#### **User Activity Monitoring – Flag Icon Tooltips**

Flag icons in the User Activity Monitoring table now include tooltips so users can quickly understand each status indicator.

Frozen users and password-locked users are now clearly identified on hover and keyboard focus, improving usability and accessibility without affecting table layout.

#### **Change Monitoring – Other Tab Export**

Change Monitoring now supports export from the Other tab.

Exports follow the same experience used in other Guard modules: select filters and results are delivered in a CSV file by email. This makes it easier to share and review event data captured outside the main Changes tab.

#### **Public File Exposure – Export**

Public File Exposure now supports export.

Teams can export the records currently shown in the view, with applied filters reflected in the output. The export includes all table columns and is delivered by email.

#### **User Monitoring – Chart Synchronization**

User Activity Monitoring charts now stay aligned with the filters applied in the Users table.

When users apply filters, the User Count by Profile and License Usage charts update to reflect the same filtered population. This creates a more consistent experience between tabular and visual analysis.

#### **User Monitoring – Updated Users Table**

The Users table in User Activity Monitoring has been refreshed with a lighter, more user-friendly layout.

The updated experience brings Name and Username together, introduces flag icons, and makes it easier to navigate directly to the User Detail page while preserving export behavior and filtering support.

#### **Salesforce Orgs – Callback URL Copy Support**

Guard now dynamically generates the callback URL during Salesforce org setup and provides a copy option directly in the Add Salesforce Org flow.

This streamlines configuration, improves accuracy across environments, and helps reduce setup friction when configuring the external client app in Salesforce.

#### **Prevent Password Reuse**

AutoRABIT Guard now enforces a password reuse restriction, preventing users from reusing previously used passwords. This enhancement improves overall security posture by ensuring stronger password hygiene and reducing the risk of compromised credentials being reused.

#### **Access Controls become Authorization Policies**

This update aligns AutoRABIT Guard with industry-standard infosec terminology and better reflects the scope and value of the feature. All references in the UI, workflows, notifications, and documentation have been updated accordingly. There are no changes to functionality, and existing configurations and permissions remain unaffected.

#### **Improved External Connected App (ECA) Credential Management**

The External Connected App (ECA) authentication flow has been enhanced to allow users to update OAuth credentials for existing org connections.

Users can now update the Client ID and Client Secret and trigger a fresh authentication flow without needing to delete and re-register the org. This reduces operational friction when credentials change and improves overall usability. Existing connected orgs are not impacted.

#### **External Connected App (ECA) Authentication Migration**

To align with Salesforce Spring ’26 security requirements, Guard has updated the authentication flow for External Connected Apps (ECA).

What’s changed:

* Guard now enforces Salesforce’s updated authentication standards for External Connected Apps.
* Connectivity remains seamless once authentication is configured.

Customer Action Required:

* When adding new Salesforce orgs via External Connected Apps, the following to be provided:
* Client ID
* Client Secret

What stays the same:

* No changes to core Guard functionality.
* No changes to user workflows after successful authentication.

This update ensures continued secure and compliant integration with Salesforce orgs under updated platform security requirements.

#### **Access Controls – Multi-Selection Support**

Access Control criteria creation has been enhanced to provide greater flexibility and precision when defining access rules.

Users can now select multiple Profiles, Roles, Company Names, and Domains when creating Access Control conditions, instead of being limited to a single value.

Existing Access Controls continue to function without any behavior changes, and all violation detection, auto-revert, and notification workflows remain unchanged.

#### **Access Controls – Modification Tracking**

Access Control detail pages now include Last Modified Date and Modified By fields to improve visibility into configuration changes.

This enhancement makes it easier for administrators to understand when an Access Control was last updated and by whom, supporting better governance and audit readiness. For newly created Access Controls, the creation date and creator are shown. For existing Access Controls, modification details are updated whenever changes are saved.

This change is informational only and does not impact Access Control enforcement or performance.

#### **Permission Explorer – Multi-Selection Filters**

Permission Explorer now supports multi-selection across query filters, enabling more advanced and targeted permission analysis.

Users can select multiple values for Profile, Role, Company Name, and Domain.

Selected filters are clearly visible in the UI and can be individually removed, making complex queries easier to build and adjust.

#### **Persistent Filters Across Guard**

Guard now remembers user-applied filters during a session, improving usability when navigating across features.

Once filters are applied, they remain active when users navigate away from a page, return later, or refresh the browser. Filter persistence is handled per feature and per user, ensuring that filters from one area do not affect another and that each user sees their own saved state.

Default filters continue to apply on initial login, and users can modify or clear filters at any time, with changes saved immediately.

#### **Filter-Aware Export**

Exports now include only records that match the currently applied filters, ensuring consistency between the UI and exported files. This enhancement applies to:

* Automated Data Classification
* API Security
* Change Monitoring
* User Activity Monitoring
* Risk Assessment

When no filters are applied, export behavior remains unchanged and continues to include all records using the default format.

#### **Change Monitoring – Content Settings Tracking**

Change Monitoring has been enhanced to provide greater visibility into content-related configuration changes.

Events related to content settings are now parsed and tracked, allowing administrators to better audit and understand changes made within Salesforce orgs.

#### **Change Monitoring – “Login as Any User” Event Tracking**

Change Monitoring now captures “Login as any user” events generated when administrators access user accounts using Salesforce’s delegated login capability.

These events are parsed and displayed in Change Monitoring in the Other tab, providing improved visibility into elevated access activity and supporting stronger audit and compliance requirements.

#### Additional Enhancements

* Access Controls – Support All Permissions Access Controls now support all permissions available in a Salesforce org, including permissions outside predefined categories.
* Partial syncing of Data Classifications to Salesforce Users can now choose which detected regulations to sync back to Salesforce on a per-field basis, with clear indicators for not synced classifications.
* Improved default view for Data Classification fields The Data Classification table now shows only fields created in the past three months by default, helping to focus on recent changes.
* Additional filtering in Data Classification New filters allow fields to be selected by Field Name and/or Sync status (Synced, Not Synced, Partially Synced).
* Visibility for unclassified fields Fields that weren’t classified now appear in the Data Classification table and are clearly marked as “None Detected,” with optional manual data scan action available.
* Expanded email domain support for Support Login Access (autorabit.com, autorabit.us) Support Login Access now allows authorized AutoRABIT support users from an additional approved email domain, while maintaining existing validation and audit.
* Improved stability of chatbot responses Enhanced handling and validation ensure more consistent and reliable responses from Guard’s expert.
* Updated menu and refreshed logo Minor UI updates improve visual consistency and overall user experience.

### **Bug Fixes** <a href="#bug-fixes" id="bug-fixes"></a>

#### **Authorization Policies – Profile Selection**

Authorization Policy creation now loads profile options more reliably for Salesforce orgs during policy setup, allowing users to continue policy configuration without profile dropdown interruptions.

#### **User Security Overview – Permission Set Names**

Permission Sets in User Security Overview now display readable Salesforce labels or names, making it easier for reviewers to understand assigned access without cross-checking technical values in Salesforce Setup.

#### **Salesforce Org Authentication Redirect**

After adding and authenticating an existing Salesforce org, Guard now completes the redirect flow cleanly and shows the organization as expected.

#### **User Activity Monitoring – Name Sorting**

Sorting by Name in User Activity Monitoring now correctly supports both ascending and descending order.

#### **User Activity Monitoring – Locked User Status**

Locked user indicators are now consistent across User Activity Monitoring and User Data details.

#### **User Security Overview – Login History**

Login History now displays accurate counts and supports pagination without request errors.

#### **Login Experience – Deactivated Users**

Users who are deactivated now receive a clear account-disabled message when attempting to log in.

#### **Permission Explorer – Custom Query Filters**

Permission Explorer custom queries now support additional filter fields more reliably, including profile-based conditions in Custom Explorer.

#### **User Activity Monitoring – Last Password Change Filter**

Filtering User Activity Monitoring by Last Password Change Date now completes successfully

#### **Guard Expert – Latest Release Notes Response**

Guard Expert now returns release information that aligns with the official Guard Knowledge Base release notes, helping users receive accurate and current product release details.

#### **Guard Expert – Organization Selection Handling**

Guard Expert now handles organization context more reliably, preventing intermittent failures caused by missing organization IDs.

#### **Salesforce Orgs – Reauthentication Flow**

Improved the reauthentication experience for Salesforce orgs so responses are handled correctly and there is a smoother flow.

#### **User Activity Monitoring – Inactive User Details**

Improved User Activity Monitoring so inactive user details are presented more clearly.

#### **Notifications – Invalid URL**

URLs have been updated in Change Notifications email templates.

#### **Improved Export Stability for Large Datasets**

Export processing has been improved to better handle large datasets, ensuring exports complete successfully even in high-volume environments. Export behavior and format remain unchanged.

#### **Duplicate Success Popups When Creating Real-Time Notifications**

Duplicate success messages when creating Real-Time Notifications are no longer shown. The system now displays a single, clear confirmation message.

#### **Session Token Expiration Error in Permission Explorer**

Fixed an intermittent issue that caused a “Session Token Expired” error when accessing Permission Explorer, ensuring uninterrupted usage.

#### **Permission Explorer Stuck on Org Switch**

Resolved loading issue when switching orgs with multiple permissions selected. Org switching complete successfully now (where applicable)

#### **Invalid ZIP when no Records found**

Exporting with no records was generating an invalid ZIP file. No-data exports are disabled now.

#### **Risk Assessment – Risk Name Typo**

Corrected a typo in a risk name to “Anonymous user access is properly restricted”.

#### **User Activity Monitoring – User Count by Profile**

Fixed an issue where User Count by Profile displayed incomplete data. Profile-based user counts are now accurate and consistent with overall user and license data.

#### **Change Monitoring – Intermittent “Subscription Error”**

Resolved an intermittent “Subscription Error” pop-up that occurred when switching filters or orgs in the Change Monitoring module. Filter navigation now works smoothly without errors.

#### Additional Fixes <a href="#enhancements-6" id="enhancements-6"></a>

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
