# Automate Merge When CI Builds Pass

### Overview

The **Run Merge process on successful deployment** feature keeps track of builds in source branches and merges them into a designated destination branch if they meet the configured criteria (for example, the build is successful). Rather than requiring manual effort, upstream merges can now be automated by the Salesforce Release Manager using revision numbers that were determined as part of a build cycle in CI jobs.

> The feature is supported for the following CI jobs:
>
> * Package and deploy SFDX source from version control
> * Deploy from version control

### Automate Merge Process Settings

#### Enabling auto-merge

You will find the **`On Successful Deployment > Run Merge Process`** checkbox under the **`Deploy`** section when you create a CI Job in ARM and fill out all required details in the **`Build`** section (such as _version control repository, branch, and revisions_).

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Configuring auto-merge**

The following fields must be configured to start a merge when the build succeeds:

<table><thead><tr><th width="238">Option</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Types of version control, example: Git, TFS.</td></tr><tr><td>Repository</td><td>Based on the version control type selection, select your repository.</td></tr><tr><td>From Branch</td><td>Specify the branch whose builds' sources will be merged.</td></tr><tr><td>To Branch</td><td>The destination branch the sources will be merged to.</td></tr><tr><td>Merge Conflict Strategy</td><td>Specify the way to resolve the merge conflict if occurs.</td></tr><tr><td>Resolve Type</td><td>Choose merge method, i.e., <strong>dry run</strong> (shows how the merge will execute without making any changes) or <strong>merge</strong> (commits the changes).</td></tr><tr><td>Merge Type</td><td>Type of merges supported in ARM, i.e., <em>entire branch, single revision, commit label, release label, ALM label</em>.</td></tr><tr><td>Create GIT Tag</td><td>Create a GIT tag. GIT tags are a simple and effective way to ensure you can keep track of the different versions of your code and the critical quality of Git's version control. GIT Tag operation allows meaningful names to a specific version in the repository.</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Users will be notified via email of the success or failure of the automated merge process.

**Merge-built revisions only**

A new checkbox called **`Merge built revisions only`** is added under the **`Deploy > On Successful Deployment > Run Merge Process`** section. On selection of the checkbox, ARM cherry-picks revisions identified as part of a build cycle to append them to the destination branch per the user's choice.

<table><thead><tr><th width="229">Option</th><th>Description</th></tr></thead><tbody><tr><td>To Branch</td><td>The destination branch the sources will be merged to.</td></tr><tr><td>Merge Conflict Strategy</td><td>Specify the way to resolve the merge conflict if it occurs.</td></tr><tr><td>Resolve Type</td><td>Choose merge method, i.e., <strong>dry run</strong> (shows how the merge will execute without making any changes) or <strong>merge</strong> (commits the changes).</td></tr><tr><td>Create GIT Tag</td><td>Create a GIT tag.</td></tr></tbody></table>

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note:**

1. Selecting the **Merge built revisions only** checkbox will disable the current merge process.
2. Users will be notified via email of the success or failure of the merge process.
{% endhint %}
