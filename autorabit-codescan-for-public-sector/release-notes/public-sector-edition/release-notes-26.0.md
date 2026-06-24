# Release Notes 26.0

## AutoRABIT CodeScan 26.0.2 Release Notes

**Release Date: 21 April 2026**

### Summary

AutoRABIT CodeScan 26.0.2 is comprised of the following 8 components:

* 4 Application Enhancements
* 1 New Rule
* 2 Rule Enhancements
* 1 Fix

Component details are listed in their corresponding sections within this document.

### Application Enhancements

**1.     CSV ISSUE EXPORT – Added Issue Status User**

**Description**

Enhanced the Issues CSV export to include a separate column called “**Status Marked By**” that shows the user name of the person who marked the current status of an issue, so that audit/user can clearly understand who last set or changed the issue’s status when reviewing exported data.

**Hypothesis**

If the CSV export includes the “Status Marked By” column with the corresponding username (or left empty when no status exists), then users will have better traceability and accountability when analyzing issues outside the platform, reducing ambiguity about ownership and status changes.

<figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

**Value / Purpose**

* Improves transparency and auditability of issue status changes in exported reports.
* Enables teams and managers to identify responsibility and follow up more effectively.

Verified the following scenarios and confirmed that all are working as expected.

* Verified with multiple users, users getting updated as expected.
* Verified with root user - status marked by updated as administrator.
* Verified by removing org user, name is still shown in CSV - working as expected.
* Verified with deactivated user, name is still shown in CSV - working as expected.
* Verified with deleted user, the status marked by field is empty.

**2.     CSV HOTSPOT EXPORT – Added Hotspot Status User**

**Description**

Enhanced the Security Hotspot CSV export to include a separate column called “**Status Marked By**” that shows the user name of the person who marked the current status of an hotspot, so that audit/user can clearly understand who last set or changed the hotspot’s status when reviewing exported data.

**Hypothesis**

If the Hotspot CSV export includes the “Status Marked By” column with the corresponding username (or left empty when no status exists), then users will have better traceability and accountability when analyzing hotspots outside the platform, reducing ambiguity about ownership and status changes.

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

**Value / Purpose**

* Improves transparency and auditability of hotspot status changes in exported reports.
* Enables teams and managers to identify responsibility and follow up more effectively.&#x20;

Verified the following scenarios are all working as expected.

* Verified with multiple users, users getting updated as expected.
* Verified with root user - status marked by updated as administrator.
* Verified by removing org user, name is still shown in CSV - working as expected.
* Verified with deactivated user, name is still shown in CSV - working as expected.
* Verified with deleted user, the status marked by field is empty.

**3.     Enhanced CSV Export with Detailed Security Hotspot Statuses**

**Description**

Enhanced the CSV export for Security Hotspots to include the full set of hotspot statuses—**TO\_REVIEW, SAFE, FIXED, EXCEPTION, ACKNOWLEDGED**—so that the exported data accurately reflects the current review and remediation state instead of the simplified **To\_Review** and **Reviewed** statuses.

**Hypothesis**

If the CSV Security Hotspots export includes granular and accurate hotspot statuses, users will be able to perform better reporting, auditing, and compliance tracking without relying on the UI or manual interpretation.

**Value / Purpose**

* Provides **accurate and actionable data** in exports for security reviews and audits.
* Enables **better integration** with external reporting, GRC, and compliance tools.&#x20;

Validated the CSV Security Hotspot Export with Detailed Statuses; below is the validation summary of the Exports:

* Verified CSV includes each of the listed statuses when present in results.
* Verified status values are exported accurately.
* Verified export remains consistent with UI status for the same hotspot set.
* Confirmed export works for mixed-status datasets and filters/sorting do not alter status values.

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

**4.     Added Closed Issue Statuses to CSV Reports**

**Description**

Currently, CSV reports do not clearly distinguish closed issue statuses, such as **Closed** and **Removed**. As such, we have enhanced the CSV export functionality to include these closed statuses explicitly in the Status column. The exported CSV now accurately reflects the latest lifecycle state of each issue, including closed states, ensuring consistency with what users see in the UI.

**Hypothesis:**

If CSV reports include detailed closed statuses (Closed, Removed), users will gain better visibility into issue resolution outcomes, enabling more accurate reporting, compliance tracking, and stakeholder communication. This will reduce manual effort in categorizing closed issues after export.

**Value / Purpose:**

* Improves reporting accuracy and transparency.
* Supports audit and compliance requirements with clear issue disposition tracking.

The enhancement for including closed issue statuses in CSV reports has been validated successfully

1. **Status: FIXED**
   * When an issue status is manually changed to **FIXED** in the Issues view, the exported CSV report correctly displays the status as **FIXED** in the **Status** column.
2. **Status: CLOSED**
   * When the source code is modified to resolve the issue and a **new analysis is executed**, the issue is automatically transitioned to **CLOSED**.
   * The exported CSV report correctly reflects the status as **CLOSED**.
3. **Status: REMOVED**
   * When the **Quality Profile is modified** such that the rule generating the issue is removed or disabled, and a new **analysis is executed**, the issue status changes to **REMOVED**.
   * The exported CSV report correctly displays **REMOVED** in the **Status** column.

Concluding that the CSV export now accurately reflects the issues, including closed statuses (**FIXED, CLOSED, REMOVED**), ensuring consistency with the UI.

<figure><img src="../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

### New Rules

**1.     New Rule: “Locale Formats in API Versions pre-v45.0”**&#x20;

{Rule ID: sf:LocaleInOldApi}

**Description**

This rule finds locale methods in Apex classes with API versions below v45.0. Locale formats before Salesforce API v45.0 default to JDK format. Now, locale formats default to ICU. It is recommended to update all components using API versions prior to v45.0 or use locale-neutral methods.

Failure to upgrade to API v45.0 or above could result in date and time formatting issues, affecting user experience and functionality.

* **Issue Type**: Bug
* **Severity**: Major
* **Message**: Avoid Using JDK Locale Formats
* **Tags**: retired
* **Remediation**: 30 minutes

Please also refer to the following documentation on Salesforce Help:&#x20;

[JDK Locale Format Retirement and the Enable ICU Locale Formats Salesforce Release Update](https://help.salesforce.com/s/articleView?id=000380618\&type=1) –

[Use Locale-Neutral Methods in Code](https://help.salesforce.com/s/articleView?id=xcloud.admin_locales_code_methods.htm\&type=5)

The rule sf:LocaleInOldApi was validated for the following methods:

* Date.format
* Datetime.format
* Date.parse
* Datetime.parse
* Date.toStartOfWeek

1. **Positive Validation (API Version < 45.0)**
   * Created Apex classes with API version 44.0 and used the above locale-dependent methods.
   * These cases are expected to be flagged since API versions prior to v45.0 rely on JDK locale formatting.
2. **Negative Validation (API Version ≥ 45.0)**
   * Created Apex classes with API version 45.0 and above using the same methods.
   * These cases are not expected to be flagged, since API v45.0+ uses ICU locale formatting by default.
3. **Verification Outcome**
   * The rule behavior was validated against the defined conditions.
   * Classes with API versions prior to v45.0 and using locale-dependent methods are considered for detection, while classes with API v45.0+ are treated as compliant.

<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

**1.       Enhanced data flow analysis logic in rule “Avoid Untrusted/Unescaped Variables in DML Query”**

{Rule ID: sf:SOQLInjection}

**Description**

**Scenario 1: Sanitized parameter still flagged**

* When a variable comes from a method parameter, the rule sometimes reports SOQL Injection **even if the variable is sanitized or overwritten later**.
* This happens because the rule uses **DataFlowNode**, which tracks where the variable originally came from.

**Scenario 2: “At least once” assignment not detected**

* DataFlowNode can detect whether an assignment is inside a condition.
* However, in some cases assignments happen **inside loops**, where the variable is still assigned at least once.
* DataFlowNode wasn’t originally designed to reliably confirm this loop behavior.
* Because of this limitation, these cases could not be properly handled and would likely result in producing false positives.

We remediated these issues with this fix, greatly improving the value of the data flow logic in tracing the vulnerability from sink to source.

Verified the following scenarios and confirmed that the are all working as expected.

* Verified error duplications are thrown - resolved (earlier)
* Verified whether a parameter is sanitized using escapeSingleQuotes but still flagged or not - after sanitized, no issue was thrown.

<figure><img src="../../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is reassigned multiple times; the issue will be thrown based on the last assigned value.

<figure><img src="../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is sanitized first and later overwritten with random function. - error thrown.
* In a condition, Verified when a variable is sanitized first and later overwritten with random function. - error thrown.

<figure><img src="../../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is assigned inside a loop before being used in the query. - If loop has non-sanitized parameters, then issue is thrown
* Verified when a user input flows through multiple helper methods before reaching the query. - trace throws error up to 5 params.

<figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

**2.     Added a new parameter to the rule “Test Class Names Should Include Test”** {Rule ID: sf:TestClassNaming}

**Description**

Several customers had reported that the CodeScan rule “Sf:testclassnaming” was producing false positives for classes containing “test.”

We verified the rule expression, and confirmed that we did not support the naming pattern PR\_TestClassName.

Instead, the rule supported only the following naming convention:\
TestClassName - prefix\
ClassNameTest - suffix\
ClassName\_Test - Underscore

As such, we enhanced this rule by adding a new parameter to Sf:testclassnaming to define allowed naming conventions.

The parameter is called allowedPatterns.

The description of the parameter is:

“A comma separated string of regular expressions matching allowed naming conventions for test classes.”

The default of this parameter is to use the preexisting current functionality of the rule.

Further, we decided that the parameter field should never be empty.

The value of this parameter is providing customers with the flexibility to add any patterns that they allow as acceptable naming conventions without restriction to our logic.

Validated the fix for the Sf:testclassnaming rule by verifying the following scenarios:

* Able to see the configurable parameter allowedPatterns (comma-separated regex list) to support custom naming conventions.
* Default behavior remains unchanged.
* Validation ensures parameter cannot be empty.
* Particular Reg expressions given in the allowed parameters skips the violations accordingly.

<figure><img src="../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1.       Set default value to “false” for “is\_archived” column in organizations table.**

**Summary of Issue**: Several customers were reporting an issue where users were unable to log in via SAML after their instance was upgraded to 26.0.3\
\
**Cause of Issue**: During our analysis, we identified that, as part of the upgrade process, a database field was unintentionally set to NULL instead of the defined default value. This disrupted the login via SAML.

**What was done to resolve**: A query was run to update the Null value to the default value.

**What we did to prevent it from happening again**: We have documented the corrective measures required to prevent this scenario in future upgrades. These improvements will be incorporated in an upcoming release to further strengthen the reliability of the upgrade process.

Verified the database for the orgs table, confirming that the “is\_archived field” is not NULL, and that DBAs are able to see the value set as **false** for all organizations in the environment.

Also verified that users who login with SAML are unblocked, which we confirmed by creating a new SAML connection on a new organization. All users are able to log in successfully without any issues.

***

## CodeScan Release 26.0.1

**Release Date: 18 January 2026**

### Summary

CodeScan 26.0.1. is comprised of the following 4 components:

* 1 New Feature
* 1 Application Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

1\.     CodeScan extension for Cursor

With this release, CodeScan introduces first-class support for Cursor, a rapidly adopted AI-focused IDE used heavily by both our customers and internal teams. By bringing CodeScan capabilities directly into Cursor, we strengthen our AI value proposition and ensure we’re present where modern development workflows are shifting.

Since Cursor is built on top of VS Code, this integration can leverage existing extension architecture—making it a natural, efficient expansion of our current IDE support. The goal is to deliver seamless scanning, issue insights, and AI-driven assistance within Cursor, enabling a smooth, intelligent coding experience for our users.

**Feature Description**

For developers who are using Cursor as their primary IDE, they can now run CodeScan

What Problem Are We Solving?

Guardrails for AI coding

Less security reviews and less rework

Faster time to market with business requirements

**User Benefits**

* Improves release management productivity
* Integrated seamlessly with CICD workflows
* Delivers on the Cursor promise of “making developers extraordinarily productive”

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### Application Enhancements

**1.     Include Issue Comments in CSV Issues Export**

**Description**

When exporting Issues to CSV, the file should include an additional column that captures all comments associated with each issue. Each entry in this column must list every comment along with the commenter’s user name, the date/time the comment was made, and the comment text, formatted in a readable, consistent manner.

**Hypothesis**\
If issue comments are included in the CSV export with clear attribution & timestamps, then users will be able to review, audit, and share issue context offline without needing to revisit the application UI.

_The image below illustrates the new format for comments added into CSV exports:_

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

**Value / Purpose**

* Enables complete issue context in offline analysis and reporting.
* Reduces dependency on the UI for reviews, audits, and stakeholder sharing.
* Improves collaboration by preserving discussion history in exported data.

Verified Issue Comments column in CSV export via the following Scenarios:\
\
Member Comment Export

* Added a comment as an existing project member.
* Exported the Issues CSV and verified that the comment is correctly displayed in the _Issue Comments_ column along with user name and timestamp.
* Invited Organization Member Comment
* Invited a new member to the organization and added a comment from that user.
* Exported the CSV and confirmed the comment appears correctly.
* Multiple Comments from Different Members
* Added multiple comments from different organization members on the same issue.
* Verified that all comments are present in the CSV export and are displayed in a readable, consistent format.
* Deleted User Comment Handling (Expected Behavior)
* Invited a user, added a comment from that user, and then deleted the user.
* Verified that the comment remains in the CSV export with a “Deleted” tag.
* Confirmed that no additional user information is shown for the deleted user, which matches the expected behavior.

### &#x20;Fixes

&#x20;**1.     Fixed three issue with CodeScan User Licenses**

Several customers reported that they were not able to activate all their team members, even though they had proper licensing. It appears that CodeScan was consuming 1 license spot.

Upon detailed research, we identified 3 issues that needed to be fixed:

1. There were some “hangin&#x67;_”_ user entries in organization\_members table, where there were entries for users present in organization\_members table, which did not have a mapped corresponding user in users table.
2. Member count query was not taking into account inactive users.
3. When AutoRABIT SRO creates a new org, the root admin user used to create the org was being automatically added to that organization as a member. Thus, the root user was taking up a standard user slot in customer’s license limit (unless explicitly removed).

We have addressed all of these issue in this release.

We have verified all the fixes related to user license counting and orphan member cleanup via the following scenarios

1. Inactive SonarQube Users Excluded from License Count
   1. Created SonarQube users and added them to CodeScan organizations.
   2. Upon deactivating users in Administration page verified:
      1. User is excluded from member/license count.
      2. Corresponding license is freed immediately.
      3. A new user can be added without encountering license limit errors.
   3. Verified for both Standard users and Platform Integration users.
2. Immediate License Release on User Removal/Deactivation
   1. Removed/deactivated active users from the organization.
   2. Confirmed license count updates instantly on:
      1. Organization → Members page
      2. Administration → Billing page
3. Orphan (Hanging) organization\_members Entries Cleanup
   1. Identified orphan entries in organization\_members table (no corresponding users users\_table entry).
   2. Executed dev-provided cleanup SQL query.
   3. Confirmed Orphan entries were successfully deleted.

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

**2.     Fixed an issue with “Issues” assignment and status update, where filters are not working (as "Bulkchange and Bulkassign" API returns 500 Internal error)**

Several customers reported issue with “Bulk Issue Assignments.”  We identified 2 main causes:

* Issue 1: Main Branch – Unable to Roll Back Issue Status to Open
* Issue 2: PR Branch – Unable to Assign Issues

We fully remediated these issues in this release by adding a logic fix for the bulk api (for pr analysis) by correctly fetching the projectuuid.

Verified the following issues have been remediated and are now working as expected.

* Regarding Issue 1: Main Branch
* Users able to revert the issue status back to Open (on the main branch).
* API able to assign/unassign multiple issues to org user
* Regarding Issue 2: PR Branch
* Issues in PR branches should be assignable to users through Bulk Issues, similar to main branch behavior.
