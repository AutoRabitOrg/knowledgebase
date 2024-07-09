# GIT Revert

### GIT Revert: Overview <a href="#git-revert-overview" id="git-revert-overview"></a>

When working with a [version control](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) system, you'll sometimes need to undo or reverse a single commit, or a sequence of commits. This is helpful if you're trying to track down a bug and discover that it was caused by a single commit. You can use revert commit to do all of this for you instead of manually going in, correcting it, and committing a new snapshot.

### What special permissions are required to revert a commit in AutoRABIT? <a href="#what-special-permissions-are-required-to-revert-a-commit-in-autorabit" id="what-special-permissions-are-required-to-revert-a-commit-in-autorabit"></a>

The following users will have the privilege to revert commits in AutoRABIT:&#x20;

1. **Commit Author:** User who has created the commit&#x20;
2. **Org Administrator** and&#x20;
3. Users with **Revert Commits** permission

### How to Revert a Commit in AutoRABIT? <a href="#how-to-revert-a-commit-in-autorabit" id="how-to-revert-a-commit-in-autorabit"></a>

To revert a commit, simply click on three dots at the end of any commit from the **Commits** page and select **Revert Commit** from the drop-down. After that, you'll be asked to confirm that you want to reverse the commit and if you say yes, the commits will be reversed.

The **New EZ-Commit** screen is best viewed when the zoom setting is set to **75%** on your chrome/firefox browser.

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

A revert introduces a new commit to the commit history whose sole purpose is to undo the changes of a targeted commit. Importantly, this means that the existing commit history prior to the newly added "undo" commit, including the original error commit, is preserved. A revert will create a new commit with a new revision number to track the changes. The reverted commits will have the identification initials as **RC** with a different label name starting with **Revert commit - {label name used earlier}**. You can view the list of committed files for the reverted commit in the **Detailed View** under the **Committed Files** tab.

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Email notifications are triggered for each revert commit along with the summary and the status report (success, failed, or revert conflicts). Sample email notifications are attached here (one with a successful revert commit and the other with conflicts):

**Success Revert Commits**

<figure><img src="../../../../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure>

**Revert Commits Conflicts**

<figure><img src="../../../../.gitbook/assets/image (9).png" alt="" width="563"><figcaption></figcaption></figure>

### Conflicts in Revert Commit <a href="#conflicts-in-revert-commit" id="conflicts-in-revert-commit"></a>

The revert feature will revert the changes of a given commit, and it will compare your current state with the PARENT of that commit whose changes you are reverting. If the current state and that parent conflict, you will get a revert commit status as **Merge Conflict**. In this case, you must first resolve the conflict (using the **Resolve Conflict** button) before proceeding with the reverting of your commits.

<figure><img src="../../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

The next screen is the **Resolve Conflicts** screen, where you can see the files that are in conflict on the left side under the Conflicted Files section. Either you can download the conflict files in your local system, resolve them and upload them again and proceed with the commit or you can use the AutoRABIT inline editor to resolve the conflicted files. [Merge Conflicts](ez-merge/merge-conflicts.md).

<figure><img src="../../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>
