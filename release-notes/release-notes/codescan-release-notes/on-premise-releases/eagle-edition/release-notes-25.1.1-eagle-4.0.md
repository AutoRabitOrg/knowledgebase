# Release Notes 25.1.1 Eagle 4.0

## CodeScan Release Notes 25.1.1 Eagle 4.0

Release Date: 18 July 2025

### Summary

CodeScan Self-Hosted (versions 25.0.2 (Tiger v4) and 25.1.1 (Eagle v4) are comprised of the following 19 components:

·       5 Enhancements

·       2 New Rules

·       12 Fixes

Component details are listed in their corresponding sections within this document.

### Enhancements

1\.     Enhanced rule “vf:AvoidJavaScriptScriptlets” by adding a new parameter to the rule

Historically, CodeScan has offered our “Avoid JavaScript Scriptlets” rule to inspect customer’s code and flag where there JavaScript Scriplets.&#x20;

With this release, a new parameter was introduced to allow users to choose whether to include or ignore violations related to code supporting the Lightning functions within script.

* Parameter Name: ignoreSupportingCode
* Type: Boolean (true or false)
* Default: false
* Description: This option allows users to ignore violations related to code supporting the Lightning functions within script. By default, it is set to false.

Verified the below scenarios for rule vf:AvoidJavaScriptScriptlets and report that all scenarios are working as expected.

1. Validated the rule with LightningFunctions and set the default value false then user is able to see the violations.
2. Validated the rule with LightningFunctions and set the value true then user is not able to see the violations which is expected.
3. Validated the rule without LightningFunctions then user is able to see the violation which is expected.
4.  Validated the rule by setting the parameter ignoreSupportingCode as false/true working as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1752).png" alt=""><figcaption></figcaption></figure>

1\.     Updated description for Deprecated rules

&#x20;

Historically, CodeScan has deprecated rules over time.  However, we recognize that we can be clearer about why the rule is being deprecated.  In this release, we have initiated this practice (and plan to adhere to this practice in the future).

1.Update the description of deprecated Apex Rule “Use System.assertEquals instead of System.assert“ and key”sf:UseAssertEqualsInsteadOfAssertEquality” with the following:

This rule detects unit test assertions in object references equality. Instead of using System.assert combined with "==" as an equality operator, these assertions should be made by more specific methods, like assertEquals.

This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseAreEqualInsteadOfAssertBoolean.

2.Update the description of deprecated Apex Rule “Use System.assertEquals instead of System.assert“ and key”sf:UseAssertEqualsInsteadOfAssert” with the following:

This rule detects Unit test assertions in object references equality. Instead of using System.assert combined with ".equals()" as an equality check, these assertions should be made by more specific methods, like assertEquals.

This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseAreEqualInsteadOfIsTrue

3.Update the description of deprecated Apex Rule “Use System.Assert instead of System.assertEquals“ and key”sf:UseAssertInsteadOfAssertEquals” with the following:

When asserting a value is the same as a boolean literal, use System.assert, instead of System.assertEquals.

This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseIsTrueInsteadOfAreEqual

4.Update the description of deprecated Apex Rule “Unnecessary Parentheses“ and key”sf:UnnecessaryParentheses” with the following:

Sometimes expressions are wrapped in unnecessary parentheses, making them look like function calls.

This rule has been deprecated. Please remove it from your custom Quality Profile and instead add the rule sf:UselessParentheses as a best practice for code styling.

2\.     Enhancement to CodeScan Rule “URL Redirection to Untrusted Site” {sf:OpenRedirect}

CodeScan has traditionally used this rule to check against redirects to user-controlled locations. This is important because untrusted input could cause an attacker to redirect the user to a malicious site thereby allowing the attacker to launch a phishing scam and steal user credentials.

<figure><img src="../../../../../.gitbook/assets/image (1753).png" alt=""><figcaption></figcaption></figure>

However, our existing rule did not specifically check for the use of Network.forwardToAuthPage.

<figure><img src="../../../../../.gitbook/assets/image (1754).png" alt=""><figcaption></figcaption></figure>

This rule has now been enhanced with this logic and we have verified that users are now able to see the violation for the use of both Network.forwardToAuthPage and PageReference.

<figure><img src="../../../../../.gitbook/assets/image (1755).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1756).png" alt=""><figcaption></figcaption></figure>

More details regarding the Network class can be found here: [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_network.htm#apex_System_Network_forwardToAuthPage)

1\.     Enhanced rule “Avoid Untrusted/Unescaped Variables in DML Query" to account for potential SOQL injections when “queryWithBinds” is used.

Historically, CodeScan has offered our “Avoid Untrusted/Unescaped Variables in DML Query” rule to inspect customer’s code and flag where there are SOQL Injection possibilities.  Recently, one of our customers had performed a test and expected this rule to flag an issue in their code, but it did not.  We determined that the rule should be enhanced for when “queryWithBinds” is used.

Our engineering team utilized specifications within Salesforce documentation (specifically,  [Help And Training Community](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_bind_var_soql.htm\&release=242\&type=5)) in order to consider only the query for executed with queryWithBinds() for vulnerability check and violation, avoiding the other parameters such as: (Map, accessLevel) .\
Database.queryWithBinds(query, bindVariablesMap, accessLevel)

Example:

<figure><img src="../../../../../.gitbook/assets/image (1757).png" alt=""><figcaption></figcaption></figure>

Verified that after the rule enhancement was engineered, users are able to see the violation for rule “Avoid Untrusted/Unescaped Variables in DML Query” as expected.

<figure><img src="../../../../../.gitbook/assets/image (1758).png" alt=""><figcaption></figcaption></figure>

1\.     Enhanced rule “Controller Naming Convention” for Apex and Visualforce

Some customers are reporting that CodeScan is flagging violations on components that should not be flagged (i.e., SandboxRefreshAdminController)

This issue is remediated in this release.

We validated the fix by:

* Creating a class file in salesforce org using UI and name the controller like in example.
* Creating a vf page in salesforce org with the controller attribute like shown in the example.
* Setting parameters for controller naming in CS, try the parameters with different cased letters ex: ConTroLLer etc.
* After scanning false positives should not be visible

### New Rules

&#x20;1\.     Server Side Request Forgery

This is a rule that checks for any changeable inputs to a url string in a method that returns a PageReference.

Type: Vulnerability\
Severity: Critical\
Name: Server Side Request Forgery (SSRF)\
Key: ServerSideRequestForgery\
Message: Sanitize input to avoid possible SSRF\
Description: This rule identifies potential Server-Side Request Forgery (SSRF) vulnerabilities by detecting unsafe URL construction and external network requests that could allow an attacker to manipulate server-side network calls.

Server-Side Request Forgery (SSRF) occurs when an attacker can influence the server to make arbitrary network requests, potentially accessing internal resources, sensitive endpoints, or bypassing security controls.

Input can be cleansed by using Id.valueOf, Date.valueOf, etc. Or escaped using String.escapeSingleQuotes().

Parameters\
Name: sanitizationMethod\
Description: A comma separated list of custom methods that provide input sanitization.

CWE: 918

Test Cases with Violations\
\
1\. Validated direct embedding of user input into a URL without sanitization, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../../.gitbook/assets/image (1759).png" alt=""><figcaption></figcaption></figure>

2.  Validated unescaped dynamic input into URL, resulting in a violation (SSRF) as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1760).png" alt=""><figcaption></figcaption></figure>
3.  Validated that one parameter is sanitised but the other is not sanitised, still resulting in a violation (SSRF) as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1761).png" alt=""><figcaption></figcaption></figure>
4.  Validated concatenated unsafe dynamic parameters in a URL, resulting in a violation (SSRF) as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1762).png" alt=""><figcaption></figcaption></figure>
5.  Validated the presence of a malicious SSRF-style payload embedded in the URL, resulting in a violation (SSRF) as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1763).png" alt=""><figcaption></figcaption></figure>
6.  Validated the attempt at "sanitization" using regex, which is not an approved method, resulting in a violation (Improper sanitization) as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1764).png" alt=""><figcaption></figcaption></figure>

Test Cases with No Violations

1\.     Validated input sanitized using Id.valueOf, resulting in no violation as expected.

<figure><img src="../../../../../.gitbook/assets/image (1765).png" alt=""><figcaption></figcaption></figure>

2.  Validated input escaped using String.escapeSingleQuotes, resulting in no violation as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1766).png" alt=""><figcaption></figcaption></figure>
3.  Validated that the URL starts with "/" ensuring an internal redirect, resulting in no violation as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1767).png" alt=""><figcaption></figcaption></figure>
4.  Validated date validated using Date.valueOf, resulting in no violation as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1768).png" alt=""><figcaption></figcaption></figure>
5.  Validated a static URL with no dynamic input, resulting in no violation as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1769).png" alt=""><figcaption></figcaption></figure>

    6.Validated fully escaped input and use of safe methods, resulting in no violation as expected.\


    <figure><img src="../../../../../.gitbook/assets/image (1770).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
NOTE: The implementation currently addresses the most common scenarios related to resource injection and SSRF vulnerabilities. However, due to the dynamic and context-dependent nature of these issues—especially when influenced by external inputs, indirect references, or complex backend behaviors—there may be edge cases that are not readily identifiable or testable. These may only surface under specific configurations or data conditions.
{% endhint %}

2. Resource Injection

Prior to this new rule, CodeScan did not catch resource injection in Apex. This is very similar to our new rule “Server Side Request Forgery” (also included in this release)

However, there are some basic things that make it resource injection and not SSRF. In this example: public PageReference init(){ AccListString = 'INIT'; BaseObjId = system.label.MY\_Label; return null; }

public PageReference prepareAccs(){ String newUrl = '/apex/maps\_\_Maps?baseOjectId='+BaseObjId+'\&recordIds='+AccListString; PageReference p = new PageReference(newUrl); p.setRedirect(true); return p; }

Here, we are looking at resource injection because the URL is internal (starts with / ) This rule should find any external variables that are used to create dynamic internal URLs.

<figure><img src="../../../../../.gitbook/assets/image (1771).png" alt=""><figcaption></figcaption></figure>

Acceptance Criteria

Type: Vulnerability\
Severity: Critical\
Name: Resource Injection\
Key: ResourceInjection\
Message: Sanitize input to avoid possible resource injection\
Description: This rule identifies potential resource injection vulnerabilities by detecting unsafe URL construction for internal network requests.

Resource injection occurs when user-controllable data is used to specify a resource identifier without proper validation.

Input can be cleansed by using Id.valueOf, Date.valueOf, etc. Or escaped using String.escapeSingleQuotes().

See:

[MITRE, CWE-99](https://cwe.mitre.org/data/definitions/99.html) - Improper Control of Resource Identifiers ('Resource Injection')

Tags: cwe

Remediation Time: 10 minutes

Parameters:\
Name: sanitizationMethod\
Description: A comma separated list of custom methods that provide input sanitization.

CWE: 99

Verified the following scenarios are all working as expected

1.  Verified that sanitizing both BaseObjId and AccListString before URL building prevents violations.\


    <figure><img src="../../../../../.gitbook/assets/image (1772).png" alt=""><figcaption></figcaption></figure>
2.  Verified that validating BaseObjId using Id.valueOf() ensures the ID is valid and safe to use in URLs.\


    <figure><img src="../../../../../.gitbook/assets/image (1773).png" alt=""><figcaption></figcaption></figure>
3.  Verified that input AccListString validated with regex and sanitized prevents violation.\


    <figure><img src="../../../../../.gitbook/assets/image (1775).png" alt=""><figcaption></figcaption></figure>
4.  Verified that using AccListString directly in URL without any sanitization or validation causes violations.\


    <figure><img src="../../../../../.gitbook/assets/image (1776).png" alt=""><figcaption></figcaption></figure>
5.  Verified that sanitizing only BaseObjId but not AccListString leads to a violation.\


    <figure><img src="../../../../../.gitbook/assets/image (1777).png" alt=""><figcaption></figcaption></figure>
6.  Verified that sanitizing the URL string after using variables has no effect, resulting in a violation.\


    <figure><img src="../../../../../.gitbook/assets/image (1778).png" alt=""><figcaption></figcaption></figure>
7.  Verified that URL encoding AccListString without further format validation leads to violation.\


    <figure><img src="../../../../../.gitbook/assets/image (1779).png" alt=""><figcaption></figcaption></figure>
8.  Verified that replacing characters rather than proper sanitization leads to security violations.\


    <figure><img src="../../../../../.gitbook/assets/image (1780).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
NOTE: This implementation currently addresses the most common scenarios related to resource injection and SSRF vulnerabilities. However, due to the dynamic and context-dependent nature of these issues, especially when influenced by external inputs, indirect references, or complex backend behaviors—there may be edge cases that are not readily identifiable or testable. These may only surface under specific configurations or data conditions.
{% endhint %}

### Fixes

1. Fixed issue with the rule “vf:UnescapedAttributes vulnerability” {where false positive violations were being flagged}

CodeScan suggests the remediation for this issue is to use JSENCODE() to escape values. However, some customers reported that when this is added to their code, the issue was still being flagged as a violation. We validated the fix by:&#x20;

• Verified the updated description and example under rule: vf:UnescapedAttributes vulnerability

<figure><img src="../../../../../.gitbook/assets/image (1781).png" alt=""><figcaption></figcaption></figure>

• Verified that Rule is throwing violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1782).png" alt=""><figcaption></figcaption></figure>

This CodeScan rule was updated with the following changes:

1\. Changed the description to the following:

Reflected Cross-site Scripting (XSS) occurs when an attacker injects browser executable code within a single HTTP response.

Using unescaped parameters can be a security risk. c:\* and apex:\* attributes are not checked unless they are known to cause problems. You can check other attributes by adding them to the configuration for this rule.

In Visualforce, escape methods such as JSENCODE can be used to sanitize variables as shown below.

For Aura components, sepcifically aura:unescapedHtml, make sure to sanitize variables in controllers before using them. This component is intended to output properly sanitized HTML from a trusted source. If properly handled, mark the issue as Resolved: False Positive/Won't Fix.

2\. Added the following Aura Example Bad Scenario:

Example :

\<aura:component>   &#x20;

&#x20; \<aura:unescapedHtml value="{!v.htmlstring}"/>.  //Bad: not recommended.

\</aura:component>

&#x20;

1\.     Fixed issue with the rule “Field Level Security Vulnerabilities” (sfmeta:PageLayoutNaming) for classes using “Without Sharing” {where false positive violations were being flagged}

&#x20;

Some customers have reported an issue with CodeScan's reporting of "Permissions should be checked before accessing resource" vulnerabilities in our Apex codebase, specifically within classes that are declared without sharing.

The without sharing keyword in Apex classes causes the code to execute in system context, bypassing standard Salesforce sharing and field-level security checks. This is intentional for certain system-level operations and utility classes within our application.

However, CodeScan is flagging fields within these without sharing classes as vulnerabilities, stating "Permissions should be checked before accessing resource." This is creating an inflated number of false positives and incorrectly portraying our code's security posture.

CodeScan is designed to identify potential security issues; however, in the context of without sharing classes, these field-level security checks are redundant and misleading.

As such, the rule update in this release enables CodeScan to recognize that when a class is declared without sharing, field-level security checks are irrelevant, and the "Permissions should be checked before accessing resource" rule is suppressed for fields within without sharing classes.

<figure><img src="../../../../../.gitbook/assets/image (1783).png" alt=""><figcaption></figcaption></figure>

Note that a new parameter has been added to this rule to Ignore Without Sharing

Name: ignoreWithoutSharing\
Message: When this parameter is true, this rule ignores Field Level Security issues in all without sharing classes.\
Default: false

<figure><img src="../../../../../.gitbook/assets/image (1784).png" alt=""><figcaption></figcaption></figure>

Appropriately, CodeScan is flagging violations properly when “with sharing” is used.

<figure><img src="../../../../../.gitbook/assets/image (1785).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed Deprecation Warning associated with sonar.login

Some customers were reporting that they were

receiving deprecation warnings in their scans indicating that the use of sonar.login is deprecated, and that instead, going forward, authentication should be done using sonar.token.

This issue has been remediated in this release.  CodeScan now supports both sonar.login and sonar.token for authentication during Codescan analyses. Top of Form

Verified the below plugins by using sonar.token and sonar.login parameters in the sonar command and sfdx; both scenarios are working as expected.

SFDX -@salesforce/cli/2.61.8

Sonar-scanner - 5.0.1.3006V

1. Validate Project analysis through above plugins
2. Validate branch analysis.



2\.     Fixed issue with the rule “sf:AtLeastOneConstructor”

The rule sf:AtLeastOneConstructor is currently not throwing violations in scenarios where both the class and methods are present; however, it should be violated.

<figure><img src="../../../../../.gitbook/assets/image (1786).png" alt=""><figcaption></figcaption></figure>

Additionally, the current implementation flags only non-static classes without constructor.  As part of the fix, classes with at least one non-static member (method or field) will also be flagged.

Also, the description will be updated from “Each class should declare at least one constructor" to “Each class should declare at least one constructor. Classes with solely static members are ignored."

&#x20;

Verified rule: sf:AtLeastOneConstructor for the below scenarios, and confirmed users are able to see the violations as expected\
\
Below are the scenarios for which violations should be throw as per the rule\
1\. Missing constructor with all non-static methods

<figure><img src="../../../../../.gitbook/assets/image (1787).png" alt=""><figcaption></figcaption></figure>

2.  Missing constructor with a mix of static and non-static methods\


    <figure><img src="../../../../../.gitbook/assets/image (1788).png" alt=""><figcaption></figcaption></figure>

Below are the scenarios which should be ignored as per the rule

1. Interface with method declarations
2. Enum with constant values\
   ![](<../../../../../.gitbook/assets/image (1789).png>)

Below are the scenarios for which violations should not throw

1.  Missing constructor, but all methods and fields are static (utility class)\


    <figure><img src="../../../../../.gitbook/assets/image (1790).png" alt=""><figcaption></figcaption></figure>
2.  Class with an explicit constructor\


    <figure><img src="../../../../../.gitbook/assets/image (1791).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed 2 issues with our SOQL Injection rule

We have discovered that the issues flagged disappear on different lines; we have also discovered that CodeScan doesn’t find the fflib method escape.

These 2 issues are remediated in this release.

Verified the SOQL Injection rule and confirm users are able to see the violations for the rule as expected.

<figure><img src="../../../../../.gitbook/assets/image (1792).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed issue with rule “sf: FieldLevelSecurityRule”

&#x20;

During maintenance testing, we discovered that this rule was triggering the null pointer exception when parsed through the trigger files. In the rule logic it was searching for relevant ASTClassOrInterfaceBody to get all the constructors in that class. Since triggers don't have constructors, control flow proceeds further if we get a non-null node for ASTClassOrInterfaceBody.\
\
We updated this rule to parse the trigger files by adding extra logic to find the Trigger specific nodes (TriggerBodyDeclaration etc).

We tested the fix to the Null pointer Exception with sf: FieldLevelSecurityRule and verified we are now no longer able to see the Null pointer exception for the trigger files in the logs (as expected).

<figure><img src="../../../../../.gitbook/assets/image (1793).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed issue with rule “RequireDescriptionComponent”

Some customers reported that the CodeScan rule “RequireDescriptionComponent” rule was not working for custom fields on standard objects.

This issue has been remediated in this release.  Previously, CodeScan offered a rule “_sfmeta:RequireDescriptionField_” which had been deprecated for this updated rule.  But the updated rule was not designed for standard objects.  When we tested the logic of the deprecated rule, we found that it could be used for reference for this update to the new rule “RequireDescriptionComponent”

The rule enhancement was verified via the below scenarios:\
\
1\. Verified Custom Field on Standard Object – Missing Description

<figure><img src="../../../../../.gitbook/assets/image (1794).png" alt=""><figcaption></figcaption></figure>

2. Verified Custom Field on Custom Object – Missing Description

<figure><img src="../../../../../.gitbook/assets/image (1795).png" alt=""><figcaption></figcaption></figure>

3. Verified Standard Fields on Standard Object – Missing Description

<figure><img src="../../../../../.gitbook/assets/image (1796).png" alt=""><figcaption></figcaption></figure>

4. Verified Custom Field on Standard Object – With Description

<figure><img src="../../../../../.gitbook/assets/image (1797).png" alt=""><figcaption></figcaption></figure>

5. Verified Custom Field (With Description) on Custom Object (Without description)

<figure><img src="../../../../../.gitbook/assets/image (1798).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed issue with CodeScan’s APEX parser

&#x20;

Some customers reported that the CodeScan parser was incorrectly flagging valid Apex code using the UPDATE AS SYSTEM syntax as a parsing error. This was occurring because the parser doesn't recognize the AS SYSTEM portion of the UPDATE statement, leading to a ParseException and preventing accurate code analysis.

This issue has been remediated with this release.

We had previously verified the Parsing error in APEX Code for DML queries if user using UPDATE AS SYSTEM syntax would throw the parser exception.  With this fix, users are now able to see the violations as expected for the file.

Verified the below queries in Apex code that users do not get any Parser errors; instead the updated CodeScan parser is working as expected.

* INSERT AS SYSTEM
* DELETE AS SYSTEM
* UNDELETE AS SYSTEM
* UPDATE AS SYSTEM&#x20;

<figure><img src="../../../../../.gitbook/assets/image (1799).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed issue with rule “Avoid running Soql and DML inside loops” {sf:AvoidSoqlInLoops}

&#x20;

Some customers reported unexpected behavior in this rule, producing false positives.

The root cause of the false positives is that when a method of an object is invoked within another method, and both methods share the same name, the current rule implementation incorrectly interprets this as a recursive call and subsequently triggers a violation.  Further, the Stack Loop trace is indefinite.

This has been remediated in this release.  The updated rule logic now handles these edge cases by checking for method image to be exactly the same (method != diffObj.method).

We have verified the fix across related and existing test cases and edge conditions by confirming that if a method of an object is invoked within another method, and both methods share the same name, the user will not see the violation (as it is false positive).

Verified the the rule sf:AvoidSoqlInLoops confirming that if a method of an object is invoked within another method, and both methods share the same name, the user will not see the violation as it is false positive.

<figure><img src="../../../../../.gitbook/assets/image (1800).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1801).png" alt=""><figcaption></figcaption></figure>

However, there’s more to this issue and fix!  A scenario which was earlier covered stopped working as expected as a result of the fix made above.

As such, an additional update to the rule implementation was made to accommodate both scenarios (the pre-existing condition but also indefinite stack loop trace).

Verified the Fix for rule sf:AvoidSoqlInLoops via several scenarios, including:

Verified – SOQL inside a method (not directly in a loop) — no violation as expected

Violations Expected for the below scenarios

1. Verified SOQL directly inside a for loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1802).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL inside nested if blocks within a loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1803).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL inside a try/catch block within a loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1804).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL in a method (or recursive call) invoked from a loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1805).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL in static helper method called from a loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1806).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL inside a while loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1807).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL inside a do-while loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1808).png" alt=""><figcaption></figcaption></figure>

1. Verified SOQL directly inside System.debug() within a loop — got violation as expected

<figure><img src="../../../../../.gitbook/assets/image (1809).png" alt=""><figcaption></figcaption></figure>

No Violations Expected for the below scenarios

1. Verified Bulkified SOQL outside the loop (e.g., IN :ids) — no violation as expected
2. Verified SOQL in deep conditional logic but not inside a loop — no violation as expected
3. Verified SOQL inside try/catch block, not inside a loop — no violation as expected
4. Verified SOQL in method not called from a loop — no violation as expected
5. Verified SOQL inside interface/abstract method (called via polymorphism from loop) — no violation as expected

14\. Verified SOQL inside constructor called from a loop — no violation (as expected for shallow analyzers)

&#x20;

1\.     Fixed issue ARM users recieving an error: “Component can't be null” while running a CodeScan analysis from ARM.

&#x20;

The issue is occurring in the SFDX retrieval. From ARM, when the user commits only the fields (or, for example, lookup fields), the .object-meta.xml is not retrieved. As a result, the retrieved file structure differs from what was expected. After analysing the rule’s implementation, it was found that the rule does not check if the .object-meta.xml file exists first and forcibly tries to throw the violation on the file. Hence, the "component can't be null" error is thrown. This required an engineering fix in the rule.

Note: The issue lies in one of the common methods many rules use, so this error is not confined to these two rules.

Other rules that use this method include:

<figure><img src="../../../../../.gitbook/assets/image (1810).png" alt=""><figcaption></figcaption></figure>

With this fix, users are now able to see the violations for all 7 rules when running a CodeScan analysis from the ARM side using the CodeScan plugin:

\
Rules:

sfmeta:CrossObjectFormulaOveruse

sfmeta:ObjectLookupsOveruse

sfmeta:RelationShipOveruse

sfmeta:ExternalIdOveruse

sfmeta:RollUpOveruse

sfmeta:LimitCustomFields

sfmeta:nCinoFieldHistoryTracking

Verified by committing only specific fields and triggering SCA analysis — violations appeared as expected.

Ran analysis for the entire Salesforce org, including objects — violations were also detected."

<figure><img src="../../../../../.gitbook/assets/image (1811).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1812).png" alt=""><figcaption></figcaption></figure>

1\.     Fixed issue with rule: “sf:AvoidGlobalModifier” {where CodeScan is flagging a false positive}

Some users have reported that CodeScan was throwing an error related to usage of a global class on the highlighted line, where the inner class CustomWrapper is defined.

<figure><img src="../../../../../.gitbook/assets/image (1813).png" alt=""><figcaption></figcaption></figure>

Since the GET() is annotated with @HttpGet, it must be set as global static as per Salesforce rules.

(See [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_http_get.htm) for more info.)

Since the return type of GET() is a custom wrapper type, the wrapper class also must be declared as global. If not, the compilation error will be thrown.

This fix addresses that false positive in the 'sf:AvoidGlobalModifier' rule. The violation is now ignored for global classes used as return types in any global static method.

&#x20;

12\.    Fixed error in scanning apex classes in SQ 25.1.0

Some users have reported that CodeScan reports an error in the logs (although the analysis is successful, there is a corresponding error in the log.)

<figure><img src="../../../../../.gitbook/assets/image (1814).png" alt=""><figcaption></figcaption></figure>

This was being caused by metrics that had been deprecated.  This fix removes those deprecated metrics.&#x20;

Verified the analysis on SQ-25.1.0 v with the latest CodeScan jars provided.  Confirmed that users no longer see the error in the logs when the analysis is successful (working as expected).

<figure><img src="../../../../../.gitbook/assets/image (1815).png" alt=""><figcaption></figcaption></figure>

