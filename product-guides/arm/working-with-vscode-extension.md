# Working with VSCode Extension

### A. Create Pre-validation Request

Create a pre-validation request to commit from your local [version control](https://www.autorabit.com/7-tips-for-salesforce-version-control-integration/) repository.

![Local Version Control Repository](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/aaa4.png)

### B. Stage Changes

#### Stage all changes

![Stage all changes](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/aaaa.png)

#### Stage changes for a file

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/aaa2.png" alt=""><figcaption></figcaption></figure>

#### Stage selective line of code

#### &#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/aaa3.png" alt=""><figcaption></figcaption></figure>

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

![prevalidation request](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-382.png)

### D. Commit approved pre-validation request

This will allow you to commit the code once the pre-validation request is approved.

![commit approved pre validation request](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-808.png)

### E. View Pre-validation Requests

#### Diff Report

![view pre validation request](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-671.png)

#### Static Code Analysis Report

![static code analysis report](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-210.png)

#### Validate Deployment Report

![validate deployment report](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-719.png)

### F. Trigger Build

This extension will also allow developers to run builds once the code is committed. Different quick actions such as Quick Deploy, or Abort are associated to each build.

![Trigger Build](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-202.png)

### G. Deployments

This extension will allow viewing results for pre-validations, builds, and deployments.&#x20;

![Deployments](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-734.png)
