---
description: Newest CodeScan Releases
---

# Release Notes 25.0

## CodeScan Cloud

## Release Notes 25.0.2&#x20;

**Release Date: 5 February 2025**&#x20;

### Summary&#x20;

CodeScan 25.0.2 is comprised of the following 4 components:&#x20;

* [1 New Feature](release-notes-25.0.md#new-feature)&#x20;
* [1 Enhancement](release-notes-25.0.md#enhancement)&#x20;
* [2 Fixes ](release-notes-25.0.md#fixes)

Component details are listed in their corresponding sections within this document.&#x20;

### New Feature&#x20;

1. **Added “Security Hotspots” in CSV Export** \
   \
   We have had a long-standing capability to export issues directly from the CodeScan user interface. However, there was not the ability to export Hotspots. \
   \
   With this new feature, we have added a new page in the CodeScan UI that allows users to directly export Hotspots.  And, similar to exporting issues, this can be done at the branch or PR level.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.40.53 PM.png" alt="" width="563"><figcaption><p>Hotspots Export</p></figcaption></figure>

{% hint style="info" %}
Please note that if the Status selected is **Reviewed**, then the Resolution field is also added as a selectable input.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.43.00 PM.png" alt="" width="563"><figcaption><p>Export Dropdown</p></figcaption></figure>

Further, to make navigation clearer and easier for users, we have renamed the existing CSV export page to “CSV Issues Export”, which is separate from the new “CSV Security Hotspots Export” page. Both pages can be opened under the “More” tab (as long as the user has the proper permissions).



<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.29 PM.png" alt="" width="563"><figcaption><p>More Dropdown</p></figcaption></figure>

Finally, we verified the following scenarios:&#x20;

* Verified that we are able to export security hotspot issues of a selected project. &#x20;
* Verified that all the required fields were included in the exported CSV with correct data.
* Verified that the resolutions are visible only when the status **Reviewed** is selected.&#x20;

### Enhancement&#x20;

1. **Enhanced rule “Avoid Classes Without Explicit Sharing" to account for interfaces**  \
   \
   Previously, CodeScan did not consider interfaces when flagging violations.  As such, the rule "sf:ClassExplicitSharing" was generating a false positive when applied to interfaces, as the Sharing keyword is not allowed on interfaces in Salesforce.  \
   \
   This issue has been remediated. We have updated the rule to exclude interfaces from its check for the Sharing keyword, ensuring accurate validation and preventing incorrect flags.  \
   \
   We have verified the rule: "sf:ClassExplicitSharing" for the following scenarios:&#x20;
   * Violation is not thrown if we use with/without sharing for classes.&#x20;
   * Violation is thrown if we don’t use with/without sharing for classes.&#x20;
   * Violation is not thrown for an interface class, not even when used with/without sharing. &#x20;
   * Violation is thrown if we only use sharing for classes.&#x20;

### New Rules

There are no new rules associated with this release.

### Fixes&#x20;

1. **Fixed issue with “Project Search” in CSV Export (within the CodeScan UI)**  \
   \
   Recently, we added a search function to the dropdown on the CSV export page to allow users to search for the name of the project they wish to export.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.43 PM.png" alt=""><figcaption><p>CSV Export</p></figcaption></figure>

Several customers reported an issue when selecting a project in the new Project Search Window.&#x20;

This updated fully remediates this reported issue.   &#x20;

Further, we have validated the CodeScan export issue is resolved via the following scenario:&#x20;

* Users are able to select the projects in the Project Search Window (on the CSV export page) as expected. &#x20;

2. **Fixed an issue with some users being unable to be converted to SAML when not assigned to a SAML org.** \
   \
   Some users were receiving the following error:&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.50 PM.png" alt="" width="563"><figcaption><p>Error Msg</p></figcaption></figure>

This was occurring when a user who had previously been either an Auth0 user or an SQ native user was attempting to log in via SAML, but the user is not part of the SAML org. This was occurring because CodeScan had been operating under the assumption that the user had previously logged in to CodeScan at least one time previously.&#x20;

This assumption, which triggered the issue, has been fully corrected with this fix.&#x20;

## Release Notes 25.0.1

**Release Date: 29 January 2025**

### **Summary**

CodeScan 25.0.1 is comprised of the following 11 components:

* [3 New Features](release-notes-25.0.md#new-features-1)
* [4 Enhancements](release-notes-25.0.md#enhancements-1)
* [1 New Rule](release-notes-25.0.md#new-rules-1)
* [3 Fixes](release-notes-25.0.md#fixes-1)

Component details are listed in their corresponding sections within this document.

### New Features

1. **Added nCino module**\
   \
   The new nCino module contains rules that scan your metadata and directly query your Salesforce org to find issues and inconsistencies with your nCino configuration.\
   \
   Please note, a portion of these rules are only available for projects created with CodeScan's direct Salesforce integration due to being based on a direct query to a Salesforce Org.
2. **nCino Rules Activation**\
   \
   Create a project analysis with the Salesforce Org that includes nCino objects. Select the nCino-specific built-in profile and run the project analysis.\
   \
   Users can choose the built-in nCino Quality Profile consisting of nCino-specific and nCino-goldstandard rules in Apex/Salesforce metadata, or Users can add nCino rules to the CodeScan Quality Profile. Users can extend existing profiles and activate more rules from Apex and Salesforce Metadata using the "nCino-specific" tag.\
   \
   Alternatively, they can add the rules directly to newly created Quality Profiles by selecting the "nCino-specific" tag from the Rules filter, then apply Bulk Change > Activate in > Choose a quality profile.\
   \
   To learn how to create a custom Quality Profile, [see this article.](https://knowledgebase.autorabit.com/product-guides/codescan/quality-profiles/customizing-quality-profiles)
3. **New nCino Specific Rules**:\
   \
   The following nCino-related rules have been added to the existing Apex/Salesforce Metadata rule sets and are tagged as "nCino-specific."
   * **Avoid Duplicates in Custom Labels**: Maintaining unique labels ensures data accuracy and consistency within the nCino platform. By avoiding the creation of multiple labels with the same value, users can rely on the uniqueness of each label for categorization and analysis purposes.
   * **Collateral Configuration Is Null**: The Collateral Configuration Field on the Collateral Type object should not be null. This will reduce the likelihood of missing or incomplete Collateral information.
   * **Duplicate LookupKeys**: In the nCino Record-Based Configuration, no two records in the configuration should have duplicate LookupKeys. The LookupKey is a critical identifier for these records, and duplicates could lead to data inconsistency and errors in the system.
   * **Fee Template Record Screen Section**: Ensure that every Fee Template record includes a Screen Section data value. This will reduce the likelihood of missing or incomplete Fee information.
   * **Field History Tracking Check**: Field History Tracking is limited according to the features in your Salesforce org. By default, Field History Tracking can be used to track a maximum of 20 fields per object.
   * **Null LookupKeys**: In the nCino Record-Based Configuration, object records without LookupKeys will cause challenges in data management and processing.
   * **Product Feature Record Does Not Exist**: Ensure that for each nCino Product Object, there is a corresponding Product Feature record. Product Object records existing without an associated Product Feature record can lead to potential data inconsistencies.
   * **Product Feature Sharing**: Ensure each nCino Product Object record is associated with unique Product Feature records. Shared Product Feature records may lead to data inconsistencies and operational challenges.
   * **nCino Custom Components with Duplicate Names**: Avoid naming conflicts with existing Managed Package Components to minimize the risk of errors and conflicts within the system, ultimately enhancing system stability and reliability.
   * **nCino Custom Fields with Duplicate Names**: Avoid naming conflicts with existing Managed Package Fields to minimize the risk of errors and conflicts within the system, ultimately enhancing system stability and reliability.
   * **nCino Data Integration User Configuration**: The Data Integration user is authenticated for background jobs such as nightly batched updates of records. Configure this user’s Permission Sets correctly to ensure updates by the Data Integration User don't execute additional tasks.
   * **nCino Deprecated Fields**: Deprecated fields in an nCino environment are labeled with a '-D' to make the deprecation visible when configuring the environment. This rule is to identify the location when deprecated fields are used and should be addressed.
   * **nCino Trigger Handler Framework**: The Trigger Handler Framework removes logic from Triggers and enforces consistency across the platform. There are many ways to create a Trigger Framework/Factory; however, the nCino Managed Package can save users time and effort. By levering the nCino Trigger Framework, users can control the execution of triggers at runtime to simplify existing customizations and logic.
   * **System Bypass Logic – Flows**: System bypass logic is required for custom Flows. Checking for the Exclude Flows Permission Set allows the system to cease further processing of the Flow if it is found at the outset. This improves the efficiency of flow execution and reduces unnecessary processing steps.
   * **System Bypass Logic – Triggers**: System bypass logic is required for custom triggers. Checks for the Exclude Trigger Permission Set allow the system to cease further processing of the Trigger if it is found at the outset. This improves the efficiency of Trigger execution and reduces unnecessary processing steps.
   * **System Bypass Logic - Validation Rules**: System bypass logic is required for Validation Rules. Checks for the Exclude Validation Permission Set allow the system to cease further processing of the rule if it is found at the outset. This improves the efficiency of Validation Rule execution and reduces unnecessary processing steps.

### Enhancements

1. **Enhanced rule “Avoid Untrusted/Unescaped Variables in DML Query" to account for potential SOQL injections when “queryWithBinds” is used.**\
   \
   Historically, CodeScan has offered our “Avoid Untrusted/Unescaped Variables in DML Query” rule to inspect customer’s code and flag where there are SOQL injection possibilities. Recently, one of our customers performed a test and expected this rule to flag an issue in their code, but it did not. We determined that the rule should be enhanced for when “queryWithBinds” is used.\
   \
   Our engineering team utilized specifications within Salesforce documentation (specifically, [Help and Training Community](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_bind_var_soql.htm\&release=242\&type=5)) to consider only the query for executed with queryWithBinds() for vulnerability check and violation, avoiding the other parameters such as: (Map, accessLevel) and Database.queryWithBinds (query, bindVariablesMap, accessLevel).\
   \
   Example:

<figure><img src="../../../../.gitbook/assets/image (1627).png" alt=""><figcaption><p>List Accounts</p></figcaption></figure>

Verified after the rule enhancement was engineered that users are able to see the violation for rule “Avoid Untrusted/Unescaped Variables in DML Query” as expected.

<figure><img src="../../../../.gitbook/assets/image (1628).png" alt=""><figcaption><p>Query Results</p></figcaption></figure>

2. **Enhanced IDE to accept email IDs that have up to 255 characters**\
   \
   We discovered that certain users could not use the IDE as expected. The root cause was that the CodeScan plug-in was not able to fetch their valid licenses from CodeScan because these users have an email id with more than 40 chars. This enhancement now allows the CodeScan IDE plug-in to accept email IDs with up to 255 characters.
3. **Fixed rule “Require CSRF protection on GET requests” to distinguish Visualforce page settings from Aura components**\
   \
   Previously, this rule was flagging violations on .cmp files that are aura:component files. The guidance in the rule suggested to change the Visualforce page setting, but this is not possible on Aura components because they are not Visualforce components. This fix for the rule “Require CSRF protection on GET requests” now enables CodeScan to distinguish Visualforce page settings from Aura components.

### &#x20;New Rule

1. **Remote Site Settings Description**\
   \
   Remote Site Settings should have a description of their functionality to make it easy for others to understand the purpose and functionality of the component, as it may not always be understandable from the name.

### Fixes

1. **Fixed issue with CodeScan plug-ins for VS Code and IntelliJ not working after the 24.0.15 release**\
   \
   Recently, we added a search function to the dropdown on the CSV export page to allow users to search for the name of the project they wish to export.
2. **Fixed issue with rule “Flow DML Should Not Be Called In Loops"**\
   \
   Recently, we observed that the rule “Flow DML Should Not Be Called In Loops" throws a null pointer exception because of access of parent node without a null check. This fix corrects the issue. We verified the fix by testing and confirming that the rule now throws a violation as expected, and, additionally, we are no longer getting the null pointer exception.
3. **Fixed issue with tracking IDE usage in CodeScan UI**\
   \
   Over the last few months, we have made several enhancements that allow admins to track IDE adoption and usage. However, we recently learned that the tokens associated with AutoRABIT ARM users were also being logged in the same report. This fix removes ARM users from the IDE user reports.

&#x20;
