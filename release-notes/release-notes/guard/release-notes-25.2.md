# Guard Release Notes 25.2

{% @mailchimp/mailchimpSubscribe cta="Guard Release Notes Mailing List:" listId="a085e26e7e" %}

## Guard 25.2.9

**Release date:** 3 December 2025

### New features

#### Embedded Virtual Assistant

A new in-product chatbot that provides real-time guidance on product features, navigation, troubleshooting, and best practices.

Includes:

* Floating in-app widget
* Natural language Q\&A
* Documentation-backed responses
* Smart fallback and escalation to Support

### Enhancements

#### Permissions Explorer Enhancements

**Permission History**

A new Permission History feature allows users to select one or multiple permissions and view history of all modification events across profiles, permission sets, and permission set groups. Results are auto sorted by permission name for streamlined review.

**Alternative View by Profile/Permission Set**

A new view selector supports switching between:

* Matching Users (default)
* Matching Profiles
* Matching Permission Sets
* Matching Permission Set Groups

Available in both Permissions Explorer and Explore Object Access.

#### Session-Wide Org Preselection

Selecting a Salesforce org in any feature now auto-selects it across all features for the duration of the session. Logging out clears the selection.

#### Salesforce Orgs Accessible from Main Menu

Salesforce orgs are now directly accessible from the main navigation menu, improving discoverability and reducing navigation steps.

#### Tenant Name Displayed in UI

Users can now see their tenant's name next to the Release version in the bottom-left corner of the interface, providing better environment awareness.

#### Spring Boot Upgrade

The platform has been upgraded to Spring Boot 4.0 for enhanced performance, security, and framework stability.

### Fixes

#### Missing Salesforce Field

User Activity Monitoring now works even in orgs missing the User.LastPasswordChangeDate field, preventing GQL errors.

#### Risk Assessment

Multiple issues have been fixed, including:

* Incomplete Risk Assessment results
* Failure to refresh after Permission Explorer errors
* Errors parsing Salesforce API usage statistics

***

## Guard 25.2.8

**Release date:** 26 November 2025

### Enhancements

#### Salesforce Org Dashboard Enhancements

* Added Change Monitoring and Data Classification widgets to the Salesforce Org Dashboard.
* Widgets link directly to their respective feature pages.
* Updated the Executive Report to include Change Monitoring and Data Classification insights.

#### Password Hints

* Added clear password requirement hints to the New Password screen.
* Helps users understand the strict password criteria and successfully set up their account.

### Fixes

#### Risk Assessment: Certificate Values

* Fixed the formatting of certificate details.
* Shows “No certificate created” when no certificates are available.

#### “Sync to Salesforce” button

* Fixed an issue with the Sync to Salesforce button appearing multiple times in Data Classification.

#### Placeholder in Permission Explorer

* Improved placeholder text shown in the Permission Explorer.
* The placeholder now displays the intended guidance.

***

## Guard 25.2.7

**Release date:** 29 October 2025

### New Features & Enhancements

#### API Security Dashboard

Gain deeper insight into your connected apps and organizational exposure with the enhanced API Security Dashboard.

View key risk metrics, filter results by org, explore detailed app information, and export data for further analysis — all from a responsive, easy-to-use interface.

#### Permissions Explorer – Support All Permissions

The Permissions Explorer now automatically supports all available Salesforce permissions, giving you a complete view of your org’s access setup.

A new “Other” category dynamically lists uncategorized permissions, ensuring nothing is missed and reducing manual effort.

#### Permissions Explorer – Object Permissions Saved Queries

You can now save custom Object Permission queries with names and descriptions, making it easy to revisit important configurations without rebuilding them each time.

#### Help Section Improvements

Access to support resources is now simpler. The Help menu has been redesigned to include quick links to the Support Portal, Guard Product Guide, and Support Login Access.

#### Guard Home Page Update

The Guard home page now features interactive cards that highlight recently added features. Each card links directly to its feature page for quick navigation, and the updated Change Monitoring card reflects the latest functionality for easier discovery.

### Fixes

#### Permissions Explorer Field Error

Fixed an issue where the “Approve Uninstalled Connected Apps” permission caused an error indicating that the field PermissionsCanApproveUninstalledApps did not exist in the PermissionSet entity.

#### Permissions Explorer Not Displaying Permissions

Resolved an issue where some permissions were not displaying correctly in the Custom Explorer view for some environments. Permissions now load correctly under their respective categories.

***

## Guard 25.2.6

**Release date:** 15 October 2025

### New features

#### Sync Data Classification Results to Salesforce

We’re thrilled to announce that users can now sync Data Classification results directly back to their Salesforce org. This closes the loop between AutoRABIT Guard and Salesforce, keeping compliance data consistent and up to date.

**Highlights:**

* Push Data Classification results (compliance categorizations and relevant regulations) back to Salesforce.
* New table view with field selectors, compliance and regulation columns, and sync status.
* “Sync to Salesforce” button for bulk or individual field syncs.
* Field detail view enhanced with Compliance and Sync options.

**Impact:** Automates alignment between Guard and Salesforce for compliance data — reducing manual effort, errors, and audit risk.

#### Salesforce Org Summary Dashboard

A brand-new Org Summary Dashboard provides a unified overview of an org’s health, compliance, and risk posture.

**Highlights:**

* Aggregates data from multiple modules:
  * Risk Assessment
  * API Security
  * Permissions Explorer
* “Export Executive Report” is available for easy reporting
* Onboarding flow updated to include a dashboard overview.

**Impact:** Gives customers an executive-level view of org performance and compliance in one place.

#### Support Login Access for Secure, Audited Troubleshooting

We’re introducing Support Login Access—a secure, auditable way for AutoRABIT Support Engineers to access Guard instances with customer approval and full transparency.

**Highlights:**

* Dedicated “Grant temporary Support access” screen.
* Customers approve access by providing case details, support representative email, and preferred access duration (7, 15, or 30 days).
* Support users are created as read-only accounts; activity is fully logged and auditable.
* Customers can revoke access at any time.

**Impact:** Faster issue resolution with complete transparency, security, and customer control.

### Enhancements

#### Re-authentication for Salesforce Orgs

We’ve added a “Reauthenticate” button to simplify reconnecting Salesforce orgs without deleting them.

**Impact:** No more data loss when tokens expire—orgs, access controls, and rules stay intact.

#### Display Risk Level of Changes in Change Monitoring

**Module:** Change Monitoring\
Risk levels (Low, Medium, High) are now visually displayed for each change.

**Impact:** Greater visibility into risky activities and faster prioritization of security review.

#### Capture Detailed Profile Permission Changes in Change Monitoring

Change Monitoring now records granular details when user permissions change on Profiles, aligning with existing tracking for Permission Sets.

**Impact:** Improved traceability and audit accuracy, enabling downstream features.

#### Tabular View in Risk Assessment

Introduced an alternative table view for displaying risks, complete with sorting and filtering by name or properties.

**Impact:** Simplifies navigation and analysis, especially for large number of orgs.

#### Separated Status and Severity in Risk Assessment

The previous single “Status” field was split into two:

* Status: Unresolved, Resolved
* Severity: Warning, Critical

**Impact:** Improves clarity, ensuring severity and progress are tracked distinctly.

#### Org Selection from Main Detail Page in Permissions Explorer

Added the ability to change the org directly from the main detail page, streamlining workflows.

**Impact:**\
Saves time for admins managing multiple orgs.

#### Show/Hide Frozen Users in Permissions Explorer

Added a new “Show Frozen Users” checkbox in Custom Explorer.

* Unchecked (default): frozen users excluded.
* Checked: frozen users included.

**Impact:**\
Provides clarity and control in results interpretation.

### Fixes

#### Notification Rules in Delete Org Confirmation Modal

Fixed an issue where the Delete Org confirmation modal displayed unrelated notification rules.

**Impact:**\
Now shows only items tied to the org being deleted, eliminating confusion.

***

## Guard 25.2.5

**Release date:** 24 September 2025

### User Activity Monitoring

A new User Activity Monitoring section is now available under Compliance, giving admins real-time visibility into Salesforce users' activity.

**Highlights**

* Real-time monitoring
* Accessible via the standard org switcher
* Data sourced from Salesforce

**Why it matters**: Strengthens compliance visibility and enables proactive security monitoring of user behavior.

### Change Monitoring Notifications

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

### Tenant Data Expiration & Deletion

Tenant data now has a mandatory expiration time to enforce lifecycle management.

**Highlights**

* Mandatory expiration is set at tenant creation.
* Automated tenant deletion is triggered on the expiration date.
* Advance notice: Tenant managers receive an email 5 days before deletion.

**Why it matters**: Ensures consistent data lifecycle management and enforces retention limits.

### Event Logging & Audit Records

The platform now provides comprehensive event logging to strengthen accountability and monitoring.

**Highlights**

* Audit records for key events.
* Logs safeguarded against unauthorized modification or deletion.
* Supports audit reduction, correlation, and reporting for easier compliance review.

**Why it matters**: Provides robust traceability and supports effective security investigations.

### Fixes

* Salesforce Org Registration OAuth Error: Fixed an issue preventing new Salesforce Orgs from being registered due to OAuth flow failures.
* Password Reset Flow: Password policy error messages now clearly display complete requirements
* Permission Explorer – User Metadata: “User Created By” displays details properly
* Permission Explorer – Custom Objects: Object access results are displayed correctly for custom objects.
* Access Controls – User Dropdown Limit: Fixed limitation where only 2,000 users were displayed in the “Define Allowed Users” dropdown; now supports all users in large Salesforce Orgs.

***

## Guard 25.2.4.3

**Release date:** 15 September 2025

### Enhanced Export Capabilities

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

### Enhancements

* Copy as JSON
  * A new **“Copy as JSON”** button has been added to the Permissions Explorer.

This feature allows users to copy the **entire JSON response**, which simplifies troubleshooting, data sharing, and downstream analysis.

### Fixes

* Implemented additional APIs and added extended logs for deeper insights during troubleshooting, improving visibility into system operations.

***

## Guard 25.2.4

**Release date:** 10 September 2025

### API Security

We’re launching API Security in Guard to help customers identify and mitigate risks from third-party apps connected to Salesforce. As attacks on Salesforce orgs increase, including from unverified or over-permissive apps, this feature gives teams visibility into which apps are connected, how they’re being used, and whether they pose a risk.

AutoRABIT Guard introduces a new API Security tab under the Risk section. From here, users can inspect API activity for a specific Salesforce org in real time.

<figure><img src="../../../.gitbook/assets/image (1986).png" alt=""><figcaption></figcaption></figure>

**Value to Users:**

* Increased security visibility: Spot risky or shadow apps that might otherwise go unnoticed.
* Proactive defense: Prevent over-permissive apps from giving unauthorized users access to critical data.
* Multi-org management: Quickly assess and compare API risks across all Salesforce orgs.

### Permission Explorer Enhancements

**User Details at a Glance**\
Admins can now view detailed user information directly within Permissions Explorer, including:

* Full name, active/inactive status, and last login.
* Creator details and their current status.

This makes it faster to investigate suspicious permissions and strengthens overall security posture.

**Object-Level Access Insights**\
A New Object Access Mode makes it easy to see who can perform actions (Read, Create, Edit, Delete) on both standard and custom Salesforce objects. With filtering by Profile, Role, or Email, compliance audits and security reviews are now faster and more accurate.

**New Filters in Permissions Explorer**\
Permissions Explorer now offers additional Super Admin permission filters, including:

* Setup & Configuration access.
* AppExchange package downloads.
* Approval of uninstalled connected apps.

These updates give admins greater visibility into high-risk privileges.

### Risk Assessment Improvements

* Business-Oriented Risk Labels: Risks are now described in simple, more understandable terms. Once resolved, risks display positive compliance outcomes to reinforce progress.
* Navigation Enhancements: Users can browse between risks with new “Previous” and “Next” buttons, cycling through seamlessly.
* Dedicated Risk Detail Page: Clicking on a specific risk now opens a full detail page, providing richer context and better usability.
* Certificate Settings Clarity: Updated UI labels make certificate key sizes and expiration values easier to understand and configure correctly.

These changes make Risk Assessment more accessible for both technical and non-technical stakeholders, while streamlining the review process.

### Usability & UI Enhancements

* Information Hierarchy: Organizations are now grouped into clear priority categories (Critical, Quick Wins, Compliant), making it easier to focus remediation efforts.
* Improved Icon Visibility: Table header icons are now larger and easier to read, improving accessibility and UI consistency.
* Data Classification Transparency: A new “Non-Started” state prevents confusion and allows users to trigger analysis manually when needed.

### Fixes

* Data Classification Export: Email notifications correctly include attached exports.
* Permissions Explorer: Accurate Access visibility ensured.
* User Management: Enforced validation for mandatory fields and added clear toast messages for success/error feedback.

### Backend & Infrastructure

* Database Cleanup: Removed legacy tables for improved performance and maintainability.
* Tenant Deletion API: A new API introduced to enable safe and auditable tenant removal.

***

## Guard 25.2.3

**Release date:** 20 August 2025

### New User Creation Simplified

Creating new users is now faster and more flexible. Admins can set up accounts with just an **email address** and **role**. Other details (username, first name, and last name) are optional and hidden by default but can be filled out as needed.

* The system now **automatically handles username conflicts** by suggesting available alternatives.
*   The **user list view** and **user icons** have been updated to reflect these enhancements.<br>

    <figure><img src="../../../.gitbook/assets/image (1933).png" alt=""><figcaption></figcaption></figure>

### Improved Account Protection

To enhance security and prevent accidental or malicious account removals:

* **Admins** can no longer delete or deactivate their own accounts but still can manage Standard User accounts.
* **Standard Users** cannot delete or deactivate their own or any other accounts.

This change helps maintain system stability and protects privileged accounts.

### Stronger Role Management Controls

We’ve introduced new safeguards to reduce the risk of privilege loss or escalation:

* Admins can no longer **downgrade themselves** to Standard User.
* Admins can still **promote Standard Users** to Admin.
* Standard Users cannot change anyone’s role.
* All role changes are now logged for better auditing and compliance.

### Single Sign-On (SSO) with Enhanced Security

Guard now supports **Single Sign-On (SSO)** using **encrypted SAML assertions**.\
This ensures:

* Sensitive authentication data is securely transmitted.
* Reduced risk of data interception or tampering.
* Compliance with **federal security standards**.

### Fixes

* **User Unlocking**: Resolved an issue with locked accounts that couldn’t be unlocked from the Settings page. Admins can now restore users' access without any errors.

### Enhancements

* **Security & Compliance**: We have strengthened our platform’s security by implementing targeted improvements that meet stringent federal standards. These updates reduce potential attack surfaces and further enhance data protection.
* Implemented a few back-end optimizations to enhance system stability and ensure long-term maintainability, supporting a smoother and more reliable user experience.

***

## Guard 25.2.2

**Release date:** 23 July 2025

1. Risk Assessment is goal-oriented now!

<figure><img src="../../../.gitbook/assets/image (1926).png" alt="" width="563"><figcaption></figcaption></figure>

We have grouped risks under four key Security Goals:

**Goal 1: Establish Secure Access & Identity**

Ensuring only authorized users access Salesforce, their identities are verified, and highly privileged access is governed.

**Goal 2: Harden Application & Session Security**

Protecting the Salesforce application from common web vulnerabilities, ensuring secure communication, and maintaining user session integrity.

**Goal 3: Safeguard Data & Control Exposure**

Protecting data confidentiality and integrity by managing sharing settings, controlling access to sensitive information, and limiting guest user access.

**Goal 4: Ensure Foundational Platform Integrity**

Maintaining the core security of the Salesforce platform via valid configurations for certificates, encryption, and secure external connections.

Users can see their progress towards achieving each Goal and remediate the associated risks accordingly.

2. Custom Permission Explorer queries can be saved

Just give your query a name and definitive description, and it will be saved for your future revisits:

<figure><img src="../../../.gitbook/assets/image (1927).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1928).png" alt=""><figcaption></figcaption></figure>

3. New home page

To help navigate and get instant value, we are happy to introduce a brand-new home page:

<figure><img src="../../../.gitbook/assets/image (1929).png" alt=""><figcaption></figcaption></figure>

4. Instance version details are available now in the bottom left corner of the expanded page:

<figure><img src="../../../.gitbook/assets/image (1930).png" alt=""><figcaption></figcaption></figure>

5. New menu

To improve application navigation, in this release we have added a new menu:

<figure><img src="../../../.gitbook/assets/image (1931).png" alt=""><figcaption></figcaption></figure>

6. While we enhance its performance and functionality, we have temporarily removed the Field usage (data) tab from Data Classification UI:

<figure><img src="../../../.gitbook/assets/image (1932).png" alt=""><figcaption></figcaption></figure>

### Fixes

1\. Zoho desk link now works as expected.

2\. User menu is no longer cut off by browser window.
