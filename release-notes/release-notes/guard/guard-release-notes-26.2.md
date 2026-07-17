# Guard Release Notes 26.2

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

For more information please see the [Drift Policies article](https://knowledgebase.autorabit.com/product-guides/guard/features/risk/drift-policies).

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
