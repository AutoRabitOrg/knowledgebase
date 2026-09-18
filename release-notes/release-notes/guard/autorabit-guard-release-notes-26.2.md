# AutoRABIT Guard Release Notes 26.2

<figure><img src="../../../.gitbook/assets/Guard_Banner_1920x1080.png" alt=""><figcaption></figcaption></figure>

{% @mailchimp/mailchimpSubscribe listId="a085e26e7e" cta="Sign up to receive Guard updates!" %}

## AutoRABIT Guard 26.2.5 Release Notes

Release Date: 23 September 2026

### New features

#### Notification Centre

Guard now provides a central location for reviewing notifications from Drift Policies, Authorization Policies, Change Monitoring Policies, and Transaction Security Policies.

A notification bell available throughout Guard indicates when there are unseen notifications. Users can review their personal Inbox and Archive, search notifications, filter by policy type, time, and Salesforce org, and open the associated policy. Administrators can also switch between their own notifications and all notifications in the tenant.

Notifications can be archived individually or in bulk. They are automatically archived 30 days after creation and permanently deleted after 90 days.

#### Notification groups and in-app policy notifications

Administrators can create reusable notification groups containing Guard users from the same tenant. Groups can be selected alongside individual users when configuring policy recipients, making it easier to notify the right teams consistently.

A default domain can also be assigned to a notification group, automatically adding the group to new policies created in that domain.

Email delivery is now optional for Authorization Policies and Change Monitoring Policies. Policies remain active and continue to generate notifications in Guard when email delivery is disabled or no email recipients are configured.

#### Transaction Security Policies

_Please speak to us about enabling this feature._

Guard now supports deploying Salesforce Transaction Security Policies from predefined templates to one or more eligible Salesforce orgs.

Administrators can review each template and its Apex code, configure the available enforcement action, and review deployment results and triggered events for each org.

The available templates include:

* Detect Large PII Exports
* Impossible Travel
* Unapproved App Access
* Legacy Device/OS Restriction

Availability depends on the Salesforce licenses and permissions configured for the connected org.

### Enhancements

#### Global search

A new search bar in the Guard header makes it easier to find pages and records across the platform. Users can open search from anywhere in Guard or use the Ctrl + K keyboard shortcut.

Search results include navigation pages, Drift Policies, Transaction Security Policies, Authorization Policies, Change Monitoring Policies, API Security apps, and Salesforce orgs. Search also recognises common abbreviations and minor typing errors.

#### Authorization Policies: Grouped conditions and exclusion operators

Criteria-based Authorization Policies now support condition groups, allowing conditions within a group to be combined using AND and multiple groups to be combined using OR. This provides greater flexibility when defining precise access requirements within a single policy.

A new Not In operator allows selected profiles, roles, and other criterion values to be excluded. Existing policies retain their current evaluation logic and do not need to be rebuilt.

These controls are also available when creating draft policies through Permission Explorer.

#### Authorization Policies: License type criteria

Salesforce License Type can now be used alongside Profile, Role, Company Name, and Email Domain when defining criteria-based Authorization Policies.

License Type is also available in Permission Explorer filters, maintaining consistency between permission investigation and policy creation.

#### Risk Assessment: History

Risk Assessment history now highlights meaningful changes in risk settings or overall results instead of repeating unchanged assessments. This makes it easier to identify how an org's risk posture has changed over time.

#### User Activity Monitoring: Historical activity

The Historical Activity Overview now records an entry only when total, active, frozen, or locked user counts change. Repeated entries with no changes are removed, making meaningful activity easier to identify.

Charts now remain independent of table filters and clearly indicate that they represent the complete Salesforce org view.

#### Risk Assessment: Certificate expiry and usage visibility

Guard now identifies certificates that have expired or will expire within 90 days. Certificate names and expiry dates are displayed with links to the corresponding Salesforce records.

Usage details also show related Named Credentials, SAML SSO configurations, and package ownership information where available, helping administrators understand the potential impact of certificate renewal or replacement.

#### Permission Explorer: Performance and history improvements

Permission Explorer now uses paginated results and improved permission resolution to provide faster, more responsive queries for larger Salesforce orgs and broad permission selections.

Permission History presents each audit event once instead of repeating it for every granting source. History can also be reviewed even when users no longer hold the selected permissions.

#### Exports: Authenticated downloads

Export downloads now use the user's authenticated Guard session instead of password-protected ZIP files.

Export emails no longer contain passwords. Download links use short-lived secure tokens and verify the tenant and user requesting the export.

#### Org Executive Reports: Generation without AI credits

Org Executive Reports now use available assessment data and a standard report template without consuming AI credits or requiring AI functionality to be enabled.

This makes report generation available across more environments while maintaining a consistent executive summary format.

#### Salesforce orgs: Search by name

The Salesforce Orgs page now supports case-insensitive name search, making it easier to locate a connected org.

#### Change Monitoring Policies: Updated naming

Real-time Change Notifications has been renamed Change Monitoring Policies across Guard navigation, page titles, and related content.

The new name distinguishes policy configuration from the notifications generated when a policy is triggered.

### Bug fixes

#### Drift Policies: Editing policies with deactivated recipients

Drift Policies can now be updated when a previous notification recipient has been deactivated. Policy settings remain editable so administrators can remove or replace inactive recipients as needed.

#### Public File Exposure: Accurate expiration status

Public File Exposure now reflects whether Salesforce actively enforces expiration for a public link. Links that have an expiration date but are not configured to expire are correctly identified as non-expiring.

#### User search: Full names and usernames

User search in User Security Overview and the Authorization Policy Allowed Users selector now matches both full names and Salesforce usernames.

#### Change Monitoring Policies: Links and event tracking

Authorization Policy links opened from Change Monitoring now direct users to the correct policy.

Change Monitoring Policies also continue tracking the relevant metadata when a monitored permission set is renamed, and profile deletion events can now trigger matching policies.

#### Permission Explorer: Reliable large exports

Large Permission Explorer exports now complete reliably and provide the full expected output.

## AutoRABIT Guard 26.2.4 Release Notes

**Release Date: 19 August 2026**

### New Features

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

### Bug Fixes

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
