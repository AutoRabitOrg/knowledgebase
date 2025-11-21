---
hidden: true
---

# Release Notes 22

## ARM Release Notes 22.3

We would like to inform you about the End of Life (EOL) for ARM version 22.3. Per our support agreement, this version is now more than 365 days old and is no longer supported. As part of our ongoing commitment to providing the best possible experience for our users and maintaining the highest standards of security and performance, we have made the decision to discontinue support for ARM 22.3.

**End of Life Date: April 1, 2024**

What Does This Mean?

* End of Support: As of April 1, 2024, we will no longer provide maintenance updates, bug fixes, or technical support for ARM 22.3. This includes both security and non-security updates.
* Security Risks: Continuing to use ARM 22.3 after the end of support date may expose your system to potential security vulnerabilities, as we will no longer release security patches.
* Upgrade Recommendations: We strongly recommend migrating to a supported version of ARM to ensure continued reliability, security, and performance. Our team is available to assist you with this transition process and provide guidance on your upgrade.
* Accessing Resources: While official support for ARM 22.3 will no longer be available, you can still access existing resources such as documentation, knowledge base articles, and the Knowledge Hub for reference purposes.

Action Required:

To mitigate any potential risks associated with the EOL of 22.3, we urge you to take proactive steps towards upgrade immediately. Our customer success and support team are here to assist you every step of the way. Please reach out to your CSM to plan this work.

We understand that this transition may present challenges, and we sincerely apologize for any inconvenience it may cause. However, we believe that focusing our efforts on our latest offerings will ultimately benefit you with enhanced features, improved performance, and better security.

Thank you for your understanding and continued support.



**December 2022 - Version 22.3 - New Features, Enhancements, Improvements and Changelogs**

**Date of release:** _18 December 2022_\
**Article last updated:** 31 _July 2023_

### New Features <a href="#new-features" id="new-features"></a>

#### 1. Retention Policy <a href="#id-1-retention-policy" id="id-1-retention-policy"></a>

You can now define a data **Retention Policy** and choose how much data should be stored for how long. ARM will now be considerably quicker by eliminating outdated data. Clearing out old and useless data from the database and moving it to the archives keeps the application from underperforming and improves speed across all modules.

A weekly clean-up will ensure that the application runs smoothly. The default data retention period is set as 12 months which will be implemented with the release of **ARM version 22.3**. Admins can specify the duration of data retention in the history tables from the My Account section and change the retention period from **12 months** to **6 months** or **3 months**.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings.md)

#### 2. Search, Group, and Filter CI Job List <a href="#id-2-search-group-and-filter-ci-job-list" id="id-2-search-group-and-filter-ci-job-list"></a>

Finding a **CI Job** has never been easier. Instead of scrolling through endless pages, you can search for a job or a group by simply typing the name in the new dropdown lists. You can further narrow the search results by combining these two options to look for a particular job within a group.

Additionally, the **filter** feature provides further options to narrow the search results by source type, date range, and more.\
[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-list.md)

#### 3. Ability to Abort a Vlocity Deployment <a href="#id-3-ability-to-abort-a-vlocity-deployment" id="id-3-ability-to-abort-a-vlocity-deployment"></a>

We just included new functionality to the **ARM 22.3 version** that allows users to terminate an ongoing Vlocity deployment process or abort it if get stuck. The **Deployment History** screen contains the **Abort** option, which allows you to terminate the deployment process.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-I1GT03M7.png)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Release Label Revamp <a href="#id-1-release-label-revamp" id="id-1-release-label-revamp"></a>

The revamp of the **Release Label** page is the feature of version 22.3 that stands out the most. This enhancement is actually a collection of multiple smaller enhancements, each of which is briefly discussed in this section.

* While creating a release label, you can choose the specific period for which you want to retrieve the **commit history** instead of loading the entire commit history, which could take a really long time.
* You can also create a release label while simultaneously creating a **package** simply by selecting a conveniently located checkbox on the same screen.
* The **selected revisions** are also displayed on the same screen and updated dynamically as you select/unselect revisions.
* Release labels are **color-coded** on the **Release Label Summary** screen for easier identification, and the search now provides leaner results.

[**Read more →**](../../../product-guides/arm/arm-features/version-control/change-labels/release-labels.md)

#### 2. Additional Metadata Support in Search and Substitute <a href="#id-2-additional-metadata-support-in-search-and-substitute" id="id-2-additional-metadata-support-in-search-and-substitute"></a>

Additional metadata types are now compatible with the **Search and Substitute** rule, allowing the application to use them for Deployments and Commits.

Until now, the Search and Substitute functionality only had the ability to select a metadata type and then perform the search for substrings across all members in that type. But now, you can select specific metadata members in a type and substitute values for that member(s).

This enhancement is also helpful when users want to add object permissions only to the production and not to the lower sandboxes.

It is also beneficial to have this feature so that the rules can be created and used in **CI Jobs** to do the replacements automatically, depending on the deployment settings in the CI Job.\
[**Read more →**](../../../product-guides/arm/arm-administration/search-and-substitute.md)

#### 3. Additional details in the Users Export List <a href="#id-3-additional-details-in-the-users-export-list" id="id-3-additional-details-in-the-users-export-list"></a>

**Export List** is a comprehensive list of all registered users with an organization. This list can be downloaded from the **Users** module. It includes details like the users' name, email, and title; and information about user accounts created, modified, deactivated, and deleted.

With the recent release, the **Export List** will include a few additional details related to the **last login** to ensure security and compliance. Details like the **location, login type, IP address, coordinates,** and the **browser** used.

The access level of users is not mentioned in the export list for security reasons, i.e., if any users are **Admin** or **Super Admin**, this will not be specified. The company can share this list, if required, with people both inside and outside their organization without jeopardizing the confidentiality of the access granted to the users.\
[**Read more →**](../../../product-guides/arm/arm-administration/user-management/users-roles-and-permissions.md)

#### 4. Dataloader Clone process <a href="#id-4-dataloader-clone-process" id="id-4-dataloader-clone-process"></a>

In addition to providing a new name, **Dataloader users** can now specify a different Salesforce org as a source or destination for the operation while cloning an existing job. This helps the users to reuse the same job configuration with a different Salesforce org without going through the entire process again.

For the **Extract** operation, users have the option to edit the query corresponding to the new org selected. For **Insert/Update/Upsert/Delete** operations, users have the option to upload a different **.CSV** file instead of the original one. Validation is done to verify whether the object is available in the new org and also if the user edits the query for the cloned process.\
[**Read more →**](release-notes-22.3.md#4-dataloader-clone-process)

***

### Improvements <a href="#improvements" id="improvements"></a>

* The `/syncbranchcommits` service is no longer supported. The users will no longer require **Auto-sync** functionality to create a release label. This simplifies the function's use and gets rid of unnecessary steps.
* For improved user experience, the **metadata.zip** file upload option has been added to the **New Deployment** page itself. When uploading large files, this is extremely useful.
* The **password policy** is reduced from **13** previously used passwords not being allowed to **5** previously used passwords. This gives users more options while resetting their passwords after the **three months** period or if they forget their password.
* Improvements have been made to **VC Repo flow** as well as to **Salesforce Org flow**. You can now run scans on a repo or an org to be tagged to the same project and run comparisons so that you have traceability across the scans. The comparison feature allows for every delta scanned to be compared with the baseline. Scans are run on the source, and the results are available in the **Reports** module. Users can trace the jobs run using the unique identifier.\
  Click [HERE](../../../product-guides/arm/static-code-analysis.md) to see a few points to note about these improvements.
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

#### 28 February 2024

**(ARM v. 22.3.55)**

| Module                                 | Summary                                                                                    | Fix Version                 | Resolution                       | Cause                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------- | -------------------------------- | ------------------------------- |
| <p> </p><p>Version Control</p><p> </p> | Merges are not being fetched when trying to create a release label for Vlocity components. | <p> </p><p>22.3</p><p> </p> | <p> </p><p>Code Fix </p><p> </p> | <p> </p><p>Use Case</p><p> </p> |
| Version Control                        | Unable to Commit the Action Overrides in Service Appointment Object                        | 22.3                        | Code Fix                         | Use Case                        |

#### 28 January 2024

**(ARM v. 22.3.54)**

<table data-full-width="false"><thead><tr><th width="130">Module</th><th width="247">Summary</th><th width="113">Status</th><th width="77">Fix Version(s)</th><th width="93">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployment</p><p> </p></td><td>Vlocity Deployment issue</td><td><p> </p><p>QA Passed</p><p> </p></td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Not fetching merges when trying to create a release label for Vlocity components</td><td>QA Passed</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 21 January 2024

**(ARM v. 22.3.53)**

<table data-full-width="true"><thead><tr><th width="151">Module</th><th width="206">Summary</th><th>Status</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue while deploying promotions from QAT to PRD the rule set criteria is compressing the value while deploying it to RD<br><br></td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr><tr><td><p> </p><p>Dataloader Pro</p><p> </p></td><td>Issue on Feature Deployments</td><td>QA Passed</td><td><p> </p><p>22.3<br> 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td>Use Case</td></tr></tbody></table>

#### 14 January 2024

**(ARM v. 22.3.52)**

<table data-header-hidden><thead><tr><th width="128">Module</th><th width="313">Summary</th><th width="90">Fix Version(s)</th><th width="111">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>MODULE</td><td>SUMMARY</td><td>FIXVERSION</td><td>RESOLUTION</td><td>CAUSE</td></tr><tr><td> Admin</td><td><p> </p><p>After baselining the branch, it did not pull all metadata for development.</p><p> </p></td><td>22.3</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td> Deployments</td><td>Deployment status failed when deploying Vlocity components</td><td>22.3 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

**10 December 2023**

**(ARM 22.3.51)**

<table data-full-width="true"><thead><tr><th width="118">Module</th><th width="263">Summary</th><th width="111" align="center">Version(s)</th><th width="130" align="center">Resolution</th><th align="center">Cause</th></tr></thead><tbody><tr><td> nCino</td><td>User is unable to do nCino Feature Deployments <br>* Requires documentation</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Admin</td><td>Getting ‘null parameters’ error when clicking on save in the user’s section.</td><td align="center"><p> </p><p>23.1, 22.3</p><p> </p></td><td align="center"><p> </p><p>Code Fix</p><p> </p></td><td align="center"><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 3 December 2023

**(ARM v. 22.3.50)**

| Module      | Summary                                                                                                  | Fix Version(s) | Resolution                  | Cause    |
| ----------- | -------------------------------------------------------------------------------------------------------- | -------------- | --------------------------- | -------- |
| Admin       | Issue adding user mapping                                                                                | 22.3, 23.1     | Code Fix                    | Use Case |
| Admin       | nCino View Object Failing                                                                                | NA             | No Code Fix - Added Loggers | Data     |
| Deployments | Org sync not completing                                                                                  | NA             | No Code Fix - Added Loggers | Data     |
| Dataloader  | Corrected a spelling mistake in ARM steps.                                                               | 23.1, 22.3     | Code Fix                    | Use Case |
| Dataloader  | Corrected data seeding error preventing upsert                                                           | 23.1, 22.3     | Code Fix                    | Use Case |
| nCino       | On-premise testing: CI Job with template option failed due to "data and metadata retrieval failed” error | 23.1, 22.3     | Code Fix                    | Use Case |

#### 26 November 2023

**(ARM v. 22.3.49)**

<table data-full-width="true"><thead><tr><th width="120">Module</th><th width="327">Summary</th><th width="140">Fix Version(s)</th><th width="124">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>CI Jobs</p><p> </p></td><td>Post activities, particular job status showing as FAILED in ARM even job execution completed with succeed</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Getting empty Configuration under "Configure Default SCA Baseline Branches"</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr><tr><td><p> </p><p>Admin</p><p> </p></td><td>Able to view empty role under permissions</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 19 November 2023

**(ARM v. 22.3.48)**

<table><thead><tr><th width="121">Module</th><th width="283">Summary</th><th width="101">Fix Version</th><th width="105">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td><p> </p><p>Deployments</p><p> </p></td><td>In sub-user, unable to get the branch in Salesforce Org Mappings section in SF Org Management screen if Admin user given only admin module permission.</td><td><p> </p><p>22.3</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>Deployments</p><p> </p></td><td>Deployment tab - Redeploy/Promote issue</td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td>Added Loggers</td><td><p> </p><p>Data</p><p> </p></td></tr><tr><td><p> </p><p>nCino</p><p> </p></td><td>Unable to create Feature Migration Template on Debt Schedule object</td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td><p> </p><p>All Modules</p><p> </p></td><td>Invalid Email ID</td><td>22.3, 23.1</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 15 November 2023

<table><thead><tr><th width="118">Module</th><th width="279">Summary</th><th width="107">Fix Version</th><th width="108">Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>Deployments</td><td>Page unresponsive in new deployment for "previous deployment" as source type</td><td>22.3</td><td>Code Fix</td><td>Use Case</td></tr></tbody></table>

#### 12 November 2023

**(ARM v. 22.3.47)**

<table><thead><tr><th width="109">Module</th><th width="240">Summary</th><th width="136">Fix Version(s)</th><th width="120">Resolution</th><th width="100">Cause</th></tr></thead><tbody><tr><td>nCino</td><td><p> </p><p>User is unable to create Feature Migration Template on Debt Schedule object.</p><p> </p></td><td><p> </p><p>22.3, 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr></tbody></table>

#### 5 November 2023

**(ARM v. 22.3.46)**

<table data-full-width="true"><thead><tr><th width="145">Module</th><th width="218">Summary</th><th>Fix Version(s)</th><th>Resolution</th><th>Cause</th></tr></thead><tbody><tr><td>All Modules</td><td>New User Creation</td><td>22.3</td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Change Request</p><p> </p></td></tr><tr><td>Environment Provisioning</td><td>View environment provisioning templates</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Enhancement</p><p> </p></td></tr><tr><td>Admin</td><td>Branching baseline is not picking all components from production</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Deployments</td><td>Help with destructive change</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>Version Control</td><td>Merge request is failing due to validation credentials</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Use Case</p><p> </p></td></tr><tr><td>CI Jobs, Deployments</td><td>Issues with a release – related to Feature Flag not automatically set: STANDARD_VALUE_SET_DELTA </td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Data</p><p> </p></td></tr><tr><td>Version Control</td><td>Approval button is not visible after successful merge validation</td><td><p> </p><p>22.3 &#x26; 23.1</p><p> </p></td><td><p> </p><p>Code Fix</p><p> </p></td><td><p> </p><p>Data</p><p> </p></td></tr></tbody></table>

#### 27 October 2023

**(ARM v. 22.3.45)**

This was a maintenance release. The following items were enhanced, fixed, or added:

* <mark style="background-color:blue;">**Loggers**</mark> were added to **Reports** and **Dashboard** modules in versions 22.3 and 23.1 due to a data error in which users were unable to fetch a Salesforce **code coverage** report.&#x20;
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Environment Provisioning** module in version 22.3 to enable users to **view Environment Provisioning** templates.
* An <mark style="background-color:blue;">**enhancement**</mark> was made by a code fix applied to the **Deployments** and **Org Synchronization** modules in versions 22.3 and 23.1 enabling users to **change deploy text for validations**.
* A code fix was applied to the **nCino** module of versions 22.3 and 23.1 due to a use-case scenario during dataset creation with saving only user info in **Json that is relevant to current dataset**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error with an **AR merge failing**.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 due to a use-case error in which the **incorrect removal of Custom Application type in package.xml on EZ-Commit** via AR occurred.
* A code fix was applied to the **Version Control** module of versions 22.3 and 23.1 in which two **external pull request** issues were occurring.

#### 25 October 2023

This was a maintenance release. The following items were enhanced, fixed, or added by code fixes resulting from use-case scenarios:

* A Code Fix was applied to the **Deployments** module due to the **Deployment initiated using Org Synchronization failing** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Version control** module due to a **Validation Error** requiring **Feature Flag:** **VALIDATE\_DEPLOY\_PICK\_FILECHANGES\_FROM\_DIFF** caused by a use case with a fix applied to versions 22.3 and 23.1.
* A Code Fix was applied to the **Reports** module due to the **Weekly Code/ Test Coverage Report** taking a long time caused by a use case with a fix applied to versions 22.3 and 23.1.

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

#### 30 July 2023 <a href="#id-23-july-2023" id="id-23-july-2023"></a>

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

#### 23 July 2023 <a href="#id-23-july-2023" id="id-23-july-2023"></a>

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

#### 18 June 2023 <a href="#id-18-june-2023" id="id-18-june-2023"></a>

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

#### 11 June 2023 <a href="#id-11-june-2023" id="id-11-june-2023"></a>

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

#### 04 June 2023 <a href="#id-04-june-2023" id="id-04-june-2023"></a>

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

#### 28 May 2023 <a href="#id-28-may-2023" id="id-28-may-2023"></a>

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

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

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

#### 14 May 2023 <a href="#id-14-may-2023" id="id-14-may-2023"></a>

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

#### 07 May 2023 <a href="#id-07-may-2023" id="id-07-may-2023"></a>

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

#### 30 April 2023 <a href="#id-30-april-2023" id="id-30-april-2023"></a>

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

#### 23 April 2023 <a href="#id-23-april-2023" id="id-23-april-2023"></a>

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

#### 16 April 2023 <a href="#id-16-april-2023" id="id-16-april-2023"></a>

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

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

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

#### 02 April 2023 <a href="#id-02-april-2023" id="id-02-april-2023"></a>

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

#### 26 March 2023 <a href="#id-26-march-2023" id="id-26-march-2023"></a>

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

#### 19 March 2023 <a href="#id-19-march-2023" id="id-19-march-2023"></a>

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

#### 12 March 2023 <a href="#id-12-march-2023" id="id-12-march-2023"></a>

**(ARM v22.3.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Static Code Anaysis** was failing due to missing property tag in **Apex PMD** rules file, but the UI log wasn't displaying this error ([#63554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101980029)).
* Fixed an issue where when there was no results generated, the report displayed an error that there are zero metrics instead of displaying the results as zero in all the places when there is no change ([#63272](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101591692)).
* Fixed an issue where user was unable to deploy a CI job with the **RelationshipGraphDefinition** components ([#64145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102836208)).
* Fixed an issue where **Validate** deployment was displayed as **failed** in UI and the database, but was successful as per the logs ([#63868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102596005)).
* Fixed an issue with **Review Artifact** where similar custom fields from different objects were not populating correctly and switching to other fields ([#63676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102181836)).
* Fixed an issue where multiple fields of the respective custom objects were getting selected parallelly while performing **edit** or **save** or **exit** operations on the **Review Artifact** screen (internal ticket).
* Enhanced ARM by adding an option for **multiple ARM instances** to share a **single database cluster** (internal ticket).

#### 05 March 2023 <a href="#id-05-march-2023" id="id-05-march-2023"></a>

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

#### 26 February 2023 <a href="#id-26-february-2023" id="id-26-february-2023"></a>

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

#### 19 February 2023 <a href="#id-19-february-2023" id="id-19-february-2023"></a>

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

#### 12 February 2023 <a href="#id-12-february-2023" id="id-12-february-2023"></a>

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

#### 05 February 2023 <a href="#id-05-february-2023" id="id-05-february-2023"></a>

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

#### 29 January 2023 <a href="#id-29-january-2023" id="id-29-january-2023"></a>

**(ARM v22.3.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment was failing with the following error when user was deploying **Permissionset** with a user-permission **Manage Public Documents**: `Permission Manage Public Documents depends on permission(s): Create Document, Delete Document, Edit Document, Read Document` ([#60597](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097399881)).
* Fixed an issue where CI jobs were failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#59050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095999076)).
* Fixed an issue where **Reports** deployment validation failed in **EZ-Merge** but was successful in **EZ-Commit** and **Deployment** modules ([#57714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093587003)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Fixed an issue where user initiated the prevalidation commit by enabling the destructive type but the deployment failed with an error `null` at **Diff** ([#59919](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096907001)).
* Fixed an issue where **Validate Deploy** failed in **QuickMerge** and displayed the following message: `This folder unique name already exists for this folder type or has been previously used. Please choose a different name` (internal ticket).
* Fixed an issue where CI job wasn't considering the metadata changes, so the destructive changes were not being prepared or displayed on the build. (internal ticket).

#### 22 January 2022 <a href="#id-22-january-2022" id="id-22-january-2022"></a>

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

#### 15 January 2022 <a href="#id-15-january-2022" id="id-15-january-2022"></a>

**(ARM v22.3.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Merge validation** failed to process when there was a **Flow** metadata ([#58309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095079556)).
* Fixed an issue with user received 6 notifications for a failed **CI Job** instead of 1 ([#58436](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095199003)).
* Fixed an issue where user was trying to register branches to AutoRABIT through GitHub, but was getting the following error: `Lower Region` ([#58888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095619252)).
* Fixed a recurring issue where **Commits** and **Merges** were slowing down at a particular step, and **EZ-Merge** was failing with an error at commit phase ([#51268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085726862)).
* Fixed an issue where while performing destructive changes in **EZ-Commit**, it was creating **package.xml** in root path folder in **SFDX** structure ([#57868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093790001)).
* Fixed a UI bug on **CI List** and **CI Results** pages where when pagination was changed, the first 25 records were repeated (internal ticket).
* Fixed an UI bug where the **LastUsedDate** column was not displayed in the **Branch Table** (internal ticket).

#### 8 January 2022 <a href="#id-8-january-2022" id="id-8-january-2022"></a>

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

#### 1 January 2022 <a href="#id-1-january-2022" id="id-1-january-2022"></a>

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

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

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

#### 18 December 2022 <a href="#id-18-december-2022" id="id-18-december-2022"></a>

**(ARM v22.3.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DataLoader Pro** where jobs executed in the last 6 months were not showing in the database process table and in the **Reports** module ([#53980](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087981132)).
* Fixed an issue with **Deploy SFDX Source With ALM Mapping** where CI job with ALM Mapping was not working as expected for Team which is not default ([#55995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091129007)).
* Fixed an issue where **Profile Diff** is working as expected for **Selective Deployment**, but not while using the same profile in the profile manager ([#52868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087005140)).
* Fixed an issue where **Environment provisioning** processes were failing to update when user was trying to change the email deliverability access level from **No access** to **All email** ([#55208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591189), [#55754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090487029)).
* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was creating an **EZ-Commit**, mapping the ALM Project (VersionOne) but received the following error: `JSONObject["Assets"] is not a string` ([#57238](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092610150)).

***

## **ARM Release Notes 22.2**

**Date of release:** _9 October 2022_\
**Article last updated:** _15 May 2023_

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

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. ApexPMD Upgrade to 6.49 version <a href="#id-1-apexpmd-upgrade-to-649-version" id="id-1-apexpmd-upgrade-to-649-version"></a>

With this release, PMD has been upgraded to version **6.49**. If you have not uploaded a rules file, ARM will use the default Apex PMD rules file. However, you can add new rules to the default ruleset.

Click [HERE](https://pmd.github.io/latest/pmd_next_major_development.html#list-of-currently-deprecated-rules) to view the list of currently deprecated rules available on GitHub.

#### 2. Auto-approve on validation success <a href="#id-2-autoapprove-on-validation-success" id="id-2-autoapprove-on-validation-success"></a>

We have moved one step closer to automating the flow by adding an option to choose if an **EZ-Commit** or an **EZ-Merge** should be approved automatically if the SCA validation is successful. Combined with the existing option to auto-commit on approval, this leads to a true CI/CD experience.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/manage-users-account-settings.md)

#### 3. HashiCorp Vault Integration <a href="#id-3-hashicorp-vault-integration" id="id-3-hashicorp-vault-integration"></a>

While adding HashiCorp credentials to ARM, you can now choose the **AWS Authentication** method so that the Vault Token will be generated automatically whenever the existing token expires. Now the user will not have to update the token manually from the application when it expires.

[**Read more →**](release-notes-22.3.md#3-hashicorp-vault-integration)

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

### Improvements <a href="#improvements" id="improvements"></a>

* Users with Admin access can now turn off the Jira comments and notifications created by AR. This ensures a cleaner workspace. These comments and notifications are very development centric, so the end users who use Jira cannot make sense of our technical comments from AR, and this may create confusion for them.

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

***

## **ARM Release Notes 22.1**

**Date of release:** _20 March 2022_\
**Article last updated:** _23 October 2022_

### New features <a href="#new-features" id="new-features"></a>

#### 1. Squash and merge <a href="#id-1-squash-and-merge" id="id-1-squash-and-merge"></a>

We have added the **Squash and Merge** feature in this release. Sometimes, when merging a long list of changes from a development branch into the master, it's helpful to squash those commits into one change for ease of review and declutter the repo's commit history. AutoRABIT offers an option to squash all commits in a merge request into one commit after the merge is approved and completed.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/squash%20and%20merge.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/ez-merge/squash-and-merge.md)

#### 2. SFDX- Import packages <a href="#id-2-sfdx-import-packages" id="id-2-sfdx-import-packages"></a>

**Packages**

The users could previously build a new package (unlocked or managed) and update the package's version in Salesforce DX. With this release, you may now import packages and update the version of packages created outside of AutoRABIT.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/import%20packages.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/import-an-unlocked-managed-package.md)

**Dev Hub management**

With this update, users will see all of the packages in their dev hub in the record view. You may expand each package to show the package's versions in order and package data such as version name, version number, ancestor version, ancestor dependencies, etc.

![Dev hub.gif](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Dev%20hub.gif)

[**Read more →**](../../../product-guides/arm/registering-a-devhub.md)

#### 3. Step-based rollback <a href="#id-3-stepbased-rollback" id="id-3-stepbased-rollback"></a>

The option to list the API-supported and unsupported API components is added to the CI job/deployment rollback. If such components may be deployed to the target environment but do not have API support to delete them, ARM will display them individually as unsupported API types. Take, for example, **RecordType**.

The **RecordType** component may be deployed to the target environment, but it cannot be removed; instead, we need to connect to the target Salesforce environment to deactivate the component.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/step%20based%20rollback.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-rollback.md)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Checkmarx upgrade to v9.4.1 <a href="#id-1-checkmarx-upgrade-to-v941" id="id-1-checkmarx-upgrade-to-v941"></a>

Checkmarx has been updated to version **9.4.1**. Earlier, Checkmarx used a username/password-based authentication method. Now, the user will be able to use token-based authentication with the Checkmarx upgrade.

#### 2. Export all users <a href="#id-2-export-all-users" id="id-2-export-all-users"></a>

The **Export All Users** feature allows the org admins to export a CSV file of all the users currently in their account. We now have added the following fields to the existing CSV file:

* CreatedDate
* CreatedByName
* DeativatedDate
* LastLoginDate
* DeactivatedByName
* LastModifiedDate
*   LastModifiedByName.<br>

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/export%20all%20users.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/users-roles-and-permissions.md)

#### 3. Pull request support for Azure cloud repositories <a href="#id-3-pull-request-support-for-azure-cloud-repositories" id="id-3-pull-request-support-for-azure-cloud-repositories"></a>

We have extended the support of having the pull request support in the CI Job for the Azure repository. This feature was previously available for Github cloud/Enterprise and Bitbucket cloud/Enterprise; however, we've added support for Azure cloud repositories (DX and non-DX repositories) with this release.

#### 4. Merge/commit approval eligibility <a href="#id-4-mergecommit-approval-eligibility" id="id-4-mergecommit-approval-eligibility"></a>

If you want to make sure one or more people approve every commit or merge, you can enforce this workflow by using merge/commit approvals. These approvals allow you to set the number of necessary approvals to approve every commit/ merge in a project.

The org admins' eligibility level has been enhanced with the ARM 22.1 version. If you're an administrator, you will have the privilege to approve self-merge even if the criteria to self-approve a merge is set to FALSE. This permission will be denied to all members of your team except the org admin. To put it another way, no criteria can restrict an org administrator from approving any EZ-commit/ EZ-Merge.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/commit-merge%20approval.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/merge-approvals.md)

#### 5. CodeScan additional metadata support <a href="#id-5-codescan-additional-metadata-support" id="id-5-codescan-additional-metadata-support"></a>

We have enhanced the scope for analysis of what CodeScan does by adding support for additional metadata and rules. For our ARM users who want to incorporate the SCA tool into their subscriptions, CodeScan would be their first choice as it now supports more robust integrations.

Below is the list of CodeScan supported metadata types:

|                                   |                         |                         |
| --------------------------------- | ----------------------- | ----------------------- |
| Apex Triggers                     | Apex Classes            | Aura Definition Bundles |
| Lightning Component Bundles (LWC) | Visualforce Pages       | Custom Object           |
| Settings                          | Flows                   | Workflows               |
| Profiles                          | Sharing Rules           | Sharing Criteria Rules  |
| Sharing Owner Rules               | Sharing Territory Rules | Permission Sets         |

#### 6. SFDX CLI update <a href="#id-6-sfdx-cli-update" id="id-6-sfdx-cli-update"></a>

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

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

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

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

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

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

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

#### 11 December 2022 <a href="#id-11-december-2022" id="id-11-december-2022"></a>

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

#### 04 December 2022 <a href="#id-04-december-2022" id="id-04-december-2022"></a>

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

#### 27 November 2022 <a href="#id-27-november-2022" id="id-27-november-2022"></a>

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

#### 20 November 2022 <a href="#id-20-november-2022" id="id-20-november-2022"></a>

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

#### 13 November 2022 <a href="#id-13-november-2022" id="id-13-november-2022"></a>

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

#### 06 November 2022 <a href="#id-06-november-2022" id="id-06-november-2022"></a>

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

#### 30 October 2022 <a href="#id-30-october-2022" id="id-30-october-2022"></a>

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

#### 23 October 2022 <a href="#id-23-october-2022" id="id-23-october-2022"></a>

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

#### 16 October 2022 <a href="#id-16-october-2022" id="id-16-october-2022"></a>

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

#### 09 October 2022 <a href="#id-09-october-2022" id="id-09-october-2022"></a>

**(ARM v22.1.28)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **nCino** where user was getting errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).
* Fixed an issue where user noticed discrepancy in the **Conflict Resolution Log** ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).

#### 02 October 2022 <a href="#id-02-october-2022" id="id-02-october-2022"></a>

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

#### 26 September 2022 <a href="#id-26-september-2022" id="id-26-september-2022"></a>

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

#### 19 September 2022 <a href="#id-19-september-2022" id="id-19-september-2022"></a>

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

#### 11 September 2022 <a href="#id-11-september-2022" id="id-11-september-2022"></a>

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

#### 04 September 2022 <a href="#id-04-september-2022" id="id-04-september-2022"></a>

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

#### 28 August 2022 <a href="#id-28-august-2022" id="id-28-august-2022"></a>

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

#### 21 August 2022 <a href="#id-21-august-2022" id="id-21-august-2022"></a>

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

#### 14 August 2022 <a href="#id-14-august-2022" id="id-14-august-2022"></a>

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

#### 07 August 2022 <a href="#id-07-august-2022" id="id-07-august-2022"></a>

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

#### 31 July 2022 <a href="#id-31-july-2022" id="id-31-july-2022"></a>

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

#### 24 July 2022 <a href="#id-24-july-2022" id="id-24-july-2022"></a>

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

#### 17 July 2022 <a href="#id-17-july-2022" id="id-17-july-2022"></a>

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

#### 10 July 2022 <a href="#id-10-july-2022" id="id-10-july-2022"></a>

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

#### 03 July 2022 <a href="#id-03-july-2022" id="id-03-july-2022"></a>

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

#### 26 June 2022 <a href="#id-26-june-2022" id="id-26-june-2022"></a>

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

#### 19 June 2022 <a href="#id-19-june-2022" id="id-19-june-2022"></a>

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

#### 12 June 2022 <a href="#id-12-june-2022" id="id-12-june-2022"></a>

**(ARM v22.1.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 05 June 2022 <a href="#id-05-june-2022" id="id-05-june-2022"></a>

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

#### 29 May 2022 <a href="#id-29-may-2022" id="id-29-may-2022"></a>

**(ARM v22.1.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 22 May 2022 <a href="#id-22-may-2022" id="id-22-may-2022"></a>

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

#### 15 May 2022 <a href="#id-15-may-2022" id="id-15-may-2022"></a>

**(ARM v22.1.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).

#### 08 May 2022 <a href="#id-08-may-2022" id="id-08-may-2022"></a>

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

#### 01 May 2022 <a href="#id-01-may-2022" id="id-01-may-2022"></a>

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

#### 24 April 2022 <a href="#id-24-april-2022" id="id-24-april-2022"></a>

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

#### 17 April 2022 <a href="#id-17-april-2022" id="id-17-april-2022"></a>

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

#### 10 April 2022 <a href="#id-10-april-2022" id="id-10-april-2022"></a>

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

#### 03 April 2022 <a href="#id-03-april-2022" id="id-03-april-2022"></a>

**(ARM v22.1.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option where not working when users use the EZ commit/ Merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 March 2022 <a href="#id-27-march-2022" id="id-27-march-2022"></a>

**(ARM v22.1.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** in the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the exclude metadata types in the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).
