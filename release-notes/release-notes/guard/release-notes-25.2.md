# Guard Release Notes 25.2

## Guard 25.2.7 Release Notes&#x20;

**Release Date:** 29 October 2025&#x20;

### New Features & Enhancements&#x20;

#### API Security Dashboard&#x20;

Gain deeper insight into your connected apps and organizational exposure with the enhanced API Security Dashboard. &#x20;

View key risk metrics, filter results by org, explore detailed app information, and export data for further analysis — all from a responsive, easy-to-use interface.&#x20;

#### Permissions Explorer – Support All Permissions&#x20;

The Permissions Explorer now automatically supports all available Salesforce permissions, giving you a complete view of your org’s access setup. &#x20;

A new “Other” category dynamically lists uncategorized permissions, ensuring nothing is missed and reducing manual effort.&#x20;

#### Permissions Explorer – Object Permissions Saved Queries&#x20;

You can now save custom Object Permission queries with names and descriptions, making it easy to revisit important configurations without rebuilding them each time.&#x20;

#### Help Section Improvements&#x20;

Access to support resources is now simpler. The Help menu has been redesigned to include quick links to the Support Portal, Guard Product Guide, and Support Login Access.&#x20;

#### Guard Home Page Update&#x20;

The Guard home page now features interactive cards that highlight recently added features. Each card links directly to its feature page for quick navigation, and the updated Change Monitoring card reflects the latest functionality for easier discovery.&#x20;

### Bug Fixes&#x20;

#### Permissions Explorer Field Error&#x20;

Fixed an issue where the “Approve Uninstalled Connected Apps” permission caused an error indicating that the field PermissionsCanApproveUninstalledApps did not exist in the PermissionSet entity. &#x20;

#### Permissions Explorer Not Displaying Permissions&#x20;

Resolved an issue where some permissions were not displaying correctly in the Custom Explorer view for some environments. Permissions now load correctly under their respective categories.

***

## Guard 25.2.6 Release Notes&#x20;

**Release Date:** 15 October 2025&#x20;

### Sync Data Classification Results to Salesforce&#x20;

We’re thrilled to announce that users can now sync Data Classification results directly back to their Salesforce org. This closes the loop between AutoRABIT Guard and Salesforce, keeping compliance data consistent and up to date.&#x20;

**Highlights:**&#x20;

* Push Data Classification results (compliance categorizations and relevant regulations) back to Salesforce.&#x20;
* New table view with field selectors, compliance and regulation columns, and sync status.&#x20;
* “Sync to Salesforce” button for bulk or individual field syncs.
* Field detail view enhanced with Compliance and Sync options.&#x20;

**Impact:** \
Automates alignment between Guard and Salesforce for compliance data — reducing manual effort, errors, and audit risk.&#x20;

### Salesforce Org Summary Dashboard&#x20;

A brand-new Org Summary Dashboard provides a unified overview of an org’s health, compliance, and risk posture.&#x20;

**Highlights:**&#x20;

* Aggregates data from multiple modules:&#x20;
  * Risk Assessment&#x20;
  * API Security&#x20;
  * Permissions Explorer&#x20;
* “Export Executive Report” is available for easy reporting&#x20;
* Onboarding flow updated to include a dashboard overview.&#x20;

**Impact:** \
Gives customers an executive-level view of org performance and compliance in one place.&#x20;

### Support Login Access for Secure, Audited Troubleshooting&#x20;

We’re introducing Support Login Access—a secure, auditable way for AutoRABIT Support Engineers to access Guard instances with customer approval and full transparency.&#x20;

**Highlights:**&#x20;

* Dedicated “Grant temporary Support access” screen.
* Customers approve access by providing case details, support representative email, and preferred access duration (7, 15, or 30 days).&#x20;
* Support users are created as read-only accounts; activity is fully logged and auditable.&#x20;
* Customers can revoke access at any time.&#x20;

**Impact:** \
Faster issue resolution with complete transparency, security, and customer control.&#x20;

### Enhancements&#x20;

#### Re-authentication for Salesforce Orgs&#x20;

We’ve added a “Reauthenticate” button to simplify reconnecting Salesforce orgs without deleting them.&#x20;

**Impact:** \
No more data loss when tokens expire—orgs, access controls, and rules stay intact.&#x20;

#### Display Risk Level of Changes in Change Monitoring&#x20;

**Module:** Change Monitoring \
Risk levels (Low, Medium, High) are now visually displayed for each change.&#x20;

**Impact:** \
Greater visibility into risky activities and faster prioritization of security review.&#x20;

#### Capture Detailed Profile Permission Changes in Change Monitoring&#x20;

Change Monitoring now records granular details when user permissions change on Profiles, aligning with existing tracking for Permission Sets.&#x20;

**Impact:** \
Improved traceability and audit accuracy, enabling downstream features.&#x20;

#### Tabular View in Risk Assessment&#x20;

Introduced an alternative table view for displaying risks, complete with sorting and filtering by name or properties.&#x20;

**Impact:** \
Simplifies navigation and analysis, especially for large number of orgs.&#x20;

#### Separated Status and Severity in Risk Assessment&#x20;

The previous single “Status” field was split into two:&#x20;

* Status: Unresolved, Resolved&#x20;
* Severity: Warning, Critical&#x20;

**Impact:** \
Improves clarity, ensuring severity and progress are tracked distinctly.&#x20;

#### Org Selection from Main Detail Page in Permissions Explorer&#x20;

Added the ability to change the org directly from the main detail page, streamlining workflows.&#x20;

**Impact:** \
Saves time for admins managing multiple orgs.&#x20;

#### Show/Hide Frozen Users in Permissions Explorer&#x20;

Added a new “Show Frozen Users” checkbox in Custom Explorer.&#x20;

* Unchecked (default): frozen users excluded.&#x20;
* Checked: frozen users included.&#x20;

**Impact:** \
Provides clarity and control in results interpretation.&#x20;

### Bug Fixes&#x20;

#### Notification Rules in Delete Org Confirmation Modal&#x20;

Fixed an issue where the Delete Org confirmation modal displayed unrelated notification rules.&#x20;

**Impact:** \
Now shows only items tied to the org being deleted, eliminating confusion.

***

## Guard 25.2.5 Release Notes&#x20;

**Release Date**: 24 September 2025

### User Activity Monitoring&#x20;

A new User Activity Monitoring section is now available under Compliance, giving admins real-time visibility into Salesforce users' activity.&#x20;

**Highlights**&#x20;

* Real-time monitoring&#x20;
* Accessible via the standard org switcher&#x20;
* Data sourced from Salesforce&#x20;

**Why it matters**: Strengthens compliance visibility and enables proactive security monitoring of user behavior.&#x20;

### Change Monitoring Notifications&#x20;

We’ve introduced a dedicated Real-time Change Notifications section with pre-built notification templates, making it easier to detect and respond to critical security-related changes.&#x20;

**Highlights**&#x20;

* Pre-built templates for key events, including:&#x20;
  * Profile created&#x20;
  * Password policy modified&#x20;
  * User assigned to new profile&#x20;
  * Sharing rules updated&#x20;
  * Login IP ranges created/modified, or deleted&#x20;
  * External credentials modified&#x20;
  * Remote site settings updated&#x20;
* Multi-org support for applying templates across environments&#x20;
* Enhanced detail pages&#x20;

**Why it matters**: Helps enforce Compliance requirements and ensures visibility into high-impact configuration changes.

### Tenant Data Expiration & Deletion&#x20;

Tenant data now has a mandatory expiration time to enforce lifecycle management.&#x20;

**Highlights**&#x20;

* Mandatory expiration is set at tenant creation.&#x20;
* Automated tenant deletion is triggered on the expiration date.&#x20;
* Advance notice: Tenant managers receive an email 5 days before deletion.&#x20;

**Why it matters**: Ensures consistent data lifecycle management and enforces retention limits.&#x20;

### Event Logging & Audit Records&#x20;

The platform now provides comprehensive event logging to strengthen accountability and monitoring.&#x20;

**Highlights**&#x20;

* Audit records for key events.
* Logs safeguarded against unauthorized modification or deletion.&#x20;
* Supports audit reduction, correlation, and reporting for easier compliance review.&#x20;

**Why it matters**: Provides robust traceability and supports effective security investigations.&#x20;

### Bug Fixes&#x20;

* Salesforce Org Registration OAuth Error: Fixed an issue preventing new Salesforce Orgs from being registered due to OAuth flow failures. &#x20;
* Password Reset Flow: Password policy error messages now clearly display complete requirements&#x20;
* Permission Explorer – User Metadata: “User Created By” displays details properly&#x20;
* Permission Explorer – Custom Objects: Object access results are displayed correctly for custom objects.&#x20;
* Access Controls – User Dropdown Limit: Fixed limitation where only 2,000 users were displayed in the “Define Allowed Users” dropdown; now supports all users in large Salesforce Orgs.&#x20;

***

## Guard 25.2.4.3 Release Notes

**Release Date**: 15 September 2025

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

### Other Enhancements

* Copy as JSON
  * A new **“Copy as JSON”** button has been added to the Permissions Explorer.

This feature allows users to copy the **entire JSON response**, which simplifies troubleshooting, data sharing, and downstream analysis.

### Bug Fixes

* Implemented additional APIs and added extended logs for deeper insights during troubleshooting, improving visibility into system operations.

***

## Guard 25.2.4 Release Notes

**Release Date: 10 September 2025**

### API Security

We’re launching API Security in Guard to help customers identify and mitigate risks from third-party apps connected to Salesforce. As attacks on Salesforce orgs increase, including from unverified or over-permissive apps, this feature gives teams visibility into which apps are connected, how they’re being used, and whether they pose a risk.

AutoRABIT Guard introduces a new API Security tab under the Risk section. From here, users can inspect API activity for a specific Salesforce org in real time.

<figure><img src="../../../.gitbook/assets/image (2010).png" alt=""><figcaption></figcaption></figure>

**Value to Users:**

* Increased security visibility: Spot risky or shadow apps that might otherwise go unnoticed.
* Proactive defense: Prevent over-permissive apps from giving unauthorized users access to critical data.
* Multi-org management: Quickly assess and compare API risks across all Salesforce orgs.

### Permission Explorer Enhancements

**User Details at a Glance**\
&#x20;Admins can now view detailed user information directly within Permissions Explorer, including:

* Full name, active/inactive status, and last login.
* Creator details and their current status.

This makes it faster to investigate suspicious permissions and strengthens overall security posture.

**Object-Level Access Insights**\
&#x20;A New Object Access Mode makes it easy to see who can perform actions (Read, Create, Edit, Delete) on both standard and custom Salesforce objects. With filtering by Profile, Role, or Email, compliance audits and security reviews are now faster and more accurate.

**New Filters in Permissions Explorer**\
&#x20;Permissions Explorer now offers additional Super Admin permission filters, including:

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

### Bug Fixes

* Data Classification Export: Email notifications correctly include attached exports.
* Permissions Explorer: Accurate Access visibility ensured.
* User Management: Enforced validation for mandatory fields and added clear toast messages for success/error feedback.

### Backend & Infrastructure

* Database Cleanup: Removed legacy tables for improved performance and maintainability.
* Tenant Deletion API: A new API introduced to enable safe and auditable tenant removal.

***

## Guard 25.2.3 Release Notes

**Release Date: 20 August 2025**

### New User Creation Simplified

Creating new users is now faster and more flexible. Admins can set up accounts with just an **email address** and **role**. Other details (username, first name, and last name) are optional and hidden by default but can be filled out as needed.

* The system now **automatically handles username conflicts** by suggesting available alternatives.
*   The **user list view** and **user icons** have been updated to reflect these enhancements.\


    <figure><img src="../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>



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
&#x20;This ensures:

* Sensitive authentication data is securely transmitted.
* Reduced risk of data interception or tampering.
* Compliance with **federal security standards**.

### Bug Fixes

* **User Unlocking**: Resolved an issue with locked accounts that couldn’t be unlocked from the Settings page. Admins can now restore users' access without any errors.

### Other Enhancements

* **Security & Compliance**: We have strengthened our platform’s security by implementing targeted improvements that meet stringent federal standards. These updates reduce potential attack surfaces and further enhance data protection.
* Implemented a few back-end optimizations to enhance system stability and ensure long-term maintainability, supporting a smoother and more reliable user experience.

***

## Guard 25.2.2 Release Notes

**Release Date: 23 July 2025**

1. Risk Assessment is goal-oriented now!

<figure><img src="../../../.gitbook/assets/image (1816).png" alt="" width="563"><figcaption></figcaption></figure>

We have grouped risks under four key Security Goals:

**Goal 1: Establish Secure Access & Identity**

Ensuring only authorized users access Salesforce, their identities are verified, and highly privileged access is governed.

**Goal 2: Harden Application & Session Security**

Protecting the Salesforce application from common web vulnerabilities, ensuring secure communication, and maintaining user session integrity.

**Goal 3: Safeguard Data & Control Exposure**

Protecting data confidentiality and integrity by managing sharing settings, controlling access to sensitive information, and limiting guest user access.

**Goal 4: Ensure Foundational Platform Integrity**

Maintaining the core security of the Salesforce platform via valid configurations for certificates, encryption, and secure external connections.

Users can see their progress towards achieving each Goal and remediate the associated risks accordingly.&#x20;

2. Custom Permission Explorer queries can be saved

Just give your query a name and definitive description, and it will be saved for your future revisits:

<figure><img src="../../../.gitbook/assets/image (1817).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1818).png" alt=""><figcaption></figcaption></figure>

3. New home page

To help navigate and get instant value, we are happy to introduce a brand-new home page:

<figure><img src="../../../.gitbook/assets/image (1819).png" alt=""><figcaption></figcaption></figure>

4. Instance version details are available now in the bottom left corner of the expanded page:

<figure><img src="../../../.gitbook/assets/image (1820).png" alt=""><figcaption></figcaption></figure>

5. New menu

To improve application navigation, in this release we have added a new menu:

<figure><img src="../../../.gitbook/assets/image (1821).png" alt=""><figcaption></figcaption></figure>

6. While we enhance its performance and functionality, we have temporarily removed the Field usage (data) tab from Data Classification UI:

<figure><img src="../../../.gitbook/assets/image (1822).png" alt=""><figcaption></figcaption></figure>

### Bug Fixes

1\.      Zoho desk link now works as expected.

2\.      User menu is no longer cut off by browser window.
