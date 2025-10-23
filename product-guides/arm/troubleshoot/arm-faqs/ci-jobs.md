# CI Jobs

### What is the webhook payload URL?

After the 25.3.9 release, the structure of the webhook payload URL was updated. Users need to update the webhook URL in the repository settings of their remote repo. Customers who are still using the old webhook URL containing **autorabitrest** should replace them with API.

Old URL: [https://na25.autorabit.com/**autorabitrest**/webhook/triggerSCMPushrequest](https://na25.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest)

Updated URL: [https://na25.autorabit.com/**api**/webhook/triggerSCMPushrequest](https://na25.autorabit.com/api/webhook/triggerSCMPushrequest)

Unless you update the payload URL, you may face pull request/trigger build-on-commit jobs triggering.

### What are the benefits of using Quick Deploy?&#x20;

When you run a validation deployment through ARM, it will pre-run all unit tests. The Quick Deploy option then allows you to skip those tests in the final production release, knowing they passed previously. Using the Quick Deploy option reduces the amount of time the Production org is locked.&#x20;

### When Is the Quick Deploy option available in a CI Job? <a href="#id-1-when-quick-deploy-option-will-be-available-in-ci-job" id="id-1-when-quick-deploy-option-will-be-available-in-ci-job"></a>

Quick deployments are available when the following requirements are met:

* The components have been successfully validated for the target environment.
* As part of the validation, Apex tests in the target org have passed.
* Code coverage requirements are met.
* If all tests in the org or all local tests are run, overall code coverage is at least _75%_, and Apex triggers have some coverage.
* If specific tests are run with the _Run specified tests_ test level, each class and trigger that was deployed is covered by at least 75% individually.
* The "Prevent Deployment" checkbox is NOT selected in the CI Job setting.

### Why am I getting a popup saying, "Not Eligible for Quick Deploy," after selecting Quick Deploy in the CI Job?

This error will occur when the "Prevent Deployment" checkbox is enabled in the CI Job setting. Deselect the checkbox, then proceed with the Quick Deploy.

### Why am I not receiving email notifications for all CI jobs that AutoRABIT has initiated? <a href="#id-3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated" id="id-3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated"></a>

You might have exceeded the maximum number of recipients; the maximum number of recipients should not exceed 50. Remove some of the recipients from the mail notification list and run the CI job again; you should now receive email notifications.

### Why is it taking longer to build CI jobs triggered on PR submission as compared to CI jobs triggered on Commit? <a href="#id-4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger" id="id-4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger"></a>

**Build on Commit Job:** When a user creates a CI job on one branch, for example, _Integration_, if any **Commits** are made on that branch on the remote, we will only perform the **Pull (Delta changes)** and then prepare the **Package**. This is why the build time is shorter.

**Build on PR Submission:** When a CI job is created on the base branch, for example, _Integration_, if the developer works on the **Feature 1** branch and creates the **Pull Request (PR)** on the **Integration** branch, then the job gets triggered in ARM. The branch will switch to the **Feature 1** branch, take the clone of the entire branch, prepare the changes between the two branches, and then switch back to the master branch when the job is completed. This is why the build time is longer for PR jobs.

### Why is my CI job failing with the error ‘HTTP ERROR 405 Problem accessing /services/Soap/m/55.0. Reason: Only POST allowed’? <a href="#id-5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on" id="id-5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on"></a>

The authentication for your destination org may have expired. Please **Re-authenticate** your target Salesforce org. Once this is done successfully, please Edit and resave the CI job, then retrigger it.

### Why are the FLS changes in the CI job reflected in the diff file but not in the sandbox? <a href="#id-6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox" id="id-6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox"></a>

This usually happens if the **Ignore missing visibility** checkbox is selected in CI Jobs. Another possibility is that the field in question is unavailable in the destination org where the FLS was deployed. Please contact our support team to determine the root cause and assist you further.

### Why am I unable to push components from a branch to an org in a CI Job? What is the ‘Maximum size of request reached’ error? <a href="#id-7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re" id="id-7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re"></a>

This error may be due to a file size limitation. We suggest you break deployments down into smaller chunks to be successful. Please refer to the Salesforce article below about the file size limits for deployments: [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_metadata.htm)

### How do User Credentials impact different types of CI Jobs? <a href="#id-8-how-does-the-user-credentials-impact-different-types-of-ci-jobs" id="id-8-how-does-the-user-credentials-impact-different-types-of-ci-jobs"></a>

Listed below are the different types of CI Jobs and their corresponding credential usage:

#### **Forced/Manually Triggered Build:**

The CI job process will consider the triggered **User Credential,** which is mapped with the respective Repo and Branch in the **My Profile** section.\
\
If the credentials are invalid/expired, authentication fails and an error message is displayed upon build initiation.\
\
To resolve this issue, the user initiating the build must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, reinitiate the CI Job

#### **Build on Commit and Scheduled CI Job:**

The CI Job process will consider the last modifying user's credentials, which are mapped with the respective Repo and Branch in the **My Profile** section.\
\
If the credentials are invalid/expired, the CI Job build fails and authentication error message is displayed in the CI Job Build log.\
\
To resolve this issue, the user who last modified the CI Job must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, the job will be executed in the next cycle.

#### **CI Job Build Initiated From API:**

The CI Job process will consider the **Token** user credential, which is mapped with the respective Repo and Branch in the **My Profile** section.\
\
If the credentials are invalid/expired, the CI Job build fails and an authentication error message is displayed in the CI Job Build log.\
\
To resolve this issue, user generating the token must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, the job will be executed in the next cycle.

### Why is CI Jobs deploying a metadata type I deselected in the "Exclude Metadata Types" section? <a href="#id-9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section" id="id-9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section"></a>

If you have deselected a metadata type but it is still being deployed in CI jobs, then it could be because of a different name. Please verify that the **folderName** committed in Git is correct for the metadata. This should resolve the issue. If it doesn’t, contact our support team for further analysis.

### Why is a CI job for production deployment running random test classes, even though there are no Apex classes in the build, causing the deployments to fail? <a href="#id-10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap" id="id-10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap"></a>

You might have selected the option to **Include default Apex tests for run test based on changes** under **Admin**-->**Salesforce settings**, so even though there are no classes present in the package, it's still running default classes for code coverage. This is an expected behavior.

### Why am I getting an error while trying to access CI job builds more than 3 months old? <a href="#id-11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds" id="id-11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds"></a>

The reason you are unable to get the details of specific builds older than 3 months is due to ARM’s **Retention Policy**. There are some details which are archived and become unretrievable.

You can change the retention period to 6 months or 12 months from the **Admin** section of your ARM account.

### Why is a CI job failing with an error during validation? <a href="#id-12-why-is-a-ci-job-failing-with-an-error-during-validation" id="id-12-why-is-a-ci-job-failing-with-an-error-during-validation"></a>

The deployment may fail if it does not detect the metadata root folder path ‘src.’ Please update the Branch settings and then re-save the CI Job.

You can then perform a Merge Request to trigger the CI job and validate the deployment.

### How do I include destructive changes in a CI job? <a href="#id-13-how-do-i-include-destructive-changes-in-a-ci-job" id="id-13-how-do-i-include-destructive-changes-in-a-ci-job"></a>

Review this [Knowledge Base article](../../arm-features/deployment/destructive-changes.md), which covers performing destructive changes through CI jobs.

### The "File Changes" tab shows that the Quick Actions metadata type is deleted. Why isn’t this reflected in the Destructive Changes tab or the package xml? <a href="#id-14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte" id="id-14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte"></a>

This may be a **GIT** behavior where the **QuickAction** metadata members are added and deleted again. As per GIT behavior, when it has to generate the delta between **From** and **To** revisions, in the case of a conflict, it skips such files from package preparation.

There is no Git logic under **File Diff** because it simply displays what was **added/modified/deleted** for better UI visibility to understand the changes and be reviewed.&#x20;

You can work around this by **updating the baseline** revision **CI job** and using **Single Revision** in the **Deployment** module.

### Why am I getting the "License is not valid" error when trying to use CodeScan as the analysis tool while running a CI job in ARM? <a href="#id-15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool" id="id-15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool"></a>

This could be due to using an older version of CodeScan. Refer to the [CodeScan License Errors](../../../../fundamentals/faq/codescan-faqs/codescan-self-hosted-issues/license-errors.md) article for further information.

### **Why am I not getting a package for the CI Job?**

Packages will only be displayed in CI jobs if created or imported through our application's SFDX -> Packages module. This ensures that we accurately track packages and their versions.

To create or import the package, refer to the following articles:

* Create a Package: [Create an Unlocked/Managed Package | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/salesforce-dx/create-an-unlocked-managed-package)
* Import a Package: [Import an Unlocked/Managed Package | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/salesforce-dx/import-an-unlocked-managed-package)

### Why am I receiving the error message: Cannot invoke "String.startsWith(String)"?&#x20;

This occurs when the return value of "com.autorabit.entity.admin.UserProject.getProjectType()" is null. A fix has been incorporated in the ARM 23.1.24 release. Reference support ticket # 109042.

### **Can I update or remove picklist values with my CI Job?**

Since Salesforce does not retrieve deleted/deactivated picklist values in a metadata API call, replacing the picklist values via BackUp to VersionControl CI Job is impossible. However, a best practice in replacing the Picklist values is using the EZ-Commit module.

This configuration for RecordType PicklistValues option only works in the EZ-Commit module. If picklist values need to be replaced, use this approach.

<figure><img src="../../../../.gitbook/assets/image (1554).png" alt=""><figcaption></figcaption></figure>

Refer to [How to Configure Record Types Picklist Values](https://knowledgebase.autorabit.com/product-guides/arm/troubleshoot/how-tos/configure-record-types-picklist-values) for more information.
