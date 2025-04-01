# Bitbucket

### About Bitbucket <a href="#about-bitbucket" id="about-bitbucket"></a>

**Bitbucket** from Atlassian is a cloud/self-hosted version control application. It provides effective ways to manage repositories, issue tracking, and technical projects. In the most basic terms, Bitbucket empowers you with total authority over the DevOps lifecycle.

### GitHub and Bitbucket <a href="#github-and-bitbucket" id="github-and-bitbucket"></a>

GitHub and Bitbucket are hosting platforms that offer developers access to both public and private repositories. The functionality of Bitbucket and GitHub is very similar, and both allow you to perform basic operations, such as:

* Create and manage repositories
* Utilize **Two-Factor Authentication (2FA)**
* Make pull requests
* Perform code reviews
* Enhance team collaboration and efficiency of the process
* Make use of inline editing and Markdown support
* Keep track of issues, etc.

### Configure Your Bitbucket Repository <a href="#configuring-your-bitbucket-repository" id="configuring-your-bitbucket-repository"></a>

#### Prerequisites for registering Bitbucket with ARM <a href="#prerequisites-for-registering-bitbucket-with-arm" id="prerequisites-for-registering-bitbucket-with-arm"></a>

* You must have a Bitbucket account. If you don’t already have a Bitbucket account, you can create one at [https://start.atlassian.com/](https://start.atlassian.com/). Once you have a Bitbucket account, you can create a new repository or use an existing one.
* You must have permission to register a repository.
* Store your Bitbucket credentials in ARM.

### Store your Bitbucket credential in ARM <a href="#store-your-bitbucket-credential-in-arm" id="store-your-bitbucket-credential-in-arm"></a>

This is an initial step where you store your user's credential (usually a username, password, or token) in ARM.

To authenticate Bitbucket, you’ll have to use the **App Password** instead of the regular password to log in to your Bitbucket account.

### **Generate a Bitbucket App Password**

1. Log in to your Bitbucket account.
2. Click your account’s **`profile picture`** in the top right-corner of the Bitbucket web page.
3. Click the **`Personal Settings`** link in the dropdown menu.
4. Select the link on the left labeled **`App Passwords`**. It is under the **`Access Management`** heading.
5. Click on the **`Create App Password`** button.
6. Enter a **`label name`** and check all the necessary permissions you want to provide. Typically, required are **`repository`**, **`webhook`**, and **`pull request permissions`**.
7. Click **`Create`** to generate the Bitbucket App Passwords and copy the access token’s value. You will not be able to view this password again once you close this window.
8. Click **`Save`**.

### **Store your Bitbucket credential in ARM**

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on the **`Credentials`** tab.
3. Next, click **`Create Credential`**.
4. On the next pop-up screen, give a **`credential name`**.
5. Choose the **`Credential Type`** as **`Username With Password`**.
6. Enter your Bitbucket’s **`username`** and **`App Password`**.
7. Click **`Save`**.

### Register a Bitbucket repository in ARM <a href="#registering-a-bitbucket-repository-in-arm" id="registering-a-bitbucket-repository-in-arm"></a>

If you wish to set up a Bitbucket repository, ensure that you have an account created and configured at Bitbucket. Next, follow the below steps:

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on **`VC Repos`**.
3. Click on the **`Register Repository`** available on the right corner of the screen.
4. On the **`Register Repository`** page, select the **`Version Control System`** as **`GIT`**.
5. Enter the **`name`** of the repository to display it locally.
6. Paste the **`Clone URL`** that Bitbucket provides you.

> Follow the steps to copy the URL from the Bitbucket account:\
> a. Select your registered Bitbucket repository.\
> b. Click on **`Clone`** and select **`HTTPS`**.\
> c. **`Copy the URL`** to paste in the ARM.\
> **Note:** _Make sure to remove “git clone” before pasting the URL._

7. Choose the correct user's **`Credentials`** from the list that you saved earlier.
8. The **`Default Branch`** selection will be in disabled mode by default. Click on the **`refresh`** button to fetch and list down all the available branches on your remote repository.
9. Select one of the default branches from the list.
10. Once the registration is successfully done, you can find the newly added repository on the **`VC Repo's`** home page.

{% hint style="info" %}
NOTE: Users may encounter an Error: **Cannot Open Git-Upload-Pack** when trying to register the Bitbucket repository. This occurs when:

* The Bitbucket account is locked.
* When registering the Bitbucket repository, the wrong credentials were used.
* The IT/Network team has whitelisted ARM's IP address.

To resolve this issue:

* Try recreating a new credential and updating the credentials under the **Admin > Credential** section.
* Re-register your bitbucket repository in ARM.
{% endhint %}
