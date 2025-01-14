# Release Labels

## Overview <a href="#overview" id="overview"></a>

A Release Label in the ARM application serves as a powerful tool for managing and deploying changes efficiently. By combining multiple commit labels into a single Release Label, teams can bundle together various revisions or code updates into a cohesive package. This approach allows for the seamless deployment of several related updates at one time, reducing the risk of partial deployments and ensuring that all interdependent changes are introduced simultaneously.&#x20;

**The use of Release Labels provides significant benefits, such as:**&#x20;

* Streamlined Deployment: Instead of deploying individual revisions separately, Release Labels allow you to deploy multiple updates at once, saving time and reducing complexity.&#x20;
* Improved Coordination: Release Labels help teams organize and track related updates, making it easier to coordinate large releases or multi-feature rollouts.&#x20;
* Reduced Risk: By bundling related changes, Release Labels reduce the risk of incompatibility issues that can arise from deploying revisions independently.&#x20;

This article will guide you through the process of creating a new Release Label in the ARM application, helping you enhance deployment efficiency and maintain control over your release management process.&#x20;

**Before you begin:**&#x20;

1. Confirm you have the Manage Label permissions to create a new release label. &#x20;
2. Ensure commit revisions were made to the version control branch to combine them under a single Release Label. For more information, refer to the article: [Commit Labels](../commit-labels.md)

## Create a new Release Label <a href="#create-a-new-release-label" id="create-a-new-release-label"></a>

1. Log in to your ARM account.
2. Hover your mouse over the [**`Version Control`**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) module and click on the **`Change Labels > Release Labels`**&#x6F;r go directly to the **`Change Labels`** tab and select **`Release Labels`** from the dropdown.&#x20;

{% hint style="info" %}
**NOTE**: The **Release Label** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

3. Click on **`Create Release Label.`**\


<figure><img src="../../../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

4. On the next screen, give the release label creation process a **`Label Name`** and a short **`Description`**.

<figure><img src="../../../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

5. Select the **`Repository`** and the **`Branch`**&#x63;ontaining the commit labels. \
   \
   Note: For the version control repository registered in the SFDX structure, you must choose an additional option: Package Directory. To learn more about Package Directory, refer to: [Salesforce DX Metadata Format](../../../../salesforce-dx-metadata-format.md).

**Supported Components for Delta Metadata Generation in Release Label Deployments**&#x20;

Delta generation is restricted to specific metadata types for DX and non-DX Release Labels, ensuring consistent and efficient processing by focusing on compatible key metadata. Only the components listed above are supported for delta metadata generation in Release Label Deployments. Metadata types outside of these lists are not currently supported, which applies to both DX and non-DX Release Labels.&#x20;

Note: For a Release Label Full deployment in Salesforce DevOps, no metadata will support incremental (delta) changes. Instead, the deployment will include a complete package based on the updated files, containing the entire file rather than just the changes.&#x20;

**DX Release Labels** \
When deploying with DX Release Labels, delta metadata is generated only for the following components:

* autoResponseRules&#x20;
* bot&#x20;
* escalation Rules&#x20;
* matchingRule&#x20;
* labels&#x20;
* object&#x20;
* sharingRules&#x20;
* workflow&#x20;

**Non-DX Release Labels** \
When deploying with non-DX Release Labels, delta metadata is generated only for the following components:&#x20;

* autoResponseRules&#x20;
* bot&#x20;
* matchingRule&#x20;
* labels&#x20;
* object&#x20;
* translation&#x20;
* sharingRules&#x20;
* workflow&#x20;

1. Select the commit **`Label Type`**, e.g., **`Salesforce`** or **`Vlocity`**.&#x20;

{% hint style="warning" %}
**Known Limitation:** If a branch-to-branch merge involves multiple commits that include data from Vlocity and Salesforce components, ARM cannot classify those commits as **Vlocity** or **Salesforce** components.
{% endhint %}

2. From the **`No of Days`** dropdown list, you can choose to retrieve the commit history for the previous **30**, **60**, **90**, **120**, **180**, or **365** days or **ALL** the commits at once. Please note that selecting **ALL** may result in a slight delay in fetching the entire commit history.
3.  You can create a release label and start the artifact preparation immediately by selecting the **`Create package manifest for Deployment`** checkbox for Salesforce labels. If you do not select this checkbox on this screen, you can still click the **`Create Artifact`** button on the **`Release Label Summary`** screen to create and run a package manually.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682584438782.png" alt="" width="563"><figcaption></figcaption></figure>
4. Click **`Fetch Commit History`** to retrieve all the revisions available on your selected repo and branch. If no records appear, then no revisions were committed to the branch.
5. Select two or more revisions from the left column to group them into a single Release Label. The **`Selected Revisions`** are displayed in a second column on the right side to make it easier to see. You can also unselect revisions from this section.

AutoRABIT now supports selective deployments directly from pre-prepared artifacts, allowing developers to deploy specific components without additional Git operations. This approach improves deployment efficiency by reducing time and minimizing the risk of errors typically associated with manual Git processes. By enabling artifact-based component selection, AutoRABIT streamlines selective deployments, making production releases faster, more reliable, and enhancing the overall release management process. Read the Knowledge Article: [Selective Deployments Using Pre-Prepared Artifacts](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/version-control/change-labels/release-labels/selective-deployments-using-pre-prepared-artifacts) for more information.\
\
Important Note: If you choose just one revision while creating a new Release Label, a notification message asks you to select at least **two revisions**. You can choose the **Single Revision** option directly from the dropdown on the **New Merge** screen to perform a merge using only one revision. This helps avoid the creation of unnecessary release labels.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685441577426.png" alt="" width="375"><figcaption></figcaption></figure>

1. Click **`OK`**. The newly created release label will be displayed on the **`Release Labels Summary`** screen.

\


<figure><img src="../../../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

It's always a good idea to break data into multiple pages when dealing with multiple-label records. You can browse **25**, **50**, **75**, or **100** records on a single page or navigate to the previous or next page using the **`Previous`** and **`Next`** buttons.

The **`Release Labels Summary`** screen has been designed to enhance user experience and displays the following detailed information for each release label created:

1. At the top left is where you can see the **`Repository`** dropdown. You can choose a different repository from the dropdown list.
2. The **release label name**, the **date** and **time** it was last updated, and the **version control branch**.
3. The release label **description**.
4. The release label **package status**: **Completed**, **Failed**, **Package Not Prepared**, **In-progress**, or **Aborted**. Abort an ongoing package preparation using the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707477393.png) icon; the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707557148.png) icon indicates an aborted process, and the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707594532.png)icon indicates the release label package creation is a success.
   * Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707408592.png) icon to view the latest version log.
   * Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707355377.png) icon to download the package.xml file in a .zip format.
5. Click on **`View Dataset`** to view the components in that release label package. You can view the components in **`JSON View`** or **`Tree View`**.

<figure><img src="../../../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

6. Click on the **Merge** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669113759125.png)) to merge the release label to a branch.
7. Click on the **Edit** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669114041351.png)) to update the Release Label information if required. You can also use the **`Search`** box to filter the results based on the label name.
8. Click on the **Delete** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669114143063.png)) to delete a Release Label. This process cannot be undone.
9. Click **`Create Artifact`** to manually create a package that got failed or was not prepared. This option will not be clickable if the package creation has been completed or is in progress. This option will be available for orange and red release labels but not for green.

{% hint style="warning" %}
On the **New Deployment** page, for the **Release Label** dropdown, the new release labels for which the package has been successfully prepared will be shown. The dropdown menu will not show Release labels created before the ARM **22.3** release.&#x20;

To manually prepare the package, use the **Create Artifact** button. The release label will then be available for deployment.
{% endhint %}

