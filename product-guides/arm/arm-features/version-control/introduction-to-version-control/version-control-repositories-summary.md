# Version Control Repositories Summary

{% hint style="info" %}
**Important Note**: This article is for the **Org Administrator** in particular. The actions discussed in the article will not be available to general users.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The lists of repositories you have added yourself and any other repositories your team members have shared can be seen on the **`VC Repo's`**` ``(`**`Version Control Repository)`** page.

Repositories with **Salesforce DX** enabled will have ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613573720637.png) icon displayed, and nCino objects configured will have ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613574637463.png) icon beside their repository under **`Repositories List`** for easier identification.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676053017632.png" alt="" width="188"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676053213037.png" alt="" width="375"><figcaption></figcaption></figure>

For each version control repository registered in ARM, the following information or fields are displayed:

Create a pull request to propose and collaborate on changes to a repository. This is discussed later.&#x20;

| Field Name             | Description                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Repository Name`      | Name of your  version control repository                                                                                                          |
| `Type`                 | Version control repository type, i.e., GIT, TFS, or SVN.                                                                                          |
| `URL`                  | Repository URL                                                                                                                                    |
| `Created Date`         | Date and time stamp for repository created or modified                                                                                            |
| `Credentials`          | User's credential linked with the version control repository                                                                                      |
| `Test Connection`      | This will allow you to check whether the connection has been authenticated. A success message is displayed after the authentication is completed. |
| `Enable nCino app`     | On selection, the nCino objects will get registered with the current repository.                                                                  |
| `Pull Request Support` | Create a pull request to propose and collaborate on changes to a repository. This is discussed later.                                             |

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676053578831.png)

#### Pull Request Support <a href="#pull-request-support" id="pull-request-support"></a>

Create a pull request to propose and collaborate on changes to a repository. These changes are proposed in a branch, which ensures that the master branch only contains finished and approved work. You can specify which branch you'd like to merge your changes into when you create your pull request.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676053727602.png" alt="" width="563"><figcaption></figcaption></figure>

Pull requests can only be opened between two branches that are different. More detailed instructions are available in a separate article; please refer [HERE](../external-pull-request/).

#### Branches/Tags <a href="#branchestags" id="branchestags"></a>

The Git tags created or branches registered for the version control repository will get displayed under the **`Branches/Tags`** section. For more information about Git Tags, check out the link [HERE](../../../arm-administration/registration/version-control-repository/git-integration/git-tag.md).

**Additional details under Branch**

**A. Create a Branch**

Create a new branch for the current repository. Newly created branches will get listed under the **`Branches`** tab. ([LEARN MORE](version-control-branch-workflow.md))

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682075996942.png)

**B. Register a Branch**

Register an existing branch to the current repository. ([LEARN MORE](../))

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676054134635.png" alt=""><figcaption></figcaption></figure>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676054216313.png)

**C. Unregister a Branch**

Select a branch or branches to unregister them from your version control system. Upon confirmation, the branch(es) gets permanently deleted from your version control system. The entire data will get erased.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676054346674.png" alt="" width="563"><figcaption></figcaption></figure>

**D. Sync Branches**

The **`Sync Branches`** option will allow you to view the branches that are no longer available in your version control repositories but present in ARM; therefore, you can delete them from the ARM application.

**E. Branch Details:**

For each branch, view the following details:\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682076122660.png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Branch Name:`** Name of the branch assigned.
2.  **`Branch Settings:`**This option allows you to update your branch configuration, which means:

    * you can add your branch to one of the standard branch types _(development, integration, quality assurance, production, etc.)_
    * configure your parent branch
    * update the metadata folder path and/or,
    * update the branch's last commit date.



    **Pieces of information related to 'Metadata Folder Path'**

    * The default metadata folder path is in the following format: _force-app/main/default_
    * When the user changes the **`Metadata Folder Path`**, ARM updates the **project-def.json** file at the time of the initial commit. The commits will now occur in the newly created _.src_ folder once the src metadata folder location has been updated. In the instance where the user has many commits on the newly created src folder and then reverts the src folder to default, all of the components in the src folder will now be included in the **package.xml** as well.
    * For ARM to detect your repository as being in DX format, it looks for an **sfdx-project.json** file in your local directory. The **sfdx-project.json** file is the configuration file. For the SFDX repository created outside and registered later with ARM, the source folder has to be declared in the **sfdx-project.json** file under the array named _packageDirectories_. This will allow you to pick the source folder you declared in the **sfdx-project.json** during the commit/ CI Job operation or while creating unlocked packages.&#x20;
    * The folder name must be entered in the **`Metadata Folder Path`** field for SFDX repositories where _foldername/force-app/main/default/_ counts as the metadata folder path.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676057120903.png" alt="" width="563"><figcaption></figcaption></figure>
3.  **`Smart Commits-Sync:`** Use this toggle button to start/stop syncing external [Smart Commits](../../../arm-administration/alm-management.md). If you try to sync external commits to a branch that has not been mapped, you will see a notification popup. You must map the required branch under **`Admin > ALM Mgmt > Repository Mappings`**, then you can proceed to sync the external smart commits. For more information on mapping a branch, refer [HERE](../../../arm-administration/alm-management.md).\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682076638548.png" alt="" width="375"><figcaption></figcaption></figure>
4. **`Status:`** View the branch status along with the branch log report.
5. **`Info:`** Hover your mouse over the icon to view the branch details, such as the branch created date, parent branch, and author details.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676054988068.png" alt="" width="375"><figcaption></figcaption></figure>

1. **`Clear AutorabitExtId:`** Deletes the **`AutorabitExtId__c`** field from your branch.
2. **`Migrate:`** Migrates custom object field **`Picklist`** to **`Value Set`** in your branch.
