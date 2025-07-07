---
description: CodeScan Cloud Release Notes
---

# Release Notes 25.1

## Integration Requirements for CodeScan v25.1.0+

Please note that there are updated requirements for customers who are using one or more of the following to integrate with CodeScan:

* SFDX
* SonarScanner
* ADO
* VS Code
* IntelliJ&#x20;

[**Please refer to our integration requirements page for further details.**](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/integration-requirements)

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.2 - "Verified: The updated message after enabling project reports and disabling the received scheduled reports in the CodeScan UI."

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.3 - "Verified: The updated message after disabling project reports in the CodeScan UI."

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

3.4 - Able to receive the project reports via email for all the above three case

&#x20;

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1. Fixed issue with certain menus where users were unable to easily scroll down and choose a value from the menu**

Some users were reporting that they were unable to scroll down in the quality profiles section in project settings.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

This issue has been remediated in this release.

The dialog box was resized.

We have verified that with this fix, users are able to scroll down in the Quality Profiles section within the Project Settings.  We also verified that the dialog box is resized.

&#x20;

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

3. **Restricting Platform Integration User Access for Standard Users**

This feature ensures that standard users who manage user access cannot switch their role to a Platform Integration User, so that user permissions are maintained correctly.

Preventing Standard users with System Admin Permission from switching to a Platform Integration User role will reduce potential misconfigurations and ensure compliance with user access policies. To enforce this, we have implemented an alert and disabled the option in the UI. This will give administrators better control over role assignments and prevent unintended access changes.

On the Members page, the following alert "You are a System Admin. You are required to have a Standard User License.“ is displayed.

&#x20;Verified the Restricting Platform Integration User Access for Standard Users via the following:\
\
1\. Verified admins are able to see the alert “You are a System Admin. You are required to have a Standard User License.“ if Standard users with System Admin Permission try switching to a Platform Integration User.

<figure><img src="../../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

2. Verified admins are able to change users from standard to platform if standard user is without System Admin Permission

<figure><img src="../../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

3. Verified admins are able to see the alert “You are a System Admin. You are required to have a Standard User License.“ if user is owner and trying to switch from standard to platform user

<figure><img src="../../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

2.Validated unescaped dynamic input into URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

3.Validated that one parameter is sanitised but the other is not sanitised, still resulting in a violation (SSRF) as expected

<figure><img src="../../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

4.Validated concatenated unsafe dynamic parameters in a URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

5.Validated the presence of a malicious SSRF-style payload embedded in the URL, resulting in a violation (SSRF) as expected.

<figure><img src="../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

6.Validated the attempt at "sanitization" using regex, which is not an approved method, resulting in a violation (Improper sanitization) as expected

<figure><img src="../../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

Test Cases with No Violations

1\.     Validated input sanitized using Id.valueOf, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

2. Validated input escaped using String.escapeSingleQuotes, resulting in no violation as expected.

<figure><img src="../../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>UI Upgrades</p></figcaption></figure>

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
