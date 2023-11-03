# Error: "Please check credentials for 'xxx' branch of 'abc' repository"

### Description

While trying to connect to the Bitbucket repo, the ARM application throws the error: **"Please check credentials for 'xxx' branch of 'abc' repository"**

### Cause

This seems to issue with the user permissions. If you are using the wrong file format for the **package.xml,** then the above error occurs.

### Resolution

1. Check the permissions you have on your Bitbucket repository with the repository owner/administrator.
2. Request the permissions that the other users have if you don't have enough permission.
