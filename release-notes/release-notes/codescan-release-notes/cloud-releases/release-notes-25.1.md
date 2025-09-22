---
description: CodeScan Cloud Release Notes
---

# Cloud Release Notes 25.1

## Integration Requirements for CodeScan v25.1.0+

Please note that there are updated requirements for customers who are using one or more of the following to integrate with CodeScan:

* SFDX
* SonarScanner
* ADO
* VS Code
* IntelliJ&#x20;

[**Please refer to our integration requirements page for further details.**](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/integration-requirements)

***

## CodeScan Release 25.1.10&#x20;

**Release Date: 21 September 2025**

### Summary

CodeScan 25.1.10 is comprised of the following 9 components:

* 1 New Feature
* 8 Rule Enhancements

Component details are listed in their corresponding sections within this document.

### New Features

1. CodeScan now imposes verification logic on email signup to enhance security. Previously, users were able to register and log in without verifying their email.  We recognize that this could potentially lead to the creation of fake or fraudulent accounts. In this release, we have implemented an email verification via unique links to a one-time verification link.  Additionally, we have added logic that restricts access to functionalities for unverified accounts.\
   \
   Verified the Migrate email verification Rule to Action in Auth0 via the following scenarios:\
   After signing up, the user receives a verification email. Only after successfully verifying the account, the user is able to log in to the instance as expected.

<figure><img src="../../../../.gitbook/assets/image (2021).png" alt="" width="359"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2022).png" alt="" width="354"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2023).png" alt="" width="185"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2024).png" alt=""><figcaption></figcaption></figure>

### Rule Enhancements

1. **Enhancement to sf:ServerSideRequestForgery Rule**\
   As part of the CodeScan 25.1.2 release (June 2025), we added this new rule (Server Side Request Forgery).  We have had several customers request an enhancement to this rule, as they reported that this rule was not catching all of the SSRF issues.\
   \
   As such, we have enhanced this rule to find all the sinks for these issues with concatenated URLs to all methods that take an HttpRequest as an input.\
   \
   This is the list of methods we have added as sinks (these are in addition to the issues that this rule is  currently finding):

* Http.send(HttpRequest)
* HttpRequest.setEndpoint(String)
* Continuation.addHttpRequest(HttpRequest)
* PageReference.getContent()\
  \
  Verified that the rule ServerSideRequestForgery is throwing violations when the following methods are used in the code:
* HttpRequest.setEndpoint(String)
* PageReference.getContent()\


2. **Enhancement to Resource Injection Rule**\
   As part of the CodeScan 25.1.2 release (June 2025), we added this new rule (Resource Injection). We have had several customers request an enhancement to this rule, as they reported that this rule was not catching all of the issues.\
   \
   As such, we have enhanced this rule to find all the sinks for these issues with concatenated URLs to all methods that take an HttpRequest as an input.\
   \
   This is the list of methods we have added as sinks (these are in addition to the issues that this rule is  currently finding):

* Http.send(HttpRequest)
* HttpRequest.setEndpoint(String)
* Continuation.addHttpRequest(HttpRequest)
* PageReference.getContent()\
  \
  Verified that the rule Resource Injection is throwing violations when the following methods are used in the code:
* HttpRequest.setEndpoint(String)
* PageReference.getContent()

<figure><img src="../../../../.gitbook/assets/image (2025).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2026).png" alt=""><figcaption></figcaption></figure>

3. **Enhancement to “Switch Statements Should Have a When Else Case” Rule**\
   Currently, the rule is not working as expected, as it does not raise violations when a switch statement lacks a when-else block. We have modified that logic to correctly identify switch statements that are missing a when-else case so that users can ensure the code is more robust, future-proof, and does not miss handling unexpected cases.\
   \
   Example:

<figure><img src="../../../../.gitbook/assets/image (2027).png" alt="" width="254"><figcaption></figcaption></figure>

Verified that the updated rule now correctly flags switch statements without a when-else block, ensuring violations are raised consistently for missing default cases.

<figure><img src="../../../../.gitbook/assets/image (2028).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2029).png" alt=""><figcaption></figcaption></figure>

4. **Enhancement to “Avoid Reversed Operators” Rule**\
   Modified the rule logic to correctly detect and report improper usage of reversed operators (=-, =+) in Apex code, so that users can avoid mistakes where variables are unexpectedly reassigned rather than incremented/decremented.\
   \
   **Current Behavior:**

* Violations are not raised when using reversed operators like target =- num; or target =+ num;.\
  \
  **Expected Behavior:**
* The rule should detect and flag cases of reversed operators (=-, =+) and provide a clear violation message.
*   The violation message should explain the confusion:

    * x =- y; assigns -y instead of subtracting.
    * x =+ y; assigns +y instead of adding.

    This new logic will prevent developers from introducing subtle logic bugs caused by operator misuse.  Further, we updated the rule example with the following:

<figure><img src="../../../../.gitbook/assets/image (2030).png" alt=""><figcaption></figcaption></figure>

Verified the new logic via the following scenarios:\
1\.  Rule sf:AvoidReversedOperators raises violations for reversed operator cases (=-, =+).

2\.  Rule does not raise false positives on valid operator usage (+=, -=).

<figure><img src="../../../../.gitbook/assets/image (2031).png" alt="" width="386"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2032).png" alt="" width="372"><figcaption></figcaption></figure>

5. **Enhancement to “CouplingBetweenObjects” Rule**\
   Modified the rule logic to correctly detect and report violations so that users can identify classes with excessive dependencies and reduce code complexity for better maintainability and testability.\
   \
   Verified that the violation is triggered when the number of classes used exceeds the defined threshold value in the rule parameter (for example, if the threshold is set to 4 and 5 classes are used, a violation will be raised).

<figure><img src="../../../../.gitbook/assets/image (2033).png" alt="" width="359"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2034).png" alt="" width="359"><figcaption></figcaption></figure>

6. **Enhancement to “Avoid Insecure Digest Algorithms” Rule**\
   Enhanced the current rule logic to correctly raise violations when MD5 or SHA-1 algorithms are used. Since these algorithms are cryptographically broken and vulnerable to hash collision attacks, their continued use poses a security risk.\
   \
   The rule should:

* Detect any instance or usage of MD5 or SHA-1 for hashing/digesting.
* Report violations with clear remediation guidance.
* Suggest secure alternatives such as SHA-256 or SHA-512. \
  \
  Verified the new logic via the following scenario:\
  Validated that users are able to see a violation for the rule _AvoidInsecureMessageDigests_. This violation indicates the use of insecure message digest algorithms such as MD5 or SHA-1.

<figure><img src="../../../../.gitbook/assets/image (2035).png" alt="" width="423"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2036).png" alt="" width="431"><figcaption></figcaption></figure>



7. **Enhancement to “Add Empty String” Rule**\
   Updated the rule logic to identify and flag expressions where literals are concatenated with an empty string (e.g., "" + 123 or 123 + "").  Also ensured that violations are reported with a clear message and that valid concatenations and type-specific toString() methods are not falsely flagged.\
   \
   Verified the below scenarios all are working as expected.\
   1\. Empty string with numeric or Boolean literals\
   Examples:\
   '' + 123, 123 + '', '' + -42, '' + 3.14, false + '', '' + true\
   \
   2\. Empty string with string/char literals or inside chains\
   Examples:\
   '' + 'abc', 'abc' + '', 'A' + '' + 'B', 1 + '' + 2\
   \
   3\. Empty string literals inside parentheses\
   Examples:\
   ('' + 1) + 2, 1 + ('' + 2)\
   \
   4\. Empty string at start of long chain with literals and variables\
   Example:\
   '' + 123 + 987 + var1 + var2\
   \
   5\. Empty string used with - operator and literals\
   Examples:\
   '' - 123, 123 - '', '' - -42

<figure><img src="../../../../.gitbook/assets/image (2037).png" alt="" width="401"><figcaption></figcaption></figure>

8. **Enhancement to “Avoid Hard-Coded Resource References” Rule**\
   Enhanced the rule logic to identify hard-coded file path references and raise violations with a clear issue message.\
   \
   Validated the logic by verifying that users are able to see the violations for the use of the attribute value that starts with '/resource/'.

<figure><img src="../../../../.gitbook/assets/image (2038).png" alt="" width="545"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2039).png" alt="" width="561"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2040).png" alt="" width="512"><figcaption></figcaption></figure>

***

## CodeScan Release 25.1.9

**Release Date: 07 September 2025**

### Summary:

CodeScan 25.1.9 is comprised of the following 4 components:

* 2 Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### Enhancements

1. Enhancement to Suppress Warnings Rule

Our rule TrackSuppressWarnings had logic to find @SuppressWarnings, but the logic didn’t include find @suppresswarnings.

This suppression tag works in any case and we recognized that our TrackSuppressWarnings rule needs to do the same (meaning the rule needs to be case insensitive.)

This logic was added to this rule in this enhancement.

Verified the  SuppressWarnings Rule enhancement and validated that the suppression tag is working in all case-insensitive instances and our TrackSuppressWarnings rule is throwing violation for all cases.

<figure><img src="../../../../.gitbook/assets/image (2003).png" alt=""><figcaption></figcaption></figure>

&#x20;

2. Rule Enhancement for sf:UnusedFormalParameter

In this rule enhancement, we introduce a configuration flag (ignoreUnusedParametersInInterfaceOverrides) in the sf:UnusedFormalParameter rule so that unused parameters in valid interface implementations and method overrides can be conditionally suppressed. By default, violations will continue to be reported unless this flag is explicitly set to true.

**How to Identify These Parameters for Suppression**

When designing your rule improvement, the logic should:

1\. Check if the method is implementing a known Salesforce interface method:

* Use method signature matching (name, parameters, visibility).
* Confirm the containing class uses implements keyword for one of the known Salesforce interfaces.
* Ensure parameter types match exactly, e.g., SchedulableContext, Database.BatchableContext.

<figure><img src="../../../../.gitbook/assets/image (2004).png" alt=""><figcaption></figcaption></figure>

2. Visibility Enforcement

* Only suppress violations if the method visibility is public or global, as required by the platform.
* Private or protected methods should never be eligible for suppression under this rule.
* This ensures that suppression only applies to methods actually callable by the platform or conforming to Apex interface rules.

3\. Override Detection

* If a method in a class overrides a method from a superclass or an abstract class:
  * Signature match is mandatory (same name, return type, and parameters).
  * Use of the override keyword confirms the intent, but even without it, structural matching should be enough.
  * In such cases, the parameter should not be flagged if unused, since it’s required by the parent contract.

Value / Purpose

* Prevent misleading or incorrect violations in valid interface and override implementations (e.g., execute \[SchedulableContext]).
* Preserve backward compatibility by keeping the rule strict by default.
* Additionally, we updated the Rule Description to “Avoid passing parameters to methods or constructors without actually referencing them in the method body. Use the ignoreUnusedParametersInInterfaceOverrides parameter to suppress violations for unused parameters in valid interface implementations and method overrides.”

Verified the rule sf:UnusedFormalParameter and validated the following conditions:

* The method implements a known Salesforce interface method.
* Method signature matches exactly in terms of:
  * Name
  * Parameters
  * Visibility
* The containing class uses the implements keyword with one of the known Salesforce interfaces (e.g., Schedulable, Database.Batchable).
* Parameter types match exactly, including types such as:
  * SchedulableContext
  * Database.BatchableContext

<figure><img src="../../../../.gitbook/assets/image (2005).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2006).png" alt=""><figcaption></figcaption></figure>

### Fixes&#x20;

1. Fixed issue with CodeScan rule detecting SOQL Injections, which was causing analyses to break.

Previously, while analyzing for SOQL Injection, if a local variable is declared using a class-level variable of same name, then CodeScan analyses were erroring with StackOverflowError as it was stuck in a loop while resolving the reference.

Example:

class Foo { private static String QUERY = 'Select '; public static List\<Opportunity> getData(String stage) { String query = QUERY + 'Id FROM Opportunity WHERE StageName = :stage'; return Database.query(query); } }

With this fix, we added validation to detect and prevent such recursive reference resolution.

Verified the SOQL injection rule fix (which was causing stack overflow error) by validating that now users are not encountering the error, and their project analyses are working as expected.

<figure><img src="../../../../.gitbook/assets/image (2007).png" alt=""><figcaption></figcaption></figure>

2. Fixed an Error that was occurring when Deleting CodeScan Projects

Some customers have reported that when attempting to do a project deletion, the task sometimes fails.  We have determined that the root cause is that the system is trying to fetch project details after the project has already been removed, which leads to missing information and, subsequently, unexpected errors.

This fix includes logic to delete projects properly.

We have verified the fix for Error When Deleting CodeScan Projects  and validated that users are able to delete their projects without any errors.

<figure><img src="../../../../.gitbook/assets/image (2008).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2009).png" alt=""><figcaption></figcaption></figure>

***

## CodeScan Release 25.1.8

**Release Date: 31 August 2025**&#x20;

### Summary:&#x20;

CodeScan 25.1.8 is comprised of the following 1 component:&#x20;

* 1 Fix&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### Fixes&#x20;

1. Fixed issue where CodeScan Project Analysis jobs getting stuck at "finalizing" stage.&#x20;

Previously, CodeScan project analysis jobs were getting stuck at "finalizing" stage, and not returning the result to GitHub PR, thus blocking all PRs.&#x20;

The root cause of the issue was that db-pool-limit-reached was occurring.  This fix remediates this issue.

After applying the fix, we validated the fix by creating jobs with alternating pass/fail quality gate statuses. Once the fix had been applied, we observed all jobs completing successfully (without getting stuck)\
\
We also verified the below Audit log cases:

Verified the category "PROJECT\_ANALYSIS" and checked the below details that are stored in the logs all are appearing as expected.

* Project Names
* Project Keys
* Lines of code count - split by ncloc languages
* Created date
* First analysis date

Also, Verified the category Quality Gates and checked the below details which are stored in the logs all are appearing as expected.

* operation": "UPDATE",
* propertyValue": "Failed/Passed”
* createdAt": “\*\*\*\*\*”
* componentKey
* componentName\
  componentUuid

<figure><img src="../../../../.gitbook/assets/image (2001).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2002).png" alt="" width="563"><figcaption></figcaption></figure>

***

## CodeScan Release 25.1.7&#x20;

#### Release Date: 24 August 2025&#x20;

### Summary&#x20;

CodeScan 25.1.7 is comprised of the following 5 components:&#x20;

* 1 New Feature&#x20;
* 4 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### New Features&#x20;

1. Enable/Disable feature of Mapping to multiple orgs from one SAML Connection at instance level.&#x20;

{% hint style="info" %}
_NOTE:  This feature is only available to customers who have a dedicated instance. It is not available for customers who are deployed on our SaaS multi-tenant instances._&#x20;
{% endhint %}

This new feature enables customers to map to multiple orgs from one SAML Connection at their instance level.

Verified the following scenarios for SAML users, and all scenarios are working as expected.&#x20;

1. Verified the User when CodeScan idp-group-mapping is disabled, user is able to log in through SSO when the Group synchronization and IDP mapping is not used.&#x20;
2. Verified the User when CodeScan idp-group-mapping is disabled, user is able to log in through SSO when the Group synchronization and IDP mapping are used.&#x20;
3. Verified the User when CodeScan idp-group-mapping is enabled, user is able to log in through SSO when the Group synchronization and IDP mapping are used.&#x20;
4. Verified the User when CodeScan idp-group-mapping is enabled, user is able to log in through SSO when the Group synchronization and IDP mapping are not used.&#x20;
5. Validated the SAML connection creation and login through SSO in the created Org.&#x20;
6. Validated the SAML connection creation and login through SSO with the other Org.&#x20;
7. Created a new user and checked the login through SSO with the same above SAML config.&#x20;
8. Verified the IDP group mapping where the user is mapped to the organization where SAML connection is created.&#x20;

{% hint style="info" %}
_NOTE:  This feature needs to be enabled in customers’ organizations.  It is NOT available by default_&#x20;
{% endhint %}

{% hint style="info" %}
_NOTE:  This feature is only available to customers who have a dedicated Instance.  It is not available for customers who are deployed on our SaaS multi-tenant instances._&#x20;
{% endhint %}

### Fixes&#x20;

1. **Fixed Broken Documentation Link in Status Module**&#x20;

It has been reported that the "Status" module in all CodeScan application contains a broken documentation link: \
[https://knowledgebase.autorabit.com/user-guide/issues/solution-overview/#life-cycle](https://knowledgebase.autorabit.com/user-guide/issues/solution-overview/#life-cycle)&#x20;

This link provides users with detailed information on the lifecycle of issue statuses but currently leads to a nonexistent page. The correct, working link should be: \
[https://knowledgebase.autorabit.com/product-guides/codescan/issues/about-issue-status](https://knowledgebase.autorabit.com/product-guides/codescan/issues/about-issue-status)&#x20;

This fix remediates this issue in full.&#x20;

Verified the fix by confirming that the documentation link under the "Status" tab in the Issues module has been updated and now redirects to the correct Knowledge Base page. \
The link is updated to [About Issue Status | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/codescan/issues/about-issue-status) &#x20;

<figure><img src="../../../../.gitbook/assets/image (1).png" alt="" width="483"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1) (1).png" alt="" width="486"><figcaption></figcaption></figure>

2. **URIs are not Valid in decorated SARIF output**

It has been reported that the URLs are not valid in the SARIF file due to spaces.  To remediate, we added logic to make certain that they are escaped.

Verified that users are now able to see valid URLs in the SARIF report even when the file names include underscores, numbers, hyphens, special characters, with spaces.

<figure><img src="../../../../.gitbook/assets/image (2).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3).png" alt="" width="305"><figcaption></figcaption></figure>

3. **Fixed issue where scheduled analyses are not running for SF projects and its comparison branches**

Several customers have reported that their daily scheduled analyses were not running for Salesforce integration projects and their corresponding comparison branches within the same project.  We determined that the Scheduled Jobs were getting stuck, even though they were consuming memory and CPU.  Further, we identified that the root cause of the issue stemmed from changes made in the previous release (25.1.6), and that scheduled jobs on our AWS infrastructure were running into “out-of-memory” issues.

This fix remediates this issue in full.

Verified the fix and validated that the scheduled jobs are now running without issue (as expected).

<figure><img src="../../../../.gitbook/assets/image (5).png" alt="" width="563"><figcaption></figcaption></figure>

4. **Fixed issue with deleting branches in projects using Salesforce Integration**

We uncovered that if the following steps were performed…

1\. Launch and log in to the CodeScan application and be on any org.\
2\. Create Salesforce project.\
3\. Create comparison and standard branch analysis.\
4\. Try deleting comparison branch.

…then users receive an error message indicating that an “unknown error occurred.”

<figure><img src="../../../../.gitbook/assets/image (6).png" alt="" width="353"><figcaption></figcaption></figure>

This issue has been fully remediated in this release.

We have verified the fix and have validated that the following scenarios are all working as expected:\
\
1\. Verified salesforce comparison branch deletion.\
2\. Verified creation of project with user having (create and analyze project permissions).\
3\. Renaming of project branch.\
4\. ALM project tags working as expected.

***

## CodeScan Release 25.1.6

**Release Date: 3 August 2025**

### Summary

CodeScan 25.1.6 is comprised of the following 6 components:

* 1 New Feature
* 3 Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

&#x20;

### New Features

1. **Categories for Project Types**

Often, customers will have a lot of projects in CodeScan.  Several customers have requested the ability to filter their projects by the type of integration including:

GitHub: github\
Bitbucket: bitbucket\
GitLab: gitlab\
Git: git\
Salesforce: salesforce

To deliver this feature, we created custom tags with the ability to add these tags when new projects are created.  Further, we wanted to provide a mechanism to retroactively add these tags to existing projects.

Unlike most tags, we designed integration type tags to remain once assigned. If the user tries to remove it the following error will occur: “Integration type tags cannot be removed from projects.”

NOTE:  Due to the change in permissions needed in the API for these tags to be added, we also adjusted the text in the API doc as well. For the endpoint api/project\_tags/set the text now states:

“Requires the ‘Administer’ or ‘Create Project’ permissions on the specified project.”

Here are the tag API references: [CodeScanCloud](https://app.codescan.io/web_api/api/project_tags)

Verified Categories for Project Types in the following scenarios, and have verified that all are working as expected:

1. **Verify that the user is able to see the correct tag for the project on the Project Information page after completing the analysis.**\
   &#xNAN;_&#x45;xample: For a Salesforce integration, the tag should display as “Salesforce.”_\


<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. **Verify that the user is able to see the correct tag for each project integration under the "Tags" column in the Projects tab of the organization.**\
   &#xNAN;_&#x45;xample: For a Salesforce integration, the tag should display as “Salesforce.”_

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3.  **Verify that the user is able to see the correct tag for each project integration under the "Tags" column in the My Projects tab.**\
    &#xNAN;_&#x45;xample: For a Salesforce integration, the tag should display as “Salesforce.”_\


    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4.  **Verify that the user is not able to remove an existing tag or add a tag of a different integration tag to the project.**\


    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
5.  **Verified that clicking on a tag correctly displays the associated projects, with accurate project count and correct project listings.**\


    <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Enhancements

**1.     Users getting error when trying to restore quality profiles.**

Currently, when a Quality Profile import fails, CodeScan displays the following error: _"An error occurred. Please contact your admin."_

We recognize that it would be a better experience (and more helpful) to make this error more verbose to allow the customer to remediate the issue themselves.  Mostly these errors are thrown because of a rule present in their Quality Profile which is not present in their organization. In these cases, the error message is now “An error occurred. A rule in your Quality Profile is not available in this organization.”

The second most common error occurs when the QP is corrupted or malformed.  In these cases, the error message now states “An error occurred. The Quality Profile backup is malformed. Please export your Quality Profile again.”

We believe that these more verbose error messages will help our customers remediate their issue much more easily.  However, if they require assistance, they can create a support ticket.

Verified this enhancement via validating the below scenarios

1.  If a malformed QP (with no profile name/language) is imported, an error message is shown.\


    <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>


2. When importing a QP with custom rules from another instance, those custom rules are also created during import.
3.  If the imported QP has no profile language, the error message says: "Profile language should be set."\


    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4.  If the QP has no profile name, the error message says: "Profile name should be set."\


    <figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
5.  If no file is selected during import, an error occurs.\


    <figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
6. If the repository key is missing, an import error is triggered.
7.  If a QP with profile name CodeScan way/CodeScan strict way/CodeScan nCino way name is imported, an error is thrown.\


    <figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



**2.     Pagination in Projects and Previous Analysis**

To provide a better experience, we have added separate pagination controls, allowing users to navigate Projects Analysis and Previous Analysis sections more easily.   This enhancement includes Projects Analysis displaying 10 entries per page and Previous Analysis displaying 15 entries per page.  This allows the user interface to remain responsive and readable even when there are many entries.

Verified the Pagination enhancement via validating the following scenarios:

1.  The _Projects Analysis_ section displays a maximum of 10 entries per page.\


    <figure><img src="../../../../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  The _Previous Analysis_ section displays a maximum of 15 entries per page.\


    <figure><img src="../../../../.gitbook/assets/image (11) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. Pagination controls (e.g., next, previous, specific result numbers) are present and functional in both sections independently.

**3.     Email Limit & Validation for Multi-User Invites**

To improve the user experience for admins inviting users to their CodeScan org, we have implemented the ability to invite multiple users at once (up to 50) using the same user type (Standard User or Platform Integration User).  Additionally, this enhancement ensures that only valid email addresses are accepted in the batch.  This ensures that the invite experience remains consistent and controlled; additionally, user onboarding will be faster and more efficient.  Further, Admins are still able to maintain control over user type classification, email validation, and system performance.

The main components of this enhancement are:

1. Added each email on a new line.
   * Text was added in UI beside Email option for multiple users invite option.
2. Add the following error during limit exceeded scenario: “Invite limit exceeded. Max 50 emails allowed.”

Value / Purpose:

* Streamlines onboarding by allowing multiple users to be invited in one action.
* Maintains role clarity by restricting each batch to a single user type (Standard or Platform Integration).
* Improves system integrity and reliability by validating email format and capping batch size.
* Prevents errors and abuse by limiting the invite size to a maximum of 50 and checking for valid emails only.

We have verified the enhancement for Email Limit & Validation for Multi-User Invites by validating the following scenarios:

1.  Verified that if invite is sent to more than 50 members, then the following is thrown:\


    <figure><img src="../../../../.gitbook/assets/image (12) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  Invite sent successfully if invite is sent to less than or equal to 50 users.\


    <figure><img src="../../../../.gitbook/assets/image (13) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Verified, if mail address is more than 100 characters, then an error is thrown; if it is less than 100 characters, then the invite is sent successfully.\


    <figure><img src="../../../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>
4.  If invite sent to non-corporate domains, the following error is thrown:\


    <figure><img src="../../../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

### Fixes

1\.     Align CSV Export filter status with Latest SQ Issue status

This enhancement implements issue status values in the CSV export filters to reflect the latest status terminology introduced after CodeScan 25.1.0 release (which occurred in April 2025).  Prior to this enhancement, the filters in CSV Issue Export were showing outdated statuses such as Opened, Confirmed, ReOpened, Resolved, and Closed.  This was in contrast to the updated statuses including Open, Accepted, False Positive, Confirmed, and Fixed.  This inconsistency was reported by several users who cited confusion and data integrity issues when analyzing or reporting exported results.

Value / Purpose:

* Ensures consistency between issues UI and CSV exported data.
* Improves user trust and understanding of exported scan results.

Acceptance Criteria

* Status Values in Export:
* Legacy Status Replacement:
* Filter Cleanup:
* UI-CSV Consistency:
* Backward Compatibility:
*
  * Existing historical issues should reflect the new status names in the export, even if their status was stored using legacy labels.

Verified this enhancement by validating the following scenarios:\


1. Status Values in Export:

The issue statuses in the exported CSV must match the latest values of Open, Accepted, Confirmed, False Positive, and Fixed\
Legacy Status Replacement:

* Legacy status values such as Opened, Confirmed, ReOpened, Resolved, and Closed must no longer appear in the exported CSV.
* These must be correctly mapped to the corresponding updated status where applicable.

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

2. Filter Cleanup:

The Resolutions filter should be completely removed from the CSV Export page.

The Is Resolved filter should be completely removed from the CSV Export page.

Only the Status filter should be visible and functional.

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

3. UI-CSV Consistency: The status shown in the exported CSV for each issue must exactly match what is shown for the same issue in the UI.
4.  The type, statuses and severity shown in the exported CSV is exactly matching what is shown in the issues page and CSV export page.\


    <figure><img src="../../../../.gitbook/assets/image (18) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

2. Fixed an unclear error message displayed when invite is sent only to non-corporate email addresses

This fix addresses an unclear message that occurs when:

* Admin clicks on "Invite user"
* Admin enters only non-corporate email addresses (e.g., Gmail, Yahoo)
* Admin clicks "Send Invitation"

After these steps, Admin receives the following unclear error message:

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

However, this issue does not occur when multiple users are invited, including at least one corporate email:

<figure><img src="../../../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

This issue has been fully remediated.  We have verified the fix via the following scenario:\
\
Validated that the proper error message is displayed when invite is sent only to non-corporate email addresses.

<figure><img src="../../../../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

***

## CodeScan Release 25.1.5

**Release Date: July 20, 2025**

### Summary:

CodeScan 25.1.5 is comprised of the following 17 components:

·       4 New Features

·       2 Enhancements

·       4 Fixes

·       1 Revenue Org Improvement

·       6 Architecture Improvements

Component details are listed in their corresponding sections within this document.

&#x20;

### New Features:

1. **Support Intelligent Prompts for A.I. LLMs**

&#x20;CodeScan can now generate prompts for LLMs including Agentforce, Copilot, ChatGPT, and Claude AI.  This feature is a component of the CodeScan extension for VS Code.

&#x20;

Requirements:

Your CodeScan environment must be running version 25.1.5 (or higher).  In addition, you need to be running the latest version of the CodeScan VS Code extension (v 2.1.1), which can be downloaded here:  [https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode](https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode)

What Problem Are We Solving?

Adoption of AI can be challenging for companies for several reasons.  CodeScan can help catalyze your AI initiatives.

User Benefits

•       Generate prompt in the IDE

•       Directly update existing code with generated code

•       Ensures security issues are addressed

&#x20;

Verified Intelligent Prompts for cls, page, component, trigger, and cmp files, all working as expected by validating the below scenarios:

1\. Able to click generate prompt and copy it

<figure><img src="../../../../.gitbook/assets/image (1825).png" alt="" width="563"><figcaption></figcaption></figure>

2. Able to paste the generated prompt in the Agentforce search box

<figure><img src="../../../../.gitbook/assets/image (1827).png" alt="" width="563"><figcaption></figcaption></figure>

3. Able to receive the message prompt copied to clipboard after generating prompt.

<figure><img src="../../../../.gitbook/assets/image (1828).png" alt="" width="563"><figcaption></figcaption></figure>

4. Able to receive a message stating that the file is too long; please select the impacted lines of code and click "Generate Prompt" if the selected file has more than 1,000 characters.

<figure><img src="../../../../.gitbook/assets/image (1829).png" alt="" width="563"><figcaption></figcaption></figure>

5. Able to copy the code generated by Agentforce as expected

<figure><img src="../../../../.gitbook/assets/image (1830).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Notes:

If the file content isn’t too long (less than 1000 characters) the \<FILE\_CONTENT> placeholder gets the contents of the entire file.  Else, only selected items will be passed (needs to be selected manually by the user).  This is intentional because although Salesforce maintains that Agentforce’s input limit is 27k, we have discovered that when we do pass large code in the prompt the response generation is only for the first few lines (around 1000 chars) then stops (causing the response to be incomplete).
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (1831).png" alt="" width="536"><figcaption></figcaption></figure>

2. **CVSS Implementation for Security Vulnerabilities**

The Common Vulnerability Scoring System is a technical standard for assessing the severity of vulnerabilities in computing systems. Scores are calculated based on a formula with several metrics that approximate ease and impact of an exploit. Scores range from 0 to 10, with 10 being the most severe.  In this release, CodeScan has applied this quantitative scoring to all security vulnerabilities, allowing organizations to more systematically prioritize the security remediations.

_The following metrics were used to generate our CVSS scores:_

Base Score Metrics

* Attack Vector (AV) (specify)
* Attack Complexity (AC) (specify)
* Privileges Required (PR) (specify)
* User Interaction (UI) (specify)
* Scope (S) (specify)
* Confidentiality Impact (C) (specify)
* Integrity Impact (I) (specify)
* Availability Impact (A) (specify)

Temporal Score Metrics

* Exploit Code Maturity (E) (specify)
* Remediation Level (RL) (specify)
* Report Confidence (RC) (specify)

Environmental Score Metrics

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

_Verified the CVSS range from 0 to 10, where users are able to see the CVSS violations for the below rules as expected._

1. OpenRedirect
2. CustomFieldSecurityInStandardObject
3. SOQL Injection
4. FieldLevelSecurity

<figure><img src="../../../../.gitbook/assets/image (1833).png" alt="" width="503"><figcaption></figcaption></figure>

Verified the CVSS Category on RULES page, ISSUES page and also verified the CVSS issues for the specific analysis.

<figure><img src="../../../../.gitbook/assets/image (1834).png" alt="" width="495"><figcaption></figcaption></figure>

&#x20;**3. When encountering an Incorrect Custom XPath rule, CodeScan Analysis continues**

&#x20;Currently, if a customer’s Xpath Rule has incorrect XPath syntax, an error is shown in the analysis log and no further checks are run on the file that the custom rule was being applied to.

We decided to make this more visible to users, as there was no further explanation of skipping the file outside of reviewing the associated logs.  Instead, users would see the issues disappearing from their files.

In this release, the following improvements were added:

* one incorrectly formatted custom rule shouldn’t stop the processing of all rules on a file
* created a project level rule that triggers a violation when this issue occurs
* implemented the logic for a project level violation that appears when this issue occurs
* created an associated message: “The custom XPath rule {rule key} failed to parse. Your {language} files were not able to display this issue. Please check your custom rule in the rule designer before your next analysis”

&#x20;

4. **Define User Type While Inviting or Adding Member**

&#x20;CodeScan now allows admins to define the user type when inviting or adding a member (either "Standard User" or "Platform Integration User").  This ensures that each user is onboarded with the appropriate role, purpose, and permissions.

\
Since the system now allows for the designation of users as either Standard Users or Platform Integration Users during the invitation or member addition process, admins are now able to manage users more effectively (and thereby Ensuring Standard Users have the appropriate access (All the features of CodeScan), and Platform Integration Users are recognized distinctly for integration IDE purposes (or similar integration purposes).

Value / Purpose:

* Improves access control by ensuring correct user roles at the point of entry.
* Differentiates Standard Users from Platform Integration Users for better tracking and reporting.
* Enhances audit logs, billing accuracy, and license management.
* Reduces post-invite administrative tasks by setting the correct user type up front.
* Supports security and compliance needs by maintaining a clear separation between user types.

&#x20;

Verified the ability to define User Type While Inviting or Adding Member by validating the below scenarios:

1. Admin must be able to select the user type ("Standard User" or "Platform Integration User") when inviting or adding a member.
2. The user type selection must be a required field.

<figure><img src="../../../../.gitbook/assets/image (1835).png" alt="" width="563"><figcaption></figcaption></figure>

3. "Standard User" should be the default selection.

<figure><img src="../../../../.gitbook/assets/image (1836).png" alt="" width="539"><figcaption></figcaption></figure>

4. Selected user type must determine the role and permissions automatically:
   * Standard Users get full access to all CodeScan features.

<figure><img src="../../../../.gitbook/assets/image (1837).png" alt="" width="563"><figcaption></figcaption></figure>

* Platform Integration Users get limited access scoped to integration IDE tasks.

<figure><img src="../../../../.gitbook/assets/image (1838).png" alt="" width="563"><figcaption></figcaption></figure>

5. User type must be clearly labeled in the member management.

<figure><img src="../../../../.gitbook/assets/image (1839).png" alt="" width="563"><figcaption></figcaption></figure>

6. “Platform user cannot be added to the Owner group.” — should be displayed when the Owners group is selected for a Platform user. Additionally, the Send Invite button should be disabled in this case.

<figure><img src="../../../../.gitbook/assets/image (1840).png" alt="" width="563"><figcaption></figcaption></figure>

7. For multi-user invites, the flow should be the same as for a single invite. Invites can be sent in batches, but only for one user type at a time.

<figure><img src="../../../../.gitbook/assets/image (1841).png" alt="" width="563"><figcaption></figcaption></figure>

8. Able to see the standard and platform user type while adding a member to the organisation

<figure><img src="../../../../.gitbook/assets/image (1842).png" alt="" width="563"><figcaption></figcaption></figure>

### Enhancements

1. &#x20;Add ESLint rules from @lwc/eslint-plugin-lwc

CodeScan has traditionally provided ESLint rules within our rules library.  Separately, Salesforce has an official ESLint plugin to analyze LWC code:[https://github.com/salesforce/eslint-plugin-lwc](https://github.com/salesforce/eslint-plugin-lwc).

The rules in this plugin are different to our current set and expand on it; expanding the rules in our LWC set is vital to support the needs of our customers using Lightning Web Components.

Our aim was to include all rules from the GitHub - salesforce/eslint-plugin-lwc:

Official ESLint rules for LWC repository added to our current list.  However, there are a few rules from this plugin that were not included.

Rules that weren’t added as part of LWC set:

* Disallow duplicate class members (no-dupe-class-members).  This wasn’t added because it’s a Deprecated Rule

Additionally, we did not include these 3 rules because of the Complex Parameter Type:

* Enforce wire adapters to be used with wire decorator (no-unexpected-wire-adapter-usages)
* Disallow usage of unknown wire adapters (no-unknown-wire-adapters)
* Disallow access to global browser APIs during SSR (no-restricted-browser-globals-during-ssr)

&#x20;

Note that all of these LWC  rules were added to our Salesforce Lightning Quality Profile.

&#x20;

Verified the Add Eslint rules from @lwc/eslint-plugin-lwc for the below scenarios:\
\
1\. Verified the 21 rules from the [GitHub - salesforce/eslint-plugin-lwc: Official ESLint rules for LWC](https://github.com/salesforce/eslint-plugin-lwc) repository added to our Salesforce Lightning Quality Profile of javascript language.\
\
2\. Verified the Description, Rule Details, Type of issue, Remediation function, Severity for all the rules.\
3\. Verified that new rules is not included in the default Quality Profile.\
4\. Verified that violation is thrown for all the 21 rules.

<figure><img src="../../../../.gitbook/assets/image (1843).png" alt="" width="503"><figcaption></figcaption></figure>

2. &#x20;Enhancement to Apex rule “Unused Formal Parameter” {sf:UnusedFormalParameter}

CodeScan has offered this rule since Dec 2017.  Recently a customer reported that Unused Formal parameter doesn’t find when variables used in SOQL.  We replicated this issue where CodeScan flagged a variable as an unused variable even though it is used in the SOQL string.

We have enhanced this rule to detect additional cases where string parameters are part of SOQL.  Bottom of FormThe  Top of FormThe rule now detects cases where string params are used as part of building soql query.

Verified the enhanced logic of rule “UnusedFormalParameter” via the following scenarios.\
\
1\. Previously, a parameter (e.g., encounterIds) used in a SOQL string (e.g., WHERE Id IN :encounterIds) was wrongly reported as unused.\
Now, this is correctly detected as usage — no violation.

<figure><img src="../../../../.gitbook/assets/image (1844).png" alt="" width="563"><figcaption></figcaption></figure>

2. Also verified below cases all are working as expected Verified: Parameter used in SOQL with bind variable (:encounterIds) — no violation Verified: Parameter used via clause string assembly — no violation Verified: Parameter incorrectly concatenated into SOQL string — violation Verified: Parameter declared but not used anywhere — violation

<figure><img src="../../../../.gitbook/assets/image (1845).png" alt="" width="518"><figcaption></figcaption></figure>

### Fixes&#x20;

1. **Fixed issue ARM users recieving an error: “Component can't be null” while running a CodeScan analysis from ARM.**

The issue is occurring in the SFDX retrieval. From ARM, when the user commits only the fields (or, for example, lookup fields), the .object-meta.xml is not retrieved. As a result, the retrieved file structure differs from what was expected. After analysing the rule’s implementation, it was found that the rule does not check if the .object-meta.xml file exists first and forcibly tries to throw the violation on the file. Hence, the "component can't be null" error is thrown. This required an engineering fix in the rule.

Note: The issue lies in one of the common methods many rules use, so this error is not confined to these two rules.

Other rules that use this method include:

<figure><img src="../../../../.gitbook/assets/image (1846).png" alt="" width="563"><figcaption></figcaption></figure>

With this fix, users are now able to see the violations for all 7 rules when running a CodeScan analysis from the ARM side using the CodeScan plugin:

#### Rules:

sfmeta:CrossObjectFormulaOveruse

sfmeta:ObjectLookupsOveruse

sfmeta:RelationShipOveruse

sfmeta:ExternalIdOveruse

sfmeta:RollUpOveruse

sfmeta:LimitCustomFields

sfmeta:nCinoFieldHistoryTracking

Verified by committing only specific fields and triggering SCA analysis — violations appeared as expected.

**Ran analysis for the entire Salesforce org, including objects — violations were also detected."**

<figure><img src="../../../../.gitbook/assets/image (1847).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1848).png" alt="" width="555"><figcaption></figcaption></figure>

2. **Fixed issue where after a user is deactivated, the user is still displayed on Members page**

Some users were reporting that after a user is deactivated, the user is still displayed on the Members page.

**Detailed Solution**

1. Made changes in the codebase to remove the user from members table when the user is deactivated.
2. Enusresd that using “search” on the Members page only active users are retrieved.
3. The user is no longer able to login via SAML

Verified the below scenarios regarding users being displayed in Members page, and all scenarios are working as expected.

1. Create and Activate New User- User appears under the Members list of the active organization
2. Add User to Inactive Organization- User is visible under the Members list of the inactive organization
3. Deactivate User from Instance- User no longer appears in the Members list. Behavior confirms that deactivated users are excluded from the UI display
4. Verify SAML Login for New User- Authentication via SAML was successful
5. Billing Page User Count Verification- User count reflects the new user addition appropriately. Billing data is updated as per user assignments

&#x20;

3. **Fixed issue with rule “Avoid running Soql and DML inside loops” {sf:AvoidSoqlInLoops}**

Recently, some customers reported unexpected behavior in this rule, producing false positives.

The root cause of the false positives is that when a method of an object is invoked within another method, and both methods share the same name, the current rule implementation incorrectly interprets this as a recursive call and subsequently triggers a violation.  Further, the Stack Loop trace is indefinite.

This had been remediated in a previous release (25.1.2 release in June 2025).  The updated rule logic now handles these edge cases by checking for method image to be exactly the same (method != diffObj.method).

However, there’s more to this issue and fix!  A scenario which was earlier covered stopped working as expected as a result of the fix made above.  This new issue was reported to us, and has been fully remediated in this release by adding additional logic to the rule implementation was made to accommodate both scenarios (the pre-existing condition but also indefinite stack loop trace).

&#x20;

Verified the Fix for rule sf:AvoidSoqlInLoops via several scenarios, including:

Verified – SOQL inside a method (not directly in a loop) — no violation as expected

Violations Expected for the below scenarios

1. Verified SOQL directly inside a for loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1849).png" alt="" width="474"><figcaption></figcaption></figure>

2. Verified SOQL inside nested if blocks within a loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1850).png" alt="" width="474"><figcaption></figcaption></figure>

3. Verified SOQL inside a try/catch block within a loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1851).png" alt="" width="443"><figcaption></figcaption></figure>

4. Verified SOQL in a method (or recursive call) invoked from a loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1852).png" alt="" width="563"><figcaption></figcaption></figure>

5. Verified SOQL in static helper method called from a loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1853).png" alt="" width="563"><figcaption></figcaption></figure>

6. Verified SOQL inside a while loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1854).png" alt="" width="449"><figcaption></figcaption></figure>

7. Verified SOQL inside a do-while loop — got violation as expected
8. Verified SOQL directly inside System.debug() within a loop — got violation as expected

<figure><img src="../../../../.gitbook/assets/image (1866).png" alt="" width="563"><figcaption></figcaption></figure>

**No Violations Expected for the below scenarios**

9. Verified Bulkified SOQL outside the loop (e.g., IN :ids) — no violation as expected
10. Verified SOQL in deep conditional logic but not inside a loop — no violation as expected
11. Verified SOQL inside try/catch block, not inside a loop — no violation as expected
12. Verified SOQL in method not called from a loop — no violation as expected
13. Verified SOQL inside interface/abstract method (called via polymorphism from loop) — no violation as expected

14\. Verified SOQL inside constructor called from a loop — no violation (as expected for shallow analyzers)

&#x20;

4. **Fixed issue regarding restricted access for CodeScan Platform Integration Users**

Some users were reporting that their platform integration users has the same accessibility to CodeScan as their standard users.  This issue is remediated in this release.

As a PIU (Platform Integration User) with restricted access in the CodeScan platform, PIU should only be able to view the Account section after logging in. All other features like Project Analysis, Project View, Issues View, and Search etc. (All except Account Section) should be inaccessible.  Within the Account section, PIU should see the following tabs:

* Profile
* Security
* Notifications
* Projects
* Organization

<figure><img src="../../../../.gitbook/assets/image (1856).png" alt="" width="560"><figcaption></figcaption></figure>

Additionally, the Help and Profile sections in the header should remain accessible. When clicking on the Profile icon, a pop-up should appear displaying (As shown in attached images):

* Username, Email
* My Account
* Logout Option

<figure><img src="../../../../.gitbook/assets/image (1857).png" alt="" width="515"><figcaption></figcaption></figure>

Verified Restricted Access for CodeScan Platform Integration User by validating the following scenarios:

1. Verified all integration project analysis and PR analysis as a Standard user.
2. Verified all IDEs as a Platform user.
3. Verified IntelliJ, VS Code, GitHub Actions, SFDX, Sonar Scanner, and Azure as a Standard user.
4. Platform users should have access only to the My Account page.

<figure><img src="../../../../.gitbook/assets/image (1858).png" alt="" width="273"><figcaption></figcaption></figure>

5. Platform users should only be able to view the Projects and Organizations tabs—no actions should be permitted.

<figure><img src="../../../../.gitbook/assets/image (1859).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1860).png" alt="" width="563"><figcaption></figcaption></figure>

6. Both Standard and Platform users should have:

* The Help section is accessible in the header.

<figure><img src="../../../../.gitbook/assets/image (1861).png" alt="" width="563"><figcaption></figcaption></figure>

* The Profile section is accessible in the header.

<figure><img src="../../../../.gitbook/assets/image (1862).png" alt="" width="563"><figcaption></figcaption></figure>

7. On clicking the Profile icon, the Platform user should be able to see:

* Username
* Email
* My Account
* Logout option

&#x20;8\. Verified Billing & Revenue Compliance for both Standard and Platform users.

9. Users who are Standard users in some organizations and Platform Integration users in other organizations should be shown the homepage of the organizations where they are Standard users upon login.
10. If Standard users do not have any homepage, they should be shown the My Projects page (All Projects), which should only display projects from the organizations where they are Standard users.

<figure><img src="../../../../.gitbook/assets/image (1863).png" alt="" width="563"><figcaption></figcaption></figure>

11. User type and UI should be organization-specific. If a user switches between organizations, the UI corresponding to their user type in the selected organization should be displayed.

<figure><img src="../../../../.gitbook/assets/image (1864).png" alt="" width="563"><figcaption></figcaption></figure>

12. If Standard users do not have any homepage, they should be shown the My Issues page (All Issues), which should only display issues from the organizations where they are Standard users.

<figure><img src="../../../../.gitbook/assets/image (1865).png" alt="" width="563"><figcaption></figcaption></figure>

***

## CodeScan Release 25.1.4

**Release Date: 6 July 2025**

### Summary

CodeScan 25.1.4 is comprised of the following 6 components:

* 1 New Features
* 3 Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

1\.     Support for Enterprise Git Connections / Configuring & Managing ALM Integrations

In CodeScan, Enterprise Git Connections enable organizations to securely integrate with self-hosted or enterprise instances of GitHub, GitLab, and Bitbucket. Admins can configure these connections at the organization level using OAuth credentials and define allowed IP ranges for secure access. Once connected, these integrations streamline project onboarding by allowing users to directly link Git repositories during project setup for automated analysis and CI/CD workflows.

<figure><img src="../../../../.gitbook/assets/image (1737).png" alt=""><figcaption><p>ALM Connections</p></figcaption></figure>

More detailed info can be found in our Knowledge Base here:&#x20;

[https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/enterprise-git-connections](https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/enterprise-git-connections)

### Enhancements

1\.     Enhancement to CodeScan Rule “URL Redirection to Untrusted Site” {sf:OpenRedirect}

CodeScan has traditionally used this rule to check against redirects to user-controlled locations. This is important because untrusted input could cause an attacker to redirect the user to a malicious site, thereby allowing the attacker to launch a phishing scam and steal user credentials.

<figure><img src="../../../../.gitbook/assets/image (1738).png" alt=""><figcaption></figcaption></figure>

However, our existing rule did not specifically check for the use of Network.forwardToAuthPage.

<figure><img src="../../../../.gitbook/assets/image (1739).png" alt=""><figcaption></figcaption></figure>

This rule has now been enhanced with this logic, and we have verified that users are now able to see the violation for the use of both Network.forwardToAuthPage and PageReference.

<figure><img src="../../../../.gitbook/assets/image (1740).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1741).png" alt=""><figcaption></figcaption></figure>

More details regarding the Network class can be found here: [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_network.htm#apex_System_Network_forwardToAuthPage).

1\.     Enhancement to CodeScan decorations of SARIF Reports

Since the 24.0.6 release (June 2024), CodeScan was enhanced to decorate standard SARIF output.  While CodeScan had been able to generate SARIF output before the 24.0.6 release, it’s noteworthy to mention that the SARIF output in GitHub does not contain the severity. As such, we added severity to our SARIF output, thereby allowing CodeScan to provide a more verbose presentation of the issues in GitHub. This change has been providing a better experience for our customers working in GitHub Actions.

The way this feature was originally designed was:

* When generateSarifFile: true, the generated SARIF file includes all issues, both open and resolved. Additionally, the report contains detailed metadata such as Type and Severity for each issue.
* When generateSarifFile: false, the generated SARIF file includes only open issues, and it does not include the Type and Severity information for the issues.

This means that when generateSarifFile is set to false, the generated SARIF file includes only open issues, but omits important metadata such as Type and Severity for each issue.

However, to maintain consistency and support downstream analysis tools, the SARIF file should always include detailed metadata for each issue, regardless of the generateSarifFile setting.

Thus, this enhancement expands upon the existing capability and introduces much more robust functionality.

With this release, when generateSarifFile: false or generateReportFile: true, the SARIF file:

* Contains only open issues respective to the baranch and PR
* Includes full metadata for each issue, including Type and Severity for rules and results



More detailed information can be found here:  [https://knowledgebase.autorabit.com/product-guides/codescan/report-and-analysis/generating-decorated-sarif-reports](https://knowledgebase.autorabit.com/product-guides/codescan/report-and-analysis/generating-decorated-sarif-reports)

Verified the below types of analyses with SARIF report all are working as expected:

* Commit request analysis
* PR analysis
* Merge analysis
* SARIF reports

Verified the SARIF report with the parameter generateSarifFile: false/true in the YML file user is able to see the open issues of the specific branch or pr and also able to see the issue TYPE and SEVERITY in the SARIF report.

2\.     On the Billing Page, a banner was added that details the level of access users have within the CodeScan UI based on user license type

Customers who are using a user-based license model will now have a banner on their Billing Page that provides additional clarity regarding the CodeScan features available to users based upon their license type.  Standard users will have access to all CodeScan features (although access can be restricted by admin based on user privileges).  Platform Integration Users will only have access to their Profile, along with access to the Security Tab and the Notifications Tab.  Additionally, both types of users can fully use the CodeScan extension for VS Code and IntelliJ.

<figure><img src="../../../../.gitbook/assets/image (1742).png" alt=""><figcaption></figcaption></figure>

### Fixes

1\.      Fixed issue where after a user is deactivated, the user is still displayed on Members page

Some users were reporting that after a user is deactivated, the user is still displayed on the Members page.

Detailed Solution

1. Made changes in the codebase to remove the user from members table when the user is deactivated.
2. Ensured that using “search” on the Members page, only active users are retrieved.
3. The user is no longer able to login via SAML

Verified the below scenarios regarding users being displayed in Members page, and all scenarios are working as expected.

1. Create and Activate New User: User appears under the Members list of the active organization
2. Add User to Inactive Organization: User is visible under the Members list of the inactive organization
3. Deactivate User from Instance: User no longer appears in the Members list. Behavior confirms that deactivated users are excluded from the UI display
4. Verify SAML Login for New User: Authentication via SAML was successful
5. Billing Page User Count Verification: User count reflects the new user addition appropriately. Billing data is updated as per user assignments

2\.     Fixed issue with codescan-scanner-action (occurring after CodeScan upgrade)

Some users were reporting that when their CodeScan project was upgraded to CodeScan 24.12.0.100206, it was incompatible with our codescan-io/codescan-scanner-action (and thus breaks customers’ GitHub Actions pipelines for pull request scanning).

This issue is remediated with this fix.

Validated that all below scenarios are working as expected.

1. Verified the GitHub Actions runner when using runs-on: ubuntu-latest
2. Verified the GitHub Actions runner when using runs-on: macos-latest
3. Verified the GitHub Actions runner when using runs-on: windows-latest
4. Verified the GitHub Actions if JRE and Sonar Scanner is not present in cache and also Verified the logs if JRE and Sonar Scanner are present in the cache.
5. Verified the below type of analysis (with SARIF report) are all working as expected.
   * Commit request analysis.
   * PR analysis.
   * Merge analysis.
   * SARIF reports.
6. Verified the SFDX analysis (with SARIF report) the analysis is successful and  able to generate the SARIF file locally where user is able to see the tags, rule text, results, type of the Bug and type of the Severity.
7. Verified the S3 integration the analysis is successful.
8. Verified the CodeScan extension in the Azure DEVOPS plugin on the TEST instance working as expected.
   * Verified the main/default analysis which is successful.
   * Verified the branch analysis which is successful.
9. Verified the below sonar scanner versions
   * sonar-scanner-5.0.1.3006 - Analysis is successful
   * sonar-scanner-6.0.0.4432 - Analysis is successful
   * sonar-scanner-6.2.1.4610 - Analysis is successful
   * sonar-scanner-7.1.0.4889 - Analysis is not successful (threw exception; nested exception is org.bouncycastle.crypto.fips.FipsOperationError: org.bouncycastle.crypto.fips.FipsOperationError: Module checksum failed: expected)

***

## CodeScan Release 25.1.3

**Release Date: 22 June 2025**&#x20;

Summary:

CodeScan 25.1.3 is comprised of the following 5 components:

* 3 Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### Enhancements:

**1.     New Banner in billing when license entitlements exceeded**

In this release, we created a new banner to inform admins when their licenses entitlements have been exceeded.  It advises the admins to contact their account team to get their entitlements amended.

Separately, the AutoRABIT account team will be notified directly as well.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

In the example shown, Customer X is licensed for 2 Platform Users, but currently have 4 Platform Users activated in their Org.  As such, the banner appears to advise the admins of this discrepancy.

Additionally, this new banner is coupled with additional billing logic (detailed in the next note) aimed to ensure that user operations are not disrupted when license entitlements are exceeded, providing a better user experience for our customers.



**2.     New logic in billing allows users continued operations**

In this release, we made an update so that users are not blocked when an organization exceeds their license entitlements.   Instead, a new banner will appear on the billing page advising the admins that their license entitlements have been exceeded (see previous note above).

This feature also ensures that user operations are not disrupted when license entitlements are exceeded, providing a better user experience for our customers.



**3.   Project Report Status update in UI**

Several customers had previously reported that on the Project Report page, the UI displays the Project Report as “stuck” in the queue.  This status persists even after users receive the corresponding email notification in Outlook.

We have remediated this issue with this release by updating the status in the UI to "Your project report is currently being processed.  You will receive it via email shortly."



_Verified that the 4 scenarios below are working as expected_

3.1 - "Verified: The updated message after enabling project reports and enabling the received scheduled reports in the CodeScan UI."

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.2 - "Verified: The updated message after enabling project reports and disabling the received scheduled reports in the CodeScan UI."

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.3 - "Verified: The updated message after disabling project reports in the CodeScan UI."

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.4 - Able to receive the project reports via email for all the above three case

&#x20;

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1. Fixed issue with certain menus where users were unable to easily scroll down and choose a value from the menu**

Some users were reporting that they were unable to scroll down in the quality profiles section in project settings.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

This issue has been remediated in this release.

The dialog box was resized.

We have verified that with this fix, users are able to scroll down in the Quality Profiles section within the Project Settings.  We also verified that the dialog box is resized.

&#x20;

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**2. Fixed Deprecation Warning associated with sonar.login**

Some customers were reporting that they were

receiving deprecation warnings in their scans indicating that the use of sonar.login is deprecated, and that instead, going forward, authentication should be done using sonar.token.

This issue has been remediated in this release.  CodeScan now supports both sonar.login and sonar.token for authentication during Codescan analyses.

Verified the below plugins by using sonar.token and sonar.login parameters in the sonar command and sfdx; both scenarios are working as expected.

SFDX -@salesforce/cli/2.61.8

Sonar-scanner - 5.0.1.3006V

1. Validate Project analysis through above plugins
2. Validate branch analysis.

***

## CodeScan Release 25.1.2

**Release Date: June 11, 2025**&#x20;

Summary:

CodeScan 25.1.2 is comprised of the following 19 components:

·       3 New Features

·       3 Enhancements

·       2 New Rules

·       11 Fixes

Component details are listed in their corresponding sections within this document.

&#x20;

### New Features:

#### 1. CWE Numbers Added to Vulnerability Rule “Unescaped Value Could Cause XSS”

We have added CWE Number [MITRE CWE-80](http://cwe.mitre.org/data/definitions/80.html) and additional CWE numbers (95 and 470) to the rule “Unescaped Value Could Cause XSS” &#x20;

Verified the CWE number on the rule Unescaped Value Could Cause XSS by confirming that user is able to see the added CWE Number [MITRE CWE-80](http://cwe.mitre.org/data/definitions/80.html) (along with additional CWE numbers 95 and 470)

<figure><img src="../../../../.gitbook/assets/image (1) (8).png" alt=""><figcaption></figcaption></figure>

Please note, these rules are only available for projects created with CodeScan's direct Salesforce integration due to being based on a direct query to a Salesforce Org.



**2. Disable “Invite Members" option**

Invite members is a feature in CodeScan designed for organizations using Auth0 for authentication.  In contrast, it is not applicable for SSO enabled environments.

To date, SSO customers would have access to this feature, even though the functionality would not be enabled for them.  We recognize that this can cause confusion and lessen the user experience.  As such, we have added a new option in CodeScan allowing any organization to disable the “Invite Members” functionality in CodeScan.

**Description**

The "Disable Invite Members" option in Administration > Organization Settings of CodeScan allows Organization Admins to control the visibility of the "Invite Member" button. By default, the option is active or visible. When enabled, the "Invite Member" button is hidden for users, while disabling it keeps the button visible and functional.

Verified below scenarios, all are working as expected\
\
1\. An option/toggle called "Disable Invite Members" should be available in Administration > Organization Settings of CodeScan.

<figure><img src="../../../../.gitbook/assets/image (2) (8).png" alt=""><figcaption></figcaption></figure>

2. The default behavior of the invite member option should be active or visible.

<figure><img src="../../../../.gitbook/assets/image (3) (7).png" alt=""><figcaption></figcaption></figure>

3. When the toggle is enabled, the "Invite Member" button is hidden in administration module and members page

<figure><img src="../../../../.gitbook/assets/image (4) (6).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (5) (7).png" alt=""><figcaption></figcaption></figure>

4. When the toggle is disabled, the "Invite Member" button remains visible and functional as usual in administration module and members page

<figure><img src="../../../../.gitbook/assets/image (6) (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7) (6) (1).png" alt=""><figcaption></figcaption></figure>

5. Other functionalities related to member management (e.g., viewing members, editing permissions) should remain unaffected.

<figure><img src="../../../../.gitbook/assets/image (8) (5).png" alt=""><figcaption></figcaption></figure>

6. Able to invite users to the codescan organization

<figure><img src="../../../../.gitbook/assets/image (9) (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (10) (5).png" alt=""><figcaption></figcaption></figure>

3. **Restricting Platform Integration User Access for Standard Users**

This feature ensures that standard users who manage user access cannot switch their role to a Platform Integration User, so that user permissions are maintained correctly.

Preventing Standard users with System Admin Permission from switching to a Platform Integration User role will reduce potential misconfigurations and ensure compliance with user access policies. To enforce this, we have implemented an alert and disabled the option in the UI. This will give administrators better control over role assignments and prevent unintended access changes.

On the Members page, the following alert "You are a System Admin. You are required to have a Standard User License.“ is displayed.

&#x20;Verified the Restricting Platform Integration User Access for Standard Users via the following:\
\
1\. Verified admins are able to see the alert “You are a System Admin. You are required to have a Standard User License.“ if Standard users with System Admin Permission try switching to a Platform Integration User.

<figure><img src="../../../../.gitbook/assets/image (11) (5).png" alt=""><figcaption></figcaption></figure>

2. Verified admins are able to change users from standard to platform if standard user is without System Admin Permission

<figure><img src="../../../../.gitbook/assets/image (12) (5).png" alt=""><figcaption></figcaption></figure>

3. Verified admins are able to see the alert “You are a System Admin. You are required to have a Standard User License.“ if user is owner and trying to switch from standard to platform user

<figure><img src="../../../../.gitbook/assets/image (14) (5).png" alt=""><figcaption></figcaption></figure>

### Enhancements

1\.      Enhanced rule “vf:AvoidJavaScriptScriptlets” by adding a new parameter to the rule

Historically, CodeScan has offered our “Avoid JavaScript Scriptlets” rule to inspect customer’s code and flag where there JavaScript Scriplets.&#x20;

With this release, a new parameter was introduced to allow users to choose whether to include or ignore violations related to code supporting the Lightning functions within script.

* Parameter Name: ignoreSupportingCode
* Type: Boolean (true or false)
* Default: false
* Description: This option allows users to ignore violations related to code supporting the Lightning functions within script. By default, it is set to false.

&#x20;

Verified the below scenarios for rule vf:AvoidJavaScriptScriptlets and report that all scenarios are working as expected.

1. Validated the rule with LightningFunctions and set the default value false then user is able to see the violations.
2. Validated the rule with LightningFunctions and set the value true then user is not able to see the violations which is expected.
3. Validated the rule without LightningFunctions then user is able to see the violation which is expected.
4. Validated the rule by setting the parameter ignoreSupportingCode as false/true working as expected.

<figure><img src="../../../../.gitbook/assets/image (15) (5).png" alt=""><figcaption></figcaption></figure>

1\.     Enhanced rule “Controller Naming Convention” for Apex and Visualforce

Some customers are reporting that CodeScan is flagging violations on components that should not be flagged (i.e., SandboxRefreshAdminController)

This issue is remediated in this release.

We validated the fix by:

* Creating a class file in salesforce org using UI and name the controller like in example.
* Creating a vf page in salesforce org with the controller attribute like shown in the example.
* Setting parameters for controller naming in CS, try the parameters with different cased letters ex: ConTroLLer etc.
* After scanning false positives should not be visible

&#x20;

2\.     Updated description for Deprecated rules

&#x20;

Historically, CodeScan has deprecated rules over time.  However, we recognize that we can be clearer about why the rule is being deprecated.  In this release, we have initiated this practice (and plan to adhere to this practice in the future).



**1.Update the description of deprecated Apex Rule “Use System.assertEquals instead of System.assert“ and key”sf:UseAssertEqualsInsteadOfAssertEquality” with the following:**

This rule detects unit test assertions in object references equality. Instead of using System.assert combined with "==" as an equality operator, these assertions should be made by more specific methods, like assertEquals.

This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseAreEqualInsteadOfAssertBoolean.

**2.Update the description of deprecated Apex Rule “Use System.assertEquals instead of System.assert“ and key”sf:UseAssertEqualsInsteadOfAssert” with the following:**

This rule detects Unit test assertions in object references equality. Instead of using System.assert combined with ".equals()" as an equality check, these assertions should be made by more specific methods, like assertEquals.

This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseAreEqualInsteadOfIsTrue

**3.Update the description of deprecated Apex Rule “Use System.Assert instead of System.assertEquals“ and key”sf:UseAssertInsteadOfAssertEquals” with the following:**

When asserting a value is the same as a boolean literal, use System.assert, instead of System.assertEquals.

_This rule has been deprecated, as Salesforce recommends using the Assert class for unit tests. Please remove this deprecated rule from your custom Quality Profile and instead add the rule sf:UseIsTrueInsteadOfAreEqual_

**4.Update the description of deprecated Apex Rule “Unnecessary Parentheses“ and key”sf:UnnecessaryParentheses” with the following:**

Sometimes expressions are wrapped in unnecessary parentheses, making them look like function calls.

This rule has been deprecated. Please remove it from your custom Quality Profile and instead add the rule sf:UselessParentheses as a best practice for code styling.

### New Rules:

**1.     Server Side Request Forgery**

This is a rule that checks for any changeable inputs to a url string in a method that returns a PageReference.

**Type:** Vulnerability\
**Severity:** Critical\
**Name:** Server Side Request Forgery (SSRF)\
**Key:** ServerSideRequestForgery\
**Message:** Sanitize input to avoid possible SSRF\
**Description:** This rule identifies potential Server-Side Request Forgery (SSRF) vulnerabilities by detecting unsafe URL construction and external network requests that could allow an attacker to manipulate server-side network calls.

Server-Side Request Forgery (SSRF) occurs when an attacker can influence the server to make arbitrary network requests, potentially accessing internal resources, sensitive endpoints, or bypassing security controls.

Input can be cleansed by using Id.valueOf, Date.valueOf, etc. Or escaped using String.escapeSingleQuotes().

**Parameters**\
**Name:** sanitizationMethod\
**Description:** A comma separated list of custom methods that provide input sanitization.

CWE: 918

**Test Cases with Violations**\
\
**1.Validated direct embedding of user input into a URL without sanitization, resulting in a violation (SSRF) as expected**

<figure><img src="../../../../.gitbook/assets/image (16) (5).png" alt=""><figcaption></figcaption></figure>

2.Validated unescaped dynamic input into URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (17) (5).png" alt=""><figcaption></figcaption></figure>

3.Validated that one parameter is sanitised but the other is not sanitised, still resulting in a violation (SSRF) as expected

<figure><img src="../../../../.gitbook/assets/image (18) (5).png" alt=""><figcaption></figcaption></figure>

4.Validated concatenated unsafe dynamic parameters in a URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (19) (5).png" alt=""><figcaption></figcaption></figure>

5.Validated the presence of a malicious SSRF-style payload embedded in the URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (21) (5).png" alt=""><figcaption></figcaption></figure>

6.Validated the attempt at "sanitization" using regex, which is not an approved method, resulting in a violation (Improper sanitization) as expected

<figure><img src="../../../../.gitbook/assets/image (22) (5).png" alt=""><figcaption></figcaption></figure>

Test Cases with No Violations

1\.     Validated input sanitized using Id.valueOf, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (23) (5).png" alt=""><figcaption></figcaption></figure>

2. Validated input escaped using String.escapeSingleQuotes, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (24) (5).png" alt=""><figcaption></figcaption></figure>

3. Validated that the URL starts with "/" ensuring an internal redirect, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

4. Validated date validated using Date.valueOf, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

5. Validated a static URL with no dynamic input, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

6. Validated fully escaped input and use of safe methods, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

_NOTE: The implementation currently addresses the most common scenarios related to resource injection and SSRF vulnerabilities. However, due to the dynamic and context-dependent nature of these issues—especially when influenced by external inputs, indirect references, or complex backend behaviors—there may be edge cases that are not readily identifiable or testable. These may only surface under specific configurations or data conditions._



2. **Resource Injection**

&#x20;

Prior to this new rule, CodeScan did not catch resource injection in Apex.

This is very similar to [our new rule  “Server Side Request Forgery”](https://autorabit.atlassian.net/browse/CD-6437) (also included in this release)

&#x20;

However, there are some basic things that make it resource injection and not SSRF.

`In this example:`

`public PageReference init(){`

&#x20;   `AccListString = 'INIT';`

&#x20;   `BaseObjId = system.label.MY_Label;`

&#x20;   `return null;`

`}`

&#x20;

`public PageReference prepareAccs(){`

&#x20;   `String newUrl = '/apex/maps__Maps?baseOjectId='+BaseObjId+'&recordIds='+AccListString;`

&#x20;   `PageReference p = new PageReference(newUrl);`

&#x20;   `p.setRedirect(true);`

&#x20;   `return p;`

`}`

&#x20;

Here, we are looking at resource injection because the URL is internal (starts with / )

This rule should find any external variables that are used to create dynamic internal URLs.

<figure><img src="../../../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

**Acceptance Criteria**

**Type:** Vulnerability\
**Severity:** Critical\
**Name:** Resource Injection\
**Key:** ResourceInjection\
**Message:** Sanitize input to avoid possible resource injection\
**Description:** This rule identifies potential resource injection vulnerabilities by detecting unsafe URL construction for internal network requests.

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

Verified the below scenarios are all working as expected

1. **Verified that sanitizing both BaseObjId and AccListString before URL building prevents violations.**

<figure><img src="../../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

2. **Verified that validating BaseObjId using Id.valueOf() ensures the ID is valid and safe to use in URLs.**

<figure><img src="../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

3. **Verified that input AccListString validated with regex and sanitized prevents violation.**

<figure><img src="../../../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

4. **Verified that using AccListString directly in URL without any sanitization or validation causes violations.**

<figure><img src="../../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

5. **Verified that sanitizing only BaseObjId but not AccListString leads to a violation.**

<figure><img src="../../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

6. **Verified that sanitizing the URL string after using variables has no effect, resulting in a violation.**

<figure><img src="../../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

7. **Verified that URL encoding AccListString without further format validation leads to violation**

<figure><img src="../../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

8. **Verified that replacing characters rather than proper sanitization leads to security violations.**

<figure><img src="../../../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

_NOTE: This implementation currently addresses the most common scenarios related to resource injection and SSRF vulnerabilities. However, due to the dynamic and context-dependent nature of these issues, specially when influenced by external inputs, indirect references, or complex backend behaviors—there may be edge cases that are not readily identifiable or testable. These may only surface under specific configurations or data conditions._

### Fixes

**1. Fixed issue with the CSV Export not functioning properly with all nCino projects**

We detected that some nCino projects are unable to export to CSV.  The issue occurs after 500 records are returned (where the request does not contain the necessary data).

This issue is remediated in this release.  We verified the fix and are now able to export the issues exceeding 500 records for all ncino projects (as expected)

**2. Fixed 2 issues with our SOQL Injection rule**

We have discovered that the issues flagged disappear on different lines; we have also discovered that CodeScan doesn’t find the fflib method escape.

These 2 issues are remediated in this release.

**3. Fixed issue with the rule “Page layout name contains special characters” (sfmeta:PageLayoutNaming)**

Some customers were reporting that CodeScan was flagging that their Page layout name contains special character even though they didn't add any special characters.

This issue has been remediated in this release.

**4. Fixed issue with the rule “vf:UnescapedAttributes vulnerability” {where false positive violations were being flagged}**

CodeScan suggests the remediation for this issue is to use JSENCODE() to escape values. However, some customers reported that when this is added to their code, the issue was still being flagged as a violation.  We validated the fix by:

* Verified the updated description and example under rule: vf:UnescapedAttributes vulnerability

<figure><img src="../../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

• Verified that Rule is throwing violation as expected

<figure><img src="../../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

This CodeScan rule was updated with the following changes:

**1. Changed the description to the following:**

Reflected Cross-site Scripting (XSS) occurs when an attacker injects browser executable code within a single HTTP response.

Using unescaped parameters can be a security risk. c:\* and apex:\* attributes are not checked unless they are known to cause problems. You can check other attributes by adding them to the configuration for this rule.

In Visualforce, escape methods such as JSENCODE can be used to sanitize variables as shown below.

For Aura components, sepcifically aura:unescapedHtml, make sure to sanitize variables in controllers before using them. This component is intended to output properly sanitized HTML from a trusted source. If properly handled, mark the issue as Resolved: False Positive/Won't Fix.

**2. Added the following Aura Example Bad Scenario:**

Example :

`<aura:component>`   &#x20;

&#x20; `<aura:unescapedHtml value="{!v.htmlstring}"/>.  //Bad: not recommended.`

`</aura:component>`

**5. Fixed issue with the rule “Open Redirect” (sfmeta:PageLayoutNaming) {where false positive violations were being flagged}**

Some customers reported that our current rule does not handle the use of “Network.forwardToAuthPage”

<figure><img src="../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

We remediated this issue and validated that CodeScan now throws a violation in both of these cases.

Verified the rule “Open Redirect” by validating:

* Users are able to see the violation for the use of both Network.forwardToAuthPage and PageReference

<figure><img src="../../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

More info regarding “Network class” can be found here:

[Network Class | Apex Reference Guide | Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_network.htm#apex_System_Network_forwardToAuthPage)

6. &#x20;**Fixed issue with the rule “Field Level Security Vulnerabilities” (sfmeta:PageLayoutNaming) for classes using “Without Sharing” {where false positive violations were being flagged}**

Some customers have reported an issue with CodeScan's reporting of "Permissions should be checked before accessing resource" vulnerabilities in our Apex codebase, specifically within classes that are declared without sharing.

The without sharing keyword in Apex classes causes the code to execute in system context, bypassing standard Salesforce sharing and field-level security checks. This is intentional for certain system-level operations and utility classes within our application.

However, CodeScan is flagging fields within these without sharing classes as vulnerabilities, stating "Permissions should be checked before accessing resource." This is creating an inflated number of false positives and incorrectly portraying our code's security posture.

CodeScan is designed to identify potential security issues; however, in the context of without sharing classes, these field-level security checks are redundant and misleading.

As such, the rule update in this release enables CodeScan to recognize that when a class is declared without sharing, field-level security checks are irrelevant, and the "Permissions should be checked before accessing resource" rule is suppressed for fields within without sharing classes.

<figure><img src="../../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

Note that a new parameter has been added to this rule to Ignore Without Sharing

Name: ignoreWithoutSharing\
Message: When this parameter is true, this rule ignores Field Level Security issues in all without sharing classes.\
Default: false

<figure><img src="../../../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

Appropriately, CodeScan is flagging violations properly when “with sharing” is used.

<figure><img src="../../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

7. **Fixed issue with CodeScan’s APEX parser**

Some customers reported that the CodeScan parser was incorrectly flagging valid Apex code using the UPDATE AS SYSTEM syntax as a parsing error. This was occurring because the parser doesn't recognize the AS SYSTEM portion of the UPDATE statement, leading to a ParseException and preventing accurate code analysis.

This issue has been remediated with this release.

We had previously verified the Parsing error in APEX Code for DML queries if user using UPDATE AS SYSTEM syntax would throw the parser exception.  With this fix, users are now able to see the violations as expected for the file.

Verified the below queries in Apex code that users do not get any Parser errors; instead the updated CodeScan parser is working as expected.

* INSERT AS SYSTEM
* DELETE AS SYSTEM
* UNDELETE AS SYSTEM
* UPDATE AS SYSTEM&#x20;

<figure><img src="../../../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

8. &#x20; Fixed issue with rule “Avoid running Soql and DML inside loops” {sf:AvoidSoqlInLoops}

&#x20;

Some customers reported unexpected behavior in this rule, producing false positives.

The root cause of the false positives is that when a method of an object is invoked within another method, and both methods share the same name, the current rule implementation incorrectly interprets this as a recursive call and subsequently triggers a violation.  Further, the Stack Loop trace is indefinite.

This has been remediated in this release.  The updated rule logic now handles these edge cases by checking for method image to be exactly the same (method != diffObj.method).

We have verified the fix across related and existing test cases and edge conditions by confirming that if a method of an object is invoked within another method, and both methods share the same name, the user will not see the violation (as it is false positive).

9. &#x20; **Fixed issue with rule “RequireDescriptionComponent”**

Some customers reported that the CodeScan rule “RequireDescriptionComponent” rule was not working for custom fields on standard objects.

This issue has been remediated in this release.  Previously, CodeScan offered a rule “_sfmeta:RequireDescriptionField_” which had been deprecated for this updated rule.  But the updated rule was not designed for standard objects.  When we tested the logic of the deprecated rule, we found that it could be used for reference for this update to the new rule “RequireDescriptionComponent”

The rule enhancement was verified via the below scenarios\
\
1\. Verified Custom Field on Standard Object – Missing Description

<figure><img src="../../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

2. Verified Custom Field on Custom Object – Missing Description

<figure><img src="../../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

3. Verified Standard Fields on Standard Object – Missing Description

<figure><img src="../../../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

4. Verified Custom Field on Standard Object – With Description

<figure><img src="../../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

5. Verified Custom Field( With Description) on Custom Object (Without description)

<figure><img src="../../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

**10.  Fixed issue with rule “sf: FieldLevelSecurityRule”**

&#x20;

During maintenance testing, we discovered that this rule was triggering the null pointer exception when parsed through the trigger files. In the rule logic it was searching for relevant ASTClassOrInterfaceBody to get all the constructors in that class. Since triggers don't have constructors, control flow proceeds further if we get a non-null node for ASTClassOrInterfaceBody.\
\
We updated this rule to parse the trigger files by adding extra logic to find the Trigger specific nodes (TriggerBodyDeclaration etc).

We tested the fix to the Null pointer Exception with sf: FieldLevelSecurityRule and verified we are now no longer able to see the Null pointer exception for the trigger files in the logs (as expected).

<figure><img src="../../../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

**11.  Fixed issue with Organization images displaying as large icons in the org list**

CodeScan has historically allowed images to be added under Organization settings by our customers.  These images are then displayed on the organization home page and in the Org list.  &#x20;

After we released CodeScan 25.1.0 (April 2025), customers org icon images could appear as large icons.  This issue was remediated in this release by restricting the size of the image on the Org page to the size of a usual non-image icon (around 30px).

We have verified the Organization image is now restricted in size, and users are able to see the image as expected.

<figure><img src="../../../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

***

## CodeScan Release 25.1.1&#x20;

**Release Date: May 11, 2025**&#x20;

### Summary:&#x20;

**CodeScan 25.1.1 is comprised of the following 3 components:**&#x20;

* 3 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

#### **New Features:**&#x20;

There are no New Features associated with this release&#x20;

#### **Enhancements:**&#x20;

There are no Enhancements associated with this release&#x20;

**New Rules:**&#x20;

There are no New Rules associated with this release&#x20;

### **Fixes**:

1. **Fixed an issue with rule tags blocking analyses**&#x20;

Several customers reported that, after the recent CodeScan upgrade to 25.1.0, some of their analyses were not properly executing.  We uncovered that this was due to new logic added to a database table.  This fix corrects this issue and will allow all blocked analyses to run properly.&#x20;

We have verified the below scenarios and report that all are working as expected.&#x20;

* Tags which are system default&#x20;
* Tags which are not system default&#x20;
* Custom tags&#x20;

1. Verified the vf:exception and sf:exception rule by adding tags in one organization and seeing the analysis working without any issue in that org or any other org.&#x20;
2. Verified the analysis for the rule sf:exception by assigning the tags.  Confirmed analysis was successful and that users are able to see the assigned tags in the issues page.&#x20;
3. Verified the analysis when the tags are not assigned. If there are any new violations the user is unable to see any tags for the violations (which is expected). &#x20;

&#x20;

2. **Fixed Error: \[CS] API GET status code: 404 when users try to generate Sarif File on their environment**&#x20;

Several customers reported the following error “Error: \[CS] API GET status code: 404 “when users try to generate Sarif File on their environment.&#x20;

This fix corrects this issue and will allow users to generate Sarif files on their environment.&#x20;

We have verified the below scenarios for GitHub Actions SARIF report on TEST environment and are able to generate SARIF reports successfully.&#x20;

1. Analysis is getting “success” and able to get the SARIF report where the results are same in the report and on CodeScan UI&#x20;
2. Validated the Pull request analysis in GitHub actions we are able see that the PR analysis is happening for the changed files.&#x20;

* Validated the Commit request analysis.&#x20;
* Validated the PR analysis.&#x20;
* Validated Merge analysis.&#x20;



3. **Fixed Error: \[CS] API GET status code: 404 when users try to generate Sarif File on their environment**&#x20;

**After the upgrade to 25.1.0, we uncovered 2 minor issues:**&#x20;

1. The IDP group mapping feature flag was not working as expected.&#x20;
2. If an ID user is member of org 1 and owner of org 2, then from org2 SAML connection she was able to make anyone an owner of org1.&#x20;

This update remediates these 2 issues.&#x20;

Verified the IDP Group Mapping flag by Enabling and Disabling the instance is now working as expected.&#x20;

<figure><img src="../../../../.gitbook/assets/image (1672).png" alt="" width="563"><figcaption></figcaption></figure>

***

## Release Notes 25.1.0&#x20;

**Release Date: 20 April 2025**&#x20;

### Summary:&#x20;

CodeScan 25.1.0 is comprised of three main components / features:&#x20;

* [New User Interface ](release-notes-25.1.md#new-user-interface)
* [Technical Architecture Improvements ](release-notes-25.1.md#technical-architecture-improvements)
* [Fixes](release-notes-25.1.md#fixes-1)

Component details are listed in their corresponding sections within this document.&#x20;

### New User Interface&#x20;

In this release, we have updated the CodeScan User Interface order to provide four key benefits:&#x20;

* Easier navigation, which provides both an improved, intuitive experience for more advanced users, while reducing the learning curve for new users
* Consistency in screen layout, providing a more cohesive experience throughout the application  &#x20;
* Enhanced performance and responsiveness within CodeScan&#x20;
* Brand modernization alignment with other AutoRABIT solutions&#x20;

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>UI Upgrades</p></figcaption></figure>

{% hint style="info" %}
Please note: CodeScan documentation pages will have new images to reflect the latest UI changes over the coming weeks. This should not affect the effectiveness of instruction steps in the meantime.&#x20;
{% endhint %}

### Technical Architecture Improvements&#x20;

* The CodeScan 25.1.0 contains various technical architecture improvements and upgrades to various libraries. We have also included several enhancements to CodeScan’s security architecture.

### **Fixes**:

* Fixed a false positive in the 'sf:AvoidGlobalModifier' rule. The violation is now ignored for global classes used as return types in any global static method.



&#x20;&#x20;

&#x20;

&#x20;
