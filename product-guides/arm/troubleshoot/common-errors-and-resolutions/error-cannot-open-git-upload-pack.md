# Error: "cannot open git-upload-pack"

### Description

ARM throws the following error: **"cannot open git-upload-pack,"** when trying to register the Bitbucket repository?

### Cause

* Your Bitbucket account is locked.
* When registering the Bitbucket repository, you used the wrong credentials.
* It is also possible that your IT/Network team has whitelisted ARM's IP address.

### Resolution

* Try recreating a new credential, and updating the credentials under the **Admin > Credential** section.
* Re-register your bitbucket repository once again in ARM.

\
