# Release Notes 22.2

**October 2022 - Version 22.2 - New Features, Enhancements, Improvements and Changelogs**

**Date of release:** _9 October 2022_\
**Article last updated:** _15 May 2023_\
\


### New Features <a href="#new-features" id="new-features"></a>

#### 1. Teams/Slack Notifications <a href="#id-1-teamsslack-notifications" id="id-1-teamsslack-notifications"></a>

**Mail Settings** module in the **Admin** section is relabeled as **Notifications**. Through this module, you can choose to send notifications about specific events triggered in ARM to specific groups or channels within your organization through **Teams** or **Slack**. For whichever messaging app you use, you can configure a webhook connection for each of the groups or channels, and then integrate them with ARM. You can customize and select which group(s) to notify when events like build failure, build success, deployment failure, merge reports, etc. are triggered.

[**Read more →**](../../../product-guides/arm/troubleshoot/how-tos/notifications-mail-server-settings.md)

#### 2. Salesforce Scanner plugin <a href="#id-2-salesforce-scanner-plugin" id="id-2-salesforce-scanner-plugin"></a>

In addition to the existing static code analysis tools, ARM now provides the ability to choose the **Salesforce Scanner CLI** plugin.

Most static code analysis tools specialize in one language or a set of languages. Many applications (including typical Salesforce packages), however, contain an assortment of components created using different languages. A single static analyzer is insufficient to address all aspects of such applications, and managing multiple static analyzer tools could prove unfeasible.

This is where the **Salesforce CLI Scanner** plugin shines. This plugin aggregates the results of static analyzers that are most relevant to Salesforce developers while providing a unified experience.

With the Salesforce CLI Scanner plugin, you can look forward to a:

* Single installation process
* A single set of commands to interact with multiple rule engines
* A unified set of rules that are checked by their respective rule engines
* Unified rule violation report that includes all issues identified by the engines.

#### 3. AutoRABIT for nCino <a href="#id-3-autorabit-for-ncino" id="id-3-autorabit-for-ncino"></a>

We’ve added the ability to view and review datasets corresponding to each version of the nCino feature template before using it for deployment. Prior to this release, the capability was available only for the latest version of the template.

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. ApexPMD Upgrade to 6.49 version <a href="#id-1-apexpmd-upgrade-to-649-version" id="id-1-apexpmd-upgrade-to-649-version"></a>

With this release, PMD has been upgraded to version **6.49**. If you have not uploaded a rules file, ARM will use the default Apex PMD rules file. However, you can add new rules to the default ruleset.

Click [HERE](https://pmd.github.io/latest/pmd\_next\_major\_development.html#list-of-currently-deprecated-rules) to view the list of currently deprecated rules available on GitHub.

***

#### 2. Auto-approve on validation success <a href="#id-2-autoapprove-on-validation-success" id="id-2-autoapprove-on-validation-success"></a>

We have moved one step closer to automating the flow by adding an option to choose if an **EZ-Commit** or an **EZ-Merge** should be approved automatically if the SCA validation is successful. Combined with the existing option to auto-commit on approval, this leads to a true CI/CD experience.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings/)

#### 3. HashiCorp Vault Integration <a href="#id-3-hashicorp-vault-integration" id="id-3-hashicorp-vault-integration"></a>

While adding HashiCorp credentials to ARM, you can now choose the **AWS Authentication** method so that the Vault Token will be generated automatically whenever the existing token expires. Now the user will not have to update the token manually from the application when it expires.

[**Read more →**](release-notes-22.2.md#3-hashicorp-vault-integration)

#### 4. SFDX CLI Upgrade <a href="#id-4-sfdx-cli-upgrade" id="id-4-sfdx-cli-upgrade"></a>

The SFDX CLI has been upgraded to the latest stable **7.169** version.

Key characteristics to look for:

* Support for the **quick deploy** functionality for SFDX jobs.
* Use CLI commands to generate the package manifest and rollbacks.

#### 5. Salesforce Winter (API 56.0) Support <a href="#id-5-salesforce-winter-api-560-support" id="id-5-salesforce-winter-api-560-support"></a>

To keep our product up to date with the most recent Salesforce updates, AutoRABIT supports the most recent **API 56.0** version in this release. The most recent API version is intended for customizing the metadata model and developing tools to manage it.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/salesforce-api-version.md)

#### 6. Merge to multiple branches <a href="#id-6-merge-to-multiple-branches" id="id-6-merge-to-multiple-branches"></a>

With this release, you can choose to **merge** from one **source branch** to multiple **destination branches** upon successful deployment.

[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/create-a-new-ci-job/deploy-from-sfdx-branch-to-a-salesforce-org.md)

#### 7. OAuth for Jira <a href="#id-7-oauth-for-jira" id="id-7-oauth-for-jira"></a>

In addition to the **Standard** access type, users can now set up **SSO** as authentication for **Jira** using the OAuth access type while registering an ALM. You can also switch between **Standard** and **OAuth** access types for already registered ALMs.

[**Read more →**](../../../product-guides/arm/arm-administration/alm-management.md)

***

### Improvements <a href="#improvements" id="improvements"></a>

* Users with Admin access can now turn off the Jira comments and notifications created by AR. This ensures a cleaner workspace. These comments and notifications are very development centric, so the end users who use Jira cannot make sense of our technical comments from AR, and this may create confusion for them.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 28 May 2023 <a href="#id-28-may-2023" id="id-28-may-2023"></a>

**(ARM v22.2.28)**\
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

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

**(ARM v22.2.27)**\
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

#### 14 May 2023 <a href="#id-14-may-2023" id="id-14-may-2023"></a>

**(ARM v22.2.26)**\
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

#### 07 May 2023 <a href="#id-07-may-2023" id="id-07-may-2023"></a>

**(ARM v22.2.25)**\
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

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

**(ARM v22.2.23)**\
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

#### 19 March 2023 <a href="#id-19-march-2023" id="id-19-march-2023"></a>

**(ARM v22.2.22)**\
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

#### 12 March 2023 <a href="#id-12-march-2023" id="id-12-march-2023"></a>

**(ARM v22.2.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Static Code Anaysis** was failing due to missing property tag in **Apex PMD** rules file, but the UI log wasn't displaying this error ([#63554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101980029)).
* Fixed an issue where when there was no results generated, the report displayed an error that there are zero metrics instead of displaying the results as zero in all the places when there is no change ([#63272](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101591692)).
* Fixed an issue where user was unable to deploy a CI job with the **RelationshipGraphDefinition** components ([#64145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102836208)).
* Fixed an issue where **Validate** deployment was displayed as **failed** in UI and the database, but was successful as per the logs ([#63868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102596005)).
* Fixed an issue with **Review Artifact** where similar custom fields from different objects were not populating correctly and switching to other fields ([#63676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102181836)).
* Fixed an issue where multiple fields of the respective custom objects were getting selected parallelly while performing **edit** or **save** or **exit** operations on the **Review Artifact** screen (internal ticket).
* Enhanced ARM by adding an option for **multiple ARM instances** to share a **single database cluster** (internal ticket).

#### 05 March 2023 <a href="#id-05-march-2023" id="id-05-march-2023"></a>

**(ARM v22.2.20)**\
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

#### 26 February 2023 <a href="#id-26-february-2023" id="id-26-february-2023"></a>

**(ARM v22.2.19)**\
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

#### 19 February 2023 <a href="#id-19-february-2023" id="id-19-february-2023"></a>

**(ARM v22.2.18)**\
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

#### 12 February 2023 <a href="#id-12-february-2023" id="id-12-february-2023"></a>

**(ARM v22.2.17)**\
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

#### 05 February 2023 <a href="#id-05-february-2023" id="id-05-february-2023"></a>

**(ARM v22.2.16)**\
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

#### 29 January 2023 <a href="#id-29-january-2023" id="id-29-january-2023"></a>

**(ARM v22.2.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment was failing with the following error when user was deploying **Permissionset** with a user-permission **Manage Public Documents**: `Permission Manage Public Documents depends on permission(s): Create Document, Delete Document, Edit Document, Read Document` ([#60597](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097399881)).
* Fixed an issue where CI jobs were failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#59050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095999076)).
* Fixed an issue where **Reports** deployment validation failed in **EZ-Merge** but was successful in **EZ-Commit** and **Deployment** modules ([#57714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093587003)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Fixed an issue where user initiated the prevalidation commit by enabling the destructive type but the deployment failed with an error `null` at **Diff** ([#59919](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096907001)).
* Fixed an issue where **Validate Deploy** failed in **QuickMerge** and displayed the following message: `This folder unique name already exists for this folder type or has been previously used. Please choose a different name` (internal ticket).
* Fixed an issue where CI job wasn't considering the metadata changes, so the destructive changes were not being prepared or displayed on the build. (internal ticket).

#### 22 January 2022 <a href="#id-22-january-2022" id="id-22-january-2022"></a>

**(ARM v22.2.14)**\
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

#### 15 January 2022 <a href="#id-15-january-2022" id="id-15-january-2022"></a>

**(ARM v22.2.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556)).
* Fixed an issue with user received 6 notifications for a failed **CI Job** instead of 1 ([#58436](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095199003)).
* Fixed an issue where user was trying to register branches to AutoRABIT through GitHub, but was getting the following error: `Lower Region` ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed a recurring issue where **Commits** and **Merges** were slowing down at a particular step, and **EZ-Merge** was failing with an error at commit phase ([#51268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085726862)).
* Fixed an issue where while performing destructive changes in **EZ-Commit**, it was creating **package.xml** in root path folder in **SFDX** structure ([#57868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093790001)).
* Fixed a UI bug on **CI List** and **CI Results** pages where when pagination was changed, the first 25 records were repeated (internal ticket).
* Fixed an UI bug where the **LastUsedDate** column was not displayed in the **Branch Table** (internal ticket).

#### 8 January 2022 <a href="#id-8-january-2022" id="id-8-january-2022"></a>

**(ARM v22.2.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189)).
* Fixed a build bug where **CI Job Build** was failing during package preparation **step 5** failing while commiting **DecisionMatrixDefinition** and throwing an error ([#58376](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095049142)).
* Fixed an issue with **Branching Baseline** where the developers were migrating the changes from dev branch to INT, but **Diff** was showing 100% addition which is incorrect\
  ([#58478](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095251543)).
* Fixed an issue where generating **Diff** for a **Commit Label** was taking much longer than expected ([#55220](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591780)).
* Fixed an issue where **Code coverage** job was running **4 hours** earlier than scheduled every time services were restarted ([#54837](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088878005)).
* Fixed a UI bug where scrollbar and pagination were not visible on the **Org Sync History** page (internal ticket).

#### 01 January 2022 <a href="#id-01-january-2022" id="id-01-january-2022"></a>

**(ARM v22.2.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Deployment** was failing with **no changes** in the package (internal ticket).
* Fixed an issue where user was unable to create **Environment Provisioning** templates for multiple component types ([#57898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093797903)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).
* Fixed an issue where AutoRABIT **SSH credentials** were failing with an error `Auth failed` while trying to connect with **AWS CodeCommit** ([#53694](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087714369)).
* Fixed an issue where **EZ-Commit Diff** was taking approximately 4 hours while **Refactoring CustomField**, which is much longer than expected ([#56650](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091636348)).
* Fixed an issue where **ExternalCredential** metadata type was not getting excluded even when user added it in the **excluded lists** in **CI Configuration** (internal ticket).
* Fixed an issue where after triggering **Branching baseline**, standard value set metadata type was getting displayed under the **deleted components** through **Autodraft** for **Non-DX repo** (internal ticket).
* Fixed an issue where **Destructive Components** are not seen in case of **PV-DX-Destructive Merge** for **Report** metadata type. Instead, it displaying a message: `Package is empty` (internal ticket).

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

**(ARM v22.2.10)**\
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

#### 18 December 2022 <a href="#id-18-december-2022" id="id-18-december-2022"></a>

**(ARM v22.2.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DataLoader Pro** where jobs executed in the last 6 months were not showing in the database process table and in the **Reports** module ([#53980](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087981132)).
* Fixed an issue with **Deploy SFDX Source With ALM Mapping** where CI job with ALM Mapping was not working as expected for Team which is not default ([#55995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091129007)).
* Fixed an issue where **Profile Diff** is working as expected for **Selective Deployment**, but not while using the same profile in the profile manager ([#52868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087005140)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189), [#55754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090487029)).
* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).

#### 11 December 2022 <a href="#id-11-december-2022" id="id-11-december-2022"></a>

**(ARM v22.2.8)**\
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

#### 04 December 2022 <a href="#id-04-december-2022" id="id-04-december-2022"></a>

**(ARM v22.2.7)**\
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

#### 27 November 2022 <a href="#id-27-november-2022" id="id-27-november-2022"></a>

**(ARM v22.2.6)**\
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

#### 20 November 2022 <a href="#id-20-november-2022" id="id-20-november-2022"></a>

**(ARM v22.2.5)**\
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

#### 13 November 2022 <a href="#id-13-november-2022" id="id-13-november-2022"></a>

**(ARM v22.2.4)**\
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

#### 06 November 2022 <a href="#id-06-november-2022" id="id-06-november-2022"></a>

**(ARM v22.2.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DX CI Job** where user selected **Do Not Include Skip Members** but the respective mapper reports were not skipped (internal ticket).
* Fixed an issue where the **Deployment** module page was loading very slowly and then throwing an error: `Page Unresponsive` ([#53675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704191)).
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

#### 30 October 2022 <a href="#id-30-october-2022" id="id-30-october-2022"></a>

**(ARM v22.2.2)**\
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

#### 23 October 2022 <a href="#id-23-october-2022" id="id-23-october-2022"></a>

**(ARM v22.2.1)**\
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

#### 16 October 2022 <a href="#id-16-october-2022" id="id-16-october-2022"></a>

**(ARM v22.2.0)**\
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
