# Working with VSCode Extension

### A. Create Pre-validation Request

Create a pre-validation request to commit from your local [version control](https://www.autorabit.com/7-tips-for-salesforce-version-control-integration/) repository.

<figure><img src="../../../../.gitbook/assets/image (889).png" alt="Pre-validation request creation in VSCode Extension"><figcaption>Creating a pre-validation request</figcaption></figure>

### B. Stage Changes

#### Stage all changes

<figure><img src="../../../../.gitbook/assets/image (890).png" alt="Staging all changes in VSCode Extension"><figcaption>Stage all changes</figcaption></figure>

#### Stage changes for a file

<figure><img src="../../../../.gitbook/assets/image (891).png" alt="Staging changes for a single file in VSCode Extension"><figcaption>Stage changes for a file</figcaption></figure>

#### Stage selective line of code

<figure><img src="../../../../.gitbook/assets/image (892).png" alt="Staging selected lines of code in VSCode Extension"><figcaption>Stage selective line of code</figcaption></figure>

### C. Submit Pre-validation Request

While submitting the pre-validation request, you may choose the following criteria as pre-checks:

1. Generate Diff Report
2. Run Static code analysis
3. Validate deployment

#### Generate Diff report

AutoRABIT compares the metadata between the source org and the destination branch and generates a metadata difference report. The diff report shows a summary of metadata component differences between the org and the branch.

#### Run Static code analysis

[Static code analysis](https://www.codescan.io/blog/what-is-salesforce-static-code-analysis/) detects data flow problems, software defects, language implementation errors, inconsistencies, dangerous usage, coding standard violations, and security vulnerabilities, if any.

#### Validate Deployment

AutoRABIT performs a check-only deployment to your selected org/branch. Nothing is deployed; however, if the deployment fails or tests do not pass, the issues will be clearly shown so they can be resolved.

<figure><img src="../../../../.gitbook/assets/image (893).png" alt="Pre-validation request options in VSCode Extension"><figcaption>Submit pre-validation with selected checks</figcaption></figure>

### D. Commit approved pre-validation request

Commit the code once the pre-validation request has been approved.

<figure><img src="../../../../.gitbook/assets/image (894).png" alt="Committing approved pre-validation request in VSCode Extension"><figcaption>Commit approved request</figcaption></figure>

### E. View Pre-validation Requests

#### Diff Report

<figure><img src="../../../../.gitbook/assets/image (895).png" alt="Viewing diff report in VSCode Extension"><figcaption>Diff Report</figcaption></figure>

#### Static Code Analysis Report

<figure><img src="../../../../.gitbook/assets/image (896).png" alt="Viewing static code analysis report in VSCode Extension"><figcaption>Static Code Analysis Report</figcaption></figure>

#### Validate Deployment Report

<figure><img src="../../../../.gitbook/assets/image (897).png" alt="Viewing deployment validation report in VSCode Extension"><figcaption>Validate Deployment Report</figcaption></figure>

### F. Trigger Build

This extension also allows developers to trigger builds once the code is committed. Actions like Quick Deploy and Abort are available for each build.

<figure><img src="../../../../.gitbook/assets/image (898).png" alt="Triggering builds using VSCode Extension" width="563"><figcaption>Triggering a build</figcaption></figure>

### G. Deployments

Use the extension to view results for pre-validations, builds, and deployments.

<figure><img src="../../../../.gitbook/assets/image (899).png" alt="Viewing deployment results in VSCode Extension" width="563"><figcaption>Viewing deployments</figcaption></figure>
