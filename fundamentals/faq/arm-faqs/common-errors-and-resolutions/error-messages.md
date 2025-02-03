# Error Messages

### OAuth Authentication Failed

Users may encounter this error when trying to register a Salesforce environment in ARM. This occurs when users do not use the My Domain URL when adding the Salesforce org to ARM. To correct this error, use **My Domain URL** while registering a Salesforce org in ARM.

### Unable to fetch Salesforce Org Users

This error may be encountered when a user tries to access the Salesforce Org in the ARM Version Control, CI Jobs, Deployment, and SFDX Modules. This may occur due to:

* Invalid username, password, or security token
* User is locked out
* Salesforce API version is incorrectly configured

Upgrade the API source flow in your Salesforce org to the most recent version and maintain the same Salesforce version in ARM by going to **Admin > My Account > My Salesforce Settings** and updating the API version.

### Uploaded file is not having Workflow Rules

This occur may occur when environment provisioning jobs are failing due to using the wrong file format for the **package.xml** file. Upload the correct package.xml file during the creation of environment provisioning jobs.
