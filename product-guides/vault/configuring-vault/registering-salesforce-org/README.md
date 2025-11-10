# Registering Salesforce Org

### Overview <a href="#overview" id="overview"></a>

When you register your Salesforce Organization, Vault is connected to your Salesforce org with required permissions that enable you to backup your data and metadata information.

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

You will need a Salesforce account. To sign up for your developer account in Salesforce, refer to the link: [`https://developer.salesforce.com/signup`](https://developer.salesforce.com/signup). Once you fill in all the details with a valid **email address**, you'll get an invitation link in your email to activate your account.

### Registering a Salesforce Account <a href="#registering-a-salesforce-account" id="registering-a-salesforce-account"></a>

To register a Salesforce org with Vault, follow the steps below in sequence:

1. Authenticate your Salesforce Org via HTTP Basic Auth or OAuth 2.0.
2. Set up a backup configuration for your Salesforce Org.
3. Schedule a backup for your Salesforce Org.
4. Set up an archive configuration for your Salesforce Org.

#### _Salesforce Org Authentication via HTTP Basic Auth or OAuth 2.0_ <a href="#salesforce-org-authentication-via-http-basic-auth-or-oauth-20" id="salesforce-org-authentication-via-http-basic-auth-or-oauth-20"></a>

1. Log in to your **Vault** account using your credentials.
2. Visit **`Setup > Register New Org`** from the Vault homepage.

<figure><img src="../../../../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

3. Next, choose an authentication type to register the org. Usually, there are two ways to authenticate your Salesforce org: **`OAuth`** or **`Standard (username/password)`**.
   * **OAuth Authentication**: An industry-standard protocol specification enables third-party applications (such as Salesforce) to gain delegated access to protected resources in Vault via an API. To use **OAuth authentication**, you must choose the **`Environment`** as **Salesforce** and select the **`Salesforce API version`** from the dropdown. Select your **`Salesforce Org type,`** i.e., _productions_, _sandbox_, or enter your _custom org type_. Enter the desired name for the org in the **`Org Title`** field and the **`Salesforce username`**. On selecting **`Authenticate`**, the page redirects you to the **Salesforce** login screen, where you enter your authentication details. You will be redirected to the Vault login page after successful authentication.

<figure><img src="../../../../.gitbook/assets/image (197).png" alt="" width="500"><figcaption></figcaption></figure>

* **Standard Authentication**: In **`Standard`** authentication, the desired **`Salesforce Cloud environment`**, the **`username`**, **`password`**, and the **`security token`** of Salesforce are entered, and Vault authenticates the connection. You would have received the security token through email when you initially set up your account or reset your password on the most recent occasion. Your token can also be reset independently. To reset your security token, go to **`My Settings > Personal > Reset My Security Token`** in Salesforce.\
  To test whether Vault can connect to the target Salesforce organization when using the credentials of the target Salesforce user, click on **`Test Connection`**.

<figure><img src="../../../../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

4. Finally, click on the **`Save`** button to complete the authentication process.
5. When the user selects the '**Custom**' option under the '**Org Type**' dropdown, the following note will be visible beside the '**Authenticate**' button: **“Use only Salesforce Classic URL for the 'Instance URL'; Lightning URL is not supported.”**

<figure><img src="../../../../.gitbook/assets/image (199).png" alt=""><figcaption></figcaption></figure>

### What's Next? <a href="#whats-next" id="whats-next"></a>

Once you register your Salesforce Org with  Vault, you will automatically navigate to the **`Configs`** tab. The next step is to set up a [backup configuration for your Salesforce Org](setup-backup-configuration-for-salesforce-org.md). The configuration backup job creates a snapshot of the data/metadata from your Salesforce org and retrieves the data required for a successful restore. If you're not redirected in the first place, you can always do so by navigating to **`Setup > Selecting your Salesforce Org >`** **`Configs > Add Backup Config`**. Proceed with the backup or archival configurations when you register your Salesforce org. [**Read More---->**](setup-backup-configuration-for-salesforce-org.md)

Similarly, you can set up an [archive configuration](archival-configuration.md) using  **`Add Archive Config`** on the **`Configs`** screen. Data Archive is about moving unwanted data components from your Salesforce Org and freeing up space for new data. With Vault, this data is safely stored for future use. In a nutshell, Vault makes Salesforce data archiving and backup a simple, productive, and effective process. [**Read More---->**](archival-configuration.md)

### Manage ORG Details

Managing ORG login details is now more streamlined with the new capability to edit and authenticate registered ORGs. The newly introduced **“EDIT”** option allows updating outdated or incorrect login credentials, ensuring that stale user details are removed from the Vault application and replaced with active, verified credentials.

About The Feature

This feature enables the secure update of login credentials for an existing ORG without affecting any associated configurations or jobs. Once the new credentials are authenticated, they are seamlessly bound to the existing ORG, ensuring uninterrupted access to configurations and scheduled jobs. This enhances operational continuity and supports compliance requirements where regular credential updates are necessary.

Step-By-Step Guide:

1.  Open any ORG through the “Setup” of the Vault application.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2. On opening the ORG click on the EDIT button to initiate editing the ORG details.
3.  Upon clicking the **EDIT** button, the fields **Org Type**, **Org Title**, and **User Name** become editable, allowing the user to make the intended updates.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. Based on the requirement update the fields “Org Type” and “Org Title” as required.
5. For updating the “User Name” authentication is required, as the login is tied to the ORG, changing the username requires authentication.
6.  Enter the required “User Name” and click on “AUTHENTICATE” to initiate the authentication.

    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. On clicking the “AUTHENTICATE” the flow will navigate to the Salesforce login page.
8.  Observe the username and continue to enter the password.

    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
9. On clicking “ALLOW” the flow will navigate to the Vault application where a message will be displayed referring to the change in the user details.
10. Read through the message and click on “OK” or “CANCEL”, to continue with the message.
11. On clicking “OK”, the login details will be updated and a message inferring the same will be displayed on the application.

    <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
12. With this the user details are updated successfully on the existing ORG
