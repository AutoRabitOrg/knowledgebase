# CodeScan GOV Edition

## CodeScan Changelog for Release GOV 25.1.6 – August 2025&#x20;

This release is a combination of our last 2 SaaS cloud releases:&#x20;

* 25.1.5 (minor release)&#x20;
* 25.1.6 (minor release)&#x20;

This release is comprised of New Features, Feature Enhancements, Fixes, and Technical Enhancements. &#x20;

### GOV 25.1.6 Release Summary&#x20;

CodeScan GOV 25.1.6 is comprised of the following 29 components:&#x20;

* 5 New Features&#x20;
* 5 Feature Enhancements&#x20;
* 6 Fixes&#x20;
* 13 Technical Enhancements&#x20;

Component details are grouped by their corresponding SaaS releases within this document.&#x20;

### SaaS 25.1.5 Release Summary&#x20;

CodeScan Release 25.1.5 is comprised of the following 17 components:&#x20;

* 4 New Features&#x20;
* 2 Feature Enhancements&#x20;
* 4 Fixes&#x20;
* 7 Technical Enhancements&#x20;

#### New Features

* CVSS Implementation for Security Vulnerabilities&#x20;
* When encountering an Incorrect Custom XPath rule, CodeScan Analysis continues (instead of skipping the file analysis)&#x20;
* Ability to define User Type While Inviting or Adding Member&#x20;
* Support Intelligent Prompts for A.I. LLMs&#x20;

&#x20;CodeScan can now generate prompts for LLMs including Agentforce, Copilot, ChatGPT, and Claude AI.  This feature is a component of the CodeScan extension for VS Code.&#x20;

#### Feature Enhancements&#x20;

* Add ESLint rules from @lwc/eslint-plugin-lwc&#x20;
* Enhancement to Apex rule “Unused Formal Parameter” {sf:UnusedFormalParameter}&#x20;

#### Fixes&#x20;

* Fixed issue ARM users recieving an error: “Component can't be null” while running a CodeScan analysis from ARM&#x20;
* Fixed issue where after a user is deactivated, the user is still displayed on Members page&#x20;
* Fixed issue with rule “Avoid running Soql and DML inside loops” {sf:AvoidSoqlInLoops}&#x20;
* Fixed issue regarding restricted access for CodeScan Platform Integration Users&#x20;

#### Technical Enhancements&#x20;

* Added a new field in product database (CodeScan) to store the Salesforce account ID&#x20;
* Created API for Audit Logging Table&#x20;
* Added “CodeScan Organization” parameter to CodeScan Audit Logs&#x20;
* Updated Permissions message / Execute Analysis Message&#x20;
* Fixed Incorrect Inactive Rule Counts on Quality Profiles&#x20;
* Fixed CVSS Rule Description Error in IDE Plugins&#x20;
* Fixed Issue:  Platform User invited as a Member is redirected to the Projects page instead of the My Account page upon login. Additionally, the user has unintended access to links on the My Account (Profile, Projects, and Organizations) page&#x20;

## SaaS Release 25.1.6&#x20;

#### CodeScan Release 25.1.6 is comprised of the following 12 components:&#x20;

* 1 New Feature&#x20;
* 3 Feature Enhancements&#x20;
* 2 Fixes&#x20;
* 6 Technical Enhancements&#x20;

#### New Features&#x20;

* Categories for Project Types&#x20;

Often, customers will have a lot of projects in CodeScan.  Several customers have requested the ability to filter their projects by the type of integration including:&#x20;

GitHub: github \
Bitbucket: bitbucket  \
GitLab: gitlab \
Git: git \
Salesforce: salesforce&#x20;

#### Feature Enhancements&#x20;

* Users getting more verbose error messages (for clarity) when trying to restore quality profiles&#x20;
* Pagination in Projects and Previous Analysis&#x20;
* Email Limit & Validation for Multi-User Invites&#x20;

#### Fixes&#x20;

* Align CSV Export filter status with Latest SQ Issue status&#x20;
* Fixed an unclear error message displayed when invite is sent only to non-corporate email addresses&#x20;

#### Technical Enhancements&#x20;

* Refactor DeleteOrgsJob&#x20;
* Refactor Delete Orgs Email Template&#x20;
* Deleting the custom rule should also deactivate the rule from all the Quality Profiles where rule is Activated.&#x20;
* Addressed identified security issue with Long-String attack buffer overflow&#x20;
* Salesforce API Usage Dashboard and Logs&#x20;
* Fixed world-writable directory ownership in SonarQube Docker image to meet STIG requirements&#x20;

## CodeScan Changelog for Release GOV 25.1.4 – July 2025

This release is a combination of our last 3 SaaS cloud releases:

* 25.1.2 (minor release)
* 25.1.3 (minor release)
* 25.1.4 (minor release)

This release is comprised of New Features, Feature Enhancements, Fixes, and Technical Enhancements.

### GOV 25.1.4 Release Summary

CodeScan GOV 25.1.4 is comprised of the following 47 components:

* 6 New Features
* 9 Feature Enhancements
* 15 Fixes
* 17 Technical Enhancements

Component details are grouped by their corresponding SaaS releases within this document.

### SaaS 25.1.2 Release Summary

CodeScan Release 25.1.2 is comprised of the following 29 components:

* 5 New Features
* 3 Feature Enhancements
* 11 Fixes
* 10 Technical Enhancements

#### New Features

* CWE Numbers Added to Vulnerability Rule “Unescaped Value Could Cause XSS”
* Ability to Disable “Invite Members" option
* Restricting Platform Integration User Access – Forbidden for Admin Users
* New Security Rule:  Server-Side Request Forgery
* New Security Rule: Resource Injection

#### Feature Enhancements

* Enhanced rule “vf:AvoidJavaScriptScriptlets” by adding a new parameter to the rule
* Enhanced rule “Controller Naming Convention” for Apex and Visualforce
* Updated descriptions for Deprecated rules

#### Fixes

* Fixed issue on the Billing Page where two fields were overlapping (nCino and Auditing)
* Fixed issue with the CSV Export not functioning properly with all nCino projects
* Fixed 2 issues with our SOQL Injection rule
* Fixed issue with the rule “Page layout name contains special characters” (sfmeta:PageLayoutNaming)
* Fixed issue with the rule “vf:UnescapedAttributes vulnerability” {where false positive violations were being flagged}
* Fixed issue with the rule “Open Redirect” (sfmeta:PageLayoutNaming) {where false positive violations were being flagged}
* Fixed issue with the rule “Field Level Security Vulnerabilities” (sfmeta:PageLayoutNaming) for classes using “Without Sharing” {where false positive violations were being flagged}
* Fixed issue with CodeScan’s APEX parser
* Fixed issue with rule “Avoid running Soql and DML inside loops” {sf:AvoidSoqlInLoops}
* Fixed issue with rule “RequireDescriptionComponent”
* Fixed issue with rule “sf: FieldLevelSecurityRule”
* Fixed issue with Organization images displaying as large icons in the org list

#### Technical Enhancements

* Addressed identified security issue with Improper Input Validation
* Addressed identified security issue with Improper Error Handling
* Implemented a Billing Notification Update via a Standard Message
* Introduced a flag to mark default profiles {for copying over in new org (rules\_profiles)}
* Stopped unnecessary calls to monitor API after closing the modal of project analysis logs
* Added email masking in Report Jobs
* Fixed Authorization issue with IDP mapping while updating SAML connection
* Disabled Refresh IP list for bitbucket and github cloud versions
* Disabled the ability to see the Password related fields under “My Account” when they are a SAML / SSO user
* Fixed Missing Column Error in New Database Setup

## SaaS Release 25.1.3

CodeScan Release 25.1.3 is comprised of the following 8 components:

* 3 Feature Enhancements
* 2 Fixes
* 3 Technical Enhancements

#### Feature Enhancements

* Project Report Status update in UI
* New Banner in billing when license entitlements exceeded
* New logic in billing allows users continued operations

#### Fixes

* Fixed issue with certain menus where users were unable to easily scroll down and choose a value from the menu
* Fixed Deprecation Warning associated with sonar.login

#### Technical Enhancements

* IDE Usage not being captured for {specific} Dedicated cloud customer
* Billing issue regarding standard and platform users
* Restrict SaaS users to map only to saml org via idp group mapping

&#x20;&#x20;

## SaaS Release 25.1.4

CodeScan Release 25.1.4 is comprised of the following 10 components:

* 1 New Feature
* 3 Feature Enhancements
* 2 Fixes
* 4 Technical Enhancements

#### &#x20;New Feature

* Support for Enterprise Git Connections / Configuring & Managing ALM Integrations

#### &#x20;Feature Enhancements

* Enhancement to CodeScan decorations of SARIF Reports
* Enhancement to CodeScan Rule “URL Redirection to Untrusted Site” {sf:OpenRedirect}
* On the Billing Page, a banner was added that details the level of access users have within the CodeScan UI based on user license type

#### &#x20;Fixes

* Fixed issue where after a user is deactivated, the user is still displayed on Members page
* Fixed issue with codescan-scanner-action (occurring after CodeScan upgrade)

#### &#x20;Technical Enhancements

* On the Billing Page, a banner was added that details the level of access users have within the CodeScan UI based on user license type
* Remediated 403 forbidden error (with error message as Insufficient Privileges) when user tries to create and execute project analyses
* Added “inviteUsersEnabled” Column to SonarQube migration Schema
* Fixed issue where Gitlab API call failure breaks our CleanUp job

***

## CodeScan Changelog for Release GOV 25.1.1.2&#x20;

**June 2025**&#x20;

This release is comprised of 1 Feature Enhancement&#x20;

### **GOV 25.1.1.2 Release Summary**

CodeScan GOV 25.1.1.2 is comprised of the following 1 component &#x20;

* 1 Feature Enhancement

_Component details are grouped by their corresponding SaaS releases within this document._&#x20;

#### **Feature Enhancements** &#x20;

* Enhanced generateSarifFile and generateReportFile so that when \{{generateSarifFile: false\}} or \{{generateReportFile: true\}}, the SARIF file contains only&#x20;
*  open issues respective to the branch and PR&#x20;
* Includes full metadata for each issue, including Type and Severity for rules and results&#x20;

***

## CodeScan Changelog for Release GOV 25.1.1.1&#x20;

**June 2025**&#x20;

This release is comprised of 1 Feature Enhancement &#x20;

### **GOV 25.1.1.2 Release Summary** &#x20;

CodeScan GOV 25.1.1.1 is comprised of the following 1 component &#x20;

* 1 Feature Enhancement&#x20;

_Component details are grouped by their corresponding SaaS releases within this document._&#x20;

**Feature Enhancements** &#x20;

* Enhanced generateSarifFile (parameter = false) to include issue severities&#x20;



***

## CodeScan Changelog for Release GOV 25.1.1&#x20;

&#x20;**May 2025**

This release is a combination of our last 3 SaaS cloud releases:&#x20;

* 25.0.3 (minor release)&#x20;
* 25.1.0 (major release)&#x20;
* 25.1.1 (minor release)&#x20;

This release is comprised of New Features, Feature Enhancements, Fixes, and Technical Enhancements. &#x20;

### GOV 25.1.1 Release Summary&#x20;

CodeScan GOV 25.1.1 is comprised of the following 35 components:&#x20;

* 1 New Feature&#x20;
* 1 Feature Enhancement&#x20;
* 7 Fixes&#x20;
* 26 Technical Enhancements&#x20;

Component details are grouped by their corresponding SaaS releases within this document.&#x20;

### SaaS 25.0.3 Release Summary&#x20;

CodeScan Release 25.0.3 is comprised of the following 5 components:&#x20;

* 1 New Feature&#x20;
* 1 Feature Enhancement&#x20;
* 1 Fix&#x20;
* 2 Technical Enhancements&#x20;

#### New Features&#x20;

* Within the “Members” page, CodeScan users can now be assigned as Standard Users (default) or as Platform Integration Users&#x20;

#### Feature Enhancements&#x20;

* Updated the “Run As” rule per the specifications of the US Department of Veteran Affairs to include a new parameter checking for only the presence of System.runAs in the test methods&#x20;

#### Fixes&#x20;

* Fixed issue on the Billing Page where two fields were overlapping (nCino and Auditing)&#x20;

#### Technical Enhancements&#x20;

* Hardened a security component to sanitize User Inputs, as well as validate and encode any user-controlled input displayed on the page to prevent text injection&#x20;
* Hardened a security component to use Authorization Headers instead of passing JWTs in URLs&#x20;

## SaaS Release 25.1.0&#x20;

CodeScan Release 25.1.0 is comprised of the following 26 components:&#x20;

* 2 Fixes&#x20;
* 24 Technical Enhancements&#x20;

#### Fixes&#x20;

* Fixed issue where some users were unable to Select Project for CSV Export in CodeScan&#x20;
* Fixed reported false positives with rule “sf:AvoidGlobalModifier” &#x20;

#### Technical Enhancements&#x20;

* Upgraded the OS Libraries inside CodeScan Docker Images&#x20;
* Upgraded the CodeScan and SonarQube Plugins to Latest Secure Versions&#x20;
* Upgraded all Spring-related dependencies to versions compatible with Spring Boot 3.3.3&#x20;
* Upgraded Non-Spring Java Libraries to Latest Versions&#x20;
* Upgraded CodeScanNG to Node v20&#x20;
* Upgraded TD Agent from V4 to V5  &#x20;
* Upgraded infrastructure to SonarQube 24.12
* To improve visibility and user understanding, replaced pop-ups with a banner for the following scenarios:&#x20;
* License Exceeded&#x20;
* Pricing Mode Loc&#x20;
* Pricing Mode User&#x20;
* IDE License Usage&#x20;
* Subscription Expired/Cancelled&#x20;
* TrialPeriod Expired&#x20;
* Bitbucket Project Without Secret&#x20;
* Removed “Modify Plan” Button from Billing Page&#x20;
* Removed Bitbucket Banner that was put in place for Q4 2024 and Q1 2025 notifications&#x20;
* Enhanced logging by “Skip Masking” the first 2 chars in User Email in CodeScanNG and SonarQube&#x20;
* Removed invocation of oauth callback url while SAML Authentication&#x20;
* Fixed Authorization Checks Around V2 SonarQube APIs&#x20;
* Fixed Compliance Issue in Dockerfile Control ID: 19511&#x20;
* Fixed and issue with Unauthorized Access to Quality Profiles & Org APIs & Quality gates and Navigation APIs&#x20;
* Configured the application to return generic error messages instead of full stack traces in error messages&#x20;
* Fixed Security Vulnerability in CodeScan Images CVE-2024-56171&#x20;
* Fixed Security Vulnerability in CodeScan Images CVE-2025-24928&#x20;
* Fixed Security Vulnerability in CodeScan Images for logback - CVE-2024-12798&#x20;
* Fixed Security Vulnerability in CodeScan Images for logback - CVE-2024-12801&#x20;
* Fixed Security Vulnerability in CodeScan Images for net.minidev:json-smart - CVE-2024-57699&#x20;
* Added Authorization/Authentication to publicly open APIs&#x20;
* Fixed an issue with the CodeScan response to only return the organization specific custom rules as per loggedIn User&#x20;
* Checked Membership for show rules API ( /api/rules/show )&#x20;

## SaaS Release 25.1.1&#x20;

CodeScan Release 25.1.1 is comprised of the following 4 components:&#x20;

* 4 Fixes&#x20;

#### Fixes

* Fixed Error: \[CS] API GET status code: 404 when users try to generate Sarif File on their environment.
* Fixed issue with the IDP group mapping where the feature flag was not working as expected.&#x20;
* Fixed issue in IDP group Mapping where a user is member of org 1 and owner of org 2, but from the org2 SAML connection was able promote users to owners of org1.&#x20;
* Fixed issue when users were attaching rule tags to rule in one org which was resulting in blocking analyses of another org.

## **CodeScan Changelog for Release GOV 25.0.3**

**March 2025**&#x20;

CodeScan GOV 25.0.3 is comprised of the following 1 component:&#x20;

* 1 Technical Enhancement&#x20;

Component details are grouped by their corresponding SaaS releases within this document. &#x20;

**Technical Enhancements**&#x20;

* Fixed issue for parsing email addresses when the SAML assertion is encrypted &#x20;

_Verified the below scenarios for SAML login when the Encryption is enabled and disabled on the Gov test instance_ &#x20;

Note that all are working as expected and didn’t find any issues.&#x20;

1. Verified the User login through SAML if the encryption is enabled on the instance - Able to login successfully.&#x20;
2. Verified the User login through SAML if the encryption is disabled on the instance - Able to login successfully.&#x20;
3. Verified the response of the SAML connection which is EncryptedAssertion if the encryption is enabled on the instance.&#x20;
4. Verified the response of the SAML connection which is samlp:Response if the encryption is disabled on the instance.&#x20;
5. Verified that the user could successfully login by providing the values and updating the connection for the SAML attributes, such as the user’s email, login, name, and group.&#x20;
6. Verified the scenario if the user is not a member of the organization where SAML connection is created and tries to login - Not able to login into the instance which is expected.&#x20;
7. Verified the IDP group mapping cases all are working as expected.&#x20;

***

## **CodeScan Changelog for Release GOV 25.0.2**&#x20;

**February 2025**&#x20;

This release is a combination of our last 5 minor SaaS cloud releases.  This release is comprised of New Features, Feature Enhancements, Fixes, and Technical Enhancements. &#x20;

### GOV 25.0.2 Release Summary&#x20;

**CodeScan GOV 25.0.2 is comprised of the following 38 components:**&#x20;

* 5 New Features&#x20;
* 8 Feature Enhancements&#x20;
* 12 Fixes&#x20;
* 13 Technical Enhancements&#x20;

Component details are grouped by their corresponding SaaS releases within this document. &#x20;

### SaaS Release 25.0.2&#x20;

**New Features**&#x20;

* “Security Hotspots” added in CSV Export (25.0.2) &#x20;

Feature Enhancements:&#x20;

* Enhanced rule “Avoid Classes Without Explicit Sharing" to account for Interfaces (25.0.2)&#x20;

**Fixes**

* Fixed issue where some users are unable to be converted to SAML users when not assigned to SAML org (25.0.2)&#x20;
* Fixed issue with “Project Search” in CSV Export (within the CodeScan U.I.) (25.0.2)&#x20;

**Technical** **Enhancements**

* Fixed issue where users are redirected to Whitelabel Error Page if SAML user tries to login into the CodeScan application (25.0.2) &#x20;

***

## SaaS Release 25.0.1&#x20;

**New Features**&#x20;

* New Rule: Required Description for Remote Site Settings (25.0.1)&#x20;

**Feature Enhancements**&#x20;

* Enhanced rule “Avoid Untrusted/Unescaped Variables in DML Query" to account for potential SOQL injections when “queryWithBinds” is used. (25.0.1)&#x20;
* Enhanced rule “Field Level Security Vulnerabilities”:  Violation message now displays the correct object instead of '{0}'. (25.0.1)&#x20;
* &#x20;Enhanced IDE to accept email IDs that have up to 255 characters (25.0.1) &#x20;

**Fixes**

* Fixed issue with CodeScan plug-ins for VS Code and IntelliJ not working after 24.0.15 release (25.0.1)&#x20;
* Fixed issue with rule “Flow DML Should Not Be Called In Loops" which was throwing null pointer exceptions because of access of parent node without null check. (25.0.1)&#x20;
* Fixed issue with tracking IDE usage in CodeScan U.I. (25.0.1)&#x20;
* Fixed rule “Require CSRF protection on GET requests” to distinguish Visual Force Page settings from Aura components (25.0.1) &#x20;

**Technical Enhancements**

* Implemented fix for discrepancy between the projects and the consumed LOC (25.0.1)&#x20;
* Added nCino module (25.0.1)&#x20;
* nCino Rules Activation: (25.0.1)&#x20;
* &#x20;New nCino Specific Rules: (25.0.1)&#x20;
* nCino - Rules naming convention update (25.0.1)&#x20;
* Removed 2 Rules from nCino Plugin (25.0.1)&#x20;
* Implemented variable changes allowing PENDO and GA scripts configurable to load (25.0.1)&#x20;
* Implemented fix where analyses are failing due to pre-existing custom rules not being properly removed from Quality Profiles (25.0.1)&#x20;

***

## SaaS Release 24.0.14&#x20;

**New Features** &#x20;

* New Rule for APEX: “OuterClassExplicitSharing” to ensure inner methods are ignored (24.0.14)&#x20;
* &#x20;New Rule for LWC: “API Version is Too Old” (24.0.14)&#x20;

**Feature Enhancements**&#x20;

* Updated the message for Security Hotspot Status “Exception” to display ”The issue has an approved exception and will be re-reviewed until mitigated or upon exception expiry.” (24.0.14)&#x20;
* “Project Search” added in CSV Export (24.0.14)&#x20;

**Fixes**

* Fixed issue with Retention Period settings where users are able to set “Delete inactive branches and PRs after {value}” (24.0.14)&#x20;
* Fixed issue in rule for APEX “sf: \{{FieldLevelSecurity\}} by accounting for SOSL queries as well (in the previous section, we noted an enhancement on SOQL queries) (24.0.14) &#x20;
* Fixed issue in CodeScan application where flagged violations are not being displayed when using the "issues in new code" filter (24.0.14)&#x20;

**Technical Enhancements**

* Block SSO configuration if saml\_email parameter is absent (24.0.14)&#x20;
* Cloud Billing Plugin improvements (24.0.14)&#x20;
* Sync Platform Integration Users to Codescan DB (24.0.14)&#x20;
* Billing Plugin UI Changes (24.0.14)&#x20;

***

## SaaS Release 24.0.13&#x20;

**Feature Enhancements**&#x20;

* Enhancement to Rule for VF: “"vf:AvoidJavaScriptScriptlets”  by implementing Regex to detect the use of Lightning components within a \{{\<script>\}} tag in Visualforce pages (24.0.13)&#x20;

**Fixes**

* Fixed issue with reference branch analyses to ensure the quality gate consistently fails whenever unresolved new issues exist in the code, preventing deployment until all issues are addressed. (24.0.13)&#x20;
* Fixed issue in rule “sf:OptimizeParallelUnitTests” where the rule detection logic has expanded from looking at annotation being defined/set individually but NOW also in combination with other annotations. (24.0.13)&#x20;
* &#x20;Fixed issue in rule for VF “vf:AvoidExternalResources” to ensure that the check is limited to the “value” attribute only, to avoid false positives and ensure the rule functions as intended.(24.0.13)&#x20;

***

## SaaS Release 24.0.12&#x20;

**New Features**

* Listed ECMA methods and their properties should be updated dynamically for any new updates (24.012)&#x20;

**Feature Enhancements**

* &#x20;Enhanced the rule sf: \{{FieldLevelSecurity\}} to eliminate false positives that are being flagged when a SOQL query has a inner query calling the related Object. by checking if using isAccessible() before accessing its data (24.0.12)&#x20;
