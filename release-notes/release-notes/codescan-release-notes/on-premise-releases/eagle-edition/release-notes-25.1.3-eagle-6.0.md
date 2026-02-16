# Release Notes 25.1.3 Eagle 6.0

## CodeScan Self-Hosted Release Notes 25.1.3 Eagle 6.0

**Release Date: 28 December 2025**

### Summary

CodeScan Self-Hosted (version 25.1.3 (Eagle v6) is comprised of the following 25 components:

* 1 New Feature
* 15 Rule Enhancements
* 2 Rule Deprecations
* 7 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

**1.     New Rules to Identify Potential Sensitive Data/PII Fields**

**Description**

These rules identify potential sensitive data and Personally Identifiable Information (PII) fields within the Salesforce Apex code. This helps organizations ensure these fields are handled securely and comply with data privacy regulations.

**Hypothesis**

By implementing these rules to identify potential sensitive PII fields, CodeScan can identify and address security risks associated with handling sensitive PII data in Salesforce.

CodeScan Sensitive Data Scanning uses regular expression patterns to search for potential sensitive PII field names. It looks for common identifiers listed below and some custom objects/fields, such as "name," "social\_security\_number," "credit\_card," or "passport," and determines if they are being assigned string literals or used in an insecure way (exposed in debug).

<table><thead><tr><th width="229" valign="top">Object</th><th valign="top">Fields Likely to Contain PII</th></tr></thead><tbody><tr><td valign="top">Contact</td><td valign="top">Birthdate, Department, Email, Fax, FirstName, HomePhone, LastName, MailingAddress, MiddleName, MobilePhone, Name, OtherAddress, OtherPhone, Phone, PhotoUrl, Title</td></tr><tr><td valign="top">Lead</td><td valign="top">Address, Company, Email, Fax, FirstName, Industry, LastName, MiddleName, MobilePhone, Name, Phone, PhotoUrl, Title, Website</td></tr><tr><td valign="top">User</td><td valign="top">Address, CompanyName, Department, Email, Fax, FederationIdentifier, FirstName, FullPhotoUrl, LastName, MiddleName, MobilePhone, Name, Phone, Title, Username</td></tr><tr><td valign="top">Account (Business)</td><td valign="top">BillingAddress, Fax, Name, Phone, PhotoUrl, ShippingAddress</td></tr><tr><td valign="top">Account (Person Account Fields)</td><td valign="top">FirstName, LastName, MiddleName, PersonBirthDate, PersonEmail, PersonHomePhone, PersonMailingAddress, PersonMobilePhone, PersonOtherPhone, PersonTitle</td></tr></tbody></table>

_NOTE: We implemented advanced logic to Ignore Violations on Dummy/Masked data as shown below:_

<table data-header-hidden><thead><tr><th width="145" valign="top">Data Type</th><th width="247" valign="top">Original / Real PII (Violation)</th><th valign="top">Dummy / Masked Data (Compliant)</th></tr></thead><tbody><tr><td valign="top">Email</td><td valign="top">john.doe@company.com</td><td valign="top">test.user@example.test</td></tr><tr><td valign="top">Phone</td><td valign="top">9876543210</td><td valign="top">5551234567 or 0000000000</td></tr><tr><td valign="top">SSN</td><td valign="top">123-45-6789</td><td valign="top">000-00-0000 or null</td></tr><tr><td valign="top">Credit Card</td><td valign="top">4111111111111234</td><td valign="top">4111111111111111 (Visa test number)</td></tr><tr><td valign="top">Address</td><td valign="top">123 Main Street, New York</td><td valign="top">123 Test Street, Test City</td></tr><tr><td valign="top">Logs</td><td valign="top">System.debug('Email: jane@corp.com')</td><td valign="top">System.debug('Email: [REDACTED]')</td></tr></tbody></table>

**Value/Purpose**

The purpose of this user story is to enhance data privacy and security within our Salesforce organization. By identifying potential sensitive PII fields, we can improve data governance and minimize the chances of data breaches.

**Acceptance Criteria**

Name: Identify Potential Sensitive PII Fields\
Key: SecurePIIFields\
Description: Certain standard Salesforce objects (such as Contact, Lead, User, Account, Person Account, and Opportunity) contain fields that may hold Personally Identifiable Information (PII), including names, addresses, phone numbers, emails, birthdates, and other identifiers. These fields must be treated as sensitive data and protected in compliance with privacy and security regulations (e.g., GDPR, CCPA, HIPAA).

NOTE: To fully maximize the value of these rules, you can also configure them to include custom fields as parameters (e.g., SSN, Social\_Security\_Number, Credit\_Card, Passport).

Ensure these fields are handled securely through encryption, masking, and strict access controls to minimize the risk of data exposure or breaches.\
Type: Vulnerability\
Severity: Major\
Message: Potential sensitive PII field detected. Ensure that this field is handled securely.\
Tags: Security\
Parameters:\
Name: sensitiveFields\
Description: A comma-separated list of sensitive custom fields. Add any custom fields you would like to monitor with this rule.

Verified that sf:SecurePIIFields rules are being triggered in following scenarios:

* Verified the sf:SecurePIIFields rules by activating these rules in a specified Quality Profile. The Project analysis should trigger the violation (Security Hotspot).
* Verified by giving custom parameters (ssn, credit\_card, passport) and validated that they are working as expected.
* Verified by sending both string and integer value for credit\_card.

<figure><img src="../../../../../.gitbook/assets/image (2291).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2292).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

**1.  Updated the description in the CodeScan APEX rule “Server Side Request Forgery (SSRF)”**

**{Rule ID: sf: ServerSideRequestForgery}**

**Description:**

Update the issue description for the sf:ServerSideRequestForgery rule to include data flow information once tracking is implemented.

Highlight how untrusted user input influences outbound requests or endpoint URLs used in HttpRequest.setEndpoint() or similar methods.&#x20;

**Hypothesis:**\
Providing a traceable flow from input source to request endpoint will help developers clearly identify unsafe URL usage leading to SSRF vulnerabilities.

**Value/Purpose:**\
Improves clarity and helps prioritize high-risk SSRF issues by showing the complete journey of untrusted data to outbound request logic.

&#x20;

**Code Example**:

public class Negative {

&#x20; public void otherMethod() {

&#x20;   String oneMore = 'somethingHere';

&#x20;   init(oneMore);

&#x20; }

&#x20;

&#x20; public PageReference init(String Lastname){

&#x20;     String FirstName = getName();

&#x20;     try {

&#x20;       HttpRequest req = new HttpRequest();

&#x20;       req.setEndpoint('callout:Third\_Party\_Authorization/v1'+Lastname);

&#x20;       request.setMethod ('POST');

&#x20;     }

&#x20; }

}

#### Existing Message:

Sanitize input to avoid possible SSRF.  Data Flow Trace: Negative.otherMethod: line 4&#x20;

#### Updated Message:

Sanitize input to avoid possible SSRF.  Data Flow Trace -

&#x20;   CALL (Negative.otherMethod: line 4)

&#x20;

Make sure to check for internal methods also (e.g., FirstName variable on line 8 if used in the set endpoint call on line 11).

<figure><img src="../../../../../.gitbook/assets/image (2293).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../../../../.gitbook/assets/image (2294).png" alt=""><figcaption></figcaption></figure>

**2.     Updated the description in the CodeScan APEX rule “Resource Injection” to account detection with Source-to-Sink Tracing {Rule ID: sf: ResourceInjection}**

**Description:**

Update the issue description for sf:ResourceInjection to display how untrusted input propagates to resource-loading statements, such as dynamic resource identifiers or file references.\
The new description should include the identified source and sink with a trace of intermediate transformations.

**Hypothesis:**\
If developers can visualize which variable or parameter is used to form a resource path without sanitization, they will better understand the exploit path and fix it faster.

**Value/Purpose:**\
Increases the usability and accuracy of Resource Injection findings by offering transparent, contextual information about the data flow chain.

**Acceptance Criteria**

Sanitize input to avoid possible resource injection. Data Flow Trace : {Class.method}: line {line number} --> {Class.method}: line {line number}

Example:

Sanitize input to avoid possible resource injection. Data Flow Trace : APIVersionsRetiredTrigger.processOldAPIVersionReferences: line 88 --> APIVersionsRetiredTrigger.processOldAPIVersionReferences: line 92Top of Form

**Code Example:**

public class Negative {

&#x20; public void otherMethod() {

&#x20;   String oneMore = 'somethingHere';

&#x20;   init(oneMore);

&#x20; }

&#x20;public PageReference init(String Lastname){

&#x20;     String FirstName = getName();

&#x20;     try {

&#x20;       HttpRequest req = new HttpRequest();

&#x20;       req.setEndpoint('/Third\_Party\_Authorization/v1'+Lastname);

&#x20;       request.setMethod ('POST');

&#x20;     }

&#x20; }

}

**Existing Message**:

Sanitize input to avoid possible resource injection.  Data Flow Trace: Negative.otherMethod: line 4

**Updated Message**:

Sanitize input to avoid possible resource injection. Data Flow Trace -

&#x20;   CALL (Negative.otherMethod: line 4)

Make sure to check for internal methods also (E.g. FirstName variable on line 8 if used in the set endpoint call on line 11)

<figure><img src="../../../../../.gitbook/assets/image (2295).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2296).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2297).png" alt=""><figcaption></figcaption></figure>

**3.     Updated the description in the CodeScan APEX rule “Avoid Calling SOQL and DML Inside Loops”**

**{Rule ID: sf:AvoidSoqlInLoops}**

**Description:**

Refine the issue description for sf:AvoidSoqlInLoops to clearly identify the loop structure and the query being executed inside it.  Include variable references and contextual flow details showing how data or parameters within the loop lead to repeated queries.

**Hypothesis:**

Providing contextual information about where and how SOQL queries are invoked within loops will improve developer understanding and reduce rework in optimizing code performance.

**Value/Purpose:**

Enhances readability and educational value of performance warnings by showing contextual flow, helping developers refactor code more efficiently.  Top of Form

Update the issue description for the sf:ServerSideRequestForgery rule to include data flow information once tracking is implemented.

**Acceptance Criteria:**

public class CaseProcessor {

&#x20;    public void processAllCases(List\<Case> caseList) {

&#x20;       // LOOP

&#x20;       for (Case c : caseList) {

&#x20;           processCase(c);                     // hop 1

&#x20;       }

&#x20;   }

&#x20;

&#x20;   void processCase(Case c) {

&#x20;       fetchOwnerDetails(c.OwnerId);           // hop 2

&#x20;   }

&#x20;

&#x20;   List\<User> fetchOwnerDetails(Id ownerId) {

&#x20;       return \[

&#x20;           SELECT Id, Name FROM User

&#x20;           WHERE Id = :ownerId                // SINK (SOQL)

&#x20;       ];

&#x20;   }

}

&#x20;

**Existing Message**:

Avoid running Soql and DML inside loops.  Loop Trace : CaseProcessor.fetchOwnerDetails: line 16 --> CaseProcessor.processCase: line 11 --> CaseProcessor.processAllCases: line 6

&#x20;

**Updated Message**:

Avoid Running SOQL and DML inside loops. Data Flow Trace -

&#x20; SOQL (CaseProcessor.fetchOwnerDetails: line 16) -->

&#x20; CALL (CaseProcessor.processCase: line 11) -->

&#x20; LOOP (CaseProcessor.processAllCases: line 6)

&#x20;

Executed the Above scenario and validated the rule description was updated as expected.

* Verified the updated behavior of the sf:AvoidSoqlInLoops rule.
* Multi-hop scenarios (loop → method → method → SOQL) correctly show the full Data Flow Trace with SOQL → CALL → LOOP.
* Direct SOQL-in-loop scenarios correctly show the simplified message, which is the expected behavior.



<figure><img src="../../../../../.gitbook/assets/image (2299).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../../../../.gitbook/assets/image (2300).png" alt=""><figcaption></figcaption></figure>

**4.     Enhanced the logic in the CodeScan rule “Unnecessary Boolean Assertion”**

**{Rule ID: sf:UnnecessaryBooleanAssertion}**

Several customers have reported that the current rule detects unnecessary boolean assertions only when using the System.assert() method.

However, it does not flag similar patterns when assertions are made through the Assert class methods such as Assert.isTrue(true) or Assert.isFalse(false).

To improve coverage, we enhanced the rule logic to include these Assert class scenarios, ensuring consistency across both assertion types.

**Fix Summary**

* Extended the rule logic to detect unnecessary boolean assertions in the following cases:
  * Assert.isTrue(true)
  * Assert.isFalse(false)
* Updated the rule message and description to clearly explain why these patterns are redundant.

**Updated Rule Description**:&#x20;

A Unit test assertion with a Boolean literal is unnecessary since it always will evaluate to the same thing. Consider using flow control (in case of assertTrue(false) or similar) or simply removing statements like System.assert(true) and Assert.isFalse(false).\
\
If you just want a test to halt after finding an error, use the System.assert(false, 'message') or Assert.isFalse(false, 'message') methods and provide an indication message of why it did.

<figure><img src="../../../../../.gitbook/assets/image (2301).png" alt=""><figcaption></figcaption></figure>

&#x20;Verified the following scenarios are working as expected:

* Noncompliant scenarios using System.assert(true), Assert.isTrue(true), and Assert.isFalse(false). All were correctly flagged as expected.
* Compliant scenarios have been tested. (by using only string values).

<figure><img src="../../../../../.gitbook/assets/image (2302).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../../../../../.gitbook/assets/image (2303).png" alt=""><figcaption></figcaption></figure>

**5.     Enhanced God Class Rule by adding parameters  {Rule ID: sf:GodClass}**

The sf:GodClass rule currently uses fixed threshold values to identify “God Class” design flaws:

* WMC (Weighted Methods Count): > 47
* ATFD (Access to Foreign Data): > 5
* TCC (Tight Class Cohesion): < 1/3 (33%)

These thresholds are hardcoded and not configurable. We decided to introduce parameters to allow users to customize these values based on their project requirements.  By making these thresholds configurable, users can fine-tune the rule according to their project’s code complexity and quality standards, reducing false positives and improving detection accuracy.

**Value / Purpose:**

* Enables users to adjust thresholds to better match their codebase.
* Improves usability and flexibility of the rule.
* Increases adoption by making the rule adaptable to various team standards.

<figure><img src="../../../../../.gitbook/assets/image (2304).png" alt=""><figcaption></figcaption></figure>

Verified the sf:GodClass by validating that users are able to see the violations as expected for the below scenarios

When users provide the following Threshold values:

* wmc=47, atfd=5, tcc=0.33                      Result: Violation
* wmc=10, atfd=5, tcc=0.50                      Result: Violation
* wmc=60, atfd=10, tcc=0.90                    Result: Violation
* wmc=30, atfd=2, tcc=0.8                       Result: Violation

&#x20;

* wmc=100, atfd=10, tcc=0.2                    Result: No violation
* wmc=9999, atfd=9999, tcc=0                 Result: No violation
* wmc=0, atfd=0, tcc=0                            Result: No violation

&#x20;

* wmc=0, atfd=0, tcc=1                            Result: Everything violates

<figure><img src="../../../../../.gitbook/assets/image (2305).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2306).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2307).png" alt=""><figcaption></figcaption></figure>

**6.     Updated the rule description for “God Class Rule” {Rule ID: sf:GodClass}**

**Description:**

The God Class rule detects the God Class design flaw using metrics. God classes do too many things, are very big and overly complex. They should be split apart to be more object-oriented.\
The rule uses the detection strategy described in "Object-Oriented Metrics in Practice".

The God Class rule evaluates classes using the following three key metrics to determine size, dependency, and cohesion:

1. WMC (Weighted Methods Count): Measures the number and complexity of methods in a class. A high WMC indicates that a class has too many methods or overly complex behavior.
2. ATFD (Access to Foreign Data): Counts how many times a class accesses data from other classes. A high ATFD means the class is overly dependent on external data, reducing modularity.
3. TCC (Tight Class Cohesion): Represents how closely the methods of a class are related to each other. A low TCC suggests poor internal cohesion, meaning the class handles unrelated responsibilities.

Every violation will include three metrics: (configurable):

* WMC : default > 47
* ATFD : default > 5
* TCC : default < 1/3 (33%)

The violations are reported against the entire class.

Note: For more information, please refer to Michele Lanza and Radu Marinescu. Object-Oriented Metrics in Practice: Using Software Metrics to Characterize, Evaluate, and Improve the Design\
of Object-Oriented Systems {Springer, Berlin, 1 edition, October 2006. Page 80}.

Verified the Updated God Class Rule Description and confirmed that users are able to see the updated description for the rule.

<figure><img src="../../../../../.gitbook/assets/image (2308).png" alt=""><figcaption></figcaption></figure>

**7.     Updated the Rule Description for rule "em" Tags Should Be Used Instead of "i" {Rule ID: vf:ItalicTagsCheck}**&#x20;

We recognized that this description was out of date and determined it needed to change to:

“The \<strong>/\<b> and \<em>/\<i> tags have exactly the same effect in most web browsers, but there is a fundamental difference between them: \<strong> and \<em> have a semantic meaning whereas \<b> and \<i> only convey styling information like CSS.

When \<b> can have simply no effect on a device with limited display or when a screen reader software is used by a visually impaired person, \<strong> will:

* Underline the characters on a phone or tablet
* Speak with lower tone when using a screen reader
* Display the text as bold in normal browsers

Consequently:

* In order to convey semantics, the \<b> and \<i> tags shall never be used,
* In order to convey styling information, the \<b> and \<i> should be avoided and CSS should be used instead.

Verified the rule description and confirmed that the updated description is displayed as expected.

<figure><img src="../../../../../.gitbook/assets/image (2309).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2310).png" alt=""><figcaption></figcaption></figure>

**8. Updated the Rule Description and Example for rule “Check for Lightning Migration Issues for Salesforce.com and Force.com Links” {Rule ID: vf:LightningAvoidHardcodedSalesforceDomain}**

This rule was updated with this new description and example:

“URL references may not work as expected in Lightning Experience or if you decide to swap to My Domain. If you decide to use My Domain, you have to replace hard-coded references to your original URL with references to your new domain. Using something like {!Site.BaseUrl} will avoid this hassle.

See: [Considerations Before Transitioning to Lightning Experience](https://resources.docs.salesforce.com/198/latest/en-us/sfdc/pdf/lex_considerations.pdf)”

Example:

![](https://internal-kb.autorabit.com/~gitbook/image?url=https%3A%2F%2F3078893355-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FsVI1KPpGaAiGiskLR12x%252Fuploads%252FNaUaCdibOr99gGX5pLTA%252Fimage.png%3Falt%3Dmedia%26token%3De9253ae6-c4b9-4149-b535-fc878d34c0bc\&width=768\&dpr=4\&quality=100\&sign=35b71da9\&sv=2)

Verified these rules updated by confirming that users are able to see the updated description and the example.<br>

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

**9.   Enhanced rule “Field Level Security” {Rule ID: sf:FieldLevelSecurity}**

Previously, CodeScan did not raise violations if a method matched the condition:

<figure><img src="../../../../../.gitbook/assets/unknown (18).png" alt=""><figcaption></figcaption></figure>

This exception was originally introduced to reduce noise and was added to our rule logic before Salesforce introduced USER\_MODE. However, with Salesforce’s updated guidance requiring all database operations to consistently enforce permissions, the exemption is no longer valid. Getters can still expose data through bindings, so excluding them would not align with best practices.

Now, DML operations in getter methods that do not enforce permissions (e.g., without USER\_MODE) will correctly raise violations.

\
&#xNAN;_&#x4E;ote:_ _The update has been refined to cover all scenarios — we’ve implemented logic to trigger violations for all getter method cases where there is no permission check, SOQL, or DML operation, and removed the previous conditional checks. As a result, violations will now be raised for every return type except_ void _(since it doesn’t return any value).  Please note that due to these rule changes, there may be a slight increase/decrease in reported issues for the FLS rule._

We have verified the rule logic and validated that users are able to see the violations for the getter methods on SOQL, DML operations.

&#x20;

<figure><img src="../../../../../.gitbook/assets/image (2311).png" alt=""><figcaption></figcaption></figure>

**10.  Enhanced rule “Aura Controller Naming Convention” {Rule ID: sf:AuraControllerNaming}**

Previously, CodeScan Controller Suffix in the rule Aura Controller Naming Convention was incorrectly case sensitive.  This meant that a violation was not triggered (expected behavior) when the suffix to controller (lowercase).  However, if the class name instead included "Controller" (uppercase), a violation was being thrown (i.e., when we set ControllerSuffix = Controller).

Verified the below scenarios and validated that both are working as expected:

* ControllerSuffix = "Controller"
* ControllerSuffix = "controller"

Further verified the sf:AuraControllerNaming rule by setting ControllerSuffix = “Controller” in first run of Project and then changed ControllerSuffix to “controller”. Both projects triggered the same number of violations based on the provided data.

**11.  Updated the rule descriptions for “CodeScan Other Rules” {Rule ID: cs-vf:unknown and Rule ID: cs-js:unknown}**

We have updated the rule description for the rule "CodeScan Other Rules" rule key

**Updated Description**:

This rule detects ESLint rule references written in code comments that are not currently recognized by the plugin. It helps identify placeholder or upcoming rules that may be added in future updates.

We have verified the Rule Description Updates on “CodeScan Other Rules (cs-vf:unknown and cs-js:unknown) and confirmed that users are able to see the updated descriptions.

<figure><img src="../../../../../.gitbook/assets/image (2312).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2313).png" alt=""><figcaption></figcaption></figure>

**12.   Enhancement to “sf:AvoidLogicInTrigger” Rule**

Historically, this rule finds any blocks of code in a trigger and throws a violation.

In this enhancement, we added a parameter to the rule allowing users to add a comma separated list of trigger frameworks that are allowed.

The new parameter is “allowedTriggerFrameworks”

Description: A comma separated list of Trigger frameworks to allow. Violations will still be reported if complex logic is present within the allowed parameters.

For more information, please review an overview of triggerframeworks: [https://www.saasguru.co/salesforce-trigger-frameworks-guide/?srsltid=AfmBOopNA\_BxSsI\_tjZ1EGP3n59fi-\_TW5Q-TQaoFFv1tIIYKZEyDJ5f](https://www.saasguru.co/salesforce-trigger-frameworks-guide/?srsltid=AfmBOopNA_BxSsI_tjZ1EGP3n59fi-_TW5Q-TQaoFFv1tIIYKZEyDJ5f)

Details of the new parameter:

* Allow:
* Trigger.is\* checks
* Direct calls to whitelisted methods/properties (including inside conditions or assignments).
* Flag:
* Any iteration (for, while, do) in a trigger is a violation, regardless of whitelist.
* Any non-whitelisted method calls.
* Any direct DML, SOQL, or field logic.
* Variables assigned from whitelisted methods used later in invalid contexts (like while(var)).

Verified the new parameter on the sf:AvoidLogicInTrigger rule to ensure compatibility with trigger frameworks via the following scenarios:

1\. Any control statement with {} (e.g., if, for, switch) in trigger body → Violation.\
\
2\. Exception: if that uses Trigger.is… → No Violation.\
However, if Trigger.is… appears inside a for loop, it’s still a Violation.\
\
3\. If a method is added to the rule parameter (allow-list) (e.g., checkPermission), then an if using it → No Violation.\
But: for, while, do-while, SOQL, DML → always Violation (allow-list does not suppress these).

But: for, while, do-while, SOQL, DML → always Violation (allow-list does not suppress these).

<figure><img src="../../../../../.gitbook/assets/image (2314).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2315).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2316).png" alt=""><figcaption></figcaption></figure>

**13.     Enhancement to “Use Annotation on Test Class” Rule**

During our routine testing of our rules, we noted that this rule is outdated, as it only detects the testMethod keyword.  It does not work with the newer @IsTest annotation, causing missed violations in modern Apex test classes.

**Fix:**\
Updated the rule logic to support detection of @IsTest annotation on test classes, ensuring compliance with current Apex best practices

Verified the enhanced rule logic in “Use Annotation on Test Class” via on the the below scenarios

1. A non-test class or Utility class without test methods → Verified: No violation raised.
2. @IsTest annotated class with test methods (@IsTest and/or testMethod) → Verified: No violation raised.
3. Class containing only testMethod methods without @IsTest → Verified: Violation raised.
4. Class containing only @IsTest methods without class-level @IsTest → Verified: Violation raised.

<figure><img src="../../../../../.gitbook/assets/image (2317).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2318).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2319).png" alt=""><figcaption></figcaption></figure>

**14.  Enhancement to sf:ServerSideRequestForgery Rule**

As part of the CodeScan 25.1.2 release (June 2025), we added this new rule (Server Side Request Forgery).  We have had several customers request an enhancement to this rule, as they reported that this rule was not catching all of the SSRF issues.

As such, we have enhanced this rule to find all the sinks for these issues with concatenated URLs to all methods that take an HttpRequest as an input.

This is the list of methods we have added as sinks (these are in addition to the issues that this rule is  currently finding)\
\
Http.send(HttpRequest)\
HttpRequest.setEndpoint(String)\
Continuation.addHttpRequest(HttpRequest)\
PageReference.getContent()

Verified that the rule ServerSideRequestForgery is throwing violations when the following methods are used in the code:

* HttpRequest.setEndpoint(String)
* PageReference.getContent()

<figure><img src="../../../../../.gitbook/assets/image (2320).png" alt=""><figcaption></figcaption></figure>

**15.     Enhancement to Resource Injection Rule**

As part of the CodeScan 25.1.2 release (June 2025), we added this new rule (Resource Injection).  We have had several customers request an enhancement to this rule, as they reported that this rule was not catching all of the issues.

As such, we have enhanced this rule to find all the sinks for these issues with concatenated URLs to all methods that take an HttpRequest as an input.

This is the list of methods we have added as sinks (these are in addition to the issues that this rule is  currently finding)\
\
Http.send(HttpRequest)\
HttpRequest.setEndpoint(String)\
Continuation.addHttpRequest(HttpRequest)\
PageReference.getContent()

Verified that the rule Resource Injection is throwing violations when the following methods are used in the code:

* HttpRequest.setEndpoint(String)
* PageReference.getContent()

<figure><img src="../../../../../.gitbook/assets/image (2321).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2322).png" alt=""><figcaption></figcaption></figure>

### Rule Deprecations

**1.     Deprecation of 2 rules for “disallow irregular whitespace outside of strings and comments” (one for Visualforce and one for JavaScript) {Rule ID: cs-vf:no-irregular-whitespace and Rule ID: cs-js:no-irregular-whitespace}**

The reason these rules are being deprecated is because they do not fire before the parser catches the issue. These types of irregular white space are no longer even seen as parsing JavaScript.

Further, we have updated the descriptions for these rules to include:&#x20;

“This rule has been deprecated due to these types of white space being caught by the JavaScript parser before a rule can be fired.  Please make sure you have the cs-js:exception rule in your javascript Quality Profile to be made aware of these errors.”

Verified the Rule Deprecations of cs-vf:no-irregular-whitespace and cs-js:no-irregular-whitespace and confirmed users are able to see the updated status as Deprecated and the updated description for these rules.

<figure><img src="../../../../../.gitbook/assets/image (2323).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2324).png" alt=""><figcaption></figcaption></figure>

**2.   Deprecation of 2 rules for “disallow octal escape sequences in string literals” (one for Visualforce and one for JavaScript) {Rule ID: cs-vf:no-octal-escape and Rule ID: cs-js:no-octal-escape}**

The reason these rules are being deprecated is because they do not fire before the parser catches the issue. These types of octal escapes are no longer even seen as parsing JavaScript.

Further, we have updated the descriptions for these rules to include:&#x20;

“This rule has been deprecated due to these types of octal escapes being caught by the JavaScript parser before a rule can be fired.  Please make sure you have the cs-js:exception rule in your javascript Quality Profile to be made aware of these errors.”

Verified the Rule Deprecation for cs-vf:no-octal-escape and cs-js:no-octal-escape and confirmed users are able to see the updated status as Deprecated and the updated description for these rules.

<figure><img src="../../../../../.gitbook/assets/image (2325).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2326).png" alt=""><figcaption></figcaption></figure>

### Fixes&#x20;

**1.  Fixed an issue in the APEX rule “Field Level Security Vulnerabilities”**

{Rule ID: sf:FieldLevelSecurity}

Several customers reported that they were receiving the error message “Permissions should be checked before accessing resource SObject” even though they were providing suitable permissions using DML and/or SOQL statements.  It was determined that CodeScan was not recognizing both DML and SOQL statements.  As such, we overhauled the rule logic to address this issue and have ensured that CodeScan is now recognizing the AccessLevel.\* commands in DML calls.

We have validated this new logic and verified that no vulnerabilities were raised (which is the expected and correct behavior for this updated rule logic).

<figure><img src="../../../../../.gitbook/assets/image (2327).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2328).png" alt=""><figcaption></figcaption></figure>

**2.     Fixed an issue in the APEX rule “Resource Injection”**

{Rule ID: sf: ResourceInjection}

Resource injections occur when user-controllable data is used to specify a resource identifier without proper validation.  This rule identifies potential resource injection vulnerabilities by detecting unsafe URL construction for internal network requests.  Input can be cleansed by using Id.valueOf, Date.valueOf, etc. Or escaped using String.escapeSingleQuotes().

However, several customers reported that this rule was firing improperly, even when the recommended methods have been applied.  After reviewing, we confirmed cases of false positives and determined that the rule required a minor update to the rule logic.

We verified the new logic and validated that the rule is now working as originally designed.

<figure><img src="../../../../../.gitbook/assets/image (2329).png" alt=""><figcaption></figcaption></figure>

**3.  Fixed an issue in the APEX rule “URLs of Salesforce pages should be relative, not absolute”**

{Rule ID: sf:AvoidAbsoluteURL}

During our routine, internal rule evaluation process, we discovered that this rule wasn’t firing as expected. As such, we overhauled the rule logic to address this issue.

Updated the rule to detect and flag violations for URLs matching the following patterns:

* \*.salesforce.com
* \*.force.com
* \*.site.com
* \*.documentforce.com
* \*.marketingcloudapis.com

Verified the updated logic to the rule AvoidAbsoluteURL by validating that the usage of any of these URLs in the code now trigger violations after activating the AvoidAbsoluteURL rule.

* \*.salesforce.com
* \*.force.com
* \*.site.com
* \*.documentforce.com
* \*.marketingcloudapis.com

<figure><img src="../../../../../.gitbook/assets/image (2330).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2331).png" alt=""><figcaption></figcaption></figure>

**4.     Fixed an issue in the rule “Require CSRF Protection On GET Requests”**

{Rule ID: vf:RequireConfirmationToken}

During our routine, internal rule evaluation process, we discovered that this rule wasn’t firing as expected.  As such, we overhauled the rule logic to address this issue.

**Summary**:

The current xpath for this rule is:

//Document//Element\[@Name='confirmationtokenrequired']\[Text\[@Image='false']]

We recognize that this will not work as expected, as the confirmation token is actually in the metadata of the page and the tag is in camel-case (confirmationTokenRequired)\\

The logic was updated to:

//Document//Element\[lower-case(@Name)='confirmationtokenrequired']\[Text\[@Image='false']]

With this enhancement, the rule will:

* find the correct tag
* look in the page-meta.xml metadata file (not the page itself)

Verified the below scenarios and confirmed that the updated rule logic is working as expected.

_“vf:RequireConfirmationToken” getting triggered only_ when the corresponding meta.xml has false for ConfirmationToken tag .

* Verified the rule behavior using by uploading only page file and then with corresponding meta.xml file with true and meta.xml file with false.

<figure><img src="../../../../../.gitbook/assets/image (2332).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2333).png" alt=""><figcaption></figcaption></figure>

**5.   Fixed an issue in the rule “Switch statements should not have too many case clauses”**

{Rule ID: sf:MaximumNumberOfCase }

Some customers have reported that this rule throws out of bounds exceptions.  Upon investigation, we determined that this is caused by an empty switch statement, which manifests as a parser error when this class is added in Salesforce.

The aim of fix is to make sure that the CodeScan parser sees empty switch statements as syntax errors.

Verified that the below scenarios are working as expected.

* Verified that the rule does not throw out of bounds exceptions in the analysis logs (it should not throw this and, as such, has been validated as working as expected).
* Verified “sf:MaximumNumberOfCase” rule is triggered only when the maximum limit is exceeded.

<figure><img src="../../../../../.gitbook/assets/image (2334).png" alt=""><figcaption></figcaption></figure>

**6.  Fixed an issue in the rule “Immutable Field”, which was causing false positives {Rule ID: sf:ImmutableField}**

Several customers have reported that the current rule logic incorrectly flags propertyVal as a candidate for final, even though its value can be modified indirectly through a property getter/setter. In the following example, the field propertyVal is updated within the getter of anotherPropertyVal via this.propertyVal = 'test' and subsequently returned:

Example code:

<figure><img src="../../../../../.gitbook/assets/image (2335).png" alt=""><figcaption></figcaption></figure>

**Expected Behavior:**\
The rule should not raise a violation when the private field’s value can be modified through class property accessors (get/set methods) or other internal logic. Such fields are not immutable, and marking them as final would cause compilation errors

Verified that the “sf:ImmutableField” is getting triggered only when the private field’s value cannot be modified.  Further, we verified the rule behavior using both mutable and immutable field patterns.

<figure><img src="../../../../../.gitbook/assets/image (2336).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2337).png" alt=""><figcaption></figcaption></figure>

**7.     Fixed an issue in the rule “Type Reflection Is Security Sensitive” {Rule ID: sf:HotspotTypeReflection}**

During our routine, internal rule evaluation process, we discovered that this rule wasn’t firing as expected.  As such, we overhauled the rule logic to address this issue.

Verified the sf:HotspotTypeReflection rule by activating the rule in a specified Quality Profile. Then, in a subsequent project analysis, validated that the rule is now working as expected.

<figure><img src="../../../../../.gitbook/assets/image (2338).png" alt=""><figcaption></figcaption></figure>

