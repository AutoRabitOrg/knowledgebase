# ARM Known Limitations

These are the known limitations in **ARM® 22.3**.

### **List of Failure Cases / Limitations** <a href="#list-of-failure-cases-limitations" id="list-of-failure-cases-limitations"></a>

1. **Patch Can't Apply Commit Failing: If there are conflicts on the same line in modified files.** For example, when multiple users make changes to the same line and User-2 has committed to the remote branch. If User-1 then tries to perform the commit on a previously created prevalidation commit label, the commit will fail.
2. **Patch Can't Apply Commit Failing: If there are conflicts on added files.** Similar to the previous case, multiple users are making commits to the same new files. If User-2 has committed to the remote branch, and User-1 then tries to perform a commit already created using a prevalidation commit label, the commit will fail.
3. **Patch Can't Apply Commit Failing: If multiple users make changes in between 3–4 lines.** This scenario leads to conflicts; the patch and commit will fail.
4. **Patch Can't Apply Commit Failing: In some cases, specific metadata type components may have conflicts, while other metadata type components may not have conflicts.** This scenario leads to conflicts; the patch and commit will fail.

### ALM Known Limitations <a href="#alm-known-limitations" id="alm-known-limitations"></a>

Jira OAuth access type is currently supported for **Cloud versions** only.

### Deployment Known Limitations <a href="#deployment-known-limitations" id="deployment-known-limitations"></a>

This section summarizes the deployment limits that ARM users should consider:

1. **Unable to remove Field Level Security (FLS) in Profiles while performing destructive changes on fields**- As of now, ARM does not support the deletion of references from Profile on a branch level. But, it is on our roadmap, and the development team is already working on it.
2. While performing deployment from one sandbox to sandbox, there are certain metadata types such as Email Template, Reports, Dashboards, Documents, etc for which the selected folder path metadata will not get retrieved in the **Compare Metadata and Deploy** screen.
3. The **Compare Metadata & Deploy** functionality for **Profile** metadata will not show the correct difference since the source side displayed delta changes while the destination side retrieved the entire profile from the destination org.
4. AccelQ applies only to the deployment of [Salesforce Org](../../arm-administration/registration/salesforce-org/) and not Vlocity.
5. Rollback initiated for a successful deployment shows **No Changes** status in the build.
6. **Pre-destructive changes and deployment changes run in separate threads in ARM, but the status of the deployment changes is only seen:** Pre-destructive changes and deployment will be sent to Salesforce as part of the same request, and Salesforce will treat them as separate actions. To check the status of pre-destructive changes in ARM, click on your **Deployment Label** then go to **Deleted Components** tab.
7. **Is it possible that my code deployment will continue if my pre-destructive changes fail for some reason?** No, because pre-destructive changes and deployment will be sent to Salesforce as part of the same request in ARM, and if one of your deployments fails, the entire process fails in ARM.
8. Due to current ARM behavior, an **object file** is considered as a **destructive change** in deployment if the object file does not exist in the branch, you commit only a field (child), and then the newly committed field is deleted from the branch. This is the case only for **Metadata API** code, not for **SFDX**.
9. In case of **Vlocity Custom Deployment**, if the **Access Key** for **Local Compilation** is incorrect, ARM is unable to capture it in the logs.
10. In **Compare Org and Deploy functionality**, a file diff will not be generated between the source and the target for **Bot Version files**.
11. If a user uses the **SFDX extension** in a **non-SFDX repository** for any metadata type, then it will not be displayed in UI as a **metadata change** and won't be picked up for deployment in **package.XML**, but the file contents will stay in the promotional **ZIP** file.&#x20;
12. When dealing with the limitations of integrating Salesforce DX (SFDX) with Vlocity components, several key considerations must be taken into account to ensure effective management and deployment of these components. Below are the **compatibility issues** that must be considered for this feature:
    * **Metadata Types**: Understand the differences in metadata types between SFDX and Vlocity. SFDX does not natively support Vlocity-specific metadata, which requires using specialized tools like the Vlocity Build Tool.
    * **Deployment Methods**: SFDX deployment methods (e.g., packages, change sets) are not fully compatible with Vlocity DataPacks, necessitating alternative deployment strategies.
    * **Hybrid Approach**:&#x20;
      * Maintain separate repositories for SFDX and Vlocity components.&#x20;
      * Use SFDX for Salesforce metadata and development, while managing Vlocity components through their own repository and tools.&#x20;
      * Follow the specific guidelines and best practices provided by Vlocity and Salesforce DX for managing and deploying each type of component.

### Version Control Known Limitations <a href="#version-control-known-limitations" id="version-control-known-limitations"></a>

This section summarizes the Version control limits that ARM users should consider:

#### During EZ-Commit <a href="#during-ezcommit" id="during-ezcommit"></a>

1. Create or append revision to **release** and **commit label** are not supported for the vlocity components deployment.
2. The **custom YAML** file being uploaded does not get saved in ARM.
3. While trying to delete aura components from a Version control branch using the EZ-Commit process in ARM, the Aura components don't get deleted. It still remains available in the version control branch. There is a dependency which prevents deletion of aura components from the version control branch although the components are not available in the Salesforce org.
4. While trying to commit via **previously validated commit labels**, you may not find components listed on the **Deleted** tab. This is expected behavior from our application. To view the deleted components, make sure you use the **Auto Draft** functionality during the EZ-commit process.
5. During an **EZ-Commit**, some of the standard fields like **Account.BillingCountry**, **Account.BillingGeocodeAccuracy**, etc. are not getting fetched from the Salesforce org. This is because there is no proper API to fetch these standard fields from Salesforce.
6.  SFDX structure methods (e.g., packages, change sets) are not fully compatible with Vlocity DataPacks, necessitating non-SFDX repositories, therefore, what is suggested is as follows:

    &#x20;

    **Hybrid Approach**:

    * Maintain separate repositories for SFDX and Vlocity components.
    * Use SFDX for Salesforce metadata and development, while managing Vlocity components through their own repository and tools.
    * Follow the specific guidelines and best practices provided by Vlocity and Salesforce DX for managing and deploying each type of component.

#### During EZ-Merge <a href="#during-ezmerge" id="during-ezmerge"></a>

1. Merge process in ARM remains valid for **7 days**. Make sure you resolve the merge conflicts (if any) for your merge label and commit the changes to another branch within 7 days or else the merge gets expired. Even merge related reports such as [static code analysis ](https://www.autorabit.com/products/codescan/)reports, deployment validation reports, or difference reports generated also gets expired after **7 days**.
2. Merge via single revision, commit Labels and release Labels is not allowed if the version control repository is in **SFDX** structure.
3. The merge request author is not allowed to approve their own merge request.
4. **Prevalidate Merge** section will be visible only if the admin has enabled the **Merge Setting** checkbox under the **My Account** section.
5. Users with the **Merge Review Overridable** role has special permission to either check or uncheck the pre-validate option. However, each time they try to commit to the branch, a notification alert mail gets triggered to the email id as configured in **My Account > Merge Settings** section.
6. If the **meta-XML** file does not exist in the destination branch and is available in the source branch, then the meta-XML file is copied from the source banch to the destination branch, before committing to the remote repository. The newly added meta-XML file will be added to the files list and will be committed to the remote repository and will also be added to **Validate Deployment** package.
7. AutoRABIT stores the static code analysis source content for **90 days**, post 90 days, the report will auto-deleted.
8. For those PMD/lint report which was generated before **ARM 19.2.1** release, those source content file will not be seen in the static analysis report.
9. For the **Dry Run** merge operation, if a user submits an already merged revision, then the **'Empty Commit Exception'** message gets displayed. See the image below.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. Users with the **Merge Review Overridable** role also can approve the commit although he does not qualify to do so. In such a scenario, a notification alert mail gets triggered to the email id(s) as configured in **My Account > Merge Settings** page.
11. While resolving merge conflict files via Inline Editor, a situation may arise where the files that you are trying to resolve are improperly resolved. This can lead to the malformation of the conflicted files. To resolve those, you need to download the file locally, work on the conflicted files using your merge tool and make necessary changes to it. Then upload the same.
12. You are allowed to manually edit and correct the code using the Inline Editor only if there are some merge conflicts. When there are no conflicts, editing is not permitted.
13. During Merge initiation, for version control registered in SFDX structure, **Source Folder** selection will not be available.
14. For the merge process where the version control is registered in the SFDX structure, the user will not have the option to create a commit label. The **Create Commit Label** checkbox will be in disabled mode.

#### For Release Label <a href="#for-release-label" id="for-release-label"></a>

When trying to get the list of commits labels committed from the merge process for your SFDX repository and choosing your package directory, the commit labels result may differ from the actual one. No outcome can be found in some situations. It is therefore recommended to search for commit labels keeping the **Package Directory** as **ALL** until the root cause of the problem is identified.

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### For Pull Request <a href="#for-pull-request" id="for-pull-request"></a>

Below are the limitations of ARM related to Pull request:

1. ARM synchronizes the pull requests to access the latest updates from the repository when clicked. Therefore, to show the latest changes, comments, or any updates, it is recommended to click on the individual pull request.
2. The **Diff** tab will allow you to view the metadata components that were committed to the new branch. However, the response includes a maximum of **300** files.
3. The CI job will get triggered only for the newly created pull requests and are in an **open** state.
4. When the **Pull Request** checkbox is checked during CI Job, some of the options may get withdrawn automatically. For example- Incremental Build, Trigger Build on Commit, or Map ALM Project. This is because such options are not required when the job is triggered via pull request.
5. When pull request is validated via CI job, the **Validate Only** option will be in the selected mode. The user won't be able to uncheck it.
6. To support pull request in ARM, enable the **skip mappings** checkbox under the **Profile** section.
7. **Pull request** is currently not supported for repositories authenticated via **SSH** protocol. However, it does support **HTTPS-based** connection via username and personal access token.
8. Github needs access to the GitHub API, which can only be accessed via HTTP(S) Oauth2 and not SSH.

### Salesforce DX Known Limitations <a href="#salesforce-dx-known-limitations" id="salesforce-dx-known-limitations"></a>

Below are the limitations of ARM related to salesforce dx:

1. [Salesforce DX](https://www.autorabit.com/blog/the-basics-of-salesforce-dx/) functionality is currently applicable only for DX-enabled version control repositories.
2. Source commit from EZ-Commit process will be done only in DX-format for SFDX enabled repositories.
3. It is mandatory to select the **SFDX Package Directory** for DX-enabled repositories while carrying out the EZ-Commit operation.
4. Dependencies will be calculated using **Salesforce Dependency API**.
5. Adding dependencies are subject to the **API limitations**.
6. In **SFDX > Modularization**, the data will be extracted only if the **CustomObject** metadata either selected/identified as a dependency.
7. A new package version gets generated each time the packages get updated. However, if you would like to install the updated packages to the same Salesforce org, the packages will not get installed. To do so, uninstall the current package from the Salesforce org and install the latest one **(Custom Deployment)**.
8. For a module or an unlocked package creation request is in progress, make sure for the same repository and branch, another creation request is not submitted.
9. The user should not include such metadata members in a package directory of a branch if the same metadata members are already available for another package directory for the same branch.
10. Profiles will not be included in the **Unlocked Packages**.
11. Listed below in the table the metadata types which are currently not supported in the DX format:

| AccountRelationshipShareRule | AnalyticSnapshot           | Audience           |
| ---------------------------- | -------------------------- | ------------------ |
| AccountRelationshipShareRule | AnalyticSnapshot           | AssessmentQuestion |
| AssessmentQuestionSet        | Audience                   | ApexTestSuite      |
| AIApplicationConfig          | BlacklistedConsumer        | CMSConnectSource   |
| CustomIndex                  | AIApplication              | ForecastingType    |
| ForecastingFilter            | ForecastingFilterCondition | InboundCertificate |

### CI Job Known Limitations <a href="#ci-job-known-limitations" id="ci-job-known-limitations"></a>

1. Vlocity components deployment is not supported from one sandbox to another sandbox as of now. However, it does support retrieval of vlocity components from the selected metadata folder path and getting it deployed from a version control branch to the sandbox.
2. ARM will retrieve the entire data that is available in the **datapacks folder path**. However, there is no provision to select any specific data or components and getting it deployed to the sandbox.

```
* autorabit_alldefault_vlocity_build: Correct folder path

* autorabit_alldefault_vlocity_build/<Folder Name>: Incorrect folder path
```

3. **For ALM configured CI jobs:** The metadata members which are associated with the revision of a merged label will be included in the build. If the user has enabled the rollback option while configuring their CI jobs, the ALM work items status will get updated once the deployment is successful. However, if the user would like to rollback the same deployment, the ALM work items status remains unchanged.
4.  The below points highlight the limitation for those CI jobs in which post-deployment activities are configured.

    <figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1).png" alt="" width="459"><figcaption></figcaption></figure>

    * Currently, workflow sequence is not supported as a post-deployment action for **"Run Skuid Pages"**
    * While carrying out the post-deployment workflow, make sure no manual effort has interfered.
    * The post-activity remains active till **12 hours**, beyond which the activity gets terminated. No further action will be performed for timed-out tasks.
    * In some scenarios, the post-activity operation can get delayed if **Jenkins jobs** are triggered.
    * While keeping various jobs in sequential order, it is a best practice to keep both Merge and Jenkin Job in the latter part of the sequencing workflow. This prevents human interference if, in case there are any conflicts arise that require your immediate action to resolve them.Until the conflicts are solved, the process remains in the incomplete stage, and till the time the conflicts are not manually resolved, other post activities that are next in the sequential order, will not get triggered.
    * For all post activities that were triggered while configuring the CI Job, their status report can be seen in the **CI Job Result > Post Activities** section. However, in order to view the detailed information of the activities, you need to view their respective History/ Summary page. For example, for a merge process triggered as a post-activity, its detailed information such as merge label name, source and destination branch, merge conflict files (if any) and other information can be seen only on the Merge Summary page.
    * While the post activities are running for **"Cycle 1"**, and if the **"Cycle 2"** deployment post activities are initiated before the **"Cycle 1"** is complete, in such case **"Cycle 1"** changes will be overridden.
    * With ARM 19.2 release onwards, the users will have another option to choose i.e., **"Process commit revision via hook only"** for Version Control as GIT (Enterprise BITBUCKET v, BITBUCKET, VSGIT, GITLAB, GITHUB) type.
5.  In case of a failed CI Job deployment, AutoRABIT sends an email notification to the users informing about the revision from which the deployment got failed. But if the number of recipients is more than 50, this notification is not sent.\


    However, for the SFDX and vlocity jobs, users will not get notified of any failed revisions.

<figure><img src="../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Code coverage results during the CI job come from any tests you've run from the AutoRABIT application, however, you will be able to view the report only if the code coverage is more than **0%**.
7. For CI Jobs builds that are more than 30 days old, **deployment/ quick deployment/ rollback reports** will not be accessible.
8. **DX deploy** - We are considering the constructive changes deployment status for updating the ALM status, but not for pre/post destructive deployment.
9. For Validate deployments and Quick Deployment, we will not update the ALM statues.
10. **Internet Explorer (IE)** is no longer supported as a **Test Browser** to **Run Test Automation Scripts** when creating CI jobs. The IE icon/checkbox has been disabled. The Firefox and the Chrome browser are still supported.

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1).png" alt="" width="536"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

The **Test Results** will not show any test scripts configured to run with the IE browser. However, the **Total Tests** in the report will include the IE tests. This may cause a discrepancy between the number of tests shown and the tests listed.

<figure><img src="../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### TAF Known Limitations <a href="#taf-known-limitations" id="taf-known-limitations"></a>

ARM is unable to load the log files for any job using the **View Log** option in the report. Instead, an error _No log file found_ appears where the logs should be.

<figure><img src="../../../../.gitbook/assets/image (22) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Vlocity Known Limitations <a href="#vlocity-known-limitations" id="vlocity-known-limitations"></a>

1. **Review Artifacts** option is disabled for vlocity components in the **EZ-Commit** screen.
2. Vlocity processing time depends on the size of the Salesforce Org metadata.
3. Vlocity commits remain in an in-progress state for a longer time: This may occur if your org storage limit has been reached. To avoid this, it's better to clean up your unwanted data from your org and re-trigger the vlocity commit once again.
4. AutoRABIT supports the below YAML file structures while uploading the YAML file manually during EZ- Commit operation.

**Structure 1**

<figure><img src="../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Structure 2**

<figure><img src="../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1).png" alt="" width="498"><figcaption></figcaption></figure>

**Structure 3**

<figure><img src="../../../../.gitbook/assets/image (25) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:**

* Structure 1 and Structure 2 can be combined and used together in a single YAML file.
* Structure 3 must be used independently and never be combined with other structures in a single YAML file.
{% endhint %}
