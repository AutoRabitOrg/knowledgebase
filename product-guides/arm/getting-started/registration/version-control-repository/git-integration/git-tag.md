# GIT Tag

### Overview <a href="#overview" id="overview"></a>

GIT tags are a simple and effective way to keep track of your code's different versions and the important quality of Git's version control. GIT Tag operation allows giving meaningful names to a specific version in the repository. Suppose Timon and Rumba decide to tag their project code so they can easily access it later.

### Creating a new Git Tag <a href="#creating-a-new-git-tag" id="creating-a-new-git-tag"></a>

#### A. Create GIT Tag in your Version Control Branch <a href="#a-create-git-tag-in-your-version-control-branch" id="a-create-git-tag-in-your-version-control-branch"></a>

1. Log in to your AutoRABIT account.
2. From the AutoRABIT home page, click ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexGitTagsOperationcustom.png)and go to the **VC Repo's** tab.
3.  Select your [Version Control ](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/)Repository under **Repository List**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515280594.png" alt=""><figcaption></figcaption></figure>
4. Go to the **Tags** tab and click on the **Create** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515323733.png" alt=""><figcaption></figcaption></figure>

5. In the **Create Tag** screen, select the **VC branch** from the drop-down. The branch that was registered with AutoRABIT for your Version Control repository will be populated here.
6. Use the **Search** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(51\).png)) button next to the Revision field to pull a list of revisions from which you can choose which revision to use in the deployment.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515470037.png" alt=""><figcaption></figcaption></figure>

\
**Get Latest HEAD** points out the last commit in the current checkout branch.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515518433.png" alt=""><figcaption></figcaption></figure>

7.  Give a name for the tag and any additional info in the **Message** section. Click **Create**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515574187.png" alt=""><figcaption></figcaption></figure>
8.  A newly created tag will be displayed under the **Tags** section.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515617451.png" alt=""><figcaption></figcaption></figure>

#### B. Create GIT Tag during Merge <a href="#b-create-git-tag-during-merge" id="b-create-git-tag-during-merge"></a>

Once the merge process is completed and pushed to the remote branch, AutoRABIT will create the GIT tag based on your configuration. To do so,

1.  From the top navigation pane, navigate to **Create New > New EZ-Merge.**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515750756.png" alt=""><figcaption></figcaption></figure>
2. On the New Merge screen, select your **GIT Version Control Repository, Base Branch,** and the **Target Branch**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617515931388.png" alt=""><figcaption></figcaption></figure>

3. Scroll a bit below and you can see the option: **Create Git Tag**. Select this checkbox.&#x20;
4.  Give a name for the tag and any additional info in the message box.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617516106138.png" alt=""><figcaption></figcaption></figure>
5. Fill in the remaining fields as per your convenience and click on **Merge/ Validate & Merge**. Once the merge process is completed, the GIT tag gets auto-created.

#### C. Create GIT Tag via CI Job <a href="#c-create-git-tag-via-ci-job" id="c-create-git-tag-via-ci-job"></a>

AutoRABIT will create the GIT tag while CI Job is triggered and is successfully build.

1. Go to the **New CI Job** screen.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617516435168.png" alt=""><figcaption></figcaption></figure>

2. The new CI Job screen gives the job a descriptive name in the **CI Job Name** field.
3. Under **Build**, select your **Version Control Systems,** your **Repository,** and the **Branch**.
4. Go to the **Deploy** section.
5. Under the **Deploy** section, select your Destination org.
6. Select the checkbox: **On Successful Deployment.**
7. Now, select the checkbox: **Run Merge Process.** This allows running the merge operation automatically once the build is triggered successfully in CI Job. For merge to run, you need to select the Version Control type, source and destination branch, merge type, and how you like to resolve the merge conflicts that may arise during the merge process.
8.  Next, select the **'Create GIT Tag'** checkbox and enter any tag message for your reference.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617517431822.png" alt=""><figcaption></figcaption></figure>
9. Fill in other details as per your wish and click **Save**. When the build is triggered successfully and the merge process is run, a tag will be created based on the **Project\_Buildnumber**.

### Deployment via GIT Tag <a href="#deployment-via-git-tag" id="deployment-via-git-tag"></a>

1. In the New Deployment screen, choose **Tag** as a dropdown in the **Deployment From** field.
2. Select the **Version Control Repository** and the **Tag** from the dropdown.
3. Choose the **Destination org** for your deployment.
4. The **Deployment Type** is auto-selected to **Full Deployment** by default. Full Deployment transfers all objects in the source org to the destination org.
5. Once you are done with the selection, click on **Deploy**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617514256063.png" alt=""><figcaption></figcaption></figure>

6. The remaining steps are similar to other deployments methods, do refer to the article: [Create and Deploy Changes](../../../../arm-features/deployment/create-and-deploy-changes-in-autorabit.md)
