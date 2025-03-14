# Release Notes 24.1.0 Eagle

## Release Notes Self-Hosted (On-Prem) 24.1.0 - EAGLE Edition

**August 29, 2024**

### Summary

CodeScan Self Hosted 24.1.0 is comprised of the following 8 components:

* 4 [Enhancements](release-notes-24.1.0-eagle.md#enhancements)
* 2 [New Rules](release-notes-24.1.0-eagle.md#new-rules)
* 1 [Fix](release-notes-24.1.0-eagle.md#fixes)
* [New Configuration Settings](release-notes-24.1.0-eagle.md#new-configuration-settings)

Component details are listed in their corresponding sections within this document.

### Enhancements

1.  **Feature Enhancement: The “sf.testfile” parameter in project settings UI**\
    \
    Summary:  Previously, customers using our Git integration could store their test coverage in their repo branches by using a parameter called sf.testfile (which allows people to add coverage to their code with SFDX JSON outputs)\
    \
    With this enhancement, CodeScan now allows for the parameter to be configured (at the project or instance level) within the UI (in General Settings ->CodeScan section).\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1498).png" alt=""><figcaption></figcaption></figure>

Adding this parameter will allow teams that work like this to view the coverage on the CodeScan dashboard. The addition of this parameter notably provides more value for SFDX workflows.

Further details are within the following article: [https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|smart-link](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|https:/knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/codescan-sfdx-plugin/importing-code-coverage-from-sfdx-projects|smart-link)&#x20;

2. **Enhancement to rule: “Use the null coalescing operator instead of ternary”**\
   \
   The original aim of this rule is to identify ternary statements and suggest the potential use of "??" operator.  Previously, CodeScan was checking for ternary statements only.\
   \
   This rule was originally developed according to common development practices in Salesforce where most usages would be in ternary. However, it can be applied in scenarios involving if-else and return statements.  As such, we have adjusted the rule to account for these use cases. With this enhancement, CodeScan suggests where null coalescing could be used instead of an “if” block (recognizing that if a developer is already thinking about shortening their code with ternary, then they are likely to be considering null coalescing operator as well).
3. **Enhancement to rule: “Validation Rule Must Reference Product”**\
   This existing CodeScan rule was enhanced to be compatible with SFDX.\
   \
   &#xNAN;_&#x50;lease note that this rule update is part of a larger initiative where we are making “validationRules of CustomObject” Compatible with SFDX._\
   \
   All Metadata rules need to be checked that they support both metadata API and SFDX formats of the issue they were built to find.\
   \
   Metadata pulled with SFDX has a different structure than Metadata pulled with Salesforce’s Metadata API. CodeScan can scan this different structure with some additions to the sf-meta suffixes. However, we need to make sure that the differences are covered within the types of metadata that have these differences. For example, the Object metadata contains all field metadata when pulled from the metadata API. When this is pulled with SFDX, the object and field metadata are separate.\
   \
   See the following SF article for details of these differences:[https://developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|https://developer.salesforce.com/docs/atlas.en-us.sfdx\_dev.meta/sfdx\_dev/sfdx\_dev\_source\_file\_format.htm|smart-link](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_file_format.htm|https:/developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_file_format.htm|smart-link)NOTE: This rule is only applicable to nCino customers.&#x20;
4. **Enhancement to rule “Misuse of Assert Class”**\
   This CodeScan rule was introduced in Self-Hosted version 24.0.8.  It is comprised of several parameters. This enhancement ensures that a newly created instance is never null. \
   With the fix, a violation is now thrown at the line in bold. \
   Example:\
   public class nullCheck {\
   public void checkOtherClassInstance() {\
   Assert.isNull(new OtherClass()); \
   }\
   }\
   (where the parameter associated with this enhancement is nullCheck)

### New Rules

1. **New Rule for “Cognitive Complexity” in CodeScan**\
   This is a new rule for assessing Cognitive Complexity. This rule aims to enhance the understanding of code readability and maintainability by identifying areas where the cognitive load on developers may be high.\
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
     * \# Hybrid - assessed on control flow structures that are not subject to a nesting increment, but which do increase the nesting count&#x20;
2. **New Rule for APEX: “Avoid Classes Without Explicit Sharing”**\
   New Rule to Enforce Sharing Rules in Classes\
   Summary:  Enforce security best practices on classes by ensuring that sharing settings ('with sharing', 'without sharing', or 'inherited sharing') are explicitly declared. This prevents accidental data exposure and enhances code maintainability and compliance with security policies.

### Fixes

1. Fixed issue in rule “sf:AvoidSoqlInLoops”\
   This CodeScan rule was found to have 2 issues:
   * SOQL in the code does not appear to be in a loop, but CodeScan is flagging as a violation
   * A violation message is displayed multiple times for the perceived detected violation

The root causes of these issues were identified, and the following enhancements were added:

Top of Form

Added condition to check if the method call is matching to the Method name; if not, do not flag as a violationBottom of Form

Top of Form

·       When checking the nested method call, if method name matches, only then it will throw violation.

·       Bottom of Form

Top of Form

·       Avoid false positive when a recursive call happens without matching to the method name

### **New Configuration Settings**

We are excited to announce that CodeScan now supports SonarQube versions 10.4, 10.5 and 10.6. In\
order for the Self-Hosted plug-in to function properly, the following configuration settings are introduced.\
\
They are:

·       sonar.lang.patterns.sf  (Replacement for sf.apex.suffixes)

·       sonar.lang.patterns.sfmeta (Replacement for sf.sfmeta.suffixes)

·       sonar.lang.patterns.vf (Replacement for sf.vf.suffixes)

These properties have the same defaults as those of the existing ones. These properties offer more control than the previous ones as they support wildcards.\
To learn more about wildcards, refer to the Wildcards section in [https://knowledgebase.autorabit.com/product-guides/codescan/report-and-analysis/analysis-scope-on-codescan-cloud](https://knowledgebase.autorabit.com/product-guides/codescan/report-and-analysis/analysis-scope-on-codescan-cloud)

<figure><img src="../../../../../.gitbook/assets/image (1496).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1497).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1493).png" alt=""><figcaption></figcaption></figure>
