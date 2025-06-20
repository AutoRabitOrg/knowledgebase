# Add a Project to CodeScan from Git

This document guides how to add a git project to your CodeScan cloud account and run the analysis.\
This method can be used to add a project from any git-based SCM; however, if you use a cloud version of GitHub, Bitbucket, or GitLab, we suggest you use the specific integration for your repository.

1. Login to your **CodeScan** account.
2. Once you log into your CodeScan account, click on the (**+**) icon in the top right corner and select **Analyze new project**.

<figure><img src="../../../../../../.gitbook/assets/AnalyzeProzect 5.9 (3).png" alt=""><figcaption></figcaption></figure>

3. It takes you to a different window. Choose the **Organization** for which you'd like to create a project.

<figure><img src="../../../../../../.gitbook/assets/ProjectSetup 7.7 (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. In the next screen, click on **Add Analysis Project** option.

<figure><img src="../../../../../../.gitbook/assets/AnalyzeProzect 5.9 (5).png" alt=""><figcaption></figcaption></figure>

5. You will now see a new popup window; select **Git** from the given options.

<figure><img src="../../../../../../.gitbook/assets/Git 7.5.png" alt=""><figcaption></figcaption></figure>

6. Enter the necessary information in the fields as mentioned below:

<figure><img src="../../../../../../.gitbook/assets/Git 7.6.png" alt="" width="375"><figcaption></figcaption></figure>

* Fill in the **GIT repository URL**. You can add two types of URL addresses in the field:
  1. An **HTTPS URL** like **`https://github.com/user/repo.git`**
  2. An **SSH URL**, like **`git@github.com:user/repo.git`** or  **`ssh://github.com/user/repo`**
* Enter the Git **username** and the **security token** in their respective fields, followed by the **project branch** name.
* Enter the CodeScan **project security key,** followed by the **project name**.
* Under **Scheduling**, choose whether to run the project automatically by selecting **Daily** or manually by selecting **Manual**.
* If you select **Daily**, another field named **Schedule** has to be selected by choosing the time you want the automatic analysis to be triggered.

{% hint style="info" %}
**Note:** To know where to find the project key, refer to our document on how to do it by clicking [here](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
{% endhint %}

This triggers the project analysis and the added project under your [CodeScan](https://www.codescan.io/) organization.

This project will now run daily at the scheduled time unless configured otherwise.
