# Release Notes 25.1.0

## ARM Release Notes 24.4.5

**Release Date: 23 February 2025**

The ARM Release 25.1.0 introduces key upgrades, new features, and critical fixes to enhance security, compatibility, and overall performance. This release includes updates to third-party libraries, improved error handling, and several bug fixes to ensure a seamless user experience.

#### Upgrades and Enhancements

* **Third-Party Library Updates:** OpenJDK, Tomcat, Salesforce CLI, Sonar Scanner, and Local DynamoDB have been updated to their latest versions for improved performance, security, and compatibility.
* **Linux Upgrade:** The underlying Linux environment has been upgraded, strengthening security and optimizing system performance.
* **Salesforce API Version 63.0 Support:** ARM now fully supports Salesforce API version 63.0, ensuring compatibility with the latest Salesforce features and functionalities.

#### Deprecated Features

* **TAF Removal:** The TAF feature was previously hidden behind a feature flag with no reported issues. It has now been fully removed from the codebase.
* **Picklist to ValueSet Migration:** The Picklist feature in the VC Repo section is now deprecated, as Salesforce has discontinued support for it starting from API version 39.

#### Bug Fixes and Improvements

* **Clearer Error Messages:** Improved UI messages provide more precise and actionable feedback, making troubleshooting easier.
* **Tag Deployment Fix:** Previously, deploying a tag would always result in the same changes, even when those changes were not present in the specified tag or branch. Tags now deploy the correct updates as expected.
* **Flow Access & LoginFlows Retrieval:** Users can now retrieve and compare Flow Access and LoginFlows seamlessly. Previously, LoginFlows were not visible during change comparisons.
* **EZ-Merge Report Accuracy:** The EZ-Merge report CSV now includes missing details, such as dates and L1/L2 review statuses, improving tracking and transparency.
* **CI Job Stability:** Resolved issues causing CI job failures and deployment errors for AccelQ tests. Test results now display the correct status and test counts in the Test Summary Report.
* **Deployment Rules Visibility:** Deployment rules are now consistently displayed in the Deployment Submit popup window across all deployment types.
* **Lightning Email Templates Retrieval:** Fixed an issue where Lightning Email Templates were not retrievable across multiple ARM modules, including EZ-Commit, EZ-Merge, Release Label Artifact Preparation, Org-to-Org Deployment, Org Sync, Auto-draft, Commit Template, and Branching Baseline.
* **Review Artifact Enhancement:** The "Review Artifact" option now correctly displays the package.xml and its corresponding data for commits, deployments, and merges. Additionally, SearchCustomization now functions as expected for both SFDX and non-DX environments, supporting merging, CI jobs, and deployments.
* **SFDX Package Naming Support:** Special characters such as @ and . can now be used in SFDX package version names, resolving previous naming limitations.

This release improves system stability, usability, and performance, ensuring a more efficient and seamless experience for all users.
