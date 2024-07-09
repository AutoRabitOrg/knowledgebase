# Azure DevOps

### What is Azure DevOps? <a href="#what-is-azure-devops" id="what-is-azure-devops"></a>

Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications. Azure DevOps supports culture and set of processes that bring developers and project managers and contributors together to complete software development. It allows organizations to create and improve products at a faster pace than they can with traditional software development approaches.

To learn more about Azure DevOps Services, see [Introduction to Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops)

### Setting Up Azure DevOps in AutoRABIT <a href="#setting-up-azure-devops-in-autorabit" id="setting-up-azure-devops-in-autorabit"></a>

This article refers to the AutoRABIT and Azure DevOps integration. AutoRABIT provides a two-way integration with Azure DevOps that allows product teams to send their planned work from AutoRABIT to their development team working in Azure DevOps.

To integrate Azure DevOps as a plugin in AutoRABIT, follow the below steps:

1. Log in to your AutoRABIT account.
2. From the AutoRABIT home page, click on the **Admin** module and go to the **My Account** tab.

<figure><img src="../../../.gitbook/assets/image (34) (1) (1) (1).png" alt="" width="289"><figcaption></figcaption></figure>

3. Click on **New ALM System** under **ALM Management**.

<figure><img src="../../../.gitbook/assets/image (35) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Select the ALM type as **Azure DevOps**.

<figure><img src="../../../.gitbook/assets/image (36) (1) (1) (1).png" alt="" width="379"><figcaption></figcaption></figure>

5. Enter the **label name** and paste the **Azure DevOps host URL**.
6. Select the user credential from the drop-down field. In case the user detail is not stored in AutoRABIT, click on **Create Credentials**.
7. Once you are done, click on **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
8. Click **Save (**![](<../../../.gitbook/assets/image (37) (1) (1) (1).png>)**)** and you are all set with Azure DevOps Integration.
9. Once you log in, Azure DevOps is integrated with your AutoRABIT account and you can start logging issues with just one click directly to Azure DevOps.

{% hint style="info" %}
**Note:**

1. To create a new credential, you need to give a **credential name**, choose the **credential type** i.e., User Name / Password credentials or basic SSH Private Key type, and the **credential scope** (global or private).
2. For **User Name/Password** as credential type authentication, a secured personal access token is required. The same token should be entered in the **Password** field.&#x20;
{% endhint %}

### Authentication Access via Azure DevOps Personal Access Tokens <a href="#authentication-access-via-azure-devops-personal-access-tokens" id="authentication-access-via-azure-devops-personal-access-tokens"></a>

1. Sign in to your organization in **Azure DevOps** _(https://dev.azure.com/{yourorganization})._
2. From your home page, navigate to your **Profile > Security** to view your security details.

<figure><img src="../../../.gitbook/assets/image (39) (1) (1) (1).png" alt="" width="275"><figcaption></figcaption></figure>

3. Go to **Security > Personal access token** and click on **+ New Token** to create a personal access token.

<figure><img src="../../../.gitbook/assets/image (40) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, **name** your token. Select a **lifespan** for your token.

<figure><img src="../../../.gitbook/assets/image (41) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Select the **scopes** that this token will authorize for your specific tasks.

<figure><img src="../../../.gitbook/assets/image (42) (1) (1) (1).png" alt="" width="458"><figcaption></figcaption></figure>

6. Click on **Create Token** available at the bottom of the screen.
7. When you're done, make sure to copy the token. You'll use this token as your password.

<figure><img src="../../../.gitbook/assets/image (43) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Enter the same token in the **Password** field while registering the user's credential via **UserName/Password** credential type in AutoRABIT.

### Mapping Azure DevOps ALM to your Salesforce Org/Version Control <a href="#mapping-azure-devops-alm-to-your-salesforce-orgversion-control" id="mapping-azure-devops-alm-to-your-salesforce-orgversion-control"></a>

Once you are done registering the plugins with AutoRABIT, make sure you map the Azure DevOps ALM with your required Salesforce Org/Version Control.

1. Login to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **SF Org Mgmt**
3. Select the **Salesforce org** for which you like to map the Azure DevOps as an **ALM**.
4. Under **Salesforce Org- Mappings** tab, choose **Azure DevOps** as ALM type and click on **Mapping**.

<figure><img src="../../../.gitbook/assets/image (44) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Select the **label** and the **project**.
6. Click **Save Mappings**.
