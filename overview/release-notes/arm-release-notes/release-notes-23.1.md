# Release Notes 23.1

## ARM Release Notes 23.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**September 2023**

**Version 23.1 – New Features, Enhancements, and Improvements**

### New Features

**1. Automatic Merge after Successful CI Build**\
We know that understanding and managing version control can sometimes be a challenge. ARM offers the flexibility to cherry-pick branch revisions for merge or deployment. Now you can automate this process of cherry-picking the revisions in CI Jobs as a post-deployment step.

The '**Run Merge process on successful deployment**' feature keeps track of builds in source branches and merges them into a designated destination branch if they meet the configured criteria (for example, if the build is successful). Rather than requiring manual effort, upstream merges may now be automated by the **Salesforce Release Manager** using revision numbers that were determined as part of a build cycle in CI jobs.

Users will be notified via email of the success or failure of the automated merge process.

**2. Create and Install an Unlocked Package Version from a Version Control Branch**\
Use ARM CI intelligence to create a package version, build using the SFDX project structure in a Version Control branch, and install the same in the destination org of your choice—all from the same page.

You can now generate an unlocked package version automatically through the CI job, and as part of the deployment, it is deployed in the same build cycle. Until the 22.2 version, it picked the latest package version that was already successfully created in ARM.

When users create a CI job using this option, ARM checks the Version Control. If there is a change, it builds a new version on top of the packages. Once the package is created, then the deployment is triggered automatically.

**3. Create Connected Apps**\
ARM now gives access to users to create and maintain their OAuth credentials. Users can set up the **Connected Apps** for Jira OAuth and register the credentials with ARM.

You can add, edit, and delete your Jira login credentials instead of contacting AutoRABIT to manage the connected apps. Once created, simply provide us with the connected app details like **Client ID** and **Secret Keys**.

We use these details to connect as an ALM and test the connection.

**4. RESTricted Emails**\
The new **RESTricted Emails** section on the **Notifications** page of the Admin module helps ensure that ARM-related emails are not sent to deactivated users.

Admins can either add users to this list manually or deactivate the respective users from the **Users** page of the Admin module, and they will be automatically added to this list. These users will not receive ANY emails including deactivation, forgotten password, reset password, jobs executed in the application, etc. Admins can also use the same two methods to reactivate a user and remove them from this list.

There is also a provision for an Admin to remove all users from the **RESTricted Emails** list at once.

**5. Dependency Analyzer**\
Dependency Analyzer helps you understand the dependencies among various components in your Salesforce org. It allows you to analyze the relationships among objects, fields, classes, triggers, and other metadata components.

With Quality Gates, ARM helps Salesforce developers run multiple checks to understand if and how their commits can break a Salesforce org. Currently, we enforce the following gates:

* SAST, SSPM, and AST (Static Code Analysis, Salesforce Security Posture Management, and Application Security Testing)
* Deployment Validation
* File Change Footprint
* Peer-to-Peer Code Review

With the introduction of the Dependency Analyzer, we can offer a fourth gate, Dependency Check, which will allow users to see what they are missing due to Salesforce specificity.

We have introduced the Dependency Analyzer in CI Jobs for now, and this is just a start at bringing this functionality to the remaining modules soon.

Users now have the option to ‘**Run Metadata Dependency on Failed Deployments**’ to view the results of failed metadata components with their dependencies and download them in Manifest and XML formats.

**6. ServiceNow – ALM Management**\
The ARM–ServiceNow integration automatically posts updates to ServiceNow tickets. It makes tracking the status of your user stories and support tickets faster and easier. Tasks can be organized by project, allowing an organization to track issues within projects transparently.

ServiceNow will make information more easily accessible and workflows more streamlined, reducing the time and effort required to manage and resolve service requests. Additionally, the integration will allow teams to work more effectively, improving collaboration and communication.

### Enhancements

1. **Salesforce Spring (API 57.0) & Summer (API 58.0) Support**\
   AutoRABIT supports the most recent API 57.0 & API 58.0 versions in this release to keep our product updated with Salesforce updates. The most recent API version is intended for customizing and developing tools to manage the metadata model.
2. **Exporting Selected User Details**\
   Users with Admin access can now choose the fields they want to include while exporting users' details to a CSV file. While selecting the Export option, the list of available fields is displayed. Admins can select and deselect the required fields by clicking the corresponding checkbox. Some of the fields are selected by default for ease of use. Admins can always deselect these fields if they are not required. Thus, based on the teams with whom they will be shared, Admins can customize the fields in the list.
3. **More Info on CI Jobs and Info**\
   Users are now able to view the CI Jobs they created in the CI Job List screen to date inside ARM. The list is displayed in chronological order with the most recent jobs listed at the top.
4. **'Created and Requested by' in Deployment UI**\
   Users are now able to view the ‘Created by’ and ‘Triggered by’ fields in the Deployment home screen without scrolling through multiple screens for this info, enabling monitoring of the deployment’s real-time progress. [Read more](../../../product-guides/arm/arm-features/deployment/)
5. **Self-Service Connected App Setup for Jira OAuth in ARM**\
   We've introduced a self-service feature allowing users to set up Jira OAuth-connected apps in ARM autonomously. With guidance from our user manual's Connected App guide, users can effortlessly create and register their app credentials, eliminating the need for support team assistance. Users can quickly establish a robust connection by inputting the generated Client ID and Server Key into ARM's settings.
6. **Unified Admin Roles**\
   We’re excited to introduce a streamlined and more efficient Admin experience. We’ve consolidated the roles of Super Admin and Registered Admin into a single empowered Admin role. This change means Admins now have a unified set of tools and permissions, streamlining tasks and creating a more user-friendly Admin experience.
7. **CI Jobs List and Results: Filter and Export Option**\
   We've enhanced the platform with a user-friendly quick filter and export feature in response to user feedback. This functionality empowers administrators, release managers, and users to efficiently organize and analyze data by alphabet or date, facilitating faster insights and informed decision-making.
8. **Create Artifact: Release label more than 180 days**\
   In the Create Artifact section, users can now generate a Release Label and have the flexibility to choose an extended timeframe of over 180 days for retrieving comprehensive commit history data. This enhancement offers users a broader historical perspective, facilitating more in-depth analysis and tracking of commits for their projects.
9. <mark style="color:blue;">**Enhanced security and user experience. (NEW)**</mark>\
   The new features focus on enhancing security and user experience. They include a single-user session control to prevent multiple active sessions under the same username, automatic logout for inactivity to bolster security, and support for multiple tabs or pages in the same browser, improving user productivity and maintaining the environment's integrity.

### Improvements

This update has implemented significant performance upgrades to enhance the tool's efficiency and responsiveness. These enhancements encompass optimized queries and leveraging newer technologies, collectively resulting in a smoother and faster user experience.

### Changelogs

**17 December 2023**

**(ARM v. 23.1.12)**

<table data-full-width="true"><thead><tr><th width="148">Module</th><th width="284">Summary</th><th width="124">Fix Version</th><th width="132">Resolution</th><th width="200">Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Profile/Permission Set Manager Report not loading</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>ARM and CodeScan integration EZ- Commit validation issue. Feature Flag: USE_MASTER_ANALYSIS_PACKAGE_DIRECTORY</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>A non admin user cannot access the repository under the VC module.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Help investigating deployment errors</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Not receiving post activity notifications</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Feedback option change to message. Will require updated documentation.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>[On-premises – Signup for Demo] The registration screen opens when clicking on 'Signup for Demo,' even if the account is already registered.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>[On-premises] Service registration tab, alignment tab not visible properly and, when clicking on the tab, redirects to the logout page.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Unable to view ‘Credential already exists’ popup under ‘My profile.’</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Reports</p><p> </p></td><td>Previously deleted log showing on other label if created Static Code Analysis label previously deleted SCA label name.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>SFDX</p><p> </p></td><td>When creating the package on a new module for the first time through modularization, Package creation failed with the error ["SaiJun19thprofile: An object 'SaiJun19thprofile' of type Profile was named in package.xml.'] Will require updated documentation.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to view committed files in direct EZ revert commit using DX repository.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>[On-Premises] Getting 'Malformed Id: Null' error displaying for a few seconds when performing a rollback operation for Org-to-Org deployment.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>[Org Synchronization] ‘SourceOrg,’ ‘Created date,’ and ‘Created by’ filters are not working properly.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>[On-Premise Testing] CI Job with template option failed due to "Data and Metadata retrieval Failed” error.</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>ARM API to perform a deployment (or validation or quick deploy)</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>[ARM-SIT] Unable to view branches in SCM history screen</td><td><p> </p><p>23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

**10 December 2023**

**(ARM v. 23.1.11)**

<table data-full-width="true"><thead><tr><th width="142">Module</th><th width="276">Summary</th><th width="111" align="center">Version(s)</th><th width="130" align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td><p> </p><p>All Modules</p><p> </p></td><td><p> </p><p>SF CLI Version upgrade to 2.19.8</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>No Code Fix</p><p> </p></td><td align="center">Configuration Change request</td></tr><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Experience bundle not properly generated when deploying using release label</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>SFDX</p><p> </p></td><td><p> </p><p>Error creating unlocked package</p><p> </p></td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>CI Job report for Master-to-BackMerge Org Sync_13-Deployment Failed</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Merge shows no modification, but a CI job is triggered</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>* User is unable to do nCino Feature Deployments * Requires documentation</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Dataloader</p><p> </p></td><td>Getting error when clicking on Dataloader configured filter </td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs and Deployments</td><td>ARM API to perform a deployment (or validation or quick deploy)</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Enchancement</p><p> </p></td></tr><tr><td><p> </p><p>Version Control</p><p> </p></td><td>Unable to perform merge for sub-user, getting error to re-login</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>On-premise: ‘Proxy Configuration settings,’ ‘Audit logs’ section, and ‘Pool Mgnt" screen tab are missing.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>On-premise: When trying to save the ‘Audit Logs’ section in ‘My Account’ screen, the error “Uncaught TypeError: Cannot read properties of undefined (reading 'showMessage')” is encountered in the console.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>For the 'Create and Install Package' job, when selecting 'Deploy Using Create a Scratch Org and Install Package,' after successfully completing the build, an error is displayed in the log: “this.salesForceOrgDAO” is null.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin</td><td>Getting ‘null parameters’ error when clicking on save in the user’s section.</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Unable to perform merge request for sub-user getting error to re-login.</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p>Version</p><p>Control</p></td><td>Unable to perform branching baseline on sub-user, getting error to re-login</td><td align="center"><p> </p><p>23.1</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 3 December 2023

**(ARM v 23.1.10)**

| Module          | Summary                                                                                                                                   | Fix Version(s) | Resolution                  | Cause          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------- | -------------- |
| Admin           | Issue adding user mapping                                                                                                                 | 22.3, 23.1     | Code Fix                    | Use Case       |
| Deployments     | Full org:org deployment failing with no proper reason                                                                                     | 23.1           | Code Fix                    | Use Case       |
| Admin           | Issue with registering new branch in the repository                                                                                       | 23.1           | Code Fix                    | Use Case       |
| Reports         | ARM and CodeScan integration EZ-Commit validation issue                                                                                   | 23.1           | Code Fix                    | Change Request |
| Reports         | New branch created CodeScan issue                                                                                                         | 23.1           | Code Fix                    | Use Case       |
| Deployments     | Destructive package is not generated properly when deploying from git revisions                                                           | 23.1           | Code Fix                    | Use Case       |
| Admin           | nCino View Object Failing                                                                                                                 | NA             | No Code Fix - Added Loggers | Data           |
| Deployments     | Org sync not completing                                                                                                                   | NA             | No Code Fix - Added Loggers | Data           |
| Dataloader      | Corrected a spelling mistake in ARM steps.                                                                                                | 23.1, 22.3     | Code Fix                    | Use Case       |
| Dataloader      | Corrected data seeding error preventing upsert                                                                                            | 23.1, 22.3     | Code Fix                    | Use Case       |
| Reports         | Getting ‘cannot invoke "String.length()" because of "text" is “null”’ error when performing the ‘Get latest reports’ in Weekly reports    | 23.1           | Code Fix                    | Use Case       |
| Reports         | When navigating to Static Code Analysis screen from Reports module, getting the “comparison method violates its general contract!” error. | 23.1           | Code Fix                    | Data           |
| Version Control | On DX branch release label artifact execution, on deleted components, the destructive changes artifact preparation is not generated.      | 23.1           | Code Fix                    | Use Case       |
| nCino           | On-premise testing: CI Job with template option failed due to "data and metadata retrieval failed” error                                  | 23.1, 22.3     | Code Fix                    | Use Case       |
| CI Jobs         | Failed to deploy destructive changes though CI jobs.                                                                                      | 23.1           | Code Fix                    | Use Case       |

#### 26 November 2023

**(ARM v 23.1.9)**

<table data-full-width="true"><thead><tr><th width="122">Module</th><th width="310">Summary</th><th width="145">Fix Version(s)</th><th width="134">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Admin</td><td>Branching baseline issue</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>The new feature of merging only revision in the CI job build is not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>CI job filter not working properly</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Commit not getting detected</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Rejecting a commit is merging the changes</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Unable to save Pull Request Plugin config</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>AR commit File Diff process is failing with errors</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Merge auto-rejected but CI job triggered</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Changing role from Dev to Admin shows orgs and branches in New EZ- Commit without mapping under profile</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control and Deployment</td><td>Release Label Artifact not including code for a commit</td><td>23.1</td><td>Loggers Added</td><td>Data</td></tr><tr><td>Dataloader</td><td>Dataloader Pro jobs causing huge threads pileup</td><td>23.1</td><td>Enhancement</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Data Retention – CI Jobs - Observing 'java.lang.NumberFormatException' error in the CI Retention process log when processing the string '2023-08-26.' Please check the date formatting to ensure it is being treated as a string and not causing the exception.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>While submitting the ALM commit with these “&#x3C;ALM Issue ID>“, “{ALM Issue ID}” ALM patterns, unable to submit the commit</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Sub-user - Deployment History - While changing the date range filter, getting "Cannot invoke "String.equalsIgnoreCase(String)" because the return value of "com.autorabit.entity.deployment.DeploymentHistory.getCreatedBy()" is null" error</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>With Release label deployment, the flow-meta.xml retrieval issue both constructive and destructive</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 22 November 2023

<table data-full-width="true"><thead><tr><th width="126">Module</th><th width="290">Summary</th><th width="138">Fix Version(s)</th><th width="138">Resolution</th><th width="98">Cause</th><th width="158">Enabled by default?</th><th>Feature Flag Name</th></tr></thead><tbody><tr><td>Version Control</td><td>Branch Protection Policy enforced and behavior of EZ- merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td>NO</td><td>GIT_LOGGEDIN_USER_AS_COMMIT_USER</td></tr><tr><td>Version Control</td><td>Issue while creating feature branches in EZ - Commit screen</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td></td><td></td></tr><tr><td>Version Control</td><td>Upload File option not available during EZ- commit with Option package manifest</td><td>23.1</td><td>Code Fix</td><td>Use Case</td><td></td><td></td></tr></tbody></table>

#### 19 November 2023

**(ARM v. 23.1.8)**

<table><thead><tr><th width="121">Module</th><th width="283">Summary</th><th width="101">Fix Version</th><th width="105">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Deployment tab - Redeploy/Promote issue</td><td>22.3, 23.1</td><td>Added Loggers</td><td>Data</td></tr><tr><td>Dataloader</td><td>Optimize the Dataloader Pro job logs in the rabit cs log</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Unable to create Feature Migration Template on Debt Schedule object</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>All Modules</td><td>Invalid Email ID</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs, Deployments, Version Control, Admin</td><td>Org Sync diff report differs for the same source org compared to different orgs.</td><td>23.1</td><td>Code Fix</td><td>Use Case *</td></tr><tr><td>Dataloader</td><td>Urgent: AutoRABIT is down</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Issue with Block button during Merge Conflict</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>CI job deployment failing: Restriction rules deployed as moderation rule and made the deployment bugged</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Urgent: Rollback of specific components - Issue</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Unexpected behavior when disabling component category on rollback destructive changes.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>SFDX</td><td>Error while using Scratch Org Management tab</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>All Modules</td><td>ARM&#x3C;>ULP Integration Issues</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Auto-reject on commit validation for SCA &#x26; Auto-reject setting in Merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 15 November 2023

<table><thead><tr><th width="118">Module</th><th width="279">Summary</th><th width="107">Fix Version</th><th width="108">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>CI Jobs</td><td>CI Job is not picking up changes committed on the branch, indicating "No modifications made."</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Org Synchronization – constructive &#x26; destructive changes are not working together</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Admin</td><td>Sync error between ARM and GIT</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Deployment validation not working correctly during new EZ-Merge</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td>Merging only revision in the CI job build not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 12 November 2023

**(ARM v. 23.1.7)**

<table><thead><tr><th width="151">Module</th><th width="249">Summary</th><th width="138">Fix Version(s)</th><th width="119">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>During Org Sync, file names are being repeated as part of the deployment results.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>User is unable to see the Deployment History.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs &#x26; Deployments</td><td>User is unable to deploy static resource.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Reports</td><td>Scheduled Code Coverage Reports are running at the wrong time.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>User is unable to create Feature Migration Template on Debt Schedule object.</td><td>22.3, 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Dataloader</td><td>User is unable to upload files and update records; system logs user out instead.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>User is getting timeouts in merge screen.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 5 November 2023

**(ARM v. 23.1.6)**

<table><thead><tr><th width="153">Module</th><th width="277.3333740234375">Summary</th><th width="121">Fix Version(s)</th><th width="108">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td>All Modules</td><td>SF CLI version upgrade to 2.14.6</td><td>23.1</td><td>Code Fix</td><td>Enhancement</td></tr><tr><td>Environment Provisioning</td><td>View environment provisioning templates</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Enhancement</td></tr><tr><td>Admin</td><td>Branching baseline is not picking all components from production</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Deployments</td><td>Help with destructive change</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Merge request is failing due to validation credentials</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs, Deployments</td><td>Issues with a release – related to Feature Flag - not automatically deployed: STANDARD_VALUE_SET_DELTA</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Version Control</td><td>Approval button is not visible after successful merge validation</td><td>22.3 &#x26; 23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Version Control</td><td>Create artifact: not completed</td><td>23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>Admin</td><td>AutoRABIT login not working</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Error pop-up during merge type selection as Commit Label in EZ-Merge</td><td>23.1</td><td>Code Fix</td><td>Data</td></tr><tr><td>CI Jobs</td><td>AutoRABIT AccelQ Integration/ bhg-inc.com</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>CI Jobs</td><td><br>Developer API for CI Jobs History not returning latest results.</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Ability to trigger nCino CI jobs using REST API</td><td>23.1</td><td>Code Fix</td><td>Customer Request</td></tr><tr><td>CI Jobs</td><td>For run test automation scripts job: More than one cycle is not displayed in the individual job history</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Unable to delete feature branch under merge request, getting internal server error</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Unable to view the entry of recently created merge request in the merge request history screen</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>Version Control</td><td>Criteria met ALM's not getting fetched under merge request</td><td>23.1</td><td>Code Fix</td><td>Use Case</td></tr><tr><td>nCino</td><td>Instead of POST methods need to change the GET</td><td>23.1</td><td>Code Fix</td><td>Customer Request</td></tr></tbody></table>

#### 27 October 2023

**(ARM v. 23.1.5)**

This was a maintenance release. The following items were enhanced, fixed, or added:

* <mark style="background-color:blue;">**Loggers**</mark> were added to **Reports** and **Dashboard** modules in versions 22.3 and 23.1 due to a data error in which users were unable to fetch a Salesforce **code coverage** report.
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Deployments** and **Org Synchronization** modules in versions 22.3 and 23.1 enabling users to **change deploy text for validations**.
* A code fix was applied to the **CI Jobs** module in version 23.1 identified by use case to **enable validation CI Job comments** to be visible on the **Bitbucket PR**.
* A code fix was applied to the **Admin** module of version 23.1 due to a use case in which modification logs were needed for **Version Control mapping setup**.
* A code fix was applied to the **Version Control** module of version 23.1 related to a use-case error in which **External Pull Requests, when expanding the files in the diff, content was not visible** and showing as undefined.
* A code fix was applied to the **Version Control** module of version 23.1 related to a use-case error in which **External Pull Requests, when expanding files in the diff,** show **duplicate** content.
* A code fix was applied to the **nCino** module of versions 22.3 and 23.1 due to a use-case scenario during dataset creation with saving only user info in **Json that is relevant to current dataset**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error with an **AR merge failing**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error in which the **incorrect removal of Custom Application type in package.xml on EZ-Commit** via AR occurred.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 in which two **external pull request** issues were occurring.

#### 25 October 2023

This was an interim maintenance release. The following items were enhanced, fixed, or added:

* A Code Fix was applied to the **Deployments** module due to the **Deployment initiated using Org Synchronization failing** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Version control** module due to a **Validation Error** requiring **Feature Flag:** **VALIDATE\_DEPLOY\_PICK\_FILECHANGES\_FROM\_DIFF** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Reports** module due to the **Weekly Code/ Test Coverage Report** taking a long time caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Admin** module due to an **SSO Error** as of Sept 25 caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Admin** module due to an AutoRABIT **Login Issue** caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Version Control** module due to **validation/merge errors** after latest release caused by a use case with a fix applied to versions 23.1.
* A Code Fix was applied to the **Dataloader** module due to the **download button not working** caused by a use case with a fix applied to versions 23.1.

**22 October 2023**

**(ARM v. 23.1.4)**

This is a maintenance release. The following items were enhanced, fixed, or added.

* Performed a code fix to version 23.1 affecting the **Reports** module resulting from a use-case error with **code coverage report emails missing test class errors in the subject.**
* Applied a code fix to version 23.1 for the **Deployments** module resulting from a use-case scenario with user **unable to see deployment history**.
* Instituted a code fix to version 23.1 for the **CI Jobs** module resulting from a use-case error with the **org management page**.
* Implemented a code fix to versions 22.3 and 23.1 affecting the **CI Jobs** module due to a use-case issue to **SFDX/CI jobs with package version installation key**.
* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue related to **custom label translation file**.
* Applied a code fix to versions 22.3 and 23.1 related to the **Deployments** module for a use-case error with previous **deployment label 'add members'** option not working.
* Performed a code fix to version 23.1 affecting the **Admin** module due to a use-case error with **MyProfile not redirecting properly** and showing the **profile icon** after clicking on the **'profile' button.**
* Implemented a **flow center change** to versions 22.3 and 23.1 for the **Dataloader** module due to a use-case error with the **download button not working**.

#### 18 October 2023

This interim release consisted of the following:

* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue with a **custom label translation file**.

#### 15 October 2023

**(ARM v23.1.3)**

**AutoRABIT provided the API 59.0 changes as part of its weekly fixes on both 22.3 and 23.1. This is available only for ARM modules, not for Dataloader or nCino. For DL and nCino, API 59.0 changes will be available next week as part of the Wednesday fixes deployment.**

This is a maintenance release. The following items were enhanced, fixed, or added.

* Instituted an <mark style="background-color:blue;">**enhancement**</mark> via code fix to versions 22.3 and 23.1 affecting **all ARM modules**, applying **Salesforce v.59 upgrade** for **Winter 2024**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **CI Jobs** module concerning a **package directory** issue.
* Applied a code fix to versions 22.3 and 23.1 due to a use-case scenario pertaining to the **Environmental Provisioning** module with **users not able to generate** a **migration template** using the **migrate custom setting data module**.
* Issued a code fix to versions 22.3 and 23.1 for a use-case error in the **Version Control** module with a **custom label translation file**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Deployments** module concerning **bugs in deployment** with **multi-packages** and **static resource**.
* Applied a code fix to version 22.3 resulting from a use-case error affecting **Dataloader** returning an '**invalid cross reference id**' error for **ProcessInput** and **ProcessingInputCondition** objects.
* Implemented a code fix to version 23.1 for a use-case error to the **Version Control** module, in which **duplicate commits** were being created.
* Performed a code fix to version 23.1 for a use-case error to the **Version Control** module pertaining to **Deployment history**, with the **deployment status not being visible**.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **nCino** module in which users are **unable to deploy nCino feature (RBC)**, instead returning a '**malformed query**' result.
* Performed a code fix to version 23.1 relating to a use-case error to the **Version Control** module with users **unable to perform new pull request commit** due to **commit template permission**.
* Executed a code fix to version 23.1 relating to a use-case error affecting the **Version Control** module with users continually **getting a login redirect error** when trying to **create a branc**h through an **EZ-Commit**.
* Performed a code fix to version 23.1 relating to a use-case error in the **Version Control** module with users **unable to create a commit label**, continually getting a **login redirect** error.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **Admin** module, particularly a **SuperAdmin** user, not getting any response to the **scheduler's service registration button** without **expanding** the selection.
* Initiated a code fix related to a use-case scenario in version 23.1 affecting the **Version Control** module with **release labels getting failed after restarting** the agent.
* Applied a code fix related to a use-case scenario affecting version 23.1 in the **nCino** module, when **parallel CI jobs limit** was reached, the **job** was **not added** to the **queu**e.
* Performed a code fix to correct a use-case error in version 23.1 related to the **nCino** module for a **merge missing changes**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the Version Control module, in which users were **unable to create/append a revision** to an **existing label** for a **sub-user**.
* Implemented a code fix to version 22.3 relating to a use-case error in the **Version Control** module in which the user was getting **empty error pop-ups** under the **ALM management screen** for a **sub-user**, not displaying the **ALM item**s.
* Performed a code fix to version 23.1 relating to a use-case error affecting the **nCino** module with a **job deployment** issue.
* Applied a code fix to version 23.1 relating to a use-case error affecting the **nCino** module for a **CI job build getting failed**.
* Initiated a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **nCino** module for a '**no modifications status**' displayed for a **version control BR job**.

#### 11 October 2023

* Performed a code fix to versions 22.3 and 23.1 related to a use case scenario affecting the **Version Control** module related to **ALM tickets** being **bugged** after using the **ALM sync refresh**.
* Performed a code fix to version 23.1 related to the **Deployments** and **CI Jobs** modules affecting a use-case error being issued during **CI Deployment** for **property 'userLicense' not valid** in version 57.0.

#### 8 October 2023

#### (ARM v23.1.2)

This is a maintenance release. The following items were enhanced, fixed, or added.

* Performed a code fix to versions 22.3 and 23.1 for a use-case error affecting the **Admin** module relating to **code coverage issues**.
* Applied a code fix to versions 22.3 and 23.1 related to a use-case error in the **Deployments** module concerning a **flow component missed in the deployment**.
* Implemented a code fix to versions 22.3 and 23.1 for a use-case error related to a specific customer’s fields for **redeployment**.
* Applied a code fix to version 23.1 for a use-case error affecting the **Deployments** module related to **metadata production and a deployment issue**.
* Integrated a code fix to version 23.1 affecting the **Deployments** and **CI Jobs** modules for a **deployment issue running all test classes**.
* Performed a code fix to the **nCino** module in version 23.1 pertaining to **Salesforce Orgs not showing** as **source orgs** for **nCino feature management deployments**.
* Applied a code fix to the **nCino** module in versions 22.3 and 23.1 pertaining to **\[arm-qan] no modification status displayed for version control BR job**.
* Added **loggers** to versions 22.3 and 23.1 to correct a use-case error in the **Deployments** module pertaining to a **deployment bug** occurring with **multi packages** and **static resources**.

#### 1 October 2023

**(ARM v23.1.1)**

This is a maintenance release. The following items were enhanced, fixed, or added.

* A code fix was applied to the version control module in releases 22.3 and 23.1 due to a use-case error with a **user being unable to create a new commit**.
* A code fix was performed in the 23.1 release to the version control module for a use-case error when **merging destructive changes**.
* A code fix was instituted to the CI Jobs module in version 23.1 to address when **a CI job has two different package directories**. Changes were failing under one package when the analysis was completed in CodeScan.
* A code fix was performed for release versions 22.3 and 23.1 to the deployments module for a use-case error resulting in a **buggy deployment** with **multi packages** and the **static resources** being bugged as well.
* A code fix was applied to the version control module in releases 22.3 and 23.1 concerning a use-case error for an **EZ-Commit**, where the **user was unable to view the 'deleted components' tab** for the commit template when unchecking the '**skip mappings**' checkbox.
* A code fix was implemented to versions 22.3 and 23.1 to correct an error with the deployments module due to a **deployment** initiated using **org synchronization failing**.
* A code fix was applied to releases 22.3 and 23.1 due to a use-case error in which the **registration date** of the **repository** **was not correct** in the **version control repository** (**created date** in AutoRABIT).
* A code fix was performed to versions 22.3 and 23.1 due to a data error in the version control module **preventing ALM working items from loading**.
* A code fix was initiated for versions 22.3 and 23.1 due to a data error affecting the reports module, which occurred when executing a **static code analysis** (CodeScan) report.
* A code fix was performed to version 23.1 in the version control module resulting from a data error on the **commit history screen**.
* A code fix was implemented in versions 22.3 and 23.1 to the version control module related to a use-case error wherein the **baseline job** has **modified the Salesforce folder structure in GitHub**.
* **Loggers were added** in the version 23.1 release due to a data error in the version control module causing **duplicate commits** to be created.
* A code fix was implemented to the nCino module for versions 22.3 and 23.1 for a data error in which the **records count** was **not** being **updated** in the object sidebar for the version control baseline revision job.

#### 24 September 2023

**(ARM v23.1)**\
This is a maintenance release. The following items were enhanced, fixed, or added:

* A code fix was applied to the Deployment module due to a data error concerning an Org difference pulling changes from the managed packages.
