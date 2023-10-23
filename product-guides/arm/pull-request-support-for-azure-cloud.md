# Pull Request Support for Azure Cloud

Pull requests let your team give feedback on changes in feature branches before merging the code into the master branch. Reviewers can step through the proposed changes, leave comments, and vote to approve or reject the code.

Previously, we had [GitHub](enabling-github-checks.md) and Bitbucket support. We've included support for [Azure DevOps](azure-devops.md) in the ARM 21.6 release.

For each pull request created inside AutoRABIT, you will have a link that will redirect you to the Azure DevOps application externally where you can view the code changes, merge the changes and close the pull request. But, if there are problems with the proposed changes, they can post feedback in the pull request. Follow-up commits will show up right next to the relevant comments.

There is also a provision to approve the pull request within the AutoRABIT application as well.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

1.  **Enable Pull Request** support for users in AutoRABIT.

    * The account owner or admin can assign the required permission to the users by visiting the **Admin > Roles** tab and selecting the **'External Pull Requests'** checkbox under the [**Version Control**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) section



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591633475.png" alt="" width="563"><figcaption></figcaption></figure>
2.  Pull Request support is enabled for the **Azure Cloud plugin**.

    * Make sure the [**Azure Cloud**](azure-cloud-authentication.md) checkbox is selected under the **My Account** > **Plugins** > **Pull Request Support** section.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591403110.png" alt=""><figcaption></figcaption></figure>
3. Users have appropriate **roles** or **permissions** to integrate their repository for pull requests.
   * Such privileges are granted by their account owner or admin. They can assign the required permission to the employees by visiting the **Admin > Roles** tab and selecting the **'Create Pull Request'** checkbox under the **'Special Permissions In Version Control'** section.
4.  The Approver should have the **Pull Request Approver** permission.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591565133.png" alt="" width="563"><figcaption></figcaption></figure>
5.  Your **version control repo** should be eligible for the Azure cloud pull requests.

    1. Go to **VC Repo's** section and look for your repository.
    2. Select the checkbox: **Enable Pull Request Support**
    3. Select **Azure Cloud** as a pull request plugin.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591525783.png" alt=""><figcaption></figcaption></figure>

Click **Save Details**.

### Creating a Pull Request <a href="#creating-a-pull-request" id="creating-a-pull-request"></a>

From the AutoRABIT tool, you can create a new PR from:

* from **External Pull Request** summary page
* during **EZ-Commit**.Point to Note:Currently, creating new PRs while running a new CI Job isn't supported. To date, both GitHub and Bitbucket allows you to create a new PR.

#### 1. Creating a new Pull Request from the External Pull Request Summary page <a href="#1-creating-a-new-pull-request-from-the-external-pull-request-summary-page" id="1-creating-a-new-pull-request-from-the-external-pull-request-summary-page"></a>

The **External Pull Request** screen is best viewed when the zoom setting is set to 80% on your chrome/firefox browser.

1. Go to **Version Control** > **External Pull Requests**.
2.  Click on the **Create Pull Request** button on the right side of the page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628533595697.png" alt=""><figcaption></figcaption></figure>

On the next pop-up screen, furnish the below details:

1. Select your [**version control repository**](arm-features/version-control/introduction-to-version-control/version-control-repositories-summary.md). Only those version control repositories for which the pull request is enabled will be listed under the **Repositories** drop-down.
2. Choose the **Source branch** and the **Destination Branch** to compare.
3. Enter a **Title** and detailed **Description** of your changes, so others can see what problems the changes solve.
4. Add reviewers' details that will accept your pull request. As you enter a name or email address, a list of matching users appears. Select the names to add as **Required reviewer** or **Optional reviewer**.&#x20;
5.  Additional checkbox to **delete the source branch once the pull request has been approved**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591093066.png" alt="" width="375"><figcaption></figcaption></figure>
6. Click **OK**. The newly created pull request will get displayed on top of the list on the **External Pull Request Summary** page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1637591201041.png" alt=""><figcaption></figcaption></figure>

#### 2. Creating a Pull Request during EZ-Commit <a href="#2-creating-a-pull-request-during-ezcommit" id="2-creating-a-pull-request-during-ezcommit"></a>

The **New EZ-Commit** screen is best viewed when the zoom setting is set to 80% on your chrome/firefox browser.

1.  From the top navigation pane, go to **Create New** > **New EZ-Commit**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-TJA6AEBZ.png" alt=""><figcaption></figcaption></figure>
2. On the **EZ-Commit** screen, select the [**Salesforce Org**](arm-administration/registration/salesforce-org/) from which the metadata components will get fetched.
3. Select the Salesforce Org registered **Author**.
4. Select the **Version Control Repository** for which the pull request support is enabled. Select its mapped **branch**.
5. Select the way to fetch the metadata components from the selected Salesforce Org under the **Fetch Changes** section. Choose the one that best fits your needs.
6.  Under **Perform** section, select the option: **Create a Pull Request**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YOHMTRD7.png" alt=""><figcaption></figcaption></figure>
7. Leave the remaining field as default and click on the **Next** button to proceed ahead.
8.  On the next page, select the metadata components and their members to be committed to the Version Control branch. Click **Next**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZC75N9RY.png" alt=""><figcaption></figcaption></figure>
9. On the next screen, you need to do the following:
   * To include your globally selected profiles/ permission sets to the commit, select the checkbox: **Apply Global Profile Permissions**
   * **Apply Search and Substitute Rules**: If you have created the SEARCH and SUBSTITUTE rules to define custom find and substitute rules, AutoRABIT applies whenever you commit and deploy files from one Sandbox to another Sandbox one Sandbox to Version Control or vice-versa, such rule can be found here.
   *   Enter the **Commit Comment**. This is a mandatory step.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-UF86KUNP.png" alt=""><figcaption></figcaption></figure>
10. Under **Create a Pull Request** section, choose where you like to commit i.e., in your base branch, or create a new branch and commit under it.
11. To create a new branch and later commit the changes, enter the new branch name.
12. Give the Pull Request a **Label Name**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-2PNFZ36I.png" alt=""><figcaption></figcaption></figure>
13. Once all the fields are filled in, click on **Finish**. This concludes the creation of a pull request and is ready for review. After you create a pull request, you can ask a specific person to review your proposed changes.
14. Once the commit process is initiated, you will be redirected to the **Commits** screen where you can view the progress of your commit operation initiated.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JGKSQPE1.png" alt=""><figcaption></figcaption></figure>
