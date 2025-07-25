# Selective Deployments Using Pre-Prepared Artifacts

The **External Pull Request Summary** screen displays all pull requests created to date. You can also create a new pull request from this page.

## Viewing the External Pull Request Summary Page <a href="#viewing-the-external-pull-request-summary-page" id="viewing-the-external-pull-request-summary-page"></a>

> For optimal viewing, set your Chrome or Firefox browser zoom to **75%**.

1. Navigate to the **Version Control** module and select **External Pull Requests**.
2. On the **External Pull Requests** screen, choose the **repository** and the **branch** where the pull request was created.
3. The most recent pull request (in **Open** state) will appear at the top, showing added/deprecated objects under the **Commits** tab.

You can display 25, 50, 75, or 100 records per page or use the **Previous** and **Next** buttons to navigate through the list.

## Create a New Pull Request <a href="#create-a-new-pull-request" id="create-a-new-pull-request"></a>

Click the **Create Pull Request** button on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image%20(58)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Create Pull Request button"><figcaption><p>Create Pull Request button</p></figcaption></figure>

Fill out the pop-up form:

<figure><img src="../../../../../.gitbook/assets/image%20(59)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Pull Request creation form" width="406"><figcaption><p>Pull Request creation form</p></figcaption></figure>

1. Select a **repository** (only enabled repositories will be listed).
2. Choose the **Source Branch** and **Target Branch**.
3. Provide a **Title** and a brief **Description**.
4. Add **Reviewers**. (The **Optional Reviewer** field is shown for Azure Cloud-supported PRs.)
5. Check **Delete source branch after Pull Request closure** if applicable.
6. Click **OK**. The pull request will appear at the top of the list.

## View Pull Request Differences <a href="#view-the-pull-request-difference" id="view-the-pull-request-difference"></a>

ARM compares metadata between the source and target branches and generates a visual diff:

* **Red** lines = deletions in the **Source Branch**
* **Green** lines = additions in the **Target Branch**

<figure><img src="../../../../../.gitbook/assets/image%20(60)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Metadata diff view showing additions and deletions"><figcaption><p>Metadata diff view showing additions and deletions</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image%20(61)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Insertions and deletions summary in diff view"><figcaption><p>Insertions and deletions summary in diff view</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image%20(62)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Inline code diff highlighting removed lines"><figcaption><p>Inline code diff highlighting removed lines</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image%20(63)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Code diff showing added lines"><figcaption><p>Code diff showing added lines</p></figcaption></figure>

You can also **view/add/edit comments** at the revision level in the **Commits** tab.

<figure><img src="../../../../../.gitbook/assets/image%20(64)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Comment section for pull request revisions"><figcaption><p>Comment section for pull request revisions</p></figcaption></figure>

> **Important Notes:**
>
> * Inline commenting is supported only for **Bitbucket**-enabled pull requests.
> * Click on individual pull requests to sync and fetch the latest updates.
> * A maximum of **300 files** are displayed per pull request.

## Additional Actions on the Pull Request Page <a href="#additional-actions-on-pull-request-page" id="additional-actions-on-pull-request-page"></a>

<figure><img src="../../../../../.gitbook/assets/image%20(65)%20(1)%20(1)%20(1)%20(1)%20(1).png" alt="Action menu on pull request list"><figcaption><p>Action menu on pull request list</p></figcaption></figure>

### More Operations <a href="#id-1-more-operations" id="id-1-more-operations"></a>

1. **Navigate to Pull Request Page** – Click on the PR label to open it in GitHub or Bitbucket.

<figure><img src="../../../../../.gitbook/assets/image%20(66)%20(1)%20(1)%20(1)%20(1).png" alt="Pull request link to GitHub/Bitbucket" width="563"><figcaption><p>Pull request link to GitHub/Bitbucket</p></figcaption></figure>

2. **Edit Pull Request** – Use the edit icon (!\[Edit icon]\(../../../../../.gitbook/assets/image (67) (1) (1) (1) (1).png)) to modify the PR details.

### Actions for the Pull Request <a href="#id-2-actions-for-the-pull-request" id="id-2-actions-for-the-pull-request"></a>

Reviewers can take the following actions:

1. **Approve** – Submit feedback and approve the changes. Status becomes **Approved**.
2. **Decline** – Reject the pull request.
3. **Merge** – Merge the approved pull request. Status becomes **Merged**.
4. **Reopen** – Reopen a previously closed pull request.
