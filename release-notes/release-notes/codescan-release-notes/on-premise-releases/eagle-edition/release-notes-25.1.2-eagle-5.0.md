# Release Notes 25.1.2 Eagle 5.0

## Release Notes 25.1.2 Eagle 5.0

**Release Date: 17 October 2025**

### **Summary**

CodeScan Self-Hosted (version 25.1.2 (Eagle v5) is comprised of the following 9 components:

* 8 Rule Enhancements
* 1 Fix

Component details are listed in their corresponding sections within this document.

### Rule Enhancements

**1.     Enhancement to “Switch Statements Should Have a When Else Case” Rule**

Currently, the rule is not working as expected, as it does not raise violations when a switch statement lacks a when else block. We have modified that logic to correctly identify switch statements that are missing a when else case so that user can ensure the code is more robust, future-proof, and does not miss handling unexpected cases.

Example:

<figure><img src="../../../../../.gitbook/assets/image (2072).png" alt=""><figcaption></figcaption></figure>

Verified that the updated rule now correctly flags switch statements without a when-else block, ensuring violations are raised consistently for missing default cases.

<figure><img src="../../../../../.gitbook/assets/image (2073).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2074).png" alt=""><figcaption></figcaption></figure>

2. **Enhancement to “Avoid Reversed Operators” Rule**

Modified the rule logic to correctly detect and report improper usage of reversed operators (=-, =+) in Apex code, so that user can avoid mistakes where variables are unexpectedly reassigned rather than incremented/decremented.

Current Behavior:

* Violations are not raised when using reversed operators like target =- num; or target =+ num;.

Expected Behavior:

* The rule should detect and flag cases of reversed operators (=-, =+) and provide a clear violation message.
* The violation message should explain the confusion:
  * x =- y; assigns -y instead of subtracting.
  * x =+ y; assigns +y instead of adding.

This new logic will prevent developers from introducing subtle logic bugs caused by operator misuse.  Further, we updated the rule example with the following:

<figure><img src="../../../../../.gitbook/assets/image (2075).png" alt=""><figcaption></figcaption></figure>

Verified the new logic via the following scenarios:\
1\. Rule sf:AvoidReversedOperators raises violations for reversed operator cases (=-, =+).

2\. Rule does not raise false positives on valid operator usage (+=, -=).

<figure><img src="../../../../../.gitbook/assets/image (2076).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2077).png" alt=""><figcaption></figcaption></figure>

**3.   Enhancement to “CouplingBetweenObjects” Rule**

Modified the rule logic to correctly detect and report violations so that users can identify classes with excessive dependencies and reduce code complexity for better maintainability and testability.

Verified that the violation is triggered when the number of classes used exceeds the defined threshold value in the rule parameter (for example, if the threshold is set to 4 and 5 classes are used, a violation will be raised).

<figure><img src="../../../../../.gitbook/assets/image (2078).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../../../../../.gitbook/assets/image (2079).png" alt=""><figcaption></figcaption></figure>

**4.   Enhancement to “Add Empty String” Rule**

Updated the rule logic to identify and flag expressions where literals are concatenated with an empty string (e.g., "" + 123 or 123 + "").  Also ensured that violations are reported with a clear message and that valid concatenations and type-specific toString() methods are not falsely flagged.

Verified the below scenarios all are working as expected.\
\
1\. Empty string with numeric or boolean literals

Examples:\
'' + 123, 123 + '', '' + -42, '' + 3.14, false + '', '' + true

2\. Empty string with string/char literals or inside chains

Examples:\
'' + 'abc', 'abc' + '', 'A' + '' + 'B', 1 + '' + 2

3\. Empty string literals inside parentheses

Examples:\
('' + 1) + 2, 1 + ('' + 2)

4\. Empty string at start of long chain with literals and variables

Example:\
'' + 123 + 987 + var1 + var2

5\. Empty string used with - operator and literals

Examples:\
'' - 123, 123 - '', '' - -42

<figure><img src="../../../../../.gitbook/assets/image (2080).png" alt=""><figcaption></figcaption></figure>

**5.  Enhancement to “Avoid Hard Coded Resource References” Rule**

Enhanced the rule logic to identify hard-coded file path references and raise violations with a clear issue message.

Validated the logic by verifying that users are able to see the violations for the use of the attribute value that starts with '/resource/'.

<figure><img src="../../../../../.gitbook/assets/image (2081).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2082).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2083).png" alt=""><figcaption></figcaption></figure>

**6.  Enhancement to Suppress Warnings Rule**

Our rule, TrackSuppressWarnings, had logic to find @SuppressWarnings, but the logic didn’t include find @suppresswarnings.

This suppression tag works in any case, and we recognized that our TrackSuppressWarnings rule needs to do the same (meaning the rule needs to be case-insensitive.)

This logic was added to this rule in this enhancement.

Verified the  SuppressWarnings rule enhancement and validated that the suppression tag is working in all case-insensitive instances and our TrackSuppressWarnings rule is throwing violations for all cases.

<figure><img src="../../../../../.gitbook/assets/image (2084).png" alt=""><figcaption></figcaption></figure>

**7.  Enhancement to Apex rule “Unused Formal Parameter” {sf:UnusedFormalParameter}**

CodeScan has offered this rule since Dec 2017. Recently, a customer reported that Unused Formal parameter doesn’t find when variables used in SOQL. We replicated this issue where CodeScan flagged a variable as an unused variable, even though it is used in the SOQL string.

We have enhanced this rule to detect additional cases where string parameters are part of SOQL.  The rule now detects cases where string parameters are used as part of building SOQL query.

Verified the enhanced logic of rule “UnusedFormalParameter” via the following scenarios.

1.  Previously, a parameter (e.g., encounterIds) used in a SOQL string (e.g., WHERE Id IN :encounterIds) was wrongly reported as unused. Now, this is correctly detected as usage — no violation.\


    <figure><img src="../../../../../.gitbook/assets/image (2085).png" alt=""><figcaption></figcaption></figure>
2.  Also verified below cases all are working as expected Verified: Parameter used in SOQL with bind variable (:encounterIds) — no violation Verified: Parameter used via clause string assembly — no violation Verified: Parameter incorrectly concatenated into SOQL string — violation Verified: Parameter declared but not used anywhere — violation\


    <figure><img src="../../../../../.gitbook/assets/image (2086).png" alt=""><figcaption></figcaption></figure>

**8.  Another Rule Enhancement for sf:UnusedFormalParameter**

In this rule enhancement, we introduce a configuration flag, ignoreUnusedParametersInInterfaceOverrides, in the sf:UnusedFormalParameter rule, so unused parameters in valid interface implementations and method overrides can be conditionally suppressed. By default, violations will continue to be reported unless this flag is explicitly set to true.

**How to Identify These Parameters for Suppression**

When designing your rule improvement, the logic should:

1.  **Check if the method is implementing a known Salesforce interface method**

    * Use method signature matching (name, parameters, visibility).
    * Confirm the containing class uses implements keyword for one of the known Salesforce interfaces.
    * Ensure parameter types match exactly, e.g., SchedulableContext, Database.BatchableContext.

    <figure><img src="../../../../../.gitbook/assets/image (2087).png" alt=""><figcaption></figcaption></figure>
2. **Visibility Enforcement**
   * Only suppress violations if the method visibility is public or global, as required by the platform.
   * Private or protected methods should never be eligible for suppression under this rule.
   * This ensures that suppression only applies to methods actually callable by the platform or conforming to Apex interface rules.
3.  **Override Detection**

    * If a method in a class overrides a method from a superclass or an abstract class:
      * Signature match is mandatory (same name, return type, and parameters).
      * Use of the override keyword confirms the intent, but even without it, structural matching should be enough.
      * In such cases, the parameter should not be flagged if unused, since it’s required by the parent contract.

    **Value / Purpose**

    * Prevent misleading or incorrect violations in valid interface and override implementations (e.g., execute(SchedulableContext)).
    * Preserve backward compatibility by keeping the rule strict by default.

Additionally, we updated the Rule Description to “Avoid passing parameters to methods or constructors without actually referencing them in the method body.  Use the ignoreUnusedParametersInInterfaceOverrides parameter to suppress violations for unused parameters in valid interface implementations and method overrides.”

Verified the rule sf:UnusedFormalParameter and validated the following conditions:

* The method **implements a known Salesforce interface** method.
* Method signature **matches exactly** in terms of:
  * Name
  * Parameters
  * Visibility
* The containing class uses the implements keyword with one of the **known Salesforce interface**s (e.g., Schedulable, Database.Batchable).
*   **Parameter types match exactly**, including types such as:

    * SchedulableContext
    * Database.BatchableContext

    <figure><img src="../../../../../.gitbook/assets/image (2088).png" alt=""><figcaption></figcaption></figure>

    \


    <figure><img src="../../../../../.gitbook/assets/image (2089).png" alt=""><figcaption></figcaption></figure>

### Fixes&#x20;

1.  **Fixed issue with CodeScan rule detecting SOQL Injections, which was causing analyses to break**\
    Previously, while analyzing for SOQL Injection, if a local variable is declared using a class-level variable of same name, then CodeScan analyses were erroring with StackOverflowError, as it was stuck in a loop while resolving the reference.\
    \
    Example:\
    class Foo { private static String QUERY = 'Select '; public static List\<Opportunity> getData(String stage) { String query = QUERY + 'Id FROM Opportunity WHERE StageName = :stage'; return Database.query(query); } }\
    \
    With this fix, we added validation to detect and prevent such recursive reference resolution.\
    \
    Verified the SOQL Injection rule fix (which was causing stack overflow error).  Validated that now users are not encountering the error, and their project analyses are working as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (2090).png" alt=""><figcaption></figcaption></figure>

