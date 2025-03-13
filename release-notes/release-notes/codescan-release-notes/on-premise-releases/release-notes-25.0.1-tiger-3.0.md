# Release Notes 25.0.1 Tiger 3.0

### Summary:

CodeScan Self-Hosted (versions 25.0.1 (Tiger v3) and 25.1.0 (Eagle v3) are comprised of the following 8 components:

[·       3 Enhancements](release-notes-25.0.1-tiger-3.0.md#enhancements)

[·       1 New Rule](release-notes-25.0.1-tiger-3.0.md#new-rules)

·       4 Fixes

Component details are listed in their corresponding sections within this document.

### Enhancements:

1. **Enhanced rule “Avoid Untrusted/Unescaped Variables in DML Query" to account for potential SOQL injections when “queryWithBinds” is used.**

Historically, CodeScan has offered our “Avoid Untrusted/Unescaped Variables in DML Query” rule to inspect customer’s code and flag where there are SOQL Injection possibilities.  Recently, one of our customers had performed a test and expected this rule to flag an issue in their code, but it did not.  We determined that the rule should be enhanced for when “queryWithBinds” is used.

Our engineering team utilized specifications within Salesforce documentation (specifically,  [Help And Training Community](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_bind_var_soql.htm\&release=242\&type=5)) in order to consider only the query for executed with queryWithBinds() for vulnerability check and violation, avoiding the other parameters such as: (Map, accessLevel) .\
Database.queryWithBinds(query, bindVariablesMap, accessLevel)

Example:

<figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Verified that after the rule enhancement was engineered, users are able to see the violation for rule “Avoid Untrusted/Unescaped Variables in DML Query” as expected

<figure><img src="../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

2. **Enhancement to our disconnected license type for self-hosted customers requiring a license with a project key embedded**

Codescan has a disconnected license type option for self-hosted license where the project key is embedded.

This feature ensures that when the license check is performed, if the project being scanned has a key that is embedded in the license, then the check will pass without needing to reach out to the license server.  This is very useful for customers who are not allowed any connection to sites outside their organization, as it allows the project analysis to complete without connecting to the license server.

Recently, some customers were reporting that while the scans were completing but also throwing a timeout error.  We have enhanced this feature by changing this notification to occur as a warning log instead of as an error log.

&#x20;

3. **Enhanced rule “Field Level Security Vulnerabilities”:  Violation message now displays the correct object instead of '{0}'.**

The existing violation message was neither clear nor accurate.  Instead, when the violation is flagged, the message should display the correct object instead of '{0}'.

This fix includes a more clear and accurate message associated with the violation.

<figure><img src="../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### New Rules:

1\.     New Rule for APEX: “OuterClassExplicitSharing”

Enforce security best practices on classes by ensuring that sharing settings ('with sharing', 'without sharing', or 'inherited sharing') are explicitly declared. This prevents accidental data exposure and enhances code maintainability and compliance with security policies.



Name: Outer Class Explicit Sharing

Key: OuterClassExplicitSharing

Type: Vulnerability

Severity: Major

Message: Class '{className}' does not have an explicit sharing rule

Tags: convention

Remediation: 5 minutes

&#x20;

Verified the rule:OuterClassExplicitSharing for the below scenarios:

\
1\. Verified the Rule’s description, type, severity, message, tag, Remediation, Key, Name

<figure><img src="../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

2. Verified that rule is not throwing violation if with sharing, without sharing, inherited sharing is used

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

3. Verified that violation is thrown if with sharing, without sharing, inherited sharing is not used.

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

_**NOTE 01:**_ This rule overlaps with the ClassExplicitSharing rule and will always overlap violations for outer classes.  This rule has been created to:

* allow for the reporting of this issue as a Vulnerability instead of as a code smell
* only flag if sharing settings are missing for outer classes (inner classes that are missing sharing settings will not be flagged (which is opposite to how the ClassExplicitSharing rule works)

_**NOTE 02:**_ If both are active, check the violations that have been reported and disable one of the rules as necessary

### Fixes

1\.     Fixed rule “Require CSRF protection on GET requests” to distinguish Visualforce Page settings from Aura components

Previously, this rule was flagging violations on .cmp files that are aura:component files. The guidance in the rule suggested to change the Visualforce page setting, but this is not possible on Aura components because they are not Visualforce components.

This fix for the rule “Require CSRF protection on GET requests” now enables CodeScan to distinguish Visualforce Page settings from Aura components

&#x20;

2\.     Fixed issue with rule “Flow DML Should Not Be Called In Loops"

Recently, we observed that the rule “Flow DML Should Not Be Called In Loops" throws null pointer exception because of access of parent node without null check.

This fix corrects this issue.

Verified the fix by testing and confirming that the rule now throws a violation as expected, and, additionally, we are no longer getting the null pointer exception.

&#x20;

3\.     Fixed issue in rule for APEX “sf: \{{FieldLevelSecurity\}} ” {Permissions should be checked before accessing resource }.

Previously, this rule was throwing violations that were false positives.  This was occurring when a SOSL query having an inner query calls the related Object. The Object needs to be checked by using isAccessible() before accessing its data.

&#x20;

_NOTE 01: We addressed a similar issue related to SOQL queries in a previous release.  That update has been extended in this release to also include SOSL queries._

&#x20;

As per Salesforce documentation, when checking the Access for the inner query object it allows to check by using \_\_c, but while making inner query on related Objects it must be in plural and end with\_\_r.

_This fix corrects this issue._  In this enhancement, the Object is checked by using isAccessible() before accessing its data.

&#x20;

Verified the rule “Field Level Security Vulnerabilities” for the below scenarios

1. Rule is throwing the violation if we didn’t check isAccessible for the objects used in inner query

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

2. Rule is not throwing the violation if we checked isAccessible for the objects used in inner query.

<figure><img src="../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

