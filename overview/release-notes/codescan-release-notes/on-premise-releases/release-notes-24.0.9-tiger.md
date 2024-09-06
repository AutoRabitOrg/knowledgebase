# Release Notes 24.0.9 Tiger

## Release Notes Self-Hosted (On-Prem) 24.0.9 (TIGER edition)&#x20;

**September 05, 2024**

### Summary

CodeScan Self Hosted 24.0.9 is comprised of the following 10 components:

* 4 [Enhancements](release-notes-24.0.9-tiger.md#enhancements)
* 3 [New Rules](release-notes-24.0.9-tiger.md#new-rules)
* 3 [Fixes](release-notes-24.0.9-tiger.md#fixes)

Component details are listed in their corresponding sections within this document.

### Enhancements

**1.     Feature Enhancement: The “sf.testfile” parameter in project settings UI**

Summary:  Previously, customers using our Git integration could store their test coverage in their repo branches by using a parameter called sf.testfile (which allows people to add coverage to their code with SFDX JSON outputs).

With this enhancement, CodeScan now allows for the parameter to be configurable at a project level.  The addition of this parameter will allow teams that work like this to view the coverage on the CodeScan dashboard. The addition of this parameter notably provides more value for SFDX workflows.

Further details are within the following article: [https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|smart-link](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|https:/knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|smart-link)

**2.     Enhancement to rule “Use the null coalescing operator instead of ternary”**

The original aim of this rule is to identify ternary statements and suggest potential use of "??" operator.  Previously, CodeScan was checking for ternary statements only.

This rule was originally developed according to common development practices in Salesforce where most usages of this would be in ternary. However, it can be applied in scenarios involving if-else and return statements. As such, we have adjusted the rule to account for these use cases. With this enhancement, CodeScan suggests where null coalescing could be used instead of an “if” block (recognizing that if a developer is already thinking about shortening their code with ternary, then they are likely to be considering null coalescing operator as well).

**3.     Enhancement to rule: “Validation Rule Must Reference Product”**

This existing CodeScan rule was enhanced to be compatible with SFDX.

_Please note that this rule update is part of a larger initiative where we are making “validationRules of CustomObject” Compatible with SFDX_

All Metadata rules need to be checked that they support both metadata api and sfdx formats of the issue they were built to find.

Metadata pulled with SFDX has a different structure than Metadata pulled with Salesforce’s Metadata API. CodeScan can scan this different structure with some additions to the sf-meta suffixes. However, we need to make sure that the differences are covered within the types of metadata that have these differences. For example, the Object metadata contains all field metadata when pulled from the metadata API. When this is pulled with SFDX, the object and field metadata is separate.

See the following SF article for details of these differences:[https://developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|https://developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|smart-link](https://developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|https:/developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|smart-link)

&#x20;NOTE:  This rule is only applicable to nCino customers

**4.     Enhancement to rule “Misuse of Assert Class”**

&#x20;This CodeScan rule was introduced in Self Hosted version 24.0.8.  It is comprised of several parameters.  This enhancement ensures that a newly created instance is never null.&#x20;

With the fix, a violation is now thrown at the line in bold.&#x20;

Example:\
public class nullCheck {\
public void checkOtherClassInstance() {\
Assert.isNull(new OtherClass()); \
}\
class OtherClass {\
public void doSomething() {\
System.debug('Doing something in OtherClass');\
}\
}\
}

(where the parameter associated with this enhancement is nullCheck)

### New Rules

1. **New Rule for “Cognitive Complexity” in CodeScan**\
   This is a new rule for assessing Cognitive Complexity. Note that we had a previous Cognitive Complexity rule.  What’s different is that this rule aims to enhance the understanding of code readability and maintainability by identifying areas where the cognitive load on developers may be high.\
   \
   Hypothesis:  By introducing a new rule for Cognitive Complexity assessment in CodeScan, we expect to pinpoint specific code structures and circumstances that contribute to increased cognitive load. This will enable developers to refactor complex sections of code, leading to improved code quality, readability, and maintainability.\
   \
   Basic criteria and methodology:  A Cognitive Complexity score is assessed according to three basic rules:
   * \# Ignore structures that allow multiple statements to be readably shorthanded into one
   * \# Increment (add one) for each break in the linear flow of the code
   * \# Increment when flow-breaking structures are nested Additionally, a complexity score is made up of four different types of increments:
     * \# Nesting - assessed for nesting control flow structures inside each other
     * \# Structural - assessed on control flow structures that are subject to a nesting increment, and that increase the nesting count
     * \# Fundamental - assessed on statements not subject to a nesting increment
     * \# Hybrid - assessed on control flow structures that are not subject to a nesting increment, but which do increase the nesting count
2. **New Rule for APEX: “Avoid Classes Without Explicit Sharing”**\
   New Rule to Enforce Sharing Rules in Classes\
   Summary:  Enforce security best practices on classes by ensuring that sharing settings ('with sharing', 'without sharing', or 'inherited sharing') are explicitly declared. This prevents accidental data exposure and enhances code maintainability and compliance with security policies.
3. **New Rule for APEX: “IsBlankForNullChecks”**\
   This is a new rule that leverages the built-in \{{isBlank\}} and \{{isNotBlank\}} methods instead of the \{{!=\}} and \{{==\}} operators to check for null or empty values.\
   \
   This approach is especially relevant in programming environments and languages where \{{IsBlank\}} or equivalent methods are provided for more readable, maintainable, and less error-prone code.  Using the \{{IsBlank\}} method for null checks improves code clarity, reduces the likelihood of bugs, and enhances maintainability compared to using the \{{!=\}} operator. \
   \
   Developers are less likely to encounter unexpected behavior due to differences in how null and empty values are handled.  Additionally, built-in methods like \{{IsBlank\}} are optimized and tested to handle various edge cases, reducing the potential for errors compared to using the \{{!=\}} operator. It also makes the code easier to read and understand.

### Fixes

1.  Fixed issue in rule “sf:AvoidSoqlInLoops” \
    This CodeScan rule was found to have 2 issues:

    * SOQL in the code does not appear to be in a loop, but CodeScan is flagging as a violation
    * A violation message is displayed multiple times for the perceived detected violation

    The root causes of these issues were identified, and the following enhancements were added:

    * Top of Form
    * Added condition to check if the method call is matching to the Method name; if not, do not flag as a violationBottom of Form\
      \
      Top of Form
    * When checking the nested method call, if the method name matches, only then will it throw a violation.
    * Bottom of Form
    * Top of Form
    * Avoid false positives when a recursive call happens without matching the method name.
2.  Fixed issue in rule “sf:AvoidPublicFields”, where issues being flagged on private classes(which are false positives).\
    \
    The rule sf:AvoidPublicFields identifies when public fields are used, and flags them as issues. Two of the three reasons this rule is important are:

    * The internal representation is exposed, and thus cannot be easily changed
    * When the value is changed in an unexpected way (for example nulled), the implementation may not handle it correctly

    But these are not concerns when those public fields are on a private class.\
    This enhancement adds a private class validation check first, and will not flag the 2 aforementioned issues if the class is a private class.
3. Fixed issue in rule “sf:FixDuplicateMethods”, where Nested statements were being flagged (which was a false positive issue).\
   \
   Previously, the sf:FixDuplicateMethods rule was throwing violations for nested statements, which is not the intended behavior. Root cause was identified and fixed, and now the rule is working as designed and expected.
