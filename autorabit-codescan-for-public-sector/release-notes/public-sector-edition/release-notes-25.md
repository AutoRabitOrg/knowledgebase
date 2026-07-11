# Release Notes 25

## AutoRABIT CodeScan PubSec 25.1.0 Release Notes

**Release Date: 24 December 2025**

### **Summary**

AutoRABIT CodeScan PubSec 25.1.0 is comprised of the following 4 components:

* 2 Rule Enhancements
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### Rule Enhancements

**1.     Updated the description in the APEX rule “Server Side Request Forgery (SSRF)”**

{Rule ID: sf: ServerSideRequestForgery}

**Description**:

Update the issue description for the sf:ServerSideRequestForgery rule to include data flow information once tracking is implemented.

**Hypothesis**:\
Providing a traceable flow from the input source to the request endpoint will help developers clearly identify unsafe URL usage leading to SSRF vulnerabilities.

**Value/Purpose**:\
Improves clarity and helps prioritize high-risk SSRF issues by showing the complete journey of untrusted data to outbound request logic.

Code Example:

```java
public class Negative {
  public void otherMethod() {
    String oneMore = 'somethingHere';
    init(oneMore);
  }
 
  public PageReference init(String Lastname){
      String FirstName = getName();
      try {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:Third_Party_Authorization/v1'+Lastname);
        request.setMethod ('POST');
      }
  }
}
```

**Existing Message**:

Sanitize input to avoid possible SSRF. Data Flow Trace: Negative.otherMethod: line 4

**Updated Message**:

Sanitize input to avoid possible SSRF. Data Flow Trace -

&#x20;   CALL (Negative.otherMethod: line 4)

<figure><img src="../../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

**2.     Updated the description in the APEX rule “Resource Injection” to account for detection with Source-to-Sink Tracing**&#x20;

{Rule ID: sf: ResourceInjection}

**Description**:

Updated the issue description for sf:ResourceInjection to display how untrusted input propagates to resource-loading statements, such as dynamic resource identifiers or file references.\
The new description includes the identified source.

**Hypothesis**:\
If developers can visualize which variable or parameter is used to form a resource path without sanitization, they will better understand the exploit path and fix it faster.

**Value/Purpose**:\
Increases the usability and accuracy of Resource Injection findings by offering transparent, contextual information about the data flow chain.

Code Example:

```java
public class Negative {
  public void otherMethod() {
    String oneMore = 'somethingHere';
    init(oneMore);
  }
 
  public PageReference init(String Lastname){
      String FirstName = getName();
      try {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('/Third_Party_Authorization/v1'+Lastname);
        request.setMethod ('POST');
      }
  }
}
```

**Existing Message**:

Sanitize input to avoid possible resource injection. Data Flow Trace: Negative.otherMethod: line 4

**Updated Message**:

Sanitize input to avoid possible resource injection. Data Flow Trace -

&#x20;   CALL (Negative.otherMethod: line 4)

<figure><img src="../../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

### Fixes

**1.     Fixed an issue in the APEX rule “Field-Level Security Vulnerabilities**”

{Rule ID: sf:FieldLevelSecurity}

Several customers reported that they were receiving the error message “Permissions should be checked before accessing resource SObject,” even though they were providing suitable permissions using DML and/or SOQL statements. As such, we overhauled the rule logic to address this issue and have ensured that AutoRABIT CodeScan is now recognizing the AccessLevel commands in DML calls.

We have validated this new logic and verified that no vulnerabilities were raised (which is the expected and correct behavior for this logic).

<figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

**2.     Fixed an issue in the APEX rule “Resource Injection”**

{Rule ID: sf: ResourceInjection}

Resource injections occur when user-controllable data is used to specify a resource identifier without proper validation. This rule identifies potential resource injection vulnerabilities by detecting unsafe URL construction for internal network requests. Input can be cleansed by using Id.valueOf, Date.valueOf, etc. or escaped using String.escapeSingleQuotes().

However, several customers reported that this rule was firing improperly, even when the recommended methods have been applied. After reviewing, we confirmed cases of false positives and determined that the rule required a minor update to the logic.

We verified the new logic and validated that the rule is now working as originally designed.

<figure><img src="../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

***

## AutoRABIT CodeScan PubSec 25.0.2 Release Notes

**Release Date: 28 October 2025**

### Summary

AutoRABIT CodeScan PubSec 25.0.2 is comprised of the following 3 components:

* 1 New Feature
* 2 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

**1.  Better Management of AutoRABIT CodeScan Orgs via Soft Deletion**

**Description**

With this release, when an Admin performs an organization deletion, the org is maintained for an additional 30 days to allow for restoration (if needed).

However, please note that the org will immediately become inaccessible to all members, owners, and IDE users, and any tokens associated with it become expired. The deleted organization will remain in a disabled state for 30 days and can only be restored by an Instance-level Admin during this period.

{% hint style="info" %}
Note: This soft deletion is triggered (and subsequently put into this disabled state) whether deleted by an org Admin or a platform-level Admin.
{% endhint %}

We recognize that we can improve organization lifecycle management and data governance for our customers, while also reducing accidental data loss, by allowing Admins to restore orgs within 30 days.

Once an organization is deleted:

* It will become immediately inaccessible to all non-admin users (members, owners, IDE users).
* All API tokens and access credentials associated with the organization will be expired.
* The deleted organization will be listed under a new "Deleted Orgs" section visible only to Instance-level Admins.
* The deleted org is in a disabled state and cannot be accessed, modified, or used in any IDE integrations.
* Instance-level Admins can restore the organization within 30 days of deletion.
* After 30 days, the organization is permanently deleted unless restored.
* Customers can notify us in writing to forgo the 30 days and have the instance deleted immediately, which we will perform at their request

**Value / Purpose**

* Ensures security and compliance by revoking access and expiring tokens immediately upon deletion.
* Provides control and flexibility to Instance-level Admins with a grace period for restoration.
* Prevents data loss from accidental deletions.
* Improves auditability and accountability in organization management.
* Aligns with standard enterprise-grade administrative controls.

{% hint style="info" %}
Note: Instance-level Admins and Org Admins (customers) are able to manage deleted organizations in a dedicated “Deleted Orgs” section, so they can view and restore them within a 30-day grace period.
{% endhint %}

### Fixes

**1.     Fixed issue where the IDE usage was not being captured properly**

Several customers have reported that Admins are not able to see any details in the IDE Usage screen in their Org, while others reported that while they see the records, they do not see the records in Order.

We have determined the root cause to be a JDBC exception and have fully remediated both of these issues with this fix.

We have verified the fix via the following scenarios and confirm that Admins are able to see the correct records without any errors:

1.  Admins can view all relevant details on the IDE Usage page after selecting the Individual tab.<br>

    <figure><img src="../../../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>
2.  Admins can also view the records displayed in the correct order under the All tab.<br>

    <figure><img src="../../../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
3.  When the user selects "All" and filters the data for 120 days in the IDE Usage screen, the "Show More" option appears, allowing them to scroll down and view additional records from the last 120 days.<br>

    <figure><img src="../../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>



**2.     Fix to AvoidAbsoluteURL Rule**

We have witnessed that, periodically, this rule does not seem to pick up new Salesforce URLs. As such, we updated the rule logic to detect and violate URLs matching the following patterns: \{{\*.salesforce.com\}} \{{\*.force.com\}} \{{\*.site.com\}} \{{\*.documentforce.com\}} \{{\*.marketingcloudapis.com\}}.

We have verified the fix of the AvoidAbsoluteURL rule via the following:

1. Updated the rule to detect and flag violations for URLs matching the following patterns:
   * \*.salesforce.com
   * \*.force.com
   * \*.site.com
   * \*.documentforce.com
   * \*.marketingcloudapis.com
2.  We also verified that usage of any of the below URLs in the code now triggers a violation after activating the AvoidAbsoluteURL rule.<br>

    <figure><img src="../../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>



***

## AutoRABIT CodeScan PubSec 25.0.1 Release Notes

**Release Date: 14 April 2025**

### Summary

AutoRABIT CodeScan PubSec 25.0.1 is comprised of the following 17 components:

·       4 New Features

·       2 Enhancements

·       4 Fixes

Component details are listed in their corresponding sections within this document.

### New Features

1. **Support Intelligent Prompts for A.I. LLMs**

AutoRABIT CodeScan can now generate prompts for LLMs, including Agentforce, Copilot, ChatGPT, and Claude AI.  This feature is a component of the AutoRABIT CodeScan's extension for VS Code.

**Requirements:**

Your \environment must be running version 25.0.1 (or higher).  In addition, you need to be running the latest version of the CodeScan VS Code extension (v 2.1.1), which can be downloaded here:  [https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode](https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode)

**What Problem Are We Solving?**

Adoption of AI can be challenging for companies for several reasons.  CodeScan can help catalyze your AI initiatives.

**User Benefits**

•       Generate prompt in the IDE

•       Directly update existing code with generated code

•       Ensures security issues are addressed

Verified Intelligent Prompts for cls, page, component, trigger, and cmp files, all working as expected by validating the below scenarios:

1\. Able to click generate prompt and copy it:

<figure><img src="../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

2. Able to paste the generated prompt in the Agentforce search box:

<figure><img src="../../../.gitbook/assets/image (48).png" alt="" width="563"><figcaption></figcaption></figure>

3. Able to receive the message prompt copied to clipboard after generating prompt:

<figure><img src="../../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

4. Able to receive a message stating that the file is too long; please select the impacted lines of code and click "Generate Prompt" if the selected file has more than 1,000 characters:

<figure><img src="../../../.gitbook/assets/image (50).png" alt="" width="563"><figcaption></figcaption></figure>

5. Able to copy the code generated by Agentforce as expected:

<figure><img src="../../../.gitbook/assets/image (51).png" alt="" width="563"><figcaption></figcaption></figure>

2. **CVSS Implementation for Security Vulnerabilities**

The **Common Vulnerability Scoring System** is a technical standard for assessing the severity of vulnerabilities in computing systems. Scores are calculated based on a formula with several metrics that approximate the ease and impact of an exploit. Scores range from 0 to 10, with 10 being the most severe.  In this release, CodeScan has applied this quantitative scoring to all security vulnerabilities, allowing organizations to more systematically prioritize the security remediations.

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

<figure><img src="../../../.gitbook/assets/image (53).png" alt="" width="503"><figcaption></figcaption></figure>

Verified the CVSS Category on RULES page, ISSUES page and also verified the CVSS issues for the specific analysis.

<figure><img src="../../../.gitbook/assets/image (54).png" alt="" width="495"><figcaption></figcaption></figure>

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

AutoRABIT CodeScan now allows admins to define the user type when inviting or adding a member (either "Standard User" or "Platform Integration User").  This ensures that each user is onboarded with the appropriate role, purpose, and permissions.

\
Since the system now allows for the designation of users as either Standard Users or Platform Integration Users during the invitation or member addition process, admins are now able to manage users more effectively (and thereby Ensuring Standard Users have the appropriate access (All the features of CodeScan), and Platform Integration Users are recognized distinctly for integration IDE purposes (or similar integration purposes).

**Value / Purpose:**

* Improves access control by ensuring correct user roles at the point of entry.
* Differentiates Standard Users from Platform Integration Users for better tracking and reporting.
* Enhances audit logs, billing accuracy, and license management.
* Reduces post-invite administrative tasks by setting the correct user type up front.
* Supports security and compliance needs by maintaining a clear separation between user types.

Verified the ability to define User Type While Inviting or Adding Member by validating the below scenarios:

1. Admin must be able to select the user type ("Standard User" or "Platform Integration User") when inviting or adding a member.
2. The user type selection must be a required field.

<figure><img src="../../../.gitbook/assets/image (55).png" alt="" width="563"><figcaption></figcaption></figure>

3. "Standard User" should be the default selection.

<figure><img src="../../../.gitbook/assets/image (56).png" alt="" width="539"><figcaption></figcaption></figure>

4. Selected user type must determine the role and permissions automatically:
   * Standard Users get full access to all CodeScan features.

<figure><img src="../../../.gitbook/assets/image (57).png" alt="" width="563"><figcaption></figcaption></figure>

* Platform Integration Users get limited access scoped to integration IDE tasks.

<figure><img src="../../../.gitbook/assets/image (58).png" alt="" width="563"><figcaption></figcaption></figure>

5. User type must be clearly labeled in the member management.

<figure><img src="../../../.gitbook/assets/image (59).png" alt="" width="563"><figcaption></figcaption></figure>

6. “Platform user cannot be added to the Owner group.” — should be displayed when the Owners group is selected for a Platform user. Additionally, the Send Invite button should be disabled in this case.

<figure><img src="../../../.gitbook/assets/image (60).png" alt="" width="563"><figcaption></figcaption></figure>

7. For multi-user invites, the flow should be the same as for a single invite. Invites can be sent in batches, but only for one user type at a time.

<figure><img src="../../../.gitbook/assets/image (61).png" alt="" width="563"><figcaption></figcaption></figure>

8. Able to see the standard and platform user type while adding a member to the organization

<figure><img src="../../../.gitbook/assets/image (62).png" alt="" width="563"><figcaption></figcaption></figure>

### Enhancements

1. &#x20;Add ESLint rules from @lwc/eslint-plugin-lwc

AutoRABIT CodeScan has traditionally provided ESLint rules within our Rules library.  Separately, Salesforce has an official ESLint plugin to analyze LWC code:[https://github.com/salesforce/eslint-plugin-lwc](https://github.com/salesforce/eslint-plugin-lwc).

The rules in this plugin are different to our current set and expand on it; expanding the rules in our LWC set is vital to support the needs of our customers using Lightning Web Components.

Our aim was to include all rules from the GitHub - salesforce/eslint-plugin-lwc:

Official ESLint rules for LWC repository added to our current list.  However, there are a few rules from this plugin that were not included.

Rules that weren’t added as part of LWC set:

* Disallow duplicate class members (no-dupe-class-members).  This wasn’t added because it’s a Deprecated Rule

Additionally, we did not include these 3 rules because of the Complex Parameter Type:

* Enforce wire adapters to be used with wire decorator (no-unexpected-wire-adapter-usages)
* Disallow usage of unknown wire adapters (no-unknown-wire-adapters)
* Disallow access to global browser APIs during SSR (no-restricted-browser-globals-during-ssr)

Note that all of these LWC  rules were added to our Salesforce Lightning Quality Profile.

Verified the Add Eslint rules from @lwc/eslint-plugin-lwc for the below scenarios:

* Verified the 21 rules from the [GitHub - salesforce/eslint-plugin-lwc: Official ESLint rules for LWC](https://github.com/salesforce/eslint-plugin-lwc) repository added to our Salesforce Lightning Quality Profile of javascript language.
* Verified the Description, Rule Details, Type of issue, Remediation function, Severity for all the rules.
* Verified that new rules is not included in the default Quality Profile.
* Verified that violation is thrown for all the 21 rules.

<figure><img src="../../../.gitbook/assets/image (63).png" alt="" width="503"><figcaption></figcaption></figure>

2. &#x20;**Enhancement to Apex rule “Unused Formal Parameter” {sf:UnusedFormalParameter}**

CodeScan has offered this rule since Dec 2017.  Recently a customer reported that Unused Formal parameter doesn’t find when variables used in SOQL. We replicated this issue where CodeScan flagged a variable as an unused variable, even though it is used in the SOQL string.

We have enhanced this rule to detect additional cases where string parameters are part of SOQL.  The rule now detects cases where string params are used as part of building SOQL query.

Verified the enhanced logic of rule “UnusedFormalParameter” via the following scenarios.\
\
1\. Previously, a parameter (e.g., encounterIds) used in a SOQL string (e.g., where Id in :encounterIds) was wrongly reported as unused.\
Now, this is correctly detected as usage — no violation.

<figure><img src="../../../.gitbook/assets/image (64).png" alt="" width="563"><figcaption></figcaption></figure>

2. Also verified below cases all are working as expected Verified:&#x20;
   * Parameter used in SOQL with bind variable (:encounterIds) — no violation&#x20;
   * Verified: Parameter used via clause string assembly — no violation&#x20;
   * Verified: Parameter incorrectly concatenated into SOQL string — violation&#x20;
   * Verified: Parameter declared but not used anywhere — violation

<figure><img src="../../../.gitbook/assets/image (65).png" alt="" width="518"><figcaption></figcaption></figure>

### Fixes&#x20;

1. **Fixed issue ARM users recieving an error: “Component can't be null” while running a CodeScan analysis from ARM.**

The issue is occurring in the SFDX retrieval. From ARM, when the user commits only the fields (or, for example, lookup fields), the .object-meta.xml is not retrieved. As a result, the retrieved file structure differs from what was expected. After analysing the rule’s implementation, it was found that the rule does not check if the .object-meta.xml file exists first and forcibly tries to throw the violation on the file. Hence, the "component can't be null" error is thrown. This required an engineering fix in the rule.

Note: The issue lies in one of the common methods many rules use, so this error is not confined to these two rules.

Other rules that use this method include:

<figure><img src="../../../.gitbook/assets/image (66).png" alt="" width="563"><figcaption></figcaption></figure>

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

<figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (68).png" alt="" width="555"><figcaption></figcaption></figure>

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

This had been remediated in a previous release.  The updated rule logic now handles these edge cases by checking for method image to be exactly the same (method != diffObj.method).

However, there’s more to this issue and fix!  A scenario which was earlier covered stopped working as expected as a result of the fix made above.  This new issue was reported to us, and has been fully remediated in this release by adding additional logic to the rule implementation was made to accommodate both scenarios (the pre-existing condition but also indefinite stack loop trace).

Verified the Fix for rule sf:AvoidSoqlInLoops via several scenarios, including:

Verified – SOQL inside a method (not directly in a loop) — no violation as expected

Violations are expected for the below scenarios:

1. Verified SOQL directly inside a for loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (69).png" alt="" width="474"><figcaption></figcaption></figure>

2. Verified SOQL inside nested if blocks within a loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (70).png" alt="" width="474"><figcaption></figcaption></figure>

3. Verified SOQL inside a try/catch block within a loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (71).png" alt="" width="443"><figcaption></figcaption></figure>

4. Verified SOQL in a method (or recursive call) invoked from a loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (72).png" alt="" width="563"><figcaption></figcaption></figure>

5. Verified SOQL in static helper method called from a loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (73).png" alt="" width="563"><figcaption></figcaption></figure>

6. Verified SOQL inside a while loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (74).png" alt="" width="449"><figcaption></figcaption></figure>

7. Verified SOQL inside a do-while loop — got violation as expected
8. Verified SOQL directly inside System.debug() within a loop — got violation as expected

<figure><img src="../../../.gitbook/assets/image (75).png" alt="" width="563"><figcaption></figcaption></figure>

**No Violations Expected for the following scenarios:**

1. Verified Bulkified SOQL outside the loop (e.g., in :ids) — no violation as expected
2. Verified SOQL in deep conditional logic but not inside a loop — no violation as expected
3. Verified SOQL inside try/catch block, not inside a loop — no violation as expected
4. Verified SOQL in method not called from a loop — no violation as expected
5. Verified SOQL inside interface/abstract method (called via polymorphism from loop) — no violation as expected
6. &#x20;Verified SOQL inside constructor called from a loop — no violation (as expected for shallow analyzers)



4. **Fixed issue regarding restricted access for CodeScan Platform Integration Users**

Some users were reporting that their platform integration users have the same accessibility to CodeScan as their standard users.  This issue is remediated in this release.

As a PIU (Platform Integration User) with restricted access in the CodeScan platform, PIUs should only be able to view the Account section after logging in. All other features like Project Analysis, Project View, Issues View, and Search etc. (all except Account Section) should be inaccessible.  Within the Account section, PIUs should see the following tabs:

* Profile
* Security
* Notifications
* Projects
* Organization

<figure><img src="../../../.gitbook/assets/image (76).png" alt="" width="560"><figcaption></figcaption></figure>

Additionally, the Help and Profile sections in the header should remain accessible. When clicking on the Profile icon, a pop-up should appear displaying (as shown in attached images):

* Username, Email
* My Account
* Logout Option

<figure><img src="../../../.gitbook/assets/image (77).png" alt="" width="515"><figcaption></figcaption></figure>

Verified Restricted Access for CodeScan PIUs by validating the following scenarios:

1. Verified all integration project analysis and PR analysis as a Standard user.
2. Verified all IDEs as a Platform user.
3. Verified IntelliJ, VS Code, GitHub Actions, SFDX, Sonar Scanner, and Azure as a Standard user.
4. Platform users should have access only to the My Account page.

<figure><img src="../../../.gitbook/assets/image (78).png" alt="" width="273"><figcaption></figcaption></figure>

5. Platform users should only be able to view the Projects and Organizations tabs—no actions should be permitted.

<figure><img src="../../../.gitbook/assets/image (79).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (80).png" alt="" width="563"><figcaption></figcaption></figure>

6. Both Standard and Platform users should have:

* The Help section is accessible in the header.

<figure><img src="../../../.gitbook/assets/image (81).png" alt="" width="563"><figcaption></figcaption></figure>

* The Profile section is accessible in the header.

<figure><img src="../../../.gitbook/assets/image (82).png" alt="" width="563"><figcaption></figcaption></figure>

7. On clicking the Profile icon, the Platform user should be able to see:

* Username
* Email
* My Account
* Logout option

&#x20;8\. Verified Billing & Revenue Compliance for both Standard and Platform users.

9. Users who are Standard users in some organizations and Platform Integration users in other organizations should be shown the homepage of the organizations where they are Standard users upon login.
10. If Standard users do not have a homepage, they should be shown the My Projects page (All Projects), which should only display projects from the organizations where they are Standard users.

<figure><img src="../../../.gitbook/assets/image (83).png" alt="" width="563"><figcaption></figcaption></figure>

11. User type and UI should be organization-specific. If a user switches between organizations, the UI corresponding to their user type in the selected organization should be displayed.

<figure><img src="../../../.gitbook/assets/image (84).png" alt="" width="563"><figcaption></figcaption></figure>

12. If Standard users do not have a homepage, they should be shown the My Issues page (All Issues), which should only display issues from the organizations where they are Standard users.

<figure><img src="../../../.gitbook/assets/image (85).png" alt="" width="563"><figcaption></figcaption></figure>
