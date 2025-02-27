# CodeScan Release Notes (GovCloud)

**CodeScan Changelog for Release GOV 25.0.2**&#x20;

February 2025&#x20;

This release is a combination of our last 5 minor SaaS cloud releases.  This release is comprised of New Features, Feature Enhancements, Fixes, and Technical Enhancements. &#x20;

### GOV 25.0.2 Release Summary:&#x20;

**CodeScan GOV 25.0.2 is comprised of the following 38 components:**&#x20;

* 5 New Features&#x20;
* 8 Feature Enhancements&#x20;
* 12 Fixes&#x20;
* 13 Technical Enhancements&#x20;

Component details are grouped by their corresponding SaaS releases within this document. &#x20;

### SaaS Release 25.0.2&#x20;

**New Features**:&#x20;

* “Security Hotspots” added in CSV Export (25.0.2) &#x20;

Feature Enhancements:&#x20;

* Enhanced rule “Avoid Classes Without Explicit Sharing" to account for Interfaces (25.0.2)&#x20;

**Fixes:**

* Fixed issue where some users are unable to be converted to SAML users when not assigned to SAML org (25.0.2)&#x20;
* Fixed issue with “Project Search” in CSV Export (within the CodeScan U.I.) (25.0.2)&#x20;

**Technical** **Enhancements:**

* Fixed issue where users are redirected to Whitelabel Error Page if SAML user tries to login into the CodeScan application (25.0.2) &#x20;

### SaaS Release 25.0.1&#x20;

**New Features:**&#x20;

* New Rule: Required Description for Remote Site Settings (25.0.1)&#x20;

**Feature Enhancements:**&#x20;

* Enhanced rule “Avoid Untrusted/Unescaped Variables in DML Query" to account for potential SOQL injections when “queryWithBinds” is used. (25.0.1)&#x20;
* Enhanced rule “Field Level Security Vulnerabilities”:  Violation message now displays the correct object instead of '{0}'. (25.0.1)&#x20;
* &#x20;Enhanced IDE to accept email IDs that have up to 255 characters (25.0.1) &#x20;

**Fixes:**&#x20;

* Fixed issue with CodeScan plug-ins for VS Code and IntelliJ not working after 24.0.15 release (25.0.1)&#x20;
* Fixed issue with rule “Flow DML Should Not Be Called In Loops" which was throwing null pointer exceptions because of access of parent node without null check. (25.0.1)&#x20;
* Fixed issue with tracking IDE usage in CodeScan U.I. (25.0.1)&#x20;
* Fixed rule “Require CSRF protection on GET requests” to distinguish Visual Force Page settings from Aura components (25.0.1) &#x20;

**Technical Enhancements:**

* Implemented fix for discrepancy between the projects and the consumed LOC (25.0.1)&#x20;
* Added nCino module (25.0.1)&#x20;
* nCino Rules Activation: (25.0.1)&#x20;
* &#x20;New nCino Specific Rules: (25.0.1)&#x20;
* nCino - Rules naming convention update (25.0.1)&#x20;
* Removed 2 Rules from nCino Plugin (25.0.1)&#x20;
* Implemented variable changes allowing PENDO and GA scripts configurable to load (25.0.1)&#x20;
* Implemented fix where analyses are failing due to pre-existing custom rules not being properly removed from Quality Profiles (25.0.1)&#x20;

### SaaS Release 24.0.14&#x20;

**New Features:** &#x20;

* New Rule for APEX: “OuterClassExplicitSharing” to ensure inner methods are ignored (24.0.14)&#x20;
* &#x20;New Rule for LWC: “API Version is Too Old” (24.0.14)&#x20;

**Feature Enhancements:**&#x20;

* Updated the message for Security Hotspot Status “Exception” to display ”The issue has an approved exception and will be re-reviewed until mitigated or upon exception expiry.” (24.0.14)&#x20;
* “Project Search” added in CSV Export (24.0.14)&#x20;

**Fixes:**&#x20;

* Fixed issue with Retention Period settings where users are able to set “Delete inactive branches and PRs after {value}” (24.0.14)&#x20;
* Fixed issue in rule for APEX “sf: \{{FieldLevelSecurity\}} by accounting for SOSL queries as well (in the previous section, we noted an enhancement on SOQL queries) (24.0.14) &#x20;
* Fixed issue in CodeScan application where flagged violations are not being displayed when using the "issues in new code" filter (24.0.14)&#x20;

**Technical Enhancements:**

* Block SSO configuration if saml\_email parameter is absent (24.0.14)&#x20;
* Cloud Billing Plugin improvements (24.0.14)&#x20;
* Sync Platform Integration Users to Codescan DB (24.0.14)&#x20;
* Billing Plugin UI Changes (24.0.14)&#x20;

### SaaS Release 24.0.13&#x20;

**Feature Enhancements:**&#x20;

* Enhancement to Rule for VF: “"vf:AvoidJavaScriptScriptlets”  by implementing Regex to detect the use of Lightning components within a \{{\<script>\}} tag in Visualforce pages (24.0.13)&#x20;

**Fixes:**&#x20;

* Fixed issue with reference branch analyses to ensure the quality gate consistently fails whenever unresolved new issues exist in the code, preventing deployment until all issues are addressed. (24.0.13)&#x20;
* Fixed issue in rule “sf:OptimizeParallelUnitTests” where the rule detection logic has expanded from looking at annotation being defined/set individually but NOW also in combination with other annotations. (24.0.13)&#x20;
* &#x20;Fixed issue in rule for VF “vf:AvoidExternalResources” to ensure that the check is limited to the “value” attribute only, to avoid false positives and ensure the rule functions as intended.(24.0.13)&#x20;

### SaaS Release 24.0.12&#x20;

**New Features:**&#x20;

* Listed ECMA methods and their properties should be updated dynamically for any new updates (24.012)&#x20;

**Feature Enhancements:**&#x20;

* &#x20;Enhanced the rule sf: \{{FieldLevelSecurity\}} to eliminate false positives that are being flagged when a SOQL query has a inner query calling the related Object. by checking if using isAccessible() before accessing its data (24.0.12)&#x20;
