---
description: Newest CodeScan Release
---

# Release Notes 24.0

## CodeScan Cloud

{% hint style="info" %}
**Exciting News! Enhanced Release Schedule for a Better Experience**

Starting **March 27, 2024**, we're thrilled to announce a new, streamlined release schedule for CodeScan! Moving forward, we'll be delivering a unified release of new features, enhancements, and architectural improvements **every two weeks**. This begins with our latest release, **24.0.3**.

**Why This Matters to You:**

* **Faster Access to New Features:** Enjoy the latest enhancements and features without the wait.
* **Stay Ahead:** Frequent updates ensure you're always using the most advanced version of CodeScan.

We're committed to enhancing your experience and ensuring CodeScan meets your evolving needs. Stay tuned for more updates!
{% endhint %}

## Release Notes 24.0.8

**Release Date: 10 July 2024**

The latest CodeScan release is comprised of  the following:

* New Features&#x20;
* Enhancements&#x20;
* Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### New Features&#x20;

This update includes several New Features and Enhancements within CodeScan’s VS Code IDE Extension: &#x20;

* New CodeScan Issue Filter: Quickly sort and filter issues by type and severity for efficient code review.&#x20;

<figure><img src="../../../../.gitbook/assets/image (1279).png" alt=""><figcaption></figcaption></figure>

* Fixed a plugin issue that caused non-recognition of CodeScan-specific JavaScript (JS) and VisualForce (VF) rules. &#x20;
* Resolved duplicate issue detection for specific Apex rules. &#x20;
* Added automatic token generation and connection flow UI. &#x20;
* Added support for SonarQube 9.9 and later versions&#x20;

### Enhancements

1. **Rule Enhancement for “Avoid Using Test.isRunningTest()” {APEX Rule}:**&#x20;

&#x20;Summary: Previously, this rule was flagging violations when finding methods written as  Test.isRunningTest(). This rule has been enhanced to also flag violations when finding methods written as System.Test.isRunningTest().&#x20;

2. **Decrease False Positives reported for Rule “sf:FixDuplicateMethods”**&#x20;

Summary: CodeScan recognizes that methods should not share the same implementations&#x20;

As such, the scope of the rule will be limited to methods with actual implementations, rather than including interface method declarations. &#x20;

This means the rule will now focus solely on detecting and addressing duplicate implementations within concrete classes, ensuring that only methods containing executable code are evaluated. &#x20;

Violations reported by this rule will now include details of all duplicate methods affected. This means each violation will list every instance of a method that shares the same implementation, making it easier to identify and resolve duplicated code. &#x20;

These updates will make the rule more precise, and its violation reports more comprehensive, enhancing its effectiveness.&#x20;

3. **Enhancement to Rule: "Field Level Security"** &#x20;

&#x20;CodeScan’s FLS rule did not detect DML methods called when syntax is insert(record), update(record), etc.&#x20;

Instead, FLS was only detecting when “insert record;” syntax was used. &#x20;

We made a parser update within CodeScan, and then an enhancement to the rule was applied which corrected the syntax detection.&#x20;

4. **Enhancement to Rule: "Field Level Security"**&#x20;

Summary: Several enhancements were applied to the rule cyclomatic complexity, including adding the decision points '?', '&&', '||', and 'catch'.&#x20;

5. **Added dashboardUrl to Job status API**&#x20;

Summary: On the Project Analysis page, we have added dashboardUrl to Job status API on success/failure of analysis:

<figure><img src="../../../../.gitbook/assets/image (1280).png" alt=""><figcaption></figcaption></figure>

### Fixes

1. UI Improvement on Rule “NullCoalescing operator”&#x20;

We have completed an alignment adjustment within the CodeScan UI for this specific rule.&#x20;

**Previous UI:**&#x20;

<figure><img src="../../../../.gitbook/assets/image (1281).png" alt=""><figcaption></figcaption></figure>

**Adjusted UI:**

<figure><img src="../../../../.gitbook/assets/image (1282).png" alt=""><figcaption></figcaption></figure>

2. UI Improvement on Rule “Lightning channel Exposed”&#x20;

We have completed an alignment adjustment within the CodeScan UI for this specific rule.&#x20;

**Previous UI:**&#x20;

<figure><img src="../../../../.gitbook/assets/image (1283).png" alt=""><figcaption></figcaption></figure>

**Adjusted UI:**

<figure><img src="../../../../.gitbook/assets/image (1284).png" alt=""><figcaption></figcaption></figure>

3. **Improved IDE Usage Tracking**&#x20;

Previously, the IDE tracking page was tracking every use of a token by a user and displaying it on this page. &#x20;

The updated functionality is: 1 entry per user, where the tracking page gets updated / refreshed when a user token is used within VS Code &#x20;

Note:  Only VS code updates on the page&#x20;

Additionally, instead of loginID , we now display the name of the user and the email under a single column called ‘User’. &#x20;

Also, we changed the title to IDE Usage instead of “IDE Usages” \* &#x20;

Finally, we removed the token information (as it is not needed). &#x20;

4. **Fixed CodeScan IntelliJ Plugin error** &#x20;

Previously, the CodeScan IntelliJ Plugin was throwing an error during binding updates when connected to SonarQube 10.&#x20;

The issue was caused from self-hosted connections being incorrectly detected as cloud connections, resulting in an error popup.&#x20;

This issue occurred when connecting to self-hosted SQ 10.x versions in both 2023 and 2024 based IntelliJ versions. The issue error message (popup) resulted from an API call failure.&#x20;

This issue has now been remedied with this fix.&#x20;

5. **Generated SARIF now associated with the branch being scanned**&#x20;

Previously, when SARIF was generated while scanning from our SFDX plugin, the SARIF was generated from the main branch of the project, and NOT the branch that is being scanned. &#x20;

This has been corrected, and now the SARIF generates from the branch of the project that has just been scanned.&#x20;

## Release Notes 24.0.7

**Release Date: 19 June 2024**

### Rule Updates&#x20;

1. The 'Hard Coded Credentials' rule name has been changed to 'Use Named Credentials' for clarity.&#x20;
2. 'Use Named Credentials' and 'Field Level Security' rules have updated descriptions highlighting Salesforce best practices and better paths to resolution.

### Bug Fixes&#x20;

Fixed a false positive in the rule 'Avoid using methods getDescribe and getMap inside Loops' when using custom methods with similar names.&#x20;

A link was fixed on the rule description pages.&#x20;

Filtering the list by project, the rule now works correctly.&#x20;

New code settings no longer switch depending on the main branch of the project; all branches can be configured independently. A warning will be shown if the setting chosen will have no effect.

## Release Notes 24.0.6

**Release Date: 5 June 2024**

### **Summary:**&#x20;

CodeScan 24.0.6 is comprised of the following 3 enhancements:&#x20;

1.  **SBOM Upgrade for ADO extension:**&#x20;

    * CodeScan currently provides an ADO extension to integrate with Azure DevOps. For this enhancement, we have upgraded components and libraries (within our SBOM), eliminating all high-severity vulnerabilities.&#x20;


2.  &#x20;**Severity added to SARIF output:**&#x20;

    * CodeScan currently generates SARIF output; however, that SARIF output in GitHub does not contain the severity. By adding severity to our SARIF output, CodeScan can now provide a more verbose presentation of the issues in GitHub. This change will provide a better experience for our customers working in GitHub Actions.&#x20;


3.  **Added more fields in our Report Header:**

    * CodeScan report header contained limited information regarding the context of the report.  This enhancement provides much more detailed information including:&#x20;



    **Field 1**&#x20;

    * Label = "Report Generation Date"
    * Value = Date report was created

    **Field 2**

    * Label = “Project Name”&#x20;
    * Value = Name of project&#x20;

    **Field 3**

    * Label = “Main Branch”&#x20;
    * Value = Name of the main branch&#x20;

    **Field 4**

    * Label = “Main Branch – Last Analysis Date”&#x20;
    * Value = Date of the last analysis of the main branch&#x20;

    **Field 5**

    * Label = “Comparison Branch”&#x20;
    * Value = Name of the comparison branch or pull request branch&#x20;

{% hint style="info" %}
NOTE: If there is not a corresponding comparison branch or pull request branch, the value should be “Not Applicable.”
{% endhint %}

**Field 6**

* Label = “Comparison Branch – Last Analysis Date”&#x20;
* Value = Date of the last analysis of the comparison branch

{% hint style="info" %}
NOTE: If there is not a corresponding comparison branch or pull request branch, the value should be “Not Applicable.”
{% endhint %}

**Field 7**

* Label = “Version”&#x20;
* Value = The corresponding version number listed in version history / measure history&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-06-01 at 9.25.18 AM.png" alt=""><figcaption></figcaption></figure>

### Changelogs

#### 27 June 2024

**v. 2.0.3**

Changes were required to support fixes and enhancements of the **VS Code CodeScan Plugin (v2.0.3)** to VS Code Extension Marketplace; specifically, we fixed a plugin issue that caused non-recognition of CodeScan-specific JS and VF rules. Support ticket #114684



**13 June 2024**

**v. 2.0.2** &#x20;

New CodeScan Issue Filter: Quickly sort and filter issues by type and severity for efficient code review. You can click on the specific _Type_ or _Severity_ to only see issues of that type.

<figure><img src="../../../../.gitbook/assets/image (567).png" alt=""><figcaption></figcaption></figure>

The released plugin can be updated directly from VSCode and also can be found in this link: [https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode](https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode)



***

## Release Notes 24.0.5

**Release Date: 15 May 2024**

### New Rules

1. **Rule Name: **_**“Comment All Hardcoded Values”**_\
   \
   **Category**: New APEX rule in CodeScan\
   \
   **Purpose**: Ensure comments are included when using hardcoded values in Apex classes\
   \
   **Detail:** Ensures any hard-coded values or strings in the code are accompanied by descriptive comments or, alternatively, use constants. This practice enhances code readability, maintainability, and will make it easier for other developers to understand the purpose of these values.\
   \

2. **Rule Name: “**_**Use the null coalescing operator instead of the ternary operator”**_\
   \
   **Category**: New APEX rule in CodeScan\
   \
   **Purpose**: CodeScan recommendation to consider replacing ternary operators (? :) for explicit null checks with the Null Coalescing operator (??) where applicable to enhance code performance and clarity.\
   \
   **Detail**: In Salesforce's Spring '24 release, the null-coalescing operator has been introduced in Apex. This rule will identify where this operator could be used but isn’t being utilized.\
   \
   For further information, please refer to Salesforce Release Documentation - [Null Coalescing Operator](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon\_apex\_NullCoalescingOperator.htm). \
   \

3. **Rule Name: “**_**Use Accessibility Attributes”**_\
   \
   **Category**: New Lightning Web Component Rule in CodeScan\
   \
   **Purpose**: Updating LWCs with certain attributes makes these components more accessible to users of assistive technology.\
   \
   **Detail**: Accessibility software such as screen readers interpret the elements on a webpage using the title attribute, so specifying a value for components is very important.\
   \
   Salesforce’s ARIA attributes allow accessibility software to gather more information on the state of the page and align with the ARIA standard.\
   \
   For further information, please refer to: \
   [Component Accessibility Attributes](https://developer.salesforce.com/docs/platform/lwc/guide/create-components-accessibility-attributes.html)\
   [Accessible Rich Internet Applications (WAI-ARIA)](https://w3c.github.io/aria/)\
   \

4. **Rule Name: “**_**nCino Inactive Workflow Rules”**_\
   \
   **Category**: New nCino Gold Standard Rule in CodeScan\
   \
   **Purpose**: Removing inactive, unmanaged workflow rules in a Salesforce instance allows organizations to maintain an organized workflow environment\
   \
   **Detail**: Removing inactive UNMANAGED workflow rules will streamline workflow processes, reduce confusion among users, and improve system performance. This action leads to a cleaner and more efficient Salesforce instance. Further, removing inactive UNMANAGED workflow rules helps declutter the Salesforce environment, making it easier for administrators and users to navigate and manage active workflows effectively.

<div align="left" data-full-width="false">

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

</div>



5. **Rule Name: “**_**Avoid JavaScript Scriptlets in Aura Components and Apex Pages”**_\
   \
   **Category**: New Aura / Lightning / Visualforce Rule in CodeScan\
   \
   **Purpose/Detail**: JavaScript scriptlets should not be directly embedded within the markup of Aura components or Apex pages. Instead, utilize Salesforce Static resources for including JavaScript code. Using direct \<script> tags in components or pages can pose a security risk, increasing the likelihood of cross-site scripting (XSS) attacks.\
   \
   For further information, please refer to: [https://developer.salesforce.com/blogs/2023/08/the-top-20-vulnerabilities-found-in-the-appexchange-security-review](https://developer.salesforce.com/blogs/2023/08/the-top-20-vulnerabilities-found-in-the-appexchange-security-review) - \
   [The Top 20 Vulnerabilities Found in the AppExchange Security Review](https://developer.salesforce.com/blogs/2023/08/the-top-20-vulnerabilities-found-in-the-appexchange-security-review)\
   [MITRE, CWE-79](https://cwe.mitre.org/data/definitions/79.html) - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')\
   \

6. **Rule Name: “**_**Exposed Lightning Message Channel”**_\
   \
   **Category**: New LWC / Aura / Visualforce rule in CodeScan\
   \
   **Purpose**: It is recommended to verify instances where the 'isExposed' flag in Lightning Message Channels is set to true. Setting this flag can lead to unintended access to the Lightning Message Service (LMS) API, potentially resulting in unauthorized message publishing and subscribing across components within the Salesforce ecosystem.\
   \
   **Detail**: This term specifically refers to cases where you have not configured the 'isExposed' flag in Lightning Message Channel to false. Since this provides access to the Lightning Message Service (LMS) API, which lets you publish and subscribe to messages across the DOM and between Aura, Visualforce, and Lightning Web Components, it should be set to false.\
   \
   For further information, please refer to: [https://developer.salesforce.com/blogs/2023/08/the-top-20-vulnerabilities-found-in-the-appexchange-security-review](https://developer.salesforce.com/blogs/2023/08/the-top-20-vulnerabilities-found-in-the-appexchange-security-review)\
   \

7. **Rule Name: “**_**Utilizing Apex Unit Tests with @IsTest(IsParallel)”**_\
   \
   **Category**: New APEX rule in CodeScan\
   \
   **Purpose**:  The annotation “@isTest(isParallel=true/false)” can be set in Apex test classes to indicate whether the particular test can be executed parallelly or sequentially (performance enhancement).\
   \
   **Detail**:  When writing Apex unit tests, ensure that the @IsTest(IsParallel) annotation is set, whether true or false. This keeps the option of running tests in parallel visible through development to optimize test execution times. However, it should only be enabled in scenarios where it adds value without introducing risks or conflicts.\
   \
   **Further information**: When utilizing Apex unit tests with the annotation @IsTest(IsParallel=true), it's essential to be aware of potential drawbacks to ensure smooth execution and accurate results. Enabling parallel testing with @IsTest(IsParallel=true) may lead to UNABLE\_TO\_LOCK\_ROW errors due to resource competition, which in turn can result in rerunning failed tests in serial mode. \
   \
   Additionally, it's important to note that this setting does not affect change set deployment or package upload processes. \
   \
   By understanding these drawbacks, developers can effectively manage test execution and deployment processes, minimizing errors, and ensuring the reliability of test results.\


### Fixes

1. **Updated the rule “Avoid duplicate conditions in "if"/"else if" and "switch" statements to eliminate dead code."**  \
   \
   **Detail**:  In the Initial implementation, the "if/else-if" statements and the nested "if/else-if" statements present within them were not allowed to have duplicate conditions. Now only the related "if/else-if" statements are checked for duplicate conditions, without considering the nested "if/else-if" statements present within them.\
   \
   **Value**: The same conditions can cause duplication and lead to dead code in statements such as "if"/"else if" and "switch." This issue often occurs due to a copy/paste error. In the best-case scenario, it results in dead code that serves no purpose, but in the worst-case scenario, it introduces bugs that may propagate as the code is maintained, potentially leading to unexpected behavior.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



2. **Updated the documentation and example on rule “API Version is Too Old” to:** “This rule identifies visual force pages which are using older versions of the API. Change the API Version of this visual force page.”\
   \
   **Reason for change**: The description and example needed to be updated for the rule.\
   \


***

## Release Notes 24.0.4

**Release Date: 21 April 2024**

### **New Features**

In this release, we've added more metadata suffixes as recognized types for Salesforce metadata:

**Newly added CodeScan logic:**

Any suffix with .\[dot] present will be treated as a correct suffix and not be modified. This means:

1. **.field-meta.xml** - will treat all files ending with .field-meta.xml as metafiles.
2. **-meta.xml** - will treat all files ending with -meta.xml as metafiles.
3. **.xml** - will treat all files with .xml suffix as metafiles.
4. **xml** - will treat all files with .xml suffix as metafiles. (.\[dot] is added at the start if not provided)

### IDE Enhancements

* Add UI element within the CodeScan Administration tab to list IDE license usage at the Org level.

<figure><img src="../../../../.gitbook/assets/image (60) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Admins are now notified within the UI when IDE licenses have exceeded the maximum allotment.

<figure><img src="../../../../.gitbook/assets/image (61) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Users are now notified in IDE when additional IDE licenses are required (i.e., the company has allocated all available licenses).

<figure><img src="../../../../.gitbook/assets/image (62) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* CodeScan now removes IDE usage records for users who have been removed from their organization’s member group.

### Fixes

* Improved the CodeScan parser as it relates to Visual Force. Specifically, the parser had some issues recognizing parts of Aura code (for example, with components (cmp), the parser was unable to recognize divs and spans across multiple lines). With this release, we have corrected these issues and verified that the Visual Force parser for .cmp, vf, xml, and .page files are all parsed properly. Further, CodeScan users can successfully see these issues after analysis.
* Fixed a NullPointerException with the Apex rule “Null Coalescing Operator.”
* Fixed an issue with New Code settings. Customers who were changing new code settings while selecting the reference branch as “main” were receiving a notification that the settings had been saved. However, the change was not reflected/applied properly to the CodeScan engine. This issue is now resolved.



***

## Release Notes 24.0.3

**Release Date: 27 March 2024**

This release has several new features that support enhanced user capabilities.

<figure><img src="../../../../.gitbook/assets/CodeScan slide 2024-04-17.jpg" alt=""><figcaption></figcaption></figure>

1. **CSV Export**: With this fix, we added a URL column to the CSV Export that enables teams to quickly navigate to the Issue and get a fix in place.
2. **CSV Export not exporting all issues**: To avoid doubling up the queries, when a user presses the **Export** button, the **Export** and **Reset** buttons are grayed out and unusable. After the buttons are clicked, the following message should show underneath: "Please remain on this page while your report is generated. Depending on the number of issues in your report, this may take up to 5 minutes. Your download will start shortly."&#x20;
3. **CSV Export added functionality – Pull Requests**: This enables CSV Exports to include the options to filter and group code issues by specific pull request(s).
4. **Quality Profile error**: A bug that caused project analysis issues is now fixed in the sfmeta:FlowNullHandler rule.
5. **NullPointerException in IdempotentBinaryOperatorsRule:** This fixes an exception when a null pointer is thrown in IdempotentBinaryOperatorRule.txt.
6. **Quick Report — Issue Counts**: This fixes a bug causing issue count errors in Quick Report.
7. **Null Pointer Exception — Apex classes**: This fixes an error causing an exception during analysis of Apex classes.
8. **Null Pointer Exception for IfElseDefaultCase Rule**: This fixes a null pointer exception thrown for triggers.
9.  **False Positives**: This fixes false positive errors for the sf:FixDuplicateConditions rule. The same conditions can cause duplication and lead to dead code in statements such as "if"/"else if" and "switch". This issue often occurs due to a copy/paste error. In the best-case scenario, it results in dead code that serves no purpose, while in the worst-case scenario, it introduces bugs that may propagate as the code is maintained, potentially leading to unexpected behavior. Addressing false positives for cases such as:

    <pre><code>public class sample{
    public static void main(){
        if(a==true){}
        else if(a == null){}

        if(super.a){}
        else if(this.a){}

        if(this.a){}
        else if(this.b){}
    }
    }
    <strong>
    </strong></code></pre>
10. **Use Relative, not Absolute URLs**: Code that uses absolute URLs for Salesforce pages will only work when running on the corresponding Salesforce instances. This can cause code to fail when deployed in another sandbox or production environment. Use relative URLs to avoid this issue.
11. **Null Pointer Exception – sf:AvoidAbsoluteURL rule**: Fixed a null pointer exception during analysis associated with the sf:AvoidAbsoluteURL rule.



***

## Release Notes 24.0.2&#x20;

**March 2024**

This update introduces several new rules and bug fixes for current rules. This includes:

1. **Apex Rules:**

* **Duplicate method implementations**: Methods should not share the same implementations. To prevent duplication and confusion, avoid using two methods with identical implementations.
* **Code length**: Lines should not be too long in APEX. Limiting the length of code lines enhances code clarity and readability by reducing complexity and improving quick understanding.
* **System.runAs to test user permissions**: To ensure accurate and realistic testing of user permissions, it is crucial to utilize System.runAs during test execution, ensuring logic is tested in the same context in which it will run.
* **Relative Salesforce URLs**: Salesforce pages should use relative URLs, as code using absolute URLs for Salesforce pages will break in different environments.
* **“If ... else if” should have “else” case**: Include a default case using an "else" statement at the end of "if" and "else if" clauses to handle all conditions and provide code clarity.
* **Limit case clauses in switch statements**: Using a large number of case clauses in switch statements creates complex, difficult-to-read code.
* **Avoid Identical Expressions on Both Sides of a Binary Operator**: When both sides of a binary operator have identical values, the condition will always give the same result.
* **Avoid Sending Emails in Loops**: Avoid using Messaging.sendEmail within loops to prevent exceeding Salesforce governor limits and to enhance application performance.
* **Avoid duplicate conditions in "if"/"else if" and "switch"**: When the same conditions are used in statements like "if"/"else if" and "switch", it can lead to duplicate or dead code.
* **API Versions 7.0 through 20.0 Retirement**: The retirement of older Salesforce Platform API versions (7.0 through 20.0) after the Summer '22 release is a critical step to ensure the continued smooth operation of Salesforce applications.
* **Avoid using methods getDescribe and getMap inside Loops**: The ‘getDescribe’ and ‘getMap’ methods typically involve fetching metadata information for objects and fields. Invoking them inside loops can result in unnecessary overhead.

2. **Assertion Rules:**

* **Use Assert.areEqual instead of Assert.isTrue**: This rule detects Unit test assertions in object references equality. Instead of using Assert.isTrue as an equality check, these assertions should be made by more specific methods, like **Assert.areEqual**.
* **Use Assert.isTrue instead of Assert.areEqual**: When asserting a value that is the same as a Boolean literal, use **Assert.isTrue**, instead of Assert.areEqual.
* **Use Assert Equals Instead of Boolean Equality Assertion**: This rule detects unit test assertions in object references equality. Instead of using Assert.isTrue combined with "==" as an equality operator, these assertions should be made by more specific methods, like **Assert.areEqual** (expected, actual).
* **Unit Assertions should include a Message**: Unit assertions should include a message. In other words, use the three-argument version of **Assert.areEquals()**, not the two-argument version.
* **Unit Test Method Contains Too Many Asserts**: Unit tests should not contain too many asserts. Many asserts are indicative of a complex test, for which it is harder to verify correctness. Consider breaking the test scenario into multiple, shorter test scenarios. Customize the maximum number of assertions used by this Rule to suit your needs.
* **Non-Unit Test Methods Should Not Contain Asserts**: Asserts should only be used in test methods.
* **Misuse of Assert Class**: Assert Class can be misused if not applied correctly. To ensure the correctness of our code and avoid common pitfalls, establish best practices for its usage.
* **Use Messages in Assert Statements**: Ensure that messages are included when using the assert method with the message parameter to improve code quality and make it easier to identify the cause of failures during testing and debugging.
* **Consider Using Assert in place of System.Assert**: This new class aims to enhance the readability and maintainability of test code for developers. It is preferable to use Assert in your tests instead of older System.Assert methods.

3. **LWC Rules:**

* **Enable Salesforce Lightning Web Security (LWS)**: Enabling LWS ensures that the Lightning components within our Salesforce instance are executed in a secure and controlled environment, reducing the risk of potential security vulnerabilities.

4. **SF Meta:**

* **Adopt the ICU Locale Formats instead of JDK locale formats**: Salesforce is retiring the JDK locale formats with the Spring ’24 release. ICU is the new standard enforced in API version 45. Make sure your custom code does not use JDK locale formats and instead uses locale-neutral methods.
* **Set Flows to Auto Layout**: Implementing auto-layout for your flows helps designers modify layouts more quickly, allowing them to iterate on their designs with greater speed. It ensures elements are perfectly aligned and evenly spaced, improving readability in complex Flows.
* **Potential Overuse of Rollup Summaries**: Ensure compliance with Salesforce's limit of 25 roll-up summary fields per object to prevent potential issues arising from exceeding Salesforce platform limits.

**Bug Fixes:**

* Improvement was provided on how to fix for the "**Deserializing JSON is Security Sensitive**" rule.
* We provided a fix on the "**sf:AvoidUsingHardCodedId**" rule not detecting hard-coded IDs as expected.
* Wrongly identified violations in specific scenarios were fixed for the "**Comments are Required"** rule.
* The rule "**sf:AvoidPublicFields"** was updated to exclude public fields with the **`@InvocableVariable`** annotation.
* We provided a fix for the rule's missing root element in "**RuleSet**."
* We provided a fix for the **"Consider removing inactive flows"** rule not working correctly.



***

### Release Notes 24.0.1 **Feb 2024**

The following items were implemented, fixed, or enhanced with this release:

* We fixed a parser issue in the "Avoid Untrusted/Unescaped Variables in DML Query" rule.
* A new rule parameter, `allowList`, was added to the "Track Usage of @SuppressWarnings" rule.
* We fixed the "Get help" action, which was not working when users clicked the plus (+) icon.
* Security tokens are now sorted by creation date.
* A fix was provided for the "Flows API Version Is Too Old" rule to prevent Null Pointer Exceptions.
