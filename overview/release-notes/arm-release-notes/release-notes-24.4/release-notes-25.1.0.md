# Release Notes 25.1.0

## ARM Release Notes 25.1.0

**Release Date: 23 February 2025**

The ARM Release 25.1.0 introduces key upgrades, new features, and critical fixes to enhance security, compatibility, and overall performance. This release includes updates to third-party libraries, improved error handling, and several bug fixes to ensure a seamless user experience.

#### Upgrades and Enhancements

* **Third-Party Library Updates:** OpenJDK, Tomcat, Salesforce CLI, Sonar Scanner, and Local DynamoDB have been updated to their latest versions for improved performance, security, and compatibility.
* **Salesforce API Version 63.0 Support:** ARM now fully supports Salesforce API version 63.0, ensuring compatibility with the latest Salesforce features and functionalities.

#### Deprecated Features

* **Picklist to ValueSet Migration:** The Picklist feature in the VC Repo section is now deprecated, as Salesforce has discontinued support for it starting from API version 39.

#### Bug Fixes and Improvements

* **Clearer Error Messages:** Improved UI messages provide more precise and actionable feedback, making troubleshooting easier.
* **Tag Deployment Fix:** Previously, deploying a tag would always result in the same changes, even when those changes were not present in the specified tag or branch. Tags now deploy the correct updates as expected. _Impacted Modules: Custom Deployments. Support Case #124672_
* **Flow Access & LoginFlows Retrieval:** Users can now retrieve and compare Flow Access and LoginFlows seamlessly. Previously, LoginFlows were not visible during change comparisons. _Impacted Modules: EZ-Commit with validate deploy, Merge with validate deploy , Profile duplicates. Support Case #126050_
* **EZ-Merge Report Accuracy:** The EZ-Merge report CSV now includes missing details, such as dates and L1/L2 review statuses, improving tracking and transparency. _Impacted Modules: Weekly Report, EZ-Merge report. Support Case #128801_&#x20;
* **CI Job Stability:** Resolved issues causing CI job failures and deployment errors for AccelQ tests. Test results now display the correct status and test counts in the Test Summary Report. &#x49;_&#x6D;pacted Modules: Accelq CI Jobs. Support Case #128701_
* **Deployment Rules Visibility:** Deployment rules are now consistently displayed in the Deployment Submit popup window across all deployment types. _Impacted Modules: Custom Deployments.  Support Case #129905_
* **Lightning Email Templates Retrieval:** Fixed an issue where Lightning Email Templates were not retrievable across multiple ARM modules, including EZ-Commit, EZ-Merge, Release Label Artifact Preparation, Org-to-Org Deployment, Org Sync, Auto-draft, Commit Template, and Branching Baseline. _Impacted Modules: EZ-Commit. Support Case #129643_&#x20;
* **Review Artifact Enhancement:** The "Review Artifact" option now correctly displays the package.xml and its corresponding data for commits, deployments, and merges. Additionally, SearchCustomization now functions as expected for both SFDX and non-DX environments, supporting merging, CI jobs, and deployments. _Impacted Modules: EZ-Commit, Merge. Support Case #130173_
* **SFDX Package Naming Support:** Special characters such as @ and . can now be used in SFDX package version names, resolving previous naming limitations. _Impacted Modules: SFDX, Unlocked Packages. Support Case #130459_

#### Upgrades and Enhancements

* **Third-Party Library Updates:** OpenJDK, Tomcat, Salesforce CLI, Sonar Scanner, and Local DynamoDB have been updated to their latest versions for improved performance, security, and compatibility.
* **Linux Upgrade:** The underlying Linux environment has been upgraded, strengthening security and optimizing system performance.

## nCino Improvements

**Release Date 23 February 2025**

See the [Release Notes](https://knowledgebase.autorabit.com/overview/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.0-release-notes) for nCino + Data Loader improvements.&#x20;
