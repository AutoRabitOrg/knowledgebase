# Release Notes 25.1

## Guard Release Notes 25.1.3

**Release Date: 21 May 2025**

AutoRABIT Guard's Automated Data Classification scans and classifies data based on major regulatory standards—PCI, HIPAA, GDPR, COPPA, and more. It provides visibility into sensitive data within your Salesforce environments and helps understand where and how it is used.

{% embed url="https://www.loom.com/share/d138a8ed553048bba934ef443012c18b?sid=bd90c408-8777-4a16-b168-f6f64328b1a0" %}
Automated Data Classification
{% endembed %}

Quick Explorer allows users to select one of the pre-built queries to get immediate security and access control insights.

{% embed url="https://www.loom.com/share/077b748c9ed44604bc7c51718506724f?sid=552fff8f-8ecd-464a-8260-fe41361eed83" %}
Permissions - Quick Explorer
{% endembed %}

Policy drafts can be created directly from Permissions Explorer now.

{% embed url="https://www.loom.com/share/9070ade3e393415f9096f3f7abfac3ed?sid=5f3e9b48-4ef3-42ea-a968-66b14d54a491" %}
Policy draft creation
{% endembed %}

Users can now filter risk assessment settings in relation to each of the compliance regulations: GDPR, HIPAA, PCI, PII, etc.&#x20;

For each risk, the user can see which categories are assigned to it and why.

{% embed url="https://www.loom.com/share/9ba90669b4464c06a5781629cafd2527?sid=2877e6e1-6341-4498-b52d-f3a59628f86b" %}
Compliance Information
{% endembed %}

We have added important information to the email received when a change happens in the monitored Salesforce org.&#x20;

{% embed url="https://www.loom.com/share/8bdb1d2868b5411eb8d5a52979c6d05b?sid=7bc9a234-1602-4f7d-b877-02b1909202be" %}
Email Notification
{% endembed %}

&#x20;

## Guard 25.1.2 Release Notes

**Release Date: 16 April 16 2025**

### **New Features**&#x20;

When users add their first Salesforce org, we automatically create two policies to be used as templates. This can help you understand policies a lot faster and use them as a starting point. &#x20;

{% embed url="https://www.loom.com/share/23f7e11276804cfb95e0f106a819e61c?sid=67f8cb82-7224-454e-8d6c-44339fc358e4" %}
Default policies assigned for first org
{% endembed %}

### Enhancements

**Additional Filters in Permissions Explorer:** Users can now add additional filters to the permissions explorer to better understand if there are overprivileged users.

{% embed url="https://www.loom.com/share/7a965014d3d44499997cef8efaa5e318?sid=feed1b0a-698e-47a8-9f3a-e73cc526fa5c" %}
New filters in Permissions Explorer
{% endembed %}

**New Metrics in Risk Assessment:** We now show an “overview” and “impact” on each risk of the Risk Assessment. This can help you understand more about each risk and how it impacts your org’s security posture.&#x20;

{% embed url="https://www.loom.com/share/b7e84e6a5ea142d28175dd756e0f3f8d?sid=15927096-c11f-4b41-ab42-2d608218e4da" %}
Details on the Risk Assessment
{% endembed %}

**Offending Changes Added to Monitoring Page:** We now show offending changes directly in the Change Monitoring page. Previously, offending changes were only visible from the Policy page.&#x20;

{% embed url="https://www.loom.com/share/99cefe3aed634cddadb38d92a996c4c7?sid=f76bd1ef-5fe3-40c7-bc2d-26edf4b1582b" %}
Viewing the Change Monitoring Page for Offending Changes
{% endembed %}

**Search in Permission Explorer:** It’s now easier to find permissions in the Permissions Explorer, using free-text search.

{% embed url="https://www.loom.com/share/fb0b0f7a1e3d4a1e88be8adbf07228fd?sid=598bfcdb-463d-4da5-898c-e9b89c3515a4" %}
Finding permissions in Permissions Explorer
{% endembed %}

***

## Guard 25.1.1 Release Notes

**Release Date: 21 March 2025**

### New Features

* **Multi-Factor Authentication (MFA) for Guard:** MFA is now implemented for Guard.
* **User Lockout After Failed Login Attempts:** Users will be locked out after three consecutive failed login attempts and notified via email.
* **New Settings Page:** The Admin section has been moved to the profile menu for improved navigation. Users can access Settings from the dropdown menu, which includes Salesforce Orgs and User Management.
* **Criteria-Based Policies for Permissions:** Users can now create criteria-based policies for permission-specific policies, extending the existing capability for permission set policies.

### Enhancements

* **Removal of Clickjack Protection Setting from Risk Assessment:** The Enable Clickjack Protection for Setup pages setting has been removed from Risk Assessment due to Salesforce limitations.
* **Rebranding of SPM to Guard in Emails:** All customer-facing emails now display "Guard" instead of "SPM."
* **Identification of Sandbox Type Upon Login:** Guard now determines and stores the sandbox type for usage tracking when a sandbox org is registered.
* **Move Management Console to Settings Page:** The Management Console is now integrated into the Settings page, and the Delete User button has been relocated to the User Detail page.
