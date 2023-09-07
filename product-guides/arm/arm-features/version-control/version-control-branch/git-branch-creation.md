# GIT Branch Creation

### Overview <a href="#overview" id="overview"></a>

Developers can create a branch to work on a new version of an existing application. Changes in the primary or other branches will only affect your branch if you pull the latest changes from those branches.&#x20;

&#x20;Creating a new branch for each task is a common practice because it allows others to identify what changes to expect and, for backtracking purposes, to understand why a particular code change is implemented.

### Creation of a GIT Branch <a href="#creation-of-a-git-branch" id="creation-of-a-git-branch"></a>

1. Log in to your ARM account.
2.  From the ARM home page, click on the **`Admin`** module and go to the **`VC Repo's`** tab.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677732985245.png" alt="" width="375"><figcaption></figcaption></figure>
3. Select a **GIT** repository for which the branch needs to be created.Note:If your GIT repository is **nCino** enabled, the nCino logo will be marked in front of your repository.&#x20;
4.  Under **`Branches`**, click on **`Create`** button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677733082796.png" alt="" width="563"><figcaption></figcaption></figure>
5.  In **`Create Branch`** screen, give a **`Branch name`** and select **`Parent Branch`** and **`Branch Type`** from the list. If the **`Parent Branch`** configures a metadata folder path, the same configuration will map to the newly created branch.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677733183225.png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note**: The characters **"//" \ , \* ? & ' " < > | \` \~ ( )** and **space** are not allowed in the **`Branch Name`** field.
{% endhint %}

6. Click **`Create`** to complete the creation process.

### Registration of an existing GIT branch <a href="#registration-of-an-existing-git-branch" id="registration-of-an-existing-git-branch"></a>

1. On the **`VC Repo's`** page, select a GIT repository from the repositories list.
2.  Click **`Register`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677738927958.png" alt=""><figcaption></figcaption></figure>
3. Checkbox the branches you need to register and enter the following details:
   * **`Parent Branch:`** Choose its parent branch from the drop-down.
   * **`Last commit date`**: The last commit date is fetched from Salesforce Org in EZ-Commit based on the specified date.
4.  Once done, click **`Register`** to complete the branch registration.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677739299894.png" alt="" width="563"><figcaption></figcaption></figure>

### Registration of nCino configured GIT branch <a href="#registration-of-ncino-configured-git-branch" id="registration-of-ncino-configured-git-branch"></a>

1. On the **`Version Control Repositories`** page, select a GIT repository marked with the **`nCino`** logo.
2.  Click **`Register`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677739864841.png" alt=""><figcaption></figcaption></figure>
3. Checkbox the branches you need to register and select its **`Parent Branch`** and last commit date _(the last commit date is used to fetch changes from Salesforce Org in EZ-Commit based on the specified date)._
4.  Click the **`Register`** button to complete the branch registration.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677739962070.png" alt="" width="563"><figcaption></figcaption></figure>
