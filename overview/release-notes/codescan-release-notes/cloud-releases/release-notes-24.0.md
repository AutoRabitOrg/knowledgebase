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

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../../../../.gitbook/assets/image (60) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Admins are now notified within the UI when IDE licenses have exceeded the maximum allotment.

<figure><img src="../../../../.gitbook/assets/image (61) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Users are now notified in IDE when additional IDE licenses are required (i.e., the company has allocated all available licenses).

<figure><img src="../../../../.gitbook/assets/image (62) (1) (1).png" alt=""><figcaption></figcaption></figure>

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
