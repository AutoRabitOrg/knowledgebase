# Release Notes 24.0

## CodeScan Cloud

{% hint style="info" %}
**27 March 2024**: Please note that CodeScan has implemented a new unified dev and release plan, with **releases occurring bimonthly** rather than on a quarterly basis for major feature / architecture releases, periodic minor releases, and weekly maintenance releases. This updated release schedule begins with the 24.0.3 iteration.
{% endhint %}

### Release Notes 24.0.3

**Release Date: 27 March 2024**

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

### Release Notes 24.0.2&#x20;

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
