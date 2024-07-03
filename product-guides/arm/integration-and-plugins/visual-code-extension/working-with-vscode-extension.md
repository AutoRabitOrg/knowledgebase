# Working with VSCode Extension

### A. Create Pre-validation Request

Create a pre-validation request to commit from your local [version control](https://www.autorabit.com/7-tips-for-salesforce-version-control-integration/) repository.

<figure><img src="../../../../.gitbook/assets/image (889).png" alt=""><figcaption></figcaption></figure>

### B. Stage Changes

#### Stage all changes

<figure><img src="../../../../.gitbook/assets/image (890).png" alt=""><figcaption></figcaption></figure>

#### Stage changes for a file

<figure><img src="../../../../.gitbook/assets/image (891).png" alt=""><figcaption></figcaption></figure>

#### Stage selective line of code

<figure><img src="../../../../.gitbook/assets/image (892).png" alt=""><figcaption></figcaption></figure>

### C. Submit Pre-validation Request

While submitting the pre-validation request, you may choose the below criteria as pre-checks:

1. Generate Diff Report
2. Run Static code analysis
3. Validate deployment

#### Generate Diff report

AutoRABIT compares the metadata between the source org and the destination branch and generates a metadata difference report. The diff report shows a summary of metadata components differences between the org and the branch.

#### Run Static code analysis

[Static code analysis](https://www.codescan.io/blog/what-is-salesforce-static-code-analysis/) will detect data flow problems, software defects, language implementation errors, inconsistencies, dangerous usage, coding standard violations, and security vulnerabilities if any.

#### Validate Deployment

AutoRABIT performs a check-only deployment to your selected org/branch. Nothing will be deployed however if anything goes wrong - for example, the deployment fails, or tests do not pass - we will show you exactly what happened, so you can fix it.

<figure><img src="../../../../.gitbook/assets/image (893).png" alt=""><figcaption></figcaption></figure>

### D. Commit approved pre-validation request

This will allow you to commit the code once the pre-validation request is approved.

<figure><img src="../../../../.gitbook/assets/image (894).png" alt=""><figcaption></figcaption></figure>

### E. View Pre-validation Requests

#### Diff Report

<figure><img src="../../../../.gitbook/assets/image (895).png" alt=""><figcaption></figcaption></figure>

#### Static Code Analysis Report

<figure><img src="../../../../.gitbook/assets/image (896).png" alt=""><figcaption></figcaption></figure>

#### Validate Deployment Report

<figure><img src="../../../../.gitbook/assets/image (897).png" alt=""><figcaption></figcaption></figure>

### F. Trigger Build

This extension will also allow developers to run builds once the code is committed. Different quick actions such as Quick Deploy, or Abort are associated to each build.

<figure><img src="../../../../.gitbook/assets/image (898).png" alt="" width="563"><figcaption></figcaption></figure>

### G. Deployments

This extension will allow viewing results for pre-validations, builds, and deployments.

<figure><img src="../../../../.gitbook/assets/image (899).png" alt="" width="563"><figcaption></figcaption></figure>
