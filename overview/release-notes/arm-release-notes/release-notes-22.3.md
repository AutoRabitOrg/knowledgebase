# Release Notes 22.3

**December 2022 - Version 22.3 - New Features, Enhancements, Improvements and Changelogs**

**Date of release:** _18 December 2022_\
**Article last updated:** 31 _July 2023_

### New Features <a href="#new-features" id="new-features"></a>

#### 1. Retention Policy <a href="#1-retention-policy" id="1-retention-policy"></a>

You can now define a data **Retention Policy** and choose how much data should be stored for how long. ARM will now be considerably quicker by eliminating outdated data. Clearing out old and useless data from the database and moving it to the archives keeps the application from underperforming and improves speed across all modules.

A weekly clean-up will ensure that the application runs smoothly. The default data retention period is set as 12 months which will be implemented with the release of **ARM version 22.3**. Admins can specify the duration of data retention in the history tables from the My Account section and change the retention period from **12 months** to **6 months** or **3 months**.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings/)

#### 2. Search, Group, and Filter CI Job List <a href="#2-search-group-and-filter-ci-job-list" id="2-search-group-and-filter-ci-job-list"></a>

Finding a **CI Job** has never been easier. Instead of scrolling through endless pages, you can search for a job or a group by simply typing the name in the new dropdown lists. You can further narrow the search results by combining these two options to look for a particular job within a group.

Additionally, the **filter** feature provides further options to narrow the search results by source type, date range, and more.\
[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-list.md)

#### 3. Ability to Abort a Vlocity Deployment <a href="#3-ability-to-abort-a-vlocity-deployment" id="3-ability-to-abort-a-vlocity-deployment"></a>

We just included new functionality to the **ARM 22.3 version** that allows users to terminate an ongoing Vlocity deployment process or abort it if get stuck. The **Deployment History** screen contains the **Abort** option, which allows you to terminate the deployment process.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-I1GT03M7.png)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Release Label Revamp <a href="#1-release-label-revamp" id="1-release-label-revamp"></a>

The revamp of the **Release Label** page is the feature of version 22.3 that stands out the most. This enhancement is actually a collection of multiple smaller enhancements, each of which is briefly discussed in this section.

* While creating a release label, you can choose the specific period for which you want to retrieve the **commit history** instead of loading the entire commit history, which could take a really long time.
* You can also create a release label while simultaneously creating a **package** simply by selecting a conveniently located checkbox on the same screen.
* The **selected revisions** are also displayed on the same screen and updated dynamically as you select/unselect revisions.
* Release labels are **color-coded** on the **Release Label Summary** screen for easier identification, and the search now provides leaner results.

[**Read more →**](../../../product-guides/arm/arm-features/version-control/change-labels/release-labels.md)

#### 2. Additional Metadata Support in Search and Substitute <a href="#2-additional-metadata-support-in-search-and-substitute" id="2-additional-metadata-support-in-search-and-substitute"></a>

Additional metadata types are now compatible with the **Search and Substitute** rule, allowing the application to use them for Deployments and Commits.

Until now, the Search and Substitute functionality only had the ability to select a metadata type and then perform the search for substrings across all members in that type. But now, you can select specific metadata members in a type and substitute values for that member(s).

This enhancement is also helpful when users want to add object permissions only to the production and not to the lower sandboxes.

It is also beneficial to have this feature so that the rules can be created and used in **CI Jobs** to do the replacements automatically, depending on the deployment settings in the CI Job.\
[**Read more →**](../../../product-guides/arm/arm-features/search-and-substitute.md)

#### 3. Additional details in the Users Export List <a href="#3-additional-details-in-the-users-export-list" id="3-additional-details-in-the-users-export-list"></a>

**Export List** is a comprehensive list of all registered users with an organization. This list can be downloaded from the **Users** module. It includes details like the users' name, email, and title; and information about user accounts created, modified, deactivated, and deleted.

With the recent release, the **Export List** will include a few additional details related to the **last login** to ensure security and compliance. Details like the **location, login type, IP address, coordinates,** and the **browser** used.

The access level of users is not mentioned in the export list for security reasons, i.e., if any users are **Admin** or **Super Admin**, this will not be specified. The company can share this list, if required, with people both inside and outside their organization without jeopardizing the confidentiality of the access granted to the users.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings/users-roles-and-permissions.md)

#### 4. Dataloader Clone process <a href="#4-dataloader-clone-process" id="4-dataloader-clone-process"></a>

In addition to providing a new name, **Dataloader users** can now specify a different Salesforce org as a source or destination for the operation while cloning an existing job. This helps the users to reuse the same job configuration with a different Salesforce org without going through the entire process again.

For the **Extract** operation, users have the option to edit the query corresponding to the new org selected. For **Insert/Update/Upsert/Delete** operations, users have the option to upload a different **.CSV** file instead of the original one. Validation is done to verify whether the object is available in the new org and also if the user edits the query for the cloned process.\
[**Read more →**](release-notes-22.3.md#4-dataloader-clone-process)

***

### Improvements <a href="#improvements" id="improvements"></a>

* The `/syncbranchcommits` service is no longer supported. The users will no longer require **Auto-sync** functionality to create a release label. This simplifies the function's use and gets rid of unnecessary steps.
* For improved user experience, the **metadata.zip** file upload option has been added to the **New Deployment** page itself. When uploading large files, this is extremely useful.
* The **password policy** is reduced from **13** previously used passwords not being allowed to **5** previously used passwords. This gives users more options while resetting their passwords after the **three months** period or if they forget their password.
* Improvements have been made to **VC Repo flow** as well as to **Salesforce Org flow**. You can now run scans on a repo or an org to be tagged to the same project and run comparisons so that you have traceability across the scans. The comparison feature allows for every delta scanned to be compared with the baseline. Scans are run on the source, and the results are available in the **Reports** module. Users can trace the jobs run using the unique identifier.\
  Click [HERE](../../../product-guides/arm/arm-features/reports/static-code-analysis.md) to see a few points to note about these improvements.
* **Super Admin** and the user currently logged in are disabled for ALL actions. They cannot be added, deleted, suspended, activated, deactivated, edited, or their roles delegated to other users. Super Admin is displayed at the top of the users' list for easy identification.
* The **Users** module now displays the last login date and time of the users instead of the phone number, and the first and last names appear under the single **Name** column for better monitoring and tracking.
* **Super Admin** can now enter the desired thread pool count while registering an ARM agent.
* Customers can now request for **Pendo** and **Full Story** to be enabled or disabled for their instance. Simple toggle buttons to do this are added under the **Product Analytics** section on the **Super User Accounts** page. Only **Super Admin** will have access to this section.
* In **DataLoader**,
  * The number of records that are going to be impacted by the specific operation (Extract, Insert, Update, Upsert, or Delete) is displayed as a message before the operation begins and also on the **Summary** screen as **Records**.
  * **Filters** have been added to differentiate between the mapped and unmapped fields when auto-map is selected.
  * **Success** and **error count** of records is displayed while the job is still in progress.\
    Click [HERE](https://knowledgebase.autorabit.com/docs/single-dataloader) to read more about these improvements for each of the operations.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

**22 October 2023**

**(ARM v. 22.3.44)**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Implemented an <mark style="background-color:blue;">**enhancement**</mark> to version 22.3 identified as part of a use-case issue affecting the **Deployments** and **Org Synchronization** modules requiring changing deploy text for validations.&#x20;
* Implemented a code fix to versions 22.3 and 23.1 affecting the **CI Jobs** module due to a use-case issue to **SFDX/CI jobs with package version installation key**.
* Performed a code fix to versions 22.3 and 23.1 affecting the **Version Control** module for a use-case issue related to **custom label translation file**.&#x20;
* Applied a code fix to versions 22.3 and 23.1 related to the **Deployments** module for a use-case error with previous **deployment label 'add members'** option not working.
* Added **loggers** to version 22.3 affecting the **Version Control** module due to a use-case error with **user roles missing**.
* Added **loggers** to version 22.3 affecting the **CI Jobs** module resulting from a use-case with **automated package generation CI job AR server exception error**.
* Implemented a **flow center change** to versions 22.3 and 23.1 for the **Dataloader** module due to a use-case error with the **download button not working**.

#### 18 October 2023

This interim release consisted of the following:

* Performed a code fix to versions 22.3 and 23.1 affecting the Version Control module for a use-case issue with a custom label translation file.

#### 15 October 2023

**(ARM v22.3.43)**

**AutoRABIT provided the API 59.0 changes as part of its weekly fixes on both 22.3 and 23.1. This is available only for ARM modules, not for Dataloader or nCino. For DL and nCino, API 59.0 changes will be available next week as part of the Wednesday fixes deployment.**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Instituted an <mark style="background-color:blue;">**enhancement**</mark> via code fix to versions 22.3 and 23.1 affecting **all ARM modules**, applying **Salesforce v.59 upgrade for Winter 2024**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **CI Jobs** module concerning a **package directory** issue.
* Applied a code fix to versions 22.3 and 23.1 due to a use-case scenario pertaining to the **Environmental Provisioning** module with users **not able to generate a migration template** using the **migrate custom setting** data module.&#x20;
* Issued a code fix to versions 22.3 and 23.1 for a use-case error in the **Version Control** module with a **custom label translation file**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Deployments** module concerning **bugs in deployment with multi-packages and static resource**.
* Applied a code fix to version 22.3 resulting from a use-case error affecting **Dataloader** returning an '**invalid cross reference id**' error for **ProcessInpu**t and **ProcessingInputCondition** objects.
* Performed a code fix to version 23.1 relating to a use-case error to the **Version Control** module with users **unable to perform new pull request commit** due to **commit template permission**.
* Performed a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **Version Control** module, in which users were **unable to create/append a revision** to an **existing label** for a **sub-user**.
* Implemented a code fix to version 22.3 relating to a use-case error in the **Version Control** module in which the user was getting **empty error pop-ups** under the **ALM management screen for a sub-user**, not displaying the **ALM items**.
* Initiated a code fix to versions 22.3 and 23.1 relating to a use-case error affecting the **nCino** module for a '**no modifications status**' displayed for a version control BR job.

#### 11 October 2023

* Performed a code fix to versions 22.3 and 23.1 related to a use case scenario affecting the **Version Control** module related to **ALM tickets being bugged** after **using the ALM sync refresh**.

#### 8 October 2023

#### (ARM v22.3.42)

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* Performed a code fix to versions 22.3 and 23.1 for a use-case error affecting the **Admin** module relating to **code coverage issues**.
* Applied a code fix to versions 22.3 and 23.1 related to a use-case error in the **Deployments** module concerning a **flow component missed in the deployment**.   &#x20;
* Implemented a code fix to versions 22.3 and 23.1 for a use-case error related to a specific customer’s fields for **redeployment**.
* Applied a code fix to the **nCino** module in versions 22.3 and 23.1 pertaining to **\[arm-qan] no modification status displayed for version control BR job**. &#x20;
* Added **loggers** to versions 22.3 and 23.1 to correct a use-case error in the **Deployments** module pertaining to a **deployment bug** occurring with **multi packages** and **static resources**.

#### 1 October 2023

**(ARM v22.3.41)**

This is a maintenance release. The following items were enhanced, fixed, or added.&#x20;

* A code fix was applied to the version control module in releases 22.3 and 23.1 due to a use-case error with a **user being unable to create a new commit**.&#x20;
* A code fix was performed for release versions 22.3 and 23.1 to the Deployments module for a use-case error resulting in a **buggy deployment** with **multi packages** and the **static resources** being bugged as well.&#x20;
* A code fix was applied to the version control module in releases 22.3 and 23.1 concerning a use-case error for an **EZ-Commit**, where the **user was unable to view the 'deleted components' tab** for the commit template when unchecking the '**skip mappings**' checkbox.&#x20;
* A code fix was implemented to versions 22.3 and 23.1 to correct an error with the Deployments module due to a **deployment** initiated using **Org Synchronization failing**.
* A code fix was applied to releases 22.3 and 23.1 due to a use-case error in which the **registration date** of the **repository** **was not correct** in the **version control repository** (**created date** in AutoRABIT).&#x20;
* A code fix was performed to versions 22.3 and 23.1 due to a data error in the version control module **preventing ALM working items from loading**.&#x20;
* A code fix was initiated to versions 22.3 and 23.1 due to a data error affecting the reports module, in which a user was getting an error message when executing a **static code analysis** (CodeScan) report.&#x20;
* A code fix was applied to version 22.3 in the version control module pertaining to a use-case error with **changes not** getting **fetched via autodraft after reverting a commit**.&#x20;
* A code fix was implemented in versions 22.3 and 23.1 to the version control module related to a use-case error wherein the **baseline job** has **modified the Salesforce folder structure in GitHub**.&#x20;
* A code fix was integrated to the version control module in version 22.3 after a data error caused by a **feature template migration** issue. The feature flag is **MERGE\_SKIP\_AUTORESOLVE\_CONFIGURATION\_FILES**.&#x20;
* A code fix to version 22.3 was implemented affecting all modules from a data error when **setting up SFDX deployment**.&#x20;
* A code fix was applied to the version control module in version 22.3 resulting from a use-case error with an **ARM commit comment label error**.&#x20;
* A code fix was implemented to the nCino module for versions 22.3 and 23.1 for a data error in which the **records count** was **not** being **updated** in the **object sidebar** for the version control baseline revision job.&#x20;

#### 24 September 2023

**(ARM v22.3.40)**\
This is a maintenance release. The following items were enhanced, fixed, or added:

* A code fix was implemented due to a use-case error to the Version Control module regarding an issue with merging destructive changes.&#x20;
* A code fix was applied to the Deployment module due to a data error concerning an Org difference pulling changes from the managed packages.&#x20;
* A code fix was applied due to a use-case error relating to the Deployments module with a user unable to deploy components via Org Sync.&#x20;
* A code fix was applied pertaining to the CI Jobs module relating to a use-case error in which the CI Job has two different package directories and changes fall under one package when an analysis is completed on CodeScan&#x20;
* Performed a code fix relating to a use-case error in on the Deployments module in which a deployment bug with multi packags and static resource was bugged.&#x20;

#### 17 September 2023

**(ARM v22.3.39)**\
This is a maintenance release. The following items were enhanced, fixed, or added.

* A code fix was implemented to the **Deployment** module related to a use-case error encountered when **deploying Vlocity components** from a **Git branch**.&#x20;
* A code fix was implemented related to the **CI Jobs** module to institute **best practices** following a user session.
* A code fix was implemented to the **Version Control** module related to a use-case error pertaining to **\[integration\_EZ-commit]**. User was getting a **"no package .xml found to retrieve the members"** through **package manifest** when selecting **'all users or the respective SF org user.'**&#x20;

#### 10 September 2023

**(ARM v22.3.38)**

This is a maintenance release. The following items were enhanced, fixed, or added:

1. As part of this fix deployment, one of the feature flags, '**RUN\_PACKAGE\_JOB\_ENTIRE\_BRANCH\_78757**,' has been provided. Enabling this feature flag only applies to one specific customer.&#x20;
2. Implemented a code fix associated with the **version control** module for a use-case error in which **ALM working items were not loading**.&#x20;
3. Implemented a code fix for a use-case error pertaining to the **version control** module for an **approval email notification error**.&#x20;
4. As a result of a use-case error relating to a **feature template migration** issue, a new **feature flag** has been provided, '**MERGE\_CONFLICTS\_AUTORESOLVE\_CONFIGFILES\_USINGSOURCE,'** which must be enabled for one specific customer only: More details are provided in the ticket itself.&#x20;
5. Implemented a code fix related to a use-case error where the **AutoRABIT deployment** **initiated using Org Synchronization fails**. This error pertains to the **Version Control** module.&#x20;
6.  Implemented a code fix related to the **CI Jobs** module related to setting up **SFDX deployment, with the Feature Flag:**&#x20;

    | **RUN\_PACKAGE\_JOB\_ENTIRE\_BRANCH\_78757** |
    | -------------------------------------------- |

    Regarding one ticket, '**Setting up SFDX Deployment'**: \
    Only for the '**Create and Install an Unlocked/Managed Package Version from a Version Control Branch'** CI, type in the CI Job configuration. When selecting the 'Trigger build on commit' option, we have hidden the '**Process commit revision received via hook only**' sub-option. This change will be incorporated into our documentation. Further details are available in the ticket itself.&#x20;
7.  Implemented a code fix related to the **nCino** module error: &#x20;

    | **LLC\_BI\_\_Schedule\_Section\_\_c migration issue#1** |
    | ------------------------------------------------------- |
8. Implemented a code fix related to an internal ticket in ARM, in which the user was **not able to migrate related data** using the **Dataloader test environment setup** module.&#x20;
9. Implemented a code fix related to the **Deployment** module for an **EBR Manual Asyncid XML Copy Automation** error.&#x20;

#### 3 September 2023

**(ARM v22.3.37)**

This is a maintenance release. The following items were enhanced, fixed, or added:

* Implemented a **code fix** associated with the **version control** module related to a use-case scenario in which a **review artifact was not working**.&#x20;
* Implemented a **code fix** to the **nCino** module resulting from a user product suggestion to the **deployment history filter**.&#x20;
* Implemented a **code fix** to the **nCino** module related to an instance in which the **org name** was **not displayed** for the **destination org value field**.&#x20;

#### 27 August 2023

**(ARM v22.3.36)**

This is a maintenance release. The following items were enhanced, fixed, or added:

* **Error: "Merging from Devint branch to Developer branch (Back merge) is getting Auto Rejected":** Code fix to Version Control module on user merging from **Devint branch to Developer branch (Back merge) getting Auto Rejected**.&#x20;
* Implemented a **UI change** to include the **“Ignore Warnings”** option in both the **prevalidation commit** and **merge flows**. This requires a documentation change. See ticket for more details.&#x20;
* **Error: “\[Client] getting frequent page unresponsive errors in ARM":** \
  Introduced a UI change to support Salesforce orgs and the **previous label deployment type** in the deployment module.&#x20;
* Performed a code fix affecting the Deployments module related to a use-case error with the client **getting frequent page unresponsive errors** in ARM. This also requires an update in our documentation. Further information is in the ticket.&#x20;
* **Error: “Branching baseline is not picking all components from production":** Based on the customer-confirmed downtime window, it was necessary to enable the "**METADATA\_API\_TO\_DX\_CONVERSION**" **feature flag** for this fix deployment.&#x20;
* Performed a code fix concerning the Admin module due to an error with a branching baseline not picking all components from production with feature flag error: **‘METADATA\_API\_TO\_DX\_CONVERSION’**.&#x20;
* Error in **CodeScan Plugin pop-up window** where the user was **unable to type text in Org key drop-down selection field**, which required a code fix to the Admin module. (Internal ticket)
* Performed a code fix related to a use-case error during **Vlocity deployments showing "NoOrgFoung" after activation** of **LWC components**. Fix applied to the CI Jobs and Deployment modules.&#x20;
* Code fix applied to SFDX module for the user receiving an error message showing **login failed**. Also related to CI Jobs, **scratch org creation was being struck in progress** and **not able to be deleted**.&#x20;
* Applied a code fix for the Version Control module related to a user being **unable to select the ALM side, getting a JAVA error**.&#x20;
* Initiated a code fix to the **Deployments** module related to an error during an **EZ deployment from a single revision with profiles and comp-specific changes pulling all comps**. &#x20;
* Executed a code fix to the Deployments module on a use-case error affecting an **AR deployment initiated using Org Synchronization failing**.&#x20;
* Applied a code fix related to the following use-case error: **\[Cijobs-DXModulePckagecreation] facing the "\["An unexpected error occurred while preparing endpoint: null. Please contact Salesforce Support and provide the following error code: 795089467-5806 (-1215335089)"]**.&#x20;
* Initiated a code fix to the **nCino** module for a client use-case error concerning **spread template issues**.&#x20;
* Performed a code fix for a customer use-case scenario regarding an error related to an **nCino CI job deployment issue**.&#x20;

#### 20 August 2023

**(ARM v22.3.35)**\
This is a maintenance release. The following items were fixed and/or added:

* Performed a code fix impacting the Deployments and CI Jobs modules related to use cases in which **selected test classes for production were not running** and users were having **code coverage issues**.&#x20;
* Performed a code fix for the Admin module related to a specific user having difficulty with **PWD policy**.&#x20;
* Performed a code fix to the CI Jobs and Deployment modules relating to users **unable to deploy changes to production orgs** due to a **CI Jobs coding issue**.&#x20;
* Performed a code fix to the CI Jobs module related to an **error message as login failed**.&#x20;
* Performed a code fix on the CI Jobs module pertaining to **Vlocity SFI components not compiling LWC on destination orgs when deploying via CI Jobs**.&#x20;
* Performed a code fix related to the CI Jobs module for **CI Job not starting according to schedule**.&#x20;
* Performed a code fix related to the CI Jobs module to resolve an error related to **setting up SFDX deployment and CI Job configuration**.&#x20;
* Performed a code fix to the **nCino** module for an error in which the **screen template failed** with a **malformed query exception**.&#x20;

#### 13 August 2023

**(ARM v22.3.34)**

This is a maintenance release. The following items were fixed and/or added:

* Performed a code fix pertaining to all modules relating to an **SFDX to SF CLI Hotfix**.&#x20;
* Performed a code fix relating to **version control, CI jobs, and deployment modules initiated via change request due to ALM working items not loading**, resolved by enabling the customer domain name.&#x20;
* Performed a code fix for a data error with **feature flag name, ‘Disable\_Merge\_Rename\_Detection’** after a merge was failing and took hours to complete.&#x20;
* Performed a code fix for the version control, CI jobs, and deployment modules pertaining to a data error, **validation failing for the LWC component despite no error message being displayed in the logs**.&#x20;
* Performed a code fix related to a use-case error in the version control module pertaining to a **commit showing a “no modification” error**.&#x20;
* Performed a code fix related to a use-case error affecting the version control, CI jobs, and deployment modules caused by an **error merging a commit from the dev environment to the INT environment**.&#x20;
* Performed a code fix to the version control module resulting from a use-case error where the **commit was incorrectly showing “no modification”**.&#x20;
* Performed a code fix related to a data error pertaining to the version control module, when **Jira integration stories redeploy post sandbox refresh**.&#x20;
* Performed a code fix for a use-case error in the deployment module related to **filter-based retrievals not working when applying the ‘created by,’ ‘modified by,’ ‘created date,’ and ‘modified date’ filters**.&#x20;
* Performed a code fix related to a performance issue in the nCino module pertaining to **Spread Template** issues.
* Fixed an error in the deployment module when ‘**Run Specified Tests**’ is selected from the Apex Test Level dropdown.&#x20;
* Rather than a code fix, a **customer-specific utility** was provided to address **SSO login issues** in the admin module. This particular utility only works in **versions 22.3.9** or lower for one individual customer.&#x20;

#### 06 August 2023

**(ARM v22.3.33)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an error under reports where **code coverage emails** were **missing information**.&#x20;
* Fixed an error related to a **second deployment** starting in the middle of a deployment.&#x20;
* Fixed an error in version control module related to **not being able to commit or Repush changes** in the **Training Branch**.&#x20;
* Fixed an error in version control module related to a feature flag: **USE\_PATCH\_LOGIC\_IN\_EZCOMMIT** for\
  **Code overwritten** (feature not enabled by default).
* Fixed an error for CI Job module where **ALM-enabled failed due to Unparsable date error**.&#x20;
* Fixed an error concerning **multiple CI Jobs failing due to data error**.&#x20;
* Fixed an error related to the Deployment, CI Jobs, and Version Control modules occurring when **merging a commit from dev environment to INT environment**.&#x20;
* Fixed an error related to deployments getting **frequent page unresponsive errors** in ARM.&#x20;
* Fixed an error under the Admin module relating to being **unable to select the revision number while creating the Tag**.&#x20;
* Fixed an error for **Create and Install Package** CI job deployment failing if having multiple package directories on the branch.&#x20;
* Fixed an error under the Admin module, **My Account >> Merge Settings: Not visible Border for "Notify All Criteria Overwrites To"** field.&#x20;
* Fixed an error under the Admin module, which enabled **Domain names to be visible in the inspect mode**.&#x20;
* Fixed an error in the nCino module related to **\[ARM-QAN] attachments’** deployment Failed with Bulk API.&#x20;
* Fixed an error in the nCino module related to a **Pricebook** entry.&#x20;
* Fixed an error related to the nCino module with **scheduled Job not showing up in UI** after completion due to **Deploy Status Not Updated**.&#x20;
* Fixed an error related to the nCino module with a **CI Job Edit not populating with scheduled time details**.&#x20;

#### 30 July 2023 <a href="#23-july-2023" id="23-july-2023"></a>

**(ARM v22.3.32)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **duplicate** not working on **EZ-merge** requests related to **version control**.&#x20;
* Fixed EZ deployments from a single revision with profiles **comp-specific changes pulling all comps** during deployments.&#x20;
* Fixed an error related to **CI Jobs** not running the pipeline.&#x20;
* Fixed situations with both **version control prevalidation commit and merge** where static code analysis processes are stuck in an **In-progress** state when VNC is not started.&#x20;
* Helped generate the reports for CI/CD pipelines for **nCino reports**.&#x20;
* Performed Jira integration story’s redeploy **post-sandbox refresh** in version control.&#x20;
* Fixed a specified metadata type is unsupported: **\[processflowmigration]** error in CI Jobs.&#x20;
* Set up the **SFDX Deployment** in CI Jobs.&#x20;
* Fixed an error with a **CI Job** not identifying changes.
* Fixed an error related to BHG with **CI Job webhooks** failing to trigger.&#x20;
* Performed **nCino AR template** updates.&#x20;

#### 23 July 2023 <a href="#23-july-2023" id="23-july-2023"></a>

**(ARM v22.3.31)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with a merge use case of handling **deleted files** in both source and target branches by using **git rm** command.
* Fixed an issue where screen redirects to login page on clicking on **User activation email**.
* Fixed an issue where **Commit stuck in InProgress**.
* Fixed an issue where we receive **“JAXB marshall/unmarshall exception”** while getting directed to CI results screen.
* Fixed an issue where **Release labels are taking 30 minutes** or more to be available for repository in Version control.
* Fixed an issue where **Merges are taking a long time** to complete in version control.
* Fixed an issue where components selected on review component pages were being repeated in the next category in **Version Control**.
* Fixed an issue where same name should be reflected instead of **Commit showing a different name in Bitbucket** in Version Control.
* Fixed an issue where **JIRA ALM Filter mappings not working** in My profile & Version Control.
* Fixed an issue where the **Login rate exceeded error** on the Salesforce Integration user.
* Fixed an issue where **Backup to Version Control** is not backing up **Matching Rules** in Salesforce in CI jobs.
* Fixed an issue where the shared server with common DB creates another customer weekly report in another server.
* Fixed an issue where **Custom field property** didn’t deploy in CI Jobs and Deployment.
* Fixed an issue where **Diff report** is not generated in New Deployment Module.
* Fixed an issue where **Unsupported metadata template** execution is failing in **Sandbox Refresh** in **Environment Provisioning** module.
* Enhanced **DataLoader uber jar upgrade to 58.0.3**.
* Fixed an issue where we are facing **Record Configuration** Time Out in nCino.
* Enhanced UI in **Post Deployment** activities result page in CI Job – nCino.
* Enhanced the **View details page** not being visible unless post-deployment activities are completed – nCino.

#### 18 June 2023 <a href="#18-june-2023" id="18-june-2023"></a>

**(ARM v22.3.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced ARM by allowing **PAT Authentication** for **Jira**.
* Fixed an issue where user ran an **Org Synchronization** history job and tried to access the **Diff** report to see the metadata difference, but the page kept loading indefinitely without the required diff.
* Upgraded **Provar** to **version 2.10.1**.
* Fixed an issue where the **Approval** option wasn't functional for **L1 Approvers**, and the **Org Admin** couldn't bypass the approval gate on EZ-Merge.
* Fixed an issue with **nCino** where user created a **Feature** deployment task, but the jobs were stuck the queue.
* Introduced a new feature in **DataLoader** called **Hard Delete** which can be used to delete the data completely and permanently instead of sending it to the **Recycle Bin** of the org.
* Fixed an issue where **CI Job build** history was not displaying the results and throwing a blank page instead.
* Fixed a UI bug where **Abort** option for CI job was displaying even after the build was successful.
* Fixed an issue where duplicate ALM Commit entries were Displaying while performing ALM Commit with Vlocity repository.
* Fixed an issue where the CI edit configuration screen was taking longer to load than expected before throwing `Page Unresponsive` alert.
* Fixed an issue with **DataLoader Pro** where user created a new job and applied filter, but the source and destination orgs are taken from history page.
* Fixed an issue with **DataLoader** where **Insert** operation bulk API selection was resulting in console error message `serializeToString`.
* Fixed an issue where **Vlocity** metadata components were getting expanded on the **Finish** page.

#### 11 June 2023 <a href="#11-june-2023" id="11-june-2023"></a>

**(ARM v22.3.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where deployment failed with the error message `File cannot be loaded`.
* Fixed an issue where the **SharingCriteriaRule** component was not deployed to Production even though the user had selected it ([#73824](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000114206402)).
* Fixed an issue where the **SharingReasons** component was ignored when the deployment/validation was done using **Commit Label** as source, but the same component was processed using **Single Revision** deployment or **CI Job** deployment ([#72073](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112029001)).
* Fixed an issue where user was trying to create an connect an **Active Directory** but it kept failing ([#73582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113941053)).
* Fixed an issue where user was migrating a field value with **Rich Text Area Field** type but it was not reflecting in the target org as expected. Hyperlinks, font size, etc., were not migrated as present in the source Salesforce org ([#73371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113607033) and [#56084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091215009)).
* Fixed a UI bug where **Deployment Failed** line was displayed twice in the logs for failed deployments (internal ticket).
* Fixed an issue where admin was unable to release a user from a team (internal ticket).
* Fixed an issue where **Null Values** were displayed on the **ALM Labels** screen as well as the **ALM Details** tab on the respective **ALM Commit Label Details** screen (internal ticket).
* Fixed an issue where selected files for DX Commits were not displayed in the **File Changes** tab, and after the commit it was showing as **No Modifications** (internal ticket).

#### 04 June 2023 <a href="#04-june-2023" id="04-june-2023"></a>

**(ARM v22.3.24)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where a **CI job** failed to pick the external commit revision which was added to an ALM Label as part of **Smart Commits** sync ([#71444](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111273077)).
* Fixed an issue where **Class Coverage Report** generated was empty for one of the Salesforce orgs, and it was intermittent.\
  The same behavior was observed for **RunSpecified** and **RunLocal** test levels ([#71367](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111185001)).
* Fixed an issue where deploying test classes from manual deployment was throwing an out of memory error ([#71872](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111679026)).
* Fixed an issue where **BackUp to Version Control CI Job** was failing due to too many retrieval error messages even though the **Bulk API** option was enabled ([#72181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112197081)).
* Fixed an issue where while performing any commit, **Pull Request** enabled **CI Job** was triggering as expected; but its **Build** and **Deployment** status was not added in the **Comments** in **Bitbucket** ([#72811](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112765004)).
* Fixed an issue where **EZ-Commits** were stuck with **In-progress** status for a few hours before failing. But the commit revisions were generated at the repository level and updated in ARM database ([#72817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112807012)).
* Fixed an issue where the **Git author** was overridden by ARM ([#71393](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111202442)).
* Fixed an issue with **DataLoader** where user was unable to create an **Update** job because the functionality prompoted user to select the **Required field** within the **Mapping Fields** ([#73515](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000113850003)).
* Fixed an issue with DataLoader where user was getting a **script error** in the console while editing an existing old job (internal ticket).
* Fixed an issue where **Destructive** commit for DX was not working as expected for **Documents**, **Reports**, and **Dashboards** types (internal ticket).
* Fixed an issue where the **Layout** file was not displayed in the **Review Artifact** screen after resolving the layout **duplicates** (internal ticket).
* Fixed an issue where **4 CI jobs** were running parallelly even though the **parallel process limit** was **1** on the e**xternal agent** (internal ticket).

#### 28 May 2023 <a href="#28-may-2023" id="28-may-2023"></a>

**(ARM v22.3.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a compliance issue with **Apache Commons** by removing the text dependency ([#71947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111886005)).
* Fixed an issue where **CI Jobs** were failing due to empty **JSON** file(s) in the remote repository, and throwing the following error: `Failed to initiate deployment. Unexpected end of JSON input` ([#72217](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112229003)).
* Improved the UI by removing the **Validate Deployment** option if **Vlocity** is selected, and hiding the whole **Board Type** option if Vlocity is not enabled ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Fixed an issue where user was performing CI jobs for **Validate and Deploy** for a successful commit, but only validation was performed but not the deployment ([#72751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112682583)).
* Fixed an issue where CI job deployment was failing because the build was picking duplicate **Layout** values ([#71214](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110698400)).
* Fixed an issue where unwanted metadata changes were observed in the **package.xml** file while performing a commit ([#72089](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000112054140) and [#71820](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111655842)).
* Fixed an issue where **Branching Baseline** was not picking all the components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Enhanced **DataLoader** by adding related objects and the fields of those objects displayed, so you can select the required fields of the related objects in the filter criteria and edit the query through SOQL editor ([#58549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095408144) and [#38339](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064118003)).
* Fixed an issue with **nCino** where CI jobs that used a **Deployment** from **Version Control** were failing when the build was triggered ([#71914](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111840343)).
* Improved the **New Merge** screen by adding **Layouts** text in the **Skip Flow /Profile/ Perm.Set Access-Setting Duplicity Check** option (internal ticket).
* Fixed a UI bug where **SF Org Test Connection** notification message was displayed on an unrelated module (internal ticket).
* Removed the option to sign up for a 30-day Salesforce trial while registering a DevHub as the trial offer is no longer applicable (internal ticket).

#### 21 May 2023 <a href="#21-may-2023" id="21-may-2023"></a>

**(ARM v22.3.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where wrong **timezone** region was displaying for users ([#71553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111412006)).
* Fixed an issue where the **EZ-Commits report file** displayed the file count but not the components count ([#71538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111479094)).
* Fixed an issue where clone build jobs were taking between 10 and 25 minutes, which is much longer than expected ([#70227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109182447)).
* Fixed an issue where CI job build failed to show changes in the org after deployment ([#70791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110120443) and [#71956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111861212)).
* Fixed an issue where CI job to generate **Code Coverage Report** was not reflected in the org or in the e-mail notification ([#72042](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111983230)).
* Fixed an issue where merge status is displayed as completed but no revision is generated, and the merge is not available in the UAT branch ([#71266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110960210)).
* Enhanced **DataLoader** by adding the ability to **field mapping** through the lookup fields ([#58480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095290579)).
* Fixed an issue with **DataLoader** where while running an **Extract** job on the **PUBLISHER** object, the job was failing with the following error `Publisher: column id is not supported in ORDER BY clause` ([#71303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111030174)).
* Enhanced the **nCino filter criteria** by adding the ability to search and filter labels using the whole or partial name ([#71826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111666181)).
* Enhanced ARM by using known vulnerable components through the **DataTables 1.10.12** plugin for advanced data table functionalities such as sorting, filtering, pagination, and more. This allows users to easily display and manipulate large sets of data on their web pages in a user-friendly manner (internal ticket).
* Fixed an issue with **Prevalidation Merge** where users were unable to deploy the **ApexClass Tests** related to ApexClasses and Apex Triggers (internal ticket).
* Fixed a UI bug where the **date column** in the **EZ-Commit Weekly report** was displaying incorrect values (internal ticket).

#### 14 May 2023 <a href="#14-may-2023" id="14-may-2023"></a>

**(ARM v22.3.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was having trouble while deploying **LighteningMessageChannel** components ([#70787](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110191524)).
* Fixed an issue where **Destructive Changes** wasn't working as expected while performing an **Entire Branch** merge ([#68882](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107824070)).
* Enhanced the ALM management feature by adding an option to sync **Smart Commits** ([#58904](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095643142)).
* Fixed an issue with **CI Jobs** **Destructive Sharing Rule** was not deploying to the Salesforce org ([#71183](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110703254)).
* Fixed an issue where user could not disable the **Smart Commits-Sync** option for a repository branch in the **VC repos section** ([#70854](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110258586)).
* Improved the **New Merge** screen by removing the **Validate Deployment** option from the UI if **Vlocity** is selected ([#70993](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110549364)).
* Enhanced the **Credentials** module by adding **SSH Cetificate** option for **Git Authentication** ([#67725](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106632579)).
* Improved **Release label** creation by requiring at least **two revisions** to be selected (internal ticket).
* Fixed an issue where **Classic SF Org URL** with a slash at the end of the URL redirects to the `400` error page, and for a **Lightning SF Org URL** without a slash gives an `OAuth Authentication Failed` error message (internal ticket).
* Fixed an issue with **nCino** where user was getting a `NullPointerException` on **Saving Permissions** using **Bulk Assignment** (internal ticket).
* Fixed an issue with **CI Jobs** where all the scheduled timings were not displayed in the **Preview & Save** page (internal ticket).
* Fixed an issue with **Dataloader** where user was able to upload a 900 MB file despite the limit being 100 MB, causing the process to hang (internal ticket).
* Fixed an issue with **Dataloader** where sever crashed after user performed an **Extract** operation from an SF org which had **Account Object** with 2 million records (internal ticket).

#### 07 May 2023 <a href="#07-may-2023" id="07-may-2023"></a>

**(ARM v22.3.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was getting a validation deployment error while performing release label deployment ([#70400](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109643126)).
* Fixed an issue where **Branching Baseline** was taking longer than expected ([#67814](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777192)).
* Fixed an issue where using the **AutoDraft** functionality in **EZ-Commit** was resulting in a malformed exception in the UI ([#70458](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109706018)).
* Fixed an issue where **Branching baseline** was not picking all components from production ([#70720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110077004)).
* Fixed an issue where **prevalidation merge** failed with empty metadata package even though there were changes in **File Diff** ([#32256](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000049822310)).
* Fixed an issue where entire **ARM** application was down temporarily ([#70658](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110024189)).
* Fixed an issue where **Merge** was **auto-rejected** due to an empty package because the **metadata folder path** not being specified under branch settings ([#69788](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108851098)).
* Fixed an issue where user was using the **Bulk Assignment** feature to assign **Sandbox** permissions on the **Permissions** page but encountered the following error: `Java.lang.NullPointerException` ([#70868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110350003)).
* Fixed an issue where users weren't receiving **SCA reports** by email even though the reports were running ([#70751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110137323)).
* Fixed an issue where while performing new **EZ-Commit**, user edited one line using review artifact option but **Diff** did not capture the same ([#70270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109345141)).
* Fixed an issue where if **CI Jobs** were added in a queue with **Scheduled jobs**, then not all jobs were displayed in the queue (internal ticket).
* Fixed an issue where existing revision file related delta still existed in agent even after uploading to rabitserver (internal ticket).
* Fixed an issue where release label creation was failing when user tried to create package manifest and aborted and refreshed the label for DX repo (internal ticket).
* Fixed an issue where **Super admin user** was getting a blank popup screen while trying to click on the **Register Agent** button from the **Pool Mgmt** screen (internal ticket).

#### 30 April 2023 <a href="#30-april-2023" id="30-april-2023"></a>

**(ARM v22.3.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced the **Version Control** module by adding **SSH Certificate** for Git authentication while creating user credentials ([#67725](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106632579)).
* Fixed an issue where CI Job was picking changes one build but not for the other, and the logs weren't capturing this ([#69164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108123319)).
* Fixed an issue where **Ignore missing visibility settings** function was not working as expected and **Record type visibility** on the profile was not getting deployed using CI Job ([#67654](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106594374)).
* Fixed an issue where user merged a new component using a single revision merge but the merge missed to perform a CodeScan analysis ([#70391](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109502039)).
* Fixed an issue where user was unable to commit the destructive **Email Template** files as part of commit in SFDX format and getting auto failure ([#70351](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109465295)).
* Fixed a UI issue where **OK** button to reject an EZ-Merge was not working ([#70041](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108965683)).
* Fixed an issue where a field was available in the package but still Validation was throwing error that the field was missing ([#69831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108972528)).
* Fixed an issue with **DataLoader** where multiple jobs were not processing parallelly when user loaded a large number of jobs to the queue ([#62559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100372446)).
* Fixed an issue with **nCino** where user created more than 100 jobs with sub-user but was still getting the following error: `No jobs exist to load` ([#69831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108972528)).
* Fixed an issue where **Release Label artifact** was not displaying metadata types in the Destructive changes tab for DX repos, but was working as expected for non-DX repos (internal ticket).
* Fixed an issue where new jobs are getting added to the queue but not getting triggered, and later throwing `NullPointer Exception` (internal ticket).
* Fixed an issue where **Rollback** button was not enabled for the first job if that job is came from a queued list (internal ticket).
* Fixed an issue where **ALM CI Job** and **Release artifact** execution was happening at the same time, and the CI Job build was failing (internal ticket).
* Fixed an issue where an empty pop-up was displayed when user tried to edit the existing CI jobs label for **Sub-User** (internal ticket).
* Fixed an issue where if **Validate only** CI job came from the queue, then direct deployment was executing for that job instead of **validate deployment** (internal ticket).
* Fixed an issue where duplicates revisions were being added to the list while creating the release label when user unselected and reselected the same revisions. (internal ticket).
* Fixed an issue where **Vlocity** revisions were not displaying while user was trying to edit a release label (internal ticket).
* Enhanced the **Release Label** creation page by adding options to the **Vlocity** label type which were only available for Salesforce revisions before (internal ticket).

#### 23 April 2023 <a href="#23-april-2023" id="23-april-2023"></a>

**(ARM v22.3.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **SCA Report** failed to run using **Codescan** plugin with the below Salesforce error: `UNKNOWN_EXCEPTION: An unexpected error occurred`. ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Enhanced the **VC Repos** page by introducing a feature that allows users to **sync external smart commits** ([#58904](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095643142)).
* Updated the UI on the **External pull request** creation page to reflect the **Source** and **Target** fields clearly so users can trace which one is the source and destination branches ([#69772](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108841212)).
* Fixed an issue where duplicate entries were created in different lines during the Merge process and user wasn't able to remove the duplicate field without clearing the layout tag as well ([#68012](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107136001)).
* Fixed an issue where the baseline branch is not displayed during Static Code Analysis job creation if the branch name contains spaces in the Reports module ([#69614](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108583086)).
* Enhanced deployment in ARM by providing a new option **Rollback on error** in merge pre-validation. This checkbox allows users to choose if deployment should proceed with remaining components in case of errors ([#47794](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081201667)).
* Fixed an issue with nCino where CI job filter changes on templates were not taking effect after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue where user created a baseline revision job with the **Automation Sanity** repo and triggered the build but it failed without any error (internal ticket).
* Fixed an issue where user could not fetch the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** as an option (internal ticket).
* Fixed an issue where error `405` in the build and deployment logs didn't display further details in the UI log (internal ticket).
* Fixed a UI bug where dropdown selection in **Reports > CodeCoverage Reports** was not working after refreshing the page (internal ticket).
* Fixed an issue where **Release Label artifact** was not displaying metadata types in the Destructive changes tab for DX repos, but was working as expected for non-DX repos (internal ticket).
* Fixed an issue where user was unable to revert the commit if a previously reverted commit was deleted while in **Conflict** state (internal ticket).

#### 16 April 2023 <a href="#16-april-2023" id="16-april-2023"></a>

**(ARM v22.3.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Enhanced the **SCA report** options by removing the **10,000** limit for exporting issues using **CodeScan** ([#48644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082753293)).
* Enhanced **Vlocity CI jobs** by allowing **Local Compilation** for **Omniscript** and **Flexcard** objects ([#55641](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090230148) and [#50301](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084720103)).
* Fixed an issue where user was unable to use the **Redeploy/Promote** option after ten iterations of an existing **Deployment** label ([#69084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000108041156)).
* Fixed an issue where user was trying to commit **System Permissions** which were enabled in Salesforce org, but while performing **EZ-Commit**, file **Diff** is not getting generated and the **system permissions** are not getting committed ([#67826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777838)).
* Fixed an issue where **ALM label** merge option was not working in **EZ-Merge** feature. This happened only when the **ALM Label** contained **`/`** in it ([#67818](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106777588)).
* Fixed an issue where **EZ-Merge** was failing with `NullPointerException` ([#67502](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106282031)).
* Fixed a recurring issue of ARM overwriting the **Salesforce Org - Default Apex Test Class Configuration** by adding a checkbox **`Do you want us to update the test classes?`** ([#65565](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104611176)).
* Fixed an issue where **Revert** commits were failing without any error messages ([#68771](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107671065)).
* Fixed an issue where user created a **Release label** with multiple commit revisions, each with dependency components, but the revisions were not displaying in the right order in UI ([#68939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107912007)).
* Fixed a UI bug where when user unchecked **Validate deployment** option in **EZ-Merge**, the **Run destructive changes** checkbox was hidden ([#68750](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000107699066)).
* Fixed an issue where when user had files in conflicted state, selecting the **ALL** checkbox was not working and user had to click on each file to resolve conflicts ([#65680](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104849001)).
* Fixed an issue where the **NPM repository Access Key** wasn't saving after clicking **Save**, causing the **Local Compilation** to fail (internal ticket).
* Fixed an issue where comments lines were not executed in **Metadata** when there were spaces in the comment line in merge flow (internal ticket).
* Fixed an issue where an empty popup screen is displayed while resolving conflicts in case of malformed file (internal ticket).
* Fixed an issue where improper validation message is displayed after clicking on **Resolve Duplicates** without selecting any files to resolve (internal ticket).
* Fixed an issue where SSO user's org was not deleted from the **Security-Context XML** (internal ticket).
* Fixed an issue where the **API Token** status was marked as **Never Accessed**, despite the API being in use already (internal ticket).

#### 09 April 2023 <a href="#09-april-2023" id="09-april-2023"></a>

**(ARM v22.3.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **validation jobs** on **Pull Requests** weren't getting triggered ([#67538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106410313), [#67494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106382311), and [#67448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106353830)).
* Fixed an issue where Salesforce components were showing under the **Apex Test Success** tab in the **Deployment** module, which is not expected behavior ([#67537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253424)).
* Enhanced the **Branching Baseline** feature by allowing admin to define default baseline branches, making it easier for developers to choose the default branch for each project ([#63571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102024066)).
* Fixed an issue where user was unable to register a branch even though **Test Connection** was successful ([#67023](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105968682)).
* Fixed an issue where ARM wasn't fetching the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** option ([#67503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106378846)).
* Fixed an issue where **SCA Report** failed to run using **Codescan** plugin with the following Salesforce error: `An unexpected error occurred. Please include this ErrorId if you contact support: 384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Fixed an issue where triggered **CI jobs** were either failing due to an error **No Such File or Directory found**, or getting aborted automatically after some time and logs weren't printing at the back end ([#67549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253579), [#66910](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106035058), [#67724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106597223), [#67720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106570720), [#66881](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936162), and [#67667](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604150)).
* Fixed an issue where triggered **CI jobs** were taking too long to build, and also slowing down ARM altogether ([#66846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105989569)).
* Fixed an issue where if the file name contained spaces, **Commit Validation** via **VS Code** plugin was unable to detect the file ([#63518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101868754)).
* Fixed an issue where **Search & Substitute** was not updating the value for a **custom label** in the SF org ([#66809](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936001)).
* Fixed an issue where there was a discrepancy between the changes captured in the ARM **Diff** and the repos in **BitBucket** ([#60596](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097396243)).
* Fixed an issue where the SF org **URL** is not displaying the updated one under **Profile** ([#67718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106581101)).
* Fixed an issue with **nCino** where CI job filter changes on templates are not reflecting after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue with **Dataloader Pro** where user tried to migrate **Account Object Data** with **Attachments Object**, but the logs verify that there is a **Null Pointer Exception**. (internal ticket).
* Improved **nCino** by adding additional loggers for **Branching baseline** for user to view the status in the UI (internal ticket).
* Fixed an issue where user was unable to filter while trying to select a job which had spaces in the job name (internal ticket).

#### 02 April 2023 <a href="#02-april-2023" id="02-april-2023"></a>

**(ARM v22.3.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Custom Metadata** type access changes were not detected in version control **Diff**. There was no diff generated even there were changes in metadata access ([#59458](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096457374)).
* Fixed an issue where user performed a **CI job deployment** that had 8 destructive change items in the **merge PR**, but ARM is displaying only 2 destructive changes ([#66587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105697158)).
* Fixed an issue where **Git backup job** was failing due to unsupported metadata ([#66536](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105610003)).
* Fixed an issue where scheduled CI jobs were getting queued or not getting triggered as per schedule ([#57749](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093607144)).
* Fixed an issue where **Quick action** was not picked for destructive changes ([#65058](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104091725)).
* Fixed an issue where while running the scan from ARM for the version control branches are failing because **.java** files were present in the current repository ([#63234](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101513612)).
* Fixed an issue where user using **non-SFDX** repo with **Custom API** enabled failed to pick the changes in the CI job ([#64497](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103321171)).
* Fixed an issue where **Release label** displayed **commit revisions** older than 30 days even when the **No. of days** filter was set as **30** ([#63845](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102526769)).
* Fixed an issue where a user had trouble creating **artifact** for a **release label** ([#65557](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104667180)).
* Fixed an issue where there are **Vlocity** components in **Merge Validation**, and the validation deployment should bypass and process the merge; instead it is **Auto-rejecting** as criteria were not met ([#65625](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104812001)).
* Fixed an issue with **Dataloader** where a job completes with **No records** status whenever attachment and content version are selected as child objects in the parent cccount object ([#66655](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105749754)).
* Fixed an issue with **nCino** where CI job build status is displayed as **Completed** for a failed job ([#64479](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103318168)).
* Fixed an issue with **nCino** where attachements to `nFORMS__Form_Template__c` failed to get deployed ([#65242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104379896)).
* Fixed an issue where user was unable to initiate **static code analysis** on a Salesforce Org ([#51559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085951433)).
* Fixed an issue with **New EZ- Commit** where while using **Custom YAML** file the page was taking much longer to load than usual ([#65742](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104883025)).
* Fixed an issue where **Merge** was happening on incorrect files ([#64485](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103318553)).
* Fixed an issue where for DX repo, **Custom field** destructive **Deployment** was failing with the error `Package generation without a valid package directory cannot be processed` (internal ticket).
* Fixed an issue from the **VS Code** where **Static Code Analysis** report was not getting executed on the selected files and report generated (internal ticket).
* Fixed an issue where **Release Label** creation with **SVN Repo** was not successful, and throwing the following errors (internal ticket):
  * `Supplied AttributeValue is empty, must contain exactly one of the supported datatypes (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ValidationException; Request ID: a59c77cb-67ad-4a58-80b4-364feb5a4d6c; Proxy: null)`
  * `No Version Control Mappings found for Repo: {} and Branch: {}. Please update it in My Profile`
* Fixed an issue where **Merge** was not **Auto-rejected** after UI logs displayed `Mock deployment is failed, so auto rejecting the merge` (internal ticket).
* Fixed an issue where **Revision** in **Vlocity** release label was not getting selected after you clicked save (internal ticket).
* Fixed an issue with **nCino** where user was getting an exception while creating a CI job, and user was selecting the same **VC Repo**/**Branch** for multiple times (internal ticket).

#### 26 March 2023 <a href="#26-march-2023" id="26-march-2023"></a>

**(ARM v22.3.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Quick action** was not picked for destructive changes ([#65058](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104091725)).
* Fixed an issue where **CI job** deployment was failing due to the following error:\
  `Error: Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field (line 0, column 0)` ([#60914](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097801217) and [#65855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105051054)).
* Fixed an issue where **WebStoreTemplates** object was not available for deployment ([#65854](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104921177)).
* Fixed an issue where **Merge Request XML** file was conflicting with an error `No conflict data found for this block` ([#65164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104169938)).
* Fixed an issue where **Release label** failed while creating the artifact ([#64491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103297164)).
* Fixed an issue where **Prevalidation EZ-Commit** shows that **Diff** does not exist even when there are changes. If user tries multiple times, then Diff is displayed sometimes ([#64612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103417610)).
* Fixed an issue where user was unable to merge the code from one branch to another branch. ([#65570](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104676278)).
* Fixed an issue where **Ignore Missing Visibility** settings not working on **EZ-Merge** validation ([#65162](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104186080)).
* Fixed an issue where user was loading multiple **DataLoader** jobs but it was not processing parallelly ([#62559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100372446)).
* Fixed a UI bug in **nCino** where the header in **template details** section was missing in **Feature Deployment** (internal ticket).
* Fixed an issue with **nCino** where **Deployment Logs** were not displayed when the **CI Job** failed (internal ticket).

#### 19 March 2023 <a href="#19-march-2023" id="19-march-2023"></a>

**(ARM v22.3.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where CI job deployments were failing with the error, `Error 405 Only POST allowed` ([#64228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103003760)).
* Fixed an issue where multiple deployment requests were being generated while performing **Org Sync** if the user selected all components instead of a few ([#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where **Rollback API** threw a **200** response but the Rollback immediately failed in the ARM UI ([#65146](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104115380)).
* Fixed an issue where SCA report Failed to run using the **Codescan Plugin** with the following Salesforce error `384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151)).
* Fixed an issue where users were having trouble logging in to ARM due to an error `Session Invalid` ([#64965](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103959064), [#65052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104090509), and [#64969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104016027)).
* Fixed an issue where after upgrading to ARM version **22.3** user was unable to approve **EZ-Commits** that were pending approval in the **22.2** ([#64094](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102809037)).
* Fixed an issue where **Auto-draft** was taking much longer than expected to retrieve the metadata in **EZ-Commit** ([#65109](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104022403), [#65007](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104076001), [#64950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103943001), [#64510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103338015), [#64645](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103513158), [#64161](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102852098), and [#64523](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103361369)).
* Fixed an issue where user was trying to resolve a conflict in EZ-Merge but was getting a message on the UI that there are no conflicts ([#64185](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102875003)).
* Fixed an issue where **Branching Baseline** job does not delete files in **static resources sub directories** even though the user has selected the **Delete existing metadata and commit new changes** option ([#64150](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102831529)).
* Fixed an issue where user was unable to retrieve **MutingPermissionSet** using the **SFDX** repository ([#64141](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102573686)).
* Fixed an issue where the **Release Label** failed while creating the artifact ([#64491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000103297164)).
* Fixed an issue where **Sharing Rule Set** metadata type was found in the **Deployment** module but not in the **Version Control** module ([#65060](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104102165)).
* Fixed an issue where the user performed a merge and approved both level 1 and level 2 reviews but was unable to approve the merge ([#65091](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104040481)).
* Fixed an issue where errors were occuring while performing **Delete Org** (internal ticket).
* Fixed an issue where for **Build only** job source from VC with DX repo, if **Master Details Object Change** is included in the build, we're getting **No Modifications** even if changes exist (internal ticket).

#### 12 March 2023 <a href="#12-march-2023" id="12-march-2023"></a>

**(ARM v22.3.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Static Code Anaysis** was failing due to missing property tag in **Apex PMD** rules file, but the UI log wasn't displaying this error ([#63554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101980029)).
* Fixed an issue where when there was no results generated, the report displayed an error that there are zero metrics instead of displaying the results as zero in all the places when there is no change ([#63272](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101591692)).
* Fixed an issue where user was unable to deploy a CI job with the **RelationshipGraphDefinition** components ([#64145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102836208)).
* Fixed an issue where **Validate** deployment was displayed as **failed** in UI and the database, but was successful as per the logs ([#63868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102596005)).
* Fixed an issue with **Review Artifact** where similar custom fields from different objects were not populating correctly and switching to other fields ([#63676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102181836)).
* Fixed an issue where multiple fields of the respective custom objects were getting selected parallelly while performing **edit** or **save** or **exit** operations on the **Review Artifact** screen (internal ticket).
* Enhanced ARM by adding an option for **multiple ARM instances** to share a **single database cluster** (internal ticket).

#### 05 March 2023 <a href="#05-march-2023" id="05-march-2023"></a>

**(ARM v22.3.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where ARM was displaying incorrect installation settings and package version information in the deployment log while installing the package version from a CI job ([#63544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101947159)).
* Fixed an issue where user chose **Exclude Metadata Type** for a particular metadata type during a **CI Job**, but it was still deployed ([#62966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101046005)).
* Fixed an issue where user was unable to perform **Destructive Commit** with **PermissionSetGroups** metadata type ([#63172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101463001)).
* Fixed an issue where users weren't receiving emails after setting up **Mail Settings** ([#55070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089394047)).
* Fixed an issue where there was a discrepancy between **EZ-Commit** and **Commit templates** while retrieving **Email Template** metadata members ([#61696](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099121314)).
* Fixed an issue where **Merge Labels** were taking much longer than expected ([#62625](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100474287)).
* Fixed an issue where user tried to commit the changes without validation and UI displayed an error `Another commit is in progress` ([#61930](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099562127)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed a UI bug where there was a discrepancy in the timestamp displayed for a commit in the **Commits History** page ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Fixed an issue where **Merge** was not auto-rejected when validation criteria was not met ([#62287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100008338)).
* Enhanced **nCino** by adding an option to specify **Baseline Revision** in **Continuous Integration** for **Version Control** to perform feature deployments ([#43642](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073759034) and [#44506](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074950579)).
* Enhanced **nCino** by allowing users to deploy nCino **CI build** to multiple target sandboxes ([#41763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070674305)).
* Fixed a UI bug where incorrect notification was displayed in certain components pages when template was created using one org and was used by another org (internal ticket).
* Fixed an issue where **Baseline Managed Package Changes** option was not displayed on the UI when navigating from **Package xml** to select manually (internal ticket).
* Fixed an issue where there was a discrepancy between the **Attachments Records Success/Failure Count** and the **Retrieved Count** when **BULK API** was enabled for **Deployment** (internal ticket).

#### 26 February 2023 <a href="#26-february-2023" id="26-february-2023"></a>

**(ARM v22.3.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a UI bug in **Profile Manager** where **User Permissions** differences are shown in the report but not in the UI ([#61672](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099032670)).
* Enhanced the **Release Label** creation by increasing the range of retrievable commit history ([#61714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099129934)).
* Fixed an issue where user was unable to use **Release Labels** to perform **Deployment**, and it failed while trying to **Create Artifact** ([#59429](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096450140)).
* Fixed an issue where users with non-admin access were unable to register branches in **EZ-Commit** since upgrading to version 22.3 ([#62723](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100650673), [#62949](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101016055), [#62979](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010456), and [#62969](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101010302)).
* Fixed an issue where **Release Artifact** execution was failing when **rabit home** did not exist with an external agent (internal ticket).
* Fixed a UI bug on the **Profile** screen where the expand option for the **My Projects** and **My Roles** sections was not working (internal ticket).
* Fixed an issue where triggering **Data Retention** for **Audit Tables** was throwing the following error: `Unable to execute HTTP request: Read timed out` (internal ticket).
* Fixed an issue where extra characters are seen in the **Fetch Commit History** results while creating a **Release Label** with **Vlocity** label type (internal ticket).
* Fixed an issue where user was unable to delete Apex test class on the SF Org Management page (internal ticket).
* Enhanced **nCino** by introducing **New Spreads Schedule** tile in the **Feature Creation** screen (internal ticket).
* Fixed an issue where if the fields did not load for **Applied Mappings** during deployment, no error was thrown by the application (internal ticket).

#### 19 February 2023 <a href="#19-february-2023" id="19-february-2023"></a>

**(ARM v22.3.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was deploying single revision deployment with only report folder but sub-reports were also getting fetched, and the deployment was failing due to field dependency error ([#61403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098537015)).
* Fixed an issue where after deployment with single revision merge, user permission appears to be removed in target org but in the Salesforce target org the user permission is not removed, and an incorrect layout is displayed in UI ([#60531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097360001)).
* Fixed an issue where user performed a pre-validation commit and each process like file diff, validate deploy happened thrice as per the logs ([#61079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097987087)).
* Fixed an issue where user was unable to select master branch as the parent branch while creating a new branch in **EZ-Commit** ([#56188](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091240174)).
* Fixed an issue where user was customer trying to register a **Salesforce Org** with **Custom URL** but it was failing with an error ([#62192](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099509581)).
* Fixed an issue where user was unable to remove **Revisions**/**Commit Labels** from a **Release label** ([#59152](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096005470) and [#61578](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098950203)).
* Fixed an issue where user was creating credentials for **JIRA** in ARM using **JIRA Token** and but application wasn't allowing more than 150 characters while JIRA Token should allow up to 192 characters ([#61791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248821) and [#61970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099521745)).
* Fixed an issue where user user uploaded a **YAML file** to retrieve the **Vlocity components** but ALL metadata types were retrieved and displayed ([#61181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248158)).
* Fixed an issue where the same merge could be approved and rejected by different users simultaneously ([#60859](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097787146)).
* Fixed an issue where branch creation was faileing for sub-users in the **EZ-Commit** screen for **Non-DX Repo** (internal ticket).
* Fixed an issue where **Null Pointer** was seen in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where all credentials were listed twice in the **Credentials** dropdown in **Create Branch** in **EZ-Commit** flow (internal ticket).
* Fixed an issue where **branch creation** was failing for sub-users in **VC repos** when the credential scope was private while Admin credentials were fetched (internal ticket).
* Fixed an issue where user was unable to delete the **Apex Test class** under the SF org Apex **default config** (internal ticket).
* Fixed an issue where the **Add manually** checkbox under Apex class config was selected by default (internal ticket).
* Fixed an issue with nCino where user created a feature Deployment for **Credit memo** template with attachments, but **Attachments Objects Data** was not fetched, and the deployment failed with the following error: `Data file not fetched for object: Attachment` (internal ticket).
* Fixed an issue with nCino where **Standard Features** were not loaded in the **Feature Management** page (internal ticket).

#### 12 February 2023 <a href="#12-february-2023" id="12-february-2023"></a>

**(ARM v22.3.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was unable to download success/failure reports in **Single Dataloader** ([#61551](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098913200)).
* Fixed an issue where when multiple **CI Jobs** are triggered, jobs are moved into the queue as expected, but new jobs are not starting automatically getting processed once the existing jobs is cleared from the **CI Job results** page ([#59082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096042290)).
* Fixed an issue where **Dependency** order defined in **json** file was being changed on every commit but it was not supposed to ([#57731](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556797)).
* Fixed an issue where **Create Artifact** was not working as expected while using **Release Label** ([#61607](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098932152)).
* Fixed an issue where user was performing an **EZ-Commit** with **Review Artifact** option and download the .zip file to make some changes, but was unable to upload it afterwards ([#61751](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099248378)).
* Fixed an issue where meta.xml file was not deleted from the repository after committing the destructive changes ([#61736](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099207347)).
* Fixed an issue where **File Diff** was empty in case of modified **Uploaded** via **Review Artifact** in **PV Commit Flow** (internal ticket).
* Fixed an issue where **Review Artifact Tree** was not responding after uploading the modified file in **Commit Flow** (internal ticket).
* Fixed an issue where **User Permissions** and **Ip Ranges** are completly removed from the branch after commiting the **Permission Sets** and **Profiles** (internal ticket).
* Fixed an issue where **Super Admin** was getting an error while trying to activate newly signed up users (internal ticket).

#### 05 February 2023 <a href="#05-february-2023" id="05-february-2023"></a>

**(ARM v22.3.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where SFDX module creation log shows that deployment is successful but the module creation had failed ([#57318](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092768029)).
* Fixed an issue with **Backup from Org CI Jobs** where **PermissionSet User Permissions** were being deleted ([#59674](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096685144)).
* Fixed an issue where **Org to Org Deployment** for **Profiles** including **Deploy Profile Access Settings for selected components only** was not working as expected ([#60559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097375154)).
* Fixed an issue where **Post Destruct** fields were also added to **Pre Destruct** despite the user setting it to post ([#61162](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098248005)).
* Fixed an issue where user set the **Max depth** value as '0' under **Vlocity Configuration Settings** but it was retrieving all level dependancy components ([#57501](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093212471)).
* Fixed an issue with DataLoader where the **Credit Memo Template** migration was not deploying after user upgraded their instance ([#57676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093470003)).
* Fixed an issue where user selected **Custom Metadata** members (records), but **EZ-Commit** was failing to generate **File Diff** with `Null` error ([#59709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096706005)).
* Fixed an issue where **Merge** was taking longer than usual, and then failing with `Null Exception` ([#60757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097574427)).
* Fixed an issue where **EZ-Commits** and **EZ-Merges** were taking much longer than usual ([#58098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094302292)).

#### 29 January 2023 <a href="#29-january-2023" id="29-january-2023"></a>

**(ARM v22.3.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment was failing with the following error when user was deploying **Permissionset** with a user-permission **Manage Public Documents**: `Permission Manage Public Documents depends on permission(s): Create Document, Delete Document, Edit Document, Read Document` ([#60597](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097399881)).
* Fixed an issue where CI jobs were failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#59050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095999076)).
* Fixed an issue where **Reports** deployment validation failed in **EZ-Merge** but was successful in **EZ-Commit** and **Deployment** modules ([#57714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093587003)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Fixed an issue where user initiated the prevalidation commit by enabling the destructive type but the deployment failed with an error `null` at **Diff** ([#59919](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096907001)).
* Fixed an issue where **Validate Deploy** failed in **QuickMerge** and displayed the following message: `This folder unique name already exists for this folder type or has been previously used. Please choose a different name` (internal ticket).
* Fixed an issue where CI job wasn't considering the metadata changes, so the destructive changes were not being prepared or displayed on the build. (internal ticket).

#### 22 January 2022 <a href="#22-january-2022" id="22-january-2022"></a>

**(ARM v22.3.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user changed the permissions to **list view** from **visible to all users** to **visible only for me** while using the previous commit label, it is added under the **Deleted** tab ([#59359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096219627)).
* Fixed an issue where commit was running for longer and remained **in-progress** and **validation check log** is also in progress ([#59199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096003630)).
* Fixed an issue where commits with SFDX metadata structure are **failing** in metadata **retrieval stage** ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed an issue where user couldn't create a managed package with the selected ancestor ([#59044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095985421)).
* Fixed an issue where **CI Job** was occasionally failing with the error `BUILD FAILED` ([#57647](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093370172)).
* Fixed an issue where CI job was taking the last modified user name if trigger through API instated of taking API token user ([#55438](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089958034)).
* Salesforce **API version 57** (Beta support) is upgraded. The label is modified throughout ARM application including DataLoader and nCino (internal ticket).
* Fixed an issue where nCino CI job was stuck in **Build Success** status for more than a week ([#59040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095982206)).
* Fixed an issue where user was trying to deploy RBC (nCino Screens) and the deployment was failing for some of the objects, but there were no error messages shown on the UI ([#58044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094164003)).
* Fixed an issue where user was using SSH credential in AutoRABIT but it was throwing the following error: `Invalid Private Key` ([#59244](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096134293)).
* Fixed an issue where user has created a Commit label but it was not available while trying to perform an **EZ-Merge** ([#55176](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089550097)).
* Fixed an issue where user was not getting file Diff to commit the previously validated commit label and getting an error in the Diff ([#59114](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096048883)).
* Fixed an issue where user was getting an error while trying to create a new branch in GitHub ([#59193](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096138920)). For more information, click [here](https://knowledgebase.autorabit.com/docs/faqs-version-control?highlight=$%20ssh-keygen%20-t%20rsa%20-b%204096%20-C#why-am-i-getting-an-error-while-trying-to-register-github-repository-with-ssh).
* Fixed an issue where user could not create an **xml package** for deployment because artifact creation and package manifest preparation were failing with an `invalid credentials` error ([#59402](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096425001)).
* Fixed an issue where user was trying to perform single revision merge but validation deployment was failing with the following error `Metadata package is empty` ([#59028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095867179)).
* Fixed an issue where when there are special characters in **Layout metadata** then the user was not able to add it manually in **Skip Members** section ([#58998](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095876003)).
* Fixed an issue where user wanted to choose commit revision in a release label based on its comment but if the comment was not in text, it was not completely visible in the UI ([#59014](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095898340)).
* Fixed a UI bug where an incorrect validation message was seen while adding **Skip Members** manually (internal ticket).
* Fixed an issue where the selected tab checkbox in the **metadata components** page in the EZ-Commit was not functioning as expected (internal ticket).
* Fixed an issue where the **EZ-Commit** validation screen was displaying incorrect notification when name of the template was empty (internal ticket).

#### 15 January 2022 <a href="#15-january-2022" id="15-january-2022"></a>

**(ARM v22.3.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556)).
* Fixed an issue with user received 6 notifications for a failed **CI Job** instead of 1 ([#58436](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095199003)).
* Fixed an issue where user was trying to register branches to AutoRABIT through GitHub, but was getting the following error: `Lower Region` ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed a recurring issue where **Commits** and **Merges** were slowing down at a particular step, and **EZ-Merge** was failing with an error at commit phase ([#51268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085726862)).
* Fixed an issue where while performing destructive changes in **EZ-Commit**, it was creating **package.xml** in root path folder in **SFDX** structure ([#57868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093790001)).
* Fixed a UI bug on **CI List** and **CI Results** pages where when pagination was changed, the first 25 records were repeated (internal ticket).
* Fixed an UI bug where the **LastUsedDate** column was not displayed in the **Branch Table** (internal ticket).

#### 8 January 2022 <a href="#8-january-2022" id="8-january-2022"></a>

**(ARM v22.3.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189)).
* Fixed a build bug where **CI Job Build** was failing during package preparation **step 5** failing while commiting **DecisionMatrixDefinition** and throwing an error ([#58376](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095049142)).
* Fixed an issue with **Branching Baseline** where the developers were migrating the changes from dev branch to INT, but **Diff** was showing 100% addition which is incorrect\
  ([#58478](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095251543)).
* Fixed an issue where generating **Diff** for a **Commit Label** was taking much longer than expected ([#55220](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591780)).
* Fixed an issue where **Code coverage** job was running **4 hours** earlier than scheduled every time services were restarted ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed an issue where **SFDX scratch org** was failing during data deployment but without any errors on UI, and the logs did not capture the failure either ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58244](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000094983001), [#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556), and [#58438](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095210005)).
* Fixed an issue where **CheckMarx** is executed successfully, but when trying to open the file user is the following error popup: `Result file not exists` (internal ticket).
* Fixed an issue where **ActionCall** and **Decision Nodes** were not shown in the **Duplicate Resolving** screen (internal ticket).

#### 1 January 2022 <a href="#1-january-2022" id="1-january-2022"></a>

**(ARM v22.3.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was unable to create **Environment Provisioning** templates for multiple component types ([#57898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093797903)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).
* Fixed an issue where AutoRABIT **SSH credentials** were failing with an error `Auth failed` while trying to connect with **AWS CodeCommit** ([#53694](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087714369)).
* Fixed an issue where **EZ-Commit Diff** was taking approximately 4 hours while **Refactoring CustomField**, which is much longer than expected ([#56650](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091636348)).
* Fixed an issue where **ExternalCredential** metadata type was not getting excluded even when user added it in the **excluded lists** in **CI Configuration** (internal ticket).
* Fixed an issue where after triggering **Branching baseline**, standard value set metadata type was getting displayed under the **deleted components** through **Autodraft** for **Non-DX repo** (internal ticket).
* Fixed an issue where **Destructive Components** are not seen in case of **PV-DX-Destructive Merge** for **Report** metadata type. Instead, it displaying a message: `Package is empty` (internal ticket).
* Fixed an issue where **Deployment** was failing with certain **Permission set metadatatypes** that were not selected (internal ticket).

#### 25 December 2022 <a href="#25-december-2022" id="25-december-2022"></a>

**(ARM v22.3.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where non-admin users were unable to select **Branch Type** while trying to create a **new branch** from **New EZ-Commit Branch** ([#57732](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556923)).
* Fixed an issue where **CI jobs** are failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#57371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880162)).
* Fixed an issue where user was trying to deploy only the **Documents** from the branch to Org, but deployment failed and **Asynch ID** is not generating ([#57263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092661381)).
* Fixed an issue where user was trying to deploy **login hours**. First they merged it to target branch, then once CI job triggers login hours are not getting deployed to target org ([#57359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880015)).
* Fixed multiple issues where user was having trouble creating **new package version** from **previous ancestor** version ([#55707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090251366)).
* Fixed an issue where **Merge** is **failing** with the following error: `failed to push some refs to 'https://github.com/salesforce-align/SFDX.git'` ([#55939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090999346)).
* Fixed an issue where the **Standard Field Account.name** is displayed in the deleted components list ([#57396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092927781)).
* Fixed an issue where the **prevalidation commit** failed at **delta** stage ([#55763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090435979)).
* Fixed an issue where user was unable to create **commit label** for the same repository second time, and branches were not displayed (internal ticket).

#### 18 December 2022 <a href="#18-december-2022" id="18-december-2022"></a>

**(ARM v22.3.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DataLoader Pro** where jobs executed in the last 6 months were not showing in the database process table and in the **Reports** module ([#53980](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087981132)).
* Fixed an issue with **Deploy SFDX Source With ALM Mapping** where CI job with ALM Mapping was not working as expected for Team which is not default ([#55995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091129007)).
* Fixed an issue where **Profile Diff** is working as expected for **Selective Deployment**, but not while using the same profile in the profile manager ([#52868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087005140)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189), [#55754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090487029)).
* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).
