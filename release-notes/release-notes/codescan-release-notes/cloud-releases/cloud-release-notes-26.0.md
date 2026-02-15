# Cloud Release Notes 26.0

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive CodeScan updates!" %}

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Application Enhancements

**1.     Include Issue Comments in CSV Issues Export**

**Description**

When exporting Issues to CSV, the file should include an additional column that captures all comments associated with each issue. Each entry in this column must list every comment along with the commenter’s user name, the date/time the comment was made, and the comment text, formatted in a readable, consistent manner.

**Hypothesis**\
If issue comments are included in the CSV export with clear attribution & timestamps, then users will be able to review, audit, and share issue context offline without needing to revisit the application UI.

_The image below illustrates the new format for comments added into CSV exports:_

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

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
