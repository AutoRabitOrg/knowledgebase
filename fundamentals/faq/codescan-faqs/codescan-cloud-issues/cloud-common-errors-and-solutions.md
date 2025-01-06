# Cloud - Common Errors and Solutions

## CodeScan Cloud

### Common Errors and Solutions

#### Why am I getting the error 'Background tasks failing'?&#x20;

This error either occurs if it’s out of memory or when multiple analyses have been triggered at the same time. The analysis triggered last gets completed first.

#### Why am I getting a 'Packfile is truncated' error?

While analyzing the project, you may encounter a “Packfile is truncated” error. Initially, access to CodeScan was denied on GitHub.&#x20;

**Resolution:**

1. **Check Access:** Verify if you have the necessary access to CodeScan in GitHub.
2. **Grant Access:** If access is denied, request and obtain the required permissions for CodeScan.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FtBr5qh68WOHLi6xxUuMk%252Fimage.png%3Falt%3Dmedia%26token%3D5c13835b-da26-4a57-9e5b-f2811adfab2b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a4c1dec5&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. **Retry Analysis:** After granting access to CodeScan in GitHub and integrating it with CodeScan, start the connection, then reattempt the project analysis. The error should no longer appear. The repositories should be synced. CodeScan should indicate the analysis was triggered, and the user should see the issues.
