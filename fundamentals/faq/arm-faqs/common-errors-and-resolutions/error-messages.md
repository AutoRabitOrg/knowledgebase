# Error Messages

### Authentication Failed

This error may occur when users are selecting an ALM on the EZ-Commit screen. This occurs due to:

* VPN connectivity appears to be the source of intermittent ALM connectivity issues.
* ALM is incorrectly configured.

To correct this issue:

1. On the **My Account** screen, look for the ALM configuration. To reauthenticate your ALM configuration, click the **Test Connection** icon to verify your credentials.
2. If the steps above do not work, create a new credential and link it to your ALM account.

### OAuth Authentication Failed

Users may encounter this error when trying to register a Salesforce environment in ARM. This occurs when users do not use the My Domain URL when adding the Salesforce org to ARM. To correct this error, use **My Domain URL** while registering a Salesforce org in ARM.

### Please check credentials for 'xxx' branch of 'abc' repository

Users may encounter this error when trying to connect to the Bitbucket repo, which typically relates to user permissions.  If you are using the wrong file format for the **package.xml,** then the above error occurs. Check the permissions you have on your Bitbucket repository with the repository owner/administrator. Request permissions other users have if you don't have the needed permissions.

### Schema is invalid

Users may encounter this error when a merge is failing for metadata members. This is due to an invalid structure. If there are any **special characters** like '**>**', '**<**', '**|**', '**=**', and the **string(length =7)**, this is considered a GIT conflict (a GIT behavior), which will cause the merge to fail. To prevent this, we recommend that you limit the previously mentioned unique characters to less than seven (7).&#x20;

For example, if you observe ">>>>>>>" character string(length =7) in any of the Apex Class files or any metadata member files, then update it to less than 7 in the branch itself and re-run the Merge.

### **Schema is invalid for the file**

Users may encounter this error when trying to perform a merge due to invalid characters like (>>>, <<<) symbols used in the file. To resolve, download the merge conflict files and validate the characters present in those XML files.

### Unable to fetch Salesforce Org Users

This error may be encountered when a user tries to access the Salesforce Org in the ARM Version Control, CI Jobs, Deployment, and SFDX Modules. This may occur due to an invalid username, password, or security token, if the user is locked out, or if the Salesforce API version is incorrectly configured.&#x20;

Upgrade the API source flow in your Salesforce org to the most recent version and maintain the same Salesforce version in ARM by going to **Admin > My Account > My Salesforce Settings** and updating the API version.

### Uploaded file is not having Workflow Rules

This occur may occur when environment provisioning jobs are failing due to using the wrong file format for the **package.xml** file. Upload the correct package.xml file during the creation of environment provisioning jobs.

### Validation checking fails for your repository

Users may encounter this error message when a Merge is failed. This occurs when repository credentials are expired or have been modified and not updated in ARM.&#x20;

1. Navigate to **Admin > VC repos**, select your repository, and perform a test connection. Please verify your repository credentials are not expired or modified.
2. Re-run the CI job after you confirm that the repository connection is successful.



