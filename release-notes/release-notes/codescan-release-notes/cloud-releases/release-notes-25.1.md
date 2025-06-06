---
description: CodeScan Cloud Release Notes
---

# Release Notes 25.1

## Integration Requirements for CodeScan v25.1.0+

Please note that there are updated requirements for customers who are using one or more of the following to integrate with CodeScan:

* SFDX
* SonarScanner
* ADO
* VS Code
* IntelliJ&#x20;

[**Please refer to our integration requirements page for further details.**](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/integration-requirements)

***

## CodeScan Release 25.1.1&#x20;

**Release Date: May 11, 2025**&#x20;

### Summary:&#x20;

**CodeScan 25.1.1 is comprised of the following 3 components:**&#x20;

* 3 Fixes&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

#### **New Features:**&#x20;

There are no New Features associated with this release&#x20;

#### **Enhancements:**&#x20;

There are no Enhancements associated with this release&#x20;

**New Rules:**&#x20;

There are no New Rules associated with this release&#x20;

### **Fixes**:

1. **Fixed an issue with rule tags blocking analyses**&#x20;

Several customers reported that, after the recent CodeScan upgrade to 25.1.0, some of their analyses were not properly executing.  We uncovered that this was due to new logic added to a database table.  This fix corrects this issue and will allow all blocked analyses to run properly.&#x20;

We have verified the below scenarios and report that all are working as expected.&#x20;

* Tags which are system default&#x20;
* Tags which are not system default&#x20;
* Custom tags&#x20;

1. Verified the vf:exception and sf:exception rule by adding tags in one organization and seeing the analysis working without any issue in that org or any other org.&#x20;
2. Verified the analysis for the rule sf:exception by assigning the tags.  Confirmed analysis was successful and that users are able to see the assigned tags in the issues page.&#x20;
3. Verified the analysis when the tags are not assigned. If there are any new violations the user is unable to see any tags for the violations (which is expected). &#x20;

&#x20;

2. **Fixed Error: \[CS] API GET status code: 404 when users try to generate Sarif File on their environment**&#x20;

Several customers reported the following error “Error: \[CS] API GET status code: 404 “when users try to generate Sarif File on their environment.&#x20;

This fix corrects this issue and will allow users to generate Sarif files on their environment.&#x20;

We have verified the below scenarios for GitHub Actions SARIF report on TEST environment and are able to generate SARIF reports successfully.&#x20;

1. Analysis is getting “success” and able to get the SARIF report where the results are same in the report and on CodeScan UI&#x20;
2. Validated the Pull request analysis in GitHub actions we are able see that the PR analysis is happening for the changed files.&#x20;

* Validated the Commit request analysis.&#x20;
* Validated the PR analysis.&#x20;
* Validated Merge analysis.&#x20;



3. **Fixed Error: \[CS] API GET status code: 404 when users try to generate Sarif File on their environment**&#x20;

**After the upgrade to 25.1.0, we uncovered 2 minor issues:**&#x20;

1. The IDP group mapping feature flag was not working as expected.&#x20;
2. If an ID user is member of org 1 and owner of org 2, then from org2 SAML connection she was able to make anyone an owner of org1.&#x20;

This update remediates these 2 issues.&#x20;

Verified the IDP Group Mapping flag by Enabling and Disabling the instance is now working as expected.&#x20;

<figure><img src="../../../../.gitbook/assets/image (1672).png" alt="" width="563"><figcaption></figcaption></figure>

***

## Release Notes 25.1.0&#x20;

**Release Date: 20 April 2025**&#x20;

### Summary:&#x20;

CodeScan 25.1.0 is comprised of three main components / features:&#x20;

* [New User Interface ](release-notes-25.1.md#new-user-interface)
* [Technical Architecture Improvements ](release-notes-25.1.md#technical-architecture-improvements)
* [Fixes](release-notes-25.1.md#fixes-1)

Component details are listed in their corresponding sections within this document.&#x20;

### New User Interface&#x20;

In this release, we have updated the CodeScan User Interface order to provide four key benefits:&#x20;

* Easier navigation, which provides both an improved, intuitive experience for more advanced users, while reducing the learning curve for new users
* Consistency in screen layout, providing a more cohesive experience throughout the application  &#x20;
* Enhanced performance and responsiveness within CodeScan&#x20;
* Brand modernization alignment with other AutoRABIT solutions&#x20;

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption><p>UI Upgrades</p></figcaption></figure>

{% hint style="info" %}
Please note: CodeScan documentation pages will have new images to reflect the latest UI changes over the coming weeks. This should not affect the effectiveness of instruction steps in the meantime.&#x20;
{% endhint %}

### Technical Architecture Improvements&#x20;

* The CodeScan 25.1.0 contains various technical architecture improvements and upgrades to various libraries. We have also included several enhancements to CodeScan’s security architecture.

### **Fixes**:

* Fixed a false positive in the 'sf:AvoidGlobalModifier' rule. The violation is now ignored for global classes used as return types in any global static method.



&#x20;&#x20;

&#x20;

&#x20;
