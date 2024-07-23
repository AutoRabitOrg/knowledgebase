# Release Notes 24.1

## ARM Release Notes 24.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**June 2024**

**Version 24.1 – Enhancements and Improvements**

### Enhancements

1. **Perform Validation Deployment for Multiple Orgs**\
   In this release, we're thrilled to introduce an enhanced **Validate Deployment** feature, responding to a key user request. Users can now choose multiple orgs simultaneously, enabling a forward-looking validation process as they promote from one sandbox to the next and eventually to production. This time-saving enhancement allows users to select up to three organizations from a convenient multi-picklist, and the subsequent summary screen provides a consolidated view of the deployment results for each selected organization. The implementation ensures a seamless experience by allowing users to toggle between different org validations. The introduction of this feature in the EZ-Merge and EZ-Commit options streamlines deployment validations, contributing to a more efficient and informed deployment workflow.\

2. **Incorporated Checkbox to Skip Prevalidation Criteria**\
   In this release, we're excited to introduce the ability for developers to **skip all prevalidation criteria** specifically for **back merges from designated branches**. This enhancement offers a streamlined approach to the back merge process, empowering developers to improve efficiency and simplify code migration upstream. To leverage this feature, developers can configure the branch type in VC Repos → Branch settings, where a new checkbox option allows you to enable skipping prevalidation criteria for a particular branch during back merges. This capability enhances flexibility and productivity, reducing unnecessary steps in the code migration workflow. With the skip option, developers have greater control over the back merge process, ensuring a smoother and more agile development experience.\

3. **Revamped Static Code Analysis View**\
   We’ve revamped our static code analysis UI to enhance the user experience. Now, errors are conveniently displayed under selected files, streamlining issue identification and resolution across various tools.\

4. **Streamlined EZ-Commit Editing**\
   This release significantly enhanced the EZ-Commit workflow to empower developers. The introduction of an integrated **Compare Changes** option in the **Review Artifact** screen allows for seamless viewing, editing, and visualizing of Salesforce metadata changes in a single, user-friendly interface. Developers can now effortlessly navigate and understand their code edits with color-coded differences, eliminating the need to toggle between multiple screens. This streamlined process enhances the user experience and addresses a crucial blocker in the journey towards CI/CD, providing a more efficient and intuitive path for developers.\

5. **Enhanced SCA Label Scheduling**\
   In this release, users can now enjoy enhanced control over SCA label scheduling with the introduction of the ability to edit/update schedules. This feature provides greater flexibility, allowing users to modify scheduled times for SCA labels, contributing to a more seamless and user-friendly experience in managing job schedules.\

6. **New Email Templates Implementation**\
   In this release, a significant enhancement has been made by implementing new email templates that align with current visualization standards. This update reflects our commitment to maintaining high standards in user interface design and enhancing overall user engagement.

### Improvements

This update improves the tool's efficiency and responsiveness and leverages new technologies, collectively resulting in a smoother, faster user experience.

1. In this release, we revolutionized the system by converting all JSP pages into a RESTful API, enhancing modularity, scalability, and interoperability.
2. SF CLI Version upgrade to 2.41.8
3. SOAP to REST services upgrade: Upgrading from SOAP to REST services improves performance by reducing overhead with lightweight JSON payloads and enhances security through stateless communication and simplified implementation of HTTPS.
4. By merging SalesforceDxHub into SalesforceOrg, it effectively reduces redundancy in data storage. Users can now register once from SalesforceOrg, with the added capability to specify a registered org as a Dev hub. When a production org is registered as a Dev hub, it appears on both screens, streamlining data management and enhancing user workflow. This release optimizes data storage, improves user experience, and simplifies registration processes, ultimately enhancing overall system efficiency.
5. Upgrade of third-party libraries
6. Salesforce integration credentials (Client ID & Secret) are now encrypted for improved security. Existing tokens are also migrated to the new format. This enhances protection against unauthorized access.
7. Log-leveling: Dynamically modify log levels for specific logger categories to enhance monitoring and troubleshooting.

### Changelogs

The following weekly fixes were implemented.

#### 24 July 2024

**ARM 24.1.6**

1. A code fix was applied to the CI Jobs module of version 24.1 due to a typo in the ARM CI Jobs creation screen. Support ticket #116616
2. A code fix was applied to the Deployments module of version 24.1 due to a use-case error in which the 'add member' option was not working. Support tickets #116545, #117480
3. A code fix was applied to the Admin module of version 24.1 to correct a use-case error in which test class mappings were missing. Support tickets #116984, #117737&#x20;
4. A code fix was applied to the Admin module of version 24.1 to correct a use-case issue with log visibility in the branching baseline for admin users. Support ticket #117485&#x20;
5. A code fix was applied to the Admin module of version 24.1 from an internal ticket identifying a use case in which the user was getting an 'unauthorized 401' error during a new account signup registration.&#x20;

#### 17 July 2024

**ARM 24.1.5**

1. A code fix was applied to version 24.1 as a result of a data error encountered in the CI Jobs module related to CI Jobs not triggering. Support ticket #116677
2. A code fix was applied to the Version Control module in version 24.1 related to a data error causing the WebLink deletion feature to not work. Support ticket #115994
3. A code fix was applied to the CI Jobs module in version 24.1 due to a data error identified internally with the CI Edit edit mode where the "Do you want us to update the test classes" feature is not saving.
4. A code fix was applied to the nCino module in version 24.1 related to a use-case error in which Data Loader Pro was not fetching the child object. Support ticket #116928

#### 10 July 2024

**ARM 24.1.4**

1. A use-case error identified in version 23.1 required a code fix applied in versions 23.1 and 24.1 to the Deployment and Version Control modules, to correct a scenario in an org-to-org full-profile deployment in which package visibility and permissions were not captured. Support ticket #110760
2. A code fix was applied to versions 23.1 and 24.1 due to a use-case error identified in version 23.1 in which commits were failing with a 'no credentials mapped' error in the Version Control module. Support ticket #116704&#x20;
3. A code fix identified in version 24.1 was applied to the Admin module in version 24.1 due to a use-case error identified by internal ticket in which the on-premises server was not starting up after migrating from 23.1 to 24.1 build.&#x20;
4. A use-case error in the Version Control module identified in version 24.1 by internal ticket required a code fix to version 24.1 to correct an instance in which the user was unable to create a release label.

#### 3 & 7 July 2024

**ARM 24.1.3**

1. A use-case error identified in version 24.1 required a code fix to the CI Jobs module, applied in versions 23.1 and 24.1, to correct instances where configuration changes were not being saved to the CI job. Support ticket #116047&#x20;
2. A code fix identified in version 24.1 by an internal ticket was implemented in version 24.1 to correct a use-case error in which the Version Control module’s Validate and Merge button was not being reflected immediately after changing the EZ-Merge validation criteria in MyAccounts.
3. A code fix identified in version 24.1 by an internal ticket was applied to version 24.1 due to the minimization feature not working in the Version Control module.
4. A code fix identified by an internal ticket in version 24.1 was applied to the Version Control module in version 24.1 due a use-case error where ‘Path View’ section highlighting is occurring when toggling from the ‘File Changes’ screen to the ‘Path’ view, then back to the ‘File Changes Path’ view.
5. A code fix identified in version 24.1 by an internal ticket was initiated to the EBR Change module in version 24.1, prompted by a change to the EBR plugin info.
6. A use-case error identified in version 24.1 by an internal ticket required a code fix to the Version Control module in version 24.1 due to the commit history screen getting stuck loading when the repo name has a special character in it (e.g., plus sign \[+]).
7. A use-case scenario identified in version 24.1 by an internal ticket required a code fix to the CI Jobs module in version 24.1 for the time-frame window to be added for the ARM admin API to fetch data.
8. A use-case error identified in version 24.1 by an internal ticket required a code fix applied to the nCino module in version 24.1 to correct where the option "automap user/owner data" is disabled by default for CI jobs created in 23.1.x versions.
9. A use-case scenario identified in version 24.1 required a code fix to the Version Control module in version 24.1 due to release labels not showing. Support ticket #116413
10. A use-case error identified in version 24.1 required a code fix to the Version Control module in version 24.1 due to an issue with choosing the Level 1 approver when performing a merge. Support ticket #116417, #116692
11. A use-case error was identified in version 24.1 that required a code fix to the nCino module due to the RBC filters not working on commits. Support ticket #116291
12. A use-case scenario identified in version 24.1 via an internal ticket required a code fix to the nCino module to correct an error in which the Data Loader clone process is not identifying the new CSV file.&#x20;
13. A use-case error identified in version 24.1 required a code fix to the Version Control module to correct an error in which user is unable to create an EZ-Merge. Support ticket #116700
14. A code fix was applied to the Deployment and Version Control modules to correct a use-case error identified in version 24.1 in which the org comparison is not showing diff results. Support ticket #116039
15. A use-case scenario required a code fix to the version 24.1 Admin module to correct an error that caused the branching baseline to keep running for 24 hours. Support ticket #114734&#x20;
16. A code fix was applied to the Version Control module to correct a use-case error identified in version 24.1 that caused commits to be failing with an 'no credentials mapped' error. Support ticket #116704
17. A use-case error identified in version 23.1 required a code fix to the Deployment module, applied in versions 23.1 and 24.1, to correct the metadata retrieval in the repository from failing. Support ticket #115818&#x20;
18. A code fix identified in version 23.1 by an internal request ticket was applied to the Admin and CI jobs modules in versions 23.1 and 24.1 to upgrade v61 (Beta) to v61.

#### 26 June 2024

**ARM 24.1.2**

1. A data error reported in version 23.1 with the Version Control module that resulted in version control being deleted was resolved in both 23.1 and 24.1 through adding loggers. Support ticket #114503
2. A use-case error reported in version 23.1 with the Version Control module in which the user was unable to use an existing conflicted file, which resulted in reraising merge requests, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115084
3. &#x20;A use-case error reported in version 23.1, which resulted in an issue with the Data Loader module in which the software was not inserting the correct record type, was resolved in both 23.1 and 24.1 through a code fix. Support ticket #114076
4. A use-case error reported in version 23.1 with the nCino module in which rollbacks were only partially being completed was resolved in both 23.1 and 24.1 through a code fix. Support ticket #115204
5. A use-case error in version 24.1 with the Version Control module in which commits were remaining in progress was resolved through a code fix. Support ticket #115691
6. A use-case error in version 24.1 with the Version Control module with commit CI Job deployment errors was resolved in 24.1 through a code fix. Support ticket #115817
7. A use-case error reported in version 24.1 required an update to the Admin module to properly reflect X rather than Twitter along with revised copyright information, which was resolved through a code fix. Support ticket #115756

#### 23 June 2024

ARM 24.1.1

1. A code fix was applied to the Version Control module for a use-case error related to an EZ-Commit re-login issue identified. Support ticket #115664
2. A code fix was applied to the Version Control and Admin modules for a use-case error related to an issue in which Azure ADO connection and password were returning errors. Support tickets #115489, 115558
3. A code fix was applied to the Version Control module for a use-case error related to a validation org being requested when attempting to merge changes. Support ticket #115787
4. A code fix was applied to the Version Control module for a use-case error related to the create artifact button not being visible when attempting to create a release label.
5. A code fix was applied to the Reports module for a use-case error related to an alignment issue in the weekly reports filter for no deployments.&#x20;
6. A code fix was applied to the Admin module for a use-case error in which the user is unable to create a search and substitute rule.&#x20;
7. A code fix was applied to the Admin module for a use-case error related to being unable to register a branch.&#x20;



### nCino Improvements

See the recent updates to [nCino release 24.1](../ncino-release-notes/release-notes-24.1.md) notes as well.&#x20;
