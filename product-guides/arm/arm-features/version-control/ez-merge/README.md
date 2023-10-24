# EZ-Merge

### What is EZ-Merge? <a href="#what-is-ezmerge" id="what-is-ezmerge"></a>

Merging is simply putting a forked history back together again. Say we have a new branch feature based on the master branch. We now want to merge this feature branch into the master. Using the merge process in ARM will merge the specified branch feature into the current branch...we'll assume the master.&#x20;

### Before you begin <a href="#before-you-begin" id="before-you-begin"></a>

Before a merge, several preparation steps must be taken to ensure the merge goes smoothly.

1. [**`Register your Version Control Repository in ARM`**](../introduction-to-version-control/version-control-repositories-summary.md)**`:`** An Admin can only perform this step. Register your Version Control Repositories, such as GIT, SVN, or TFS, in ARM.&#x20;
2. [**`Register your Salesforce Organization in ARM`**](../../../arm-administration/registration/salesforce-org/)**`:`** ARM connects to your Salesforce Org using the secure OAuth method or username/password connections. An Admin can only perform this step.&#x20;
3. [**`Set Up a Branch`**](../../../arm-administration/registration/version-control-branch/)**`:`** Instead of directly making changes to the code base, you can branch off from the mainline and work on a specific feature in an isolated branch. An Admin can only perform this step.&#x20;
4. [**`Mapping the users with the Version Control and Salesforce Orgs`**](../../../arm-administration/user-management/view-my-profile.md) **`in the "My Profile" section:`** Set up the permissions to create a project in ARM.&#x20;
5. **`Fetch the latest remote commits:`** Ensure the receiving branch and the merging branch are up to date with the latest remote changes.

### How do I merge my changes to a branch? <a href="#how-do-i-merge-my-changes-to-a-branch" id="how-do-i-merge-my-changes-to-a-branch"></a>

The merge process is generally performed when a feature is ready for user testing in Salesforce Orgs and usually involves code review by other development team members.

Important Note:The merge process in ARM remains valid for **seven days**. Make sure you resolve the merge conflicts (if any) for your merge label and commit the changes to another branch within **seven days,** or the merge expires. Even merge-related reports such as Static Code Analysis reports, Deployment Validation reports, or Difference reports generated also expire after **seven days**.

1.  Hover your mouse over the [**`Version Control`**](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) module and select **`Commits.`**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669369957052.png" alt=""><figcaption></figcaption></figure>
2.  Click on the **`New EZ-Merge`** button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669369999153.png" alt=""><figcaption></figcaption></figure>

The **`New EZ-Merge`** screen is best viewed when the zoom setting is set to 80% on your Chrome/Firefox browser.

3. You can also reach the **`New Merge`** screen directly by selecting **`Create New > New EZ-Merge`** from the top navigation bar.
4. In the **`New EZ-Merge`** screen, select the **`version control repository`** from where the metadata components will be fetched.
5.  Select your **`source (base) branch`** and the **`target (destination) branch`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685102090819.png" alt=""><figcaption></figcaption></figure>
6. Select the **`Merge Type`** from the dropdown:
   * _`Entire Branch`_&#x20;
   * _`Single Revision`_
   * _`Commit Label`_
   * _`Release Label`_
   * _`ALM Label`_

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669370184751.png)

#### Merge Type <a href="#merge-type" id="merge-type"></a>

**A. Entire Branch**

This option will merge the entire change from one branch to another branch.&#x20;

**Different options for `"Entire Branch"` merge type**&#x20;

*   **`Delete Source Branch:`** Once you have successfully merged the changes from the source branch to another, you can permanently delete the source branch. Select the **`Delete Source Branch`** checkbox to delete the source branch, which auto-populates whenever Entire Branch as a merge type is selected.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685102208843.png" alt=""><figcaption></figcaption></figure>

**B. Single Revision**

Merge a Single Revision from the Commits that you have performed. You can either enter the revision number (in case you remember it) or use the **`Search`** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(51\).png)) button next to the **`Single Revision`** field to pull a list of revisions from which you can choose which revision to use in the deployment.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669370328562.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669370429144.png" alt=""><figcaption></figcaption></figure>

**`Get Latest HEAD`** points out the last commit in the current checkout branch.

There could be a situation where you have entered an incorrect revision number and hit the **`Search`** button. In this case, an error message indicates that the revision number entered is incorrect.

You can also use the **`'Get All Revisions'`** button to try and get all the revisions and check for your revision from the list.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669370554952.png" alt=""><figcaption></figcaption></figure>

**C. Commit Label**

Select the commit labels created while committing to Version Control System. The commit labels created during the EZ-Commit or Merge process will be fetched in the **`Commit Label`** field.

For example, _**DXTES-19\_EZ-Commit**_, here _**DXTES-19**_ indicates the _commit label_ _name_, and _**EZ-Commit**_ denotes the label created during the _EZ-Commit_ process.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675799102097.png" alt=""><figcaption></figcaption></figure>

Click on the **`View Revisions`** link to view the list of revisions for the commit label. A new dialog box appears with the revisions, date/time stamp, comments, and author details. There is a provision to search for specific revisions using the **`Revision Search`** filter on the top right corner of the dialog box.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675799282921.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675799236641.png" alt=""><figcaption></figcaption></figure>

**D. Release Label**

You can select the release labels created using the committed revisions and the labels.

1. Select the **`Merge Type`** as **`Release Label`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675798682828.png" alt=""><figcaption></figcaption></figure>

2. The **`Release Labels`** field populates with all the available release labels in that repository/branch. If no release label is created for the above repository/ branch, an error notification states, **`"No Release Labels found."`**
3. Select your **Release Label.**&#x20;
4. Click on the **`View Revisions`** link to view the list of revisions for the release label. A new dialog box appears with the revisions, date/time stamp, comments, and author details. There is a provision to search for specific revisions using the **`Revision Search`** filter on the top right corner of the dialog box.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675798887544.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669374783969.png" alt=""><figcaption></figcaption></figure>

**E. ALM Label**

This allows you to choose and promote the ALM user stories to a higher or lower branch.

1. Select the **`Merge Type`** as **`ALM Label`**.
2.  The Work Item will gather all the user stories for which the ALM commits happened in the Source Branch of chosen Version Control Repository. Click on the **`Search`** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-112.png)) icon to find the list of user stories or work items fetched.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669374420816.png" alt=""><figcaption></figcaption></figure>

Note:You will not have the option to enter the work item details manually, you need to select the work item from the list fetched.

3. Select one of the work items from the list fetched, and click **OK**.\


#### More Options: <a href="#more-options" id="more-options"></a>

1. **Conflict Resolution Strategy**: This field allows you to select how to resolve the conflicts. If you and another user change the same file in different sandboxes or on different branches, a conflict arises when you try to commit your modified files. When the conflict occurs, ARM will use the below resolve method:
   1. **Manually resolve conflicts**: Resolve the conflicts manually.
   2. **Choose the file from the source**: Replaces the copy of the file in your workspace with the version in the repo, discarding your changes.&#x20;
   3. **Choose the file from the destination**: Accept the file in your workspace, overwriting the version in the repo when you submit the file.
2. Enter the **Merge Label name** and **comment** (if any).
3. Enter the **Email ID(s)** to send an email notification of the merge reports.
4.  **Create Commit Label:** To create a commit label for the merge operation, select this checkbox. Choose the **Salesforce** or **Vlocity** commit label type from the drop-down menu.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685102542645.png" alt="" width="375"><figcaption></figcaption></figure>
5. **Create a GIT Tag:** GIT tags are a simple and effective way to ensure you can keep track of the different versions of your code and the critical quality of Git's version control. GIT Tag operation allows meaningful names to a specific version in the repository.
6. **Skip Layout/Profile/Perm. Set Access-Setting Duplicity Check:** If you do not want ARM to list all duplicate entries for your layout/profile/permission sets, please select this checkbox. ([Learn More](merge-conflicts.md))
7. **Review Artifact:** Select this checkbox to see the list of the changed files staged for commit (during merge conflicts). This allows you to preview the changes, review them or edit the files before pushing them into your version control. ([Learn More](merge-conflicts.md))

#### Prevalidate Merge <a href="#prevalidate-merge" id="prevalidate-merge"></a>

In this section, you can assign certain pre-validation merge operations (such as deployment validation with another Salesforce Org, choosing the Apex test class to run, selecting the static code analysis tool, generating difference reports, etc.) before merging to your target branch.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682070811281.png" alt=""><figcaption></figcaption></figure>

**Different Prevalidate Merge Criteria:**

1. **Generate Diff Report:** Select this option to auto-generate a code difference report on completion of the commit.
2. **Run Static code Analysis:** Select this option if you want to run a [static code analysis tool](https://www.autorabit.com/products/codescan/) to identify potential software quality issues before the code moves to production. Similar to "**Generate Diff Report,"** this option will also be auto-selected by default if the criteria are set globally (under the **My Account > Commit Validation - Approval Settings** section).
   *   For _ApexPMD, Checkmarx, CodeScan,_ and _SonarQube_: ARM allows you to set the criteria for running the SCA tool, whether to run on all supported metadata types from the full source or to run on the newly added components.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1669375413127.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: Whenever a code analysis is triggered, ARM will wait up to **5** hours for a response. If the code analysis is not completed within 5 hours, ARM will throw a timeout exception error. This applies to all SCA tools.
{% endhint %}

1. **Validate Deployment**: Choose a Salesforce org to validate a future deployment. Further, there are different options to choose from:
   1. **Rollback on error:** This checkbox is selected by default to avoid major deployments. However, you can deselect the checkbox to skip the rollback on error under the validate deploy section in merge pre-validation so that it ignores any errors and deploys the remaining components. This is captured in the **Failed Components** tab of the **Deployment Validation** section on the commit's details page. The deployment status will be captured as **Partially Succeeded**.\
      NoteThis checkbox should be selected for Production org deployments.
   2. **Run Destructive Changes:** Here, you can specify whether to run pre or post-destructive changes while carrying out the merge process.
   3. &#x20;**Ignore Missing Visibility:** With this option, differences in visibility settings between the source and destination branches will not cause the merge to fail. ARM will compare the source and destination branches and keep only the common settings between both branches.\
      Important Note**Standard fields** are not supported for **Ignore Missing Visible Settings**.\

   4. **Ignore installed components:** When selected, ARM will scan for the components that are deployed, and if there are any managed package components located in the destination branch, these components will be excluded from the metadata.zip files while the remaining components are deployed.&#x20;
   5.  **Apex Test Level:** Choose your [Apex Test Level](../../../apex-unit-tests.md) to validate your merge.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682260915531.png" alt=""><figcaption></figcaption></figure>

Points to Remember:

1. **Prevalidate Merge** section will be visible only if the Admin has enabled the **'Merge Setting'** checkbox under the **My Account** section.&#x20;
2. Users with the **'Merge Review Overridable'** role have special permission to check or uncheck the pre-validate option. However, each time they try to commit to the branch, a notification alert mail gets triggered to the email ID as specified in **My Account > Merge Settings**.&#x20;
3. **Prevalidate Merge** section will not be displayed for Version control repositories registered in the **'SFDX'** structure.
4. Suppose the meta-XML file does not exist in the Destination Branch and is available in the Source Branch. The meta-XML file is copied from the source to the destination branch before committing to the remote repository. The newly added meta-XML file will be added to the files list, committed to the remote repository, and added to the **Validate Deployment** package.
5. Based on the permission assigned by your Admin, you will see the options in the active state. Suppose your Admin has assigned you permission to run a static code analysis tool only to review your code before merging them. In that case, the **Run Static Code Analysis** option will remain inactive, while other options will remain disabled or won't be seen.
6. Based on the Approval Reviewer level set in '**Merge Settings'** (under the **My Account** section), you need to specify the email address of the reviewers for a given proposed code change and to approve merge requests.

#### ALM Integration <a href="#alm-integration" id="alm-integration"></a>

You can update the status of the ALM work item through the **ALM Integration** section (below the **Pre-validate Merge** section), and the same gets reflected in your ALM system.

1. Select the **ALM label**.
2. Select the **Project** and the **sprint** for which the commit is planned.
3.  Select the **Work Item,** and the **Current Status** for the work item gets auto-populated. This allows you to update the ALM for the Merge operation with or without changing the current work item status. Click on the **+** icon to add another work item and update its status.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658758875620.png" alt=""><figcaption></figcaption></figure>

Click on either **Dry Run** or **Validate & Merge**.

| Dry Run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Validate & Merge                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>The dry run option will show the user how the merge will execute without making any changes.</li><li>Don’t merge anything; show what would be done.</li><li>Lists what will be pushed to the Integration branch from the Dev branch.</li><li>The status shows as <strong>"MERGE NOT COMMITTED."</strong></li><li>View the conflicts if there are any during the dry run merge. Later, it will ask to initiate a merge in the <strong>View Conflict</strong> screen, which gets converted to a standard validation merge.</li></ul> | <ul><li>Changes are validated and later merged from the Dev branch to the Integration branch without committing to the remote repository.</li><li>The difference report and the static code analysis report are published based on the delta and shared with the user.</li><li>The admin/reviewer can approve or reject the changes.</li><li>The user can merge the changes to the remote repository if approved.</li></ul> |

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682071104699.png)

*   A notification appears that the merge request has been submitted for Entire Branch and Single Revision merge types. Click **OK**, and you will be auto-redirected to the **Commits** screen, where you can find the status of the initiated merge.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658757897595.png" alt=""><figcaption></figcaption></figure>
*   A confirmation dialog box will ask you to approve the requested operation for **Release Label**, **Commit Label**, and **ALM Label** merge types. Click **OK**, and you will be auto-redirected to the **Commits** screen, where you can find the status of the initiated merge.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658755378925.png" alt=""><figcaption></figcaption></figure>

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

For merge labels that are either in progress or have some conflicts, in such a scenario, you will find a popup that will appear as shown below when you press the **Validate & Merge** button. _**These merge conflict statuses will only be shown for the merges created within seven days**._

![Merge Labels](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1611089484695.png)

**Resolution:** To prevent this, first, resolve current merge conflicts or allow the in-progress merge status to move to the completed state and then restart the merge process again.

### Common Issues with EZ-Merge

While performing an EZ-Merge, inaccurate file changes are being merged into the destination branch.

**Issue references in stackoverflow link:** [https://stackoverflow.com/questions/63365836/git-is-showing-a-file-as-moved-on-bitbucket-i-want-it-as-a-new-file-for-pull-r](https://stackoverflow.com/questions/63365836/git-is-showing-a-file-as-moved-on-bitbucket-i-want-it-as-a-new-file-for-pull-r)

&#x20;**What do I need to do outside of ARM?**

1. Checkout to the target branch.
2. Merge the branch by executing the command shown in the ‘applying merge’ log.
3. Check the results for the modified files.
4. If the result matches the ARM file changes, then this is a Git behavior.
