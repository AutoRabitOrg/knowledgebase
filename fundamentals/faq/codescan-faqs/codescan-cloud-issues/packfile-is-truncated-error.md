# 'Packfile is truncated' error

**Error:** While analyzing the project, you may encounter a “Packfile is truncated” error.&#x20;

**Cause**: Initially, access to CodeScan was denied on GitHub.&#x20;

**Resolution:**

1. **Check Access:** Verify if you have the necessary access to CodeScan in GitHub.
2. **Grant Access:** If access is denied, request and obtain the required permissions for CodeScan.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. **Retry Analysis:** After granting access to CodeScan in GitHub and integrating it with CodeScan, start the connection, then reattempt the project analysis. The error should no longer appear. The repositories should be synced. CodeScan should indicate the analysis was triggered, and the user should see the issues.
