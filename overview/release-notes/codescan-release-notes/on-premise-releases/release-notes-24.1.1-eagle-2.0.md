# Release Notes 24.1.1 Eagle 2.0

## CodeScan Self-Hosted/On-Premises

## Release Notes Eagle 2.0 (v. 24.1.1)&#x20;

**Release Date: November 13, 2024**

### Summary

The CodeScan On-Premises/Self Hosted Eagle 2.0 (24.1.1) edition is comprised of the following 12 components:

* [4 New Rules](release-notes-24.1.1-eagle-2.0.md#new-rules)
* [3 Enhancements](release-notes-24.1.1-eagle-2.0.md#enhancements)
* [5 Fixes](release-notes-24.1.1-eagle-2.0.md#fixes)

Component details are listed in their corresponding sections within this document.

### New Rules

1.  **New CodeScan rule to check for special characters in Page Layout Name (for example: : , ( ) ' " - & )**\
    \
    This is a new rule that checks for special characters used in a Page Layout name (note: Metadata API name: “Layout”). This rule will enforce naming conventions for Page Layouts, which are in line with Salesforce best practices as well as several existing customers’ standards. Further, this new rule will help identify components for refactoring of current Page Layouts that are incorrectly named. The rule checks layout and layout-meta.xml files for file names that include: - ! @ # $ % ^ & \* ? ' : ; ” + =

    \
    Verified the rule:PageLayoutNaming for the following scenarios:

    *   Verified the rules: Name, Key, Description, Type, Severity, Message, Tags, and Remediation.

        <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>


    *   Verified that a violation is thrown for **layout** and **.layout-meta.xml** files when file names include: **- ! @ # $ % ^ & \* ? ' : ; ” + =**

        <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
    * Verified that **NO** violation is thrown for **other file suffixes** (other than **layout** and **.layout-meta.xml** files) when file names include: **- ! @ # $ % ^ & \* ? ' : ; ” + =**
    * Verified that **NO** violation is thrown for **layout** and **.layout-meta.xml** files when file names **do not** include: **- ! @ # $ % ^ & \* ? ' : ; ” + =**\

2.  **New Rules for LWC: Added ESLint rules from @lwc/eslint-plugin-lwc**\
    \
    Expanding the rules in our LWC set is vital to support the needs of our customers using Lightning Web Components. This new set expands our list of LWC rules significantly. This library is comprised of Salesforce’s official ESLint plugin, allowing CodeScan to analyze LWC code more effectively.  Detailed documentation is available at [https://github.com/salesforce/eslint-plugin-lwc|https://github.com/salesforce/eslint-plugin-lwc](https://github.com/salesforce/eslint-plugin-lwc|https:/github.com/salesforce/eslint-plugin-lwc)\


    <div align="center"><figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

{% hint style="info" %}
**NOTE**: These following four rules were **not** added to the CodeScan library:

* no-dupe-class-members (due to it being a deprecated rule).
* Disallow access to global browser APIs during SSR (due to the complex parameter type).
* Enforce wire adapters to be used with wire decorator (due to the complex parameter type).
* Disallow usage of unknown wire adapters (due to the complex parameter type).
{% endhint %}

3.  **New Rule for APEX: “IsBlankForNullChecks”**

    \
    This is a new rule that leverages the built-in \{{isBlank\}} and \{{isNotBlank\}} methods instead of the \{{!=\}} and \{{==\}} operators to check for null or empty values.\


    This approach is especially relevant in programming environments and languages where \{{IsBlank\}} or equivalent methods are provided for more readable, maintainable, and less error-prone code. Using the \{{IsBlank\}} method for null checks improves code clarity, reduces the likelihood of bugs, and enhances maintainability compared to using the \{{!=\}} operator. Developers are less likely to encounter unexpected behavior due to differences in how null and empty values are handled. Additionally, built-in methods like \{{IsBlank\}} are optimized and tested to handle various edge cases, reducing the potential for errors compared to using the \{{!=\}} operator. It also makes the code easier to read and understand.\

4. **New Rule for LWC: “API Version is Too Old”**\
   \
   This is a new rule to ensure that all LWC components are using an acceptable API version (including the most current API version).\
   \
   Using outdated API versions can lead to compatibility issues, missed opportunities to leverage new features, and potential security vulnerabilities. This rule aims to streamline the process of identifying and updating LWC components to the latest API version. By identifying and updating LWC components to the latest API version, developers can maintain higher code quality, reduce the risk of deprecated features, and improve the overall performance and security of the application.\
   \
   Verified the new LWC rule (API Version is Too Old) for these scenarios:
   *   Verified the description, issue type, severity, message, tags, remediation, and parameters of the rule.

       <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
   *   Verified that a violation is thrown if the API version used is lower than the minimum version allowed.\


       <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
   *   Verified that a violation is thrown if the API version used is higher than the maximum version allowed.\


       <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
   * Verified that no violation is thrown when the API version is between the minimum and maximum versions allowed.

### Enhancements

1. **Enhancement to Rule for APEX: “"sf:ClassExplicitSharing” {Avoid Classes Without Explicit Sharing}**\
   \
   In order to help enforce security best practices on classes by ensuring that sharing settings ('with sharing', 'without sharing', or 'inherited sharing') are explicitly declared, CodeScan recently added a new rule to enforce sharing rules in classes. This rule helps prevent accidental data exposure and enhances code maintainability and compliance with security policies.\
   \
   However, there was a limitation on this rule causing customers to get violations flagged on interfaces. This was occurring because using “Sharing” as a keyword is not allowed on interfaces. As a result, these issues flagged on interfaces were false positives.\
   \
   This issue was addressed by updating the rule to exclude interfaces from its check for the Sharing keyword, ensuring accurate validation and preventing incorrect flags, an effective enhancement to the rule.\
   \
   Verified the rule:**ClassExplicitSharing** for the following scenarios is working as expected:
   * Verified that **NO** violation is thrown when used with/without sharing for classes.
   * Verified that a violation is thrown when **NOT** used with/without sharing for classes.
   * Verified that **NO** violation is thrown for interface class even when NOT used with/without sharing.
   * Verified that a violation is **ONLY** thrown when used with sharing for classes.\

2. **Enhancement to Rule for VF: “"vf:AvoidJavaScriptScriptlets”**\
   \
   We recognize that using direct \<script> tags in components or pages can pose a security risk by increasing the likelihood of cross-site scripting (XSS) attacks.\
   \
   Separately, but importantly, you cannot use “includeScript” to embed an Aura Application to a Visualforce page (as the $Lightning global object is not available if put in a separate .js file as a static resource). To address this, Salesforce details how to “create a component on a Page,” advising you to add your top-level component to a page using $Lightning.createComponent(String type, Object attributes, String domLocator, function callback). Note that this function is similar to $A.createComponent(), but it includes an additional parameter, domLocator, which specifies the DOM element where you want the component inserted. Access the full documentation at[https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components\_visualforce.htm](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_visualforce.htm).\
   \
   Considering both of these items together, we recognize that there was limitation on this rule where customers were getting violations flagged as false positives. This enhancement involves implementing Regex to detect the use of Lightning components within a \{{\<script>\}} tag in Visualforce pages. The rule \{{vf:AvoidJavaScriptScriptlets\}} should not trigger a violation if only Lightning components are found. However, if any additional lines of non-Lightning code are detected within the script, a violation will be raised. This ensures the proper use of Lightning components while avoiding insecure or outdated practices in scriptlets.\

3. **Enhancement to ECMA Intrinsic Methods** \
   \
   We recognize that the listed ECMA methods and their properties should be updated dynamically upon any new updates. This custom ESLint list will be maintained by CodeScan; as such, if any violation is thrown based on the ESLint Salesforce Repo, this custom ESLint library will be checked. If the latest method is available, we will not violate it, including:
   * [The Global Object](https://tc39.es/ecma262/#sec-global-object)
   * [Fundamental Objects](https://tc39.es/ecma262/#sec-fundamental-objects)
   * [Numbers and Dates](https://tc39.es/ecma262/#sec-numbers-and-dates)
   * [Text Processing](https://tc39.es/ecma262/#sec-text-processing)
   * [Indexed Collections](https://tc39.es/ecma262/#sec-indexed-collections)
   * [Keyed Collections](https://tc39.es/ecma262/#sec-keyed-collections)
   * [Structured Data](https://tc39.es/ecma262/#sec-structured-data)
   * [Managing Memory](https://tc39.es/ecma262/#sec-managing-memory)
   * [Control Abstraction Objects](https://tc39.es/ecma262/#sec-control-abstraction-objects)
   * [Reflection](https://tc39.es/ecma262/#sec-reflection)

### Fixes

1.  **Fixed issue in rule “sf:OptimizeParallelUnitTests” (IsParallel)**\
    \
    This rule is designed to ensure that isParallel is present, either True or False. Previously, when a second flag was added to a test, the rule threw a violation, e.g., @IsTest(SomeFlag=True IsParallel=False). This should not throw a violation since IsParallel is specified. Instead, something like @IsTest(SomeFlag=True) should throw a violation, as IsParallel is not specified.\
    \
    This issue was occurring because the rule detection logic was looking for “@isTest(isParallel=true/false)” annotation being defined/set individually on its own (only), but not when used in combination with other annotations.\
    \
    Not being able to detect combination annotations setting was thereby causing false positive violations.\
    \
    Various scenarios tested outcomes for the rule BEFORE the fix was added:

    1. Not setting “@isTest(isParallel=false)” (or true) – Violation – Correct behavior.
    2. Setting @isTest(isParallel=false) or @isTest(isParallel=true) – No violation – Correct behavior.
    3. Setting @isTest(OnInstall=true isParallel=False) – Violation – Incorrect behavior as isParallel is set.
    4. Setting @isTest(SeeAllData=False isParallel=True) – Violation – Incorrect behavior as isParallel is set.

    \
    Results demonstrated that scenarios a and b were working as expected; however, in scenarios c and d, the rule was not able to understand multiple combined annotations format of @IsTest(xxx=false yyy=true)\
    \
    &#xNAN;_&#x54;his fix corrects the issue._\
    \
    We have verified the Apex rule sf:OptimizeParallelUnitTests via multiple scenarios, and all are working as expected.\


    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

    \


    <figure><img src="../../../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  **Fixed issue in rule for VF “vf:AvoidExternalResources”** (in which the rule was checking **ALL** attributes for external resources, producing false positives).\
    \
    Previously, the rule vf:AvoidExternalResources was checking **ALL** attributes for external resources, which it should not do. This resulted in false positives being flagged as violations.\
    \
    This fix ensures that the check is limited to the **“value”** attribute only, to avoid false positives and ensure the rule functions as intended.\
    \
    As an example, the following will NOT be flagged as a violation:

    * \<apex:includeScript value="{!$Resource.example\_js}" loadOnReady="true"/>    //Good: Uses a static resource.


3.  **Fixed issue in APEX rule “sf:AvoidPublicFields”, in which issues were being flagged on private classes (which are false positives)**

    \
    The rule sf:AvoidPublicFields identifies when public fields are used and flags them as issues. Two of the three reasons this rule is important are:&#x20;

    * The internal representation is exposed, and thus cannot be easily changed.
    * When the value is changed in an unexpected way (for example nulled), the implementation may not handle it correctly.

    But these are not concerns when those public fields are on a private class.

    &#x20;

    This enhancement adds a private class validation check first and will not flag these two issues if the class is a private class.\

4. **Fixed issue in rule for APEX “sf: \{{FieldLevelSecurity\}}”** **(Permissions should be checked before accessing resource).** \
   \
   Previously, this rule was throwing violations that were false positives. This was occurring when an SOQL query having an inner query calls the related Object. The Object needs to be checked by using isAccessible() before accessing its data.\
   \
   As per Salesforce documentation, when checking the Access for the inner query object, it allows to check by using \_\_c, but while making inner query on related Objects, it must be in plural and end with \_\_r.\
   \
   &#xNAN;_&#x54;his fix corrects this issue._  In this enhancement, the Object is checked by using isAccessible() before accessing its data.\
   \
   We also added support for the SYSTEM\_MODE in this rule. A new parameter has been added, allowing users to choose true or false to include or ignore violations related to SYSTEM\_MODE.\
   \
   We have verified the rule:**FieldLevelSecurity** for the following scenarios:
   * Rule throws the violation when the object is NOT checked via isAccessible for the methods used in inner query.
   * Rule is NOT throwing a violation if the system mode value is set = “true” (and the object IS NOT checked via isAccessible for methods).
   * Rule is NOT throwing a violation if the system mode value is set = “false” (and the object IS checked via isAccessible for the methods).\

5.  **Fixed issue in rule “sf:FixDuplicateMethods”, in which nested statements were being flagged (which was a false positive issue).**\


    Previously, the sf:FixDuplicateMethods rule was throwing violations for nested statements, which is not the intended behavior. The root cause was identified and fixed, and now the rule is working as designed and expected.

