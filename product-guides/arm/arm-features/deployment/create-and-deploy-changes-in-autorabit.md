# Create and Deploy Changes in AutoRABIT

### Deployment in ARM <a href="#deployment-in-arm" id="deployment-in-arm"></a>

The deployment process allows you to quickly and safely transfer new developments from your sandbox instance to a production instance. In this article, we'll go over how to perform the deployment operation in the ARM application.

#### 1. Configuring Deployment Details <a href="#id-1-configuring-deployment-details" id="id-1-configuring-deployment-details"></a>

1. Log in to your ARM account.
2. Click on the **`Deployment`** module.
3. Click on **`New Deployment`**.

\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656592937821.png" alt=""><figcaption></figcaption></figure>



1. On the **`New Deployment`** page, choose the basic parameters of your deployment, including the source org from which you'll be retrieving output and the destination org from which you'll be deploying the retrieved components.
2. Give your deployment a name.
3. Choose the deployment method from the **`Deployment From`** dropdown to carry out the deployment. There are approx. 10-14 different deployment ways to carry out your deployment in the ARM application.

\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656593093596.png" alt="" width="375"><figcaption></figcaption></figure>



1. Important Note: Only the new release labels for which the package has been successfully prepared will be visible in the **Release Label** dropdown if you choose **Deployment From:** **Release Label**. Release labels created before the **22.3** release will not be visible under this dropdown yet. Please go to the **Release Label Summary** screen and click **Create Artifact** to prepare the package. Then, the release label will be available to use for deployment.
2. Choose the **`Metadata Type(s)`**. This allows you to deploy the entire Salesforce Org, Full Profiles, or Permission Sets.
   1. **`Full Profiles`** fetches all the profiles available in the selected source.
   2. **`Full Permission Sets`** fetches all the permission sets from your selected source.
3. Select your **`Source Org/`**[**`Version Control`**](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/).
4. Select your **`Destination Org`**.
5. Choose the **`Deployment Type:`**
   1. **`Selective Deployment`** is a deployment in which only the metadata types you’ve selected are deployed from the source org to the destination org.
   2.  **`Full Deployment`** transfers all metadata types in the source org to the destination org. However, a few metadata types, such as dynamic package XML files, can’t be retrieved in this process. In this case, the irretrievable data types will generate warnings during deployment, but ARM will continue the deployment and transfer the retrievable metadata types.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656593431871.png" alt="" width="375"><figcaption></figcaption></figure>

#### 2. Metadata Filter (optional) <a href="#id-2-metadata-filter-optional" id="id-2-metadata-filter-optional"></a>

The **`Metadata Filter`** section allows you to specify filters limiting the [metadata](https://www.autorabit.com/blog/why-do-i-need-to-protect-my-salesforce-metadata/) included in your deployment. You can enter filter parameters here or leave these fields blank if they do not apply.

#### 3. Additional Profile/PermissionSet Refactoring Settings <a href="#id-3-additional-profilepermissionset-refactoring-settings" id="id-3-additional-profilepermissionset-refactoring-settings"></a>

This section lets you control how the profile settings and permissions are passed on from the source org during the deployment. Remember that in **API version 40.0 and later**, when the user deploys retrieved permission set output from one org to another, the metadata in the deployment replaces the target org metadata. In **API version 39.0 and earlier**, the deployment contents are merged with the current org data.

* **`Deploy Profile Access Settings for selected components only:`** Select this check box to refactor the profile settings based on the selected components. Refactored profiles are deployed along with the selected components.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656594840166.png" alt="" width="375"><figcaption></figcaption></figure>

#### 4. Selection of Metadata <a href="#id-4-selection-of-metadata" id="id-4-selection-of-metadata"></a>

Once you're done with the initial setup for your deployment, click on **`Retrieve Metadata`**. You'll be redirected to the metadata selection screen, which allows you to select the metadata components for deployment. You can also use the search filter to find particular metadata types quickly.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1676633626270.png" alt="" width="563"><figcaption></figcaption></figure>

The selected components will be listed under the **`Selected Items`** tab.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656596058753.png" alt="" width="375"><figcaption></figcaption></figure>

You’ll see the list of metadata components in your target org but not in your source under the **`Destructive Items`** tab. Check the box next to a component you want to delete, and it will be deleted when you deploy. For a detailed explanation of destructive changes, refer to the article: [Destructive Changes](destructive-changes.md).\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656596073273.png" alt="" width="563"><figcaption></figcaption></figure>

Once you’ve chosen the metadata members to include in the deployment, select one of the two options at the bottom of the page:

* **`Deploy:`** This option will immediately deploy to the destination org.
* **`Compare Metadata & Deploy (recommended):`** This option allows you to compare the metadata members between the two sources before you proceed with the deployment.

#### 5. Compare Metadata & Deploy <a href="#id-5-compare-metadata-deploy" id="id-5-compare-metadata-deploy"></a>

On this screen, you will be presented with a list of metadata types and their respective member lists.

Deployment via Salesforce Org Further expanding the member's list will allow you to view the members' dependent components, and selecting them means deploying the dependent components to the destination org.

The **`Diff`** tab will indicate if there are any differences between the members from the source and the target org.&#x20;

* If there are no differences, the right column will display the![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(54\).png)icon for each member.
* If there are any differences, the right column will display the![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(55\).png)icon.

![Salesforce Deployment](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1614019893712.png)

Clicking on the difference icon in the right column will display a new page with details of the differences between the orgs. You will have the option to download the log from this page. If the difference report contains more than 10,000 lines, it is best practice to download the report first and view its changes.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1614020465745.png" alt="" width="563"><figcaption></figcaption></figure>

When you have determined which metadata members to include in the deployment, click the checkbox next to each member to select it, and then click the **`Deploy`** button. It will take you to the **`Deployment Settings`** page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1614020712178.png" alt="" width="563"><figcaption></figcaption></figure>

#### 6. Deployment Settings and Filters <a href="#id-6-deployment-settings-and-filters" id="id-6-deployment-settings-and-filters"></a>

On the **`Deployment Settings`** page, you will be presented with a list of filters to use in the [deployment](https://www.autorabit.com/blog/autorabit-tames-complex-software-deployments/):\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656658812827.png" alt="" width="563"><figcaption></figcaption></figure>

| Filters                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ignore warnings                               | When this filter is checked, metadata types that trigger warnings during the retrieval process will not cause the deployment to fail, and ARM will deploy all other metadata types as possible.                                                                                                                                                                                                                                                                                                                                                                                             |
| Validate only                                 | Checking this option will validate and save the deployment label without actually executing the deployment. The label can then be used later for a Quick Deploy if the target org is a production environment against which the validation was done                                                                                                                                                                                                                                                                                                                                         |
| Take backup                                   | This option creates a backup of the original state of the metadata to which you can revert if the deployment fails or has other functional issues. **This option will not be visible for "deployment via Vlocity components".**                                                                                                                                                                                                                                                                                                                                                             |
| Ignore missing visibility settings (profiles) | With this option, differences in visibility settings between the source and destination orgs will not cause the deployment to fail. ARM will compare the source and destination orgs and keep only the common settings between both orgs. Standard fields are not supported for this option.                                                                                                                                                                                                                                                                                                |
| Remove Login IP Ranges                        | This option will remove IP ranges from your profile while deploying                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Remove System and User Permissions            | Remove the user's permission from your profile while deploying.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Do not include 'Destructive members'          | Select this checkbox if you have configured certain metadata types to skip while deploying. You can configure such metadata types under the **`Admin >`** [**`Salesforce Org Management`**](../../getting-started/salesforce-org-management.md) page                                                                                                                                                                                                                                                                                                                                        |
| Ignore installed components                   | When selected, ARM will scan for the components that are deployed, and if there are any managed package components located in the target org, these components will be excluded from the metadata.zip files while the remaining components are deployed.                                                                                                                                                                                                                                                                                                                                    |
| Fetch Wavexmd components                      | <p>Upon selection, this checkbox will allow you to select the respective wavexmd files belonging to the wave dashboard metadata type and deploy them via selective deployment to another Salesforce Org. This checkbox will be hidden if the <strong>WaveDashboard</strong> metadata type or its corresponding members are not picked.<br><br><strong>Note:</strong>This feature is currently applicable only for the following deployment methods:</p><ul><li>Deployment via Salesforce Org</li><li>Deployment via Package XML</li><li>Deployment via Previous Deployment Labels</li></ul> |

**`Apex Test Level:`** Next, choose the Apex unit test level to validate your deployment. To know more about Apex tests, please refer to the article: [Apex Unit Tests](https://knowledgebase.autorabit.com/arm/docs/apex-unit-tests).

**`Static Code Analysis (SCA)`**: Choose the SCA tool to detect bugs, code smells, and security vulnerabilities before the deployment begins.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656659193140.png" alt="" width="375"><figcaption></figcaption></figure>

SCA Supported Metadata Types:

* For **ApexPMD, Checkmarx, SonarQube**: _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
* For **Codescan**: _ApexClasses, ApexPages, ApexTriggers, AuraDefinitionBundle, CustomObjects, Flow, LightningComponentBundle, PermissionSets, Profiles, Settings, SharingRules, Workflows._

You can stop the deployment if the SCA doesn't meet the criteria set globally. Go to **`My Account >`** [**`Validation Criteria- Static Code Analysis`**](../../arm-administration/user-management/manage-users-account-settings/) to set the global configuration for your SCA tool.

Also, you can select the recipients for the alert under the **`SCA Mail Notifications`** field. Multiple recipients can be added here.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656659294706.png)

[**`Search and Substitute`**](../../arm-administration/search-and-substitute.md) If you have created the search and substitute rules to define custom find and substitute rules that ARM applies whenever you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control, or vice-versa, such rule can be found here.&#x20;

From the **`Apply Search and Substitute Rules`** list, select the rule that will be associated with the current deployment process. Use the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402857647.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402882169.png) button to add/remove the rule and using the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402900576.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402922812.png) button, move the rules list up and down. Based on the selection, the top rule will be deployed initially, and the process will continue for the remaining rules.

**`Fetch the Test Cases:`** Before running the deployment, you may like to run the functional test cases to test the code's functionality being deployed to the Destination Environment. Therefore, select how you would like to fetch the test cases.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656673582738.png)

**`Deployment Notes:`** In the Deployment Notes box, specify the reason for the deployment and what has changed across your Salesforce Org.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1656673657412.png" alt="" width="375"><figcaption></figcaption></figure>

#### 7. Final Configuration <a href="#id-7-final-configuration" id="id-7-final-configuration"></a>

The next screen is the **`Deployment Summary`** page, where you can view the components one final time before deployment.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Click on **`Validate Deployment.`** You will be redirected to the [Deployment Summary](monitor-deployments.md) screen, showing the deployment progress.
