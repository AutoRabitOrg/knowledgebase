# Deploying OmniStudio Components

### Overview <a href="#overview" id="overview"></a>

OmniStudio integration with ARM allows you to retrieve and deploy OmniStudio metadata in the same way as Salesforce metadata and deploy OmniStudio components to the destination Salesforce org directly from ARM. Using the Deployment feature in ARM, you can quickly deploy components to your destination environment.&#x20;

### Before you begin <a href="#before-you-begin" id="before-you-begin"></a>

Before you proceed with the deployment, it is mandatory to configure your OmniStudio data pack type from the **My Account > OmniStudio Configuration Settings** section.

<figure><img src="../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Deploying OmniStudio Components <a href="#deploying-vlocity-components" id="deploying-vlocity-components"></a>

1. Log in to your AutoRABIT account.
2. Click on **Create New > New Deployment** from the top navigation bar.

<figure><img src="../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="299"><figcaption></figcaption></figure>

3. Give a **label** name for the deployment.
4. Choose **Deployment From** as **OmniStudio Components.**

<figure><img src="../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="350"><figcaption></figcaption></figure>

5. Select the **Source Pack** from where the OmniStudio components data packs will be fetched. There are five options to choose from:

| Source Pack               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pack from Salesforce Org  | <p>The OmniStudio components will be fetched from the source Salesforce org. You need to specify the destination org where the OmniStudio components will be deployed.</p><p><img src="../../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"></p><p><strong>Note:</strong> <em>Only those Salesforce orgs must be chosen under the source and the destination org fields in which the</em> OmniStudio <em>managed package is installed.</em><br></p>        |
| Pack from AutoRABIT Build | <p>The OmniStudio components will be fetched from the build number of the specified project, as shown below—only those built to be selected constructed on OmniStudio components.<br><img src="../../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""></p>                                                                                                                                                                                                                        |
| Pack from Version Control | <p>Select this option if you want to fetch the OmniStudio components from your source version control's data pack folder path. For the same, you need to fill in the details such as version control type (GIT, SVN, TFS), repository and its mapped branch, the data pack folder path, and the destination org where the OmniStudio components will be deployed.<br><img src="../../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""></p>                                        |
| Pack from Commit Label    | <p>This will allow you to fetch the OmniStudio components from the data pack folder path of the commit label and deploy them to the destination org. For the same, you need to fill in the details such as version control type (GIT, SVN, TFS), repository and its mapped branch, commit label, data pack folder path, and the destination org where the OmniStudio components will be deployed.</p><p><img src="../../../../.gitbook/assets/image (51) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><br></p> |
| Pack from Release Label   | <p>Pack from Release Label will allow you to fetch the OmniStudio components from the data pack folder path of the release label and deploy them to your destination org.</p><p><img src="../../../../.gitbook/assets/image (52) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><br></p>                                                                                                                                                                                                                             |

6. Choose the **metadata types**. The metadata types field allows you to deploy the entire Salesforce org, Full Profiles, or Permission Sets. _Full Profiles_ will fetch all the profiles available in the selected Salesforce Org, and the _Full Permission Sets_ will allow you to grant additional access to one or more users without changing or reassigning their profiles.
7. Enter your **target org**.
8. Based on the source pack selection, you will have different fields to fill in to proceed with the OmniStudio deployments.
9. Click on **Retrieve Metadata**.
10. Based on the above selection, the metadata components will be fetched and will be displayed on the next screen. Select the metadata and their corresponding members that will be deployed. Click **Deploy**.

<figure><img src="../../../../.gitbook/assets/image (53) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

11. On the **Deployment Settings** page, you will be presented with the filters below to use in the deployment:

    * **Pack Update:** This option will refresh the data packs settings to the version included in the project in the destination org. However, this is recommended only if you are on the latest major version of the OmniStudio managed package. For example, if some of the records that exist as part of the data pack data were not upserted into Salesforce, then it means that there is a mismatch between the configuration data in the target org compared to the source org, so by enabling **Pack Update** checkbox and performing the deployment, then this will update the data pack settings in the target org and will resolve the issue.
    * **Pack Retry**: Continues a Job, retrying all errors to redeploy once again. _**For example**_, if the job contains 10 data packs and where seven were successfully deployed since we enabled the **Pack Retry** option, then the three errors will be set back to redeploy again.

    <figure><img src="../../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
12. **Static Code Analysis (SCA)**: Choose the SCA tool to detect bugs, code smells, and security vulnerabilities before the deployment begins. SCA-Supported Metadata Types:
    * For **ApexPMD, Checkmarx, Salesforce Scanner,** and **SonarQube**: _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
    * For **CodeScan**: _ApexClasses, ApexPages, ApexTriggers, AuraDefinitionBundle, CustomObjects, Flow, LightningComponentBundle, PermissionSets, Profiles, Settings, SharingRules, Workflows._
13. You can stop the deployment if the SCA doesn't meet the global criteria. Go to **My Account >** [**Validation Criteria- Static Code Analysis**](../../../arm/arm-administration/user-management/manage-users-account-settings.md) to set the global configuration for your SCA tool.
14. Also, you can select the recipients for the alert under the **"SCA Mail Notifications"** field. Multiple recipients can be added here.

<figure><img src="../../../../.gitbook/assets/image (55) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="476"><figcaption></figcaption></figure>

15. Under **Deployment Notes**, specify the reason for the deployment and what has changed across your Salesforce org. This is optional too.
16. Click **OK**. The **Deployment Summary** page will be displayed, where you can view the components one final time before deploying them.
17. Finally, click on **Deploy**. You will now be redirected to the **Deployment History** screen, which will show you the progress of the deployment. We just included new functionality to the **ARM 22.3** version that allows users to terminate an ongoing OmniStudio deployment process or abort it if it becomes stuck. The **Deployment History** screen contains the **Abort** option, which allows you to terminate the deployment process.

<figure><img src="../../../../.gitbook/assets/image (56) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

18. The detailed report can be viewed on this page, such as total OmniStudio components successfully deployed, failed components (if any), code coverage details, etc. In addition to viewing the report, you can also download the OmniStudio components packs for the selected deployment.

{% hint style="info" %}
**Important Note:** **Redeploy** and **Rollback** are currently not supported for OmniStudio deployments.&#x20;
{% endhint %}

### Using Continuous Integration (CI) Jobs <a href="#using-continuous-integration-ci-job" id="using-continuous-integration-ci-job"></a>

1. Go to the **New CI Job** screen.

<figure><img src="../../../../.gitbook/assets/image (57) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Select the **Deploy from the Version Control** tile.

<figure><img src="../../../../.gitbook/assets/image (58) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Give the job a descriptive name in the **CI Job Name** field.
4. In the **Build** section, select your version control repository and branch.
5. Select the **OmniStudio Build** checkbox.
6.  Enter the data packs folder path from where the components will be retrieved for the deployment.

    * **Pack Update:** This option will refresh the data packs settings to the version included in the project in the destination org. However, this is recommended only if you are on the latest major version of the OmniStudio managed package.
    * **Pack Retry**: Continues a Job, retrying all errors to redeploy once again.

    <figure><img src="../../../../.gitbook/assets/image (59) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. Fill in the remaining fields as per your requirements and click on **Save**.
