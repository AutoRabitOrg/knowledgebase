# Version Control-FAQs

## What is a Version Control System (VCS)? <a href="#what-is-a-version-control-system-vcs" id="what-is-a-version-control-system-vcs"></a>

Version Control Systems are a category of software tools that helps in recording changes made to files by keeping a track of modifications done to the code.

## What are the version control tools supported by ARM? <a href="#what-are-the-version-control-tools-supported-by-arm" id="what-are-the-version-control-tools-supported-by-arm"></a>

The following version controls are supported:

* GIT
* TFS
* SVN

## What is GitHub and how does it work? <a href="#what-is-github-and-how-does-it-work" id="what-is-github-and-how-does-it-work"></a>

GitHub is the home for all developers—a platform where you can share code, contribute to open source projects, or even automate your workflow with tools like GitHub Actions and Packages. If you’re just getting started with GitHub, you may know us best as a place for version control and collaboration.

## Are Git and GitHub the same? <a href="#are-git-and-github-the-same" id="are-git-and-github-the-same"></a>

Git is a version control system (VCS). GitHub is the platform where Git repositories can be hosted and teams can work on them together.

## What's the difference between git fetch and git pull? <a href="#whats-the-difference-between-git-fetch-and-git-pull" id="whats-the-difference-between-git-fetch-and-git-pull"></a>

* **git fetch** really only downloads new data from a remote repository - but it doesn't integrate any of this new data into your working files. Fetch is great for getting a fresh view on all the things that happened in a remote repository.
* **git pull**, in contrast, is used with a different goal in mind: to update your current HEAD branch with the latest changes from the remote server. This means that pull not only downloads new data; it also directly integrates it into your current working copy files.

## Why do Merge Conflicts happen? <a href="#why-merge-conflicts-happens" id="why-merge-conflicts-happens"></a>

When working in Version Control System such as GIT, users can combine commits from two different branches through an action known as merging. Files are automatically merged unless there are conflicting sets of changes (i.e. the commits update the same line of code differently).

A merge conflict is an event that occurs when your version control is unable to automatically resolve differences in code between two commits.

When there are conflicting changes on the same lines, a “merge conflict” occurs because the version control doesn’t know which code to keep and which to discard.

## What is Commit in AutoRABIT? <a href="#what-is-commit-in-autorabit" id="what-is-commit-in-autorabit"></a>

As you work with your files that are under version control, each change is tracked automatically. This can include modifying a file, deleting a directory, adding a new file, moving files or just about anything else that might alter the state of the file. Instead of recording each change individually, the version control system will wait for you to submit your changes as a single collection of actions. In version control, this collection of actions is known as a commit.

## **How does Git handle Duplicate File Change Commits?**

Git's handling of duplicate file change commits can be a different aspect of Version Control management, particularly when merging branches with identical changes.

1.  **Q: Why does Git allow duplicate commits when performing duplicate merges in AutoRABIT?**

    **A:** Git's behavior of creating new commits for each merge, even if the changes are merged multiple times, is intrinsic to its design. This allows Git to maintain a detailed commit history and track changes accurately.
2.  **Q: How can users prevent unintended duplicate merges in AutoRABIT when encountering duplicate commit scenarios?**

    **A:** To prevent unintended duplicate merges, users should follow version control best practices, such as reviewing changes before committing, resolving merge conflicts promptly, and educating themselves on Git's behavior regarding commit history.
3.  **Q: Is the behavior of duplicate merges in Git a flaw in AutoRABIT's integration with Git?**

    **A:** No, the behavior of duplicate merges in Git is not a flaw in AutoRABIT but rather a fundamental aspect of Git's functionality. AutoRABIT works within the framework of Git's design and behaviour when handling merge operations.
4.  **Q: How can AutoRABIT users effectively manage duplicate merges and maintain code integrity in their development processes?**

    **A:** Users can effectively manage duplicate merges by understanding Git's behavior, educating themselves on version control best practices, training on commit history management, and implementing enhanced error handling mechanisms to alert users of potential duplicate commits.

## Branching and Merging- what's the difference? <a href="#branching-and-merging-whats-the-difference" id="branching-and-merging-whats-the-difference"></a>

A **branch** allows you to create a copy (or snapshot) of the repository that you can modify in parallel without altering the main set. You can continue to commit new changes to the branch as you work, while others commit to the trunk or master without the changes affecting each other.

Once you’re comfortable with the experimental code, you will want to make it part of the trunk or master again. This is where **merging** comes in. Since the version control system has recorded every change so far, it knows how each file has been altered. By merging the branch with the trunk or master (or even another branch), your version control tool will attempt to seamlessly merge each file and line of code automatically. Once a branch is merged it then updates the trunk or master with the latest files.

## What are Remote repositories? <a href="#what-are-remote-repositories" id="what-are-remote-repositories"></a>

Remote repositories allow us to share our changes with other members of the team. They can be on a private server, on a different computer than yours, or hosted on a different service. Wherever yours is hosted, you'll need to be able to sync your local repository with the remote repository frequently. To start sharing changes with others, you have to push them to a remote repository. This will cause the remote repository to update and synchronize with your local repository.

## Why merge is getting auto-rejected during deployment? <a href="#why-merge-is-getting-auto-rejected-during-deployment" id="why-merge-is-getting-auto-rejected-during-deployment"></a>

Below are the reasons why ARM rejects your merge request:

* It will be auto-rejected if the proper **merge criteria** are not enabled. The merge criteria must be enabled before you are performing the jobs.
  * Navigate to **Admin > My Account > Merge Setting** to select the proper merge criteria. Click [Here](https://knowledgebase.autorabit.com/product-guides/arm/arm-administration/user-management/manage-users-account-settings#id-9-merge-settings) for a more detailed explanation.
* **Workspaces** is wrongly configured
  * Search for the workspace id which has the name of the source & target branch and reset that workspace. Once the workspace reset is complete, trigger a new merge.
* Failed to meet the actual code coverage criteria
  * Please update the merge criteria as needed by disabling code coverage under **Admin > My Account > Merge Settings**.

## ARM says, **"Local and remote repositories are not on the same revision,"** what does it mean?" <a href="#autorabit-says-local-and-remote-repositories-is-not-on-same-revision-what-does-it-mean" id="autorabit-says-local-and-remote-repositories-is-not-on-same-revision-what-does-it-mean"></a>

There are several possible explanations for AutoRABIT to throw an error **"local and remote repo is not on same revision"**:

1. The local repository is out of date.
2. The branch that contains the commit was deleted, so the commit is no longer referenced
3. Someone force pushed over the commit.

## How long does it take to register a version control branch in ARM? <a href="#how-long-does-it-take-to-register-a-version-control-branch-in-arm" id="how-long-does-it-take-to-register-a-version-control-branch-in-arm"></a>

The actual registration of a branch depends on the data available in your version control repository. Mostly, the registration can be accomplished in a matter of **1-2 minutes**, however, in some rare cases, it can take anywhere from **30 minutes** to **an hour**.

## Is it possible with the ARM tool to have merge approval only for one specific branch and not for others? <a href="#is-it-possible-with-arm-tool-to-have-merge-approval-only-for-one-specific-branch-and-not-for-others" id="is-it-possible-with-arm-tool-to-have-merge-approval-only-for-one-specific-branch-and-not-for-others"></a>

We don't have a feature to limit approvals to specific branches right now. However, there are a few options that can assist you in obtaining merge approval for a specific branch:

* When performing a merge, make sure none of the options under **New EZ Merge > Prevalidation Merge** are selected; this allows you to merge without approval.
* Under **Admin > MyAccount > Merge Settings**, make sure the **disable merge self-approval** checkbox is not selected.

## I can only see the Production org and none of the development instances when I try to do a new EZ commit. <a href="#i-can-only-see-the-production-org-and-none-of-the-development-instances-when-i-try-to-do-a-new-ez-co" id="i-can-only-see-the-production-org-and-none-of-the-development-instances-when-i-try-to-do-a-new-ez-co"></a>

You haven't switched on the skip mapping feature, which is why this is happening. Select **"Skip Mappings"** from the drop-down menu in **My Profile > My Roles**.

## What is the cause of ARM's inability to initiate the auto build on commit, as well as the failure of a GitHub pull request? <a href="#what-is-the-cause-of-arm-inability-to-initiate-the-auto-build-on-commit-as-well-as-the-failure-of-a" id="what-is-the-cause-of-arm-inability-to-initiate-the-auto-build-on-commit-as-well-as-the-failure-of-a"></a>

1. Allow pull requests and build on commit in your VC repository.
2. To see the external pull request, switch on ARM's **auto-sync** option.

## Why is ARM rejecting my merge request at the final step? <a href="#why-is-arm-rejecting-my-merge-request-at-the-final-step" id="why-is-arm-rejecting-my-merge-request-at-the-final-step"></a>

This is due to the fact that the merge criteria do not match the ARM settings. Before submitting the merge request, configure it in ARM to match your needs. Make the appropriate modifications under **Admin > Merge Settings**.

## All merge deployments in ARM fail when I try to deploy code from one sandbox to another. Could you assist me with this? <a href="#all-merge-deployments-in-arm-fail-when-i-try-to-deploy-code-from-one-sandbox-to-another-could-you-as" id="all-merge-deployments-in-arm-fail-when-i-try-to-deploy-code-from-one-sandbox-to-another-could-you-as"></a>

You won't be able to deploy the code to the target org if all of the profile objects in the package have access permissions set to **"false."** _It's not an ARM issue; it's a salesforce behavior_.

Change the access permission to **"True"** in all profile objects and deploy to fix the problem; it should now work.

## I am getting a space issue with my development team, and they are not able to commit the changes through AutoRABIT, due to this branch creation is getting failed. Why? <a href="#i-am-getting-space-issue-with-my-development-team-and-they-are-not-able-to-commit-the-changes-throug" id="i-am-getting-space-issue-with-my-development-team-and-they-are-not-able-to-commit-the-changes-throug"></a>

* Branch creation seems to fail due to the huge Workspace checkout. I would recommend unregistering the unused branches that are already registered in AutoRABIT so that the base checkout will get deleted and the workspace size will be increased.
* Under **Workspaces**, there are some workspace IDs where there is Delete button is greyed out and those are the base checkouts it will get deleted only if we unregister those branches. So, ensure if there are any unused branches then proceed with unregistering them in AutoRABIT.

## I have access to the apex class for the profiles, but I am not able to find the updated profile data in AutoRABIT. <a href="#i-have-access-to-the-apex-class-for-the-profiles-but-i-am-not-able-to-find-the-updated-profile-data" id="i-have-access-to-the-apex-class-for-the-profiles-but-i-am-not-able-to-find-the-updated-profile-data"></a>

The Apex class permissions for the profiles can be committed only when you select both Apex classes and profile metadata members while performing EZ-Commit. Also, you need to select the checkbox **"Commit Only Profiles for selected metadata members"** on the **Commits Summary** page to commit only profile changes that contain apex class permissions.and&#x20;

## Why does a Git branch not display in the "My version control Mapping list" under "My Profile" after being registered in AutoRABIT? <a href="#why-does-a-git-branch-not-display-in-the-my-version-control-mapping-list-under-my-profile-after-bein" id="why-does-a-git-branch-not-display-in-the-my-version-control-mapping-list-under-my-profile-after-bein"></a>

This is because you haven't given permission to that branch in AutoRABIT yet. Re-register the branch in AutoRABIT by checking the checkboxes next to the GIT lists to whom you want to access in the **My Profile** section.

## Why the Profiles/Permission sets are not getting committed to my development branch during EZ-Commit? <a href="#why-the-profilespermissionsets-are-not-getting-committed-to-my-development-branch-during-ezcommit" id="why-the-profilespermissionsets-are-not-getting-committed-to-my-development-branch-during-ezcommit"></a>

For such a case, there can be three possibilities:

* There are **no changes** in metadata components between the sandbox and the branch.
* **Salesforce** is not allowing it
  * Retrieve the permission sets using the workbench. If still the permission sets are not retrieved, then it is a limitation from Salesforce. Request you contact Salesforce Support Team for further assistance.
* Components (StandardField, Report, Dashboard, etc.) related to the **Profile/Permission sets** are not selected during the commit.
  * Select the appropriate components related to the Profiles/ Permissions object under **"Select metadata members"** in the **New EZ-Commit** screen and commit once again.

## How to deploy the Field level Security (FLS) permission from version control to your target org? <a href="#how-to-deploy-the-field-level-security-fls-permission-from-version-control-to-your-target-org" id="how-to-deploy-the-field-level-security-fls-permission-from-version-control-to-your-target-org"></a>

Field Level Security (FLS) settings will allow you to restrict the users’ access to view and edit specific fields. In order to deploy the FLS settings from a branch to a sandbox in AutoRABIT, you need to perform the below steps:

* **During "EZ-Commit"**
  * While committing the changes from a sandbox to a destination branch, commit the custom fields and profiles in a single commit.
* **During "Deployment"**
  * While deploying the Field Level Security (FLS) permissions from the version control branch to the target org, ensure the custom fields and profiles are a part of the same revision.

## What is the functional difference between Release Label Merge and Release Label Deployment? <a href="#what-is-the-functional-difference-between-release-label-merge-and-release-label-deployment" id="what-is-the-functional-difference-between-release-label-merge-and-release-label-deployment"></a>

Release Label is a set of commit revisions.

* When you **merge** using a release label, ARM will cherry-pick all the revisions and labels in that release label and consolidate all the changes made to that branch. These delta changes are pushed to the destination branch after the conflicts (if any) have been resolved.
* Whereas, when you deploy a release label, ARM identifies and uses the latest revision in that Release Label as **HEAD**. The latest revision is identified based on the commit date. Any files in that revision that may have been modified, added, or deleted are consolidated, including any changes made to those files in other revisions besides the **HEAD** revision. When the deployment is performed, this consolidated metadata file is retrieved.

## While creating a new Release Label, I did not select the 'Create package manifest for Deployment' check box. Can I still create a package? <a href="#while-creating-a-new-release-label-i-did-not-select-the-create-package-manifest-for-deployment-check" id="while-creating-a-new-release-label-i-did-not-select-the-create-package-manifest-for-deployment-check"></a>

Yes. If you did not select the check box while creating the release label, you can click on the **Create Artifact** button on the **Release Label Summary Screen** to manually create and run the package.

## Why can't I click the 'Create Artifact' button on the Release Label Summary screen? <a href="#why-cant-i-click-on-the-create-artifact-button-on-the-release-label-summary-screen" id="why-cant-i-click-on-the-create-artifact-button-on-the-release-label-summary-screen"></a>

If the **Create Artifact** button is unavailable to click, the package has been created successfully and can be used for Deployment. It will also be unavailable if package preparation is **In-Progress** and will be available shortly. You can view the status on the **Release Label Summary** screen. **Create Artifact** button will only be available if the package has not been prepared or has failed during preparation.

## Why am I getting an error while registering the GitHub repository with SSH? <a href="#why-am-i-getting-an-error-while-trying-to-register-github-repository-with-ssh" id="why-am-i-getting-an-error-while-trying-to-register-github-repository-with-ssh"></a>

**GitHub** no longer allows new **RSA** keys with **SHA-1** signatures. Execute the `ssh-keygen -t ed25519 -C “sampath.c@autorabit.com”` command in the terminal to create a new key, or contact **support@autorabit.com** for further assistance. Please note that you must create the new key in **Linux** or **Unix**, not in Windows. For more information, visit [https://github.blog/2021-09-01-improving-git-protocol-security-github/](https://github.blog/2021-09-01-improving-git-protocol-security-github/)

## My commit failed with errors like 'Tip of your current branch is behind' and '\[rejected] Partial -> Partial (non-fast-forward)'. Why did this happen, and how can I resolve it? <a href="#my-commit-failed-with-errors-like-tip-of-your-current-branch-is-behind-and-rejected-partial-partial" id="my-commit-failed-with-errors-like-tip-of-your-current-branch-is-behind-and-rejected-partial-partial"></a>

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-OION20SF.png)

To put it simply, this was caused because of an expected **Git** behavior.

Basically, if the commit is rejected with the error message **"Tip of your current branch is behind,"** it means that there is another commit that has already been done on top of the target branch.

Let us assume that you have initiated a merge, and while it is processing, someone else (other developers) performs a commit onto the target branch. This will modify the **HEAD revision**, and the merge that had set a HEAD revision will no longer be the latest HEAD on the target branch. After resolving the conflicts and while committing the merge, this error is displayed.

This merge process will fail, and it is not possible to **Re-Push** because when compared to the latest HEAD revision, it should bring up the conflicts again, which is not possible.

You must **re-perform** the merge so the commit will set up the **latest HEAD revision** on the **destination branch** and process further.

## How can I get rid of a malformed duplicate file in the merge? <a href="#how-can-i-get-rid-of-a-malformed-duplicate-file-in-the-merge" id="how-can-i-get-rid-of-a-malformed-duplicate-file-in-the-merge"></a>

If the **Permissionset** file you're trying to upload has some malformed structure, please contact our support team so we can validate using **XML validator**. After resolving it, you can upload the Permissionset file successfully and proceed with the merge.

## I performed a commit using two fields and used that same commit to perform a merge. Why is the second field showing differently and picked up by another object? <a href="#i-performed-a-commit-using-two-fields-and-used-that-same-commit-to-perform-a-merge-why-is-the-second" id="i-performed-a-commit-using-two-fields-and-used-that-same-commit-to-perform-a-merge-why-is-the-second"></a>

The merge with the **cherry-pick command** by GIT gives you results of such **Custom Fields** while merging to the target branch. The same thing happened when there was a new commit. The merge process followed even before reverting the actual commit and got the same result from GIT. There is no issue with the workspaces here.

## I’m trying to create a commit, but the delta fails with the error 'REJECTED\_NONFASTFORWARD.' <a href="#im-trying-to-create-a-commit-why-is-delta-failing-with-the-error-rejectednonfastforward" id="im-trying-to-create-a-commit-why-is-delta-failing-with-the-error-rejectednonfastforward"></a>

Suppose the error REJECTED\_NONFASTFORWARD is thrown in your EZ-Commit; in that case, the issue is specific to your repository, and the error occurs at the GIT version control level when multiple developers try to modify a file simultaneously. If you reencounter this issue, please wait a few minutes and reattempt the commit.

## Why can’t I select the Report Type for deployment? <a href="#why-cant-i-select-the-report-type-for-deployment" id="why-cant-i-select-the-report-type-for-deployment"></a>

Please go to Admin->My account-> Salesforce Settings->Included Metadata Types, and check if the Report and Report Type are included in the Salesforce Settings.\
If these are not included, please include them to see them during the metadata selection for deployment.

## Why is the API name change showing under Deleted Components in Commit? <a href="#why-is-api-name-change-showing-under-deleted-components-in-commit" id="why-is-api-name-change-showing-under-deleted-components-in-commit"></a>

When there is an **API name change**, Salesforce considers it a **new metadata API** while the retrieved call occurs.\
When committing such API name change components, please select the new API name, and the older one can be deleted as a destructive commit.\
Now, while deploying these changes, we recommend using the **Pre-destructive** option to deploy the deleted one first, and then the actual API name change components get deployed.

## Why can't I see any Salesforce Orgs or Version Control repositories while performing EZ-Commit? <a href="#why-cant-i-see-any-salesforce-orgs-or-version-control-repositories-while-performing-ezcommit" id="why-cant-i-see-any-salesforce-orgs-or-version-control-repositories-while-performing-ezcommit"></a>

Salesforce Orgs are displayed on the EZ-Commit screen if an admin selects the **Skip Mappings** checkbox on the **Profile** page.\
**Profile > My Roles > Skip Mappings**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RWBAABG4.png" alt=""><figcaption></figcaption></figure>

If the admin does not enable **Skip Mappings**, users must map their respective **Version Control repository** branch to their **Salesforce Org**.\
**Admin > Salesforce Org Mgmt > Selected Salesforce Org > Salesforce Org- Mapping**, then map the respective branches individually.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-NQZR70NU.png" alt=""><figcaption></figcaption></figure>

To avoid this, contact your admin to select the **Skip Mappings** checkbox under the **My Roles** section on the **Profile** page.\
More information on how to map a branch to a Salesforce org is available [here](https://knowledgebase.autorabit.com/docs/salesforce-org-management#salesforce-org-mappings).

## How can I commit restricted 'Profile User Permissions'? <a href="#how-can-i-commit-restricted-profile-user-permissions" id="how-can-i-commit-restricted-profile-user-permissions"></a>

Due to limitations from Salesforce, **User Permissions** set to **`False`** cannot be retrieved via **Metadata API** call.\
Hence, those changes are not displayed under the **File Diff** report in **EZ-Commit** for **Profiles**. This is an expected behavior.\
For more information on the Profile Metadata, click [here](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_profile.htm?q=profile).\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AFEGV45F.png" alt=""><figcaption></figcaption></figure>

## Why are metadata members added to or removed from the package.xml during a commit even if they are not part of the commit? <a href="#why-are-metadata-members-added-to-or-removed-from-the-packagexml-during-a-commit-even-if-they-are-no" id="why-are-metadata-members-added-to-or-removed-from-the-packagexml-during-a-commit-even-if-they-are-no"></a>

The metadata members present in the **target branch** are added to the **package.xml**, and those absent from the **target branch** are removed. Verify that the deleted members no longer exist and the added members are listed in the target branch of your version control repository.\
If the added/deleted metadata members do not match those in the target branch, contact the AutoRABIT support team at support@autorabit.com for further assistance and troubleshooting.

## Why are Wave Components missing from the component list during EZ-Commit despite being listed as 'Included Metadata Types' in the Salesforce settings? <a href="#why-are-wave-components-missing-from-the-component-list-during-ezcommit-despite-being-listed-as-incl" id="why-are-wave-components-missing-from-the-component-list-during-ezcommit-despite-being-listed-as-incl"></a>

If the user who registered the SF Org in ARM has no **Einstein Analytics license**, Wave Components do not appear under metadata members in EZ-Commit.

## Why did the Merge/Commit Prevalidation deployment fail due to the error 'Picklist not found'? <a href="#why-did-the-mergecommit-prevalidation-deployment-fail-due-to-the-error-picklist-not-found" id="why-did-the-mergecommit-prevalidation-deployment-fail-due-to-the-error-picklist-not-found"></a>

The potential causes of _Picklist not found_ error-related Merge/Commit Prevalidation deployment failures are listed below, along with the procedures you need to follow to fix them:

* **Verify the field name:** Verify the API name or the label of the picklist field you're trying to reference and the spelling and capitalization of your source.
* **Check the object:** Verify the object you're working with has the picklist field you're looking for. Locate the proper object by going to the **Object Manager** in **Salesforce Setup**. Look for the disputed field in the **Fields & Relationships** section in the target org.
* **Validate field-level security:** Make sure the user or profile you're using can see and access the picklist field. Ensure the user has the appropriate permissions to see and update the field by checking the field-level security settings for their profile. Check the **field-level security settings** to ensure the user's profile has appropriate permissions to view and edit the field.
* **Consider record types:** If your Salesforce org utilizes record types, check to see if the picklist field is specific to a particular record type. If it is, ensure that the user or profile you're using has access to the relevant record type.
* **Consider field dependencies:** If the picklist field has any field dependencies or controlling fields, ensure that the controlling field values are set correctly. If the controlling field values are incorrect or incompatible, it can lead to the "picklist field not found" error.

## Why are unexpected files not part of a revision picked in the merge when the revision is cherry-picked? <a href="#why-are-unexpected-files-that-are-not-part-of-a-revision-picked-in-the-merge-when-the-revision-is-ch" id="why-are-unexpected-files-that-are-not-part-of-a-revision-picked-in-the-merge-when-the-revision-is-ch"></a>

This is not an ARM issue but rather an expected behavior from Git.\
Perform the following actions outside of ARM to determine whether the issue stems from ARM or Git:

1. Take a local clone of the repository and then checkout of that branch using the command below:\
   _git checkout \<branchname>_
2. Cherry-pick merge the revision by executing the command in the applying merge log which is as shown below:\
   _git cherry-pick < revision > -n --strategy recursive --strategy-option ignore-cr-at-eol_
3. Check the results for the modified files by running the command below:\
   _git status_

Compare the results with the changes in the ARM file. If the results match the changes in the ARM file, we can conclude that this is Git behavior. If the results do not match, contact the AutoRABIT support team at support@autorabit.com so we can assist you further.

## Why am I getting an **Invalid Schema error during the Merge Prevalidation Process?**

This issue will occur if there are any special characters like the one below and if the string (length=7) is considered a GIT conflict (it is a GIT behavior), it will not perform the Merge.

Special Characters: '>' ; '<' ; '|' ; '=' &#x20;

We recommend maintaining the above four special characters to less than 7 to avoid such problems.

For example, in the Class file, if you observe this **">>>>>>>"** character string (length=7), then update it to less than 7 in the branch itself and rerun the Merge operation.

## Why is my EZ-Commit revert failing with an "Invalid ID" error?

Sometimes you need to undo or reverse a single commit while working with a version control system. This is helpful if you're trying to track down a bug and discover that a single commit caused it. You can use revert commit to do this for you instead of manually going in, correcting it, and committing a new snapshot. When a user tries to reverse the EZ-Commit, it fails with an exception. The expected behavior is to revert the EZ-Commit as per the design and create a new commit.

In this scenario, the feature's proper operation requires a successful commit on the branch. Users should have the following privileges to revert commits in AutoRABIT:

1. **Commit Author:** User who has created the commit
2. **Org Administrator** and
3. Users with **Revert Commits** permission

### Step-by-Step Guide:

Here are the steps to reproduce the scenario:

1. Create a commit from the source to the destination branch.
2. Commit some data.
3. Once the commit is successful, go to commit history, and for the commit, click on three dots.
4. Click on the revert commit option. It will create a new job for the revert.
5. This will fail with the error/exception Invalid ID.

A code fix has resolved this issue. There is a fix available in the ARM 23.1.31 build version.

## Why do I get the following error: "Cannot find the declaration of element 'web:validateSalesforceOrgConnection'" when selecting an org in EZ-Merge?

The error below pops up while selecting the org for merge validation: `cvc-elt.1.a: Cannot find the declaration of element 'web:validateSalesforceOrgConnection'`

**Cause of the issue:** This may be due to a cache problem while selecting the Salesforce Org.

**Resolution:** Clearing the browser cache and refreshing the browser will resolve the issue.



