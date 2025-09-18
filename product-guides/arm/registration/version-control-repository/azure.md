# Azure

## Steps to register AzureDevOps Repository/ VCS within ARM

### #1 Prerequisites for registering Azure with ARM

Before registering AzureDevOps Repository with ARM, you must check off some of the boxes on the prerequisites list.

1.  Ensure you enable the GIT plugin under Plugins in the My Account section to use GIT for version control.\


    <figure><img src="../../../../.gitbook/assets/image (2013).png" alt=""><figcaption></figcaption></figure>
2. You must have an Azure account. Once you have an Azure account, you can create a new repository or use an existing one.
3. You must have permission to register a repository.
4. Store your Azure credentials in ARM.

### #2 Store your Azure credential in ARM

1. Log in to your ARM account.
2.  Hover your mouse over the Admin module and click on the Credentials tab.\


    <figure><img src="../../../../.gitbook/assets/image (2014).png" alt=""><figcaption></figcaption></figure>
3. Next, click on Create Credential from the right navigation bar.
4. On the next pop-up screen, give a Credential name.
5.  Choose the Credential Type as Username with Password.\


    <figure><img src="../../../../.gitbook/assets/image (2015).png" alt="" width="563"><figcaption></figcaption></figure>
6. Enter your Azure Username and API Token (in the Password field), and we will store this encrypted.
7. Click Save.

### #3 Registering a GIT repository in ARM

1. Log in to your ARM account.
2.  Hover your mouse over the Admin module and click on VC Repo's.\


    <figure><img src="../../../../.gitbook/assets/image (2016).png" alt="" width="563"><figcaption></figcaption></figure>
3.  Click on Register Repository.\


    <figure><img src="../../../../.gitbook/assets/image (2017).png" alt=""><figcaption></figcaption></figure>
4.  Select the Version Control System as GIT on the Register Repository page.\


    <figure><img src="../../../../.gitbook/assets/image (2018).png" alt=""><figcaption></figcaption></figure>
5. Enter the name of the repository to display it locally.
6. Paste the Repository URL that Azure provides you.
7. Choose the correct user's Credentials from the list. To create new credentials, click on the “+”.

{% hint style="info" %}
Note: Click Test Connection to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
{% endhint %}

8. The Default Branch selection will be in disabled mode by default. Click the icon to fetch and list all the available branches on your remote repository.
9. Select one of the default branches from the list.
10. Once the registration is done, you can find the newly added repository on VC Repo's home page.

#### Points to Remember:

1. Select the Enable SFDX checkbox to register your Azure repository in the SFDX structure.
2. Select the Enable nCino checkbox if you want to register the Azure repository with nCino objects included. To quickly identify nCino registered Version Control Repositories among all other repositories, nCino logos are marked in front of the Repository Label.
3. The user can enable their Version Control Repository with SFDX or nCino enabled. Both cannot be enabled at the same time.

### Creating a Personal Access Token

This section guides you through creating your personal access token directly on Azure.

1. Log in to your Azure account.
2.  In the upper-right corner of any page, click on the user settings beside profile photo, then click on Personal Access tokens.\


    <figure><img src="../../../../.gitbook/assets/image (2019).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (2020).png" alt=""><figcaption></figcaption></figure>

    &#x20;\
    Click on New token.
3. Give your token a descriptive name.
4. Select the scopes or permissions you want to grant this token. Select repo to use your token to access repositories from the command line.
5. Click Create.
6. Copy the token to your clipboard. You cannot see the token again after navigating off the page for security reasons.
7. Use the copied token as a password for creating/updating the credential in ARM.
8. Once updated, please use the same credential to authenticate the Azure.

{% hint style="info" %}
Important Note: Treat your tokens like passwords and keep them secret. When working with the API, use tokens as environment variables instead of hardcoding them into your programs.
{% endhint %}

&#x20;
