# External Pull Request Summary Page

The **External Pull Request Summary** screen displays the list of pull requests created to date. Also, you have a provision to create a new pull request on this page.

## Viewing the External Pull Request Summary Page <a href="#viewing-the-external-pull-request-summary-page" id="viewing-the-external-pull-request-summary-page"></a>

The **External Pull Request** screen is best viewed when the zoom setting is **75%** on your Chrome/Firefox browser.

1. Hover your mouse over the **Version Control** module and choose **External Pull Requests.**
2. On the **External Pull Requests** screen, choose your **repository** and the **branch** on which the pull request was initiated.
3. Your new pull request initiated will be displayed on the top with **Open** state, including the list of added/ depreciated objects detail under the **Commits** tab.

It's always a good idea to break data into multiple pages when dealing with multiple pull request records. You can browse 25, 50, 75, or 100 records on a single page or navigate to the previous or next page using the **Previous** and **Next** buttons.

## Create a new Pull Request. <a href="#create-a-new-pull-request" id="create-a-new-pull-request"></a>

To create a new pull request, use the **Create Pull Request** button on the right side of the screen.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682074039069.png" alt=""><figcaption></figcaption></figure>

On the next pop-up screen, furnish the below details:\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682074115729.png" alt=""><figcaption></figcaption></figure>

1. Select your version control repository. Only those version control repositories for which the pull request is enabled will be listed under the **Repositories** drop-down.
2. Choose the **Source Branch** and the **Target Branch** from the respective dropdowns.
3. Give the pull request operation a **Title** and a brief **Description**.
4. **Add Reviewers** that will accept your pull request. The **Optional Reviewer** field will be displayed for repositories with Azure Cloud PRs supports.
5. Select the **Delete source branch after Pull Request closure** to delete the branch once the pull request has been approved.
6. Click **OK** to create a new pull request. The newly created pull request will get displayed on top of the list on the **External Pull Request Summary** page.

## View the Pull Request difference. <a href="#view-the-pull-request-difference" id="view-the-pull-request-difference"></a>

ARM compares the metadata between the **Source and Target branches** and generates a metadata difference report. Such information can be viewed on the **Diff** screen. This screen will display the number of insertions and deletions to each metadata file. The lines highlighted in **RED** color indicate those that are deleted in the **Source Branch,** and for **GREEN** color indicates those that are newly added in the **Target Branch**.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628533785612.png)

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1627806364594.png" alt=""><figcaption><p>Diff UI for GitHub Pull Request </p></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1627806699705.png" alt=""><figcaption><p>Diff UI for Bitbucket Pull Request (provision to add/edit/reply comment for each line)</p></figcaption></figure>

![For the Bitbucket repo-enabled pull request, you can add/ edit/ reply to comments for each line of the code.](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1627807138273.png)

Similarly, you can **view/add/edit comments** on the revision level (revisions under **Commit** sections).

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1614025855307.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}


Important Note:

1. AutoRABIT supports inline add, edit, and reply comments for **Bitbucket-enabled pull requests** only. This feature is currently not supported by **GitHub**.
2. AutoRABIT synchronizes the pull requests to access the latest updates from the repository when clicked. Therefore, to show the latest changes, comments, or any updates, it is recommended to click on the individual pull request.
3. The response includes a maximum of **300** files.
{% endhint %}

## Additional Actions on the Pull Request Page <a href="#additional-actions-on-pull-request-page" id="additional-actions-on-pull-request-page"></a>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1627807564908.png)

### 1. More Operations <a href="#1-more-operations" id="1-more-operations"></a>

1.  **Navigate to Pull Request Page:** Clicking on the Pull Request label will take you to your _GitHub/Bitbucket_ Pull Request page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1614026509580.png" alt=""><figcaption></figcaption></figure>
2. **Edit Pull Request:** Modify the pull request information using the **Edit** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1627807634837.png)) button.

### 2. Actions for the Pull request <a href="#2-actions-for-the-pull-request" id="2-actions-for-the-pull-request"></a>

After you create a pull request, you can ask a specific person to review your proposed changes. A reviewer has four possible statuses:

* **Approve:** Submit feedback and approve merging the changes proposed in the pull request. Once the pull request is approved, the status changes to **"Approved"**.
* **Decline:** Reject the pull request
* **Merge:** Merge the changes proposed in the pull request. Once the pull request is approved, the status changes to **"Merged"**.
* **Reopen:** Reopen the closed pull request again.
