# Error: "Job too long after 1 hour of analysis"

### Description

Why are my analysis status failing and I'm getting the error **"Job too long after 1 hour of analysis"** when using CodeScan as a code analysis tool?

### Cause

In CodeScan Cloud, the default setting for unit test timeouts is **1 hour (3600 seconds)** for limited Metadata analysis. These timeouts might not be enough if your project has a lot of metadata. This is the reason behind the error message.

### Steps for Resolution

Increase the timeouts to avoid problems like these. To increase the timeouts, follow the procedures below:

1. Click **Project Settings > General Settings** in your Project Overview.
2. Click the **CodeScan** tab on the left and modify the timeout under the **Unit Test Timeout** once you're in **General Settings**.

For detailed information on how to change the timeouts, click [HERE](https://knowledgebase.autorabit.com/codescan/docs/unit-test-timeout).

\
