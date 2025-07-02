# External Pull Request Summary Page

The **External Pull Request Summary** screen displays all pull requests created to date. You can also create a new pull request from this page.

## Viewing the External Pull Request Summary Page <a href="#viewing-the-external-pull-request-summary-page" id="viewing-the-external-pull-request-summary-page"></a>

> For optimal viewing, set your Chrome or Firefox browser zoom to **75%**.

1. Navigate to the **Version Control** module and select **External Pull Requests**.
2. On the **External Pull Requests** screen, choose your **repository** and the **branch** where the pull request was created.
3. The most recent pull request (in **Open** state) will appear at the top, showing added/deprecated objects under the **Commits** tab.

You can choose to display 25, 50, 75, or 100 records per page or use **Previous** and **Next** to browse through records.

## Create a New Pull Request <a href="#create-a-new-pull-request" id="create-a-new-pull-request"></a>

Click the **Create Pull Request** button on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (58) (1) (1) (1) (1) (1).png" alt="Create Pull Request button"><figcaption><p>Create Pull Request button</p></figcaption></figure>

Complete the form on the pop-up screen:

<figure><img src="../../../../../.gitbook/assets/image (59) (1) (1) (1) (1) (1).png" alt="Pull Request creation form" width="406"><figcaption><p>Pull Request creation form</p></figcaption></figure>

1. Select a **repository** (only enabled ones are listed).
2. Choose the **Source Branch** and **Target Branch**.
3. Enter a **Title** and a **Description**.
4. Add **Reviewers** (Optional Reviewers field appears for Azure-supported PRs).
5. Enable **Delete source branch after Pull Request closure** if needed.
6. Click **OK** to create the pull request. It will appear at the top of the list.

## View Pull Request Differences <a href="#view-the-pull-request-difference" id="view-the-pull-request-difference"></a>

ARM compares metadata between source and target branches and generates a difference report. This is viewable on the **Diff** screen:

* **Red** lines = deletions in the **Source Branch**
* **Green** lines = additions in the **Target Branch**

<figure><img src="../../../../../.gitbook/assets/image (60) (1) (1) (1) (1) (1).png" alt="Metadata diff view showing additions and deletions"><figcaption><p>Metadata diff view showing additions and deletions</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (61) (1) (1) (1) (1) (1).png" alt="Insertions and deletions summary in diff view"><figcaption><p>Insertions and deletions summary in diff view</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (62) (1) (1) (1) (1) (1).png" alt="Inline code diff highlighting removed lines"><figcaption><p>Inline code diff highlighting removed lines</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (63) (1) (1) (1) (1) (1).png" alt="Code diff showing added lines"><figcaption><p>Code diff showing added lines</p></figcaption></figure>

You can also **view/add/edit comments** at the revision level in the **Commits** section.

<figure><img src="../../../../../.gitbook/assets/image (64) (1) (1) (1) (1) (1).png" alt="Comment section for pull request revisions"><figcaption><p>Comment section for pull request revisions</p></figcaption></figure>

> **Important Notes:**
>
> * Inline commenting is supported only for **Bitbucket**-enabled pull requests.
> * Click on individual pull requests to synchronize and fetch the latest updates.
> * A maximum of **300 files** are included in the response.

## Additional Actions on the Pull Request Page <a href="#additional-actions-on-pull-request-page" id="additional-actions-on-pull-request-page"></a>

<figure><img src="../../../../../.gitbook/assets/image (65) (1) (1) (1) (1) (1).png" alt="Action menu on pull request list"><figcaption><p>Action menu on pull request list</p></figcaption></figure>

### More Operations <a href="#id-1-more-operations" id="id-1-more-operations"></a>

1. **Navigate to Pull Request Page** – Click on the pull request label to open it on GitHub or Bitbucket.

<figure><img src="../../../../../.gitbook/assets/image (66) (1) (1) (1) (1).png" alt="Pull request link to GitHub/Bitbucket" width="563"><figcaption><p>Pull request link to GitHub/Bitbucket</p></figcaption></figure>

2. **Edit Pull Request** – Click the edit icon (!\[Edit icon]\(../../../../../.gitbook/assets/image (67) (1) (1) (1) (1).png)) to update PR details.

### Actions for the Pull Request <a href="#id-2-actions-for-the-pull-request" id="id-2-actions-for-the-pull-request"></a>

Reviewers can take the following actions:

1. **Approve** – Submit feedback and approve the PR. Status updates to **Approved**.
2. **Decline** – Reject the PR.
3. **Merge** – Accept and merge the PR. Status changes to **Merged**.
4. **Reopen** – Reopen a closed PR if needed.
