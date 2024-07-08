# Commits Summary

### Commits Summary <a href="#commits-summary" id="commits-summary"></a>

In ARM, you can see descriptions of every commit or merge, including a diff in the commit/merge modifications implemented. Commits are segregated based on the date the commit was committed in ARM. By default, only commits by the logged-in user are listed, seen in reverse chronological order—that is, the most recent commits are shown first.

1. Navigate to **`Version Control > Commits`** to view the **`Commits`** screen.
2. The **Commit Summary** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
3. To see all your teammates' commits, turn **`Created By Me`** toggle bar to the left, and all the commits will be shown there. Or, you can filter by commits for which the reviewer approval is pending by moving the **`Pending Approvals`** toggle bar to the right.
4. It's also possible to **`search`** for commits based on the content. You can enter the commit label, revision number, or comment in the search field to filter the exact commit.
5. Content search is case-sensitive.

<figure><img src="../../../../../.gitbook/assets/image (1061).png" alt=""><figcaption></figcaption></figure>

6. Each commit shows:
   * Commit identification initials:
     1. Prevalidation commit (PV)
     2. EZ-Commit (EZ)
     3. Merge Commit (M)
     4. Validate and Merge (VM)
     5. Branching Baseline (BB)
     6. Revert Commit (RC)
     7. Commit initiated from CI job (CI)
     8. Dry Run (DR)
     9. External Commit (EC)
   * The commit label name
   * The commit message
   * The committer's username
   * The date the commit was created
   * [Version Control](../) Repository, Destination, and Source Branch details
   * Salesforce Org details (applicable only to prevalidated commits and EZ-Commits)
   * Commit Revision label
   * Commit/Merge status

### About Quick Merge <a href="#about-quick-merge" id="about-quick-merge"></a>

Quick Merge lets you merge your changes to a Version Control branch directly from the Commits screen.

Suppose you’ve committed your changes to a child branch and are now ready to merge them into your master branch. To do that, you can hover the mouse over the three dots at the right side of the screen and click on **`Quick Merge`** to quickly merge the changes into your master branch, rather than navigating to the **`New Merge`** screen and configuring the steps again.

<figure><img src="../../../../../.gitbook/assets/image (1062).png" alt=""><figcaption></figcaption></figure>

A pop-up will ask for your permission to proceed with the **`Quick Merge`** operation.

<figure><img src="../../../../../.gitbook/assets/image (1063).png" alt="" width="467"><figcaption></figcaption></figure>

Quick Merge is not applicable to:

1. Prevalidation Merge commits with approval as pending
2. Commits that have already been merged

### Commits Detailed View <a href="#commits-detailed-view" id="commits-detailed-view"></a>

You can view the detailed commit report by hovering the mouse over the three dots at the right side of the screen and clicking on **`Detailed View`**.

<figure><img src="../../../../../.gitbook/assets/image (1064).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** The detailed view for prevalidated commits or merges can be seen by clicking the three dots beside the Commit label name.

![](<../../../../../.gitbook/assets/image (1065).png>)
{% endhint %}

For failed commit/merge prevalidation, the red dot symbol next to the three dots for the commit labels easily distinguish them from the rest of the commits list.

<figure><img src="../../../../../.gitbook/assets/image (1066).png" alt="" width="563"><figcaption></figcaption></figure>

The detailed report covering commit type, commit label, comment, source org, repo/branch, reviewer details, etc., is displayed at the top of the page. In short, the features chosen during merge/EZ-Commit are seen here.

<figure><img src="../../../../../.gitbook/assets/image (1067).png" alt=""><figcaption></figcaption></figure>

Clicking on the drop-down icon will display in-depth features chosen during the Merge/EZ-Commit process.

<figure><img src="../../../../../.gitbook/assets/image (1068).png" alt=""><figcaption></figcaption></figure>

The **`Pull Request`** element will display only for the EZ-commit process (not for Merge or Prevalidation merge).

<figure><img src="../../../../../.gitbook/assets/image (1069).png" alt=""><figcaption></figcaption></figure>

You can even view the step-by-step process for your commits to complete.

<figure><img src="../../../../../.gitbook/assets/image (1070).png" alt=""><figcaption></figcaption></figure>

You can view any reviewer comments under the **`Reviewer Comments`** section.

<figure><img src="../../../../../.gitbook/assets/image (1071).png" alt=""><figcaption></figcaption></figure>

The commit log details, ALM details, code analysis report, metadata changes report, and deployment validation report can be viewed here.

<figure><img src="../../../../../.gitbook/assets/image (1072).png" alt=""><figcaption></figcaption></figure>

1.  **`Log:`** Contains the detailed history of the check-in performed. You can also download and save the log report to your local machine.\
    Important Notes:

    * For each operation performed in the commit phase, the log report will be available. A (![](<../../../../../.gitbook/assets/image (1073).png>)) mark against each log segment shows the completion of the operation; you will have (![](<../../../../../.gitbook/assets/image (1074).png>)) and (![](<../../../../../.gitbook/assets/image (1075).png>)) icons, present with each log segment for failed and partially successful operation, respectively.
    * For Commits created by **Auto Backup CI Jobs**, the log file information is unavailable in this section. Instead, all the log information is available in the **CI Job Build Log**.

    <figure><img src="../../../../../.gitbook/assets/image (1076).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (1077).png" alt=""><figcaption></figcaption></figure>
2. **`Deployment Validation:`** For Commit/Merge prevalidation, ARM performs a check-only deployment to your destination branch. Nothing is deployed to your destination branch. However, if anything goes wrong—for example, the deployment fails or tests don’t pass—we’ll show you exactly what happened so that you can fix it.

<figure><img src="../../../../../.gitbook/assets/image (1078).png" alt=""><figcaption></figcaption></figure>

3. **`Code Analysis File:`** Static Code Analysis is usually performed as part of a Code Review and is carried out at the Implementation phase of a Security Development Lifecycle (SDL). Static Analysis tools such as ApexPMD, Checkmarx, Salesforce Scanner, and CodeScan, continuously detect and report on dataflow problems, software defects, language implementation errors, inconsistencies, dangerous usage, coding standard violations, and security vulnerabilities.\
   The SCA provides information for the selected report. This report has info about the files reviewed and related violations that occurred. Click on each file to view related violations that appear at the bottom right of the page. If you click on any violation, it will take you to the respective line (in the black screen on the right side) where the violation occurred.\
   **Download the Report:** Get the report in XLSX format on your local machine using the **`Download Report`** button.

<figure><img src="../../../../../.gitbook/assets/image (1079).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** For **CodeScan** SCA, if the commit is pending review or rejected manually by the approver, click on **`View Scanner Analysis Report`** to view the SCA report on the CodeScan dashboard. If the commit is auto-rejected, then this button is not available.
{% endhint %}

4.  **`Files Changed:`** ARM compares the metadata between the _base branch_ and the _destination branch_ (for a merge) and _source Salesforce org_ with the _destination branch_ (for an EZ-Commit operation) and generates a metadata difference report and log detail. This information can be viewed in this tab. The tab displays each metadata file's number of insertions and deletions. The lines highlighted in **RED** color indicate those that are modified (added/updated/deleted) in the source Salesforce org/branch and the lines in **GREEN** color indicate those that are modified (added/updated/deleted) in the destination branch. The modified lines are the highlighted lines.

    <figure><img src="../../../../../.gitbook/assets/image (1080).png" alt=""><figcaption></figcaption></figure>

    *   Expanding each component allows you to view the inline comparison between the source and the destination files

        1. inline comments are allowed for each file
        2. modified lines are the highlighted ones
        3. download individual metadata file changes report using the download icon.

        <figure><img src="../../../../../.gitbook/assets/image (1082).png" alt=""><figcaption></figcaption></figure>


5. **`ALM Details:`** View the ALM configured during your commit/merge operation.

<figure><img src="../../../../../.gitbook/assets/image (1083).png" alt=""><figcaption></figcaption></figure>

6. **`Comments`**: Add/edit/reply to comments for each commit process on this tab.

<figure><img src="../../../../../.gitbook/assets/image (1084).png" alt=""><figcaption></figcaption></figure>

### Commit Status <a href="#commit-status" id="commit-status"></a>

1. **`Completed:`** This indicates the commit/merge was successful with no conflicts. View the revision detail for each completed commit/merge.

<figure><img src="../../../../../.gitbook/assets/image (1085).png" alt=""><figcaption></figcaption></figure>

2. **`Failed:`** The commit operation failed. Here, you can re-push the failed commits after the changes are updated (for the prevalidation commit) or view the detailed report for the commit to fail (for validation and merge).

<figure><img src="../../../../../.gitbook/assets/image (1086).png" alt=""><figcaption></figcaption></figure>

3. **`Merge Conflicts:`** Sometimes you get merge conflicts when merging or pulling from a branch. A Merge Report gives you a detailed report of the conflicting files during a merge. In this scenario, you need to resolve the merge conflicts to move forward. To do so, click on **`Resolve Conflict`**.

<figure><img src="../../../../../.gitbook/assets/image (1087).png" alt=""><figcaption></figcaption></figure>

4. **`Auto Rejected:`** This occurs if the reviewer fails to approve the prevalidated commit within the stipulated days mentioned in **Commit Validation - Approval Settings** section (**Admin > My Account > Commit Validation - Approval Settings**).

<figure><img src="../../../../../.gitbook/assets/image (1088).png" alt=""><figcaption></figcaption></figure>

5. **`Review Pending:`** The status shows as Review Pending for commits/merges when approvals are requested. In this case, the requested approvers need to approve the open request by clicking on the **`Approve/Reject`** button.

<figure><img src="../../../../../.gitbook/assets/image (1089).png" alt=""><figcaption></figcaption></figure>

It is mandatory to add comments when rejecting an open request. A comment is optional for approval.

<figure><img src="../../../../../.gitbook/assets/image (1090).png" alt=""><figcaption></figcaption></figure>

6. **`No Modifications:`** If there are no metadata component differences between the commits, you will find your commit with the status **`No Modifications`**.

<figure><img src="../../../../../.gitbook/assets/image (1091).png" alt=""><figcaption></figcaption></figure>

### Filtering the Commits <a href="#filtering-the-commits" id="filtering-the-commits"></a>

1. By **`Repository`** and **`Branch:`** Filter the commits by version control repository and branch.

<figure><img src="../../../../../.gitbook/assets/image (1092).png" alt=""><figcaption></figcaption></figure>

2. **By Content:** You can search for commits based on content. You can also enter the commit label, revision number, or comment in the search field to filter the exact commit.Content search is case-sensitive.

<figure><img src="../../../../../.gitbook/assets/image (1093).png" alt=""><figcaption></figcaption></figure>

3. By **`Pending Approvals:`** Filters the commits for which reviewer approval is pending.

<figure><img src="../../../../../.gitbook/assets/image (1094).png" alt=""><figcaption></figcaption></figure>

4. By **`Date Range:`** You can enter a date range to show only the commits in that timeframe.

<figure><img src="../../../../../.gitbook/assets/image (1095).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1096).png" alt=""><figcaption></figcaption></figure>

**By Commits type:** Filter the commits based on their type, e.g., EZ-Commit, prevalidated commit, merge, or prevalidated merge type.

<figure><img src="../../../../../.gitbook/assets/image (1097).png" alt=""><figcaption></figcaption></figure>

**By Author:** When you’re only looking for commits committed by a particular user, use the **Committed By filter**.

<figure><img src="../../../../../.gitbook/assets/image (1098).png" alt=""><figcaption></figcaption></figure>

5. By **`Board:`** Filter the commits based on the Salesforce or Vlocity commits.

<figure><img src="../../../../../.gitbook/assets/image (1099).png" alt=""><figcaption></figcaption></figure>

### Delete Commits/Merges <a href="#delete-commitsmerges" id="delete-commitsmerges"></a>

If you want to redo or delete an incorrect commit/merge initiated in ARM but not yet pushed to the repository, you can do so from the **`Commits Summary`** page by hovering your mouse over the three dots on the right side of the screen and clicking on **`Delete Commit`**.

<figure><img src="../../../../../.gitbook/assets/image (1100).png" alt=""><figcaption></figcaption></figure>

Click **`Yes`** on the **`Confirmation`** screen to permanently delete the commit/merge.

<figure><img src="../../../../../.gitbook/assets/image (1101).png" alt=""><figcaption></figcaption></figure>

**Important Notes:**

* Commits/merges can only be deleted by the user who created the commit or by the org admin.
* Approvers do not have permission to delete commits.
* Commits, once deleted, cannot be retrieved.
* Only the commits with the following status can be deleted:
  * **Merged - No Modifications**
  * **No Modifications**
  * **Review Pending**
  * **Commit Pending**
  * **Failed**
  * **Auto Rejected**
  * **Merge Conflict**
  * **Waiting for Approval**
* Commits in **Completed** or **In-progress** status cannot be deleted.

<figure><img src="../../../../../.gitbook/assets/image (1102).png" alt=""><figcaption></figcaption></figure>

Once the commit is deleted, an automated email is sent to the user who created the commit, the user who deleted the commit, and the org admin.

### Commit Workspace <a href="#commit-workspace" id="commit-workspace"></a>

The queue commits will be reflected here when various commits are deployed to a branch. Introducing the commit workspace allows parallel commits from the same source org to different VC branches.

When you commit multiple times, keeping the target VC branch the same, the commits will run one after another. This applies to your selected Salesforce Org.

The customer has the option to delete a commit in a queue if it is no longer needed.

<figure><img src="../../../../../.gitbook/assets/image (1103).png" alt=""><figcaption></figcaption></figure>

A consolidated merge request with the respective logs as an attachment is triggered to the org admin via email for better visibility for merge requests in the queue for more than 4 hours. A sample email notification is attached below for your reference:

<figure><img src="../../../../../.gitbook/assets/image (1104).png" alt=""><figcaption></figcaption></figure>

### Deployment Workspace <a href="#deployment-workspace" id="deployment-workspace"></a>

The prevalidated deployments in the queue are displayed in this space.

<figure><img src="../../../../../.gitbook/assets/image (1105).png" alt=""><figcaption></figcaption></figure>
