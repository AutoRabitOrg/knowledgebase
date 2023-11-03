# Error: "Not Authorized to Merge"

### Description

When I perform a merge, I get the following error: "Not authorized"

### Cause

You are experiencing this issue because your credentials were not properly mapped in the ARM application.

### Steps for Resolution

1. In Azure, create a new token.
2. In ARM, go to **Admin > Credential** and create a new credential.
3. Re-test the connection after mapping the credential to your version control branch (in the _**Profile**_ section).

If the test connection for the mapped repository and branch fails, we recommend upgrading your password and altering the credential in the credential section, then retrying the connection.
