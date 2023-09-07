# Add a Project to CodeScan from Git

This document guides how to add a git project to your CodeScan cloud account and run the analysis.\
This method can be used to add a project from any git-based SCM; however, if you use a cloud version of GitHub, Bitbucket, or GitLab, we suggest you use the specific integration for your repository.

1. Login to your **CodeScan** account.
2. Once you log into your CodeScan account, click on the (**+**) icon in the top right corner and select **Analyze new project**.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634904515112.png)
3. &#x20;It takes you to a different window. Choose the **Organization** for which you'd like to create a project.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634904623955.png)
4. In the next screen, click on **Add Analysis Project** option.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634904639645.png)
5. You will now see a new popup window; select **Git** from the given options.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045899468.png)
6. Enter the necessary information in the fields as mentioned below:![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685083354675.png)
   1. Fill in the **GIT repository URL**. You can add two types of URL addresses in the field:
      * An **HTTPS URL** like **`https://github.com/user/repo.git`**
      * An **SSH URL**, like **`git@github.com:user/repo.git`** or  **`ssh://github.com/user/repo`**
   2. Enter the Git **username** and the **security token** in their respective fields, followed by the **project branch** name.
   3. Enter the CodeScan **project security key,** followed by the **project name**.\
      Note:To know where to find the project key, refer to our document on how to do it by clicking [here](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
   4. Under **Scheduling**, choose whether to run the project automatically by selecting **Daily** or manually by selecting **Manual**.
   5. If you select **Daily**, another field named **Schedule** has to be selected by choosing the time you want the automatic analysis to be triggered.

This triggers the project analysis and the added project under your [CodeScan](https://www.codescan.io/) organization.

This project will now run daily at the scheduled time unless configured otherwise.
