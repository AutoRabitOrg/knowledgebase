# Cloud Release Notes 26.0

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive CodeScan updates!" listId="a085e26e7e" %}

## CodeScan Release Notes 26.0.15

**Release Date: 05 July 2026**

### Summary

CodeScan 26.0.15 is comprised of the following 5 components:&#x20;

* 1 New Feature&#x20;
* 1 New Rule&#x20;
* 1 Rule Enhancement&#x20;
* 2 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

New Features:&#x20;

1. CodeScan now has “salesforce-project-only” tags for Rules with SF queries&#x20;

Description&#x20;

Several CodeScan rules perform queries directly against Salesforce to execute their analysis. These rules require an active Salesforce project connection and cannot be used in a standard static analysis context. To improve discoverability and filterability, the tag salesforce-project-only should be added to each of these rules.&#x20;

The following rules require this tag:&#x20;

* sfmeta:NcinoDuplicateLabels&#x20;
* sfmeta:NcinoComponentNamingDuplicate&#x20;
* sfmeta:NcinoIntUserConfig&#x20;
* sfmeta:NcinoDeprecatedFields&#x20;
* sfmeta:NcinoDuplicateLookupKeys&#x20;
* sfmeta:NcinoFeeTemplateScreenSection&#x20;
* sfmeta:NcinoNullLookupKeys&#x20;
* sfmeta:NcinoProductFeatureNotExist&#x20;
* sfmeta:NcinoProductFeatureSharing&#x20;
* sfmeta:NcinoNullCollateral&#x20;
* sfmeta:ExcessivePageLayout&#x20;
* sfmeta:CheckSystemAdministrator&#x20;
* sfmeta:CustomProfilesPermission&#x20;

Value&#x20;

Users working in non-Salesforce-connected environments are exposed to rules that will never produce valid results for their project type. By tagging these rules with salesforce-project-only, users can quickly filter them in or out of their rule sets, reducing noise and improving the overall rule browsing experience. It also makes it clearer to new users why certain rules may not be firing.&#x20;

Acceptance Criteria&#x20;

* The tag salesforce-project-only is added to all 13 rules listed above.&#x20;
* The tag appears on the rule detail page for each affected rule in the CodeScan UI.&#x20;
* Users can filter the rules list by the tag salesforce-project-only and only the 13 listed rules (and any others previously tagged) are returned.&#x20;
* No existing tags on any of the affected rules are removed or modified.&#x20;
* The tag is consistent in formatting (lowercase, hyphenated) with salesforce-project-only across all rules.&#x20;
* A smoke test has been performed to confirm the tag is visible and filterable in a non-production environment before release.

We have verified that the tag "salesforce-project-only" has been added to all 13 rules, and that the tag is visible, consistent, and filterable in the CodeScan UI. &#x20;

Test Scenarios Validated:&#x20;

1: Tag presence — All 13 rules have "salesforce-project-only" tag&#x20;

* sfmeta:NcinoDuplicateLabels&#x20;
* sfmeta:NcinoComponentNamingDuplicate&#x20;
* sfmeta:NcinoIntUserConfig&#x20;
* sfmeta:NcinoDeprecatedFields&#x20;
* sfmeta:NcinoDuplicateLookupKeys&#x20;
* sfmeta:NcinoFeeTemplateScreenSection&#x20;
* sfmeta:NcinoNullLookupKeys&#x20;
* sfmeta:NcinoProductFeatureNotExist&#x20;
* sfmeta:NcinoProductFeatureSharing&#x20;
* sfmeta:NcinoNullCollateral&#x20;
* sfmeta:ExcessivePageLayout&#x20;
* sfmeta:CheckSystemAdministrator&#x20;
* sfmeta:CustomProfilesPermission&#x20;

&#x20;

<img src="../../../../.gitbook/assets/unknown (87).png" alt="" height="386" width="594">

2: Tag visible on rule detail page for each affected rule&#x20;

<img src="../../../../.gitbook/assets/unknown (88).png" alt="" height="312" width="624">

3: Filter by "salesforce-project-only" returns all 13 rules&#x20;

<img src="../../../../.gitbook/assets/unknown (89).png" alt="" height="365" width="562">

4: No existing tags removed or modified on any of the 13 rules&#x20;

5: Issue got triggered for a random rule, working as expected. Hence closing this user story.&#x20;

<img src="../../../../.gitbook/assets/unknown (90).png" alt="" height="320" width="578">

New Rules:&#x20;

1. New CodeScan Metadata Rule: “Communities With Guest Access” &#x20;

{Rule ID: sfmeta:CommunityGuestUserAccess"} &#x20;

Description

Identify Salesforce Experience Cloud communities (Network metadata) that allow guest user access and correlate them with associated Guest User Profile metadata to detect excessive permissions (object, field, or Apex access). The rule flags communities where unauthenticated users may access or modify sensitive data.&#x20;

Hypothesis&#x20;

If a community allows guest access and the associated guest user profile has elevated permissions, then sensitive data or functionality may be exposed to unauthenticated users, leading to potential data breaches or unauthorized actions.&#x20;

EXACT CONDITIONS TO FLAG &#x20;

A. Object-Level Permissions &#x20;

From:&#x20;

\<objectPermissions>&#x20;

Flag if ANY of the following:&#x20;

* allowRead = true on standard objects: &#x20;
* Account &#x20;
* Contact &#x20;
* Lead&#x20;
* User&#x20;
* OR any custom object (\_\_c) &#x20;

OR&#x20;

* Any of these are true: &#x20;
* allowCreate = true &#x20;
* allowEdit = true &#x20;
* allowDelete = true &#x20;

B. Field-Level Access (Sensitive Data Exposure)&#x20;

From:&#x20;

\<fieldPermissions>&#x20;

Flag if:&#x20;

* readable = true for sensitive fields like: &#x20;
* Contact.Email &#x20;
* Contact.Phone &#x20;
* Lead.Email &#x20;
* Any field matching patterns: &#x20;
* \*Email\* &#x20;
* \*Phone\* &#x20;
* \*SSN\* &#x20;
* \*Password\* &#x20;

👉 This is your PII exposure condition&#x20;

C. Apex Class Access (Public Logic Exposure)&#x20;

From:&#x20;

\<classAccesses>&#x20;

Flag if:&#x20;

\<enabled>true\</enabled>&#x20;

👉 Especially risky if:&#x20;

* Classes expose: &#x20;
* @AuraEnabled &#x20;
* REST endpoints  &#x20;

Parameters should be displayed as below:&#x20;

<img src="../../../../.gitbook/assets/unknown (91).png" alt="" height="165" width="624">

Note: Regarding fields, the functionality should work as PII rule. &#x20;

Value / Purpose&#x20;

* Detects real-world data exposure risks from misconfigured guest access&#x20;
* Prevents unauthenticated access to sensitive objects and fields&#x20;
* Ensures secure configuration of Experience Cloud communities&#x20;
* Reduces risk of public data leaks and compliance violations&#x20;
* Provides context-aware, high-confidence vulnerability detection&#x20;

Acceptance Criteria&#x20;

Name: Community Guest User Has Excessive Permissions \
Key: CommunityGuestUserAccess&#x20;

\
Description: This rule identifies Salesforce Experience Cloud communities that allow guest access and where the associated Guest User Profile has elevated permissions such as object-level permissions (read, create, edit, delete), field-level access to sensitive data, or Apex class access. This may expose sensitive data to unauthenticated users.&#x20;

Type: Vulnerability \
Severity: Critical \
Message: Guest user profile has elevated permissions in a community, which may expose sensitive data or allow unauthorized actions.&#x20;

\
Tags: salesforce, security&#x20;

CWE : 732&#x20;

Remediation: 15 Minutes&#x20;

NOTE:  This is a project level rule.&#x20;

Verification: We have verified the new Salesforce Metadata rule "CommunityGuestUserAccess" (Communities With Guest Access) and have validated via the following scenarios:&#x20;

* Rule correctly detects communities with guest access enabled.&#x20;

<img src="../../../../.gitbook/assets/unknown (92).png" alt="" height="405" width="624">

* Flags guest user profiles with elevated object-level permissions (read, create) on standard objects.&#x20;

<img src="../../../../.gitbook/assets/unknown (93).png" alt="" height="350" width="624">

* Flags guest user profiles with elevated object-level permissions (read, create) on custom objects.

<img src="../../../../.gitbook/assets/unknown (94).png" alt="" height="343" width="624">

* Identifies sensitive/PII field-level access (Email, Phone, SSN patterns) on guest profiles.

<img src="../../../../.gitbook/assets/unknown (95).png" alt="" height="344" width="624">

* Detects enabled Apex class access on guest profiles.

<img src="../../../../.gitbook/assets/unknown (96).png" alt="" height="345" width="624">

* Configurable parameters (Sensitive Fields, Include Custom Objects) work as expected.

<img src="../../../../.gitbook/assets/unknown (97).png" alt="" height="346" width="624">

<img src="../../../../.gitbook/assets/unknown (98).png" alt="" height="344" width="624">

* Rule severity correctly classified as Critical Vulnerability.&#x20;

<img src="../../../../.gitbook/assets/unknown (99).png" alt="" height="318" width="624">

* Above scenarios verified with Comparison branch as well, work as expected.

<img src="../../../../.gitbook/assets/unknown (100).png" alt="" height="341" width="624">

* Re-run & Run manual verified regarding the new changes, work as expected.

Notes: &#x20;

* To get the rule triggered correctly make sure to add “Network” in codescan.cloud.packageTypes and “network” & “profile” in sonar.sfmeta.file.suffixes in project settings.&#x20;
* To give guest users access to the site's APIs, enable “Allow guest users to access public APIs” in Salesforce> Setup > all Sites > Workspaces > Administration > Preferences (or Builder > Settings > Public access)&#x20;

<img src="../../../../.gitbook/assets/unknown (101).png" alt="" height="314" width="624">

* To take away guest users access to the site's APIs, disable “Allow guest users to access public APIs” in Salesforce> Setup > all Sites > Workspaces > Administration > Preferences (Also verify Builder > Settings > Public access is disabled)&#x20;
* For custom sensitive/PII field-level access, configure “Filed Name” in the rule parameters. ( Field name and Field label can be different, get field name from sf org)&#x20;

All verification use cases passed successfully, the rule is working as expected, and no issues were reported during verification. &#x20;

Rule Enhancements&#x20;

1. Enhanced logic in CodeScan Apex rule “Unused Formal Parameter” to address common false positives {Rule ID: sf:UnusedFormalParameter}&#x20;

Description&#x20;

Several customers had reported false positives associated with this rule.  Upon analysis, we determined that at the Salesforce level, when parameters are consumed as SOQL bind variables inside a dynamically built query string, these parameters are generally used (and resolved from local scope at runtime).  \
&#x20;\
CodeScan was flagging them because its bind-detection only covers the IN :var form passed as a direct argument — not as strings built through the QueryFactory chain.  &#x20;

As such, we enhanced the rule logic to ensure that the rule (sf:UnusedFormalParameter) will not raise a violation when a method parameter is referenced as a SOQL bind variable within a string passed to dynamic SOQL execution.&#x20;

The rule shall recognize bind variable usage for operators such as =, !=, >, <, >=, <=, and IN.&#x20;

Existing support for IN :variable patterns shall remain unchanged.&#x20;

A violation shall still be reported when a method parameter is genuinely unused.&#x20;

We have verified that the rule sf:UnusedFormalParameter no longer raises false positives for formal parameters consumed as SOQL/SOSL bind variables (:var) in dynamic query patterns including fflib\_QueryFactory and Database.query().&#x20;

Fixes&#x20;

1. Fixed grammatical error in CodeScan Project Summary Report&#x20;

Description of issue:  Misspelling in Project Report&#x20;

Details:  When users access the second page of a CodeScan Project report, there was a grammatical error in the error message: "There is no any issues in the project analysis yet".&#x20;

We have updated error message to now display: “There are currently no issues in the project analysis.”&#x20;

We have verified that the error messages have been properly updated to “There are currently no issues in the project analysis.” in the project reports. All reports are working as expected.  &#x20;

1. Verified in the new project’s report&#x20;

<img src="../../../../.gitbook/assets/unknown (102).png" alt="" height="349" width="452">

2. Verified in the old project’s report

<img src="../../../../.gitbook/assets/unknown (103).png" alt="" height="312" width="399">

3. Verified in the scheduled cron job reports&#x20;

<img src="../../../../.gitbook/assets/unknown (104).png" alt="" height="412" width="416">

2. Fixed issue with CSV Export where the "Status Marked By" Column was empty for Bulk Operations&#x20;

Summary&#x20;

The "Status Marked By" column in the CSV Issue Export is empty when issue statuses are changed via bulk operations (api/issues/bulk\_change). The column works correctly when statuses are changed via single-issue operations (api/issues/do\_transition).&#x20;

Expected Result&#x20;

The "Status Marked By" column should display the name of the user who performed the bulk status change for all affected issues.&#x20;

We analyzed the :Status Marked By” population logic and found that bulk status change records were being skipped due to a startsWith() check. Updated the logic to correctly process bulk change entries and populate the user information.  With this logic change, this issue has been fully remediated.&#x20;

Scenarios Validated:&#x20;

1. Bulk status change to CONFIRMED – "Status Marked By" column correctly populated with the user name&#x20;
2. Bulk status change to EXCEPTION – Column populated as expected&#x20;
3. Bulk status change to FALSE\_POSITIVE – Column populated as expected&#x20;
4. Bulk status change to ACCEPTED – Column populated as expected&#x20;
5. Mixed bulk + single-issue transitions in same CSV export – Both reflect correct user names&#x20;

<img src="../../../../.gitbook/assets/unknown (105).png" alt="" height="486" width="624">

6. Multiple bulk operations by different users – Each row shows the respective user who performed the action&#x20;

<img src="../../../../.gitbook/assets/unknown (106).png" alt="" height="69" width="624">

<img src="../../../../.gitbook/assets/unknown (107).png" alt="" height="52" width="624">

<img src="../../../../.gitbook/assets/unknown (108).png" alt="" height="72" width="624">

7. Single-issue regression – No regression, column still works correctly for single transitions

<img src="../../../../.gitbook/assets/unknown (109).png" alt="" height="104" width="624">

8. Re-transition after bulk change – "Status Marked By" updates to the latest user

<img src="../../../../.gitbook/assets/unknown (110).png" alt="" height="69" width="624">

<img src="../../../../.gitbook/assets/unknown (111).png" alt="" height="52" width="624">

<img src="../../../../.gitbook/assets/unknown (112).png" alt="" height="72" width="624">

9. Issues with no status change – "Status Marked By" appropriately empty only for untouched issues - OPEN Sate&#x20;

<img src="../../../../.gitbook/assets/unknown (113).png" alt="" height="173" width="624">

Verified the same scenarios with Root level admin, working as expected.\
Verified the same scenarios with PR, working as expected.

<img src="../../../../.gitbook/assets/unknown (114).png" alt="" height="122" width="624">

\--

## CodeScan Release Notes 26.0.14

**Release Date: 28 June 2026**

### Summary&#x20;

CodeScan 26.0.14 is comprised of the following components:&#x20;

* 1 Fix

Component details are listed in their corresponding sections within this document.&#x20;

### Fixes&#x20;

1. **Resolved CI Jobs Analyzing Entire Codebase Instead of Delta Changes**

Fixed an issue where CodeScan CI jobs could analyze the entire repository instead of only the files modified in the current pull request or commit.

Previously, delta analysis was not consistently applied in certain CI execution scenarios, causing CodeScan to process all files in the repository. This could result in longer analysis times, increased resource consumption, and findings unrelated to the current code changes.

**Behavior**

* CI jobs now correctly analyze only the files included in the current delta (changed files).
* Delta analysis is consistently applied across supported CI integrations.
* Unmodified files are excluded from analysis when delta scanning is enabled.
* Analysis execution time and resource utilization are reduced for incremental scans.
* Results are focused on issues introduced or affected by the current changes.

**Outcome**

Improves CI pipeline performance and ensures analysis results remain relevant to the code changes being reviewed.

***

## CodeScan Release Notes 26.0.13

**Release Date: 21 June 2026**

### Summary&#x20;

CodeScan 26.0.13 is comprised of the following 6 components:&#x20;

* 0 New Features&#x20;
* 1 Application Enhancements&#x20;
* 1 New Rule&#x20;
* 2 Rule Enhancements&#x20;
* 0 Rule Deprecations&#x20;
* 2 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### Application Enhancements&#x20;

1. **Enhanced CSV Export Reporting for Issues and Security Hotspots**&#x20;

Enhanced CSV export reporting for both Issues and Security Hotspots to provide additional information for ownership tracking, exception management, auditing, and compliance reporting.&#x20;

Previously, CSV exports contained limited information, requiring users to manually retrieve assignment, severity, and exception details from within the CodeScan application.&#x20;

**New Export Fields**&#x20;

Issue and Security Hotspot CSV exports now include:&#x20;

* Severity &#x20;
* Assigned To &#x20;
* Assigned Date &#x20;
* Exception Expiry Date &#x20;
* Exception Reason &#x20;

Exported data reflects the current state of issues and hotspots at the time of export.&#x20;

**Exception Reason Tracking Improvements**&#x20;

Issue exception reasons are now stored separately from standard issue comments, improving traceability and reporting accuracy.&#x20;

Previously, exception reasons for Issues were stored using the same change type as standard comments, making it difficult to distinguish exception justifications from normal discussion history.&#x20;

**Reporting Improvements**&#x20;

The enhanced exports provide greater visibility into:&#x20;

* Severity classification &#x20;
* Ownership and assignment history &#x20;
* Exception lifecycle management &#x20;
* Expiring exceptions &#x20;
* Compliance and audit reporting activities &#x20;

Issue CSV exports now clearly distinguish between:&#x20;

* Issue Comments &#x20;
* Exception Reasons &#x20;

Fields are clearly labeled and consistently formatted within the generated CSV files.&#x20;

The updated exports provide users with improved visibility into severity, ownership, exception status, and exception lifecycle details, making it easier to perform external analysis, compliance reviews, and governance activities.&#x20;

**Outcome**&#x20;

* Improves auditability and compliance reporting. &#x20;
* Provides greater visibility into issue and hotspot ownership. &#x20;
* Simplifies exception tracking and lifecycle management. &#x20;
* Reduces the need to manually gather information from multiple areas of the platform. &#x20;
* Enhances offline analysis and reporting workflows.&#x20;

### New Rules&#x20;

1. **Connected App Missing Description**&#x20;

Added a new Salesforce Metadata rule to identify Connected Apps that do not have a defined description in metadata.&#x20;

Connected Apps without descriptions can be difficult to govern because administrators may not have enough context about the app’s purpose, ownership, or access usage.&#x20;

**Rule Details**&#x20;

* Rule key: _ConnectedAppMissingDescription_&#x20;
* Type: Code Smell &#x20;
* Default Severity: Major &#x20;
* Remediation effort: 2 minutes &#x20;
* Tags: salesforce &#x20;

**Behavior**&#x20;

The rule raises a violation when a Connected App metadata file does not contain a valid description.&#x20;

Violations are raised when the description is:&#x20;

* Missing &#x20;
* Empty &#x20;
* Self-closing &#x20;
* Commented out &#x20;
* Whitespace-only &#x20;
* Defined only in an unrelated nested location &#x20;

The rule does not raise a violation when a valid description is present, including descriptions with multiline text or special characters.&#x20;

**Message**&#x20;

_Connected App does not have a description defined. Add a description for better governance and traceability._&#x20;

**Outcome**&#x20;

* Improves governance and documentation of Salesforce Connected Apps. &#x20;
* Helps identify orphaned, unmanaged, or poorly documented integrations. &#x20;
* Supports security audits and compliance reviews. &#x20;
* Provides better visibility into app purpose and ownership.&#x20;

### Rule Enhancements&#x20;

**1. Improved Rule Engine Stability and Error Handling**&#x20;

Improved the stability and resilience of Apex rule execution by addressing multiple edge cases that could result in internal exceptions being exposed in analysis logs.&#x20;

Previously, certain rule evaluation scenarios could generate internal exceptions during analysis, resulting in Java stack traces being written to logs. Although analysis often completed successfully, these errors could lead to incomplete rule evaluation and reduced confidence in results.&#x20;

Edge cases addressed:&#x20;

* _SOQL Injection Rule Stability_&#x20;

Improved handling of Apex data-flow analysis scenarios that could previously result in internal type-casting exceptions during rule evaluation.&#x20;

* _LocaleInOldApiRule Stability_&#x20;

Improved handling of chained method invocations such as DateTime.now().format()to prevent internal rule execution errors while analyzing valid Apex code.&#x20;

* _Defensive Null Handling Across Rule Execution_&#x20;

Enhanced null-safety handling for multiple Apex rules, including:&#x20;

* Unescaped Output &#x20;
* SOQL Injection &#x20;
* Avoid SOQL in Loops &#x20;

Additional validation and defensive checks were introduced to ensure rule execution can safely handle unresolved AST and semantic-analysis paths without exposing internal exceptions.&#x20;

**Outcome**&#x20;

* Improves overall rule engine stability. &#x20;
* Prevents internal implementation details from appearing in analysis logs. &#x20;
* Reduces the risk of incomplete rule evaluation. &#x20;
* Provides more reliable and professional analysis output. &#x20;
* Improves confidence in analysis results for Apex projects.&#x20;

2. **Enhanced Documentation for Sensitive PII Field Detection Rule**&#x20;

Updated the documentation and guidance for the Identify Potential Sensitive PII Fields rule (sf:SecurePIIFields) to provide clearer information about the types of data covered by the rule and how organizations can extend detection coverage.&#x20;

**Documentation Improvements**&#x20;

The updated rule description now clarifies that certain standard Salesforce objects may contain sensitive personal information, including:&#x20;

* Contact &#x20;
* Lead &#x20;
* User &#x20;
* Account &#x20;
* Person Account &#x20;
* Opportunity &#x20;

Examples of potentially sensitive data include:&#x20;

* Names &#x20;
* Email addresses &#x20;
* Phone numbers &#x20;
* Physical addresses &#x20;
* Birth dates &#x20;
* Other personal identifiers &#x20;

The documentation also highlights the importance of protecting this information in accordance with privacy and security regulations such as:&#x20;

* GDPR &#x20;
* CCPA &#x20;
* HIPAA &#x20;

**Configuration Guidance**&#x20;

Organizations can define additional sensitive field names through rule parameters, including:&#x20;

* SSN &#x20;
* Social\_Security\_Number &#x20;
* Credit\_Card &#x20;
* Passport &#x20;

and other organization-specific fields that may contain regulated personal information.&#x20;

**Outcome**&#x20;

* Improves understanding of the rules' purpose and scope. &#x20;
* Provides clearer guidance for identifying and protecting sensitive data. &#x20;
* Helps organizations extend detection coverage to custom fields. &#x20;
* Supports privacy, security, and compliance initiatives through improved rule documentation.&#x20;

### Fixes&#x20;

1. **Resolved SAML Login Issue with Uppercase Organization Domains**&#x20;

Fixed an issue where users could be unable to log in when the organization's domain name contained uppercase letters.&#x20;

Previously, the SAML login flow treated organization domains as case-sensitive. As a result, valid domains entered with uppercase or mixed-case characters could fail authentication, even though domain names should be handled case-insensitively.&#x20;

**Behavior**&#x20;

* Organization domain matching is now handled case-insensitively during SAML login. &#x20;
* SAML connection creation now stores organization domain names consistently in lowercase. &#x20;
* Domains entered in lowercase, uppercase, or mixed case are handled correctly. &#x20;
* Leading and trailing spaces in domain input are handled safely. &#x20;
* Invalid domains continue to be rejected as expected. &#x20;

**Outcome**&#x20;

* Improves SAML login reliability for organizations using mixed-case or uppercase domain entries.&#x20;
* Aligns organization domain handling with standard case-insensitive domain behavior. &#x20;
* Prevents valid users from being blocked due to domain capitalization differences.&#x20;

&#x20;

2. **Resolved Salesforce Integration Error When Using Previous Test Run Results**&#x20;

Fixed an issue that could prevent Salesforce integrations from running successfully when configured to use unit test results from a previous execution.&#x20;

Previously, analyses configured with the _Use previous run_ option could fail while attempting to retrieve historical test execution data.&#x20;

**Behavior**&#x20;

* Corrected the retrieval of previous unit test execution results. &#x20;
* Improved handling of Salesforce test coverage queries and historical test result lookups. &#x20;
* Analysis now successfully reuses previously executed unit test results when available. &#x20;
* Organizations without prior test execution history are handled gracefully. &#x20;

**Outcome**&#x20;

* Improves the reliability of Salesforce integrations using previously executed unit tests. &#x20;
* Prevents failures caused by test result retrieval errors. &#x20;
* Reduces unnecessary test execution by allowing the successful reuse of historical test results. &#x20;
* Provides more resilient handling of organizations with limited or no prior test execution history.&#x20;

***

## CodeScan Release Notes 26.0.12

**Release Date: 7 June 2026**

### Summary

CodeScan 26.0.12 is comprised of the following 8 components:

* 3 Application Enhancements
* 1 New Rule
* 1 Rule Enhancement
* 3 Fixes

Component details are listed in their corresponding sections within this document.

### Application Enhancements

1. &#x20;**Instance-Level Severity Masking**

{% hint style="info" %}
NOTE: This feature is only available to customers who have a dedicated instance. It is not available for customers who are deployed on our SaaS multi-tenant instances.
{% endhint %}

Added support for instance-level severity masking, allowing CodeScan Administrators to centrally customize how severity labels are displayed across the platform while preserving underlying severity values, analysis behavior, and reporting logic.&#x20;

Previously, severity labels were displayed using the default values throughout CodeScan and could not be customized at the instance level. This enhancement introduces centralized severity masking that is consistently applied across the Web UI, reports, exports, APIs, and IDE plugins.&#x20;

**Behavior**&#x20;

* Administrators can configure severity label mappings through the Admin UI. &#x20;
* Severity masking settings are stored and managed at the instance level. &#x20;
* Severity mappings are exposed through secure APIs and applied consistently across the platform. &#x20;
* Custom severity labels are displayed throughout: &#x20;
* Web UI &#x20;
* Reports &#x20;
* CSV exports &#x20;
* SARIF exports &#x20;
* IDE plugins &#x20;
* Default severity labels are automatically used when no severity masking configuration exists. &#x20;
* Changes are applied immediately without requiring a refresh.&#x20;

<img src="../../../../.gitbook/assets/unknown (64).png" alt="" height="308" width="624">

**Supported Default Severity Labels**&#x20;

* Blocker &#x20;
* Critical &#x20;
* Major &#x20;
* Minor &#x20;
* Info&#x20;

**Validation**&#x20;

* Validation is enforced at both API and UI levels. &#x20;
* Invalid severity mappings are rejected with clear error messages. &#x20;
* Only administrators can modify severity masking settings. &#x20;
* Unauthorized users are restricted from making configuration changes. &#x20;

**Functional Integrity**&#x20;

Severity masking affects display labels only. The following behaviors remain unchanged:&#x20;

* Underlying severity values &#x20;
* Issue counts and metrics &#x20;
* Quality Gate evaluations &#x20;
* Severity-based sorting &#x20;
* Severity-based filtering &#x20;
* Analysis processing &#x20;
* Reporting calculations &#x20;
* Export generation &#x20;
* SARIF standards compliance &#x20;
* IDE plugin workflows &#x20;
* Downstream integrations &#x20;

**Outcome**&#x20;

* Provides consistent severity representation across the entire CodeScan platform. &#x20;
* Enables centralized governance of severity terminology. &#x20;
* Reduces inconsistencies between Web UI, reports, exports, and IDE plugins. &#x20;
* Preserves existing functionality and compatibility with integrations. &#x20;



2. **Exception Expiry Notifications**

Added subscription-based exception expiry notifications for Issues and Security Hotspots, enabling users to receive automated reminders before approved exceptions reach their expiry date.&#x20;

**Subscription Management**&#x20;

Users can now manage exception expiry notification preferences through:&#x20;

Profile → My Account → Notifications&#x20;

Notification options are available in:&#x20;

* Overall Notifications &#x20;
* Project Notifications &#x20;
* Project-level notification settings &#x20;

Users can enable or disable exception expiry notifications based on their preferences.&#x20;

**Reminder Notifications**&#x20;

Subscribed users receive automated email reminders for Issues and Security Hotspots with approved exceptions.&#x20;

Notifications are sent:&#x20;

* One week before expiry &#x20;
* One business day before expiry &#x20;

Business-day scheduling is automatically applied.&#x20;

**Notification Controls**&#x20;

Notifications respect:&#x20;

* User notification preferences &#x20;
* Project notification settings &#x20;
* User permission settings &#x20;

Notifications are not sent for:&#x20;

* Archived organizations &#x20;
* Deleted projects &#x20;
* Unsubscribed users &#x20;

**Outcome**&#x20;

* Helps teams proactively review exceptions before they expire. &#x20;
* Reduces the risk of unnoticed expired exceptions. &#x20;
* Improves compliance and governance processes. &#x20;
* Provides users direct control over exception-related notifications.&#x20;



3. **Rules Evaluation Export Report**

Added a new Rules Evaluation Export Report that provides visibility into all rules evaluated during a scan, including scans where no issues are detected.&#x20;

**Behavior**&#x20;

A new export option, CSV Rules Evaluation Report, is available from the More menu.&#x20;

Users can select:&#x20;

* Project &#x20;
* Branch &#x20;

and export a report containing all rules evaluated during the selected scan.&#x20;

**Report Contents**&#x20;

The report includes:&#x20;

* rule\_key &#x20;
* rule\_name &#x20;
* rule\_language &#x20;
* rule\_category &#x20;
* rule\_severity &#x20;
* issues\_found &#x20;

Rules are included regardless of whether violations were detected.&#x20;

**Outcome**&#x20;

* Improves auditability and compliance reporting. &#x20;
* Provides visibility into scan coverage. &#x20;
* Allows users to validate rule execution even when no issues are found. &#x20;
* Preserves historical accuracy based on the quality profiles used during the scan.

### &#x20;New Rules

1. **Connected App Uses High-Risk OAuth Scopes**

Added a new Salesforce Metadata security rule to identify Connected Apps configured with high-risk OAuth scopes that may grant excessive or persistent access to organizational data and APIs.&#x20;

**Rule Details**&#x20;

* Rule key: _ConnectedAppHighRiskScopes_ &#x20;
* Type: Vulnerability &#x20;
* Default Severity: Major &#x20;
* CWE: CWE-272 &#x20;
* Remediation effort: 10 minutes &#x20;

**Behavior**&#x20;

The rule analyzes Salesforce Connected App metadata and raises a violation when high-risk OAuth scopes are detected within the Connected App configuration.&#x20;

The following OAuth scopes are currently identified as high-risk:&#x20;

* full &#x20;
* api &#x20;
* refresh\_token &#x20;

When one or more of these scopes are present, the rule reports the detected values in the violation message.&#x20;

**Message**&#x20;

_Connected App contains high-risk OAuth scopes: {scopes}. Review and restrict access._&#x20;

**Outcome**&#x20;

* Helps security teams identify over-privileged Salesforce integrations. &#x20;
* Improves visibility into Connected Apps that may expose organizational data through excessive OAuth permissions. &#x20;
* Encourages implementation of least-privilege access principles. &#x20;
* Reduces the risk of unauthorized or persistent access through overly permissive OAuth scope configurations.&#x20;

### Rule Enhancements

1. **Enhanced Avoid Calling SOQL and DML Inside Loops Rule**

Enhanced the _sf:AvoidSoqlInLoops_ rule to optionally detect Salesforce platform methods that consume SOQL queries internally when executed within loops.&#x20;

**New Parameter**&#x20;

| Parameter          | Default  | Description                                                           |
| ------------------ | -------- | --------------------------------------------------------------------- |
| checkInternalSoql  | false    | Checks for methods with internal SOQL consumption used within loops.  |

**Behavior**&#x20;

When enabled, the rule identifies supported platform methods that may consume hidden SOQL queries inside loops, for example:&#x20;

* Messaging APIs &#x20;
* UserInfo APIs &#x20;
* FeatureManagement APIs &#x20;
* Approval APIs &#x20;
* Flow invocation APIs &#x20;
* ConnectApi operations &#x20;
* Visualforce content APIs &#x20;

Outcome&#x20;

* Improves detection of governor limit risks. &#x20;
* Identifies hidden SOQL consumption. &#x20;
* Helps developers avoid query-limit violations. &#x20;
* Preserves existing behavior unless explicitly enabled.&#x20;

### Fixes

1. **GitHub Enterprise Integration Improvements**

Resolved multiple GitHub App integration issues affecting project creation, Pull Request analysis, and commit status reporting.&#x20;

a. GitHub App Installation Flow&#x20;

* Fixed an issue where organization members could receive a 404 error during GitHub App installation and project creation workflows.&#x20;

b. Pull Request Analysis Scope&#x20;

* Fixed an issue where PR analysis could process unrelated base branch files when the GitHub App lacked required permissions to retrieve changed PR files.&#x20;
* Required permission (PR): Read &#x20;

c. Commit Status Reporting&#x20;

* Fixed an issue where CodeScan could not publish analysis status updates to GitHub Pull Requests due to insufficient GitHub App permissions.&#x20;
* Required permission (Commit statuses): Read & Write &#x20;

Outcome&#x20;

* Improves GitHub project onboarding. &#x20;
* Ensures PR analysis processes only changed files. &#x20;
* Restores CodeScan status reporting on Pull Requests. &#x20;
* Improves support for all types of environments.&#x20;

{% hint style="info" %}
**GitHub App Permission Update**

**As** part of this release, we have updated the permissions required by the CodeScan GitHub App. GitHub will send a permission update request to any account or organization that has the CodeScan GitHub App installed.

\
The account or organization Owner should review and approve this request in GitHub:\
Settings → GitHub Apps&#x20;

(or Applications → Installed GitHub Apps → CodeScan → Review Request)

\
Once the request is approved, no further action is required.
{% endhint %}

2. **Resolved User Invitation and Group Assignment Issues**

Fixed issues in the user invitation workflow where invited or re-created users were not being assigned correctly to organizations and default groups.&#x20;

Previously:&#x20;

* Users invited from an organization were not always added to that organization after signup. &#x20;
* Users who were deleted or deactivated from the UI and later re-created were not added back to the default Members group. &#x20;
* This could prevent invited users from accessing the expected organization context after completing signup. &#x20;

**Behavior**&#x20;

* New users now follow the invite link flow correctly after signup and are added to the intended organization. &#x20;
* Email verification handling was updated so first-time signup flows redirect users through the invite workflow as expected. &#x20;
* Re-created users are now added back to the default Members group after activation. &#x20;
* Invite validation and post-login handling were improved to ensure organization and group membership are applied correctly. &#x20;

**Outcome**&#x20;

* Ensures invited users are added to the correct organization after signup. &#x20;
* Restores default group assignment for users who are re-created after deletion or deactivation. &#x20;
* Improves reliability of onboarding and access management workflows.&#x20;



3. **Analysis Permission Validation Improvements**

Fixed an issue where users with valid scan permissions could receive unauthorized errors when executing analyses.&#x20;

**Behavior**&#x20;

* Improved user-level scan permission validation. &#x20;
* Improved group-level scan permission validation. &#x20;
* Corrected effective permission evaluation during analysis startup. &#x20;

**Outcome**&#x20;

* Prevents false authorization failures. &#x20;
* Improves the reliability of project analysis execution. &#x20;
* Ensures consistent permission enforcement across user and group access models.&#x20;

***

## CodeScan Release Notes 26.0.11

**Release Date: 24 May 2026**

### Summary

CodeScan 26.0.11 is comprised of the following 10 components:

* 1 Application Enhancements
* 1 New Rule
* 8 Fixes

Component details are listed in their corresponding sections within this document.

### Application Enhancements

**1.    Severity Selection for Custom Security Hotspots**

Added support for assigning severity levels when creating or editing custom Security Hotspot rules.

Previously, severity levels were available for standard Security Hotspot rules, but custom Security Hotspots did not provide a severity selection option. This created inconsistency in rule configuration and made it harder for users to prioritize custom hotspot findings.

**Behavior**

* Severity selection is now available during custom Security Hotspot rule creation.
* Severity can also be configured when editing custom Security Hotspots.
* Supported severity values include:
  * Blocker
  * Critical
  * Major
  * Minor
  * Info
* Custom Security Hotspots now follow the same severity flow as standard rules.
* Severity filters on the Rules page correctly return matching custom Security Hotspots.

**Outcome**

* Provides consistent severity configuration across standard and custom Security Hotspot rules.
* Improves risk prioritization for custom security findings.
* Enhances filtering accuracy and rule management usability.

{% hint style="info" %}
NOTE:  Severity selection wasn’t available for custom Security Hotspots. To ensure consistency across standard and custom rules, we expanded functionality, and users can now select and assign a severity level during the creation and editing of custom Security Hotspots.
{% endhint %}

### New Rules

**1.    Avoid Plain Text Values in External Credential Parameters**

Added a new Salesforce Metadata security rule to detect plain text values in External Credential parameter values.

**Rule Details**

* Rule key: _sfmeta:ExternalCredentialPlainTextValue_
* Type: Vulnerability
* Default Severity: Critical
* CWE: CWE-798
* Remediation effort: 5 minutes

**Behavior**

The rule raises a violation when an External Credential metadata file contains a static plain text value in a _parameterValue_ field.

The rule does not raise a violation when:

* parameterValue uses a dynamic merge field reference.
* The sibling parameterName is Content-Type.
* The file does not contain any parameterValue fields.

**Message**

_Plain text value detected in parameterValue field. Use a dynamic merge field reference instead to avoid exposing sensitive credentials._

**Outcome**

Helps prevent sensitive credentials such as API keys, client IDs, and authentication tokens from being exposed in source control.&#x20;

### Fixes

1. **Improved Handling for Invalid Base Branches in Comparison and Pull Request Analysis**

Fixed an issue where analyses configured with branch comparison or pull request parameters could create invalid comparison branches and display unclear errors when the specified base branch did not exist.

**Affected Parameters**

Comparison Analysis:

* sonar.comparison.base
* sonar.comparison.branch

Pull Request Analysis:

* sonar.pullRequest.branch
* sonar.pullRequest.key
* sonar.pullRequest.base

Previously, when an invalid or nonexisting base branch was provided:

* Analysis did not fail immediately.
* A 404 error appeared later in analysis logs.
* Invalid comparison or PR branches could still appear in the dashboard.
* Users received limited visibility into the root cause.

**Behavior**

* Analysis now validates base branch existence before proceeding.
* Comparison and PR branches are no longer created when the base branch is invalid or missing.
* Analysis fails gracefully with clear and verbose error messaging in logs.
* Failure occurs earlier in the analysis lifecycle whenever possible.&#x20;

**Validation**

Validated across multiple integrations and analysis entry points, including:

* Sonar Scanner
* SFDX Scanner
* GitHub Analysis
* GitLab Analysis
* Salesforce Integration
* Bitbucket
* GitHub Actions
* Copado Integration
* Azure DevOps Pipelines
* IDE Plugin workflows

**Outcome**

* Prevents invalid branch artifacts from being created in the dashboard.
* Improves troubleshooting with clearer failure visibility.
* Provides more reliable branch comparison and pull request analysis behavior across integrations.&#x20;

2. **Improved Validation for Comparison Branch Analysis Without Main Branch Baseline**

Fixed an issue in Salesforce Integration where comparison branch analysis could complete successfully even when the configured main branch had not been analyzed.

Previously, users could create and analyze comparison branches without a valid analyzed baseline branch. This resulted in inconsistent behavior where:

* The analysis appeared as successfully completed.
* Quality Gate and metric calculations could not be computed.
* The UI displayed the error:
  * _metric.level.NOT\_COMPUTED_

**Behavior**

* Comparison branch creation and analysis validation was improved to ensure a valid analyzed main branch exists before processing.
* Users are now prevented from creating comparison branches when the main branch analysis is incomplete or interrupted.
* Improved user-facing messaging was added for incomplete analysis states.
* Instead of displaying technical metric computation errors, the UI now shows a clearer status message:
  * _Branch is not yet analyzed_

**Validation**

Validated through Salesforce Integration workflows using scenarios where:

* Main branch analysis was not executed.
* Main branch analysis was interrupted.
* Comparison branch analysis was interrupted.

Confirmed that:

* Comparison branch analysis no longer proceeds without a valid baseline.
* Invalid comparison states are blocked correctly.
* User-facing messages are displayed consistently without metric computation errors.

**Outcome**

* Prevents inconsistent comparison analysis states.
* Improves reliability of branch comparison workflows.
* Provides clearer and more user-friendly error handling for missing baseline scenarios.

3. &#x20;  **Support for Special Characters in Salesforce Organization Names**

Fixed an issue where project creation could fail when Salesforce Organization Names contained special characters such as registered trademark (®) or trademark (™) symbols.

Previously, organizations using special characters in the Salesforce Organization Name could encounter the following error during project creation:

_Error attempting to apply attribute converter_

This could result in partially created projects with missing associated data such as issues, code, and analysis information.

**Behavior**

* Special characters in Salesforce Organization Names are now properly supported.
* UTF-8 safe handling was added for organization name processing and database conversion logic.
* Attribute conversion handling was improved to prevent failures during project creation.
* Input validation and sanitization were enhanced while preserving expected functionality.

**Validation**

Validated using Salesforce organizations containing special characters including:

* ®
* ™
* Other UTF-8 supported characters

Verified successful project creation without attribute converter failures or data inconsistencies.

**Outcome**

* Prevents project creation failures caused by special characters in organization names.
* Eliminates incomplete project records and reduces manual database cleanup.
* Improves onboarding reliability and overall customer experience.

4. &#x20; **Resolved Salesforce Connection Deletion Issue with Special Characters in Connection Names**

Fixed an issue where creating a Salesforce connection using special characters in the connection name could trigger attribute converter errors and unexpectedly remove existing Salesforce connections from the application.

Previously, when users created a Salesforce connection with characters such as ® in the connection name:

* The create request failed with an attribute converter error.
* Existing Salesforce connections could disappear from the UI.
* The new connection was not created correctly.

**Behavior**

* Salesforce connection names now properly support special characters and UTF-8 input handling.
* Existing Salesforce connections remain unaffected during new connection creation.
* Attribute converter handling was improved to prevent unintended data impact.
* Validation and persistence behavior were stabilized for connection management workflows.

**Validation**

Validated by creating Salesforce connections using special characters including:

* ®
* ™
* Other supported UTF-8 characters

Confirmed that:

* New connections are created successfully.
* Existing Salesforce connections remain intact.
* No attribute converter errors occur in API or UI flows.

**Outcome**

* Prevents accidental removal of existing Salesforce connections.
* Improves reliability of Salesforce connection management.
* Enhances support for organizations using special characters in naming conventions.

5. &#x20;    **Resolved Duplicate Email Notifications and Organization Deletion Exceptions**

Fixed issues related to organization deletion workflows where duplicate email notifications and unexpected exceptions could occur during archive cleanup processing.

Previously, under specific conditions involving missing Quality Gate associations:

* Organizations could become inaccessible from the UI while still remaining in the database.
* Both success and exception notification emails could be triggered for the same deletion event.
* Instance Admin users were unable to fully remove affected organizations through the UI or API.
* Exceptions could occur during cleanup processing when Quality Gate data was missing.

The issue was identified in the Delete Archive Job flow, where:

* Exception emails were incorrectly triggered for all organizations instead of only failed deletions.
* Missing presence validation for Quality Gate data caused runtime exceptions during processing.

**Behavior**

* Email notifications are now triggered correctly based on actual deletion outcomes.
* Exception notifications are sent only for failed deletion scenarios.
* Additional validation checks were added before accessing Quality Gate data.
* Organization cleanup handling was improved to prevent inconsistent deletion states.

**Validation**

Validated organization deletion workflows under scenarios involving missing or invalid Quality Gate associations.

Confirmed that:

* Organizations are removed cleanly without residual inaccessible records.
* Duplicate email notifications no longer occur.
* No exceptions are triggered during archive cleanup processing.
* Instance Admin deletion workflows behave correctly.

**Outcome**

* Improves reliability of organization deletion workflows.
* Prevents inconsistent organization states between UI and database records.
* Reduces unnecessary exception notifications and administrative overhead.

6. &#x20;**Resolved Stack Overflow Issue in Field Level Security Rule Analysis**

Fixed an issue where project analysis could become stuck or fail due to a stack overflow error in the Field Level Security rule during Apex analysis.

Previously, specific Apex files containing deeply nested or recursive method call patterns could trigger repeated recursive evaluation within the _FieldLevelSecurityRule_, resulting in:

* Stack overflow exceptions during analysis.
* Excessively long analysis execution times.
* Analysis workflows appearing stuck or unresponsive.

**Behavior**

* Improved handling of recursive and nested method traversal within the Field Level Security rule.
* Added safeguards to prevent stack overflow conditions during rule evaluation.
* Analysis now completes successfully for previously failing customer scenarios.

**Validation**

Validated using customer-reported files and additional large project analysis scenarios.

Confirmed that:

* Stack overflow errors no longer occur during analysis.
* Analysis workflows complete successfully without interruption.
* Existing Field Level Security rule detection behavior continues to function correctly.

**Outcome**

* Improves stability and reliability of Apex security analysis.
* Prevents analysis failures caused by recursive execution paths.
* Reduces risk of stalled or incomplete project analysis workflows.

7. **Fix for Incorrect "No Scan Access for Project" Error During Analysis Execution**

Fixed an issue where analysis jobs were failing to proceed and displaying the error message: **"No scan access for project"**.\
The access validation logic for analysis jobs was updated to correctly verify user scan permissions before initiating the scan process.

**Previous Behavior**

When users attempted to run an analysis on certain projects, the scan would not progress further and would fail with a **"No scan access for project"** error, even in scenarios where valid access should have been permitted.

**Validation**

* Verified analysis execution for users with valid scan permissions.
* Confirmed that the access validation logic correctly handles project-level scan authorization.
* Tested scenarios for both authorized and unauthorized users to ensure expected behavior.
* Ensured analysis jobs now proceed successfully when appropriate access is available.

**Outcome**

Users with valid project scan access can now successfully start and complete analysis jobs without encountering the erroneous **"No scan access for project"** failure. The fix improves reliability and accuracy of permission validation during scan execution.

8. Resolved “No Scan Access for Project” Error During Analysis Execution

Fixed an issue where project analysis could fail to start and remain stuck while displaying the error:

_No scan access for project_

**Previous Behavior**

When users attempted to run an analysis on certain projects, the scan would not progress further and would fail with a "No scan access for project" error, even in scenarios with valid access.

**Validation**

* Verified analysis execution for users with valid scan permissions.
* Confirmed that the access validation logic correctly handles project-level scan authorization.
* Tested scenarios for both authorized and unauthorized users to ensure expected behavior.
* Ensured analysis jobs now proceed successfully when appropriate access is available.

**Outcome**

Users with valid project scan access can now successfully start and complete analysis jobs without encountering "No scan access for project" error. The fix improves reliability and accuracy of permission validation during scan execution.

***

## CodeScan Release Notes 26.0.10

**Release Date: 17 May 2026**

### Summary

CodeScan 26.0.10 is comprised of the following 2 components:

* 2 Fixes

Component details are listed in their corresponding sections within this document.

### Fixes

#### 1.     Resolved “No Scan Access for Project” Errors Caused by Expired Salesforce Tokens

Fixed an issue where users could encounter a “No scan access for project”/ “expired access/refresh token” error when running scans against Salesforce-connected projects after Salesforce authentication token expiration.

The issue affected environments using Salesforce connected app integrations where expired or invalid access/refresh tokens prevented scan authorization and project access validation.

**Outcome**

* Improved handling of expired Salesforce authentication tokens
* Restored scan access reliability for affected projects
* Reduced scan interruptions caused by token validation failures
* Improved compatibility with Salesforce authentication changes introduced in May 2026

#### 2.     Resolved Intermittent Delays in PR-Scoped EZ-Commit Analysis Jobs

Fixed an issue where PR-scoped EZ-Commit analysis jobs could intermittently remain in the preparing state for an extended period during the “Compute new coverage” step.

In affected scenarios, jobs scanning only a small number of Salesforce metadata files could take significantly longer than expected to complete, eventually resulting in a Start Job Timeout from AutoRABIT ARM™.

**Outcome**

PR-scoped EZ-Commit analysis jobs now complete the new coverage computation step reliably and within the expected processing time.

***

## CodeScan Release 26.0.9

**Release Date: 10 May 2026**

### Summary

CodeScan 26.0.9 is comprised of the following 12 components:

* 1 New Feature
  * NOTE: This New Feature consists of 2 components
* 4 Application Enhancements
  * NOTE: 1 of the Application Enhancements consists of 2 components
* 2 Rule Enhancements
* 3 Fixes

Component details are listed in their corresponding sections within this document.

### New Feature

**1.    Cross-File Analysis in IDE**

**a.     Configurable Cross-File Analysis in IDE Extensions**

Introduced configurable Cross-File Analysis support in the IDE extension to improve rule accuracy for scenarios where analysis depends on context across multiple files.

Previously, the IDE extension performed file-wise analysis only, which could miss issues where logic was split across classes, triggers, or dependent files.

**Behavior**

When Cross-File Analysis is enabled:

* The engine traverses relevant files required by cross-file rules.
* Only issues related to the currently opened file are displayed in the IDE.
* Issues found in other files during traversal are used for context but not shown in the IDE panel.
* Traversal is rule-aware and profile-aware to avoid unnecessary scanning.

**Optimization**

* If a class file is opened, class files are prioritized first.
* If no cross-file rules are active in the Quality Profile, full traversal is skipped.
* Cross-file analysis is disabled by default to preserve performance.

**Outcome**

* More accurate detection for interdependent rules.
* Reduced missed violations in IDE analysis.
* Focused developer feedback without showing unrelated issues.&#x20;

**b.     Cross-File Analysis Controls in UI**

Added UI controls to enable or disable Cross-File Analysis from project-level settings.

**Project-Level Control**

Users can enable Cross-File Analysis for individual projects through:

Project Settings → General Settings → CodeScan → CodeScan Lang → Cross-file Analysis Control

**Outcome**

* Project teams can enable the feature only where needed.
* Improves usability and configurability of Cross-File Analysis.&#x20;

### Application Enhancements

**1.    Issue Exceptions Enhancements**

**a.     Manual Expiry Date for Exception Issues**

Enhanced Exception issue handling by allowing users to manually set an expiry date when marking issue an Exception.

**Behavior**

Users can:

* Select any future expiry date.
* Leave expiry unselected, resulting in No Expiry.
* Override admin-configured default expiry duration.

**System Behavior**

* When the selected expiry date is reached, the issue transitions from Exception → Open.
* Issues with No Expiry remain in Exception status.
* Admin expiry setting changes do not affect issues with manually selected expiry dates.

**Validation**

Validated across UI, API, functional behavior, admin configuration interaction, auto-transition behavior, and bulk issue transitions.

**Outcome**

Improves flexibility and aligns Exception handling with existing hotspot expiry workflows.



**b.     Auto-Assign Expiry Dates for Issue Exceptions**

Enhanced Exception issue handling by allowing Admins to configure automatic expiry dates based on issue severity.

**Admin Configuration**

Instance Admins can enable or disable auto-expiry and configure default expiry duration by severities:

* Blocker
* Critical
* Major
* Minor
* Info

**Behavior**

When enabled:

* Expiry date is calculated as current date plus configured severity duration.
* Expiry is assigned automatically when an issue is moved to Exception.
* Auto-assigned expiry is not editable at project or user level.
* Existing issues are not affected by later admin configuration changes.

**Validation**

Validated through UI, API, workflow transitions, invalid input handling, permissions, bulk assignment, time zone behavior, and regression testing.

**Outcome**

Standardizes SLA handling for exceptions and reduces manual administrative effort.



**2.    Showing Invited Users in Members List with pending status**

We have enhanced user management by showing invited users in the Members list immediately after an invitation is sent:

<figure><img src="../../../../.gitbook/assets/image (2500).png" alt=""><figcaption></figcaption></figure>

Previously, invited users did not appear in the Members tab until they accepted the invitation, making it difficult for admins to track pending invites.

**Behavior**

* Invited users appear under Pending Invitations.
* Status is shown as Invited.
* Once accepted, status changes from Invited → Active Member.
* Empty state displays:\
  &#x20;“No pending invitations. Invite new members to collaborate.”

**Validation**

Validated at organization level, including multiple invites, invite cleanup after 7 days, DB record creation, UI consistency, and status transition.

**Outcome**

Improves administrator visibility, reduces duplicate invite confusion, and provides clearer user management.



**3.    Improved Error Messaging in Invite Module for Existing Users**

Enhanced flow where inviting a user who already exists in the organization displayed a generic error message:

_“An unknown error occurred”_

**Behavior**

The UI now displays the actual backend validation message, such as:

_“This email already exists in the organization”_

**Outcome**

Provides clearer feedback and reduces confusion during user invitations.

&#x20;

**4.    Add Default Salesforce Metadata file suffixes to CodeScan for customers running DX projects**

**Description**

Previously, we only had default settings for files and projects using the metadata type.

This enhancement ensures that CodeScan defaults now cover all types in both metadata and source format.

**The new defaults are now:**

settings

object

profile

flow

workflow

permissionset

profileSessionSetting

sharingRules

profilePasswordPolicy

settings-meta.xml

object-meta.xml

field-meta.xml

profile-meta.xml

flow-meta.xml

workflow-meta.xml

permissionset-meta.xml

profileSessionSetting-meta.xml

sharingRules-meta.xml

profilePasswordPolicy-meta.xml

<figure><img src="../../../../.gitbook/assets/image (2501).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

**1.    Added CVSS Scoring for Security Rules**

Enhanced selected security rules by adding standardized CVSS scoring.

**Rules Updated:**

* Avoid Using Unfiled Public Folders
* GitLeaks Secret Detection in Apex Files
* GitLeaks Secret Detection in Salesforce Metadata Files
* GitLeaks Secret Detection in Visualforce & Lightning Files
* Identify Potential Sensitive PII Fields
* Resource Injection
* Server Side Request Forgery
* Validate Flow Run Context Mode

**CVSS Details Added**

* Base Score
* Temporal Score
* Environmental Score
* Severity Rating
* Vector String, where applicable

**Validation**

Validated in rule details view and CVSS filters. No impact was observed on rule execution or detection logic.

**Outcome**

Improves severity visibility and helps users prioritize remediation more effectively.



**2.    Enhanced AvoidDMLInLoops Rule with Interprocedural Analysis**

Rule key: sf:AvoidSoqlInLoops

Enhanced the Avoid DML/SOQL Inside Loops rule to detect violations across method calls, files, and nested execution paths.

Previously, some violations were missed when DML or SOQL was executed indirectly through methods called inside loops.

**Scenarios Now Supported**

* Recursive call paths
* Deep and nested method chains
* Cross-class traces
* Cross-file scenarios
* While-loop scenarios
* Transitive call chains such as A → B → C → SOQL/DML

**Outcome**

Improves rule accuracy and helps detect governor-limit risks that were previously missed.

### Fixes&#x20;

**1.     Resolved Tag Filter Issue on CodeScan Rules Page**

Fixed an issue where searching for a custom tag on the Rules page returned no results and showed a count of 0 unless additional filters were applied.

**Resolution**

Corrected tag filtering behavior, so matching rules appear immediately when searching by tag.

**Outcome**

* Accurate tag counts.
* Correct rule results.
* No need for extra filtering steps.

&#x20;

**2.     UI Now Displays Actual Duplicate Project Key Message During Project Creation instead of Generic “Unknown Error” Message**

**Description**

While creating a project, if the entered project key already exists, the UI displays a generic error message: “An unknown error occurred”.

However, the actual API response in the Network tab contains a meaningful validation message stating: _“Could not create Project with key: ‘gitleaks’. A similar key already exists: ‘gitleaks’”_.

As such, we have enhanced the UI to now display the backend validation message instead of the generic error so users can clearly understand the reason for the failure.

<figure><img src="../../../../.gitbook/assets/image (2502).png" alt=""><figcaption></figcaption></figure>

**3.     Resolved Blank Edit Project Settings Page for S3 Integration Projects**

Fixed an issue where the Edit Project Settings page appeared blank for S3 integration projects, and console errors were shown.

**Outcome**

Users can now open and update settings for S3-based projects, including memory allocation, without errors.

***

## CodeScan Release 26.0.8&#x20;

&#x20;**Release date: 26 April 2026**

### Summary&#x20;

CodeScan 26.0.8 is comprised of the following 6 components:&#x20;

* 2 Application Enhancements&#x20;
* 4 Fixes&#x20;
* 4 New GitLeaks specific rules introduced

Component details are listed in their corresponding sections within this release document.&#x20;

### Application Enhancements&#x20;



1. **Updated Bitbucket Integration to Use Workspace-Scoped Repository APIs**&#x20;

Bitbucket integration was updated to replace deprecated repository APIs with workspace-scoped APIs.&#x20;

Now CodeScan fetches repositories by:&#x20;

1. Retrieving user workspaces&#x20;
2. Fetching repositories per workspace&#x20;
3. Aggregating results&#x20;

**Outcomes:**&#x20;

* Continued compatibility with Bitbucket API changes&#x20;
* Failures due to deprecated endpoints prevented&#x20;
* Improved reliability of repository fetching &#x20;

**Validation:**&#x20;

Verified the Bitbucket project analysis. Users are able to see the repos as expected, and  the Project analysis and PR analysis are working as expected.

&#x20;

2. **Enhanced Parsering for Methods Named “void”**&#x20;

Earlier, CodeScan parser wouldn’t process Apex methods named **void**.&#x20;

**This enhancement:** &#x20;

* Ensures accurate parsing of valid Apex code &#x20;
* Improves analysis reliability &#x20;

The parser enhancement to support Apex methods named void has been thoroughly validated by QA across multiple scenarios on Preview instance.&#x20;

**Positive Validation Scenarios:**&#x20;

The following valid Apex patterns were tested and are now parsed correctly:&#x20;

* Basic Cases&#x20;
  * public void void() {}&#x20;

Method with body statements&#x20;

* Access Modifiers&#x20;
  * private void void() {}&#x20;
  * protected void void() {}&#x20;
  * global void void() {}&#x20;
* Modifiers & Combinations&#x20;
  * public static void void() {}&#x20;
  * public final static void void() {}&#x20;
* Parameterized Methods&#x20;
  * public void void(String name, Integer count) {}&#x20;
* Annotations&#x20;

@AuraEnabled public static void void() {}&#x20;

* Exception Handling&#x20;

Method containing throw statements&#x20;

* Constructor + Method Coexistence&#x20;

Class containing both constructor and method named void&#x20;

* Multiple Methods&#x20;

Classes with multiple methods including one named void&#x20;

* Method Overloading&#x20;

Multiple overloaded methods named void with different parameters&#x20;

* Nested Structures&#x20;

Method inside inner classes&#x20;

* Test Classes&#x20;

@IsTest classes with method named void&#x20;

* Interface & Implementation Context&#x20;

Class implementing interface along with method named void&#x20;

* Formatting Variations&#x20;

Extra spacing in declaration&#x20;

Multiline method signatures&#x20;

Inline and line comments within method declaration&#x20;

**Negative Validation (Expected to Fail – Parser Strictness Maintained)**&#x20;

The following invalid syntaxes were tested and correctly rejected:&#x20;

* Missing method name&#x20;
  * public void () {} → Parse error&#x20;
* Duplicate return type&#x20;
  * public void void void() {} → Parse error&#x20;
* Missing parentheses&#x20;
  * public void void {} → Parse error&#x20;
* Invalid keyword as method name&#x20;
  * public void class() {} → Parse error&#x20;

These failures are expected and confirm that parser strictness is preserved.&#x20;

**Conclusion**&#x20;

* Parser now correctly supports void as a valid method name in Apex.&#x20;
* All valid usage patterns are successfully parsed across different contexts.&#x20;
* Invalid syntax continues to be rejected as expected.&#x20;
* No regressions observed in parsing behavior.&#x20;

### Fixes&#x20;

1. **Improved Validation for Salesforce User Permissions During ECA Authentication**&#x20;

Fixed an issue where users with insufficient Salesforce permissions could authenticate Salesforce successfully but encountered failures later during analysis.&#x20;

**Resolution:**&#x20;

* Permissions are now validated immediately after authentication &#x20;
* Users without required permissions are blocked early with a clear error message &#x20;

&#x20;

2. **Resolved 403 Error When Activating Rules in US Instance**&#x20;

Fixed an issue where rule activation failed with a 403 Forbidden error in the US instance.&#x20;

**Result:**&#x20;

Rule activation now works consistently across environments &#x20;

&#x20;

3. **Resolved “Component cannot be null” Error in Cross Object Formula Overuse Rule**&#x20;

Fixed a runtime error occurring during PR and subset analyses when related metadata files were not included in the scan.&#x20;

**Result:**&#x20;

* Improved stability of rule execution &#x20;
* Graceful handling of missing metadata &#x20;

QA verified the fix in the Preview environment:&#x20;

* Re-ran the same reproduction steps after the fix deployment&#x20;
* Confirmed that the analysis completes successfully without any errors&#x20;
* Overuse Rule now handles the scenario correctly when the parent .object-meta.xml is not part of analyzed sources&#x20;

&#x20;

4. **Resolved False Positives in Field Level Security Rule for USER\_MODE Queries**&#x20;

Fixed an issue where queries executed in USER\_MODE were incorrectly flagged.&#x20;

**Result:**&#x20;

* Eliminates false positives &#x20;
* Aligns rule behavior with Salesforce FLS enforcement&#x20;

The fix for handling AccessLevel.USER\_MODE has been validated across multiple scenarios on the preview Instance.&#x20;

The following cases were tested and are no longer flagged, as expected:&#x20;

* Direct usage of AccessLevel.USER\_MODE&#x20;
* USER\_MODE via variable assignment&#x20;
* USER\_MODE passed through method parameters&#x20;
* USER\_MODE returned from methods&#x20;
* USER\_MODE used in ternary expressions&#x20;
* Formatting variations of USER\_MODE usage&#x20;

This confirms that the rule now correctly recognizes USER\_MODE across different usage patterns and does not raise false positives when FLS is enforced by Salesforce.&#x20;

#### New GitLeaks Rules in CodeScan

CodeScan has implanted new logic within the Rules Engine that can detect GitLeaks vulnerabilities. GitLeaks is a tool for detecting secrets like passwords, API keys, and tokens. We have extended this logic to cover Salesforce specific languages and components.

The following rules are introduced:

1. **Rule Name:** GitLeaks Secret Detection in Apex Files\
   **Rule ID:** sf:ApexGitLeaksSecrets\
   This rule runs GitLeaks on Apex source files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
2. **Rule Name:** GitLeaks Secret Detection in Salesforce Metadata Files\
   **Rule ID:** sfmeta:MetadataGitLeaksSecrets\
   **Description:** GitLeaks Secret Detection in Salesforce Metadata Files: This rule runs GitLeaks on Salesforce Metadata files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
3. **Rule Name:** GitLeaks Secret Detection in Visualforce & Lightning Files\
   **Rule ID:** vf:VFLightningGitLeaksSecrets\
   **Description:** This rule runs GitLeaks on Visualforce source files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
4. **Rule Name:** GitLeaks Secret Detection in Javascript\
   **Rule ID:** cs-js:javascript-gitLeaks-secrets\
   **Description:** This rule runs GitLeaks on Javascript files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.

**Summary**\
These rules run GitLeaks on Salesforce source files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.

**Availability:**\
This feature is currently available on **AUS and EU instances**.\
&#x20;

***

## CodeScan Release 26.0.7

**Release Date: 12 April 2026**

### Summary

CodeScan 26.0.7 is comprised of the following 8 components:

* 3 New Features
* 1 Application Enhancement
* 4 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

**1.     GitHub Apps Integration for GitHub Enterprise in CodeScan**

**Description**

Users of GitHub Enterprise can now connect their GitHub Enterprise organization to CodeScan using a GitHub App. This allows CodeScan to securely access repositories, receive webhook events, and perform code analysis without relying on personal access tokens or user-owned credentials.

**Benefit**

Because CodeScan can now integrate with GitHub Enterprise via a GitHub App, authentication is now more secure, scalable, and enterprise compliant. This reduces credential management issues while enabling reliable multi-repo and multi-org analysis.

**Value / Purpose**

* Enables enterprise-grade authentication aligned with GitHub’s recommended model.
* Supports secure, scalable access across multiple organizations and repositories.
* Improves compliance, auditability, and long-term maintainability of CodeScan’s GitHub integrations.

We have validated the GitHub Enterprise flow in CodeScan for the following scenarios and verify that all are working as expected:

* Main branch analysis
* Pull Request analysis
* Merge request analysis
* Run manual analysis
* Re-run analysis
* Schedule jobs analysis
* Delete analysis
* Rename analysis

For creating a GitHub App for an Enterprise account, users need to follow the steps outlined in the documentation [CodeScan GitHub Apps Integration (Technical Approach)](https://app.gitbook.com/o/vIHQCTOOUDcNoPic3AQi/s/9vAxMuDrkUkB4OXlH9CL/product-guides/codescan/codescan-integration/codescan-github-apps-integration-for-github-enterprise). Once completed, users need to create an ALM connection in the CodeScan application by providing the following details:

* App ID
* Client ID
* Client Secret

After successfully creating the connection with the GitHub Enterprise account, users will be able to run the analysis.

<figure><img src="../../../../.gitbook/assets/image (2470).png" alt=""><figcaption></figcaption></figure>

Please note these important TECHNICAL details:

1\. GitHub Apps Authentication Flow Change:

After implementing the GitHub Apps feature, the flow of authorization has changed for the user. For the first-time user, they will be navigated to the GitHub apps installation page, where they need to Authorize and Install the app. Then, the user will be navigated to the CodeScan GitHub Integration pop-up to run the analysis.

&#x20;2\. GitHub Apps - Token Refresh:

How it works:

* Before API calls, check if token expired
  * If expired, automatically refresh (generate new JWT → get new token)
* NOTE: We have updated all API call methods to support both OAuth and GitHub Apps, and verified that OAuth continues to work (it is backward compatible).
* Additionally, analysis execution was verified after 8 hours, confirming that the token refresh mechanism (every 8 hours) is functioning as designed.

**2.     Added a new {Resolution} Status for Issues – “Exception”**

**Description**

We have introduced a new **Exception** status in the issue lifecycle that allows users to mark an issue as an approved exception when the organization decides not to remediate it due to valid business or technical reasons.

When an issue is moved to the **Exception** status, CodeScan captures and stores the justification for auditing and tracking purposes. The status appears alongside existing issue statuses and is visible in issue details, filters, and reports.

NOTE: The following description has been added to the Exception status: “The issue has an approved exception and will be re-reviewed until mitigated or upon exception expiry.“

**Benefit**\
Users are provided with a dedicated **Exception** status, allowing them to clearly differentiate between resolved issues and intentionally accepted risks. This improves issue tracking, compliance transparency, and auditability.

**Value / Purpose**

* Enables teams to formally document and track approved risk exceptions.
* Improves visibility and governance over issues that are intentionally not fixed.

Validated this new feature via the following scenarios and have verified that all scenarios are working as expected.

1.  Exception status is available in the status list in issues page.<br>

    <figure><img src="../../../../.gitbook/assets/image (2471).png" alt=""><figcaption></figcaption></figure>
2.  Issues status changed to Exception (through single assign and bulk assign).<br>

    <figure><img src="../../../../.gitbook/assets/image (2472).png" alt=""><figcaption></figcaption></figure>


3.  Issues status changed from Exception to Open (Rollback) (through single assign and bulk assign).<br>

    <figure><img src="../../../../.gitbook/assets/image (2473).png" alt=""><figcaption></figcaption></figure>
4.  Able to view the Exception status in CSV Issues export (in list and downloaded CSV).<br>

    <figure><img src="../../../../.gitbook/assets/image (2475).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (2476).png" alt=""><figcaption></figcaption></figure>


5.  Status visible in a single rule.<br>

    <figure><img src="../../../../.gitbook/assets/image (2477).png" alt=""><figcaption></figcaption></figure>


6.  Comments in Activity.<br>

    <figure><img src="../../../../.gitbook/assets/image (2478).png" alt=""><figcaption></figcaption></figure>

    Comments in the activity section for Exception are able to deleted by the user (after these issues are moved into exception).<br>

    Also, user already assigned to issues will remain assigned, even when moved to exception (if issue assigned before moving or while moving the issues to exception).



**3.     New Email Notifications alert admins when (Pre & Post) Project Analysis Errors occur** &#x20;

**Description**

Currently, users receive email notifications primarily for Quality Gate results, but failures occurring during the **project analysis lifecycle** are not communicated. This enhancement aims to include **pre-analysis and post-analysis errors** via email subscriptions, so users can be proactively informed when analysis fails.

The scope includes:

* **Pre-Analysis Errors**
  * Queue setup failures
  * Branch does not exist
  * Salesforce authentication issues
  * Authorization token (Auth token) failures
* **Post-Analysis Errors**
  * Compute Engine (CE) job timeout
  * Cleanup job delays or long-running failures

When such errors occur, an email notification is triggered (based on user subscription preferences), providing high-level error details and guidance for resolution.

**Benefit**

Users are notified about analysis failures (both pre and post stages) via email, enabling them to quickly identify and resolve issues, reducing failed analysis cycles, improving system trust, and decreasing support dependency.

**Value / Purpose**

* Improves visibility into analysis failures beyond Quality Gate results
* Reduces turnaround time for issue resolution

Validated that users are able to receive the email notifications for pre/post analysis errors, and verified that these users are able to receive notifications as expected. Several examples have been provided below for illustrative purposes.

<figure><img src="../../../../.gitbook/assets/image (2479).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2480).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2481).png" alt=""><figcaption></figcaption></figure>

Please note these important TECHNICAL details:

1\. We have included the ability for users to Enable / Disable Subscription for Analysis Failure Notifications so that users can manage whether they need to receive failure alerts based on chosen preferences.

The system will leverage the **existing subscription-specific UI,** i.e., _**Profile> My Account>Notifications> Overall Notifications,**_ to allow users to opt in or opt out of analysis failure notifications.

<figure><img src="../../../../.gitbook/assets/image (2482).png" alt=""><figcaption></figcaption></figure>

User preferences will be persisted using APIs, and any changes will be applied immediately when resolving notification recipients for analysis failures.

**Benefit**

End users can independently manage their own subscriptions for analysis failure notifications,\
then notifications will be **more relevant at an individual level**, reducing alert fatigue while ensuring the right users stay informed.

**Value / Purpose**

* Empowers **all end users** to manage their own notification preferences.
* Reduces **unwanted or noisy alerts** from intermittent analysis failures.

**Acceptance Criteria**

* The **“Project analysis execution failures”** checkbox is available under **Overall Notifications** for all users.
* Users can **enable or disable** the checkbox to manage their personal subscription.
* The checkbox state **reflects the user’s current saved preference** on page load.
* Any change to the checkbox is **persisted immediatel**y via the notification subscription APIs.
* Subscription changes take effect **without page refresh**.
* Only users with the checkbox **enabled receive email notifications** when a project analysis execution failure occurs.
* Users with the checkbox **disabled do not receive** analysis execution failure notifications.
* Changes to the subscription are **applied immediately** during notification recipient resolution.
* Users subscribed to get the notification should receive emails for only the projects to which they have access. Users should not get mail notification for projects they are not part of.

The ticket “Enable / Disable Subscription for Analysis Failure Notifications” has been verified successfully.

* The user is able to view the option “Project analysis execution failure on my administered projects.”
* A checkbox is available alongside this option.
* The user can enable and disable the checkbox as expected without any issues.

Functionality is working as expected.

<figure><img src="../../../../.gitbook/assets/image (2483).png" alt=""><figcaption></figcaption></figure>

2\. Triggered Email Notifications are immediately sent to Subscribed Users on Analysis Failure, so they can be promptly informed and subsequently take action without waiting for manual checks or follow-up runs.

When an intermittent project analysis failure is detected, the system will **trigger notifications in real time**, resolve recipients using the **Notification Subscribers module**, and send **email notifications containing relevant project context and failure details**.

**Benefit**

Subscribed users are notified immediately when intermittent analysis failures occur; teams can quickly **identify and address failures faster**, reducing downtime, re-runs, and uncertainty around analysis results.

**Value / Purpose**

* Provides **timely visibility** into intermittent analysis failures
* Ensures notifications are sent **only to subscribed users**
* Enables **faster troubleshooting and recovery**

### Application Enhancements

**1.     Track Cursor IDE Usage in the VS Code Extension**

**Description**

In our previous release (CodeScan 26.0.6), we delivered a new CodeScan feature that captures the Cursor IDE usage details (User Name, IDE Type = Cursor, Timestamp) within CodeScan Cloud. This allows customers to track IDE adoption, user activity, and engagement trends alongside existing usage data. (You can find more details under “Track Cursor IDE Usage on CodeScan 'IDE USAGE' Page” within those release notes as well as our Knowledge Base.)

In this release, we have enhanced this capability within the IDE plug-in, which allows us to more precisely determine whether the user is currently on Cursor or VS Code. We then send this value to CodeScan Cloud.

1. Verified the Cursor plugin using the provided VSIX file across multiple file types: .cls, .page, .java, .js, .trigger, .css, .ts, and .cmp. Violations are displayed as expected.
2. Also verified the IDE Usage page, where Cursor usage is correctly reflected. We have tested and validated with multiple users and verified cross-user usage visibility is working as expected on the IDE Usage page.
3. Additionally, verified the VS Code plugin using the same VSIX file. Violations are displayed correctly for all supported file types, e.g., .cls, .page, .java, .js, .trigger, .css, .ts, .cmp, in the PREVIEW environment.
4. Confirmed that VS Code usage is accurately shown on the IDE Usage page and validated that cross-user usage visibility is also functioning as expected.

<figure><img src="../../../../.gitbook/assets/image (2484).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1.     Fixed issue with rule “Unescaped Error Message XSS” {Rule ID: sf:UnescapedOutput}**

**Summary**

Several customers were reporting a StackOverflowError for the rule “Unescaped Error Message XSS” {Rule ID: sf:UnescapedOutput}

Earlier, the Unescaped Output Rule was able to trace data flow through methods but not through assignment chains effectively. Due to missing/inefficient assignment data flow handling, the rule repeatedly re-entered isSanitized while resolving sanitization status for variables passed through assignments. This resulted in deep recursive calls and ultimately a StackOverflowError, instead of reporting a violation.

**Reproduction Analysis:**\
Initial attempts with small assignment chains did not reproduce the issue. The issue was successfully reproduced only with very deep assignment chains (\~5,000 assignments).

This indicates that:

* The problem is related to **depth of assignment traversal**
* Recursive evaluation of isSanitized leads to stack overflow at large depths

**Validation**

✔ Rule evaluation now terminates correctly without recursion overflow\
→ Verified. No StackOverflowError observed even for deep assignment chains.

✔ isSanitized now handles edge cases without re-entering indefinitely\
→ Verified. Deep assignment chains no longer cause recursive overflow.

As such, we confirm that the issue has been successfully remediated. The rule now handles deep assignment chains correctly and avoids infinite recursion in isSanitized, without causing a StackOverflowError.

<figure><img src="../../../../.gitbook/assets/image (2485).png" alt=""><figcaption></figcaption></figure>



**2.     Fixed issue with rule “Avoid Cleartext Transmission of Sensitive Information”**

{Rule ID: sf:InsecureEndpoint}

**Summary**

Previously, the rule InsecureEndpointRule was throwing a ClassCastException due to an invalid cast from ClassNameDeclaration to VariableNameDeclaration when analyzing endpoint expressions involving enum/class references (e.g., MODE.ERASE).&#x20;

**After the fix:**

* Proper type checking has been implemented before casting symbol table declarations.
* The rule now safely handles enum and class references without making incorrect assumptions.
* No runtime exceptions are observed during analysis.

**Result:**

* No ClassCastException observed.
* Rule executes as expected across all tested scenarios.&#x20;



**3.     Fixed issue with rule “Field Level Security Vulnerabilities” {Rule ID: sf:FieldLevelSecurity}**

**Summary**

Previously, the rule FieldLevelSecurityRule was throwing a NullPointerException when analyzing DML operations (Database.update) inside a trigger body due to the absence of an enclosing ASTMethodDeclaration. The failure was a NullPointerException caused by attempting to invoke findChildNodesWithXPath on a null methodDeclaration object within FieldLevelSecurityRule.

**After the fix:**

* Proper null handling for methodDeclaration has been implemented.
* The rule no longer assumes the presence of a method context.
* Trigger-based DML scenarios are now handled gracefully without runtime exceptions.

**Result**:

* No NullPointerException observed.
* Rule behaves as expected.&#x20;



**4.     Fixed issue with rule “Resource Injection”** {Rule ID: sf:ResourceInjection}

**Description**

Several customers were reporting a StackOverflowError for the rule “Resource Injection” {Rule ID: sf:ResourceInjection}. Based on the analysis of logs and review of implementation, we uncovered an infinite recursive call in the isSanitized method in the UrlSanitization.java and determined that this is the reason for the StackOverflowError.

Previously, the analysis stayed in Running state and logs showed a StackOverflowError for the mutual-recursion flow (methodA -> methodB -> methodA) with no exit condition, ending in req.setEndpoint(url) with the Rule Resource Injection. After the fix, the same code analyzes successfully, completes normally, and no StackOverflowError is observed in logs.

**Validation after fix:**

* Ran analysis on CodeScan
* Analysis completed successfully
* Analysis no longer remained in Running state
* StackOverflowError was no longer seen in logs

As such, we are reporting that this issue has been fully remediated.

***

## CodeScan Release 26.0.6

**Release Date: 29 March 2026**

### Summary

CodeScan 26.0.6 is comprised of the following 5 components:

* 1 New Feature
* 4 Application Enhancements
* 1 Fix

Component details are listed in their corresponding sections within this document.

### New Features

**1.     CodeScan Audit Logs API**

**Description**

Currently, the Audit Logging API is available only for internal use by AutoRABIT. This new feature enables our customers to access audit logs via a secure, user-facing API (which is restricted to organization-level administrators with _Administer System_ permissions.

The API will allow these authorized org admins to view system and user activity events related to their organization, ensuring appropriate access controls and data isolation.

**Hypothesis**

If organization administrators are given access to audit logs for their organization, they will be better equipped to monitor platform usage, investigate issues, and meet internal governance or compliance requirements, reducing reliance on CodeScan support for routine operational visibility.

**Value / Purpose**

* Provides greater transparency and trust for enterprise and security-conscious customers.
* Empowers org admins to self-serve audit and usage insights without support intervention.
* Supports compliance, security reviews, and internal audits.<br>

**Audit log API**

For more details, refer to the [CodeScan API Documentation.](../../../../product-guides/codescan/codescan-api-documentation/)

### Application Enhancements

**1.     Configurable Default User Role for SSO-Provisioned Users**

**Description**

Currently, users created via SSO are **always provisioned as CodeScan Standard Users**. This creates manual overhead for admins who need certain users to be assigned **Platform User** roles after login.

This new feature allows organization admins to configure the default CodeScan user role (Standard User or Platform User) for users provisioned via SSO, including UI updates in SSO setup, back-end role assignment logic, data model impacts, security considerations, and backward compatibility with existing SSO configurations.

**How It Works**

User type selection directly in the SSO/SAML configuration page to select either Platform Integration Users or Standard users.

<figure><img src="../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

The following scenarios have been verified and are working as expected:

* **SAML Connection Creation (New Org)**
  * Created a SAML connection on a new organization.
  * Verified login with a user.
  * Result: User was able to log in successfully.
* **Platform User Login Validation**
  * Updated the user type to **Platform User**.
  * Logged in using a newly created user.
  * Result: Login was successful, and the user could access **only the My Account page**, as expected for Platform users.
* **Standard User Login Validation**
  * Updated the user type to **Standard User.**
  * Logged in using the new user.
  * Result: Login was successful as a **Standard User**.

Further, we verified the behavior for the previous user also, and it is working as expected via SAML authentication.&#x20;

**2.     Track Cursor IDE Usage on CodeScan 'IDE USAGE' Page**

**Description**

This CodeScan feature captures the Cursor IDE usage details (User Name, IDE Type = Cursor, Timestamp) within CodeScan Cloud, allowing customers to track IDE adoption, user activity, and engagement trends alongside existing usage data.

Additional details regarding the Cursor IDE usage data:

* Stored consistently with existing IDE usage records
* Viewable using existing filters:
  * Individual user
  * All users
  * Last X days
* Can be exported as CSV for reporting and analysis

Verified the Cursor IDE Usage on CodeScan in the page 'IDE USAGE' of the Adminstration and confirmed users are able to see the added Cursor symbol through the API call in the UI of the application. We also verified that existing behavior for VS Code and Intellij is working as expected.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;**3.     Updated Filter Message for Security Hotspot CSV Export**

**Description**

When exporting Security Hotspots, if the user chooses a list of filters that do not match any security hotspots, the current message displayed was: **"Security Hotspots not found."**

We have updated the message to provide greater clarity: **"No Security Hotspots have been found with the current filters."**

Verified the updated Security Hotspot export filter message.

* The message displayed is **“No Security Hotspots have been found with the current filters,”** instead of **“Security hotspot is not found.”**
* Validated exporting Security Hotspots by changing the status to **Acknowledged, Exception, Fixed, and Safe** — the exported count matches the respective status correctly.
* Validated exporting Security Hotspots with status **To Review** — the export shows the exact count of items currently in the **To Review** state.

All the above scenarios are working as expected.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**4.     Automatically generate Callback URL when adding ECA in Salesforce Org**

**Description**

Currently, while adding an ECA in Salesforce Org, the application does not provide a dynamically generated Callback URL for External Client App (ECA) configuration.

* Users are required to manually construct and enter the Callback URL in Salesforce during ECA setup. The system does not display the exact instance-specific Callback URL within the application, nor does it provide a copy-to-clipboard option.
* Users will assume the Call back URL as https://**\{{hostname\}}**.codescan.io, but the actual Callback URL that needs to be given while creating the ECA could be different.

This manual process increases the risk of:

* Typographical errors
* Missing or incomplete URL entries
* Configuration failures due to incorrect Callback URL
* Increased onboarding/support effort

**As such, we decided to enhance this feature by:**

* Automatically generating the Callback URL.
* Dynamically constructing it based on the selected/connected instance/environment (e.g., test, preview).
* Ensure correct and consistent formatting.
* Clearly display the generated Callback URL on the “Add Salesforce Org” screen.
* Make it visible at the point of ECA configuration.
* Provide a **“Copy”** button next to the generated URL.
* Allow one-click copying of the exact URL.
* Prevent manual typing errors.

Steps Taken

Implemented Callback URL button in the UI.

Added a custom tooltip, copy icon and copied label when user copies the URL

We have verified that **Callback URL** is displayed correctly, and the **Copy** button is working as expected.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**NOTE:** When hovering over the Callback URL button, the notes are displayed. The notes do not disappear when clicking on the Callback URL. They only disappear when clicking anywhere else on the page. This is the expected behavior.
{% endhint %}

### Fixes

**Custom Rule creation validation update:**

1. Resolved an inconsistency between custom rule creation and update workflows. Previously, the update flow enforced stricter validation on the description field, restricting certain formats (e.g., descriptions containing HTTP/HTTPS protocols). \
   With this fix, the additional validation has been removed from the update flow. Users can now update rule descriptions with any valid content, including URLs or HTTP/HTTPS references, ensuring consistency with the rule creation behavior.

***

## CodeScan Release 26.0.5

**Release Date: 15 March 2026**

### Summary

CodeScan 26.0.5 is comprised of the following 8 components:

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

<figure><img src="../../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Value / Purpose**

* Improves transparency and auditability of hotspot status changes in exported reports.
* Enables teams and managers to identify responsibility and follow up more effectively.&#x20;



Verified the following scenarios are all working as expected.

* Verified with multiple users, users getting updated as expected.
* Verified with root user - status marked by updated as administrator.
* Verified by removing org user, name is still shown in CSV - working as expected.
* Verified with deactivated user, name is still shown in CSV - working as expected.
* Verified with deleted user, the status marked by field is empty.



* Issues:
  * Also, verified that if user clicked on export after selecting the project and branch - only those security hotspots that are available for review are getting download (not the reviewed ones)
  * Also, if the user selects only certain reviewed options, all the reviewed getting downloaded.



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

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>



**4.     Added Closed Issue Statuses to CSV Reports**

**Description**

Currently, CSV reports do not clearly distinguish closed issue statuses, such as **Closed** and **Removed**. As such, we have enhanced the CSV export functionality to include these closed statuses explicitly in the Status column. The exported CSV now accurately reflects the latest lifecycle state of each issue, including closed states, ensuring consistency with what users see in the UI.

**Hypothesis:**

If CSV reports include detailed closed statuses (Closed, Removed ), users will gain better visibility into issue resolution outcomes, enabling more accurate reporting, compliance tracking, and stakeholder communication. This will reduce manual effort in categorizing closed issues after export.

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

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

### New Rule

**1.     New Rule: “Locale Formats in API Versions pre-v45.0” {Rule ID: sf:LocaleInOldApi}**

**Description**

This rule finds locale methods in Apex classes with API versions below v45.0.  Locale formats before Salesforce API v45.0 default to JDK format. Now, locale formats default to ICU. It is recommended to update all components using API versions prior to v45.0 or use locale-neutral methods.

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

&#x20;

1. **Positive Validation (API Version < 45.0)**
   * Created Apex classes with API version 44.0 and used the above locale-dependent methods.
   * These cases are expected to be flagged since API versions prior to v45.0 rely on JDK locale formatting.
2. **Negative Validation (API Version ≥ 45.0)**
   * Created Apex classes with API version 45.0 and above using the same methods.
   * These cases are not expected to be flagged, since API v45.0+ uses ICU locale formatting by default.
3. **Verification Outcome**
   * The rule behavior was validated against the defined conditions.
   * Classes with API versions prior to v45.0 and using locale-dependent methods are considered for detection, while classes with API v45.0+ are treated as compliant.

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

1\.       Enhanced data flow analysis logic in rule “Avoid Untrusted/Unescaped Variables in DML Query” {Rule ID: sf:SOQLInjection}

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

<figure><img src="../../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is reassigned multiple times - the issue will be thrown based on the last assigned value.

<figure><img src="../../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is sanitized first and later overwritten with random function. - error thrown.
* In a condition, Verified when a variable is sanitized first and later overwritten with random function. - error thrown.

<figure><img src="../../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

* Verified when a variable is assigned inside a loop before being used in the query. - If loop has non sanitized parameters then issue is thrown
* Verified when a user input flows through multiple helper methods before reaching the query. - trace throws error up to 5 params.

<figure><img src="../../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

&#x20;

**2.     Added a new parameter to the rule “Test Class Names Should Include Test”**{Rule ID: sf:TestClassNaming}

**Description**

Several customers had reported that the CodeScan rule “Sf:testclassnaming” was producing false positives for classes containing “test”.

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
* Particular Reg expressions given in the allowed parameters skips the violations Accordingly.

<figure><img src="../../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1.       Set default value to “false” for “is\_archived” column in organizations table.**

**Summary of Issue**: Several customers were reporting an issue where users were unable to log in via SAML after their instance was upgraded to 26.0.3\
\
**Cause of Issue**: During our analysis, we identified that, as part of the upgrade process, a database field was unintentionally set to NULL instead of the defined default value. This disrupted the login via SAML.

**What was done to resolve**: A query was run to update the Null value to the default value.

**What we did to prevent it from happening again**: We have documented the corrective measures required to prevent this scenario in future upgrades. These improvements will be incorporated in an upcoming release to further strengthen the reliability of the upgrade process

Verified the database for the orgs table, confirming that the “is\_archived field” is not NULL, and that DBAs are able to see the value set as **false** for all organizations in the environment.

Also verified that users who login with SAML are unblocked, which we confirmed by creating a new SAML connection on a new organization. All users are able to log in successfully without any issues.

***

## CodeScan Release 26.0.4

**Release Date: 01 March 2026**

{% hint style="info" %}
As of release 26.0.4, CodeScan has adopted the External Client App (ECA) flow for Salesforce, replacing our existing Connected Apps flow.&#x20;

Key points:

1. If you have an existing Salesforce org registered, you are using the existing Connected App flow. No action is required at this time, and your analyses will run as expected.
2. Please note that any new Salesforce org you wish to register in CodeScan must use the new [local ECA flow](../../../../product-guides/codescan/getting-started/connection-to-salesforce-with-eca.md).
3. Please note that if your existing Salesforce orgs need to be reattached, if your tokens expire, or after Sandbox refresh, your Connected App flow will no longer work, and you will need to re-register your org using the[ local ECA flow](https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/connection-to-salesforce-with-eca). Please note that in these circumstances, your comparison branches in Salesforce will need to be set up again.
{% endhint %}

### Summary

CodeScan 26.0.4 is comprised of the following 2 components:

* 1 Application Enhancement
* 1 Fix

Component details are listed in their corresponding sections within this document.

### New Features

There are no New Features in this release.&#x20;

### Application Enhancements

**1.     Salesforce External App Connection**

**Description**

To align with Salesforce Spring ’26 security requirements, CodeScan now offers an authentication flow for External Client Apps (ECA).

What’s changed:

* CodeScan now supports Salesforce’s updated authentication standards for External Client Apps.
* Connectivity remains seamless once authentication is configured.

Customer Action Required:

* When adding new Salesforce orgs via External Client Apps, the following needs to be provided:
* Client ID
* Client Secret

What stays the same:

* No changes to core CodeScan functionality.
* No changes to user workflows after successful authentication.

This update ensures continued secure and compliant integration with Salesforce orgs under updated platform security requirements.

For more detailed information, please review AutoRABIT’s published article “Salesforce OAuth External Client App (ECA) Transition” at [https://knowledgebase.autorabit.com/fundamentals/announcements/salesforce-oauth-external-client-app-eca-transition](https://knowledgebase.autorabit.com/fundamentals/announcements/salesforce-oauth-external-client-app-eca-transition)

### New Rules

There are no New Rules in this release.&#x20;

### Rule Enhancements

There are no Rule Enhancements in this release.

### Rule Deprecations

There are no Rule Deprecations in this release.

### Fixes

1\.       Fixed issue with data flow analysis logic in rule “Avoid Untrusted/Unescaped Variables in DML Query” {Rule ID: sf:SOQLInjection}

**Description**

We identified an issue in CodeScan where the Data Flow Trace for a SOQL injection rule where the trace repeatedly shows the same assignment instead of a clean, non-duplicated trace.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

We determined the root cause of the issue and updated the rule logic accordingly.  With this fix, this issue is now fully remediated.Top of Form

Verified the following scenarios and report that the rule is now working as expected.

* Verified for duplicated traces : verified along with test instance\
  in preview: no duplicated traces

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## CodeScan Release 26.0.3&#x20;

**Release Date: 15 February 2026**

### Summary

CodeScan 26.0.3 is comprised of the following 5 components:

* 1 New Feature
* 2 Application Enhancements
* 1 New Rule
* 1 Fix

Component details are listed in their corresponding sections within this document.

### New Features

**1.     Expiry Dates for Exception Status on Security Hotspots**

**Description**

The Exception Status has previously been added to the CodeScan Security hotspots.

This new feature allows for configurable expiry dates for the Status.

The user wants to add the status with an expiry date so when changing the hotspot status, they can supply a date when the issue will reopen as “To review”.

Default will be no expiry. It will stay in the Exception Status until it is moved manually or given an expiry date.

**Acceptance Criteria**

* The ability to add an expiry date to the Security Hotspot resolution
* The HotSpot needs to return to “to review” status when the expiry date is reached.
* The expiry is optional and configurable; further, it can be any date in the future.
* The Expiry date selector can be the same style as found in the issues page under creation date

Verified the Security Hotspot Exception expiry behavior from the CodeScan UI on Staging Environment.

* Users can optionally set an expiry date while changing a hotspot status to **Exception**.
* Hotspots without an expiry remain in **Exception** status.
* Hotspots with an expiry date automatically reappear in “**To review**” after the expiry is reached.

<figure><img src="../../../../.gitbook/assets/image (2425).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2426).png" alt=""><figcaption></figcaption></figure>

Also verified the scheduled job functionality for the Security Hotspots.

* Security Hotspots marked as **Exception** remain unchanged when no expiry date is provided.
* When an expiry date is set, the scheduled job automatically transitions the hotspot back to “**To review**” after the expiry is reached.

<figure><img src="../../../../.gitbook/assets/image (2428).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2429).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2430).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2431).png" alt=""><figcaption></figcaption></figure>

### Application Enhancements

**1.     CVSS Metrics: Advanced Calculations**

**Description**

The current descriptions of our vulnerabilities do not contain the metrics for CVSS. There are multiple variables that determine a CVSS score and with this update, users will now be able to see this level of detail.

Use the following vulnerability rule values in CodeScan to provide all necessary inputs for calculating the CVSS score.

Vulnerability Rule Details

Rule Title: Array is Stored Directly

Rule Name: sf:ArrayIsStoredDirectly

Type: Vulnerability

Language: Apex

Description:

Constructors and methods receiving arrays should clone objects and store the copy.

This prevents future changes from the user affecting the internal functionality.

See

MITRE, CWE-374 - Passing Mutable Objects to an Untrusted Method

CERT, OBJ06-J. - Defensively copy mutable inputs and mutable internal components

CERT, OBJ13-J. - Ensure that references to mutable objects are not exposed

Rule Message: (Not specified)

Severity Level: Major

Example:

public class Foo {

&#x20; private String \[] x;

&#x20;   public void foo (String \[] param) {

&#x20;     this.x=param;                //Bad: don't do this, make a copy of the array at least.

&#x20;   }

}

Tags: cwe, cert, unpredictable

Remediation Effort:  5min-constant\_issue

**Additional Information**:

Meaning of severity in CodeScan, use this to calculate CIA:

BLOCKER has a value of 1

CRITICAL 2

MAJOR 3

MINOR  4

INFO has a value of 5

With this completed, we now provide the following values in tabular form, specify the vector and give the CVSS score:

**Base Score Metrics**

* Attack Vector (AV) (specify)
* Attack Complexity (AC) (specify)
* Privileges Required (PR) (specify)
* User Interaction (UI) (specify)
* Scope (S) (specify)
* Confidentiality Impact (C) (specify)
* Integrity Impact (I) (specify)
* Availability Impact (A) (specify)

**Temporal Score Metrics**

* Exploit Code Maturity (E) (specify)
* Remediation Level (RL) (specify)
* Report Confidence (RC) (specify)

**Environmental Score Metrics**

* Modified Attack Vector (MAV) (specify)
* Modified Attack Complexity (MAC) (specify)
* Modified Privileges Required (MPR) (specify)
* Modified User Interaction (MUI) (specify)
* Modified Scope (MS) (specify)
* Modified Confidentiality Impact (MC) (specify)
* Modified Integrity Impact (MI) (specify)
* Modified Availability Impact (MA) (specify)
* Confidentiality Requirement (CR) (specify)
* Integrity Requirement (IR) (specify)
* Availability Requirement (AR) (specify)

**CVSS Descriptions UI/UX Update**

**2.      CVSS: UI/UX Update**

**Description**

Per the enhancement above, all the CVSS rules are now updated with CVSS score values in the CVSS Break Down tab UI provided (below Metric category specific tabs).

<figure><img src="../../../../.gitbook/assets/image (2432).png" alt=""><figcaption></figcaption></figure>

All the below Vector Metric names and values of score table are now visible in above UI

<figure><img src="../../../../.gitbook/assets/image (2433).png" alt=""><figcaption></figcaption></figure>

Verified the CVSS UI/UX update via the following scenarios:

* The CVSS Breakdown tab correctly shows Base, Temporal, and Environmental score sections.
* All vector metric names and values are displayed as per the updated CVSS v3.1 table for CodeScan vulnerability rules (VF, SF, Apex).
* Update is visible and working as expected.

<figure><img src="../../../../.gitbook/assets/image (2434).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2435).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2436).png" alt=""><figcaption></figcaption></figure>

### New Rules

**1.     New Rule: “Avoid Using Unfiled Public Folders” {Rule ID: sf-meta:AvoidUnfiledPublic}**

**Description**

This rule detects when Salesforce records are stored in unfiled public folders (identified by the path "unfiled$public").

Unfiled public folders pose several security and governance risks:

* **Lack of Organization**: Records in unfiled public folders are difficult to manage, locate, and maintain, leading to poor data governance
* **Excessive Access**: Public folders are accessible to all users in the organization by default, potentially exposing sensitive data to unauthorized users
* **No Access Controls**: Unfiled public folders typically lack granular permission settings, making it impossible to restrict access based on role or profile
* **Compliance Risk**: Storing records in unsecured, publicly accessible locations may violate data privacy regulations (GDPR, HIPAA, etc.)
* **Audit Trail Issues**: Unfiled public folders make it difficult to track who accessed or modified records

Best practices recommend organizing all Salesforce records into properly structured folders with:

* Clear naming conventions
* Appropriate sharing settings
* Role-based access controls
* Regular audits and cleanup processes

Move metadata from unfiled public folders to dedicated folders with restricted access aligns to business requirements and the principle of least privilege.

**Type**: Vulnerability

**Message**: Metadata should not be stored in unfiled public folders

**Tags**: **CWE**: 732\
**Remediation**: 5 minutes

Verified the newly added CodeScan rule **sf-meta:AvoidUnfiledPublic (Avoid Using Unfiled Public Folders**) via the following scenarios:

* The rule description is visible in CodeScan and correctly explains the security and governance risks associated with storing Salesforce metadata in unfiled public folders.
* The rule is working as expected and consistently raises violations whenever Salesforce metadata is stored under a file path containing /unfiled$public/.
* This behavior is expected, as metadata placed in unfiled public folders can lead to unrestricted access, lack of proper organization, and potential compliance concerns.
* No issues were observed with the rule configuration or behavior.

<figure><img src="../../../../.gitbook/assets/image (2437).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2438).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1.       Fixed issue with rule “Sf:fieldlevelsecurity” where user mode subquery false positive was reported**

**Description**

If code is running in the user mode, it should not need to check FLS, since user mode already does that. As such, CodeScan should not flag the rule/violation if it is in user mode. Only if it is not in user mode should the rule be triggered. However, several customers have reported that this behavior is not occurring properly.

We have determined the root cause, and have concluded that there is an edge case that was not accounted for in our logic. Specifically, when the mode is defined via AccessLevel in the return statement, the rule incorrectly flags it as a violation, resulting in a false positive.

For further reference, please see Salesforce Developers - Accesslevel Class [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_AccessLevel.htm)

This scenario wasn’t currently handled by the rule logic but has been addressed with a logic update.

The issue has now been fully remediated with this release.

Verified the Sf:fieldlevelsecurity – USER\_MODE subquery false positive via several scenarios and confirm that the rule now correctly skips FLS violations when AccessLevel.USER\_MODE is provided via **direct assignment**, including:

* Inline usage in Database.getQueryLocator
* Simple variable assignment (AccessLevel mode = AccessLevel.USER\_MODE)

which resolves the originally reported false positive.

<figure><img src="../../../../.gitbook/assets/image (2439).png" alt=""><figcaption></figcaption></figure>

***

## CodeScan Release 26.0.2

**Release Date: 01 February 2026**

### Summary

CodeScan 26.0.2 is comprised of the following 10 components:

* 1 New Feature
* 3 Application Enhancements
* 1 New Rule
* 5 Rule Enhancements

Component details are listed in their corresponding sections within this document.

### New Features

**1.     Data Flow Analysis**

In our CodeScan 25.1.17 release (Jan 04, 2026), we announced that CodeScan had implanted new logic in some of our rules that detect vulnerabilities. This advanced logic provides precise visibility into where unsafe data originates and how it propagates, helping developers fix vulnerabilities at their source rather than applying superficial patches at the output stage.

In that first release, we added this advanced “source to sink” logic in 3 rules:

* Unescaped Error Message XSS {Rule ID: sf:UnescapedOutput}
* URL Parameters should be Escaped/Sanitized {Rule ID: sf:UnescapedSource}
* Avoid Calling SOQL and DML Inside Loops {Rule ID: sf:AvoidSoqlInLoops}

In this current CodeScan 26.0.2 release (Feb 01, 2026), we added this advanced “source to sink” logic to 3 additional rules:

* Avoid Untrusted/Unescaped Variables in DML Query {Rule ID: sf:SOQLInjection}
* JavaScript Reflected XSS {Rule ID: vf:CrossSiteScriptingReflected}
* Flow DML Should Not Be Called In Loops {Rule ID: sfmeta:DmlInFlowLoop}

You can find specific details about each of these 3 newly updated rules in the “Rule Enhancements” section of these release notes.

### Application Enhancements

**1.     Updated the UI for the CVSS Filter**

**Description**

We updated the CVSS filter to a slider (for the values), allowing users to select a single value (pushing both sliders to a single value) or a range of values (pushing both sliders to either end of the required scale).

Default should be 0 - 10 (sliders at each end of the scale)

We verified the CVVS UI enhancement and have validated that users are able to see the updated Slider in the UI.

* CVSS filter is displayed as a slider.
* Default range is 0–10.
* Supports both single-value and range-based selection.
* Results are filtered correctly based on selected values.

No functional or UI issues were encountered or reported during testing.

<figure><img src="../../../../.gitbook/assets/image (2381).png" alt=""><figcaption></figcaption></figure>

**2.     Added the ability to Download/Export IDE Usage Data from the IDE Usage page**

**Description**

On the IDE Usage page, a “Export CSV” feature has been added. Based on the date filter, the connection list will be downloadable as CSV.

Testing was done with 18,000 records to validate performance standards.

**Acceptance Criteria**

* On hovering over the download button, the application displays “Download the IDE usage history based on current filters.“
* On clicking the download button, download of a CSV file commences and respects the filters the user has selected.

<figure><img src="../../../../.gitbook/assets/image (2382).png" alt=""><figcaption></figcaption></figure>

**3.     Added Enhanced our logic for Queries in JavaScript to only contain fields that are used**

**Description**

By including only the necessary fields in queries, developers can optimize the performance of their LWC components. When a query includes only the required fields, the amount of data retrieved from the Salesforce database is minimized, resulting in faster query execution times and reduced network overhead.

**Hypothesis:**

By limiting the fields in the queries to only those that are required for our LWC components, we expect to observe a significant reduction in query execution times and a decrease in network overhead.

Example 1: Retrieve the name of an Account and its owner's Name via getRecord

<figure><img src="../../../../.gitbook/assets/image (2383).png" alt=""><figcaption></figcaption></figure>

**Value/Purpose:**

The main purpose of this user story is to enhance the performance of LWC components and streamline the data retrieval process from the Salesforce database. By implementing this optimization, the benefits we expect to achieve are faster query execution and improved load times for LWC components.

[Drive Consistency and Grow Developer Skills with a Developer Best Practices Checklist](https://developer.salesforce.com/blogs/2022/01/drive-consistency-and-grow-developer-skills-with-a-developer-best-practices-checklist)

**Acceptance Criteria**

Name: Avoid Querying Fields That Aren’t Used\
Key: cs-js:unused-query-field\
Description: By including only the necessary fields in queries, developers can optimize the performance of their LWC components.

Including only required fields reduces the amount of data retrieved from the Salesforce database, resulting in faster query execution times and reduced network overhead.

Type: Code Smell\
Severity: Minor\
Message: Avoid using the queries with unused fields\
Tags: performance

Validated the newly added CodeScan rule UnusedQueryField via the following scenarios:

* Verified that the rule “Avoid Querying Fields That Aren’t Used” is successfully added and visible in CodeScan with correct metadata (rule key, severity, type and tags).
* Validated rule behavior using both positive (no-violation) and negative (violation) LWC test cases.
* Confirmed that CodeScan correctly flags violations when unused fields are queried and does not report issues when all queried fields are used.

<figure><img src="../../../../.gitbook/assets/image (2384).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2385).png" alt=""><figcaption></figcaption></figure>

### New Rules

**1.     New Rule that validates the runInMode (or equivalent context property) of a Flow**

**Description**

We have created a new rule for Flow metadata that validates the runInMode (or equivalent context property of a Flow). This rule inspects whether the flow is executing in DefaultMode, SystemModeWithSharing, or SystemModeWithoutSharing. If configured to DefaultMode, the rule produces a violation as the default behavior of the rule. The rule ensures that flows explicitly check access permissions and don’t unintentionally run with improper privilege elevation. The developer should be able to override or configure the rule to allow certain modes as exceptions.

**Hypothesis:**\
We believe that enforcing stricter validation on Flow execution context will prevent developers from inadvertently exposing sensitive operations or data access when Flows run under unclear or unsafe privilege assumptions. If CodeScan alerts developers when unsafe Flow run modes are used, developers will configure the correct context mode and explicitly handle permissions, leading to fewer security vulnerabilities in customer orgs.

_Note_: The runInMode of the flow in Default Mode violations should be given for all the below mentioned flows except Screen Flows, which will include an additional parameter to reduce false positives.

<figure><img src="../../../../.gitbook/assets/image (2386).png" alt=""><figcaption></figcaption></figure>

**Value/Purpose:**

* Prevent improper access to protected Salesforce objects and records.
* Detect misconfigurations where a Flow runs unintentionally in elevated or ambiguous context.

**Rule Details**

Name: Validate Flow Run Context Mode\
Key: FlowRunContextValidation\
Description: This rule checks the execution context (runInMode) of a Salesforce Flow to ensure that it is not unintentionally configured to run with elevated privileges. Flows running in DefaultMode or SystemModeWithoutSharing can grant broad data access or excessive privileges to users who would normally not have such permissions. This rule enforces that flows explicitly use appropriate run contexts and encourages proper access validation to avoid unauthorized access to protected records or sensitive operations.\
See

* [Determining the Flow Running User and Its Execution Context](https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context) - Salesforce
* [CWE-282](https://cwe.mitre.org/data/definitions/282.html) - Improper Ownership Management
* [CWE-284](https://cwe.mitre.org/data/definitions/284.html) - Improper Access Control

Type: Vulnerability\
Severity: Major\
Message: This flow’s execution mode may grant unintended access. Use explicit access checks or adjust the run mode.\
Tags: salesforce, owasp-a1, owasp-a2

Remediation: 5 Minutes

Parameter:

Name: ignoreScreenFlows\
Description: If enabled, the rule will _ignore_ Screen flows using runInMode in DefaultMode. Default: false

We validated this newly added CodeScan rule “Validate Flow Run Context Mode (FlowRunContextValidation)” via the following scenarios:

* Verified that the rule is successfully added and visible in CodeScan with correct metadata:
  * Type: Vulnerability
  * Severity: Major
  * Parameter: ignoreScreenFlows (default = false)
* Validated rule behavior using Flow metadata:
  * Flows running in Default execution context (identified via environments=Default or equivalent) are correctly flagged with a Major vulnerability.
  * The violation message and rule key are displayed as expected.
  * The reported issue correctly points to the affected Flow metadata file.

<figure><img src="../../../../.gitbook/assets/image (2387).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2388).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

**1.     New Parameter added to rule “Outer Class Explicit Sharing” allowing configurable enforcement of the rule for abstract and virtual classes**

**{Rule ID: sf:OuterClassExplicitSharing }**

**Description**

We have updated the rule sf:OuterClassExplicitSharing to provide a configurable parameter that controls whether violations are raised for abstract and virtual outer classes.  With this new parameter, users can avoid false positives in framework or base classes while still having the option to enforce explicit sharing when required by the security standards.

**Hypothesis**:\
Introducing a configurable parameter to disable rule enforcement for abstract and virtual outer classes by default will reduce noise in scan results while preserving flexibility for teams that require strict sharing enforcement across all Apex class types.

**Value / Purpose:**

* Reduces false positives for commonly used base and framework classes
* Improves rule adoption and trust by making enforcement intentional

**Acceptance Criteria**

**Parameter Name: EnableForAbstractAndVirtual**

**Description**:\
The violation will be skipped for abstract and virtual outer classes in sf:OuterClassExplicitSharing if marked as false. Default is false.

**Default Value:**\
false

Verified the newly added parameter via the following scenarios:

BEFORE the parameter was added, the rule sf:OuterClassExplicitSharing enforced explicit sharing declarations as follows:

1. Classes declared with with sharing → No violation
2. Classes declared with inherited sharing → No violation
3. Classes without any sharing keyword → Violation raised

NOW, a new configurable parameter has been added:

**Parameter Name: EnableForAbstractAndVirtual**\
**Default Value**: false

This parameter allows to control whether the rule should enforce explicit sharing on abstract and virtual outer classes\
\
\
Current Behavior (After Fix):

<figure><img src="../../../../.gitbook/assets/unknown (19).png" alt=""><figcaption></figcaption></figure>

This behavior aligns with the intended design:

* Reduces noise and false positives by default
* Allows stricter enforcement when required by security standards

<figure><img src="../../../../.gitbook/assets/image (2389).png" alt=""><figcaption></figcaption></figure>

**Parameter set to False:**

<figure><img src="../../../../.gitbook/assets/image (2390).png" alt=""><figcaption></figcaption></figure>

**Parameter set to True:**

<figure><img src="../../../../.gitbook/assets/image (2391).png" alt=""><figcaption></figcaption></figure>

**2.     Added Data Flow Tracking for SOQL Injection Detection to rule “Avoid Untrusted/Unescaped Variables in DML Query” {Rule ID: sf:SOQLInjection}**

**Description**

Enhanced the sf:SOQLInjection rule to trace variable origins used in dynamic SOQL queries.\
For example,

String field1 = getFilter();

String field2 = 'SELECT Id FROM Account WHERE ';

Database.query(field2 + field1);

Variables like field1 should be tracked from input to query construction, identifying whether proper escaping or validation occurred before concatenation.

We also updated the issue description to show the source of untrusted input, transformations, and the exact sink (query line).

**Hypothesis:**\
If the rule details how an input variable flows into a dynamic query without proper sanitization, developers can quickly locate injection vectors and remediate them effectively.

**Value/Purpose:**\
Improves developer trust in reported SOQL injection issues by offering context-rich, data flow–backed explanations and reducing guesswork in identifying the unsafe variable.

Verified the enhancement for sf:SOQLInjection via the following scenarios:

* The rule correctly triggers for Apex code where untrusted input flows into dynamically constructed SOQL queries.
* The issue message now includes an updated Data Flow Trace, clearly showing:
* the origin/source of the untrusted input,
* intermediate assignments / concatenations, and
* the exact sink where the query is executed (Database.query).

<figure><img src="../../../../.gitbook/assets/image (2392).png" alt=""><figcaption></figcaption></figure>

**3.     Enhancement to Cross-Site Scripting (Reflected) Detection with Data Flow Tracing logic**

**{Rule ID: vf:CrossSiteScriptingReflected}**

**Description**

Implemented data flow tracking for the vf:CrossSiteScriptingReflected rule to trace how untrusted input propagates from sources like location.href, location.search, document.location, and window.location to sinks such as document.write, .innerHTML, or eval().

We also updated the issue description to display the complete source → propagation → sink path, highlighting the flow of potentially malicious data through intermediate variables and functions.

**Hypothesis:**\
If the rule can visualize how untrusted user input moves from sources to sinks through variable assignments and transformations, developers will more easily understand and remediate reflected XSS vulnerabilities.

**Value/Purpose:**\
This enhancement improves clarity and confidence in issue results, reduces false positives, and empowers developers to identify the exact vulnerable flow within Visualforce pages for faster and more accurate remediation.

Verified the enhancement logic of Cross-Site Scripting (Reflected) Detection with Data Flow Tracing via the following scenarios:

* Validated that the rule correctly detects reflected XSS vulnerabilities involving untrusted user input.
* Validated that the updated issue message now includes a Data Flow Trace that clearly indicates:
* The source of untrusted input
* Intermediate variable propagation
* The final sink where the vulnerability occurs

**4.     Implemented Data Flow Tracking Logic for rule “Flow DML in Loops”**

**{Rule ID: sfmeta:DmlInFlowLoop}**

**Description**

Enhanced the sfmeta:DmlInFlowLoop rule to include **data flow tracking** that identifies how DML operations (Create, Update, Delete Records) are executed within loop elements in Flows.\
This enhancement should trace data variables flowing from loop iterators to DML elements.

We also updated the issue description accordingly to clearly indicate the source and flow of data.

Updated Message:\
DML element UPD should not be called in loop loop\_one. Data Flow Trace -\
LOOPS (Loops loop\_one line: 15) →\
DECISION (decisions DEC line: 4) →\
RECORD UPDATES (recordUpdates UPD line: 29)

**Hypothesis:**\
If we add data flow tracking to detect DML operations triggered inside loops, developers will gain better visibility into where and how loop data is used in DML actions, helping them refactor Flows for better performance.

**Value/Purpose:**\
Improves the accuracy and clarity of Flow DML-in-loop detections, helping developers understand performance risks, prevent governor limit issues, and optimize Flow design.

Verified the enhancement of the rule **sfmeta:DmlInFlowLoop** via the following scenarios:

* Validated that the rule correctly detects DML operations (Create/Update/Delete) executed inside Flow loops.
* Validated that the rule reports a clear **Data Flow Trace** from the loop through intermediate elements (e.g., Decision) to the DML element.

<figure><img src="../../../../.gitbook/assets/image (2393).png" alt=""><figcaption></figcaption></figure>

**5.     Added New Parameters for rule “Flow DML Should Not Be Called In Loops”**

**{Rule ID: sfmeta:DmlInFlowLoop}**

**Description**

Rule is enhanced to flag DML operations inside Salesforce Flows as violations across all flow types. However, some flow types (e.g., Scheduled Flows, Record-Triggered Flows configured for specific contexts) may legitimately require DML operations and should not be treated as violations.\
To provide flexibility and prevent unnecessary noise, we have introduced a series of configurable parameters that allow admins to **enable or disable specific Flow Types** for which DML-in-Flow should **not** generate a violation.

This configuration is part of rule settings, which allows users to choose which flow types are exempt (e.g., Screen Flow, Record-Triggered Flow, Subflow, Scheduled Flow).

**Hypothesis**

If users can configure flow types to be excluded from DML-in-Flow violations, then:

* False positives will be reduced.
* Teams will have better control over enforcing governance rules based on their architecture.
* Developers will get cleaner, more relevant issue reports.

**Value / Purpose**

* Reduces unnecessary violations for legitimate flow designs.
* Provides team-level customization aligned with their Salesforce practices

**Acceptance Criteria**

**Parameter Name: IgnoreRecordTriggeredFlow**

**Description**: The violation for DML operations inside the flow will be skipped for _Record-Triggered Flows_ if marked as false. Default is false.\
**Default Value**:\
false

***

**Parameter Name: IgnoreScreenFlow**

**Description**: The violation for DML operations inside the flow will be skipped for _Screen Flows_ if marked as false. Default is false.\
**Default Value:**\
false

***

**Parameter Name: IgnoreAutolaunchedFlow**

**Description**: The violation for DML operations inside the flow will be skipped for _Autolaunched Flows_ if marked as false. Default is false.\
**Default Value**:\
false

***

**Parameter Name: IgnoreScheduleTriggered Flow**

**Description**: The violation for DML operations inside the flow will be skipped for _Schedule Triggered Flows_ if marked as false. Default is false.\
**Default Value**:\
false

***

**Parameter Name: IgnorePlatformEventTriggeredFlow**

**Description**: The violation for DML operations inside the flow will be skipped for _Platform Event–Triggered Flows_ if marked as false. Default is false.\
**Default Value**:\
false

Verified the new, configurable **Ignore parameters** for the **sfmeta:DmlInFlowLoop** rule, allowing selective exclusion of specific Salesforce Flow types from DML-in-loop violations via the following scenarios:

* All the parameters that are mentioned are added and are default to **false** supporting the correct behavior.
* The rule was tested using Flow metadata containing DML operations executed inside loops across different Flow types
* When an **Ignore** parameter is set to **false** (default), the rule correctly reports DML-in-loop violations.
* When the corresponding **Ignore** parameter is set to **true**, violations are correctly skipped for that Flow type.
* Flow types are correctly identified by the rule.
* Violations are conditional based on rule configuration.

<figure><img src="../../../../.gitbook/assets/image (2394).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Application Enhancements

**1.     Include Issue Comments in CSV Issues Export**

**Description**

When exporting Issues to CSV, the file should include an additional column that captures all comments associated with each issue. Each entry in this column must list every comment along with the commenter’s user name, the date/time the comment was made, and the comment text, formatted in a readable, consistent manner.

**Hypothesis**\
If issue comments are included in the CSV export with clear attribution & timestamps, then users will be able to review, audit, and share issue context offline without needing to revisit the application UI.

_The image below illustrates the new format for comments added into CSV exports:_

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

&#x20;
