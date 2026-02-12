# Azure DevOps YAML Pipeline

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

{% hint style="info" %}
**Note**: Users have Azure SSO enabled in CodeScan. If an integration user has to be set up for Jenkins/Bitbucket projects, then the user must be created in Azure SSO.
{% endhint %}

## Install the CodeScan Cloud Extension <a href="#install-the-codescan-cloud-extension" id="install-the-codescan-cloud-extension"></a>

1. In the **Azure DevOps** app, go to the **Marketplace** and then select **Browse Marketplace**.
2. Search for **CodeScan**, select the **CodeScan Cloud** extension and then click **Get it free**.
3. Select your **account** and complete the installation.

### Create a Service Endpoint

1. Open **Project Settings**&#x20;
2. Under **Pipelines** select **Service Connections**
3. Select **CodeScanCloud** from the list and click Next
4. Add your CodeScan server URL (e.g., https://app.codescan.io/)
5. You will need a **token** from your CodeScan Cloud account for this step. [Learn how to create security token here](https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/setting-up-a-codescan-cloud-organization/generate-a-security-token).
6. Add a name for your connection.
7. If you would like this connection available everywhere, click **Grant access permissions to all pipelines**. If you would like to restrict the use of this connection, leave this box unchecked and [see this article](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#set-service-connection-security-in-azure-pipelines).
8. Click **Verify and Save**

## Setup <a href="#setup" id="setup"></a>

1. On your **Project** dashboard screen, select **Pipeline > Pipelines** and create a **new Pipeline**.
2. Once you are in the "**Where is your code?**" page, select the source of your code. &#x20;
3. On the **Select a Repository** page, select the repository you would like to scan from.
4. On the **Configure Your Pipeline** page, select **Starter Pipeline**
5. You should see a bare bones YAML file.  Remove the header comments, test step and script as you wont need those.

#### Add Prepare Analysis Configuration <a href="#azure-devops-repo" id="azure-devops-repo"></a>

1. On the right hand side of the page, click **Show Assistant**&#x20;
2. Search for **CodeScan**&#x20;
3. Click on **Prepare Analysis Configuration**.&#x20;
4. Select your new **Service Endpoint** and the **Organization** you would like to connect to from the dropdown menu. If you are not sure, the [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys) is available at the top left of your **Organization** page.
5. Select **Use standalone scanner** under the **Choose a way to run the analysis**.
6. Under **Mode**, select the **Manually provide configuration** checkbox.
7. Click **Add**

#### Now, in CodeScan Cloud we can set up the project. <a href="#now-in-codescan-cloud-we-can-set-up-the-project" id="now-in-codescan-cloud-we-can-set-up-the-project"></a>

1. In your selected [CodeScan Cloud](https://www.codescan.io/products/cloud/) organization, navigate to **Administration > Projects Management**.
2. Click **Create Project**.
3. Enter your desired **Project Name** and **Project Key** and click **Create**. Keep these in mind, we'll need them in a second.
4. Click on your new empty project and navigate to **Administration > Branches and Pull Requests**.
5. Change your _main branch_ name to the name of the _default branch_ that you selected.

#### Now, back to Azure DevOps. <a href="#now-back-to-azure-devops" id="now-back-to-azure-devops"></a>

1. Enter the **Project Name** and **Project Key** you just created.
2. Click on **Advanced.** Remove the contents and add **sonar.qualitygate.wait=true .** This will fail the analysis if the Quality Gate fails.
3. Click **Add**

#### Add Run Code Analysis

1. On the right hand side of the page, click **Show Assistant**&#x20;
2. Search for **CodeScan**&#x20;
3. Click on **Run Analysis**
4. Click **Add**

#### Add Publish Quality Gate Result

1. On the right hand side of the page, click **Show Assistant**&#x20;
2. Search for **CodeScan**&#x20;
3. Click on **Publish Quality Gate Result**
4. Click **Add**

Your script should now look similar to the image below.

<figure><img src="../../../../.gitbook/assets/image (2423).png" alt=""><figcaption></figcaption></figure>

### Triggering Builds from a Repository <a href="#triggering-builds-from-an-azure-devops-repository" id="triggering-builds-from-an-azure-devops-repository"></a>

The triggers in Azure DevOps can be configured for pushes to your branches or pull requests made against them.

[Please see this article for information on triggers in YAML.](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops#branch-consideration-for-triggers-in-yaml-pipelines)

