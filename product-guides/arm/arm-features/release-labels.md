# Release Labels

### Overview <a href="#overview" id="overview"></a>

A **Release Label** is a combination of multiple commit labels. Creating a release label will allow you to combine a group of single revisions, allowing all the revisions to be deployed in one go. This article will discuss creating a new release label in the ARM application.

**Before you begin:**

1. Confirm you have the **Manage Label** permissions to create a new release label.&#x20;
2. Commit revisions were made to the version control branch to combine them under a single release label. For more information, refer to the article: [Commit Labels](../commit-labels.md)

### Create a new Release Label <a href="#create-a-new-release-label" id="create-a-new-release-label"></a>

1. Log in to your ARM account.
2. Hover your mouse over the [**`Version Control`**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) module and click on the **`Change Labels > Release Labels`** or directly go to the **`Change Labels`** tab and select **`Release Labels`** from the dropdown.The **Release Label** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
3.  Click on **`Create Release Label.`**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1671006223283.png" alt="" width="563"><figcaption></figcaption></figure>
4.  On the next screen, give the release label creation process a **`Label Name`** and a short **`Description`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682583370810.png" alt="" width="563"><figcaption></figcaption></figure>
5. Select the **`Repository`** and the **`Branch`** containing the commit labels.Note:For the version control repository registered in the SFDX structure, you must choose an additional option, i.e., Package Directory. To know more about Package Directory, refer to the article: [Salesforce DX Metadata Format](../salesforce-dx-metadata-format.md)
6. Select the commit **`Label Type`**, i.e., **`Salesforce`** or **`Vlocity`**.Known LimitationsIf a branch-to-branch merge involves multiple commits that include data from Vlocity and Salesforce components, the ARM cannot classify those commits as **Vlocity** or **Salesforce** components.
7.  From the **`No of Days`** dropdown list, you can choose to retrieve the commit history for the previous **30**, **60**, **90**, **120**, **180**, or **365** days, or **ALL** the commits at once. Please note that selecting **ALL** may result in a slight delay in fetching the entire commit history.InfoWith the ARM 22.3 release, you can create a release label and start the artifact preparation immediately by selecting the **`Create package manifest for Deployment`** checkbox for Salesforce labels. If you do not select this checkbox on this screen, you can still click the **`Create Artifact`** button on the **`Release Label Summary`** screen to create and run a package manually.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682584438782.png" alt="" width="563"><figcaption></figcaption></figure>
8. Click **`Fetch Commit History`** to retrieve all the revisions available on your selected repo and branch. If no records appear, then no revisions have been committed to the branch.
9.  Select two or more revisions from the left column to group them into a single release label. The **`Selected Revisions`** are displayed in a second column on the right side to make it easier to see. You can also unselect revisions from this section.\
    Important Note:If you choose just one revision while creating a new Release Label, a notification message asks you to select at least **two revisions**. You can choose the **Single Revision** option directly from the dropdown on the **New Merge** screen to perform a merge using only one revision. This helps in avoiding the creation of needless release labels.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685441577426.png" alt="" width="375"><figcaption></figcaption></figure>
10. Click **`OK`**. The newly created release label will be displayed on the **`Release Labels Summary`** screen.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707172293.png" alt="" width="563"><figcaption></figcaption></figure>

It's always a good idea to break data into multiple pages when dealing with multiple-label records. You can browse **25**, **50**, **75**, or **100** records on a single page or navigate to the previous or next page using the **`Previous`** and **`Next`** buttons.

With the **ARM 22.3** release, the **`Release Labels Summary`** screen has been redesigned to enhance user experience and displays the following detailed information for each release label that is created:

1. At the top-left is where you can see the **`Repository`** drop-down. You can choose a different repository from the dropdown list.
2. The **release label name**, the **date** and **time** it was last updated, and the **version control branch**.
3. The release label **description**.
4. The release label **package status**: **Completed**, **Failed**, **Package Not Prepared**, **In-progress**, or **Aborted**. Abort an ongoing package preparation using the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707477393.png) icon, the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707557148.png) icon indicates an aborted process, and the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707594532.png)icon indicates the release label package creation is a success.
   * Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707408592.png) icon to view the latest version log.
   * Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669707355377.png) icon to download the package.xml file in a .zip format.
5. Click on **`View Dataset`** to view the components in that release label package. You can view the components in **`JSON View`** or **`Tree View`**.

\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669708007625.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669708019273.png" alt=""><figcaption></figcaption></figure>

1. Click on the **Merge** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669113759125.png)) to merge the release label to a branch.
2. Click on the **Edit** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669114041351.png)) to update the Release Label information if required. You can also use the **`Search`** box to filter the results based on the label name.
3. Click on the **Delete** icon (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669114143063.png)) to delete a Release Label. This process cannot be undone.
4. Click **`Create Artifact`** to manually create a package that got failed or was not prepared. This option will not be clickable if the package creation has been completed or is in progress. This option will be available for orange and red release labels but not for green.

Important Note

On the **New Deployment** page, for the **Release Label** dropdown, the new release labels for which the package has been successfully prepared will be shown. The dropdown menu will not show Release labels created before the ARM **22.3** release.&#x20;

To manually prepare the package, use the **Create Artifact** button. The release label will then be available for deployment.
