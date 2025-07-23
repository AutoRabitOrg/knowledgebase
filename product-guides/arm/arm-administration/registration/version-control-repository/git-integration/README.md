# GIT Integration

### What is Git? <a href="#what-is-git" id="what-is-git"></a>

**Git** is the world's most popular version control system. Version control allows you to maintain a history of changes to text files (such as a codebase) over time, tracking what changes were made, by whom, at what time, and for what purpose. Projects in Git are organized into repositories: a collection of files and changes to those files over time. Git is a distributed version control system, meaning that the main repository can be cloned (for example to a developer's laptop) and changes from multiple developers can be merged and pushed to a shared central repository.

### What Is a Git Host? <a href="#what-is-a-git-host" id="what-is-a-git-host"></a>

A Git host is a service provider who hosts Git repositories. Git hosts may be on the cloud or in corporate on-premises infrastructure. A Git host provides a central place for teams to synchronize their changes, provides a central backup of the Git repository, and provides other services such as APIs, a user interface, and the ability to create merge requests (aka pull requests). There are many Git hosts. The most popular ones are:

* GitHub
* BitBucket
* GitLab
* Azure Repos
* AWS CodeCommit (not accepting new customers)

### Prerequisites for Registering a Git Repository with ARM <a href="#prerequisites-for-registering-git-with-arm" id="prerequisites-for-registering-git-with-arm"></a>

Before registering Git with ARM, there are some prerequisites.

1. Ensure you enable the **`Git`** plugin under **`Plugins`** in the **`My Account`** section to use Git for version control.

<figure><img src="../../../../../../.gitbook/assets/image (647).png" alt=""><figcaption></figcaption></figure>

2. You must have permission in ARM to register a repository.
3. You must have credentials for the repository you want to access.
4. You must store these Git credentials in ARM.

### Store Your Git Credentials in ARM <a href="#store-your-git-credential-in-arm" id="store-your-git-credential-in-arm"></a>

This is an initial step in storing your user's credentials (usually a username, password, or token) in ARM. Some Git hosts like GitHub no longer support basic authentication using a username and password. You must now authenticate using an **API token**, such as a personal access token.

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on the **`Credentials`** tab.
3. Next, click on **`Create Credential`** from the right navigation bar.

<figure><img src="../../../../../../.gitbook/assets/image (648).png" alt=""><figcaption></figcaption></figure>

4. On the next pop-up screen, give a **`Credential name`**.
5. Choose the **`Credential Type`** as **`Username With Password.`**
6. Enter your **`Username`** for the Git host and **API Token** (in the **`Password`** field), and we will store this encrypted. For more information on how to create an API token, see the **Troubleshooting** section on this page.

<figure><img src="../../../../../../.gitbook/assets/image (649).png" alt="" width="416"><figcaption></figcaption></figure>

{% hint style="info" %}
**NOTE**: If you are using SSO to log in to your Git Repository, you must Authorize the **Generate API** token. Click on the '**Configure SSO**' dropdown to authorize the generated token.
{% endhint %}

<figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Authorize the personal access token to allow external systems like AutoRABIT to connect to SAML-connected software, e.g., GitHub.&#x20;
8.  Following creation of the personal access token, configure and authorize SSO. \


    <figure><img src="../../../../../../.gitbook/assets/image (1736).png" alt=""><figcaption></figcaption></figure>
9. Click **`Save`**.

### Registering a Git Repository in ARM <a href="#registering-a-git-repository-in-arm" id="registering-a-git-repository-in-arm"></a>

To set up a Git repository, follow the steps below:

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on **`VC Repo's`**.

<figure><img src="../../../../../../.gitbook/assets/image (650).png" alt="" width="285"><figcaption></figcaption></figure>

3. Click on **`Register Repository`**.

<figure><img src="../../../../../../.gitbook/assets/image (651).png" alt="" width="563"><figcaption></figcaption></figure>

4. Select the **`Version Control System`** as **`Git`** on the **`Register Repository`** page.

<figure><img src="../../../../../../.gitbook/assets/image (652).png" alt="" width="412"><figcaption></figcaption></figure>

5. Enter the name of the repository to display it locally.
6. Paste the **`Repository URL`** from your Git host.
7. Choose the correct user's **`Credentials`** from the list. To create new credentials, click on the \*\*`+`\*\*icon.

{% hint style="info" %}
**Note:** Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
{% endhint %}

9. The **`Default Branch`** selection will be in disabled mode by default. Click the icon to fetch and list all the available branches on your remote repository.
10. Select one of the default branches from the list. Note:Ensure the default branch is available in your remote repository with some files committed to it. If no file is available, create a README.txt file and add it to the repository.
11. Once the registration is done, you can find the newly added repository on **`VC Repo's`** home page.
12. The Sync Branches radio button allows you to view branches that are no longer available in your version control repositories but are still visible in the ARM application, and you can delete them from the ARM application as well.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-64UAR2YT.png)



{% hint style="info" %}
**Points to Remember:**

1. Select the **`Enable SFDX`** checkbox to register your Git repository in the SFDX structure.
2. Select the **`Enable nCino`** checkbox to register the Git repository with nCino objects included. To quickly identify nCino registered Version Control Repositories among all other repositories, nCino logos are marked in front of the Repository Label.
3. The user can enable their Version Control Repository with **SFDX** or **nCino** enabled. Both cannot be enabled at the same time.
{% endhint %}

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

While registering Git with ARM, Git fails to connect, resulting in _Authenticate Failure_**.** This is because your credentials are invalid. Check the URL, username, and API token (or other authentication mechanism).
