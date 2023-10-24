# External Pull Request

### About External Pull Request <a href="#about-external-pull-request" id="about-external-pull-request"></a>

Create a pull request to propose and collaborate on changes to a repository. These changes are proposed in a branch, which ensures that the master branch only contains finished and approved work.

You can specify which branch you'd like to merge your changes into when you create your pull request. Pull requests can only be opened between two branches that are different.

### External Pull Request vs Merge Request <a href="#external-pull-request-vs-merge-request" id="external-pull-request-vs-merge-request"></a>

**Merge Request** and **Pull Request** are equivalent. Both are means of pulling changes from another branch or fork into your branch and merging the changes with your existing code.

#### Merge Request  <a href="#merge-request" id="merge-request"></a>

Merge Request is essentially a **request** to merge one branch into another. With Merge Request, AutoRABIT allows you (the reviewer) to go through the suggested changes. From here, you can choose to apply them or add comments to make further changes to the code. It is particularly useful as it helps merge code from different branches and make sure the code that gets deployed to production is bug-free.

An internal pull request is the same thing as a merge request.

**Ex:** For instance, one of your developers has just finished working on a feature in a dedicated branch. Now, this feature should be merged with the development branch. But first, other team members should review it.

So, your developer creates a merge request, chooses the feature branch as _Source_ and the development branch as _Destination._ The developer can add the title and the description of the merge request and choose who will be the _Reviewers_ of it.

The reviewer can:

* see what files have been edited, what commits have been made
* add comments to the whole merge request or a particular code line and discuss it
* decline a pull request
* merge a pull request

Note:Only AutoRABIT users can be added as merge request reviewers.

#### External Pull Request <a href="#external-pull-request" id="external-pull-request"></a>

AutoRABIT allows you to create a **new pull request** to pull changes from another branch. For each pull request created inside AutoRABIT, you will have a link that will redirect you to GitHub/Bitbucket application externally where you can view the code changes, merge the changes and close the pull request. But, if there are problems with the proposed changes, they can post feedback in the pull request. Follow-up commits will show up right next to the relevant comments.

There is also a provision to approve the pull request within the AutoRABIT application as well.

Important Note:AutoRABIT users with the pull request reviewer option enabled and a reviewer role in version control (Github/Bitbucket/Azure Cloud) can be added as external pull request reviewers.

### Before You proceed for External Pull Request <a href="#before-you-proceed-for-external-pull-request" id="before-you-proceed-for-external-pull-request"></a>

1. **Enable Pull Request** support for users in AutoRABIT. The account owner or admin must perform this function.
2. Users have appropriate **roles** or **permissions** to integrate their Version Control Repository for pull requests. Such privileges are granted by their account owner or admin. They can assign the required permission to the employees by visiting the **Admin > Roles** tab and selecting the **'Create Pull Request'** checkbox under the **'Special Permissions In** [**Version Control**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/)**'** section.
3.  The Approver should have the **Pull Request Approver** permission.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617526294656.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Users are allowed to access the **'External Pull Requests'** page. The account owner or admin can assign the required permission to the users by visiting the **Admin > Roles** tab and selecting the **'External Pull Requests'** checkbox under the **Version Control** section.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617526367326.png" alt="" width="563"><figcaption></figcaption></figure>

### Enable Pull Request Support <a href="#enable-pull-request-support" id="enable-pull-request-support"></a>

1. Go to the **My Account** page.
2.  Under **Plugins**, select the hosting service to manage your repositories. AutoRABIT currently supports both GitHub/Bitbucket (cloud and server) and Azure Cloud in raising a pull request.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1645675496677.png" alt=""><figcaption></figcaption></figure>
3. Click **Save**.
4. Next, go to the **Version Control Repository** page.
5. On this page, select your [**Version Control Repository**](../) from which you like to enable the pull request support.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617526688904.png" alt=""><figcaption></figcaption></figure>

6. On the right side of the screen, select the checkbox: **Enable Pull Request Support**
7. Next, select the pull request plugins enabled for your account. For more details, please contact your administrator.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617526858128.png" alt=""><figcaption></figcaption></figure>

Copy the auto-generated URL (applicable only for _Github cloud and enterprise service_) and create a webhook push event for pull requests in your repository. This integration can be used to trigger CI jobs while creating a pull request.

8. Click **Save Details** to save the Pull Request configuration.

### Creating an External Pull Request <a href="#creating-an-external-pull-request" id="creating-an-external-pull-request"></a>

Pull requests are a mechanism for a developer to notify team members that they have completed a feature. Once their feature branch is ready, the developer files a pull request via their account. This lets everybody involved know that they need to review the code and merge it into the master branch.

#### How it works <a href="#how-it-works" id="how-it-works"></a>

1. A developer creates the feature in a dedicated branch in their local repository.
2. The developer pushes the branch to a public Version Control repository via AutoRABIT.
3. The developer files a pull request via AutoRABIT.
4. The rest of the team reviews the code, discusses it, and alters it.
5. The approved Merger merges the feature into the official repository and closes the pull request.

#### Creating a Pull Request <a href="#creating-a-pull-request" id="creating-a-pull-request"></a>

**During EZ-Commit**

1.  From the top navigation pane, go to **Create New > New EZ-Commit**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617527510055.png" alt=""><figcaption></figcaption></figure>
2. On the EZ-Commit screen, select the [**Salesforce Org**](https://knowledgebase.autorabit.com/docs/salesforce-org) from which the metadata components will get fetched. Select the Salesforce Org registered **Author**.
3. Select the **Version Control Repository** for which the pull request support is enabled. Select its mapped branch.
4. Select the way to fetch the metadata components from the selected Salesforce Org under the **Fetch Changes** section. Choose the one that best fits your needs.
5.  Under **Perform** section, select the option: **Create a Pull Request**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628532642058.png" alt=""><figcaption></figcaption></figure>
6. Leave the remaining field as default and click on the **Next** button to proceed ahead.
7. On the next page, select the metadata components and their members to be committed to the Version Control branch. Click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628532790669.png" alt=""><figcaption></figcaption></figure>

1. On the next screen, you need to do the following:
   1. To include your globally selected profiles/ permissionsets to the commit, select the checkbox: **Apply Global Profile Permissions**
   2. **Apply Search and Substitute Rules:** If you have created the SEARCH and SUBSTITUTE rules to define custom find and substitute rules, AutoRABIT applies whenever you commit and deploy files from one Sandbox to another Sandbox one Sandbox to Version Control or vice-versa, such rule can be found here.
   3.  Enter the **Commit Comment**. This is a mandatory step.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628532916172.png" alt=""><figcaption></figcaption></figure>
2. Under **Create a Pull Request** section, choose where you like to commit i.e., in your base branch, or create a new branch and commit under it.
3. To create a new branch and later commit the changes, enter the new branch name.
4. Give the Pull Request a **Label Name**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628533006752.png" alt="" width="563"><figcaption></figcaption></figure>

5. Once all the fields are filled in, click on **Finish**. This concludes the creation of a pull request and is ready for review. After you create a pull request, you can ask a specific person to review your proposed changes.
6.  Once the commit process is initiated, you will be redirected to the **Commits** screen where you can view the progress of your commit operation initiated.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628533121338.png" alt=""><figcaption></figcaption></figure>

#### Creating Pull Request during CI Job <a href="#creating-pull-request-during-ci-job" id="creating-pull-request-during-ci-job"></a>

Now since you have enabled pull requests for your Version Control Repository, you can trigger CI Job via AutoRABIT using the pull request webhook.&#x20;

The CI Job will get triggered for the newly created pull requests and are in the **OPEN** state.

1. Go to **Create New > New CI Job**.
2.  On the next screen, select one of the below criteria for running the CI Job:

    * _Package from Version Control_&#x20;
    * _Deploy from Version Control_
    * _Deploy SFDX source from Version Control_



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617528784541.png" alt=""><figcaption></figcaption></figure>
3. Go to the **Build** section.
4. Select the **Version Control Repository** for which the pull request is enabled. Then, select the **Branch**.
5. Now, select the **Pull Request** checkbox. You can see that some of the options have been withdrawn automatically, for example, Incremental Build, Trigger Build on Commit, or Map ALM Project. This is because such options are not supported when raising requests via pull webhook.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617528995514.png" alt=""><figcaption></figcaption></figure>

1. Pull Request facilitation is provided for both GitHub and Bitbucket (cloud and enterprise) services.
2. When Pull Request is validated via CI job, the **'Validate Only'** option (under **Deploy** section) will be in the selected mode. The user won't be able to deselect it.
3. Choose the remaining fields that best fit your needs and click **Save**.
4. &#x20;Go to the **'External Pull Requests'** page, where you can find the CI Job details that were triggered via webhook pull request. Upon successful Build/Deploy, comments get updated to the pull request. The revisions associated with the pull request will be packaged. These changes will be validated and the results will get updated back to the pull request as a comment.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628533207029.png" alt=""><figcaption></figcaption></figure>
