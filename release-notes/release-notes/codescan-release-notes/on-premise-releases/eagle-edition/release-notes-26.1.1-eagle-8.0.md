# Release Notes 26.1.1 Eagle 8.0

**Release Date: 17 July 2026**

### Summary&#x20;

CodeScan Self-hosted 26.1.1 is comprised of the following 6 components:&#x20;

* 0 New Features&#x20;
* 0 Application Enhancement&#x20;
* 0 New Rules&#x20;
* 3 Rule Enhancements&#x20;
* 0 Rule Deprecations&#x20;
* 3 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### &#x20;Rule Enhancements&#x20;

**1. Improved Rule Stability and Error Handling**&#x20;

Improved the stability and resilience of Apex rules execution by addressing multiple edge cases that could result in internal exceptions being exposed in analysis logs.&#x20;

Previously, certain rule evaluation scenarios could generate internal exceptions during analysis, resulting in Java stack traces being written to logs. Although analysis is often completed successfully, these errors could lead to incomplete rule evaluation and reduced confidence in results.&#x20;

Edge cases addressed:&#x20;

* SOQL Injection Rule Stability&#x20;

Improved handling of Apex data-flow analysis scenarios that could previously result in internal type-casting exceptions during rule evaluation.&#x20;

* LocaleInOldApi Rule Stability&#x20;

Improved handling of chained method invocations such as DateTime.now().format()to prevent internal rule execution errors while analyzing valid Apex code.&#x20;

* Defensive Null Handling Across Rule Execution&#x20;

Enhanced null-safety handling for multiple Apex rules, including:&#x20;

* Unescaped Output &#x20;
* SOQL Injection &#x20;
* Avoid SOQL in Loops &#x20;

Additional validation and defensive checks were introduced to ensure rule execution can safely handle unresolved AST and semantic-analysis paths without exposing internal exceptions.&#x20;

**Outcome**&#x20;

1. Improves overall rule engine stability. &#x20;
2. Prevents internal implementation details from appearing in analysis logs. &#x20;
3. Reduces the risk of incomplete rule evaluation. &#x20;
4. Provides more reliable and professional analysis output. &#x20;
5. Improves confidence in analysis results for Apex projects.&#x20;

**2. Enhanced Documentation for Sensitive PII Field Detection Rule**&#x20;

Updated the documentation and guidance for the Identify Potential Sensitive PII Fields rule (_sf:SecurePIIFields_) to provide clearer information about the types of data covered by the rule and how organizations can extend detection coverage.&#x20;

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

3\. Enhanced Avoid Calling SOQL and DML Inside Loops Rule&#x20;

Enhanced the _sf:AvoidSoqlInLoops_ rule to optionally detect Salesforce platform methods that consume SOQL queries internally when executed within loops.&#x20;

New Parameter&#x20;

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

**Outcome**&#x20;

* Improves detection of governor limit risks. &#x20;
* Identifies hidden SOQL consumption. &#x20;
* Helps developers avoid query-limit violations. &#x20;
* Preserves existing behavior unless explicitly enabled.&#x20;

### Fixes&#x20;

1. **Improved SOQL in Loops Rule Accuracy**&#x20;

Resolved an issue where the Avoid SOQL in Loops rule (_sf:AvoidSoqlInLoops_) could incorrectly report violations for certain method invocation patterns, resulting in false positives.&#x20;

Previously, the rule could identify SOQL or DML operations as being executed within a loop based solely on nested method call analysis, even when the queried method was not actually invoked from a looping execution path. In some scenarios, method calls originating from Apex test classes could also be included in the analysis, contributing to incorrect findings.&#x20;

**Behavior**&#x20;

The rule has been enhanced to improve analysis accuracy by validating the actual execution path before reporting nested-call violations.&#x20;

Improvements include:&#x20;

* Reduced false positives for SOQL and DML operations that are not executed within loop constructs. &#x20;
* Improved evaluation of nested method invocation chains. &#x20;
* Exclusion of Apex test class method calls from nested execution path analysis. &#x20;
* Improved validation to ensure nested-call violations are reported only when a genuine loop execution path exists. &#x20;

**Improved Diagnostics**&#x20;

The rule now provides more accurate reporting by distinguishing between nested method calls and actual SOQL/DML execution within loops, reducing misleading violations for valid code.&#x20;

**Outcome**&#x20;

* Reduces false positives reported by the Avoid SOQL in Loops rule. &#x20;
* Improves accuracy of data flow and nested-call analysis. &#x20;
* Prevents Apex test classes from influencing production rule evaluation. &#x20;
* Provides developers with more reliable and actionable rule findings. &#x20;
* Improves confidence in SOQL and DML loop detection for complex Apex applications.&#x20;

2. **Updated Guidance for Custom Field Requirement Configuration Rule**&#x20;

Updated the documentation and messaging for the Custom Field Security in Standard Object rule (_sfmeta:CustomFieldSecurityInStandardObject_) to provide clearer guidance on the recommended approach for configuring required custom fields on Salesforce standard and shared objects.&#x20;

Previously, the rule messaging did not clearly explain why marking custom fields as required at the schema level could have unintended consequences across different data entry mechanisms.&#x20;

The following rule metadata has been updated:&#x20;

* Title: Use the Page Layout to mark the custom field as required. &#x20;
* Message: Use the Page Layout to mark the custom field as required. &#x20;
* Description: Expanded to clarify that custom fields on standard and shared objects should be marked as required through page layouts rather than at the schema (system) level. &#x20;

The updated guidance explains that using page layouts limits the requirement to users interacting through the Salesforce UI, while avoiding unintended impacts on other data entry points such as:&#x20;

* APIs &#x20;
* Data Loader &#x20;
* Apex &#x20;
* Integrations &#x20;

Outcome&#x20;

* Provides clearer remediation guidance for Salesforce administrators. &#x20;
* Encourages Salesforce best practices for configuring required custom fields. &#x20;
* Helps prevent unintended validation issues across integrations and automated processes. &#x20;
* Improves the usability and clarity of rule findings.&#x20;



3. **Improved Unused Formal Parameter Detection for Dynamic SOQL Queries**&#x20;

Enhanced the Unused Formal Parameter rule (_sf:UnusedFormalParameter_) to improve detection of method parameters used as bind variables in dynamically constructed SOQL queries.&#x20;

Previously, the rule could incorrectly report unused parameter violations when parameters were referenced as bind variables within dynamic query strings, such as queries built using the fflib QueryFactory pattern. Although these parameters were resolved and used by Salesforce at runtime, they were not recognized by the rule, resulting in false-positive findings.&#x20;

**Behavior**&#x20;

The rule now recognizes method parameters used as SOQL bind variables within dynamic query execution patterns, including:&#x20;

* Database.query() &#x20;
* fflib\_QueryFactory &#x20;
* Dynamically constructed SOQL query strings &#x20;

Support has also been expanded to recognize bind variables used with common SOQL operators, including:&#x20;

* \= &#x20;
* != &#x20;
* \> &#x20;
* < &#x20;
* \>= &#x20;
* <= &#x20;
* IN &#x20;

Existing detection for direct IN :variable usage remains unchanged.&#x20;

The rule continues to report violations for method parameters that are genuinely unused.&#x20;

**Outcome**&#x20;

* Reduces false positives for applications using dynamic SOQL construction patterns. &#x20;
* Improves compatibility with the Salesforce Enterprise Patterns (fflib) framework. &#x20;
* Provides more accurate detection of genuinely unused method parameters. &#x20;
* Increases confidence in rule results for projects using dynamic query generation.&#x20;

