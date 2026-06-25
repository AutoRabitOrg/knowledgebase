# Bitbucket

{% hint style="warning" %}
Bitbucket App Passwords are being deprecated by Atlassian and **will no longer be supported after June 9, 2026**. Depending on your Bitbucket environment and rollout status, you may already be unable to create new App Passwords. AutoRABIT recommends using Bitbucket API Tokens for all new integrations.\
\
For all new Bitbucket integrations, AutoRABIT recommends using **Bitbucket API Tokens** instead of App Passwords.

For more information, see: [**Bitbucket App Password Deprecation – Action Required Before June 9, 2026**](../../../../../../fundamentals/announcements/bitbucket-app-password-deprecation-action-required-before-june-9-2026.md)**.**
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

#### Store your Bitbucket credential in ARM <a href="#store-your-bitbucket-credential-in-arm" id="store-your-bitbucket-credential-in-arm"></a>

This is an initial step where you store your user's credential (usually a username, password, or token) in ARM.

To authenticate Bitbucket, you’ll have to use **API Tokens** instead of the regular password to log in to your Bitbucket account.

**Steps to generate a Bitbucket API Token**

1. Log in to your Bitbucket account.
2. Click your account’s **`profile picture`** in the top right-corner of the Bitbucket webpage.
3. Click the **`Personal Settings`** link in the dropdown menu.
4. Navigate to **`API Tokens`**.
5. Select the link on the left labeled **`Create API Token with Scopes`**. It is under the **`Access Management`** heading.
6. Click on **`Create API Tokens`** button.
7. Enter a **`label name`** and check all the necessary permissions that you’d want to provide.&#x20;
   1. Select the following required scopes:
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
8. Click **`Create`** to generate the Bitbucket API Token and copy the access token’s value. You will not be able to view this token again once you close this window.
9. Click **`Save`**.

{% hint style="info" %}
Tokens created without the required scopes may fail authentication or repository registration.
{% endhint %}

**Store your Bitbucket credential in ARM**

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** module and click on the **`Credentials`** tab.
3. Next, click **`Create Credential`**.
4. On the next pop-up screen, give a **`credential name`**.
5. Choose the **`Credential Type`** as **`Username with Password`**.
6. Enter your Bitbucket **`username`** and **`API Token`**.
7. Click **`Save`**.

The credential is now available for use when registering Bitbucket repositories in ARM.

#### Registering a Bitbucket repository in ARM <a href="#registering-a-bitbucket-repository-in-arm" id="registering-a-bitbucket-repository-in-arm"></a>

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



### Troubleshooting

#### Unable to Create an App Password

Bitbucket App Passwords are being deprecated by Atlassian and may no longer be available in some environments. Link to announcement: [https://knowledgebase.autorabit.com/fundamentals/announcements/bitbucket-app-password-deprecation-action-required-before-june-9-2026#overview](https://knowledgebase.autorabit.com/fundamentals/announcements/bitbucket-app-password-deprecation-action-required-before-june-9-2026#overview)

Create and use a Bitbucket API Token instead.

#### Authentication Failed

Verify that:

* The API Token is active.
* The API Token was created using **Create API Token with Scopes**.
* All required scopes have been assigned.
* The Bitbucket user has access to the repository.

#### Repository Registration Failed

Verify:

* Repository URL and configuration details.
* API Token permissions.
* Repository access permissions.
* Connectivity between ARM and Bitbucket.

If the issue persists, contact AutoRABIT Support.
