# CI Jobs- FAQ

## 1. Why isn't the 'Quick Deployment' option enabled after the CI/Custom Deployment? <a href="#1-why-isnt-the-quick-deployment-option-enabled-after-the-cicustom-deployment" id="1-why-isnt-the-quick-deployment-option-enabled-after-the-cicustom-deployment"></a>

Quick deployments are only available when the following criteria are met:

* The components have been successfully validated for the target environment **within the last ten days**.
* Apex tests in the target org have passed as part of the validation.
* Code coverage requirements are met.
* If all tests in the org or all local tests are run, overall code coverage is at least **75%**, and Apex triggers have some coverage.
* If specific tests are run with the **Run Specified Tests** test level, each class and trigger deployed is covered by at least **75%** individually.

***

## 2. Why isn't the CI Job able to choose the changes for commits that have already been validated? <a href="#2-why-isnt-the-ci-job-able-to-choose-the-changes-for-commits-that-have-already-been-validated" id="2-why-isnt-the-ci-job-able-to-choose-the-changes-for-commits-that-have-already-been-validated"></a>

If the baseline revisions aren't picking up the two, clear the baseline revision and choose the same one again.

***

## 3. Why am I not receiving email notifications for all CI jobs that AutoRABIT has initiated? <a href="#3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated" id="3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated"></a>

You might have exceeded the maximum number of recipients; the maximum number of recipients should not exceed 50. Remove some recipients from the mail notification list and rerun the CI job; you should now receive email notifications.

***

## 4. Why is it taking longer to build CI jobs triggered on PR submission as compared to CI jobs triggered on Commit? <a href="#4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger" id="4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger"></a>

**Build on Commit job:** The user creates a CI job on one branch (For example, _Integration_). If any **Commits** are made on that branch on the remote, we will only perform the **Pull (Delta changes)** and then prepare the **Package**. This is why the build time is shorter.

**Build on PR submission:** CI job is created on the base branch (For example, **Integration**). If the developer works on the **Feature 1** branch and creates the **PR** on the **Integration** branch, the job gets triggered in ARM. The branch will switch to the **Feature 1** branch, take the clone of the entire branch, prepare the changes between the two branches, and switch back to the master branch once the job is completed. This is why the build time is longer for PR jobs.

## 5. Why is a CI job failing with the error ‘HTTP ERROR 405 Problem accessing /services/Soap/m/55.0. Reason: Only POST allowed’? <a href="#5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on" id="5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on"></a>

The authentication for your destination org may have expired. Please **Re-authenticate** your target Salesforce org. Once this is done successfully, please Edit and resave the CI job, then retrigger it.

## 6. Why are the FLS changes in the CI job reflected in the diff file but not in the sandbox? <a href="#6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox" id="6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox"></a>

This usually happens if the **Ignore missing visibility** checkbox is selected in CI Job. Another possibility is that the field in question is unavailable in the destination org where the FLS was deployed. Please contact our support team to determine the root cause and assist you further.

## 7. I cannot push components from branch to org in CI Job. What is the ‘Maximum size of request reached’ error? <a href="#7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re" id="7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re"></a>

Based on the error, this may be due to the file size limit. We request you break down deployments into smaller chunks to be successful. Please refer to the Salesforce article below about the file size limits for deployments:\
[Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.salesforce\_app\_limits\_cheatsheet.meta/salesforce\_app\_limits\_cheatsheet/salesforce\_app\_limits\_platform\_metadata.htm)

## 8. How do User Credentials impact different types of CI jobs? <a href="#8-how-do-user-credentials-impact-different-types-of-ci-jobs" id="8-how-do-user-credentials-impact-different-types-of-ci-jobs"></a>

Below are the types of CI jobs and their corresponding credential usage:

1. **Forced/manually triggered build:**\
   CI job process will consider the triggered **User Credential** mapped with the respective Repo and Branch in the **My Profile** section.\
   If the credentials are invalid/expired, authentication fails, and the following error message is displayed upon build initiation: _**Validation Checking failed. Version Control Mappings not found for Repo: ”test\_repo” and Branch: “test\_branch“. Please update it in 'My Profile'.**_\
   To resolve this issue, the user initiating the build must **update the credentials** in **My Profile** and perform a **Test Connection**. If it is successful, reinitiate the CI job.
2. **Build on Commit and Scheduled CI Job:**\
   CI job process will consider the **last modifying user's credentials** mapped with the respective Repo and Branch in the **My Profile** section.\
   If the credentials are invalid/expired, the CI job build fails, and the following authentication error message is displayed in the CI job Build log: _**Validation Checking failed. Version Control Mappings not found for Repo: ”test\_repo” and Branch: “test\_branch. “ Please update it in 'My Profile.'**_\
   To resolve this issue, the user who last modified the CI job must **update the credentials** in **My Profile** and perform a **Test Connection**. The job will be executed in the next cycle if it is successful.
3. **CI job build initiated from API:**\
   CI job process will consider the **Token** user credential mapped to the respective Repo and Branch in the **'My Profile'** section.\
   If the credentials are invalid/expired, the CI job build fails, and an authentication error message is displayed in the CI job Build log.\
   To resolve this issue, the user generating the token must update the credentials in **My Profile** and perform a **Test Connection**. The job will be executed in the next cycle if it is successful.

## 9. Why is CI Jobs deploying a metadata type I deselected in the ‘Exclude Metadata Types’ section? <a href="#9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section" id="9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section"></a>

If you have deselected a metadata type, but it is still being deployed in CI jobs, it could be because of a different name. Please verify that the **folderName** committed in Git is correct for the metadata. This should resolve the issue; if not, contact our support team for further analysis.

## 10. Why is a CI job running random test classes for production deployment, even though there are no Apex classes in the build, causing the deployments to fail? <a href="#10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap" id="10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap"></a>

You might have selected the option to **Include default Apex tests for run tests based on changes** under **Admin**-->**Salesforce settings**, so even though there are no classes in the package, it's still running default classes for code coverage. This is an expected behavior.

## 11. Why am I getting an error while accessing 3-month-old CI job builds? <a href="#11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds" id="11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds"></a>

The reason you are unable to get the details of specific builds older than 3 months is due to ARM’s **Retention Policy**. There are some details which are archived and become unretrievable.

You can change the retention period to 6 months or 12 months from the **Admin** section of your ARM account.

## 12. Why is a CI job failing with an error during validation? <a href="#12-why-is-a-ci-job-failing-with-an-error-during-validation" id="12-why-is-a-ci-job-failing-with-an-error-during-validation"></a>

The deployment may fail if it does not detect the metadata root folder path ‘src.’ Please update the Branch settings and then re-save the CI Job.

You can then perform a Merge Request to trigger the CI job and validate the deployment.

## 13. How do I include destructive changes in a CI job? <a href="#13-how-do-i-include-destructive-changes-in-a-ci-job" id="13-how-do-i-include-destructive-changes-in-a-ci-job"></a>

Review this [Knowledge Base article](https://knowledgebase.autorabit.com/arm/docs/destructive-changes) covering destructive changes through CI jobs.

## 14. The ‘File Changes’ tab shows that the Quick Actions metadata type is deleted. Why isn’t this reflected in the Destructive Changes tab or the package XML? <a href="#14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte" id="14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte"></a>

This may be a **GIT** behavior where the **QuickAction** metadata members are added and deleted again. As per GIT behavior, when it has to generate the delta between **From** and **To** revisions, it skips such files from package preparation in case of a conflict.\
There is no Git logic under **File Diff** because it simply displays what was **added/modified/deleted** for better UI visibility to understand the changes and be reviewed.\
You can work around this by **updating the baseline** revision **CI job** and using **Single Revision** in the **Deployment** module.

## 15. Why am I getting the 'License is not valid' error when using CodeScan as the analysis tool while running a CI job in ARM? <a href="#15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool" id="15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool"></a>

This could be due to using an older version of CodeScan. Refer to the [CodeScan License Errors](https://knowledgebase.autorabit.com/codescan/docs/license-errors#version-errors) article for further information.

## 16. Why are duplicate cycles triggered for the CI job, one iteration with changes and another with 'No Modifications'? <a href="#16-why-are-duplicate-cycles-being-triggered-for-ci-job-one-iteration-with-changes-and-another-with-n" id="16-why-are-duplicate-cycles-being-triggered-for-ci-job-one-iteration-with-changes-and-another-with-n"></a>

Duplicate cycles for CI jobs can occur when configuring a CI job as a child job for **Post** activities for the parent job and then configuring the same child job to **Trigger Build on Commit**. In this case, initiating two parallel cycles is possible, generating a duplicate cycle - one with the actual changes and the other with '_No Modifications_'.\
To prevent this duplicity, avoid choosing the CI job as a child CI job in post activities if it is a **Trigger Buid on Commit** CI job, and vice versa.

## 17. Why are Webhook-enabled CI Jobs not triggered after committing to the branch? <a href="#17-why-are-webhookenabled-ci-jobs-not-triggered-after-committing-to-the-branch" id="17-why-are-webhookenabled-ci-jobs-not-triggered-after-committing-to-the-branch"></a>

Before troubleshooting the issue, please ensure the following:

* CI job is configured with the **Build on Commit** option.
* Webhook is configured in the remote repository. Refer [here](https://knowledgebase.autorabit.com/docs/configure-a-webhook-in-github) for a details article on configuring webhook.

One of the following factors could prevent a CI job build with a webhook from being triggered upon commit:

*   **Response Code:** If the response code in the remote **Manage Webhook** section (for example: GITHUB _Recent Deliveries_) is not **200**, there may be a problem with the **Webhook URL** configuration.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-TO32LJAG.png)

    To resolve this, **edit** the CI job from the **CI Job List** page, select the **Trigger Build on Commit** checkbox to retrieve the Webhook URL, and configure it in your version control system (GitHub, BitBucket, etc.)
* **Repository URL:** If the URL registered in ARM does not match the one in the webhook request, you cannot simply edit it in ARM. You must re-register the repository from **Admin > VC Repo's > Register Repository** and use the Repository URL provided by your VCS.
*   **Content type:** If the content type is set to any option other than **application/json** in the webhook configuration, you must edit the webhook configuration and select the **Content-Type** as **application/json**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XAEC7AVJ.png" alt=""><figcaption></figcaption></figure>

    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-4973O6UZ.png)

After you check the factor responsible and perform the respective resolution steps, the next time there is a Commit to the branch, the webhook-enabled CI job build will be triggered.

## 18. Why are Metadata Changes missing from the Build package? <a href="#18-why-are-metadata-changes-missing-from-the-build-package" id="18-why-are-metadata-changes-missing-from-the-build-package"></a>

Metadata changes may be missing from the build package due to one of the following reasons:

* The metadata is excluded globally in the **My Account** section. To check, go to **Admin > My Account > Salesforce Settings**, and remove any metadata types if they're present in the **Excluded Metadata Types** column.
* If the **Build** source is **Version Control**, the metadata changes are considered based on the **Git Diff**. Ensure that the metadata changes missing from the build package are present within the **from** and **to** revisions. For example:\
  _git diff --name-status {fromrevision}...{torevision}_\
  _git diff --name-status 50b480a...6087df2_\
  ARM will only consider the above output files in the build.
