# Error Messages

### 413: Status Error

Users may encounter a **413-status error** in the browser console when trying to upload duplicate profile files that have been resolved after downloading from version control. This occurs when users try to download numerous files at one time. Download one profile file at a time to resolve the error.

### Authentication Failed

This error may occur when users are selecting an ALM on the EZ-Commit screen. This occurs due to:

* VPN connectivity appears to be the source of intermittent ALM connectivity issues.
* ALM is incorrectly configured.

To correct this issue:

1. On the **My Account** screen, look for the ALM configuration. To reauthenticate your ALM configuration, click the **Test Connection** icon to verify your credentials.
2. If the steps above do not work, create a new credential and link it to your ALM account.

### **Cannot Open Git-Upload-Pack**&#x20;

Users may encounter this error message when trying to register the Bitbucket repository. This occurs when:

* The Bitbucket account is locked.
* When registering the Bitbucket repository, the wrong credentials were used.
* The IT/Network team has whitelisted ARM's IP address.

To resolve this issue:

* Try recreating a new credential and updating the credentials under the **Admin > Credential** section.
* Re-register your bitbucket repository in ARM.

### Failed to initiate deployment. Unexpected end of JSON input.

When running a CI job, if any of the folders in the remote repository has an empty **JSON** file, that will cause SFDX commands to fail with an incorrect JSON error. Delete the **empty JSON file(s)** from the remote repository to resolve this issue and re-run the CI job.

### **GH006: Protected branch update failed for refs/heads/master. Remote: error: Cannot force-push to a protected branch.**

This error may be encountered while attempting to commit changes for a production organization to the GitHub master branch. This occurred because protected branches are not allow force pushes. Get in touch with your Administrator to turn off the protection on that branch.

### GIT Push Result: RemoteRefUpdate\[remoteName=refs/heads/release/CI\_UAT2\_Refresh, REJECTED\_OTHER\_REASON, 3235de0aa8e9edd83ab68d4d723c0301847caf78...9b4c80cea9e7217aa7d16486f1f30b609406c2f1, fastForward, srcRef=refs/heads/release/CI\_UAT2\_Refresh, message="pre-receive hook declined"] Status of the GIT Push process: REJECTED\_OTHER\_REASON

Multiple Branching Baseline jobs show no local modifications to commit. As a result the following error message is thrown. This occurs when one of your commit messages is missing a valid issue key:

&#x20; 9b4c80c: Commit From AutoRABIT \[Branch Baseline] \[LabelName:UAT2 Baseline]

Cross-verify the following things:

Create a new repository link where the key should include part of the commit comment from AutoRABIT.

(or)

Modify the existing Repository Link’s Key to align with the AutoRABIT Branching Baseline commit comment.

(or)

Disable the Repository Link.

For more content, go through![](<../../../../.gitbook/assets/image (783).png>)[Link to a web service | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/link-to-a-web-service/)

### **Invalid meta-xml name: lwc/xxx/xxx.css-meta.xml, should end with js-meta.xml**

When a deployment fails, this error usually occurs due to behavior in the Salesforce CLI 7.83 version. When retrieving the LWC components, it retrieves .css-meta.xml rather than .js-meta.xml file, which results in the deployment failing. Try renaming the .css-meta.xml file to .js-meta.xml and running the deployment again.

### Job too long after 1 hour of analysis

In CodeScan Cloud, the default setting for unit test timeouts is **1 hour (3600 seconds)** for limited Metadata analysis. These timeouts might not be enough if your project has a lot of metadata. This is the reason behind the error message.

Increase the timeouts to avoid this problem:

1. Click **Project Settings > General Settings** in your Project Overview.
2. Click the **CodeScan** tab on the left and modify the timeout under the **Unit Test Timeout** once you're in **General Settings**.

For detailed information on how to change the timeouts, click [HERE](https://knowledgebase.autorabit.com/codescan/docs/unit-test-timeout).

### Not Authorized (to Merge)

This error message occurs when performing a merge when credentials are not properly mapped in ARM. Follow the steps below to resolve this issue.

1. In Azure, create a new token.
2. In ARM, go to **Admin > Credential** and create a new credential.
3. Re-test the connection after mapping the credential to your version control branch (in the _**Profile**_ section).

If the test connection for the mapped repository and branch fails, we recommend upgrading your password and altering the credential in the credential section, then retrying the connection.

### OAuth Authentication Failed

Users may encounter this error when trying to register a Salesforce environment in ARM. This occurs when users do not use the My Domain URL when adding the Salesforce org to ARM. To correct this error, use **My Domain URL** while registering a Salesforce org in ARM.

### **Permission Import Personal Contacts depends on permission(s): create account, Create Contact, Edit Account, Edit Contact**

Please refer to this article, [https://developer.salesforce.com/forums/?id=906F00000008lFkIAI](https://developer.salesforce.com/forums/?id=906F00000008lFkIAI)​Comment

### **Permissions Read All ServiceTerritory depends on permission(s): Read All OperatingHours**

Please refer to this article, [https://developer.salesforce.com/forums/?id=906F0000000AkbzIAC](https://developer.salesforce.com/forums/?id=906F0000000AkbzIAC)

### Please check credentials for 'xxx' branch of 'abc' repository

Users may encounter this error when trying to connect to the Bitbucket repo, which typically relates to user permissions.  If you are using the wrong file format for the **package.xml,** then the above error occurs. Check the permissions you have on your Bitbucket repository with the repository owner/administrator. Request permissions other users have if you don't have the needed permissions.

### Schema is invalid

Users may encounter this error when a merge is failing for metadata members. This is due to an invalid structure. If there are any **special characters** like '**>**', '**<**', '**|**', '**=**', and the **string(length =7)**, this is considered a GIT conflict (a GIT behavior), which will cause the merge to fail. To prevent this, we recommend that you limit the previously mentioned unique characters to less than seven (7).&#x20;

For example, if you observe ">>>>>>>" character string(length =7) in any of the Apex Class files or any metadata member files, then update it to less than 7 in the branch itself and re-run the Merge.

### **Schema is invalid for the file**

Users may encounter this error when trying to perform a merge due to invalid characters like (>>>, <<<) symbols used in the file. To resolve, download the merge conflict files and validate the characters present in those XML files.

### SCM Authentication Failed

When a commit returns this error, it is either because:&#x20;

* Version control mapped to your Salesforce org user is incorrect.
* Your user credentials are incorrectly configured in ARM.

1. Ensure your account is correctly mapped with the version control branch to reflect the commits under your name.
2. Verify your credentials in the **Admin > Credential Manager** section and authenticate the connection again.

### **TF402455: Pushes to this branch are not permitted; you must use a pull request to update this branch.**

This error may be encountered while attempting to commit changes for the production organization to the GitHub master branch.  This is expected. When the branch is set with the branch policy, you cannot push it directly and need to create a pull request to update it. Once you remove the branch policy, you should have the ability to push changes to the master branch. Please contact the GitHub Administrator to request push permissions.

### **The layout Must Contain an item for the required layout field: IsnonStandard**

Please refer to this article, [https://developer.salesforce.com/forums/?id=906F00000008sDkIAI](https://developer.salesforce.com/forums/?id=906F00000008sDkIAI)

### **This test is already in the execution queue**

When generating a code coverage report for a registered Salesforce org, the test fails with this error if the Apex test execution takes a long time. Go to **TAF > Apex Test Execution** and clear all of the tests in the queue, then run the code coverage report through ARM again.

### Unable to fetch Salesforce Org Users

This error may be encountered when a user tries to access the Salesforce Org in the ARM Version Control, CI Jobs, Deployment, and SFDX Modules. This may occur due to an invalid username, password, or security token, if the user is locked out, or if the Salesforce API version is incorrectly configured.&#x20;

Upgrade the API source flow in your Salesforce org to the most recent version and maintain the same Salesforce version in ARM by going to **Admin > My Account > My Salesforce Settings** and updating the API version.

### Uploaded file is not having Workflow Rules

This occur may occur when environment provisioning jobs are failing due to using the wrong file format for the **package.xml** file. Upload the correct package.xml file during the creation of environment provisioning jobs.

### Validation checking fails for your repository

Users may encounter this error message when a Merge is failed. This occurs when repository credentials are expired or have been modified and not updated in ARM.&#x20;

1. Navigate to **Admin > VC repos**, select your repository, and perform a test connection. Please verify your repository credentials are not expired or modified.
2. Re-run the CI job after you confirm that the repository connection is successful.

### **You are not authorized to push changes to the remote repository**

This error occurs during the branching baseline operation when version control credentials are insufficient for pushing changes to a branch. This indicates that you have read permissions but not write permissions. After updating your permissions, re-run a new branching baseline operation.

### Your connection is private.

If you are unable to connect to the ARM instance and get this error, it is due to cache and cookies in your system. To resolve this issue, follow the steps below.

1. On your computer, open **Chrome**.
2. At the top right, click **More**.
3. Click **More tools**.
4. Clear **browsing data**.
5. At the top, choose a **time range**. To delete everything, select **All time**.
6. Next to **Cookies and other site data** and **Cached images and files,** check the boxes.
7. Click **Clear data**.
8. Now, log in to your instances using the new browser tab.

### Why am I getting an error when I try to install CodeScan Sonar as a plugin in ARM? <a href="#why-am-i-getting-an-error-when-i-try-to-install-codescan-sonar-as-a-plugin-in-arm" id="why-am-i-getting-an-error-when-i-try-to-install-codescan-sonar-as-a-plugin-in-arm"></a>

You're getting an error because you're using an old version of CodeScan. Install the most recent version of CodeScan to avoid any installation errors.



