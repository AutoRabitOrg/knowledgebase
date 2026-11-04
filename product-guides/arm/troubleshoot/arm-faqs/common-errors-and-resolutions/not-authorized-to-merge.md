# Not Authorized (to Merge)

## Error message: Not Authorized (to Merge)

This error message occurs when performing a merge when credentials are not properly mapped in ARM. Follow the steps below to resolve this issue.

1. In Azure, create a new token.
2. In ARM, go to **Admin > Credential** and create a new credential.
3. Re-test the connection after mapping the credential to your version control branch (in the _**Profile**_ section).

If the test connection for the mapped repository and branch fails, we recommend upgrading your password and altering the credential in the credential section, then retrying the connection.
