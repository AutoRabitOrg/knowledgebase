# Guard Release Notes 26.2

## AutoRABIT Guard Release Notes 26.2.1

**Release Date: 17 June 2026**

### New Features

#### **Agentic Code Analysis**

Guard introduces Agentic Code Analysis: an AI-powered code review experience that runs through the Guard CLI in CI/CD pipelines, displays structured scan results in Guard, and helps teams review findings with actionable remediation guidance, including recommended code patches. This first release includes:

* Optional Advanced AI Suggestions. For a slightly longer run time you get more insightful results that allow you to quickly make changes to your code. Enabling this feature gives downloadable, file-by-file patch support for all findings.
* Custom rule validation. Create additional policies for your Salesforce code by uploading a PDF or writing in natural language. Get the rules checked by AI for quality and duplication before running your first scan.

For more information please see our article \[link] and User Guide \[link].

#### **Drift Policies**

This release also introduces Drift Policies: a dedicated area for monitoring meaningful changes in security posture across supported Guard data sources. Users can:

* Create policies from recommended templates;
* Define your own criteria using custom conditions;
* Apply policies to one or more Salesforce orgs;
* Receive email notifications when policy conditions are triggered.

For more information please see the Drift Policies article \[link].

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
