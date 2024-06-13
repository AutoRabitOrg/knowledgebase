# Release Notes 24.0.5

## CodeScan On-Premises

### Release Notes 24.0.5

**Release Date: 7 June 2024**

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

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



2. **Updated the documentation and example on rule “API Version is Too Old” to:** “This rule identifies visual force pages which are using older versions of the API. Change the API Version of this visual force page.”\
   \
   **Reason for change**: The description and example needed to be updated for the rule.
