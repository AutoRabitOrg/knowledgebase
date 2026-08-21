# Create Pull Request on Merged Changes in ez-Merge

### Overview

The **Create Pull Request On Merged Changes** option allows users to create a Pull Request for merged changes instead of committing them directly to the destination branch.

ARM creates a temporary branch, applies and validates the selected changes, and then creates a Pull Request against the destination branch for external code review.

### Prerequisites

* Available in the **New UI**.
* **Pre-validation Merge** must be configured.
* Repository must support Pull Requests.
* Valid destination branch credentials must be configured under **My Profile**.

### Using Create Pull Request On Merged Changes

Navigate to **Version Control → ez-Merge** and select the required source and destination branches.

<figure><img src="../../../../../.gitbook/assets/image (2776).png" alt=""><figcaption></figcaption></figure>

Select the required Merge Type Such as Single Revision, Entire Branch,Commit Label, Release Label, ALM Label.

<figure><img src="../../../../../.gitbook/assets/image (2777).png" alt=""><figcaption></figcaption></figure>

Configure **Pre-validation Merge** and the required validation options, such as:

* File Diff
* Static Code Analysis
* Validate Deploy

<figure><img src="../../../../../.gitbook/assets/image (2778).png" alt=""><figcaption></figcaption></figure>

Enable **Create Pull Request On Merged Changes**.

When enabled, ARM creates a Pull Request instead of directly committing the merged changes to the destination branch.

<figure><img src="../../../../../.gitbook/assets/image (2779).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2780).png" alt=""><figcaption></figcaption></figure>

The following options are not applicable to this flow:

* Create commit label
* Create GIT tag
* Delete source branch
* Approvers / reviewers selection

Review the configuration and click **Create Pull Request**.

ARM will:

1. Create a temporary branch from the destination branch.
2. Apply the selected revisions to the temporary branch.
3. Run the configured merge validations.
4. Create a Pull Request from the temporary branch to the selected destination branch.

<figure><img src="../../../../../.gitbook/assets/image (2781).png" alt=""><figcaption></figcaption></figure>

### Process Logs

A new **Pull Request Creation** process log provides:

* Temporary branch creation details
* Pull Request creation details
* Pull Request URL

<figure><img src="../../../../../.gitbook/assets/image (2782).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2783).png" alt=""><figcaption></figcaption></figure>

The **Commit** and **Post Merge Updates** process logs are not available for this flow because ARM does not directly commit changes to the destination branch.

### Review and Merge

Once the Pull Request is created, use the URL available in the process log to open it in the external repository.

The Pull Request can then go through the repository's standard review process, including external or AI-based code review.

<figure><img src="../../../../../.gitbook/assets/image (2784).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2785).png" alt=""><figcaption></figcaption></figure>

The final merge can be completed through:

* **External Pull Requests History** in ARM, or
* The external Git repository.

### Expected Result

The selected revisions are applied to a temporary branch, validated, and a Pull Request is created against the destination branch. The destination branch remains unchanged until the Pull Request is reviewed and merged.
