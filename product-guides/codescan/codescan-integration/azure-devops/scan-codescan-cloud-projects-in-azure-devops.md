# Scan CodeScan Cloud projects in Azure DevOps

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* CodeScan version **4.4+**
* An Azure DevOps Project for your Salesforce code

{% hint style="info" %}
**Note**: Users have Azure SSO enabled in CodeScan. If an integration user has to be set up for Jenkins/Bitbucket projects, then the user must be created in Azure SSO.
{% endhint %}

## Install the CodeScan Cloud Extension <a href="#install-the-codescan-cloud-extension" id="install-the-codescan-cloud-extension"></a>

1. In the **Azure DevOps** app, go to the **`Marketplace`** and then select **`Browse Marketplace`**.
2. Search for **`CodeScan`**, select the **`CodeScan Cloud`** extension and then click **`Get it free`**.
3. Select your **account** and complete the installation.

## Setup <a href="#setup" id="setup"></a>

1. On your **`Project`** dashboard screen, select **`Pipeline > Pipelines`** and create a **new Pipeline**.
2. Once you are in the "**Where is your code?**" page, click **Use the classic editor to create a pipeline without YAML**.

Follow the instructions below for your source code location.

### Azure DevOps Repo <a href="#azure-devops-repo" id="azure-devops-repo"></a>

1. Select **`Azure Repos Git`** and your **`Repository name`**.
2. For your default branch, select the **`branch`** you would like to check pull requests against. Keep this branch name in mind, we will use it later in the setup. Click **`Continue`**.
3. On the **`Select a Template`** page, select the **`Salesforce with CodeScan Cloud`** template and click **`Apply`**.
4. In the Agent pool dropdown menu, select **`Azure Pipelines`**.
5. In the **`Agent Specification`** dropdown menu, select **`ubuntu-20.04`**.
6. Click the **`Prepare Analysis on CodeScan Cloud`** section and create a new service endpoint.
   * Add your CodeScan server URL (e.g., https://app.codescan.io/)
   * You will need a **token** from your CodeScan Cloud account for this step. Learn how to create security token [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).
   * Add a **name** for your connection.
   * Make sure to **verify the connection** before leaving the pop-up.
7. Select your new **`Service Endpoint`** and the **`Organization`** you would like to connect to from the dropdown menu. If you are not sure, the [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys) is available at the top left of your **`Organization`** page.
8. Select **`Use standalone scanner`** under the **`Choose a way to run the analysis`**.
9. Under **`Mode`**, select the **`make sure Manually provide configuration`** checkbox.

#### Now, in CodeScan Cloud we can set up the project. <a href="#now-in-codescan-cloud-we-can-set-up-the-project" id="now-in-codescan-cloud-we-can-set-up-the-project"></a>

1. In your selected [CodeScan Cloud](https://www.codescan.io/products/cloud/) organization, navigate to **`Administration > Projects Management`**.
2. Click **`Create Project`**.
3. Enter your desired **`Project Name`** and **`Project Key`** and click **`Create`**. Keep these in mind, we'll need them in a second.
4. Click on your new empty project and navigate to **`Administration > Branches and Pull Requests`**.
5. Change your _main branch_ name to the name of the _default branch_ that you selected.

#### Now, back to Azure DevOps. <a href="#now-back-to-azure-devops" id="now-back-to-azure-devops"></a>

1. Enter the **`Project Name`** and **`Project Key`** you just created.
2. Click **`Save and Queue`** and let the analysis complete to see your results in CodeScan Cloud.

## Triggering Builds from an Azure DevOps Repository <a href="#triggering-builds-from-an-azure-devops-repository" id="triggering-builds-from-an-azure-devops-repository"></a>

To trigger the builds, you will need to create a build policy on the branch you would like to check pull requests against.

1. Navigate to **`Repos > Branches`**.
2. Click on the **`More`** menu for the desired branch and click **`Branch Policies`**.
3. In the **`Build Validation`** section, **`add a new build policy`**.
4. Select your **`new pipeline`** and select **`Automatic for the Trigger settings`** and choose your policy requirements.

This pipeline will now run when:

* Pull requests are created against the branch
* Pull requests are updated
* Pull requests are merged.

The **project branches** on CodeScan Cloud will be updated accordingly.

## Breaking the Builds <a href="#breaking-the-builds" id="breaking-the-builds"></a>

To break the builds based on the Quality Gate once this analysis has run, you can add a _PowerShell script_ to the pipeline.

1. First create a [Security Token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token) and add it as a variable named **`CODESCAN_TOKEN`** in your pipeline Variables menu.
2.  Add a PowerShell step to your pipeline after the Publish Quality Gate step and add the following script inline, changing the below parameters:

    > **`<<project_key>>`** to your actual project key.
    >
    > **`{codescan_instance_url}:`** Your instance's URL, for example, [_https://app.codescan.io/_](https://app.codescan.io/) for **US** region, [_https://app-eu.codescan.io/_](https://app-eu.codescan.io/) for **EU** region or [_https://app-aus.codescan.io/_](https://app-aus.codescan.io/) for **AUS** region.

{% code fullWidth="true" %}
```
 $token = [System.Text.Encoding]::UTF8.GetBytes($env:CODESCAN_TOKEN + ":")
 $base64 = [System.Convert]::ToBase64String($token)
 $basicAuth = [string]::Format("Basic {0}", $base64)
 $headers = @{ Authorization = $basicAuth }
 
 Write-Host "Pull Request ID:$($env:SYSTEM_PULLREQUEST_PULLREQUESTID)"
 
 $Target = "$env:SYSTEM_PULLREQUEST_PULLREQUESTID"
 $URL = "{codescan_instance_url}/api/qualitygates/project_status?projectKey=<<project_key>>&pullRequest={0}"
 
 if( !$Target)
 {
   $Target = "$env:BUILD_SOURCEBRANCH"
   $Target = $Target.Replace('refs/heads/','')
   $URL = "{codescan_instance_url}/api/qualitygates/project_status?projectKey=<<project_key>>&branch={0}"
 } 
 
 $URL = [string]::Format($URL, $Target)
 
 $result = Invoke-RestMethod -Method Get -Uri $URL  -Headers $headers
 $result | ConvertTo-Json | Write-Host
  
 if ($result.projectStatus.status -eq "OK") {
 Write-Host "Quality Gate Succeeded"
 }else{
 throw "Quality Gate failed"
 }
```
{% endcode %}

The pipeline will now fail if the quality gates for the project are not passed.
