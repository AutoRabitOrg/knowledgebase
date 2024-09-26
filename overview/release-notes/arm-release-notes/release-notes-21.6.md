# Release Notes 21.6

**November 2021 - Version 21.6 - New Features, Enhancements, Improvements, and Changelogs**

**Date of Release:** _21 November 2021_

\


**On this page:**

1. [New Features](release-notes-21.6.md#new-features)
2. [Enhancements](release-notes-21.6.md#enhancements)
3. [Improvements](release-notes-21.6.md#improvements)
4. [Changelogs](release-notes-21.6.md#changelogs)

### New Features <a href="#new-features" id="new-features"></a>

#### Pull Request Support for Azure DevOps <a href="#pull-request-support-for-azure-devops" id="pull-request-support-for-azure-devops"></a>

Pull request is a feature that allows you to review code and provide feedback before merging it into the master branch. Previously, we had GitHub and Bitbucket support. We've included support for Azure DevOps in this release. ([Learn More](../../../product-guides/arm/arm-features/version-control/external-pull-request/pull-request-support-for-azure-cloud.md))

* During **Ez-Commit** and new **Pull Requests**, you can now create a Pull Request in Azure with the assignee.
* You should be able to choose the repository, the base branch, and another branch to compare during the creation of a pull request.
* A link to the Azure DevOps application will be included in each pull request created in AutoRABIT. The pull request can also be approved directly from the AutoRABIT application.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### Audit Log Report <a href="#audit-log-report" id="audit-log-report"></a>

AutoRABIT had an audit report feature that gave you a comprehensive view of your business operations by fostering a collaborative operational audit environment. In this release, we've made some enhancements and added a button called **"Audit Log Report"** on the CI job page, which allows you to generate a report in PDF format for a specific period.

* We've improved the **CI Job Result** screen by giving users the option to generate an Audit log report for internal auditing purposes. This is a report of CI jobs deployments and the commits associated with each deployment, including commit details such as Author, Commit Time Stamp, and so on.
* We changed the timestamp in the Audit log report from **12-Hour** format to **24-hour UTC** format by default to comply with ISO 8601 notation, which is a commonly recommended format for representing date and time.
* Added support for custom _“keynames”_, _“Salesforce Org type“_ and _“AR SF Org type”_ in the Audit trail report wherever Salesforce org name details are applicable.

#### **Salesforce CLI Upgrade** <a href="#salesforce-cli-upgrade" id="salesforce-cli-upgrade"></a>

Salesforce CLI is a command-line interface for working with your Salesforce org that makes development and build automation easier. It can be used to create and manage organizations, synchronize sources to and from organizations, create and install packages, and more. In this version of ARM, Salesforce-DX CLI is upgraded to the latest **7.129** version.

#### **Salesforce Winter (API 53) Support** <a href="#salesforce-winter-api-53-support" id="salesforce-winter-api-53-support"></a>

In order to keep our product up to date with the most recent Salesforce updates. AutoRABIT now supports the most recent **API version 53** in this release. Now our Salesforce developers will begin using API 53 on their Sandboxes for development. The most recent API version is intended for customizing the metadata model and developing tools to manage it.

### Improvements <a href="#improvements" id="improvements"></a>

#### Platform Improvements <a href="#platform-improvements" id="platform-improvements"></a>

* We've been working hard over the last few weeks to improve our platform's stability, performance, query optimizations, code smells, security vulnerabilities, and reliability. With this release, you will notice significant improvements in our application, such as faster page load times, improved performance, and faster search functionality, among other things.
* **JQuery Upgrade**: JQuery was updated from version **1.8.3** to version **3.6**. Upgrading to the most recent version of jQuery makes our application more secure, as well as potentially faster in terms of script execution and loading.

#### **UI Improvement** <a href="#ui-improvement" id="ui-improvement"></a>

Across the CI Job module, **"Load More"** buttons have been replaced with **"Previous"** and **"Next"** buttons. This new feature will allow our users to display 25, 50, 75, or 100 records on a single page and navigate between pages using the Previous and Next buttons. This feature was previously limited to the Version Control module, but it has recently been expanded to include the CI Job module as well.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 11 Mar 2022 <a href="#11-mar-2022" id="11-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to deploy release labels ([#40600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068395530)).
* Fixed the following SSO errors:
  * Unable to use SSO for AutoRABIT authentication ([#37767](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062637173)).
  * Unable to log in via SSO in the chrome and the firefox browser.
  * Fixed "**domain name does not exist**" error ([#41853](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070865403)).
* Fixed a bug where users were getting an undefined error for the standard templates while editing the CI job.
* Fixed an issue where the status of the AutoRABIT ExternalId field was showing as processing, but it was marked as completed in the log report ([#40669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068569430)).
* Fixed a bug that restricted users from using Dataloader Pro's **Auditable Standard** field feature ([#40794](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068711163)).
* Fixed an issue where the users were unable to replace attachment records in the destination org.
* Fixed an issue where the attachments were not completely deployed in the target environment ([#41208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069667003)).
* Fixed an issue where users were unable to deploy the nCino feature from org to org using the **nCino-Forms** **standard template** ([#38764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065055277)).
* Fixed an issue where the users were unable to **stop/delete** the dataloader running jobs ([#39556](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066791149)).
* Fixed an issue where the users when attempting to initiate the deployment, were failing with the **"Failed to initiate deployment request"** error ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to perform the branching baseline operation ([#41622](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070417055)).
* Fixed an issue where the users were not able to configure the approver's lists on the **New Merge Request** screen ([#41844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070874003)).
* Fixed an issue where the users trying to revert a commit for a commit label was getting failed ([#39613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066805855)).

#### 06 Mar 2022 <a href="#06-mar-2022" id="06-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option was not working when users use the EZ-Commit/merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for the EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 Feb 2022 <a href="#27-feb-2022" id="27-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** on the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the excluded metadata types on the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for the Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).
* Fixed an issue where the users when trying to start a deployment, it was getting failed with the "**Failed to start deployment request** error" ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to revert the commits using AutoRABIT ([#39957](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067378384)).
* Fixed an issue where the users were not able to use the "**Files Changed**" functionality on the **Merge Request History** page ([#41456](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070069155)).
* Fixed an issue where the users were unable to delete the changes made in the version control branch via AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed a bug that prevented users from performing commit and merge operations in AutoRABIT ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where the external objects with lookup relationships were not getting displayed under the child objects in the Dataloader Pro ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed an issue where the users were unable to update the "**Validation checks**" status from the in-progress state to the completed state.
* Fixed an issue where changes from multiple package directories were not being retrieved without selecting a package directory.
* Fixed an issue where the users were unable to attach the CSV file while carrying out the CI deployment.
* Fixed an issue that caused users to receive an invalid session error when changing their password.

#### 20 Feb 2022 <a href="#20-feb-2022" id="20-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to see the commits ID in the release label ([#41284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069797001)).
* Fixed an issue where the users were unable to view their permission details in the Users and Roles tab ([#41043](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069219179)).
* Fixed an issue where users were not able to delete the changes made in the source branch using AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed an issue where the branching baseline for a profile and branch to branch merge was not working ([#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* There was an AutoRABIT performance issue that caused searching for revisions, validations, and commits to taking a long time. It has now been fixed ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where users were not able to commit their changes to the branch ([#39269](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066103022)).
* When users attempted to update changes in the target org using the profile manager, the deployment getting failed. It has now been fixed ([#40599](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068421379)).
* Fixed an issue where users were unable to switch from a credential-based login to an SSO-based login ([#40871](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068784190)).
* AutoRABIT instances were not supporting the Salesforce API 54 version. It has now been fixed. ([#40921](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068957023)).
* When a user performs a pre-validation commit on the Azure repository branches, it creates a duplicate external commit with the same revision ID. This issue has now been fixed ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).

#### 13 Feb 2022 <a href="#13-feb-2022" id="13-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **"Group By"** functionality was not fetching the correct CI job results ([#38870](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069460109)).
* Fixed an issue where the deployment status of CI Job has failed in logs but the process is still in-progress stage ([#40805](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068697958)).
* Fixed an issue where the users were unable to use the SCA for LWC components unlike apex class, triggers, and aura bundle ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* When a pull request is in progress, the job is not triggered for additional changes committed before the work is completed. This is now fixed ([#38877](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065276358)).
* Fixed a bug where the users were facing challenges while merging the entire branch changes to the target environment ([#39451](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066611145)).
* Fixed an issue where the File Diff shows full component (especially Aura, LWC components) as a change instead of delta changes ([#39351](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066320276)).
* Fixed a bug where the sub-users without admin privileges were able to export and download the org users' data from **Admin > Users** section.
* Fixed an issue where the dataloader pro throws the error **"Error creating output directory: configs"** while uploading data from one environment to another ([#40832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068736307)).
* Fixed an issue where the external object-related lookups were unable to verify the relationship associated with the external objects in the destination org ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed a minor user-interface bug where the users were unable to find the **Resolve Conflict button** to resolve the merges conflict. This is now resolved.

Limitations identified in this release:**RestrictionRule** metadata type is not supported for the SFDX deployment.

#### 06 Feb 2022 <a href="#06-feb-2022" id="06-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed the below UI issues:
  * The **"Commit"** button was not available for the merge request label job. ([#38876](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065275014)).
  * For the entire deployment, the **"To Revision"** radio button was disabled, and users were unable to select revisions from the list provided.
  * Although the field **"Timezone"** was mandatory upon signup, the users were able to proceed without picking a timezone.
* Fixed an issue where the admin was unable to assign permissions to its sub-users. This is now working as expected ([#40017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067565003)).
* Fixed an issue where the validation rule automation was not working for the **Environment Provisioning** module ([#41035](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069198519), ([#40991](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069108736)).
* Fixed an issue where the dataloader pro job is not able to load data for objects with fields exceeding limits([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the users were unable to register the existing branches to AutoRABIT ([#40894](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068809067)).
* Fixed an issue where the EZ-Merge was showing status as failed in the AutoRABIT application however, in the Salesforce environment the status shows as success ([#40673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068536502)).
* Fixed a bug where the users were unable to register a dev hub on the **SDFX > Hub Management** page.

#### 30 Jan 2022 <a href="#30-jan-2022" id="30-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 29 Jan 2022 <a href="#29-jan-2022" id="29-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 23 Jan 2022 <a href="#23-jan-2022" id="23-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to generate the code coverage log report from the **Report** Module ([#38717](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939344)).
* Fixed an issue where the users were unable to upload the package.xml file to resolve the merge conflict ([#39960](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067372236)).
* Fixed an issue where the users were able to commit the changes although the validation got failed. ([#38228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775343)).
* Fixed an issue where the user was unable to perform the **Enable/Disable validation rule** on the Managed package object using the environment provisioning functionality ([#40297](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068017532)).
* Fixed a bug where the user was unable to deploy the **Email Template** on their target environment ([#40241](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067922013)).
* Fixed an issue where users were unable to upload/migrate the knowledge articles from one sandbox to another sandbox ([#37922](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063030291)).
* Fixed an issue where the users were facing the **"Null Pointer Exception"** error during the merge prevalidation process.
* Fixed an issue where If the users picked all the conflicted files during a merge request, they would receive an error message saying **"Please click on any conflicted file."**
* Fixed an issue where the users were unable to find the log report for the newly created branch in AutoRABIT.
* Fixed an issue where the users were unable to find out the work item statuses during the deployment process for the unlocked packages.
* **ALM Enhancements:**
  * Added a new section called **"ALM Management"** to the **Admin** module for merge requests
  * Detailed information on all of your ALM's active and inactive sprints.
  * Smart commits to reading the comment in a revision associated with your ALM story.
  * We have introduced the **ALM Details** section that lists the work items linked with the commits along with the existing and post-merge status.
  * Ability to keep the work item status without a change or update it during EZ-Commit.
  * You may now configure the job to pick up revisions based on your work item status while deploying from version control to a Salesforce org, allowing you to adjust the status even after a successful rollback.

#### 16 Jan 2022 <a href="#16-jan-2022" id="16-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 09 Jan 2022 <a href="#09-jan-2022" id="09-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 02 Jan 2022 <a href="#02-jan-2022" id="02-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI Job builds are getting stuck and no log information was displayed ([#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed an issue where the conflicted files downloaded were incorrect during the merge process ([#39364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066317317)).
* Fixed an issue where the aura components were not getting retrieved while carrying out the branching baseline operation ([#38610](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064710558)).
* Fixed a bug that restricted users from entering the credential name on the **"Create Credential"** screen because the field was disabled.
* Fixed a bug where the super administrator was getting an empty popup screen when navigating to the **Process Summary** page.
* Fixed an issue where the users were able to find the **Abort** option even when the CI Job had been completed successfully ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463)).

#### 26 Dec 2021 <a href="#26-dec-2021" id="26-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as the parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 19 Dec 2021 <a href="#19-dec-2021" id="19-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 12 Dec 2021 <a href="#12-dec-2021" id="12-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when the user is trying to perform pre-validation commit for report metadata, it is getting added under emailservice functions in diff report ([#37925](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063067009), [#38581](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064666105), [#38880](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065272149), [#38734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064981980)).
* Fixed an issue where the case _entitlementProcess-meta.xml_ files were not picked up during deployment ([#39069](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065734191), [#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed an issue where the deployment report is getting failed while doing prevalidation merge with the report folder.
* Fixed an issue where users were unable to retrieve a package which has more than 1000 components ([#38737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064985007)).
* Fixed a bug where a null pointer exception was thrown while loading in Dataloader Pro ([#38286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063928003)).
* Fixed an issue where the entitlement process is getting removed from Package.xml ([#39097](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065777009)).
* Fixed an issue where the external commits did not show up on the release label ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed a bug that displays the wrong statuses in the test reports ([#39008](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065572975), [#38986](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564303)).
* Fixed an issue where the code coverage percent is not available in the case of SFDX merge operation.
* Fixed an issue where the dataloader pro jobs were not able to load data for objects with fields exceeding 800 ([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the code coverage percentage shows as 0 in the UI logs even after deployment validation is passed.
* Fixed a bug where the changes are being committed even after a failed validation.
* Fixed an issue where the package directory filter in the release labels is not working as expected.

#### 05 Dec 2021 <a href="#05-dec-2021" id="05-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when pre- and post-destructive changes were added to the process, it caused the deployment to fail ([#38330](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064040175), [#38721](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064967175)).
* Fixed a bug where for fewer CI jobs, the **Older** button was disabled. This has now been enabled and is working as expected ([#39050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065702042)).
* Fixed an issue in the SFDX module that prevented commits from being executed using scratch org ([#38789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076258)).
* Fixed an issue where the external commits were not displayed when creating release labels or merging single revisions. This is now working as it should ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed an issue where users were unable to run SCA within the reports module due to an error stating **"Invalid mapping credentials."** In addition, the number of issues indicated in the Ez-commit process does not match the CodeScan analysis ([#38917](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065373386)).
* Fixed a bug where single dataloader jobs couldn't be edited and there was a mapped field cache issue ([#38753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065026084)).
* Fixed an issue where the alm mapping details for the scratch org with alm configuration could not be found.
* While executing scratch org alm commit with skip mapping set to false, the current ALM work item status was reporting _"empty"_ results. This is now fixed.
* Fixed a bug that allowed users to save multiple criteria rows with the same priorities for ApexPMD.
* Fixed an issue where the repository filter on the _Commit History_ screen was reset to default after resolving a conflict.
* Fixed a bug where the failed component count position is wrong when the window is scrolled.

#### 28 Nov 2021 <a href="#28-nov-2021" id="28-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed nCino objects deployment issue during using nCino CI Jobs ([#39375](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058591003)).
* Fixed an issue where the custom object is being listed during CI Job operation but not during Ez-commit ([#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed Ez-merge issue which shows different results in AutoRABIT when compared to the production environment ([#38831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065181230)).
* Fixed an issue where the users were unable to extract deleted records and threw **"Malformed Query Fault"** error ([#38448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064441154)).
* Fixed an issue where the pull request support with BitBucket was not working properly. This is now fixed ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed a bug in the merge request and pull request validation builds which were unable to list the changed components whereas the CI Job build was able to pick them up ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017), [38713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064936484)).
* Fixed an issue where the org administrator was unable to assign hub level permissions to its sub-users ([#38898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065336005)).
* Fixed wrong metadata identification for deletion issue ([#37703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062453147)).
* Fixed an issue where the user was unable to update **"Configuration For recordTypes picklistValues"** ([#38901](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065355005)).
* Fixed API version error in the CI Job screen ([#36550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059178003)).
* Fixed CI build failing issue ([#38630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064788278)).
* Fixed EZ-Commit issue where the file diff was throwing an error due to credential scope issue ([#38950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065446001), [38795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065077341)).
* Fixed an issue where duplicate entries were seen while creating release labels ([#37300](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061440253)).
* Fixed a bug where the user was unable to click on the **OK** button on the **Merge Request History** screen ([#38781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085003)).
* Fixed an issue where the **"include delete records"** checkbox is de-selected automatically during editing the dataloader extract job.
* Fixed an issue where the scratch org permissions are not visible on **"hub level permissions"** and _"_**scratch org permissions"** screens.
* Fixed Ez-commit issue where a sub user with only one repository registered with AutoRABIT, is not able to find/select his repository in the **EZ-Commit** screen.
* Fixed an issue where the repository filter is reset to default during the conflict resolve flow.
* Fixed registering the branch issue when the branch registration crossed 100 limits in AutoRABIT.
* Fixed a bug where the parent checkbox in the download zip for CI Job is not working as expected.
* Fixed wave-dependent missing files from the package during the prevalidation merge operation.
* Fixed an issue where the non-SFDX CI job for WaveTemplates is showing no modifications when triggered.
* Fixed single dataloader and dataloader pro filter issues while carrying out the edit functionality.

#### 21 Nov 2021 <a href="#21-nov-2021" id="21-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the quick deployment feature was not working as expected and was throwing **"Invalid Login"** error ([#37802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062709159)).
* Fixed a bug where the merge request validation was getting failed ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017)).
* Fixed an issue where the commit search was not working as expected in the **Version Control** module ([#36548](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059165111)).
* Fixed an issue where the users were facing invalid credentials issue while updating the src as metadata folder path in-branch settings **(Admin > VC' Repos)** ([#38727](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939824)).
* Fixed an issue where the pull request support for BitBucket was not working properly as expected ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed an issue where the deployment shows failed status although there are no failures and the items did get moved to the destination org. This is now working as expected ([#37774](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062644015), [#38363](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064201151)).
* Fixed an issue where the user was not able to retrieve the metadata to deploy the changes using AutoRABIT's deployment feature.
* Fixed dataloader pro issue which was throwing unknown error while migrating the data objects ([#38566](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064649001)).
