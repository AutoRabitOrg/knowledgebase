# Release Notes 25

## AutoRABIT Guard PubSec 25.2.9 Release Notes

**Release Date:  15 January 2026**

### New Features&#x20;

#### **Embedded Virtual Assistant**

A new in-product chatbot that provides real-time guidance on product features, navigation, troubleshooting, and best practices.

Includes:

* Floating in-app widget
* Natural language Q\&A
* Documentation-backed responses
* Smart fallback and escalation to Support

#### API Security Dashboard

Gain deeper insight into your connected apps and organizational exposure with the enhanced API Security Dashboard.

View key risk metrics, filter results by org, explore detailed app information, and export data for further analysis — all from a responsive, easy-to-use interface.

#### **Sync Data Classification Results to Salesforce**

We’re thrilled to announce that users can now sync Data Classification results directly back to their Salesforce org. This closes the loop between AutoRABIT Guard and Salesforce, keeping compliance data consistent and up to date.

**Highlights:**

* Push Data Classification results (compliance categorizations and relevant regulations) back to Salesforce.
* New table view with field selectors, compliance and regulation columns, and sync status.
* “Sync to Salesforce” button for bulk or individual field syncs.
* Field detail view enhanced with Compliance and Sync options.

**Impact:** Automates alignment between Guard and Salesforce for compliance data — reducing manual effort, errors, and audit risk.

#### **Salesforce Org Summary Dashboard**

A brand-new Org Summary Dashboard provides a unified overview of an org’s health, compliance, and risk posture.

**Highlights:**

* Aggregates data from multiple modules:
  * Risk Assessment
  * API Security
  * Permissions Explorer
* “Export Executive Report” is available for easy reporting
* Onboarding flow updated to include a dashboard overview.

**Impact:** Gives customers an executive-level view of org performance and compliance in one place.

#### **Support Login Access for Secure, Audited Troubleshooting**

We’re introducing Support Login Access—a secure, auditable way for AutoRABIT Support Engineers to access Guard instances with customer approval and full transparency.

**Highlights:**

* Dedicated “Grant temporary Support access” screen.
* Customers approve access by providing case details, support representative email, and preferred access duration (7, 15, or 30 days).
* Support users are created as read-only accounts; activity is fully logged and auditable.
* Customers can revoke access at any time.

**Impact:** Faster issue resolution with complete transparency, security, and customer control.

#### User Activity Monitoring <a href="#user-activity-monitoring" id="user-activity-monitoring"></a>

A new User Activity Monitoring section is now available under Compliance, giving admins real-time visibility into Salesforce users' activity.

**Highlights**

* Real-time monitoring
* Accessible via the standard org switcher
* Data sourced from Salesforce

**Why it matters**: Strengthens compliance visibility and enables proactive security monitoring of user behavior.

#### Change Monitoring Notifications <a href="#change-monitoring-notifications" id="change-monitoring-notifications"></a>

We’ve introduced a dedicated Real-time Change Notifications section with pre-built notification templates, making it easier to detect and respond to critical security-related changes.

**Highlights**

* Pre-built templates for key events, including:
  * Profile created
  * Password policy modified
  * User assigned to new profile
  * Sharing rules updated
  * Login IP ranges created/modified, or deleted
  * External credentials modified
  * Remote site settings updated
* Multi-org support for applying templates across environments
* Enhanced detail pages

**Why it matters**: Helps enforce Compliance requirements and ensures visibility into high-impact configuration changes.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Permissions Explorer Enhancements**

**Permission History**

A new Permission History feature allows users to select one or multiple permissions and view history of all modification events across profiles, permission sets, and permission set groups. Results are auto sorted by permission name for streamlined review.

**Alternative View by Profile/Permission Set**

A new view selector supports switching between:

* Matching Users (default)
* Matching Profiles
* Matching Permission Sets
* Matching Permission Set Groups

Available in both Permissions Explorer and Explore Object Access.

#### **Session-Wide Org Preselection**

Selecting a Salesforce org in any feature now auto-selects it across all features for the duration of the session. Logging out clears the selection.

#### **Salesforce Orgs Accessible from Main Menu**

Salesforce orgs are now directly accessible from the main navigation menu, improving discoverability and reducing navigation steps.

#### **Tenant Name Displayed in UI**

Users can now see their tenant's name next to the Release version in the bottom-left corner of the interface, providing better environment awareness.

#### **Spring Boot Upgrade**

The platform has been upgraded to Spring Boot 4.0 for enhanced performance, security, and framework stability.

#### **Salesforce Org Dashboard Enhancements**

* Added Change Monitoring and Data Classification widgets to the Salesforce Org Dashboard.
* Widgets link directly to their respective feature pages.
* Updated the Executive Report to include Change Monitoring and Data Classification insights.

#### **Password Hints**

* Added clear password requirement hints to the New Password screen.
* Helps users understand the strict password criteria and successfully set up their account.

#### **Permissions Explorer – Support All Permissions**

The Permissions Explorer now automatically supports all available Salesforce permissions, giving you a complete view of your org’s access setup.

A new “Other” category dynamically lists uncategorized permissions, ensuring nothing is missed and reducing manual effort.

#### **Permissions Explorer – Object Permissions Saved Queries**

You can now save custom Object Permission queries with names and descriptions, making it easy to revisit important configurations without rebuilding them each time.

#### **Help Section Improvements**

Access to support resources is now simpler. The Help menu has been redesigned to include quick links to the Support Portal, Guard Product Guide, and Support Login Access.

#### **Guard Home Page Update**

The Guard home page now features interactive cards that highlight recently added features. Each card links directly to its feature page for quick navigation, and the updated Change Monitoring card reflects the latest functionality for easier discovery.

#### **Re-authentication for Salesforce Orgs**

We’ve added a “Reauthenticate” button to simplify reconnecting Salesforce orgs without deleting them.

**Impact:** No more data loss when tokens expire—orgs, access controls, and rules stay intact.

#### **Display Risk Level of Changes in Change Monitoring**

**Module:** Change Monitoring Risk levels (Low, Medium, High) are now visually displayed for each change.

**Impact:** Greater visibility into risky activities and faster prioritization of security review.

#### **Capture Detailed Profile Permission Changes in Change Monitoring**

Change Monitoring now records granular details when user permissions change on Profiles, aligning with existing tracking for Permission Sets.

**Impact:** Improved traceability and audit accuracy, enabling downstream features.

#### **Tabular View in Risk Assessment**

Introduced an alternative table view for displaying risks, complete with sorting and filtering by name or properties.

**Impact:** Simplifies navigation and analysis, especially for large number of orgs.

#### **Separated Status and Severity in Risk Assessment**

The previous single “Status” field was split into two:

* Status: Unresolved, Resolved
* Severity: Warning, Critical

**Impact:** Improves clarity, ensuring severity and progress are tracked distinctly.

#### **Org Selection from Main Detail Page in Permissions Explorer**

Added the ability to change the org directly from the main detail page, streamlining workflows.

**Impact:** Saves time for admins managing multiple orgs.

#### **Show/Hide Frozen Users in Permissions Explorer**

Added a new “Show Frozen Users” checkbox in Custom Explorer.

* Unchecked (default): frozen users excluded.
* Checked: frozen users included.

**Impact:** Provides clarity and control in results interpretation.

#### Tenant Data Expiration & Deletion <a href="#tenant-data-expiration-and-deletion" id="tenant-data-expiration-and-deletion"></a>

Tenant data now has a mandatory expiration time to enforce lifecycle management.

**Highlights**

* Mandatory expiration is set at tenant creation.
* Automated tenant deletion is triggered on the expiration date.
* Advance notice: Tenant managers receive an email 5 days before deletion.

**Why it matters**: Ensures consistent data lifecycle management and enforces retention limits.

#### Event Logging & Audit Records <a href="#event-logging-and-audit-records" id="event-logging-and-audit-records"></a>

The platform now provides comprehensive event logging to strengthen accountability and monitoring.

**Highlights**

* Audit records for key events.
* Logs safeguarded against unauthorized modification or deletion.
* Supports audit reduction, correlation, and reporting for easier compliance review.

**Why it matters**: Provides robust traceability and supports effective security investigations.

### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

#### **Missing Salesforce Field**

User Activity Monitoring now works even in orgs missing the User.LastPasswordChangeDate field, preventing GQL errors.

#### **Risk Assessment fixes**

Multiple issues have been fixed, including:

* Incomplete Risk Assessment results
* Failure to refresh after Permission Explorer errors
* Errors parsing Salesforce API usage statistics
* Fixed the formatting of certificate details.
* Shows “No certificate created” when no certificates are available.

#### **“Sync to Salesforce” button**

* Fixed an issue with the Sync to Salesforce button appearing multiple times in Data Classification.

#### **Placeholder in Permission Explorer**

* Improved placeholder text shown in the Permission Explorer.
* The placeholder now displays the intended guidance.

#### **Permissions Explorer Field Error**

Fixed an issue where the “Approve Uninstalled Connected Apps” permission caused an error indicating that the field PermissionsCanApproveUninstalledApps did not exist in the PermissionSet entity.

#### **Permissions Explorer Not Displaying Permissions**

Resolved an issue where some permissions were not displaying correctly in the Custom Explorer view for some environments. Permissions now load correctly under their respective categories.

#### **Notification Rules in Delete Org Confirmation Modal**

Fixed an issue where the Delete Org confirmation modal displayed unrelated notification rules.

**Impact:** Now shows only items tied to the org being deleted, eliminating confusion.

### Additional fixes

* Salesforce Org Registration OAuth Error: Fixed an issue preventing new Salesforce Orgs from being registered due to OAuth flow failures.
* Password Reset Flow: Password policy error messages now clearly display complete requirements
* Permission Explorer – User Metadata: “User Created By” displays details properly
* Permission Explorer – Custom Objects: Object access results are displayed correctly for custom objects.
* Access Controls – User Dropdown Limit: Fixed limitation where only 2,000 users were displayed in the “Define Allowed Users” dropdown; now supports all users in large Salesforce Orgs.

***

## AutoRABIT Guard PubSec 25.2.4 Release Notes

**Release Date**: **12 September 2025**

### New features <a href="#api-security" id="api-security"></a>

#### API Security <a href="#api-security" id="api-security"></a>

We’re launching API Security to help customers identify and mitigate risks from third-party apps connected to Salesforce. As attacks on Salesforce orgs increase, including from unverified or over-permissive apps, this feature gives teams visibility into which apps are connected, how they’re being used, and whether they pose a risk.

AutoRABIT Guard introduces a new API Security tab under the Risk section. From here, users can inspect API activity for a specific Salesforce org in real time.

<img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FyMK4GAYDnbhUvCPE5Ams%252Fimage.png%3Falt%3Dmedia%26token%3De448eea7-e54e-4e4c-87d8-5d35ab3ae0cc&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=a4c4211a&#x26;sv=2" alt="" width="563">

**Value to Users:**

* Increased security visibility: Spot risky or shadow apps that might otherwise go unnoticed.
* Proactive defense: Prevent over-permissive apps from giving unauthorized users access to critical data.
* Multi-org management: Quickly assess and compare API risks across all Salesforce orgs.

### Enhancements

#### Permission Explorer Enhancements <a href="#permission-explorer-enhancements" id="permission-explorer-enhancements"></a>

**User Details at a Glance**&#x20;

Admins can now view detailed user information directly within Permissions Explorer, including:

* Full name, active/inactive status, and last login.
* Creator details and their current status.

This makes it faster to investigate suspicious permissions and strengthens overall security posture.

**Object-Level Access Insights**&#x20;

A New Object Access Mode makes it easy to see who can perform actions (Read, Create, Edit, Delete) on both standard and custom Salesforce objects. With filtering by Profile, Role, or Email, compliance audits and security reviews are now faster and more accurate.

**New Filters in Permissions Explorer** Permissions Explorer now offers additional Super Admin permission filters, including:

* Setup & Configuration access.
* AppExchange package downloads.
* Approval of uninstalled connected apps.

These updates give admins greater visibility into high-risk privileges.

#### Risk Assessment Improvements <a href="#risk-assessment-improvements" id="risk-assessment-improvements"></a>

* Business-Oriented Risk Labels: Risks are now described in simple, more understandable terms. Once resolved, risks display positive compliance outcomes to reinforce progress.
* Navigation Enhancements: Users can browse between risks with new “Previous” and “Next” buttons, cycling through seamlessly.
* Dedicated Risk Detail Page: Clicking on a specific risk now opens a full detail page, providing richer context and better usability.
* Certificate Settings Clarity: Updated UI labels make certificate key sizes and expiration values easier to understand and configure correctly.

These changes make Risk Assessment more accessible for both technical and non-technical stakeholders, while streamlining the review process.

#### Usability & UI Enhancements <a href="#usability-and-ui-enhancements" id="usability-and-ui-enhancements"></a>

* Information Hierarchy: Organizations are now grouped into clear priority categories (Critical, Quick Wins, Compliant), making it easier to focus remediation efforts.
* Improved Icon Visibility: Table header icons are now larger and easier to read, improving accessibility and UI consistency.
* Data Classification Transparency: A new “Non-Started” state prevents confusion and allows users to trigger analysis manually when needed.

#### Enhanced Export Capabilities <a href="#enhanced-export-capabilities" id="enhanced-export-capabilities"></a>

* **Change Monitoring Export**
  * Users can now export the **Change Monitoring** Changes table into CSV file.
  * Export includes all columns available in the UI, as well as _detail_ and _modifiedProperty_ fields for improved auditing and analysis.
* **Data Classification Export Enhancement**
  * The **Data Classification Export** now includes a new **rationale** column for each field in the CSV output.
  * Provides better context and justification for field classifications, improving clarity and audit readiness.
* **Risk Assessment Export**
  * A new **“Export Assessment”** button is now available in Risk Assessment.
  * Users can export the **entire assessment** as a CSV file.
* **API Security Export**
  * Customers can now export all data from the **API Security** page into a CSV file.
  * This export provides a complete view of connected applications and their security posture.

#### Other Enhancements <a href="#other-enhancements" id="other-enhancements"></a>

* Copy as JSON
  * A new **“Copy as JSON”** button has been added to the Permissions Explorer.

This feature allows users to copy the **entire JSON response**, which simplifies troubleshooting, data sharing, and downstream analysis.

### Bug Fixes <a href="#bug-fixes-6" id="bug-fixes-6"></a>

* Data Classification Export: Email notifications correctly include attached exports.
* Permissions Explorer: Accurate Access visibility ensured.
* User Management: Enforced validation for mandatory fields and added clear toast messages for success/error feedback.
* Implemented additional APIs and added extended logs for deeper insights during troubleshooting, improving visibility into system operations.

