# Release Notes 23.1

## ARM Release Notes 23.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**September 2023**

**Version 23.1 – New Features, Enhancements, and Improvements**

### New Features

**1. Automatic Merge after Successful CI Build**\
We know that understanding and managing version control can sometimes be a challenge. ARM offers the flexibility to cherry-pick branch revisions for merge or deployment. Now you can automate this process of cherry-picking the revisions in CI Jobs as a post-deployment step.

The '**Run Merge process on successful deployment**' feature keeps track of builds in source branches and merges them into a designated destination branch if they meet the configured criteria (for example, if the build is successful). Rather than requiring manual effort, upstream merges may now be automated by the **Salesforce Release Manager** using revision numbers that were determined as part of a build cycle in CI jobs.

Users will be notified via email of the success or failure of the automated merge process.

[Read more](https://knowledgebase.autorabit.com/docs/automatic-merging-when-ci-builds-pass)

**2. Create and Install an Unlocked Package Version from a Version Control Branch**\
Use ARM CI intelligence to create a package version, build using the SFDX project structure in a Version Control branch, and install the same in the destination org of your choice—all from the same page.

You can now generate an unlocked package version automatically through the CI job, and as part of the deployment, it is deployed in the same build cycle. Until the 22.2 version, it picked the latest package version that was already successfully created in ARM.

When users create a CI job using this option, ARM checks the Version Control. If there is a change, it builds a new version on top of the packages. Once the package is created, then the deployment is triggered automatically.

[Read more](https://knowledgebase.autorabit.com/docs/create-and-install-an-unlockedmanaged-package-version-from-a-version-control-branch)

**3. Create Connected Apps**\
ARM now gives access to users to create and maintain their OAuth credentials. Users can set up the **Connected Apps** for Jira OAuth and register the credentials with ARM.

You can add, edit, and delete your Jira login credentials instead of contacting AutoRABIT to manage the connected apps. Once created, simply provide us with the connected app details like **Client ID** and **Secret Keys**.

We use these details to connect as an ALM and test the connection.

[Read more](about://knowledgebase.autorabit.com/docs/jira#creating-connected-apps)

**4. RESTricted Emails**\
The new **RESTricted Emails** section on the **Notifications** page of the Admin module helps ensure that ARM-related emails are not sent to deactivated users.

Admins can either add users to this list manually or deactivate the respective users from the **Users** page of the Admin module, and they will be automatically added to this list. These users will not receive ANY emails including deactivation, forgotten password, reset password, jobs executed in the application, etc. Admins can also use the same two methods to reactivate a user and remove them from this list.

There is also a provision for an Admin to remove all users from the **RESTricted Emails** list at once.

[Read more](about://knowledgebase.autorabit.com/docs/configure-mail-server-settings#restricted-emails)

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

**1. Salesforce Winter (API 57.0) & Spring (API 58.0) Support**\
AutoRABIT supports the most recent API 57.0 & API 58.0 versions in this release to keep our product updated with Salesforce updates. The most recent API version is intended for customizing and developing tools to manage the metadata model.

[Read more](https://knowledgebase.autorabit.com/docs/salesforce-api-version)

**2. Exporting Selected User Details**\
Users with Admin access can now choose the fields they want to include while exporting users' details to a CSV file.

While selecting the Export option, the list of available fields is displayed. Admins can select and deselect the required fields by clicking the corresponding checkbox. Some of the fields are selected by default for ease of use. Admins can always deselect these fields if they are not required.

Thus, based on the teams with whom they will be shared, Admins can customize the fields in the list.

[Read more](about://knowledgebase.autorabit.com/docs/users-roles-and-permissions#export-users)

**3. More Info on CI Jobs and Info**\
Users are now able to view the CI Jobs they created in the CI Job List screen to date inside ARM. The list is displayed in chronological order with the most recent jobs listed at the top.

[Read more](about://knowledgebase.autorabit.com/docs/users-roles-and-permissions#export-users)

**4. 'Created and Requested by' in Deployment UI**\
Users are now able to view the ‘Created by’ and ‘Triggered by’ fields in the Deployment home screen without scrolling through multiple screens for this info, enabling monitoring of the deployment’s real-time progress.

[Read more](https://knowledgebase.autorabit.com/docs/single-dataloader)

**5. Self-Service Connected App Setup for Jira OAuth in ARM**\
We've introduced a self-service feature allowing users to set up Jira OAuth-connected apps in ARM autonomously. With guidance from our user manual's Connected App guide, users can effortlessly create and register their app credentials, eliminating the need for support team assistance. Users can quickly establish a robust connection by inputting the generated Client ID and Server Key into ARM's settings.

**6. Unified Admin Roles**\
We’re excited to introduce a streamlined and more efficient Admin experience. We’ve consolidated the roles of Super Admin and Registered Admin into a single empowered Admin role.

This change means Admins now have a unified set of tools and permissions, streamlining tasks and creating a more user-friendly Admin experience.

**7. CI Jobs List and Results: Filter and Export Option**\
We've enhanced the platform with a user-friendly quick filter and export feature in response to user feedback. This functionality empowers administrators, release managers, and users to efficiently organize and analyze data by alphabet or date, facilitating faster insights and informed decision-making.

**8. Create Artifact: Release label more than 180 days**\
In the Create Artifact section, users can now generate a Release Label and have the flexibility to choose an extended timeframe of over 180 days for retrieving comprehensive commit history data. This enhancement offers users a broader historical perspective, facilitating more in-depth analysis and tracking of commits for their projects.

### Improvements

This update has implemented significant performance upgrades to enhance the tool's efficiency and responsiveness. These enhancements encompass optimized queries and leveraging newer technologies, collectively resulting in a smoother and faster user experience.\


## nCino Release Notes 23.1 <a href="#ncino-release-notes-23-1" id="ncino-release-notes-23-1"></a>

**September 2023**\
**Version 23.1 – Streamlined CI/CD and Enhanced Control**

We're thrilled to introduce a series of exciting enhancements to elevate your nCino experience. Get ready for:

**1. Precision Deployment:** Define your baseline revisions and effortlessly trigger builds for new revisions, enabling delta deployments. Package multiple commit revisions together for swift Record-Based Configuration (RBC) deployments.

**2. Multi-Sandbox Mastery:** Seamlessly deploy nCino CI builds to multiple target sandboxes, with the flexibility to choose up to 5 organizations per job. Say goodbye to redundant job creations for the same deployment across multiple Orgs.

**3. Effortless Job Management:** Our revamped CI job flow guides you directly to the ‘Job List’ page, streamlining your experience. A simple ‘Run’ button on this page empowers you to initiate jobs effortlessly.

**4. Rollback Assurance:** Take control of your nCino RBC deployments with our rollback feature. Capture snapshots before deployment and confidently revert your Org to its prior state if needed.

**5. Access + Validation:** We've renamed 'Applied Mappings' to 'External ID Mapping' for clarity. Plus, enjoy peace of mind with automated validation, ensuring your access to objects and essential external ID fields.

**6. Post-Deployment Insights:** Keep a finger on the pulse of post-deployment activities. The ‘Post Deploy Details' section provides consolidated updates for multiple Orgs. Dive deeper with 'View Details’ to explore Orgs and their records effortlessly.

## Changelogs

#### 8 October 2023

#### (ARM v23.1.2)

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Performed a code fix to versions 22.3 and 23.1 for a use-case error affecting the **Admin** module relating to **code coverage issue**s.
* Applied a code fix to versions 22.3 and 23.1 related to a use-case error in the **Deployments** module concerning a **flow component missed in the deployment**.   &#x20;
* Implemented a code fix to versions 22.3 and 23.1 for a use-case error related to a specific customer’s fields for **redeployment**.
* Applied a code fix to version 23.1 for a use-case error affecting the **Deployments** module related to **metadata production and a deployment issue**. &#x20;
* Integrated a code fix to version 23.1 affecting the **Deployments** and **CI Jobs** modules for a **deployment issue running all test classes**.
* Performed a code fix to the **nCino** module in version 23.1 pertaining to **Salesforce Orgs not showing** as **source orgs** for **nCino feature management deployments**.
* Applied a code fix to the **nCino** module in versions 22.3 and 23.1 pertaining to **\[arm-qan] no modification status displayed for version control BR job**. &#x20;
* Added **loggers** to versions 22.3 and 23.1 to correct a use-case error in the **Deployments** module pertaining to a **deployment bug** occurring with **multi packages** and **static resources**.

#### 1 October 2023

**(ARM v23.1.1)**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* A code fix was applied to the version control module in releases 22.3 and 23.1 due to a use-case error with a **user being unable to create a new commit**.&#x20;
* A code fix was performed in the 23.1 release to the version control module for a use-case error when **merging destructive changes**.&#x20;
* A code fix was instituted to the CI Jobs module in version 23.1 to address when **a CI job has two different package directories**. Changes were failing under one package when the analysis was completed in CodeScan.&#x20;
* A code fix was performed for release versions 22.3 and 23.1 to the deployments module for a use-case error resulting in a **buggy deployment** with **multi packages** and the **static resources** being bugged as well.&#x20;
* A code fix was applied to the version control module in releases 22.3 and 23.1 concerning a use-case error for an **EZ-Commit**, where the **user was unable to view the 'deleted components' tab** for the commit template when unchecking the '**skip mappings**' checkbox.&#x20;
* A code fix was implemented to versions 22.3 and 23.1 to correct an error with the deployments module due to a **deployment** initiated using **org synchronization failing**.&#x20;
* A code fix was applied to releases 22.3 and 23.1 due to a use-case error in which the **registration date** of the **repository** **was not correct** in the **version control repository** (**created date** in AutoRABIT).
* A code fix was performed to versions 22.3 and 23.1 due to a data error in the version control module **preventing ALM working items from loading**.&#x20;
* A code fix was initiated for versions 22.3 and 23.1 due to a data error affecting the reports module, which occurred when executing a **static code analysis** (CodeScan) report.&#x20;
* A code fix was performed to version 23.1 in the version control module resulting from a data error on the **commit history screen**.&#x20;
* A code fix was implemented in versions 22.3 and 23.1 to the version control module related to a use-case error wherein the **baseline job** has **modified the Salesforce folder structure in GitHub**.
* **Loggers were added** in the version 23.1 release due to a data error in the version control module causing **duplicate commits** to be created.&#x20;
* A code fix was implemented to the nCino module for versions 22.3 and 23.1 for a data error in which the **records count** was **not** being **updated** in the object sidebar for the version control baseline revision job.&#x20;

#### 24 September 2023

**(ARM v23.1)**\
This is a maintenance release. The following items were enhanced, fixed, or added:

* A code fix was applied to the Deployment module due to a data error concerning an Org difference pulling changes from the managed packages.&#x20;
