# Release Notes 26.1.0 Eagle 7.0

**Release Date: 1 June 2026**

### Summary

CodeScan Self-Hosted version 26.1.0 (Eagle v7) is comprised of the following 23 components:

* 1 New Feature
* 5 New Rules
* 12 Rule Enhancements
* 6 Fixes

Component details are listed in their corresponding sections within this document.

### New Features&#x20;

#### 1. Data Flow Analysis&#x20;

CodeScan has implemented new logic in some of the rules that detect vulnerabilities.  This advanced logic provides precise visibility into where unsafe data originates and how it propagates, helping developers fix vulnerabilities at their source rather than applying superficial patches at the output stage. &#x20;

In this release, we have added an advanced “source to sink” logic to the following rules: &#x20;

* Unescaped Error Message XSS {Rule ID: sf:UnescapedOutput} &#x20;
* URL Parameters should be Escaped/Sanitized {Rule ID: sf:UnescapedSource} &#x20;
* Avoid Calling SOQL and DML Inside Loops {Rule ID: sf:AvoidSoqlInLoops}&#x20;
* Avoid Untrusted/Unescaped Variables in DML Query {Rule ID: sf:SOQLInjection} &#x20;
* JavaScript Reflected XSS {Rule ID: vf:CrossSiteScriptingReflected} &#x20;
* Flow DML Should Not Be Called In Loops {Rule ID: sfmeta:DmlInFlowLoop}&#x20;

Specific details about the rules updates are available under the “Rule Enhancements” section of these Release Notes.

### New Rules&#x20;

#### 1. Avoid Querying Fields That Aren’t Used Rule &#x20;

**Rule details**&#x20;

Name: Avoid Querying Fields That Aren’t Used&#x20;

Key: _cs-js:unused-query-field_&#x20;

Description: &#x20;

By including only the necessary fields in queries, developers can optimize the performance of their LWC components. When a query includes only the required fields, the amount of data retrieved from the Salesforce database is minimized, resulting in faster query execution times and reduced network overhead. &#x20;

**Hypothesis:** &#x20;

By limiting the fields in the queries to only those that are required for our LWC components, we expect to observe a significant reduction in query execution times and a decrease in network overhead. &#x20;

**Example**

Retrieve the name of an Account and its owner's Name via getRecord:&#x20;

<img src="../../../../../.gitbook/assets/unknown (73).png" alt="" height="312" width="513">

This way, we are enhancing the performance of LWC components and streamlining the data retrieval process from the Salesforce database.&#x20;

#### 2. Avoid Querying Fields That Aren’t Used Rule&#x20;

Created a new rule for Flow metadata that validates the runInMode (or equivalent context property of a Flow). This rule inspects whether the flow is executing in DefaultMode, SystemModeWithSharing, or SystemModeWithoutSharing. If configured to DefaultMode, the rule produces a violation as the default behavior of the rule. The rule ensures that flows explicitly check access permissions and don’t unintentionally run with improper privilege elevation. The developer should be able to override or configure the rule to allow certain modes as exceptions. &#x20;

**Hypothesis:**&#x20;

We believe that enforcing stricter validation on Flow execution context will prevent developers from inadvertently exposing sensitive operations or data access when Flows run under unclear or unsafe privilege assumptions. If CodeScan alerts developers when unsafe Flow run modes are used, developers will configure the correct context mode and explicitly handle permissions, leading to fewer security vulnerabilities in customer orgs. &#x20;

<img src="../../../../../.gitbook/assets/unknown (74).png" alt="" height="323" width="574">

**Value/Purpose:** &#x20;

Prevent improper access to protected Salesforce objects and records. &#x20;

Detect misconfigurations where a Flow runs unintentionally in elevated or ambiguous context. &#x20;

**Rule Details**&#x20;

Name: Validate Flow Run Context Mode &#x20;

Key: _FlowRunContextValidation_ &#x20;

Description: &#x20;

This rule checks the execution context (runInMode) of a Salesforce Flow to ensure that it is not unintentionally configured to run with elevated privileges. Flows running in DefaultMode or SystemModeWithoutSharing can grant broad data access or excessive privileges to users that would normally not have such permissions. This rule enforces that flows explicitly use appropriate run contexts and encourages proper access validation to avoid unauthorized access to protected records or sensitive operations. &#x20;

CWE-282 - Improper Ownership Management &#x20;

CWE-284 - Improper Access Control &#x20;

Type: Vulnerability &#x20;

Severity: Major &#x20;

Message: &#x20;

_This flow’s execution mode may grant unintended access. Use explicit access checks or adjust the run mode._ &#x20;

Parameter: &#x20;

Name: ignoreScreenFlows &#x20;

Description: &#x20;

If enabled, the rule will ignore Screen flows using runInMode in DefaultMode (Default: false)&#x20;

#### 3. Locale Formats in API Versions pre-v45.0 Rule&#x20;

This new rule finds locale methods in Apex classes with API versions below v45.0.  Failure to upgrade to API v45.0 or above could result in date and time formatting issues, affecting user experience and functionality. &#x20;

Please also refer to the following documentation on Salesforce Help: &#x20;

[JDK Locale Format Retirement and the Enable ICU Locale Formats Salesforce Release Update](https://help.salesforce.com/s/articleView?id=000380618\&type=1) –  \
[Use Locale-Neutral Methods in Code](https://help.salesforce.com/s/articleView?id=xcloud.admin_locales_code_methods.htm\&type=5)&#x20;

**Rule Details**&#x20;

Name: Locale Formats in API Versions pre-v45.0&#x20;

Key: _sf:LocaleInOldApi_&#x20;

Issue Type: Bug &#x20;

Severity: Major &#x20;

Message: &#x20;

_Avoid Using JDK Locale Formats_&#x20;

The rule sf:LocaleInOldApi was validated for the following methods: &#x20;

* Date.format &#x20;
* Datetime.format &#x20;
* Date.parse &#x20;
* Datetime.parse &#x20;
* Date.toStartOfWeek  &#x20;

The rule behavior was validated against the defined conditions. &#x20;

Classes with API versions prior to v45.0 and using locale-dependent methods are considered for detection, while classes with API v45.0+ are treated as compliant.&#x20;

#### 4. Avoid Plain Text Values in External Credential Parameters Rule&#x20;

Added a new Salesforce Metadata security rule to detect plain text values in External Credential parameter values.&#x20;

**Rule Details**&#x20;

* Rule key: _sfmeta:ExternalCredentialPlainTextValue_ &#x20;
* Type: Vulnerability &#x20;
* Default Severity: Critical &#x20;
* CWE: CWE-798 &#x20;
* Remediation effort: 5 minutes &#x20;

**Behavior**&#x20;

The rule raises a violation when an External Credential metadata file contains a static plain text value in a parameterValue field.&#x20;

The rule does not raise a violation when:&#x20;

* parameterValue uses a dynamic merge field reference. &#x20;
* The sibling parameterName is Content-Type. &#x20;
* The file does not contain any parameterValue fields. &#x20;

**Message**&#x20;

_Plain text value detected in parameterValue field. Use a dynamic merge field reference instead to avoid exposing sensitive credentials._&#x20;

**Outcome**&#x20;

Helps prevent sensitive credentials such as API keys, client IDs, and authentication tokens from being exposed in source control.&#x20;

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

### Rule Enhancements&#x20;

#### 1. Updated Unescaped Error Message XSS Rule&#x20;

Reimplemented the _sf:UnescapedOutput_ rule to include data flow tracing for variables passed to addError() (e.g., addError(html, false)). &#x20;

This determines whether variables originate from unsanitized sources by tracing them across methods and assignments. Use UrlSanitizationRule logic as reference for tracking unescaped values. &#x20;

We have also updated the issue description to include the exact source variable and its data path before being rendered. &#x20;

**Hypothesis:** &#x20;

If we trace the data flow from unescaped or unsanitized sources to the point of output in addError, developers can clearly see how unsafe data reaches the output layer, making the issue more actionable. &#x20;

**Value/Purpose:**&#x20;

Provides precise visibility into where unsafe data originates and how it propagates, helping developers fix vulnerabilities at their source rather than applying superficial patches at the output stage.&#x20;

<img src="../../../../../.gitbook/assets/unknown (75).png" alt="" height="272" width="442">

Verified that the data flow tracking logic for unescaped output in Apex is working, and the updated description has been applied.&#x20;

#### 2. Updated URL Parameters should be Escaped/Sanitized Rule&#x20;

Extended the _sf:UnescapedSource_ rule to track the flow of URL parameters retrieved from ApexPages.currentPage().getParameters().get(...). The data flow analysis will identify whether these variables are properly sanitized or escaped before reaching any sensitive sink or being rendered. &#x20;

We have also updated issue descriptions to show both the untrusted source and its usage path.&#x20;

**Hypothesis:** &#x20;

If the system highlights the full journey of parameters from getParameters() to their usage points, developers will better understand how unescaped data can lead to vulnerabilities and where sanitization is missing. &#x20;

**Value/Purpose:**&#x20;

Enables developers to pinpoint missing sanitization in their Apex controllers by visualizing data flow paths, thus improving the security posture of Visualforce and Lightning pages.&#x20;

#### 3. Updated the Avoid Calling SOQL and DML Inside Loops Rule&#x20;

Refined the issue description for _sf:AvoidSoqlInLoops_ to clearly identify the loop structure and the query being executed inside it. &#x20;

**Hypothesis:** &#x20;

Providing contextual information about where and how SOQL queries are invoked within loops will improve developer understanding and reduce rework in optimizing code performance. &#x20;

**Value/Purpose:**&#x20;

Enhances readability and educational value of performance warnings by showing contextual flow, helping developers refactor code more efficiently.&#x20;

#### 4. Added Data Flow Tracking for SOQL Injection Detection to Avoid Untrusted/Unescaped Variables in DML Query Rule&#x20;

Enhanced the _sf:SOQLInjection_ rule to trace variable origins used in dynamic SOQL queries. &#x20;

For example,  &#x20;

String field1 = getFilter();  &#x20;

String field2 = 'SELECT Id FROM Account WHERE ';  &#x20;

Database.query(field2 + field1);  &#x20;

Variables like field1 should be tracked from input to query construction, identifying whether proper escaping or validation occurred before concatenation. &#x20;

We also updated the issue description to show the source of untrusted input, transformations, and the exact sink. &#x20;

**Hypothesis:** &#x20;

If the rule details how an input variable flows into a dynamic query without proper sanitization, developers can quickly locate injection vectors and remediate them effectively. &#x20;

**Value/Purpose:**&#x20;

Improves developer trust in reported SOQL injection issues by offering context-rich, data flow–backed explanations and reducing guesswork in identifying the unsafe variable.Bottom of Form &#x20;

Verified the enhancement for sf:SOQLInjection via the following scenarios: &#x20;

* The rule correctly triggers for Apex code where untrusted input flows into dynamically constructed SOQL queries. &#x20;
* The issue message now includes an updated Data Flow Trace, clearly showing the origin/source of the untrusted input, and intermediate assignments / concatenations, and the exact sink where the query is executed.&#x20;

#### 5. Enhancement to Cross-Site Scripting (Reflected) Detection with Data Flow Tracing logic&#x20;

Implemented data flow tracking for the _vf:CrossSiteScriptingReflected_ rule to trace how untrusted input propagates from sources like location.href, location.search, document.location, and window.location to sinks such as document.write, .innerHTML, or eval(). &#x20;

We also updated the issue description to display the complete source → propagation → sink path, highlighting the flow of potentially malicious data through intermediate variables and functions. &#x20;

**Hypothesis:** &#x20;

If the rule can visualize how untrusted user input moves from sources to sinks through variable assignments and transformations, developers will more easily understand and remediate reflected XSS vulnerabilities. &#x20;

**Value/Purpose:** &#x20;

This enhancement improves clarity and confidence in issue results, reduces false positives, and empowers developers to identify the exact vulnerable flow within Visualforce pages for faster and more accurate remediation. &#x20;

Verified the enhancement logic of Cross-Site Scripting (Reflected) Detection with Data Flow Tracing via the following scenarios: &#x20;

1. Validated that the rule correctly detects reflected XSS vulnerabilities involving untrusted user input. &#x20;
2. Validated that the updated issue message now includes a Data Flow Trace that clearly indicates: &#x20;

* The source of untrusted input &#x20;
* Intermediate variable propagation &#x20;
* The final sink where the vulnerability occurs  &#x20;

#### 6. Data Flow Tracking Logic added to Flow DML in Loops Rule&#x20;

Enhanced the _sfmeta:DmlInFlowLoop_ rule to include data flow tracking that identifies how DML operations (Create, Update, Delete Records) are executed within loop elements in Flows. &#x20;

This enhancement should trace data variables flowing from loop iterators to DML elements. &#x20;

We also updated the issue description accordingly to clearly indicate the source and flow of data. &#x20;

**Updated message example:**  &#x20;

_DML element UPD should not be called in loop loop\_one. Data Flow Trace -_  &#x20;

_LOOPS (Loops loop\_one line: 15) →_  &#x20;

_DECISION (decisions DEC line: 4) →_  &#x20;

_RECORD UPDATES (recordUpdates UPD line: 29)_&#x20;

**Hypothesis:** &#x20;

If we add data flow tracking to detect DML operations triggered inside loops, developers will gain better visibility into where and how loop data is used in DML actions, helping them refactor Flows for better performance. &#x20;

**Value/Purpose:** &#x20;

Improves the accuracy and clarity of Flow DML-in-loop detections, helping developers understand performance risks, prevent governor limit issues, and optimize Flow design. &#x20;

Verified the enhancement of the rule sfmeta:DmlInFlowLoop via the following scenarios: &#x20;

* Validated that the rule correctly detects DML operations (Create/Update/Delete) executed inside Flow loops. &#x20;
* Validated that the rule reports a clear Data Flow Trace from the loop through intermediate elements (e.g., Decision) to the DML element.&#x20;

#### 7. Added New Parameters to Flow DML Should Not Be Called In Loops Rule&#x20;

Enhanced lag DML operations inside Salesforce Flows as violations across all flow types. However, some flow types (e.g., Scheduled Flows, Record-Triggered Flows configured for specific contexts) may legitimately require DML operations and should not be treated as violations. &#x20;

To provide flexibility and prevent unnecessary noise, we have introduced a series of configurable parameters for _sfmeta:DmlInFlowLoop_ rule that allow admins to enable or disable specific Flow Types for which DML-in-Flow should not generate a violation. &#x20;

This configuration is part of rule settings, which allows users to choose which flow types are exempt (e.g., Screen Flow, Record-Triggered Flow, Subflow, Scheduled Flow). &#x20;

**Hypothesis:**&#x20;

If users can configure flow types to be excluded from DML-in-Flow violations, then:&#x20;

* False positives will be reduced. &#x20;
* Teams will have better control over enforcing governance rules based on their architecture. &#x20;
* Developers will get cleaner, more relevant issue reports. &#x20;

**Value / Purpose:**&#x20;

* Reduces unnecessary violations for legitimate flow designs. &#x20;
* Provides team-level customization aligned with their Salesforce practices  &#x20;

**Parameter Name:** IgnoreRecordTriggeredFlow &#x20;

**Description:** &#x20;

The violation for DML operations inside the flow will be skipped for Record-Triggered Flows if marked as false. &#x20;

**Default Value:** false &#x20;

**Parameter Name:** IgnoreScreenFlow &#x20;

**Description:**&#x20;

The violation for DML operations inside the flow will be skipped for Screen Flows if marked as false. &#x20;

**Default Value:** false &#x20;

**Parameter Name:** IgnoreAutolaunchedFlow &#x20;

**Description:**&#x20;

The violation for DML operations inside the flow will be skipped for Autolaunched Flows if marked as false. &#x20;

**Default Value:** false &#x20;

**Parameter Name:** IgnoreScheduleTriggered Flow &#x20;

**Description:**&#x20;

The violation for DML operations inside the flow will be skipped for Schedule Triggered Flows if marked as false. &#x20;

**Default Value:** false &#x20;

**Parameter Name:** IgnorePlatformEventTriggeredFlow &#x20;

**Description:**&#x20;

The violation for DML operations inside the flow will be skipped for Platform Event–Triggered Flows if marked as false. &#x20;

**Default Value:** false &#x20;

Verified the new, configurable Ignore parameters for the sfmeta:DmlInFlowLoop rule, allowing selective exclusion of specific Salesforce Flow types from DML-in-loop violations via the following scenarios: &#x20;

All the parameters that are mentioned are added and are default to false supporting the correct behavior. &#x20;

#### 8. New Parameter added to rule Outer Class Explicit Sharing Rule&#x20;

We have updated the rule _sf:OuterClassExplicitSharing_ to provide a configurable parameter that controls whether violations are raised for abstract and virtual outer classes.  With this new parameter, users can avoid false positives in framework or base classes while still having the option to enforce explicit sharing when required by the security standards. &#x20;

**Hypothesis:** &#x20;

Introducing a configurable parameter to disable rule enforcement for abstract and virtual outer classes by default will reduce noise in scan results while preserving flexibility for teams that require strict sharing enforcement across all Apex class types. &#x20;

**Value / Purpose:** &#x20;

* Reduces false positives for commonly used base and framework classes &#x20;
* Improves rule adoption and trust by making enforcement intentional &#x20;

**Parameter Name:** EnableForAbstractAndVirtual &#x20;

**Description:** &#x20;

The violation will be skipped for abstract and virtual outer classes in sf:OuterClassExplicitSharing if marked as false. Default is false. &#x20;

**Default Value:** false &#x20;

Verified the newly added parameter via the following scenarios: &#x20;

BEFORE the parameter was added, the rule sf:OuterClassExplicitSharing enforced explicit sharing declarations as follows: &#x20;

* Classes declared with with sharing → No violation &#x20;
* Classes declared with inherited sharing → No violation &#x20;
* Classes without any sharing keyword → Violation raised &#x20;

A new configurable parameter EnableForAbstractAndVirtual has been added, this parameter allows to control whether the rule should enforce explicit sharing on abstract and virtual outer classes &#x20;

Current Behavior:&#x20;

<img src="../../../../../.gitbook/assets/unknown (76).png" alt="" height="210" width="560">

This behavior aligns with the intended design: &#x20;

* Reduces noise and false positives by default &#x20;
* Allows stricter enforcement when required by security standards&#x20;

#### 9. Improved Field Level Security Rule where User mode subqueries generated false positives&#x20;

We have identified false positives and have concluded that there is an edge case that was not accounted for in _Sf:fieldlevelsecurity_ rule.  Specifically, when the User mode is defined via AccessLevel in the return statement, the rule flagged it as a violation, resulting in false positives.  &#x20;

This behavior has now been fully remediated with this release. &#x20;

Verified the Sf:fieldlevelsecurity – USER\_MODE subquery false positive via several scenarios and confirm that the rule now correctly skips FLS violations when AccessLevel.USER\_MODE is provided via direct assignment, including: &#x20;

* Inline usage in Database.getQueryLocator &#x20;
* Simple variable assignment (AccessLevel mode = AccessLevel.USER\_MODE)&#x20;

#### &#x20;10. Added Data Flow Tracking for SOQL Injection Detection to Avoid Untrusted/Unescaped Variables in DML Query Rule&#x20;

We verified the rule expression, and confirmed that we did not support the naming pattern PR\_TestClassName in _Sf:testclassnaming_ rule. &#x20;

Instead, the rule supported only the following naming convention: &#x20;

* TestClassName - prefix &#x20;
* ClassNameTest - suffix &#x20;
* ClassName\_Test - Underscore &#x20;

As such, we enhanced this rule by adding a new parameter to Sf:testclassnaming to define allowed naming conventions.  &#x20;

The parameter is called **allowedPatterns**. &#x20;

**Description:**&#x20;

A comma-separated string of regular expressions matching allowed naming conventions for test classes.

The default of this parameter is to use the preexisting current functionality of the rule.  &#x20;

Further, we decided that the parameter field should never be empty. &#x20;

The value of this parameter is providing customers the flexibility to add any patterns that they allow as acceptable naming conventions without restriction to our logic. &#x20;

Validated the enhancement for the Sf:testclassnaming rule by verifying the following scenarios: &#x20;

* Able to see the configurable parameter allowedPatterns (comma-separated regex list) to support custom naming conventions. &#x20;
* Default behavior remains unchanged. &#x20;
* Validation ensures parameter cannot be empty. &#x20;
* Particular Reg expressions given in the allowed parameters skips the violations cccordingly.&#x20;

#### 11. Enhanced Parser for Methods Named “void”&#x20;

Earlier, our parser wouldn’t process Apex methods named void.&#x20;

Current behavior: &#x20;

* Ensures accurate parsing of valid Apex code &#x20;
* Improves analysis reliability &#x20;

The parser enhancement to support Apex methods named void has been thoroughly validated by QA across multiple scenarios on Preview instance.&#x20;

Positive Validation Scenarios:&#x20;

The following valid Apex patterns were tested and are now parsed correctly:&#x20;

* Basic Cases&#x20;

public void void() {}&#x20;

Method with body statements&#x20;

* Access Modifiers&#x20;

private void void() {}&#x20;

protected void void() {}&#x20;

global void void() {}&#x20;

* Modifiers & Combinations&#x20;

public static void void() {}&#x20;

public final static void void() {}&#x20;

* Parameterized Methods&#x20;

public void void(String name, Integer count) {}&#x20;

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

Negative Validation&#x20;

The following invalid syntaxes were tested and correctly rejected:&#x20;

* Missing method name \
  public void () {} → Parse error&#x20;
* Duplicate return type \
  public void void void() {} → Parse error&#x20;
* Missing parentheses \
  public void void {} → Parse error&#x20;
* Invalid keyword as method name \
  public void class() {} → Parse error&#x20;

These failures are expected and confirm that parser strictness is preserved.&#x20;

Conclusion&#x20;

* Parser now correctly supports void as a valid method name in Apex&#x20;
* All valid usage patterns are successfully parsed across different contexts&#x20;
* Invalid syntax continues to be rejected as expected&#x20;
* No regressions observed in parsing behavior&#x20;

#### 12. Enhanced AvoidDMLInLoops Rule with Interprocedural Analysis&#x20;

Enhanced the Avoid DML/SOQL Inside Loops rule to detect violations across method calls, files, and nested execution paths.&#x20;

Previously, some violations were missed when DML or SOQL was executed indirectly through methods called inside loops.&#x20;

**Scenarios Now Supported**&#x20;

* Recursive call paths &#x20;
* Deep and nested method chains &#x20;
* Cross-class traces &#x20;
* Cross-file scenarios &#x20;
* While-loop scenarios &#x20;
* Transitive call chains such as A → B → C → SOQL/DML &#x20;

**Outcome**&#x20;

Improves rule accuracy and helps detect governor-limit risks that were previously missed. &#x20;

### Fixes&#x20;

#### 1. Fixed issue with data flow analysis logic in Avoid Untrusted/Unescaped Variables in DML Query Rule&#x20;

We identified an issue in CodeScan where the Data Flow Trace for a SOQL injection rule where the trace repeatedly shows the same assignment instead of a clean, non-duplicated trace. &#x20;

The image displays a software project dashboard with a highlighted vulnerability: a potential SQL injection issue in the 'ProductController.getProducts' method.&#x20;

We determined the root cause of the issue and updated the rule logic accordingly. With this fix, this issue is now fully remediated. &#x20;

Verified relevant scenarios and rule is now working as expected. &#x20;

#### 2. SOQL Injection Rules Improvements&#x20;

Fix addresses a few scenarios described below.&#x20;

_Scenario 1:_ Sanitized parameter still flagged &#x20;

When a variable comes from a method parameter, the rule sometimes reports SOQL Injection even if the variable is sanitized or overwritten later. &#x20;

This happens because the rule uses DataFlowNode, which tracks where the variable originally came from. &#x20;

DataFlowNode is shared by multiple rules (SOQL Injection, Open Redirect, Useless Assignment, etc.). &#x20;

Because of this, we can’t easily change this behavior for one rule without impacting others. &#x20;

_Scenario 2:_ “At least once” assignment not detected &#x20;

DataFlowNode can detect whether an assignment is inside a condition. &#x20;

However, in some cases assignments happen inside loops, where the variable is still assigned at least once.&#x20;

DataFlowNode wasn’t originally designed to reliably confirm this loop behavior. &#x20;

Because of this limitation, these cases could not be properly handled and would likely result in producing false positives. &#x20;

We remediated these issues with this fix, greatly improving the value of the data flow logic in tracing the vulnerability from sink to source.&#x20;

#### 3. Fixed issue with Avoid Cleartext Transmission of Sensitive Information Rule&#x20;

Previously, the rule _InsecureEndpointRule_ was throwing a ClassCastException due to an invalid cast from ClassNameDeclaration to VariableNameDeclaration when analyzing endpoint expressions involving enum/class references (e.g., MODE.ERASE). &#x20;

After the fix:&#x20;

Proper type checking has been implemented before casting symbol table declarations.&#x20;

The rule now safely handles enum and class references without making incorrect assumptions.&#x20;

No runtime exceptions are observed during analysis.&#x20;

**Result:**&#x20;

* No ClassCastException observed.&#x20;
* Rule executes as expected across all tested scenarios.&#x20;

#### 4. Fixed issue with Resource Injection Rule&#x20;

Several customers were reporting a StackOverflowError for the _sf:ResourceInjection_ rule. Based on the analysis of logs and review of implementation, we uncovered an infinite recursive call in the isSanitized method in the UrlSanitization.java and determined that this is the reason for the StackOverflowError.&#x20;

Previously, the analysis stayed in Running state and logs showed a StackOverflowError for the mutual-recursion flow (methodA -> methodB -> methodA) with no exit condition, ending in req.setEndpoint(url) with the Rule Resource Injection. After the fix, the same code analyzes successfully, completes normally, and no StackOverflowError is observed in logs.&#x20;

Validation after fix:&#x20;

* Ran analysis on CodeScan&#x20;
* Analysis completed successfully&#x20;
* Analysis no longer remained in Running state&#x20;
* StackOverflowError was no longer seen in logs&#x20;

As such, we are reporting that this issue has been fully remediated.&#x20;

#### 5. Fixed issue with Unescaped Error Message XSS Rule

Earlier, the Unescaped Output Rule was able to trace data flow through methods but not through assignment chains effectively. Due to missing/inefficient assignment data flow handling, the rule repeatedly re-entered isSanitized while resolving sanitization status for variables passed through assignments. This resulted in deep recursive calls and ultimately a StackOverflowError, instead of reporting a violation&#x20;

**Validation**&#x20;

* Rule evaluation now terminates correctly without recursion overflow &#x20;
* isSanitized now handles edge cases without re-entering indefinitely &#x20;

As such, the issue has been successfully remediated. The rule now handles deep assignment chains correctly and avoids infinite recursion in isSanitized, without causing a StackOverflowError.&#x20;

#### 6. Resolved Stack Overflow Issue in Field Level Security Rule Analysis&#x20;

Fixed an issue where project analysis could become stuck or fail due to a stack overflow error in the Field Level Security rule during Apex analysis.&#x20;

Previously, specific Apex files containing deeply nested or recursive method call patterns could trigger repeated recursive evaluation within the _FieldLevelSecurityRule_, resulting in:&#x20;

* Stack overflow exceptions during analysis. &#x20;
* Excessively long analysis execution times. &#x20;
* Analysis workflows appearing stuck or unresponsive. &#x20;

**Behavior**&#x20;

* Improved handling of recursive and nested method traversal within the Field Level Security rule. &#x20;
* Added safeguards to prevent stack overflow conditions during rule evaluation. &#x20;
* Analysis now completes successfully for previously failing customer scenarios. &#x20;

**Validation**&#x20;

Validated using customer-reported files and additional large project analysis scenarios.&#x20;

Confirmed that:&#x20;

* Stack overflow errors no longer occur during analysis. &#x20;
* Analysis workflows complete successfully without interruption. &#x20;
* Existing Field Level Security rule detection behavior continues to function correctly. &#x20;

**Outcome**&#x20;

* Improves the stability and reliability of the Apex security analysis. &#x20;
* Prevents analysis failures caused by recursive execution paths. &#x20;
* Reduces the risk of stalled or incomplete project analysis workflows. &#x20;

