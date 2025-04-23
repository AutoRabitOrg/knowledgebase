# GIT Integration

### What is GIT? <a href="#what-is-git" id="what-is-git"></a>

**Git** is an extremely popular version control system that is at the heart of a wide variety of high-profile projects. Git is installed and maintained on your local system (rather than in the cloud), giving you a self-contained record of your ongoing programming versions.

"_Simply put, Git is a version control system that lets you manage and keep track of your source code history_."

### What Is GitHub? <a href="#what-is-github" id="what-is-github"></a>

GitHub is designed as a Git repository hosting service. It lets you track and share your Git version control projects outside your local computer/server. Unlike Git, GitHub is exclusively cloud-based.

### Prerequisites for registering GIT with ARM <a href="#prerequisites-for-registering-git-with-arm" id="prerequisites-for-registering-git-with-arm"></a>

Before registering Git with ARM, you must check off some of the boxes on the prerequisites list.

1.  Ensure you enable the **`GIT`** plugin under **`Plugins`** in the **`My Account`** section to use GIT for version control.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667468658459.png" alt="" width="563"><figcaption></figcaption></figure>
2. You must have a GitHub account. If you don’t already have a GitHub account, you can create one at [github.com](https://github.com/). Once you have a GitHub account, you can create a new repository or use an existing one.
3. You must have permission to register a repository.
4. Store your GIT credentials in ARM.

### Store your GIT credential in ARM <a href="#store-your-git-credential-in-arm" id="store-your-git-credential-in-arm"></a>

This is an initial step in storing your user's credentials (usually a username, password, or token) in ARM. GitHub no longer supports basic authentication using a username and password. You must now authenticate to GitHub with an **API token**, such as an **OAuth** access token, GitHub App installation access token, or personal access token. For more information, see the [blog](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api/) post.

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on the **`Credentials`** tab.
3.  Next, click on **`Create Credential`** from the right navigation bar.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667468735012.png" alt="" width="563"><figcaption></figcaption></figure>
4. On the next pop-up screen, give a **`Credential name`**.
5. Choose the **`Credential Type`** as **`Username With Password.`**
6.  Enter your GitHub **`Username`** and **API Token** (in the **`Password`** field), and we will store this encrypted. GitHub no longer supports basic authentication using passwords. You must now authenticate to GitHub with an API token instead. For more information on how to create an API token, see the **Troubleshooting** section on this page.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667468804666.png" alt="" width="375"><figcaption></figcaption></figure>
7. Click **`Save`**.

### Registering a GIT repository in ARM <a href="#registering-a-git-repository-in-arm" id="registering-a-git-repository-in-arm"></a>

To set up a GIT repository, ensure an account is created and configured at [GIT](https://github.com/). Next, follow the below steps:

1. Log in to your ARM account.
2.  Hover your mouse over the **`Admin`** module and click on **`VC Repo's`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667469343490.png" alt="" width="375"><figcaption></figcaption></figure>
3.  Click on **`Register Repository`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667469387799.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Select the **`Version Control System`** as **`GIT`** on the **`Register Repository`** page.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667469498995.png" alt="" width="375"><figcaption></figcaption></figure>
5. Select the **AWS CodeCommit Repository** checkbox. ARM fetches data from the repository if the GIT gets hosted on **AWS (Amazon Web Services)**.
6. Enter the name of the repository to display it locally.
7. Paste the **`Repository URL`** that Git provides you.
8. Choose the correct user's **`Credentials`** from the list. To create new credentials, click on the **`+`**&#x69;con.Note:Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
9. The **`Default Branch`** selection will be in disabled mode by default. Click the icon to fetch and list all the available branches on your remote repository.
10. Select one of the default branches from the list.Note:Ensure the default branch is available in your remote repository with some files committed to it. If no file is available, create a README.txt file and add it to the repository.
11. Once the registration is done, you can find the newly added repository on **`VC Repo's`** home page.

Points to Remember:

1. Select the **`Enable SFDX`** checkbox to register your GIT repository in the SFDX structure.
2. Select the **`Enable nCino`** checkbox to register the GIT repository with nCino objects included. To quickly identify nCino registered Version Control Repositories among all other repositories, nCino logos are marked in front of the Repository Label.
3. The user can enable their Version Control Repository with **SFDX** or **nCino** enabled. Both cannot be enabled at the same time.

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

While registering GIT with ARM, GIT fails to connect, resulting in _Authenticate Failure_**.** This is because GitHub no longer supports basic username and password authentication. You must now authenticate to GitHub with an API token, such as an OAuth access token, GitHub App installation access token, or personal access token, depending on what you need to do with the token. For more information, see the [blog](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api/) post.

#### Creating a Personal Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

This section guides you through creating your personal access token directly on GitHub.

1. Log in to your GitHub account.
2.  In the upper-right corner of any page, click your profile photo, then click **`Settings`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573644442.png" alt="" width="188"><figcaption></figcaption></figure>
3.  In the left sidebar, click **`Developer settings`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573747686.png" alt="" width="188"><figcaption></figcaption></figure>
4.  In the left sidebar, click **`Personal access tokens`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573815455.png" alt="" width="188"><figcaption></figcaption></figure>
5.  Click **`Generate new token`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573866680.png" alt=""><figcaption></figcaption></figure>
6.  Give your token a descriptive name.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573923768.png" alt=""><figcaption></figcaption></figure>
7.  Select the scopes or permissions you want to grant this token. Select **`repo`** to use your token to access repositories from the command line.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677573994564.png" alt="" width="563"><figcaption></figcaption></figure>
8.  Click **`Generate token`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677574050356.png" alt="" width="563"><figcaption></figcaption></figure>
9.  Click ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606156266000.png) to copy the token to your clipboard. You cannot see the token again after navigating off the page for security reasons.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677577004671.png" alt=""><figcaption></figcaption></figure>
10. Use the copied token as a password for creating/updating the credential in ARM.
11. Once updated, please use the same credential to authenticate the GIT.Important Note:Treat your tokens like passwords and keep them secret. When working with the API, use tokens as environment variables instead of hardcoding them into your programs.
