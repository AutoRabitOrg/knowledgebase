# CI Jobs

#### 1. When will the "Quick Deploy" option be available in a CI Job? <a href="#id-1-when-quick-deploy-option-will-be-available-in-ci-job" id="id-1-when-quick-deploy-option-will-be-available-in-ci-job"></a>

Quick deployments are available when the following requirements are met.

* The components have been validated successfully for the target environment.
* As part of the validation, Apex tests in the target org have passed.
* Code coverage requirements are met.
* If all tests in the org or all local tests are run, overall code coverage is at least _75%_, and Apex triggers have some coverage.
* If specific tests are run with the _Run specified tests_ test level, each class and trigger that was deployed is covered by at least 75% individually.
* The 'Prevent Deployment' checkbox is NOT selected in the CI Job setting.

#### 2. Why isn't the CI Job able to choose the changes for commits that have already been validated? <a href="#id-2-why-isnt-the-ci-job-able-to-choose-the-changes-for-commits-that-have-already-been-validated" id="id-2-why-isnt-the-ci-job-able-to-choose-the-changes-for-commits-that-have-already-been-validated"></a>

If the baseline revisions aren't picking up the two revisions, clear the baseline revision and choose the same revision again.

#### 3. Why am I not receiving email notifications for all CI jobs that AutoRABIT has initiated? <a href="#id-3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated" id="id-3-why-am-i-not-receiving-email-notifications-for-all-ci-jobs-that-autorabit-has-initiated"></a>

You might have exceeded the maximum number of recipients; the maximum number of recipients should not exceed 50. Remove some of the recipients from the mail notification list and run the CI job again; you should now receive email notifications.

#### 4. Why is it taking longer to build CI jobs triggered on PR submission as compared to CI jobs triggered on Commit? <a href="#id-4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger" id="id-4-why-is-it-taking-longer-to-build-ci-jobs-triggered-on-pr-submission-as-compared-to-ci-jobs-trigger"></a>

**Build on Commit job:** The user creates a CI job on one branch (For example, _Integration_). If any **Commits** are made on that branch on the remote, we will only perform the **Pull (Delta changes)**, and then prepare the **Package**. This is why the build time is shorter.

**Build on PR submission:** CI job is created on the base branch (For example, **Integration**). If the developer works on the **Feature 1** branch and creates the **PR** on the **Integration** branch, then the job gets triggered in ARM. The branch will switch to the **Feature 1** branch, take the clone of the entire branch, prepare the changes between the two branches, and the switch back to master branch once the job is completed. This is why the build time is longer for PR jobs.

#### 5. Why is a CI job failing with the error ‘HTTP ERROR 405 Problem accessing /services/Soap/m/55.0. Reason: Only POST allowed’? <a href="#id-5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on" id="id-5-why-is-a-ci-job-failing-with-the-error-http-error-405-problem-accessing-servicessoapm550-reason-on"></a>

The authentication for your destination org may have expired. Please **Re-authenticate** your target Salesforce org. Once this is done successfully, please Edit and resave the CI job, then retrigger it.

#### 6. Why are the FLS changes in the CI job reflected in the diff file but not in the sandbox? <a href="#id-6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox" id="id-6-why-are-the-fls-changes-in-the-ci-job-reflected-in-the-diff-file-but-not-in-the-sandbox"></a>

This usually happens if the **Ignore missing visibility** checkbox is selected in CI Job. Another possibility is that the field in question is unavailable in the destination org where the FLS was deployed. Please contact our support team to determine the root cause and assist you further.

#### 7. I am unable to push components from branch to org in CI Job. What is the ‘Maximum size of request reached’ error? <a href="#id-7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re" id="id-7-i-am-unable-to-push-components-from-branch-to-org-in-ci-job-what-is-the-maximum-size-of-request-re"></a>

Based on the error, this may be due to the file size limit. We request you break down deployments into smaller chunks to be successful. Please refer to the Salesforce article below about the file size limits for deployments:\
[Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.salesforce\_app\_limits\_cheatsheet.meta/salesforce\_app\_limits\_cheatsheet/salesforce\_app\_limits\_platform\_metadata.htm)

#### 8. How does the User Credentials impact different types of CI jobs? <a href="#id-8-how-does-the-user-credentials-impact-different-types-of-ci-jobs" id="id-8-how-does-the-user-credentials-impact-different-types-of-ci-jobs"></a>

Below are the types of CI jobs and their corresponding credential usage:

1. **Forced/Manually Triggered Build:**\
   CI job process will consider the triggered **User Credential** which is mapped with the respective Repo and Branch in the **My Profile** section.\
   If the credentials are invalid/expired, authentication fails and an error message is displayed upon build initiation.\
   To resolve this issue, the user initiating the build must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, reinitate the CI job.
2. **Build on Commit and Scheduled CI Job:**\
   CI job process will consider the last modifying user's credentials which is mapped with the respective Repo and Branch in the **My Profile** section.\
   If the credentials are invalid/expired, the CI job build fails and authentication error message is displayed in the CI job Build log.\
   To resolve this issue, the user who last modified the CI job must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, the job will be executed in the next cycle.
3. **CI job build initiated from API:**\
   CI Job process will consider the **Token** user credential which is mapped with the respective Repo and Branch in the **My Profile** section.\
   If the credentials are invalid/expired, the CI job build fails and authentication error message is displayed in the CI job Build log.\
   To resolve this issue, user generating the token must update the credentials in **My Profile** and perform a **Test Connection**. If it is successful, the job will be executed in the next cycle.

#### 9. Why is CI Jobs deploying a metadata type I deselected in the ‘Exclude Metadata Types’ section? <a href="#id-9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section" id="id-9-why-is-ci-jobs-deploying-a-metadata-type-i-deselected-in-the-exclude-metadata-types-section"></a>

If you have deselected a metadata type but it is still being deployed in CI jobs, then it could be because of a different name. Please verify that the **folderName** committed in Git is correct for the metadata. This should resolve the issue. If it doesn’t, contact our support team for further analysis.

#### 10. Why is a CI job for production deployment running random test classes, even though there are no Apex classes in the build, causing the deployments to fail? <a href="#id-10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap" id="id-10-why-is-a-ci-job-for-production-deployment-running-random-test-classes-even-though-there-are-no-ap"></a>

You might have selected the option to **Include default Apex tests for run test based on changes** under **Admin**-->**Salesforce settings**, so even though there are no classes present in the package, it's still running default classes for code coverage. This is an expected behavior.

#### 11. Why am I getting an error while trying to access 3-month-old CI job builds? <a href="#id-11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds" id="id-11-why-am-i-getting-an-error-while-trying-to-access-3monthold-ci-job-builds"></a>

The reason you are unable to get the details of specific builds older than 3 months is due to ARM’s **Retention Policy**. There are some details which are archived and become unretrievable.

You can change the retention period to 6 months or 12 months from the **Admin** section of your ARM account.

#### 12. Why is a CI job failing with an error during validation? <a href="#id-12-why-is-a-ci-job-failing-with-an-error-during-validation" id="id-12-why-is-a-ci-job-failing-with-an-error-during-validation"></a>

The deployment may fail if it does not detect the metadata root folder path ‘src.’ Please update the Branch settings and then re-save the CI Job.

You can then perform a Merge Request to trigger the CI job and validate the deployment.

#### 13. How do I include destructive changes in a CI job? <a href="#id-13-how-do-i-include-destructive-changes-in-a-ci-job" id="id-13-how-do-i-include-destructive-changes-in-a-ci-job"></a>

Review this [Knowledge Base article](../../product-guides/arm/arm-features/deployment/destructive-changes.md), which covers performing destructive changes through CI jobs.

#### 14. The ‘File Changes’ tab shows that the Quick Actions metadata type is deleted. Why isn’t this reflected in the Destructive Changes tab or the package xml? <a href="#id-14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte" id="id-14-the-file-changes-tab-shows-that-the-quick-actions-metadata-type-is-deleted-why-isnt-this-reflecte"></a>

This may be a **GIT** behavior where the **QuickAction** metadata members are added and deleted again. As per GIT behavior, when it has to generate the delta between **From** and **To** revisions, in the case of a conflict, it skips such files from package preparation.\
There is no Git logic under **File Diff** because it simply displays what was **added/modified/deleted** for better UI visibility to understand the changes and be reviewed.\
You can work around this by **updating the baseline** revision **CI job** and using **Single Revision** in the **Deployment** module.

#### 15. Why am I getting the 'License is not valid' error when trying to use CodeScan as the analysis tool while running a CI job in ARM? <a href="#id-15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool" id="id-15-why-am-i-getting-the-license-is-not-valid-error-when-trying-to-use-codescan-as-the-analysis-tool"></a>

This could be due to using an older version of CodeScan. Refer to the [CodeScan License Errors](codescan-faqs/codescan-self-hosted-issues/license-errors.md) article for further information.

#### 16. **Why am I not getting a package for the CI Job?**

Packages will only be displayed in CI jobs if created or imported through our application's SFDX -> Packages module. This ensures that we accurately track packages and their versions.

To create or import the package, follow the articles below:

Create a Package: [Create an Unlocked/Managed Package | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/salesforce-dx/create-an-unlocked-managed-package)

Import a Package: [Import an Unlocked/Managed Package | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/salesforce-dx/import-an-unlocked-managed-package)

#### 17. What is causing the 'Not Eligible for Quick Deploy' popup after selecting 'Quick Deploy' in the CI Job?

This error will occur when the 'Prevent Deployment' checkbox is enabled in the CI Job setting. Deselect the checkbox, then proceed with the Quick Deploy.
