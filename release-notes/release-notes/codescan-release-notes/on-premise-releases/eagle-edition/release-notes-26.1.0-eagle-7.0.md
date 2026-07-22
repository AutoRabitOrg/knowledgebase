# Release Notes 26.1.0 Eagle 7.0

**Release Date: 1 June 2026**

### Summary

CodeScan Self-Hosted version 26.1.0 (Eagle v7) is comprised of the following 24 components:

* 1 New Feature
* 5 New Rules
* 12 Rule Enhancements
* 6 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

#### 1. Data Flow Analysis

CodeScan has implemented new logic in some of the rules that detect vulnerabilities. This advanced logic provides precise visibility into where unsafe data originates and how it propagates, helping developers fix vulnerabilities at their source rather than applying superficial patches at the output stage.

In this release, we have added an advanced “source to sink” logic to the following rules:

* Unescaped Error Message XSS {Rule ID: sf:UnescapedOutput}
* URL Parameters should be Escaped/Sanitized {Rule ID: sf:UnescapedSource}
* Avoid Calling SOQL and DML Inside Loops {Rule ID: sf:AvoidSoqlInLoops}
* Avoid Untrusted/Unescaped Variables in DML Query {Rule ID: sf:SOQLInjection}
* JavaScript Reflected XSS {Rule ID: vf:CrossSiteScriptingReflected}
* Flow DML Should Not Be Called In Loops {Rule ID: sfmeta:DmlInFlowLoop}

Specific details about the rules updates are available under the “Rule Enhancements” section of these Release Notes.

### New Rules

#### 1. Avoid Querying Fields That Aren’t Used Rule

**Rule details**

Name: Avoid Querying Fields That Aren’t Used

Key: _cs-js:unused-query-field_

Description:

By including only the necessary fields in queries, developers can optimize the performance of their LWC components. When a query includes only the required fields, the amount of data retrieved from the Salesforce database is minimized, resulting in faster query execution times and reduced network overhead.

**Hypothesis:**

By limiting the fields in the queries to only those that are required for our LWC components, we expect to observe a significant reduction in query execution times and a decrease in network overhead.

**Example**

Retrieve the name of an Account and its owner's Name via getRecord:

<img src="../../../../../.gitbook/assets/unknown (65).png" alt="" height="312" width="513">

This way, we are enhancing the performance of LWC components and streamlining the data retrieval process from the Salesforce database.

#### 2. Avoid Querying Fields That Aren’t Used Rule

Created a new rule for Flow metadata that validates the runInMode (or equivalent context property of a Flow). This rule inspects whether the flow is executing in DefaultMode, SystemModeWithSharing, or SystemModeWithoutSharing. If configured to DefaultMode, the rule produces a violation as the default behavior of the rule. The rule ensures that flows explicitly check access permissions and don’t unintentionally run with improper privilege elevation. The developer should be able to override or configure the rule to allow certain modes as exceptions.

**Hypothesis:**

We believe that enforcing stricter validation on Flow execution context will prevent developers from inadvertently exposing sensitive operations or data access when Flows run under unclear or unsafe privilege assumptions. If CodeScan alerts developers when unsafe Flow run modes are used, developers will configure the correct context mode and explicitly handle permissions, leading to fewer security vulnerabilities in customer orgs.

<img src="../../../../../.gitbook/assets/unknown (67).png" alt="" height="323" width="574">

**Value/Purpose:**

Prevent improper access to protected Salesforce objects and records.

Detect misconfigurations where a Flow runs unintentionally in elevated or ambiguous context.

**Rule Details**

Name: Validate Flow Run Context Mode

Key: _FlowRunContextValidation_

Description:

This rule checks the execution context (runInMode) of a Salesforce Flow to ensure that it is not unintentionally configured to run with elevated privileges. Flows running in DefaultMode or SystemModeWithoutSharing can grant broad data access or excessive privileges to users that would normally not have such permissions. This rule enforces that flows explicitly use appropriate run contexts and encourages proper access validation to avoid unauthorized access to protected records or sensitive operations.

CWE-282 - Improper Ownership Management

CWE-284 - Improper Access Control

Type: Vulnerability

Severity: Major

Message:

_This flow’s execution mode may grant unintended access. Use explicit access checks or adjust the run mode._

Parameter:

Name: ignoreScreenFlows

Description:

If enabled, the rule will ignore Screen flows using runInMode in DefaultMode (Default: false)

#### 3. Locale Formats in API Versions pre-v45.0 Rule

This new rule finds locale methods in Apex classes with API versions below v45.0. Failure to upgrade to API v45.0 or above could result in date and time formatting issues, affecting user experience and functionality.

Please also refer to the following documentation on Salesforce Help:

[JDK Locale Format Retirement and the Enable ICU Locale Formats Salesforce Release Update](https://help.salesforce.com/s/articleView?id=000380618\&type=1) –\
[Use Locale-Neutral Methods in Code](https://help.salesforce.com/s/articleView?id=xcloud.admin_locales_code_methods.htm\&type=5)

**Rule Details**

Name: Locale Formats in API Versions pre-v45.0

Key: _sf:LocaleInOldApi_

Issue Type: Bug

Severity: Major

Message:

_Avoid Using JDK Locale Formats_

The rule sf:LocaleInOldApi was validated for the following methods:

* Date.format
* Datetime.format
* Date.parse
* Datetime.parse
* Date.toStartOfWeek

The rule behavior was validated against the defined conditions.

Classes with API versions prior to v45.0 and using locale-dependent methods are considered for detection, while classes with API v45.0+ are treated as compliant.

#### 4. Avoid Plain Text Values in External Credential Parameters Rule

Added a new Salesforce Metadata security rule to detect plain text values in External Credential parameter values.

**Rule Details**

* Rule key: _sfmeta:ExternalCredentialPlainTextValue_
* Type: Vulnerability
* Default Severity: Critical
* CWE: CWE-798
* Remediation effort: 5 minutes

**Behavior**

The rule raises a violation when an External Credential metadata file contains a static plain text value in a parameterValue field.

The rule does not raise a violation when:

* parameterValue uses a dynamic merge field reference.
* The sibling parameterName is Content-Type.
* The file does not contain any parameterValue fields.

**Message**

_Plain text value detected in parameterValue field. Use a dynamic merge field reference instead to avoid exposing sensitive credentials._

**Outcome**

Helps prevent sensitive credentials such as API keys, client IDs, and authentication tokens from being exposed in source control.

#### **5. Avoid Using Unfiled Public Folders Rule**

**Rule ID:** _sf-meta:AvoidUnfiledPublic_

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

Verified the newly added rule _sf-meta:AvoidUnfiledPublic_ **(Avoid Using Unfiled Public Folders**) via the following scenarios:

* The rule description is visible in CodeScan and correctly explains the security and governance risks associated with storing Salesforce metadata in unfiled public folders.
* The rule is working as expected and consistently raises violations whenever Salesforce metadata is stored under a file path containing /unfiled$public/.
* This behavior is expected, as metadata placed in unfiled public folders can lead to unrestricted access, lack of proper organization, and potential compliance concerns.
* No issues were observed with the rule configuration or behavior.

### Rule Enhancements

#### 1. Updated Unescaped Error Message XSS Rule

Reimplemented the _sf:UnescapedOutput_ rule to include data flow tracing for variables passed to addError() (e.g., addError(html, false)).

This determines whether variables originate from unsanitized sources by tracing them across methods and assignments. Use UrlSanitizationRule logic as reference for tracking unescaped values.

We have also updated the issue description to include the exact source variable and its data path before being rendered.

**Hypothesis:**

If we trace the data flow from unescaped or unsanitized sources to the point of output in addError, developers can clearly see how unsafe data reaches the output layer, making the issue more actionable.

**Value/Purpose:**

Provides precise visibility into where unsafe data originates and how it propagates, helping developers fix vulnerabilities at their source rather than applying superficial patches at the output stage.

<img src="../../../../../.gitbook/assets/unknown (69).png" alt="" height="272" width="442">

Verified that the data flow tracking logic for unescaped output in Apex is working, and the updated description has been applied.

#### 2. Updated URL Parameters should be Escaped/Sanitized Rule

Extended the _sf:UnescapedSource_ rule to track the flow of URL parameters retrieved from ApexPages.currentPage().getParameters().get(...). The data flow analysis will identify whether these variables are properly sanitized or escaped before reaching any sensitive sink or being rendered.

We have also updated issue descriptions to show both the untrusted source and its usage path.

**Hypothesis:**

If the system highlights the full journey of parameters from getParameters() to their usage points, developers will better understand how unescaped data can lead to vulnerabilities and where sanitization is missing.

**Value/Purpose:**

Enables developers to pinpoint missing sanitization in their Apex controllers by visualizing data flow paths, thus improving the security posture of Visualforce and Lightning pages.

#### 3. Updated the Avoid Calling SOQL and DML Inside Loops Rule

Refined the issue description for _sf:AvoidSoqlInLoops_ to clearly identify the loop structure and the query being executed inside it.

**Hypothesis:**

Providing contextual information about where and how SOQL queries are invoked within loops will improve developer understanding and reduce rework in optimizing code performance.

**Value/Purpose:**

Enhances readability and educational value of performance warnings by showing contextual flow, helping developers refactor code more efficiently.

#### 4. Added Data Flow Tracking for SOQL Injection Detection to Avoid Untrusted/Unescaped Variables in DML Query Rule

Enhanced the _sf:SOQLInjection_ rule to trace variable origins used in dynamic SOQL queries.

For example,

String field1 = getFilter();

String field2 = 'SELECT Id FROM Account WHERE ';

Database.query(field2 + field1);

Variables like field1 should be tracked from input to query construction, identifying whether proper escaping or validation occurred before concatenation.

We also updated the issue description to show the source of untrusted input, transformations, and the exact sink.

**Hypothesis:**

If the rule details how an input variable flows into a dynamic query without proper sanitization, developers can quickly locate injection vectors and remediate them effectively.

**Value/Purpose:**

Improves developer trust in reported SOQL injection issues by offering context-rich, data flow–backed explanations and reducing guesswork in identifying the unsafe variable.Bottom of Form

Verified the enhancement for sf:SOQLInjection via the following scenarios:

* The rule correctly triggers for Apex code where untrusted input flows into dynamically constructed SOQL queries.
* The issue message now includes an updated Data Flow Trace, clearly showing the origin/source of the untrusted input, and intermediate assignments / concatenations, and the exact sink where the query is executed.

#### 5. Enhancement to Cross-Site Scripting (Reflected) Detection with Data Flow Tracing logic

Implemented data flow tracking for the _vf:CrossSiteScriptingReflected_ rule to trace how untrusted input propagates from sources like location.href, location.search, document.location, and window.location to sinks such as document.write, .innerHTML, or eval().

We also updated the issue description to display the complete source → propagation → sink path, highlighting the flow of potentially malicious data through intermediate variables and functions.

**Hypothesis:**

If the rule can visualize how untrusted user input moves from sources to sinks through variable assignments and transformations, developers will more easily understand and remediate reflected XSS vulnerabilities.

**Value/Purpose:**

This enhancement improves clarity and confidence in issue results, reduces false positives, and empowers developers to identify the exact vulnerable flow within Visualforce pages for faster and more accurate remediation.

Verified the enhancement logic of Cross-Site Scripting (Reflected) Detection with Data Flow Tracing via the following scenarios:

1. Validated that the rule correctly detects reflected XSS vulnerabilities involving untrusted user input.
2. Validated that the updated issue message now includes a Data Flow Trace that clearly indicates:

* The source of untrusted input
* Intermediate variable propagation
* The final sink where the vulnerability occurs

#### 6. Data Flow Tracking Logic added to Flow DML in Loops Rule

Enhanced the _sfmeta:DmlInFlowLoop_ rule to include data flow tracking that identifies how DML operations (Create, Update, Delete Records) are executed within loop elements in Flows.

This enhancement should trace data variables flowing from loop iterators to DML elements.

We also updated the issue description accordingly to clearly indicate the source and flow of data.

**Updated message example:**

_DML element UPD should not be called in loop loop\_one. Data Flow Trace -_

_LOOPS (Loops loop\_one line: 15) →_

_DECISION (decisions DEC line: 4) →_

_RECORD UPDATES (recordUpdates UPD line: 29)_

**Hypothesis:**

If we add data flow tracking to detect DML operations triggered inside loops, developers will gain better visibility into where and how loop data is used in DML actions, helping them refactor Flows for better performance.

**Value/Purpose:**

Improves the accuracy and clarity of Flow DML-in-loop detections, helping developers understand performance risks, prevent governor limit issues, and optimize Flow design.

Verified the enhancement of the rule sfmeta:DmlInFlowLoop via the following scenarios:

* Validated that the rule correctly detects DML operations (Create/Update/Delete) executed inside Flow loops.
* Validated that the rule reports a clear Data Flow Trace from the loop through intermediate elements (e.g., Decision) to the DML element.

#### 7. Added New Parameters to Flow DML Should Not Be Called In Loops Rule

Enhanced lag DML operations inside Salesforce Flows as violations across all flow types. However, some flow types (e.g., Scheduled Flows, Record-Triggered Flows configured for specific contexts) may legitimately require DML operations and should not be treated as violations.

To provide flexibility and prevent unnecessary noise, we have introduced a series of configurable parameters for _sfmeta:DmlInFlowLoop_ rule that allow admins to enable or disable specific Flow Types for which DML-in-Flow should not generate a violation.

This configuration is part of rule settings, which allows users to choose which flow types are exempt (e.g., Screen Flow, Record-Triggered Flow, Subflow, Scheduled Flow).

**Hypothesis:**

If users can configure flow types to be excluded from DML-in-Flow violations, then:

* False positives will be reduced.
* Teams will have better control over enforcing governance rules based on their architecture.
* Developers will get cleaner, more relevant issue reports.

**Value / Purpose:**

* Reduces unnecessary violations for legitimate flow designs.
* Provides team-level customization aligned with their Salesforce practices

**Parameter Name:** IgnoreRecordTriggeredFlow

**Description:**

The violation for DML operations inside the flow will be skipped for Record-Triggered Flows if marked as false.

**Default Value:** false

**Parameter Name:** IgnoreScreenFlow

**Description:**

The violation for DML operations inside the flow will be skipped for Screen Flows if marked as false.

**Default Value:** false

**Parameter Name:** IgnoreAutolaunchedFlow

**Description:**

The violation for DML operations inside the flow will be skipped for Autolaunched Flows if marked as false.

**Default Value:** false

**Parameter Name:** IgnoreScheduleTriggered Flow

**Description:**

The violation for DML operations inside the flow will be skipped for Schedule Triggered Flows if marked as false.

**Default Value:** false

**Parameter Name:** IgnorePlatformEventTriggeredFlow

**Description:**

The violation for DML operations inside the flow will be skipped for Platform Event–Triggered Flows if marked as false.

**Default Value:** false

Verified the new, configurable Ignore parameters for the sfmeta:DmlInFlowLoop rule, allowing selective exclusion of specific Salesforce Flow types from DML-in-loop violations via the following scenarios:

All the parameters that are mentioned are added and are default to false supporting the correct behavior.

#### 8. New Parameter added to rule Outer Class Explicit Sharing Rule

We have updated the rule _sf:OuterClassExplicitSharing_ to provide a configurable parameter that controls whether violations are raised for abstract and virtual outer classes. With this new parameter, users can avoid false positives in framework or base classes while still having the option to enforce explicit sharing when required by the security standards.

**Hypothesis:**

Introducing a configurable parameter to disable rule enforcement for abstract and virtual outer classes by default will reduce noise in scan results while preserving flexibility for teams that require strict sharing enforcement across all Apex class types.

**Value / Purpose:**

* Reduces false positives for commonly used base and framework classes
* Improves rule adoption and trust by making enforcement intentional

**Parameter Name:** EnableForAbstractAndVirtual

**Description:**

The violation will be skipped for abstract and virtual outer classes in sf:OuterClassExplicitSharing if marked as false. Default is false.

**Default Value:** false

Verified the newly added parameter via the following scenarios:

BEFORE the parameter was added, the rule sf:OuterClassExplicitSharing enforced explicit sharing declarations as follows:

* Classes declared with with sharing → No violation
* Classes declared with inherited sharing → No violation
* Classes without any sharing keyword → Violation raised

A new configurable parameter EnableForAbstractAndVirtual has been added, this parameter allows to control whether the rule should enforce explicit sharing on abstract and virtual outer classes

Current Behavior:

<img src="../../../../../.gitbook/assets/unknown (71).png" alt="" height="210" width="560">

This behavior aligns with the intended design:

* Reduces noise and false positives by default
* Allows stricter enforcement when required by security standards

#### 9. Improved Field Level Security Rule where User mode subqueries generated false positives

We have identified false positives and have concluded that there is an edge case that was not accounted for in _Sf:fieldlevelsecurity_ rule. Specifically, when the User mode is defined via AccessLevel in the return statement, the rule flagged it as a violation, resulting in false positives.

This behavior has now been fully remediated with this release.

Verified the Sf:fieldlevelsecurity – USER\_MODE subquery false positive via several scenarios and confirm that the rule now correctly skips FLS violations when AccessLevel.USER\_MODE is provided via direct assignment, including:

* Inline usage in Database.getQueryLocator
* Simple variable assignment (AccessLevel mode = AccessLevel.USER\_MODE)

#### 10. Added Data Flow Tracking for SOQL Injection Detection to Avoid Untrusted/Unescaped Variables in DML Query Rule

We verified the rule expression, and confirmed that we did not support the naming pattern PR\_TestClassName in _Sf:testclassnaming_ rule.

Instead, the rule supported only the following naming convention:

* TestClassName - prefix
* ClassNameTest - suffix
* ClassName\_Test - Underscore

As such, we enhanced this rule by adding a new parameter to Sf:testclassnaming to define allowed naming conventions.

The parameter is called **allowedPatterns**.

**Description:**

A comma-separated string of regular expressions matching allowed naming conventions for test classes.

The default of this parameter is to use the preexisting current functionality of the rule.

Further, we decided that the parameter field should never be empty.

The value of this parameter is providing customers the flexibility to add any patterns that they allow as acceptable naming conventions without restriction to our logic.

Validated the enhancement for the Sf:testclassnaming rule by verifying the following scenarios:

* Able to see the configurable parameter allowedPatterns (comma-separated regex list) to support custom naming conventions.
* Default behavior remains unchanged.
* Validation ensures parameter cannot be empty.
* Particular Reg expressions given in the allowed parameters skips the violations cccordingly.

#### 11. Enhanced Parser for Methods Named “void”

Earlier, our parser wouldn’t process Apex methods named void.

Current behavior:

* Ensures accurate parsing of valid Apex code
* Improves analysis reliability

The parser enhancement to support Apex methods named void has been thoroughly validated by QA across multiple scenarios on Preview instance.

Positive Validation Scenarios:

The following valid Apex patterns were tested and are now parsed correctly:

* Basic Cases

public void void() {}

Method with body statements

* Access Modifiers

private void void() {}

protected void void() {}

global void void() {}

* Modifiers & Combinations

public static void void() {}

public final static void void() {}

* Parameterized Methods

public void void(String name, Integer count) {}

* Annotations

@AuraEnabled public static void void() {}

* Exception Handling

Method containing throw statements

* Constructor + Method Coexistence

Class containing both constructor and method named void

* Multiple Methods

Classes with multiple methods including one named void

* Method Overloading

Multiple overloaded methods named void with different parameters

* Nested Structures

Method inside inner classes

* Test Classes

@IsTest classes with method named void

* Interface & Implementation Context

Class implementing interface along with method named void

* Formatting Variations

Extra spacing in declaration

Multiline method signatures

Inline and line comments within method declaration

Negative Validation

The following invalid syntaxes were tested and correctly rejected:

* Missing method name\
  public void () {} → Parse error
* Duplicate return type\
  public void void void() {} → Parse error
* Missing parentheses\
  public void void {} → Parse error
* Invalid keyword as method name\
  public void class() {} → Parse error

These failures are expected and confirm that parser strictness is preserved.

Conclusion

* Parser now correctly supports void as a valid method name in Apex
* All valid usage patterns are successfully parsed across different contexts
* Invalid syntax continues to be rejected as expected
* No regressions observed in parsing behavior

#### 12. Enhanced AvoidDMLInLoops Rule with Interprocedural Analysis

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

### Fixes

#### 1. Fixed issue with data flow analysis logic in Avoid Untrusted/Unescaped Variables in DML Query Rule

We identified an issue in CodeScan where the Data Flow Trace for a SOQL injection rule where the trace repeatedly shows the same assignment instead of a clean, non-duplicated trace.

The image displays a software project dashboard with a highlighted vulnerability: a potential SQL injection issue in the 'ProductController.getProducts' method.

We determined the root cause of the issue and updated the rule logic accordingly. With this fix, this issue is now fully remediated.

Verified relevant scenarios and rule is now working as expected.

#### 2. SOQL Injection Rules Improvements

Fix addresses a few scenarios described below.

_Scenario 1:_ Sanitized parameter still flagged

When a variable comes from a method parameter, the rule sometimes reports SOQL Injection even if the variable is sanitized or overwritten later.

This happens because the rule uses DataFlowNode, which tracks where the variable originally came from.

DataFlowNode is shared by multiple rules (SOQL Injection, Open Redirect, Useless Assignment, etc.).

Because of this, we can’t easily change this behavior for one rule without impacting others.

_Scenario 2:_ “At least once” assignment not detected

DataFlowNode can detect whether an assignment is inside a condition.

However, in some cases assignments happen inside loops, where the variable is still assigned at least once.

DataFlowNode wasn’t originally designed to reliably confirm this loop behavior.

Because of this limitation, these cases could not be properly handled and would likely result in producing false positives.

We remediated these issues with this fix, greatly improving the value of the data flow logic in tracing the vulnerability from sink to source.

#### 3. Fixed issue with Avoid Cleartext Transmission of Sensitive Information Rule

Previously, the rule _InsecureEndpointRule_ was throwing a ClassCastException due to an invalid cast from ClassNameDeclaration to VariableNameDeclaration when analyzing endpoint expressions involving enum/class references (e.g., MODE.ERASE).

After the fix:

Proper type checking has been implemented before casting symbol table declarations.

The rule now safely handles enum and class references without making incorrect assumptions.

No runtime exceptions are observed during analysis.

**Result:**

* No ClassCastException observed.
* Rule executes as expected across all tested scenarios.

#### 4. Fixed issue with Resource Injection Rule

Several customers were reporting a StackOverflowError for the _sf:ResourceInjection_ rule. Based on the analysis of logs and review of implementation, we uncovered an infinite recursive call in the isSanitized method in the UrlSanitization.java and determined that this is the reason for the StackOverflowError.

Previously, the analysis stayed in Running state and logs showed a StackOverflowError for the mutual-recursion flow (methodA -> methodB -> methodA) with no exit condition, ending in req.setEndpoint(url) with the Rule Resource Injection. After the fix, the same code analyzes successfully, completes normally, and no StackOverflowError is observed in logs.

Validation after fix:

* Ran analysis on CodeScan
* Analysis completed successfully
* Analysis no longer remained in Running state
* StackOverflowError was no longer seen in logs

As such, we are reporting that this issue has been fully remediated.

#### 5. Fixed issue with Unescaped Error Message XSS Rule

Earlier, the Unescaped Output Rule was able to trace data flow through methods but not through assignment chains effectively. Due to missing/inefficient assignment data flow handling, the rule repeatedly re-entered isSanitized while resolving sanitization status for variables passed through assignments. This resulted in deep recursive calls and ultimately a StackOverflowError, instead of reporting a violation

**Validation**

* Rule evaluation now terminates correctly without recursion overflow
* isSanitized now handles edge cases without re-entering indefinitely

As such, the issue has been successfully remediated. The rule now handles deep assignment chains correctly and avoids infinite recursion in isSanitized, without causing a StackOverflowError.

#### 6. Resolved Stack Overflow Issue in Field Level Security Rule Analysis

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

* Improves the stability and reliability of the Apex security analysis.
* Prevents analysis failures caused by recursive execution paths.
* Reduces the risk of stalled or incomplete project analysis workflows.
