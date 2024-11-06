# Deployment-FAQs

## If you are getting the following errors during the deployment in ARM, refer to the corresponding Salesforce article to resolve the issue: <a href="#if-you-are-getting-the-below-errors-during-the-deployment-in-arm-follow-the-respective-salesforce-ar" id="if-you-are-getting-the-below-errors-during-the-deployment-in-arm-follow-the-respective-salesforce-ar"></a>

* For error: **The layout Must Contain an item for the required layout field: IsnonStandard,** please refer to this article: [https://developer.salesforce.com/forums/?id=906F00000008sDkIAI](https://developer.salesforce.com/forums/?id=906F00000008sDkIAI)
* For error: **Permission Import Personal Contacts depends on permission(s): create account, Create Contact, Edit Account, Edit Contact,** please refer to this article: [https://developer.salesforce.com/forums/?id=906F00000008lFkIAI](https://developer.salesforce.com/forums/?id=906F00000008lFkIAI)
* For error: **Permissions Read All ServiceTerritory depends on permission(s): Read All OperatingHours,** please refer to this article: [https://developer.salesforce.com/forums/?id=906F0000000AkbzIA](https://developer.salesforce.com/forums/?id=906F0000000AkbzIAC)

## Is it possible to transfer Analytics Dataset Metadata, Dashboards, and Dataflows from one Salesforce Org to another using AutoRABIT? <a href="#is-it-possible-to-transfer-analytics-dataset-metadata-dashboards-and-dataflows-from-one-salesforce-o" id="is-it-possible-to-transfer-analytics-dataset-metadata-dashboards-and-dataflows-from-one-salesforce-o"></a>

Yes, AutoRABIT can move Analytics Components Metadata, Dashboards, and Dataflows from one Salesforce Org to another Org and these data will be available under the **Wave Components** list.

When you want to deploy the Analytics data, make sure you have enabled **Tableau CRM** in your Source Org and should have assigned permissions to your user record page through the permission set.

To enable the Tableau CRM in your Salesforce Org, follow these steps:

1. Log in to your Salesforce account.
2. Go to **Salesforce Setup** and enter **Analytics** in the **Quick Find / Search** field.
3. Select **Getting Started**.
4. Click **Enable Tableau CRM**.

Before you enable this option, you must have a license for the Analytics platform and this permission in your AutoRABIT profile.

To learn more about how to set up the Analytics Platform, refer to: [https://blog.bessereau.eu/assets/pdfs/bi\_admin\_guide\_setup.pdf](https://blog.bessereau.eu/assets/pdfs/bi\_admin\_guide\_setup.pdf)

## How can I make the metadata components (ex: ReportType) available for commit and deployment? <a href="#how-can-i-make-the-metadata-components-ex-reporttype-available-for-commit-and-deployment" id="how-can-i-make-the-metadata-components-ex-reporttype-available-for-commit-and-deployment"></a>

Go to the **'My Salesforce Settings'** section of the **My Account** page to activate the metadata components. After that, select the metadata types you want to include in the **excluded metadata types**.

## Why am I unable to retrieve metadata components during deployment? <a href="#unable-to-retrieve-metadata-components-during-deployment" id="unable-to-retrieve-metadata-components-during-deployment"></a>

If you cannot retrieve the components in ARM, although the components are available in Salesforce Org, check for the Salesforce API version from which you're deploying. You can look for the Salesforce API configured for your account under **Admin > My Account > My Salesforce Settings** section.

## Why am I unable to access my Salesforce Production org? <a href="#i-am-unable-to-access-my-sf-production-org" id="i-am-unable-to-access-my-sf-production-org"></a>

1. When registering your production org, double-check the credentials.
2. Create a new API token for your Salesforce organization and re-enter your credentials with the new API token.

## Why does my deployment from one sandbox to another fail without errors? <a href="#when-i-try-to-deploy-one-sandbox-to-another-sandbox-it-fails-without-any-errors" id="when-i-try-to-deploy-one-sandbox-to-another-sandbox-it-fails-without-any-errors"></a>

This commonly occurs when the Salesforce API version in your ARM application is incorrectly configured. You must upgrade the API source flow in your Salesforce org to the most recent version and maintain the same Salesforce version in ARM. To do so, go to **Admin > My Account > My Salesforce Settings** and update the API version.

## Why am I unable to use AutoRABIT to deploy changes made to standard Salesforce fields? <a href="#im-unable-to-use-autorabit-to-deploy-changes-made-to-standard-salesforce-fields" id="im-unable-to-use-autorabit-to-deploy-changes-made-to-standard-salesforce-fields"></a>

One of the prominent causes is when the standard value set is not included in the commit. The deployment validation will succeed if you include it in addition to the standard field while committing.

When it's a _standard field_, we recommend including the **Standard Value Set** and selecting metadata from the picklist option. When it's a _custom field_, we recommend including the custom field.

## Why does my deployment not appear in the target org when I run CI Jobs in AutoRABIT? <a href="#why-does-my-deployment-not-appear-in-the-target-org-when-i-run-ci-jobs-in-autorabit" id="why-does-my-deployment-not-appear-in-the-target-org-when-i-run-ci-jobs-in-autorabit"></a>

You are unable to see your deployment in the target org if the CI job was configured with the remove system and user permissions. Run the deployment while unchecking the user permissions option to resolve the issue.

## When selecting the Autodraft features to commit the changes, why are some components missing? <a href="#when-selecting-the-autodraft-features-to-commit-the-changes-some-of-the-components-are-missing" id="when-selecting-the-autodraft-features-to-commit-the-changes-some-of-the-components-are-missing"></a>

This usually happens if you have used the filter with the most recent modified date rather than the source org's last modified date during the EZ-Commit process.

## How do I use ARM to deploy case assignment rules? <a href="#how-do-i-use-the-autorabit-to-deploy-case-assignment-rules" id="how-do-i-use-the-autorabit-to-deploy-case-assignment-rules"></a>

Go to the **Deployment** module and select the case assignment rule during the metadata retrieval process to pick the rules. Errors commonly encountered due to Salesforce issues are listed at the [top](deployment-faqs.md#if-you-are-getting-the-below-errors-during-the-deployment-in-arm-follow-the-respective-salesforce-ar) of this page.

## Where can I find the standard picklist values for my deployments in AutoRABIT? <a href="#where-can-i-find-the-standard-picklist-values-for-my-deployments-in-autorabit" id="where-can-i-find-the-standard-picklist-values-for-my-deployments-in-autorabit"></a>

You can see the standard picklist fields under standard value set metadata.

## Why am I unable to deploy the profile change from the version control repo to my target sandbox using a single revision?

Select the following checkboxes after picking up the required metadata and the profile members:

* **Commit Options for Profile:** This option allows you to commit settings for a full profile operation.
* **Commit Access Settings for selected metadata (Profiles ONLY):** This allows you to perform the commit operation based on the Profiles available only for the selected metadata.

## Can CI Jobs be deployed using the "Run Tests Based On Changes" option if some of the LWC components do not have test classes? <a href="#is-it-possible-to-deploy-ci-jobs-using-the-run-tests-based-on-changes-option-if-some-of-the-lwc-comp" id="is-it-possible-to-deploy-ci-jobs-using-the-run-tests-based-on-changes-option-if-some-of-the-lwc-comp"></a>

Yes, even if one of the LWC components does not have test classes, you can deploy by selecting **"Run Tests Based On Changes"** because the test is run on the existing test classes for the change-relevant components. Click [here](https://knowledgebase.autorabit.com/docs/apex-unit-tests) for more detailed information about deployment configurations.

## **Why are deployments based on revisions from a version control branch to my target environment failing?**

This occurs when the metadata folder path in the VC repository section is not configured. This problem will not occur once the **.src path** has been configured. For detailed information about how to configure the VC repository, click [here](https://knowledgebase.autorabit.com/docs/version-control-repositories-summary-page).

## Why don't I see the Release Label I created in the dropdown when performing a New Deployment?

It could be due to one of the following reasons:

* You have created a release label in **ARM version 22.2 or older**.
* You did not select the **Create package manifest for Deployment** checkbox while creating the release label in ARM 22.3.
* You selected the **Create package manifest for Deployment** checkbox, but the package preparation failed.

All of these problems can be solved by going to the **Release Label Summary** screen and clicking on **Create Artifact** for the respective release label. Once this is successful, the release label will be visible on the **New Deployment** page.

## Why did the deployment fail without any error message? <a href="#why-did-the-deployment-fail-without-any-error-message" id="why-did-the-deployment-fail-without-any-error-message"></a>

To resolve this issue, please reauthenticate the Salesforce org and perform the deployment again. If the issue continues, please contact our support team.

## Why is ARM not picking the latest activated version of the record trigger flow? <a href="#why-is-arm-not-picking-the-latest-activated-version-of-the-record-trigger-flow" id="why-is-arm-not-picking-the-latest-activated-version-of-the-record-trigger-flow"></a>

If you are trying to retrieve a recently updated **Flow** and not getting the latest metadata in the review artifact, modify the **Salesforce Metadata API** selected for the flow to the latest version, then retry the metadata retrieval. This time, you should see the latest metadata of the flow.

## Why is deployment on the Salesforce org through CI Job failing with an error? <a href="#why-is-deployment-on-the-salesforce-org-through-ci-job-failing-with-an-error" id="why-is-deployment-on-the-salesforce-org-through-ci-job-failing-with-an-error"></a>

Change the **baseline revision** under CI jobs, then perform the deployment again. This should resolve the issue.

## Why did the Release Label Merge fail with an error message on validation deployment? <a href="#why-did-the-release-label-merge-fail-with-an-error-message-on-validation-deployment" id="why-did-the-release-label-merge-fail-with-an-error-message-on-validation-deployment"></a>

One of the revisions in that **Release Label** may have duplicate values for the **Layout** file, as it could not pick the delta, so the validation failed. To resolve this:

1. Turn off **On Successful Mock Deployment** in the merge criteria and proceed with the merge, even though you have the validation deployment failure on the layout file.
2. Then manually modify the layout file on the target branch by removing the duplicate entries and triggering the CI Job deployment.
3. We recommend the same steps to avoid duplicates if you move changes into the Prod branch.

## While trying to deploy a profile from our development org to the UAT org using the Profile Manager option, why is the profile not being deployed correctly to the UAT org? <a href="#while-trying-to-deploy-a-profile-from-our-development-org-to-the-uat-org-using-the-profile-manager-o" id="while-trying-to-deploy-a-profile-from-our-development-org-to-the-uat-org-using-the-profile-manager-o"></a>

This type of issue can occur if you have a profile in your UAT org and want to deploy it to the clone org, but the profile does not exist in your target org. We recommend using the Full Profile option in the Deployment module to resolve this. Then trigger the deployment again; the profile should successfully deploy to your target org.

## Why did the quick deploy fail in ARM? <a href="#why-did-quick-deploy-fail-in-arm-but-restart-in-salesforce" id="why-did-quick-deploy-fail-in-arm-but-restart-in-salesforce"></a>

Quick Deploy may have failed due to the **Metadata API version**. Please update the Metadata API to the latest version and then perform the deployment again.

## What does the 'Ignore Missing Visibility Settings' option do, and how does it affect the Deployment? <a href="#what-does-the-ignore-missing-visibility-settings-option-do-and-what-effect-does-it-have-on-the-deplo" id="what-does-the-ignore-missing-visibility-settings-option-do-and-what-effect-does-it-have-on-the-deplo"></a>

The **'Ignore Missing Visibility Settings'** option refactors the **Profiles/Permissions** metadata.\
If users enable this option, the metadata that does not exist in the **target org members' access settings/permissions** will be removed from the package to reduce deployment failures.\
The following permissions are skipped if they're missing from the destination org:

* applicationVisibilities
* classAccesses
* customMetadataTypeAccesses
* fieldPermissions
* flowAccesses
* layoutAssignments
* objectPermissions
* page accesses
* recordTypeVisibilities
* tabVisibilities

{% hint style="info" %}
**Limitation**

This option only works for **List** metadata-retrieved components. List the metadata from the workbench to view the metadata types.
{% endhint %}

## Why does the Deployment appear as 'Failed' in ARM despite being successful in Salesforce? <a href="#why-does-the-deployment-appear-as-failed-in-arm-despite-being-successful-in-salesforce" id="why-does-the-deployment-appear-as-failed-in-arm-despite-being-successful-in-salesforce"></a>

If a deployment was successful in Salesforce but failed in ARM, this may be a Salesforce permission issue.

Please follow the troubleshooting steps given by Salesforce to enable the **Exempt from Transaction Security** permission: [https://issues.salesforce.com/issue/a028c00000gAwsxAAC/intermittent-transaction-security-policy-error-while-login-or-making-api-calls-to-salesforce-we-cant-complete-the-action-because-enabled-transaction](https://issues.salesforce.com/issue/a028c00000gAwsxAAC/intermittent-transaction-security-policy-error-while-login-or-making-api-calls-to-salesforce-we-cant-complete-the-action-because-enabled-transaction)

## **Various Deployment sources and their functionalities:** <a href="#various-deployment-sources-and-their-functionalities" id="various-deployment-sources-and-their-functionalities"></a>

**1. Deployment via Commit Label:** The entire files from the most recent revision under the commit label will be packaged together.\
**Example:** The entire profile will be part of the deployment.

**2. Deployment via Single Revision:** The delta change of the revision will be packaged.\
**Example:** If file permissions are included in the revision, only the file permissions will be considered as part of the change.

## Can I deploy standard fields throughout ARM?

Often, users who are having issues deploying HTML reports in AutoRABIT are not aware of an SFDC limitation. Unfortunately, AutoRABIT cannot deploy standard fields because they cannot be edited in Salesforce. They are restricted from the SFDC side. You can commit standard fields but cannot deploy them. &#x20;

