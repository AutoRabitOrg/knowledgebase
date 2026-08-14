# AutoRABIT Guard Release Notes 26.2

<figure><img src="../../../.gitbook/assets/Guard_Banner 2 (1).png" alt=""><figcaption></figcaption></figure>

## AutoRABIT Guard 26.2.4 Release Notes

Release Date: 19 August 2026

### New features

#### Digital Experience Assessment

Guard now provides a dedicated Digital Experience Assessment area for Salesforce Experience Cloud sites built using Aura or LWR.

Users can initiate scans, filter scan history and review detected security findings, exposed objects and fields, exposed files, external domains and trusted sites.

When Automated Data Classification is enabled, scan results can also identify exposed fields containing sensitive data and display the associated regulatory classifications.

A new Security Risks Library shows the checks Guard performs, including each risk’s framework, category and severity. Administrators can accept risks for selected sites, manage exclusions and review an activity log showing who changed each exclusion.

#### Drift Policies: User-specific access changes

Drift Policies can now monitor changes to individual users.

Administrators can create rules for changes to a user’s role, profile or license. Rules can detect any change or specific transitions, and multiple conditions can be combined using match-all or match-any logic.

When a matching change is detected, the alert identifies the affected user and includes the previous and new values.



### Enhancements

#### Permissions Explorer: CSV export

Permissions Explorer results can now be exported to CSV from the User Permissions and Object Access views.

Exports include all matching users and permission paths and respect the selected permissions, filters and Include Frozen Users setting.

#### User Activity Monitoring: Clearer change history

User history now focuses on meaningful changes instead of displaying repeated daily snapshots.

A new history entry is added only when a tracked attribute changes. This will make it easier to identify changes in profile, role, license and status.

#### User Management: Invitation email handling

Guard now provides clearer feedback when a user is created but the invitation email cannot be sent.

Administrators can see the relevant invitation error and resend the invitation from the user page.



### Bug fixes

#### API Security: Stable dashboard rendering

The Connected Apps chart now renders smoothly at its final size and position while the API Security dashboard loads.

#### Large Salesforce organization support

User Activity Monitoring, Permission History and User Security Overview now handle large Salesforce organizations more efficiently.

Paged retrieval, server-side search and streaming reduce long-running queries and unnecessary memory usage.

#### Permission History: Organization selection

The organization selector is now locked while Permission History results are being retrieved, keeping the selected organization and results consistent.

***

## AutoRABIT Guard Release Notes 26.2.3&#x20;

**Release Date: 5 August 2026**

### Enhancements

#### Drift Policies – Richer User Activity Monitoring Trigger Details

Drift Policy trigger details now provide clearer context for User Activity Monitoring changes.

For supported events, users can review the affected users and navigate directly to the relevant User Activity Monitoring detail. This applies to password changes and changes to user license, profile, and role assignments.

#### Drift Policies – Locked-User Count Monitoring

Custom Drift Policies can now monitor changes in the number of locked Salesforce users.

This enables administrators to identify increases or decreases in locked user accounts using existing User Activity Monitoring history and Drift Policy notifications.

#### Drift Policies – Clearer Template Policy Setup

When creating a Drift Policy from a template, users can now view the metrics and comparison behavior included in the template before saving.

### Bug Fixes

#### Automated Data Classification – Custom Regulations

Automated Data Classification now keeps Custom Regulations up to date when a Salesforce compliance categorization is deactivated, deleted, or removed from an organization.

#### Drift Policies – Combined Condition Display

Drift Policy evaluations using combined AND conditions now display correctly.

#### Drift Policies – Deleted Organization Handling

Triggered Drift Policy events associated with a deleted organization are now handled reliably, allowing policies to load as expected.

#### Risk Assessment – PII Labels and Object Counts

Risk Assessment now displays PII labels consistently and accurately counts distinct exposed objects for the relevant external access risk.

***

## AutoRABIT Guard Release Notes 26.2.2

**Release Date: 15 July 2026**

### Enhancements

#### Main Navigation Link for IZ Suite

AutoRABIT Guard now includes an IZ Suite item in the main navigation. Selecting this option opens the Integral Zone login page in a new browser tab.

#### Immediate Drift Policy Evaluation

When creating a new Drift Policy, users can now choose to evaluate the policy immediately using the two most recent snapshots. This helps users see whether a newly created policy would trigger without waiting for the next scheduled daily evaluation.

#### Multiple Real-Time Change Notification Recipients

Real-time change notifications now support multiple email recipients. Users can select one or more Guard users from the same tenant as notification recipients, making it easier to keep the right teams informed.

Recipient selection is also aligned across Real-Time Change Notifications and Drift Policies.

#### User Management Date Visibility

The User Management interface now displays each user’s Creation Date and Last Login. These fields are available in the Users table and in the User Details view, helping admins review account age and identify inactive users.

### Bug Fixes

#### Drift Policy Direct Links

Opening a Drift Policy from a direct link, such as a notification email, will no longer take the user to a blank page.

***

## AutoRABIT Guard Release Notes 26.2.1

**Release Date: 17 June 2026**

### New Features

#### **Drift Policies**

This release introduces Drift Policies: a dedicated area for monitoring meaningful changes in security posture across supported Guard data sources. Users can:

* Create policies from recommended templates;
* Define your own criteria using custom conditions;
* Apply policies to one or more Salesforce orgs;
* Receive email notifications when policy conditions are triggered.

For more information, please see the [Drift Policies article](https://knowledgebase.autorabit.com/product-guides/guard/features/risk/drift-policies).

### Enhancements

#### **Public File Exposure Improvements**

Public File Exposure now provides clearer visibility into public links. This includes:

* Org-level summary metrics;
* Active and expired statuses;
* Filtering by expiration date and active-only;
* Remediation actions to expire links immediately or schedule expiration.

#### **Real-Time Change Notification Filtering**

Real-Time Change Notifications now support filtering and sorting by organization.

#### **Permission Set Targeting for Change Notifications**

Users can now configure Real-Time Change Notifications to track changes for specific permission sets.

#### **Guard CLI Export Filtering**

Guard CLI export commands now support more targeted data extraction with filtering options.

### Bug Fixes

#### **Session Timeout Improvements**

Guard now handles client-side idle timeout more consistently across browser tabs, helping inactive sessions expire as expected.

#### **Risk Assessment**

Fixed an issue where auto-resolve controls could be bypassed when auto-resolution was disabled.

#### **User Activity Monitoring**

Fixed an issue where large Salesforce orgs could encounter errors when browsing beyond the first set of user records.

#### **Permissions Explorer**

Fixed inconsistencies where user status could appear incorrectly across Permissions Explorer table and user detail views.

#### **Automated Data Classification**

Fixed an issue where classification analysis could fail after refresh.

#### **User Management**

Improved validation so user details cannot be saved with empty or whitespace-only values. Also fixed an issue where temporary locks could not be removed for users who had not yet logged in.

#### **General UI Error Handling**

Fixed an issue where some error messages appeared twice in the UI.
