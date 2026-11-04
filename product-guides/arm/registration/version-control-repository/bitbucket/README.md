# Bitbucket

{% hint style="warning" %}
As of 9 September 2025, app username and passwords have been deprecated as a type of authentication method. However, as of 9 June 2026, all existing app passwords will be disabled. Users are required to create API tokens and migrate this function prior to the deadline to avoid disruptions: [https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/). Follow the steps below for creating an API token instead of a password.
{% endhint %}

### About Bitbucket <a href="#about-bitbucket" id="about-bitbucket"></a>

**Bitbucket** from Atlassian is a cloud/self-hosted version control application. It provides effective ways to manage repositories, issue tracking, and technical projects. In the most basic terms, Bitbucket empowers you with total authority over the DevOps lifecycle.

### GitHub and Bitbucket <a href="#github-and-bitbucket" id="github-and-bitbucket"></a>

GitHub and Bitbucket are hosting platforms that offer developers access to both public and private repositories. The functionality of Bitbucket and GitHub is very similar, and both allow you to perform basic operations, such as:

* Create and manage repositories
* Utilizing **Two-Factor Authentication (2FA)**
* Make pull requests
* Perform code reviews
* Enhances team collaboration and efficiency of the process.
* Make use of inline editing and Markdown support
* Keep track of issues, etc.

### Configuring Your Bitbucket Repository <a href="#configuring-your-bitbucket-repository" id="configuring-your-bitbucket-repository"></a>

#### Prerequisites for registering Bitbucket with ARM <a href="#prerequisites-for-registering-bitbucket-with-arm" id="prerequisites-for-registering-bitbucket-with-arm"></a>

* You must have a Bitbucket account. If you don’t already have a Bitbucket account, you can create one at [https://start.atlassian.com/](https://start.atlassian.com/) Once you have a Bitbucket account, you can create a new repository or use an existing one.
* You must have permission to register a repository.
* Store your Bitbucket’s credentials in ARM.

### Creating Your Bitbucket Credential in ARM <a href="#store-your-bitbucket-credential-in-arm" id="store-your-bitbucket-credential-in-arm"></a>

This is an initial step where you store your user's credential (usually a username, password, or token) in ARM.

To authenticate Bitbucket, you’ll have to use **API Token** instead of the regular password to login to your Bitbucket account.

For ARM and Bitbucket connectivity to work end-to-end, you will need the following minimal permissions to be enabled as part of the API scope:

* admin:project:bitbucket
* admin:repository:bitbucket
* read:account
* read:me
* read:permission:bitbucket
* read:project:bitbucket
* read:pullrequest:bitbucket
* read:repository:bitbucket
* read:webhook:bitbucket
* write:permission:bitbucket
* write:pullrequest:bitbucket
* write:repository:bitbucket
* write:webhook:bitbucket

### Creating an API Token

1. Go to **Settings** → **Account settings** (Atlassian account settings)
2. Go to **Security** → **API tokens with scope**
3.  Once the API token is generated, the customer should use the Bitbucket repository URL while configuring the connection.

    **Example:**\
    Repo URL: [`https://bitbucket.org/pavankumar_kodange/arm-test.git`](https://bitbucket.org/pavankumar_kodange/arm-test.git)

    * **Username:** `pavankumar_kodange`
    * **Password:** _(API token generated from Atlassian Account Settings → Security → API tokens with scope)_

### **Storing your Bitbucket credential in ARM**

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on the **`Credentials`** tab.
3. Next, click **`Create Credential`**.
4. On the next pop-up screen, give a **`credential name`**.
5. Choose the **`Credential Type`** as **`Username with Password`**.
6. Enter your Bitbucket **`username`** and **`App Password`**.
7. Click **`Save`**.

### Registering a Bitbucket repository in ARM <a href="#registering-a-bitbucket-repository-in-arm" id="registering-a-bitbucket-repository-in-arm"></a>

If you wish to set up a Bitbucket repository, ensure that you have an account created and configured at Bitbucket. Next, follow these steps:

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
10. Once the registration is successfully done, you can find the newly added repository on **`VC Repo's`** home page.
