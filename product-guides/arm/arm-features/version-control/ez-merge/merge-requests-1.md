---
hidden: true
---

# (DRAFT) Merge Requests

### Merge Request- Overview <a href="#merge-request-overview" id="merge-request-overview"></a>

A merge request is essentially a request to merge one branch into another.

The branch you added your changes into is called the **source branch** while the branch you request to merge your changes into is called the **target branch**. The target branch can be the default or any other branch, depending on the branching strategies you choose.

As a Salesforce developer, you can collaborate on proposed changes to source code using merge requests. Once you are ready to merge your changes to the target branch, you can raise a merge request to do the following:

1. Provide visibility on changed files in your commits that you are introducing to the source code.
2. Visualize, review, and comment on these potential changes with other members of your team.
3. Set up CI jobs to execute and report Apex test results, SAST (Static Application Security Testing) test results, and Functional test results on your source branch for every check-in.&#x20;
4. Add follow-up commits before your changes are merged to the base branch.
5. In case of a conflict, you can use our IDE-powered conflict editor to resolve them and merge your changes.

### How to create a merge request  <a href="#how-to-create-a-merge-request" id="how-to-create-a-merge-request"></a>

To initiate a new merge request, go to the [**Version Control**](https://www.autorabit.com/8-benefits-of-version-control-in-salesforce-development/) module and click on the **New Merge Requests** call-to-action button.

The **Merge Request History** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.

<figure><img src="../../../../../.gitbook/assets/image (56) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

1. On the **New Merge Request** page, choose the **source repository** and **branch** that contain your changes, and the **target branch** where you want to merge the changes.
2. Click on **Compare Branches and Continue**.

<figure><img src="../../../../../.gitbook/assets/image (57) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, give the merge request a **name** and a short **description** (if required).
4. Enter the **assignee** username. You can assign the merge request to yourself by clicking on the _assign to yourself_ link. The assignee will be notified by email about the created merge request.
5. In the **Approver** field, enter the user email address from whom you want to request a review. It is also possible to assign multiple approvers to review your merge request.&#x20;
6. Enable the **"Delete Source Branch when Merge Request is closed"** option to keep your repository clean. By doing this, the source branch will be automatically deleted right after the merge request is accepted. This is optional.
7. **Squash and Merge**: Sometimes, when merging a long list of changes from a development branch into the master, it’s useful to squash those commits into one change for ease of review and to declutter the repo’s commit history. AutoRABIT now offers the option to squash all of the commits in a merge request into one commit after the merge is approved and completed. **(**[**Learn More**](squash-and-merge.md)**)**

<figure><img src="../../../../../.gitbook/assets/image (58) (1) (1) (1) (1) (1) (1).png" alt="" width="561"><figcaption></figcaption></figure>

8. In the **ALM DETAILS** section, you will have the list of the Jira IDs with the current status and the expected status after a successful merge.For no ALM configured, you will have the message popup stating **"No ALM details found."**

<figure><img src="../../../../../.gitbook/assets/image (59) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

9. Click on **Create Merge Request.**

### Running a merge request during CI Job <a href="#running-a-merge-request-during-ci-job" id="running-a-merge-request-during-ci-job"></a>

While triggering a new CI job, you can run a merge request on your GitHub version control repository. To do so, select the **Merge Request** checkbox for your repo under the **Build** section.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (60) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Whenever the job runs, [AutoRABIT](https://www.autorabit.com/) will run a merge request on the target branch, and the details can be found on the **Merge Request History** page.

### Email Notifications <a href="#email-notifications" id="email-notifications"></a>

When the assignee initiates a new merge request, an email notification is sent to the assignee's email address. The approvers, on the other hand, are responsible for analyzing and approving or rejecting merge requests, and they will be notified through email whenever one arrives. The assignee and the relevant approvers will also be notified via email anytime there is an update or addition of comments to the merge requests.

**Sample email attached:**

<figure><img src="../../../../../.gitbook/assets/image (61) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Merge Request History <a href="#merge-request-history" id="merge-request-history"></a>

The merge request screen displays the list of merge requests created to date along with their current statuses.&#x20;

It's a good idea to break data into multiple pages when dealing with multiple merge request records. You can browse 25, 50, 75, or 100 records on a single page, or you can navigate to the previous or next page using the **Previous** and **Next** buttons.

<figure><img src="../../../../../.gitbook/assets/image (62) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. Under the **Detail View**, you can find detailed information for the initiated merge request.

<figure><img src="../../../../../.gitbook/assets/image (63) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. The status will be shown as **Open** for the merge request in the open state, or, **Merge Conflict** for any merging conflicts, which you need to resolve before merging the changes to the target branch. The status normally appears as **Commit** for no conflicts.

<figure><img src="../../../../../.gitbook/assets/image (64) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3.  The merge request log details, together with the metadata changes report, commits, and the comments can be viewed here.&#x20;

    * **Log**: Contains the detailed history of the check-in performed.

    <figure><img src="../../../../../.gitbook/assets/image (65) (1) (1) (1) (1) (1) (1).png" alt="" width="497"><figcaption></figcaption></figure>

    * **Log Statuses:** For each operation performed in the commit phase, the log report will be available. A (![](<../../../../../.gitbook/assets/image (66) (1) (1) (1) (1) (1).png>)) mark against each log segment shows the completion of the operation; you will have (![](<../../../../../.gitbook/assets/image (67) (1) (1) (1) (1) (1).png>)) and (![](<../../../../../.gitbook/assets/image (68) (1) (1) (1) (1) (1).png>)) icons, respectively present against each log segment for a failed or a partially successful operation.
    * **Files Changed**: This tab displays the number of insertions and deletions to each metadata file. The lines highlighted in **RED** color indicate those are updated (added/deleted/modified) in the source branch and in **GREEN** color indicate those are updated (added/deleted/modified) in the destination branch. The highlighted lines are the modified lines.

    <figure><img src="../../../../../.gitbook/assets/image (69) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**nCino Changes Limitation:** In the **File View**, nCino-related metadata and data components will show the differences, but the **Path View** will be empty.
{% endhint %}

4. **ALM Details:** This section displays the ALM status for your configured work items.

<figure><img src="../../../../../.gitbook/assets/image (70) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. **Commits**: If there are already commits on the branch, those will be listed in this tab.

<figure><img src="../../../../../.gitbook/assets/image (71) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. **Comments**: In the comments tab, add your suggestions or other information required. You can edit your own comments at any time, reply to a comment or delete it. Replying to a comment creates another comment.

<figure><img src="../../../../../.gitbook/assets/image (72) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. **CI Info**: This tab details when you have enabled pull requests while creating a CI job. Along with your CI job details, you can also find the SCA report in detail (PMD).

<figure><img src="../../../../../.gitbook/assets/image (73) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Reviewing the Merge Request <a href="#reviewing-the-merge-request" id="reviewing-the-merge-request"></a>

After you create a merge request, you can ask a specific person to review your proposed changes. A reviewer has three possible statuses:

* **Comment**: Submit general feedback without explicitly approving the changes or requesting additional changes. Such comments will be updated under the **Comments** tab.
* **Request changes**: Submit feedback that must be addressed before the merge request can be merged.
* **Commit:** Submit feedback and approve merging the changes proposed in the merge request. Once the merge request is approved, you can proceed with the **Commit**.

### Filtering Merge Requests <a href="#filtering-merge-requests" id="filtering-merge-requests"></a>

1. **Filtering merge requests by “repository”**: To filter merge requests by repository, you can select your source repository from the dropdown.

<figure><img src="../../../../../.gitbook/assets/image (74) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. **Filtering merge requests by “status”:** You can search through **Open**, **Closed**, **All** issues, or **Opened** issues assigned to you directly from the **Filter By** dropdown for your selected source repository.

<figure><img src="../../../../../.gitbook/assets/image (75) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. **Filtering merge requests by “title”**: You can filter merge requests by specific terms included in titles.

<figure><img src="../../../../../.gitbook/assets/image (76) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4.  **Advanced Filters:**

    * **Filtering merge requests by “branch”**: Filters merge requests by source/target branch.
    * **Filtering merge requests by “author”**: To filter merge requests by a particular user, you can select the user from the **Author** dropdown.
    * **Filtering merge requests by “date range”:** You can select a date range to show only the merge requests contained during that time frame.

    <figure><img src="../../../../../.gitbook/assets/image (77) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (78) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Frequently Asked Questions <a href="#why-is-arm-rejecting-my-merge-request-at-the-final-step" id="why-is-arm-rejecting-my-merge-request-at-the-final-step"></a>

### Why is ARM rejecting my merge request at the final step? <a href="#why-is-arm-rejecting-my-merge-request-at-the-final-step" id="why-is-arm-rejecting-my-merge-request-at-the-final-step"></a>

This occurs when merge criteria do not match the ARM settings. Before submitting the merge request, configure it in ARM to match your needs. Make the appropriate modifications under **Admin > Merge Settings**.
