# Automate Merge When CI Builds Pass

### Overview

The **Run Merge process on successful deployment** feature keeps track of builds in source branches and merges them into a designated destination branch if they meet the configured criteria (for example, the build is successful). Rather than requiring manual effort, upstream merges can now be automated by the Salesforce Release Manager using revision numbers that were determined as part of a build cycle in CI jobs.

> The feature is supported for the following CI jobs:
>
> * Package and deploy SFDX source from version control
> * Deploy from version control

### Automate Merge Process Settings

#### Enabling auto-merge

You will find the **`On Successful Deployment > Run Merge Process`** checkbox under the **`Deploy`** section when you create a CI job in ARM and fill out all required details in the **`Build`** section (such as _version control repository, branch, and revisions_).\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-HDWJHIYE.png" alt=""><figcaption></figcaption></figure>

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZPLBS2F8.png)

**Configuring auto-merge**

The following fields must be configured to start a merge when the build succeeds:

| Option                  | Description                                                                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Repository Type         | Types of version control, example: Git, TFS.                                                                                                                                                                                                                        |
| Repository              | Based on the version control type selection, select your repository.                                                                                                                                                                                                |
| From Branch             | Specify the branch whose builds' sources will be merged.                                                                                                                                                                                                            |
| To Branch               | The destination branch the sources will be merged to.                                                                                                                                                                                                               |
| Merge Conflict Strategy | Specify the way to resolve the merge conflict if occurs.                                                                                                                                                                                                            |
| Resolve Type            | Choose merge method, i.e., **dry run** (shows how the merge will execute without making any changes) or **merge** (commits the changes).                                                                                                                            |
| Merge Type              | Type of merges supported in ARM, i.e., _entire branch, single revision, commit label, release label, alm label_.                                                                                                                                                    |
| Create GIT Tag          | Create a GIT tag. GIT tags are a simple and effective way to ensure you can keep track of the different versions of your code and the critical quality of Git's version control. GIT Tag operation allows meaningful names to a specific version in the repository. |

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Q6I3832K.png)

Users will be notified via email of the success or failure of the automated merge process.

**Merge-built revisions only**

A new checkbox called **`Merge built revisions only`** is newly added under the **`Deploy > On Successful Deployment > Run Merge Process`** section. On selection of the above-mentioned checkbox, ARM cherry-picks revisions identified as part of a build cycle to append them to the destination branch per the user's choice.

| Option                  | Description                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| To Branch               | The destination branch the sources will be merged to.                                                                                    |
| Merge Conflict Strategy | Specify the way to resolve the merge conflict if it occurs.                                                                              |
| Resolve Type            | Choose merge method, i.e., **dry run** (shows how the merge will execute without making any changes) or **merge** (commits the changes). |
| Create GIT Tag          | Create a GIT tag.                                                                                                                        |

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-6DAHNPB6.png)

Point to Note:

1. Selecting the **Merge built revisions only** checkbox will disable the current merge process.
2. Users will be notified via email of the success or failure of the merge process.
