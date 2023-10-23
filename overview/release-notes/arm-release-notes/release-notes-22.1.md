# Release Notes 22.1

**March 2022 - Version 22.1 - New Features, Enhancements, Improvements and Changelogs**

**Date of release:** _20 March 2022_\
**Article last updated:** _23 October 2022_\


### New features <a href="#new-features" id="new-features"></a>

#### 1. Squash and merge <a href="#1-squash-and-merge" id="1-squash-and-merge"></a>

We have added the **Squash and Merge** feature in this release. Sometimes, when merging a long list of changes from a development branch into the master, it's helpful to squash those commits into one change for ease of review and declutter the repo's commit history. AutoRABIT offers an option to squash all commits in a merge request into one commit after the merge is approved and completed.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/squash%20and%20merge.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/squash-and-merge.md)

#### 2. SFDX- Import packages <a href="#2-sfdx-import-packages" id="2-sfdx-import-packages"></a>

**Packages**

The users could previously build a new package (unlocked or managed) and update the package's version in Salesforce DX. With this release, you may now import packages and update the version of packages created outside of AutoRABIT.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/import%20packages.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/import-an-unlocked-managed-package.md)

**Dev Hub management**

With this update, users will see all of the packages in their dev hub in the record view. You may expand each package to show the package's versions in order and package data such as version name, version number, ancestor version, ancestor dependencies, etc.

![Dev hub.gif](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Dev%20hub.gif)

[**Read more →**](../../../product-guides/arm/registering-a-devhub.md)

#### 3. Step-based rollback <a href="#3-stepbased-rollback" id="3-stepbased-rollback"></a>

The option to list the API-supported and unsupported API components is added to the CI job/deployment rollback. If such components may be deployed to the target environment but do not have API support to delete them, ARM will display them individually as unsupported API types. Take, for example, **RecordType**.

The **RecordType** component may be deployed to the target environment, but it cannot be removed; instead, we need to connect to the target Salesforce environment to deactivate the component.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/step%20based%20rollback.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/ci-job-rollback.md)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Checkmarx upgrade to v9.4.1 <a href="#1-checkmarx-upgrade-to-v941" id="1-checkmarx-upgrade-to-v941"></a>

Checkmarx has been updated to version **9.4.1**. Earlier, Checkmarx used a username/password-based authentication method. Now, the user will be able to use token-based authentication with the Checkmarx upgrade.

#### 2. Export all users <a href="#2-export-all-users" id="2-export-all-users"></a>

The **Export All Users** feature allows the org admins to export a CSV file of all the users currently in their account. We now have added the following fields to the existing CSV file:

* CreatedDate
* CreatedByName
* DeativatedDate
* LastLoginDate
* DeactivatedByName
* LastModifiedDate
*   LastModifiedByName.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/export%20all%20users.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings/users-roles-and-permissions.md)

#### 3. Pull request support for Azure cloud repositories <a href="#3-pull-request-support-for-azure-cloud-repositories" id="3-pull-request-support-for-azure-cloud-repositories"></a>

We have extended the support of having the pull request support in the CI Job for the Azure repository. This feature was previously available for Github cloud/Enterprise and Bitbucket cloud/Enterprise; however, we've added support for Azure cloud repositories (DX and non-DX repositories) with this release.

#### 4. Merge/commit approval eligibility <a href="#4-mergecommit-approval-eligibility" id="4-mergecommit-approval-eligibility"></a>

If you want to make sure one or more people approve every commit or merge, you can enforce this workflow by using merge/commit approvals. These approvals allow you to set the number of necessary approvals to approve every commit/ merge in a project.

The org admins' eligibility level has been enhanced with the ARM 22.1 version. If you're an administrator, you will have the privilege to approve self-merge even if the criteria to self-approve a merge is set to FALSE. This permission will be denied to all members of your team except the org admin. To put it another way, no criteria can restrict an org administrator from approving any EZ-commit/ EZ-Merge.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/commit-merge%20approval.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/merge-approvals.md)

#### 5. CodeScan additional metadata support <a href="#5-codescan-additional-metadata-support" id="5-codescan-additional-metadata-support"></a>

We have enhanced the scope for analysis of what CodeScan does by adding support for additional metadata and rules. For our ARM users who want to incorporate the SCA tool into their subscriptions, CodeScan would be their first choice as it now supports more robust integrations.

Below is the list of CodeScan supported metadata types:

|                                   |                         |                         |
| --------------------------------- | ----------------------- | ----------------------- |
| Apex Triggers                     | Apex Classes            | Aura Definition Bundles |
| Lightning Component Bundles (LWC) | Visualforce Pages       | Custom Object           |
| Settings                          | Flows                   | Workflows               |
| Profiles                          | Sharing Rules           | Sharing Criteria Rules  |
| Sharing Owner Rules               | Sharing Territory Rules | Permission Sets         |

#### 6. SFDX CLI update <a href="#6-sfdx-cli-update" id="6-sfdx-cli-update"></a>

The SFDX CLI has been upgraded to the latest stable **7.134** version.

Key characteristics to look for:

* Single deployment request for constructive and destructive changes
* Quick deploy and rollbacks work for both constructive and destructive changes
* Package preparation has been improved.

***

### Improvements <a href="#improvements" id="improvements"></a>

* The jquery-UI version has been upgraded to **v1.13.0** to fix security issues. Upgrading to the most recent version of jquery makes our application more secure and potentially faster in script execution and loading.
* Minor performance, bug fixes, and security improvements can also be observed in the ARM portal.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 21 May 2023 <a href="#21-may-2023" id="21-may-2023"></a>

**(ARM v22.1.48)**\
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

#### 09 April 2023 <a href="#09-april-2023" id="09-april-2023"></a>

**(ARM v22.1.46)**\
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

#### 25 December 2022 <a href="#25-december-2022" id="25-december-2022"></a>

**(ARM v22.1.38)**\
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

#### 11 December 2022 <a href="#11-december-2022" id="11-december-2022"></a>

**(ARM v22.1.37)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where multiple metadata types where not able to retrieve ([#56668](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091694003)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was creating the **feature template** for some of the **nCino** objects but it was taking too long to **retrieve** the objects from **Source Org** ([#53915](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087934809)).
* Enhanced **nCino** to:
  * Modify **notification** messages for null checks on request parameters (internal ticket).
  * Display only **nCino** revisions for Version Control in nCino feature **deployment** (internal ticket).

#### 04 December 2022 <a href="#04-december-2022" id="04-december-2022"></a>

**(ARM v22.1.36)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Flexi pages** were not picked up in a **CI Job** even after the commit with same set of metadata was excluded by user ([#54518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088461033)).
* Fixed an issue where **Abort** function to stop **Provar** jobs was not working as expected ([#55511](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090032787)).
* Fixed an issue where production backup **CI Job** was not picking all the changes, and when user modified the job configuration and retriggered the job, the application was throwing the following error `java.lang.NullPointerException: null` ([#55213](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591408)).
* Fixed an issue where all **Slack Notifications** were selected by default and user was unable to unselect all at once ([#55817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090727146)).
* Fixed an issue where **SFI components** were not being fetched both in **Commit** and **Deployment** modules ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue with **DataLoader Pro** where user selected a field as **External ID** in a job and saved it, but the saved entry was lost and user was unable to map it ([#55011](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089299148)).
* Fixed an issue where **Deployment validation** in **Prevalidation Commit** fails because profile validation automatically picks **User Permissions** even though **Remove User Permissions** option is selected ([#54941](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088985107)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where **Release Label Merge** was failing and throwing the following error: `fatal: bad revision` ([#55000](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089278434)).
* Fixed an issue with **EZ-Commit** where user was unable to upload a **Custom YAML** file ([#55826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090770005)).
* Fixed an issue where the **Vlocity Component** option under **Fetch Changes** is not populating for sub-users with roles that have all permissions and access ([#54962](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089032619)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was performing a merge operation and validating the package on the **target org** but the validation was failing with multiple errors ([#55541](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090145025)).

#### 27 November 2022 <a href="#27-november-2022" id="27-november-2022"></a>

**(ARM v22.1.35)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was trying to migrate **Products**, **Pricebooks**, and its entries but the **Deploy** was failing for **Pricebook** and throwing the following error: `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY: insufficient access rights on cross-reference id:--` ([#55263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089652641)).
* Fixed an issue with **nCino** where user was trying to create a custom feature template including **product objects** as well as **product line** but the deployment was failing with the following error: `Required fields are missing: [LLC_BI_Product_Line_c]` ([#51209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085641324)).
* Fixed an issue with **nCino** where **CI Job** was stuck in **Build Success** status ([#53605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087564091)).
* Fixed an issue where **CI Job** build was failing with a **NullPointerException** ([#55204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089616148)).
* Fixed an issue where the **Repository Branch** was unavailable to select to run the **Merge** process after selecting **On successful deployment** option ([#55537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090158003)).
* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue with **EZ-Commit** where user was trying to perform a **destructive commit** using **Autodraft** option, but was unable to select **deleted components** under the **Deleted** tab ([#55507](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089979335) and [#55651](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090293003)).
* Fixed an issue where user was getting a **NullPointerException** when trying to resolve a **Merge conflict** ([#55137](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089410195)).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was able to create a **Delegated Group** but was unable to add a **Delegated Admin** user to the group using **Environment Provisioning** ([#55266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089705014)).

#### 20 November 2022 <a href="#20-november-2022" id="20-november-2022"></a>

**(ARM v22.1.34)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing **Prevalidation Commit** but commits in the repository have different components than the ones shown in **Diff** before the commit ([#52307](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086491044)).
* Fixed an issue with **Install an Unlocked or Managed Package from a Version Control Branch** where CI job getting an exception and the build status was showing as successful but the **Scratch Org** was not being created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **CI Job** shows that the ALM status has been updated successfully but on **Azure ALM** it is not updated ([#54669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088657005)).
* Fixed an issue where **Test Automation CI Jobs** were failing due to **InitializeDriver** & **quit methods** ([#45878](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077372830)).
* Fixed a bug where user was able to access certain branches in the **Deployment** module to which he did not have access under **Profile Settings** ([#54879](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089011291)).
* Fixed an issue with **CI Jobs** where the build failed with **Checkout** conflict for an **.svg file** ([#54172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088252005)).
* Fixed an issue with **nCino** where **Record Classification** and **Classification Objects** were missing in the template (internal ticket).
* Fixed an issue with **nCino** where user was creating a CI Job and observed that `Use UTF-8 file encoding for the file read and write operations` flag was displayed at the bottom below the **Commit Details** section (internal ticket).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was unable to add another branch to **Azure** in the **ALM MGMT Repository mappings** ([#55133](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089433593)).
* Fixed an issue where the **Destructive** commit **Diff** was including more components than selected ([#54795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088780309)).
* Fixed an issue where a merge got stuck for a long time and the **Commit ID** was reflected in **BitBucket** but unavailable to select for release label deployment ([#52964](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087060140)).

#### 13 November 2022 <a href="#13-november-2022" id="13-november-2022"></a>

**(ARM v22.1.33)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was trying to create an **Extract** process in **DataLoader** but after validating the query the application was throwing an error: `not supported; requires @DynamoDBTyped or @DynamoDBTypeConverted` ([#54648](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088630160)).
* Fixed an issue with **CI Jobs** where **External Credential** metadata was not identified during **Deployment** ([#53939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087955144)).
* Fixed a UI bug where user was performing an **org to org deployment** using **package.xml** file and the components were successfully deployed and also verified on Salesforce target, but the status on ARM was still **In-Progress** ([#50459 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375)and [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue with **DX CI Jobs** where user is not getting details of faulty commit revisions in the notification ([#54063](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088015242)).
* Fixed an issue with **Profile Manager** where the deployment is not showing any progress in the logger detail in front end. It was updated only after completion of the deployment job at backend ([#53706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704963)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed a bug where **Merge Commit** validation was not considering special characters like %,#, etc. as a value and throwing the following error: `Merge comment should not contain an empty space` ([#54512](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088479003)).
* Fixed an issue where ARM was slowing at different phases in the **EZ-Commit** module ([#50503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084910726)).
* Fixed an issue where Git check response was not delivered for validation **CI Job** even though user has added the comment for a **Pull request** in the remote repository ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).

#### 06 November 2022 <a href="#06-november-2022" id="06-november-2022"></a>

**(ARM v22.1.32)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DX CI Job** where user selected **Do Not Include Skip Members** but the respective mapper reports were not skipped (internal ticket).
* Fixed an issue where the **Deployment** module page was loading very slowly and then thrwing an error: `Page Unresponsive` ([#53675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704191)).
* Fixed the following issues in **CI** and **Reports** modules (internal ticket):
  * Build With **NULL ERROR** (issue exists both with Proxy and without Proxy)
  * SF Org Code coverage Execution is failing (issue exists both with Proxy and without Proxy)
  * Jenkins Build is updated with **FAILED** status even after it is successfully completed (issue exists only without Proxy)
  * Checkmarx text is not displaying the **Proxy Configuration** note (Only With Proxy)
* Fixed an issue with **QA Environments** where user was unable to create and delete the **SFDX module** because of the **Apache config CACHE** settings (internal ticket).
* Fixed an issue with the **Deployment** module where user initiated a **Deployment** without selecting the **Do not Include Skip Members** option, but this option was auto-enabled and skipped the member at the time of deployment ([#53747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087811296)).
* Fixed an issue with **Modularization** where user creating a module and selected the **Ignore installed components** check box but the installed components were not ignored causing the deployment to fail ([#53703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087755311)).
* Fixed an issue with **AccelQ Test Automation** where test case fails but the error details pop-up is not showing the details of the error that caused the failure ([#54224](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088281589)).
* Fixed an issue where user is setting up the **Apex PMD rules** as **Priority 1** & **Priority 2** in the **CI Job** but the SCA Report is showing the **Priority 3, P4 & P5** which wasn't selected ([#54017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087969396)).
* Fixed an issue where the **Git** check response was not delivered for a validation **CI Job** ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).
* Fixed an issue where the **Deleted Report** metadata components were not found in the **EZ-Commit** ([#53119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087247293)).
* Fixed an issue where user was trying to perform a **Quick Merge** but was getting an **Undefined** error for all labels (internal ticket).

#### 30 October 2022 <a href="#30-october-2022" id="30-october-2022"></a>

**(ARM v22.1.31)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where triggering a **CI Job** in **Objects** was resulting in an ambiguous error in the **CI Job Build** ([#53066](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087190013), [#52955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087099268), [#53631](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087579265)).
* Fixed an issue where all **CI Jobs** were failing and throwing the error: `Validation Checking failed Version Control Mappings not found for Repo: SA Repo and Branch: bugfix/Bugfix_PQT_Rel_Validation` ([#52945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087098136), [#52950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087101272), [#52757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086925007)).
* Fixed a UI bug on the **CI Jobs** page for **Install an Unlocked or Managed Package from a Version Control Branch** type where old **Dev Hub**dropdown list was displayed in the **Deploy** section (internal ticket).
* Fixed an issue with **AccelQ** where running a test execution was successful even before the jobs were completed in AccelQ, but the status was always showing as **Not Run** instead of **Success** or **Failure** even if the jobs have been successfully completed ([#50181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084509148)).
* Fixed a **Page Unresponsive** issue while creating a new **Release Label** by adding a feature to list limited results on each page ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where a merge got auto-approved and was in **Merged Not Commit** status ([#52398](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086586845), [#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed an issue where user created a **Release Label**, performed a **Merge** operation, committed changes to the target branch, and created two revisions in the **Github** branch.\
  But ARM was throwing an error while applying merge stage and only on the revision generated ([#51364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085859319)).
* Fixed an issue where **EZ-Commit** initiation was stuck with the error: `Unable to fetch Salesforce Org users. Reason: Invalid login: invalid user name or password or security token or api version or user locked out` ([#52550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086834002)).
* Fixed an issue where user was not able to select the orgs in the **EZ-Commit** drop down ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001), [#51219](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085620605)).
* Fixed an issue where **Page Size** value on the **Edit Release Label** screen is defaulting to the previous value instead of the set value (internal ticket).
* Fixed a UI bug where **OK Button** in **Automation** is not visible in the **Create Release Label** pop-up when opened in 100% zoom (internal ticket).

#### 23 October 2022 <a href="#23-october-2022" id="23-october-2022"></a>

**(ARM v22.1.30)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **CI Job** was successful but was including components from **GIT revisions** from old deleted branches ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a production deployment using CI job for an object, but it failed with the following error: `Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field` ([#48626](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082749181)).
* Fixed an issue where **CI Job** was getting an exception, **Build** status was showing as _successful_, but **Scratch Org** not getting created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **Managed Package** was picking the wrong ancestor by adding a feature to manually select the preferred ancestor while creating a package version ([#48311](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223305)).
* Fixed an issue where user was adding **URLs** to the **Proxy Configuration Settings** but the **URL List** was not reflecting the same (internal ticket).
* Fixed an issue where **Custom Template Creation** failed and the **Logs** did not record the reason for failure ([#52147](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086277150)).
* Fixed an issue where the **Created By** value was not visible in **Dataloader**, **Dataloader Pro DL Config**, and the **TestEnv History** page (internal ticket).
* Fixed an issue where the **Comment Box** was not accepting more than **100 characters** while rejecting a **Commit**, but was working as expected while approving a commit ([#51384](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085891476)).
* Fixed an issue with **Apex Test Class Config.** in **SF MGMT ORG** where the **Fetch Current Set**, **Add Manually**, and **Auto Populate** options were throwing an error: `Error 200` ([#52408](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086578687), [#52328](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086485900)).
* Fixed an issue where user set **Commit validation Criteria** to **Auto reject after 7 days** but the older Pre-validation commits are not auto rejected after 7 days ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user cannot add **Skip** members manually and it is failing due to **special characters** being included ([#53139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087266642)).

#### 16 October 2022 <a href="#16-october-2022" id="16-october-2022"></a>

**(ARM v22.1.29)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where skipped members were present in many components but only **Report Metadata** was failing during **Deployment** ([#51040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085433814)).
* Fixed an issue where **CI Job** was getting stuck in **In Progress** status but the log showed that the deployment was successful ([#51140](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085583019)).
* Fixed an issue where GitHub login credentials were not working when user triggered a CI Job for the second time ([#50630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085136003)).
* Fixed an issue where CI Job has failed in the Salesforce org, but still stuck in **In Progress** status in ARM ([#50435](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084823763)).
* Fixed an issue where user raised a **Pull request** on a branch and was getting a webhook response, but CI Job build was not triggered ([#51592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085996953)).
* Fixed a UI bug where **Add to dashboard** button was unavailable for widgets ([#52333](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086514169)).
* Fixed an issue where a new database file is created and overwritten with an existing database file whenever the server was restarted (internal ticket).
* Fixed an issue where user was trying to resolve conflicts on **Merge Request Labels** created more than 7 days ago, but application was throwing an error: `undefined` (internal ticket).
* Fixed an issue where **Custom Email Template** was not working for **Email notifications** ([#47484](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080506162)).
* Fixed an issue where user was testing **SSH Connection** but the application was throwing an error: `invalid privateKey` ([#50940](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371198)).
* Fixed an issue with **nCino** where **UI Log** was not generated for failed CI Jobs ([#50442](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084795478)).
* Fixed an issue where **New EZ-Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue where **Audit Logs** were not generating via **Postman Services** ([#50221](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084545179)).
* Fixed an issue where **Commits** were getting stuck and throwing the following error: `No credential have been found with Name:git`, but was not reflecting in the UI log ([#51713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086127001)).
* Fixed an issue with **Workspace Settings** where unused workspaces were not being cleared despite selecting **Clear all workspaces which are not used in last 7 days** ([#50164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084481079)).
* Fixed an issue where user was performing a **Prevalidation EZ-Commit** and found that some **Layout Assignments** were deleted though those layouts were not part of the commit ([#50945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371456)).
* Fixed an issue with **nCino** where migration was failing due to errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).

#### 09 October 2022 <a href="#09-october-2022" id="09-october-2022"></a>

**(ARM v22.1.28)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **nCino** where user was getting errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).
* Fixed an issue where user noticed discrepancy in the **Conflict Resolution Log** ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).

#### 02 October 2022 <a href="#02-october-2022" id="02-october-2022"></a>

**(ARM v22.1.27)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where components were successfully deployed, but deployment status was still showing **In-Progress** in ARM ([#50459](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375), [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where CI Jobs were getting stuck and throwing the following error: `Too many open files` ([#44319](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001), [#49273](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001)).
* Fixed an issue where **email notification** wasn't sent for some of the **CI Jobs** ([#48028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081639899)).
* Fixed an issue where the Custom label and remote site setting URLs were not getting updated by ARM through **Environmental Provisioning** ([#49612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083684001)).
* Fixed an issue with **Vlocity** where selecting one component from a GIT repository was causing all the components from the category to get selected ([#49806](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084007005)).
* Fixed an issue with **ALM Mgmt.** where item status was not retrieved properly for **Merge Request**, but was working as expected for **EZ-Merge** ([#50628](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085133005)).
* Fixed a UI bug where **Release Labels** were showing duplicate **Time Stamps** ([#51205](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085689003)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected after 7 days as the user had configured under **Commit Validation Criteria** ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user was getting an error pop-up on the **Permissions** and the **SF ORG MGMNT** pages, and the SF org and VC repo mappings were lost in the profile section of a role ([#49108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083164265)).

#### 26 September 2022 <a href="#26-september-2022" id="26-september-2022"></a>

**(ARM v22.1.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** test job was throwing an error while in queue ([#49797](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083986945)).
* Fixed an issue where scheduled auto-sync of external commits was not working (internal ticket).
* Fixed an issue with the **New EZ-Commit** screen where **ALM Types** are changing to old ALM type names after resaving details on the **ALM Management** screen (internal ticket).
* Fixed an issue with **Pre-validation merge** where the **Object** file content was empty in the **CodeScan Analysis SCA** report (internal ticket).
* Fixed an issue with **Branching Baseline** where some of the custom object metadata nodes were deleted from the repository ([#47239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080102001), [#47270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080113166)).
* Fixed an issue with **EZ-Merge** where **Diff** was not being generated even though there were file changes between the source branch and the destination branch ([#50323](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084689471)).
* Fixed a UI bug in **DataLoader** where user was switching from **Graphical View** to **Grid View** but **Graphical View** options were still being displayed ([#50431](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084822478)).
* Fixed an issue with **nCino** where the **Insert/Update With Null Values** option was not getting updated for CI jobs ([#50259](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084641005)).
* Fixed an issue where users were unable to **re-authenticate** the **Salesforce Org** after refreshing their personal sandboxes ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001)).
* Fixed an issue where **Environment Provisioning Template** was not functioning as expected for **Custom Labels** containing URL ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue with **EZ-Commit** where user was trying to deploy **Permission Sets** and **Profiles** together, and the pre-validation process was stuck in **In-Progress** status ([#49340](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083456001)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected as configured ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).

#### 19 September 2022 <a href="#19-september-2022" id="19-september-2022"></a>

**(ARM v22.1.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed multiple issues with **CodeScan<>ARM** Integration (internal ticket).
* Fixed an issue where **CI Jobs** and **Deployments** were both failing for **Reports** and **Dashboards** because the folder could not be found (internal ticket).
* Fixed an issue with **New Commit** screen where the **Select All** checkbox was getting unselected when navigating from the **DELETED** tab to the **ADDED/MODIFIED METADATA COMPONENTS** tab and back to the **DELETED** tab (internal ticket).
* Fixed an issue with **Version Control Prevalidation Commit** where for the selected **Custom Metadata** and **Permission Set**, **Diff** was being generated as expected but the **Deployment** was failing (internal ticket).
* Fixed an issue with **Version Control Prevalidation Merge** where SCA report was empty, and throwing the following error in the console: `Uncaught TypeError: Cannot read properties of undefined (reading 'length')` (internal ticket).
* Fixed an issue where user was unable to reset the AutoRABIT password, and was getting an error: `getAttribute: Session already invalidated` ([#50145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084391472)).
* Fixed an issue where **CI Jobs** was not picking the right number of components unless the user cancelled the build and retriggered it ([#47164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921675)),([#46981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079504156)).
* Fixed an issue where the user tried to merge to the Dev branch but the **CI Job** failed and was throwing a **Duplicate** error ([#49661](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083729177)).
* Fixed an issue where user was trying to install **Unlocked Package** via **CI Job** but it was failing and throwing the following error: `ERROR 178928269770891:275 - For input string: "0-2" java.lang.NumberFormatException: For input string: "0-2"` ([#50093](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084341003)).
* Enhanced **Vlocity** loggers for **Branching Baseline** by displaying to the user **Status Count** of **Remaining**, **Success**, **Error** and **Ignored** (internal ticket).
* Fixed an issue where **Test Connection** was failing on the **Version Control Summary** page under the **Admin** module ([#49299](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083372346)).
* Fixed an issue with **Prevalidation Merge** by increasing the **SCA Response timeout** from **50 minutes** to **5 hours** ([#48613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082720068)).
* Fixed an issue where merging **Master Branch** with the **Production** branch was throwing the following error: `No merge head specified` ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed a bug where **New A-Z Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue with **Autorabit Commit Label** related to **Permission Sets Deployment** ([#48709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082892203)).

#### 11 September 2022 <a href="#11-september-2022" id="11-september-2022"></a>

**(ARM v22.1.24)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was selecting a single package to import, but all available package versions were being imported ([#49426](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083542359)).
* Fixed an issue with **Profile Manager** where user was comparing a profile but the deployment was not starting ([#48620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082696017)).
* Fixed an issue where deploying components with profiles was not working as expected and throws the following error: `Duplicate layoutAssignment:PersonAccount (PersonAccount.Person_Prospect)` ([#49021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083082001)).
* Fixed an issue where custom metadata records were not being selected during deployment ([#49167](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083203846)).
* Fixed an issue in **Version Control Commit Labels** history where **Created By** and **Created Date** values were exchanged (internal ticket).
* Fixed an issue where user was getting an error while trying to deploy **Vlocity Metadata** using **CI Jobs** ([#47568](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080830005)).
* Fixed an issue where **Branching Baseline** was not retrieving **Workflow Metadata types** ([#49403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083447017)).
* Fixed an issue where **Release Label** failed to load revisions from a particular branch and the browser was hanging and throwing an _Out of memory_ error ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where **EZ-Commit** was not getting auto-rejected when **CodeScan** analysis failed, even though user select the option to run **Static Code Analysis** ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).
* Fixed an issue where merge was failing at the **Validate Deploy** step even before selecting the org to validate ([#49724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083898393)).
* Fixed an issue where **Layout** was being removed from the **Diff** while deploying **Profile** changes with related **Layouts** and **RecordTypes** ([#48268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082045983)).
* Fixed multiple issues with **CodeScan<>ARM** Integration ([#49605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083671017)).

#### 04 September 2022 <a href="#04-september-2022" id="04-september-2022"></a>

**(ARM v22.1.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing a new deployment but getting an error when using the **Compare Orgs & Deploy** button ([#48707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860460), [#48676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860003), [#48737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082918005), [#48734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082914003)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.NullPointerException: null` ([#48706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860315)).
* Fixed an issue where few fields were not being analyzed in CodeScan SFDX. User was selecting Custom Fields, Apex Classes, and Record Types in E-Z Commit, but Static Code Analysis was only Apex Classes ([#48547](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082584398)).
* Fixed an issue where dashboards and reports were changing to **Destructive** and getting deleted ([#48119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081915009)).
* Fixed an issue where discrepancies for **Document**, **Assignment Rule** and **AutoResponseRule** metadata types content was observed in **package.xml** for SFDX and non-SFDX CI Jobs ([#47017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079534439)).
* Fixed an issue where the Dataloader Pro Jobsfailing and throws the following error: `java.lang.NullPointerException: null` ([#49170](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182317), [#49283](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083331025), [#49331](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083407003), [#49199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182597)).
* Fixed an issue where nCino CI Jobs via RBC were failing during parallel deployment. Instead of falling in queue, the first job was failing while the other succeeded, and the user had to retrigger the failed job ([#47335](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080272507)).
* Fixed an issue where creating multiple deployment jobs from the same source org to the same destination org for different templates, the jobs were failing with **Null Pointer Exception** error (internal ticket).
* Fixed an issue with **DX Pre-validation merge** where **Destructive Deployment** for custom labels failed without any errors (internal ticket).

#### 28 August 2022 <a href="#28-august-2022" id="28-august-2022"></a>

**(ARM v22.1.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Unpackaged Packages Directory** folder was being created in the **Deployment Promotion** zip package when deploying **Static Resource Metadata type** using **Single revision DX Deployment** (internal ticket).
* Fixed an issue where after upgrading the AR instance, deployment jobs kept removing the custom metadata access on the **Permission Sets** ([#48296](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082147005)).
* Fixed an issue where **Org difference** jobs were running for more than 24 hours ([#48324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223730)).
* Fixed an issue where Environment provisioning template was not working when trying to update custom label values that contain URL, and the incorrect value was being updated in the org ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue where choosing the **Select Manually** option while doing a commit was resulting in a blank screen for the **Deleted** tab (internal ticket).
* Fixed an issue where while doing Prevalidation commit in AR, **Commit Only Permissionsets For The Selected Metadata** functionality was not working properly for both DX and Non-DX cases (internal ticket).
* Fixed an issue in Dataloader where an **Undefined Error** was displayed when user was trying to create and save the **Screens Template** (internal ticket).
* Fixed an issue where user was trying to validate the commit using single revision, but was getting an **Empty Package** error even though there were changed files in the commit ([#47530](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080730150)).
* Fixed an issue where DataLoader Pro jobs were failing with an error **duplicate value found: SetupOwnerId duplicates value on record with id** for the custom setting **Multichannel\_Settings\_vod\_\_c**, even though there is no field mapped with name **SetupOwnerId** ([#48230](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081981779)).
* Fixed an issue where the **search** functionality was not working in Dataloader Configuration as well as Dataloader Test Environment Setup (internal ticket).
* Fixed an issue where EZ Commit Logs and Change Labels were not displaying for some of the commit labels ([#45364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076464250)).
* Fixed an issue where the user was not able to see the deployment report because the build was failing when only custom fields were being selected without the related object ([#45663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077048275)).
* Fixed an issue where merge request was being auto rejected if the selected approver was no longer with AR ([#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed a bug where user had enabled Squash and Merge while performing a new merge, but the Squash and Merge option was not displayed after the Merge Request was approved ([#48246](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082046388)).
* Fixed an issue in CI Jobs deployments where Bulk API option for **Attachments** was throwing an error (internal ticket).
* Fixed an issue where **nCino CI Jobs** were failing the first time and completing the second time successfully ([#46545](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644141)).

#### 21 August 2022 <a href="#21-august-2022" id="21-august-2022"></a>

**(ARM v22.1.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI job build was getting stuck in **In-progress** status ([#47934](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081483565)).
* Fixed an issue where **RunSpecifiedTest** level execution was failing with Test classes dependency errors ([#47666](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081029378)).
* Fixed an issue where DX CI Job build failed if document metaxml change commit revision includes in the build \[Including Email templates and Static Resources types] (internal ticket).
* Fixed an issue where entire branch merge was failing with multiple common ancestor errors ([#47334](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080237436)).
* Enhanced the Dataloader history screen (internal ticket):
  * Column mover added to table column alignment for text view.
  * Moved **Last Run** details to the **Date/Time** column.
* Fixed an issue where Standard fields are not retreiving when included in **package.xml**, and retrieving through **E-Z Commit (Package Manifest)** option ([#47961](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081505333)).
* Fixed an issue for the **nCino CI Jobs** were failing due to default selection of **AutorabitExtId\_\_c** in **Mappings** (internal ticket).
* Fixed an issue for the nCino Deployments where even if **LookupKey** is available, by default **Name** is selected in **External ID Mapping** (internal ticket).
* Fixed an issue for the nCino CI Jobs where **Attachments** were failing due to **External Mappings** not being set to the **NAME** field (internal ticket).
* Added the feature to dynamically handle the respective nCino Prefix rather than depending on the JSON file to identify the External Id field

***

#### 14 August 2022 <a href="#14-august-2022" id="14-august-2022"></a>

**(ARM v22.1.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushed with special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).

***

#### 07 August 2022 <a href="#07-august-2022" id="07-august-2022"></a>

**(ARM v22.1.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the package URL was not visible for the SFDX modules successfully configured in ARM (internal ticket).
* Fixed an issue where our internal team members got the undefined error while creating a new scratch org and selecting the module (internal ticket).
* Fixed an issue where after triggering the CI job, the **File Changes** and **Check-ins** results mismatched ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue where the package created to deploy ExperienceBundle misses some of the folder and metadata files contained in it ([#46692](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079024001)).
* Fixed the below deployment-related issues:
  * Unable to find commits that are part of a Release Label while performing a new deployment ([#47337](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080246444))
  * Unable to retrieve components from a Release Label during deployment ([#47534](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080713440))
  * Changes are not deployed to the destination org which are part of a Release Label ([#46908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079358877))
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).
* Fixed an issue where the deployment failed to initiate when search and substitute rules are selected ([#47802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081320007)).
* Fixed an issue where the status log .csv files are inconsistent for deployment via CI jobs (internal ticket).
* Fixed an issue where the users were unable to process the migration of RBC object (nForce\_\_Views\_\_c) using the nCino CI jobs, feature template migration, or the Dataloader Pro jobs ([#47098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079761055)).
* Fixed an issue where while deploying a **nCino-User Interface** template, only partial records are deployed and no deployment logs are generated ([#47494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080488668)).
* Fixed an issue where the users, while performing an EZ-Commit by enabling the run SCA option, the CodeScan analysis is getting failed, but EZ-Commit is not getting auto-rejected ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).

***

#### 31 July 2022 <a href="#31-july-2022" id="31-july-2022"></a>

**(ARM v22.1.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Upgraded the Spring and AWS libraries on ARM for addressing the Spring vulnerability ([#46970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079471289)).
* Fixed an issue where the users were unable to login to ARM via SSO (internal ticket).
* Fixed an issue where the ARM is not able to fetch any component using the release label ([#46662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078894834)).
* Fixed an issue where the baselining of branches has wiped out the records types for many records, and the users were forced to do manual changes to the Record types ([#42719](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072309163)).
* Fixed an issue where the ARM allows to associate only one branch to one package, and not able to build beta package versions from various branches. This is now fixed ([#46841](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262193)).
* Fixed an issue where the CI job, while deploying manage packages, is installing all the manage packages instead of installing a single package ([#46832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262054)).
* Fixed an issue where the links on the **CI Job log** screen are redirected to the user's login page instead of redirecting to user's Salesforce org screen ([#47151](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079912283)).
* Salesforce API version 55 (Beta support) is upgraded. The label is modified throughout ARM application to Salesforce API version 55.0 ([#47404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080386152)).
* Duplicate classes from the ARM repo has been removed (internal ticket).
* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushedwith special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the merge was getting failed with the following error: `Fetch operation is failed due to some runtime exceptions from Git` ([#46773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079094055)).
* Fixed an issue where the username and passwords fields were not editable for users registered in ARM with basic authentication ([#47099](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079788018)).

***

#### 24 July 2022 <a href="#24-july-2022" id="24-july-2022"></a>

**(ARM v22.1.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when user triggers a code coverage run in the production environment, the action takes more time than expected. Also, the total time taken for the task completion is shown inaccurate in the log report ([#44544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040590), [#43527](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073512143)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.OutOfMemoryError: Java heap space` ([#47182](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988001), [#47190](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988142), [#47209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080017264), [#47191](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079950166)).
* Fixed an issue where the **Rollback settings** were not getting saved in the **My Account** page (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue with the permissionsets where instead of delta changes, the Permissionset retrieving entire file from the branch and causing dependency issues ([#46846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262334)).
* Fixed an UI bug where the ARM application displays unwanted scrollbar when **"Exclude Installed (Managed) components"** is selected in the **My Account** page (internal ticket).
* Enhanced the ARM workspace feature to automatically unlock the workspace after sufficient time to run the workspace operations.
* Added the feature to set **Limit 0** option for the Dataloader Pro jobs. This limit will allow users to skip migrating child or Ancestors objects.
* Fixed an issue where while editing an existing nCino CI Job, the version control is not automatically choosing the previous repository set. This is causing the selected nCino Templates to reset ([#46952](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079432380)).
* Fixed an issue where the ALM labels were missing from the ALM Label lists page ([#44410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074860453)).
* Fixed an issue where the settings related with user permissions were erased ([#46472](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078507457)).
* Fixed an issue where the users when performed EZ-Commit using a package manifest file, doesn't include managed components that are in the **package.xml** file ([#47083](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079769291)).

***

#### 17 July 2022 <a href="#17-july-2022" id="17-july-2022"></a>

**(ARM v22.1.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the Execute Anonymous Apex metadata is not working as expected when configured as Environment Provisioning template ([#46817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079248146)).
* Fixed a bug where our internal team were able to use the perform the prevalidation commit and direct commit without giving the prevalidation commit label name and without commit comment, which are mandatory fields (internal ticket).
* Fixed an issue where the ALM workitems are not retrieved in CI job through merge (internal ticket).
* Fixed a bug where our internal team were able to save the **Install an Unlocked or Managed Package from a Version Control Branch** CI job even though Installation key were not uploaded which is a mandatory field (internal ticket).
* **\[Enhancement]** Added the Salesforce versions information in the logs for all Dataloader related jobs activities.
* **\[Enhancement]** Added the ability to delete a commit before it is pushed to your remote repository so that you have a choice to redo incorrect commits/ merges.
* Fixed an issue where the merge prevalidations were auto rejected with status as **Approval Pending** ([#46665](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078888152), [#46864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079289063)).
* Fixed an issue where the **Delete Commit** button was not seen after approving an EZ-Commit label (internal ticket).
* Fixed an issue where the toggle button for the dashboard metadata type in the commit label screen is not working as expected (internal ticket).
* Fixed an issue for the nCino Feature Deployments where the users were getting audit field issue when trying to deploy with `Insert/Update with Null Values` option (internal ticket).
* Fixed an issue for the nCino CI jobs using Spreads Templates where the users were getting `NullPointerException` error when trying to deploy with `Insert/Update with Null Values` option (internal ticket).

***

#### 10 July 2022 <a href="#10-july-2022" id="10-july-2022"></a>

**(ARM v22.1.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users failed to enable the pull request support for their version control repositories ([#46336](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078290172)).
* Fixed an issue where the re-use previously validated commit label takes more time to load ([#46171](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077992017)).
* Fixed an issue where the constructive changes are picked in the CI build, although no constructive changes are in-between _From_ and _To_ revisions (internal ticket).
* Fixed a bug marked deployment as failed, whereas the log report says successful ([#46737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079038631)).
* Fixed an issue with the SFDX job, where for the Report metadata type, the rollback feature was working weirdly (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue where entering the package installation key in `Install an Unlocked or Managed Package from Version Control Branch` CI Job gets altered when manually entered or pasted ([#46836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079265163)).
* Fixed an issue where the user could not run the static code scan report on GitHub with APEX PMD Lint Scanner metadata type ([#46781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079122007)).
* Fixed an issue with the CodeScan analysis report that failed when running from ARM ([#44404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074862389)).
* Fixed an issue where the user could not fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Enhanced the Dataloader Pro, where the attachments are now supported ([#41077](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299001)).
* Fixed a bug where editing the Dataloader job shows **"Job Group"** as _null_ or _empty_ (internal ticket).
* Vlocity has been upgraded to v1.15.5.
* Fixed an issue with the CI job where the version control using Salesforce with attachments was not picking the attachments during CI build (internal ticket).
* Fixed an issue with the EZ-Merge, where merging the main branch to the dev branch failed with a `No merge head specified` error ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed an issue that throws `Schema as invalid` error while running the branching baseline operation ([#46593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078805109)).
* Fixed an issue where the merge failed using a single revision ([#46491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644005), [#45764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077211038)).
* Fixed an issue where our internal team members could not create a new role from the **Admin** section (internal ticket).
* Fixed a bug where the `Invalid Schema` error is seen for non-SFDX prevalidation merge (internal ticket).
* Fixed an EZ-Commit issue where additional permissions were removed from Profiles metadata type, which is not a part of the commit ([#44543](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040441)).

***

#### 03 July 2022 <a href="#03-july-2022" id="03-july-2022"></a>

**(ARM v22.1.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment via CI job picked unnecessary components for deletion ([#44204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074533873)).
* Fixed the issue where the user when trying to delete a component in **Community** metadata type, deletes the whole Community rather than its components ([#43698](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073869007)).
* Fixed an issue where DevHub registration in ARM was failing ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed a bug where our internal team members were not able to view the Salesforce Org URLs in the **My Profile** section (internal ticket).
* Fixed an issue where the deployment using **Commit/Release Label** was not working ([#46419](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078496053)).
* Fixed an issue where the mapping more than one class to same test class is not recognized by ARM during commit/merge operation ([#46396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078430859), [#45159](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076223139)).
* Fixed an issue where the CI job builds were failing because of missing revisions ([#45532](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076855001), [#46352](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078378003)).
* Fixed an issue where the **Compact Layout** were not getting deployed and throws undefined error([#46592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078798022)).
* Fixed an issue where the ALM statuses were not updated/rolled back post CI job rollback completion ([#45945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077581145)).
* Fixed an issue where the destructive changes were not working as expected for the CI jobs ([#46216](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049311)).
* Fixed an issue where the ARM failed to update the Audit fields when trying to run nCino feature deployment ([#46356](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078401001)).
* Fixed an issue where our internal team were not able to register their credentials on one of the ARM SAAS instances ([#46315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078239277)).
* Fixed an issue where prevalidation commits were getting failed due to credential issues. The following error was thrown `No credentials found` ([#46274](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078213003), [#46098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077754153)).
* Fixed a bug where the deleted components were tagged as **UC (UnChanged)** instead of **D (Deleted)** in the EZ-Commit ([#46087](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077760173)).
* Fixed an issue where the metaXML file were not retrieved for the ContentAsset metadata type for the **SFDX "Entire Branch"** merge case (internal ticket).
* Fixed an issue where the deployment validation were failing for the prevaildation merge with the error: `No source backed components present in the package` (internal ticket).
* Fixed an issue where the merge using single revision (baseline revision) receives the metadata schema error ([#46570](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078699087)).
* Fixed an issue where the merges were getting failed and throws the `Schema is invalid for the file` error ([#45768](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077202614)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).

***

#### 26 June 2022 <a href="#26-june-2022" id="26-june-2022"></a>

**(ARM v22.1.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Spread Template** in the **nCino** module was not working as expected ([#45078](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076003188)).
* Fixed an issue where the user was getting `"field integrity exception: unknown (CreatedByID(0051X00000BbMIR) is not in org"` for the records that were available in the destination org.
* Fixed the issue where the **Disable Workflow** template in the **Environment Provisioning** module was not working as expected ([#46195](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049157)).
* Fixed an issue where the creation of a scratch org were getting failed. The fix has been deployed to in this weekly release ([#46021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690007)).
* Fixed an issue where the users were unable to use the **release label** for deployment ([#45415](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076584626)).
* Fixed an issue where the users were not able to register same DevHub with two different usernames ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed an issue where the CI Job was picking the deleted components from GitHub branch although the **Prepare Destructive Changes** checkbox was not selected. This caused the deployment to fail ([#42553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the users were not able to view their GitHub branches in the ARM application ([#46044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690473), [#46353](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078386013)).
* Fixed an issue where the CI Job for backing up from org to the version control branch was failing with null pointer exception error ([#45646](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the **EZ-Commits**, when included **Profile**, was not working as expected ([#45902](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077441170)).
* Fixed an issue where the commits were getting stuck at the delta stage ([#45101](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076070023)).
* Fixed an issue where the Git tags were being added to the queue but not being processed (internal ticket).
* Fixed an isse where the delta was getting failed in the **EZ-Commit** flow (internal ticket).
* Fixed an issue where the Dalaloader Pro job is failing with `Required field missing on "nCino_Screen__c" object`, however the user were able to view the `Screen__c` object has a value in their source org ([#45139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076158018)).
* Fixed an issue where the user were not able to save the Dataloader Pro jobs and throws the `JAVA.NullPointerException` error ([#46385](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078393786)).
* Fixed a bug where the users were not able to view the log reports after registering **Tags** via ARM (internal ticket).
* Fixed an issue where the tags creation got failed when the tag name contains **'error'** with custom API flow (internal ticket).

***

#### 19 June 2022 <a href="#19-june-2022" id="19-june-2022"></a>

**(ARM v22.1.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a minor bug where the child members checkboxes remained checked even when the parent metadata type was unchecked (internal ticket).
* Fixed an issue where CI job build **ToRevision** number was mismatched in the **CI Job Results** and the **CI Build Info** page ([#45580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076910037)).
* Fixed an issue where the request parameters were empty in the **nCino Feature Commit History** screen ([#45855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077344165)).
* Fixed an issue where the users while accessing the commits older than 30 days, ARM throws `Request parameters are empty/null` error (internal ticket).
* Fixed an issue where the users when accessing the **Commit History** page throws `Invalid FilterExpression` error (internal ticket).
* Fixed an issue where the user were unable to fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Fixed an issue where the **Diff report** in the **Merge Request** was not working as expected ([#45315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076389550)).
* Fixed an issue where the user ran the branching baseline operation by excluding the Managed package components, however, the **Package.xml** file still had all the managed package components listed in it ([#45125](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076117289)).
* Fixed an issue where the code coverage report was being generated at a different time than what was scheduled ([#45703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077145009)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).
* Fixed an issue where the TAF execution were getting failed (internal ticket).
* Fixed an issue where the **From Revision** was not visible when user access their CI job from **CI Job History** page (internal ticket).
* Fixed an issue that caused **Chrome** to crash anytime a user attempted to view the functional test results for the task of running a Selenium Maven test. The functional test results screen enters a continuous cycle of requests, which crashes the browser (internal ticket).
* Fixed an issue where the **skip members** feature of ARM was not working as expected (internal ticket).
* Fixed an issue where the user while performing **EZ-Commit** with SonarQube code analysis was getting failed with `Failed to run the sonar-scanner: null` error ([#46070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077717988)).

***

#### 12 June 2022 <a href="#12-june-2022" id="12-june-2022"></a>

**(ARM v22.1.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

***

#### 05 June 2022 <a href="#05-june-2022" id="05-june-2022"></a>

**(ARM v22.1.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).

***

#### 29 May 2022 <a href="#29-may-2022" id="29-may-2022"></a>

**(ARM v22.1.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

***

#### 22 May 2022 <a href="#22-may-2022" id="22-may-2022"></a>

**(ARM v22.1.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

***

#### 15 May 2022 <a href="#15-may-2022" id="15-may-2022"></a>

**(ARM v22.1.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).

***

#### 08 May 2022 <a href="#08-may-2022" id="08-may-2022"></a>

**(ARM v22.1.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

***

#### 01 May 2022 <a href="#01-may-2022" id="01-may-2022"></a>

**(ARM v22.1.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).
* Fixed an issue where the commits triggered in ARM shows a different author in Azure DevOps ([#44225](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074591143), [#43503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073518014)).
* Fixed a bug where selecting the "**Deployment**" icon after signing in to the ARM application caused the user to log off and on and return to the home page ([#44040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301863)).
* Fixed a bug where the check-ins display the wrong number of files changed during commit ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue in the TAF module where nothing pops up when you click on the "**View Log**" button ([#42020](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071114057), [#40284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067992205)).
* Fixed an issue where the users while accessing the help center from ARM application, receiving the **({"result":"failure","cause":"E105 - Request Delayed"})** error ([#43579](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652168)).
* Fixed a bug where the commits was getting failed due to SCM (Software Configuration Management) authentication failure ([#42276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071577005)).
* Fixed a bug where the merge operations ran for more than 12 hours and later failed ([#38755](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065037173), [#42874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072544001), [#38913](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065383003)).
* Fixed an issue where extra metadata members are picked up for the profile component during the EZ-Commit process ([#41361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069919263)).
* Fixed an issue where the users could not use commit template for the deployment ([#43995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074325045), [#43586](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073635324), [#43905](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074163310), [#43407](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073339003)).

***

#### 24 April 2022 <a href="#24-april-2022" id="24-april-2022"></a>

**(ARM v22.1.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

***

#### 17 April 2022 <a href="#17-april-2022" id="17-april-2022"></a>

**(ARM v22.1.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue for the Chrome browser where the ApexPMD ruleset was not uploading incorrectly (under the **Plugins** section). For other browsers, it was working as expected ([#42954](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072670003)).
* Fixed the issue with the merge where the changes present in the source branches were not picked up, and therefore latest changes did not reflect on the destination branch ([#43553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073610001), [#43598](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073662177), [#43595](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073653614), [#43593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652863), [#43591](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073629096), [#43580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652300), [#43574](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073651134)).
* Fixed an issue where the Salesforce-DX deployment and rollback mismatches ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040))
* Added the criteria to trigger the callout URL post-deployment. If you set it to _success_, the callout URL is activated if the salesforce deployment is successful ([#38990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065571472)).
* Enabled feature flag settings to select between classic ARM and Salesforce CLI process to generate package manifest.
* Fixed an issue where the commit validation is successful for an empty field, whereas the CI job fails ([#43324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073218067)).
* Fixed an issue where the deleted metadata components were showing under the **"File Changes"** tab but did not appear under the **"Destructive Changes"** column while carrying out a manual deployment ([#41670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070494027)).
* Fixed Dataloader Pro job issue where the job is completed successfully without loading all ancestors/master objects data to the destination environment ([#43276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073123039)).
* Fixed branching baseline issue where all metadata from the production org were not copied to the version control repo/branch ([#42938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072633029), [#42685](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072244001), [#42955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072644308), [#42445](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071818001), [#43038](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072780490), [#42753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072314347), [#42242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071424143), [#42766](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072375048), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed the below nCino issues:
  * Unable to proceed with feature deployment using an existing community feature migration template due to the following error: **"No External Id field exist in source org."** This is now fixed and working as expected ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
  * Non-template records were being picked up during nCino deployment.
  * Non-template records are fetched in the dataset.
  * Spread Statement Record failing with the error **“Missing Statement Types.”** This is now fixed.

***

#### 10 April 2022 <a href="#10-april-2022" id="10-april-2022"></a>

**(ARM v22.1.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Abort** option was showing for completed CI jobs ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463), [#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed the issue where the SFDX deployment is getting failed even though the user uploaded the correct file.
* Fixed a bug where the static code analysis (SCA) status shows as **in progress** for a failed execution.
* Fixed an issue where deleting a custom field was affecting other custom objects where the globalpicklistvalue is shared by multiple objects ([#42782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072370556)).
* Fixed a bug where the users were not able to view specific values under the standard value sets in the **New EZ-Commit** screen ([#41773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070686445)).
* Fixed a bug where the **New EZ-Commit > Deleted Component** tab throws a null error on expanding the metadata types.
* Fixed a bug where the deploying records via record based configurations (RBC) was throwing error: **"No external Id field exists in the source org"** ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
* Fixed an issue where creating a new nCino feature migration template takes longer than expected ([#41855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070869289)).
* Addressed out of memory (OOM) and other performance issues in this weekly release.

***

#### 03 April 2022 <a href="#03-april-2022" id="03-april-2022"></a>

**(ARM v22.1.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option where not working when users use the EZ commit/ Merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

***

#### 27 March 2022 <a href="#27-march-2022" id="27-march-2022"></a>

**(ARM v22.1.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** in the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the exclude metadata types in the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).
