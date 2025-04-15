# Merge Conflicts

## About Merge Conflicts <a href="#about-merge-conflicts" id="about-merge-conflicts"></a>

When working in a [Version Control System](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) like Git—especially in Salesforce development where multiple team members may be working on Apex classes, Lightning Web Components, or metadata files—merge conflicts can occur during the process of combining changes from different branches. This typically happens when two developers modify the same lines in a file, such as an Apex trigger or a custom object’s metadata.

If the changes are on separate lines or in different sections of the file, Git merges them automatically. But when conflicting changes are made to the same lines—like different updates to a validation rule or conflicting field-level security settings—Git can’t decide which version to keep, and a _merge conflict_ is triggered. Resolving the conflict manually ensures that only the correct, intended changes are preserved in your Salesforce org.

## Resolving Merge Conflicts <a href="#resolving-merge-conflicts" id="resolving-merge-conflicts"></a>

There are 2 ways to resolve the conflicted files:

1. Download conflicted files locally or
2. Using merge conflict Inline editor.

### Download Conflicted Files Locally <a href="#download-conflicted-files-locally" id="download-conflicted-files-locally"></a>

ARM has given a provision to the user to download the conflicted files in their local machine, resolve them locally and upload the same.

To do so,

1. Go to the **Commits** screen.&#x20;
2. Search for your merge label that has a conflict. Click on the **Resolve Conflict** button.

<figure><img src="../../../../../.gitbook/assets/image (33) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. The list of **conflicted files** or **merged files** will display on the next screen.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (34) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="534"><figcaption></figcaption></figure>

4.  To sort all listed items in ascending or descending order, click on![](<../../../../../.gitbook/assets/image (35) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon.

    * ![](<../../../../../.gitbook/assets/image (36) (1) (1) (1) (1) (1) (1) (1) (1).png>)will sort the listed items in ascending order
    * ![](<../../../../../.gitbook/assets/image (37) (1) (1) (1) (1) (1) (1) (1) (1).png>)will sort the items in descending order

    <figure><img src="../../../../../.gitbook/assets/image (38) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="534"><figcaption></figcaption></figure>
5. The **File Path view** displays a dynamic, hierarchical list of conflicted/merged items. The **Tree view** displays the parent-child relationships of the conflicted/merged files.

<figure><img src="../../../../../.gitbook/assets/image (39) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="549"><figcaption></figcaption></figure>

6. Now, select the conflicted files that you want to resolve and click on the **Download** (![](<../../../../../.gitbook/assets/image (40) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon.

<figure><img src="../../../../../.gitbook/assets/image (41) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="533"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** If there is a conflict related to file tree, then GIT shows that the file does not have any conflicts.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/image (42) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="367"><figcaption></figcaption></figure>

7. To proceed further, select the check box for the respective conflict, click on the **3 dots**, and then select if you want to use the **source** changes or the **destination** changes. Then you can go ahead and proceed with the next step to resolve the conflict.
8. When you click on the **Download** icon, a confirmation message box to include **.git** or **.svn folder** with **"Yes"** and **"No"** buttons will be displayed. If you select the **'Yes'** button only, then the conflicted files including the **.git** or **.svn folder** will be downloaded to your local machine in **zip** format.

<figure><img src="../../../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Now, work on the conflicted files using your merge tool (example- TortoiseSVN, TortoiseGit) and make necessary changes to it.&#x20;
10. Click on the **Upload** (![](<../../../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon and upload the resolved files. Make sure the file uploaded is in **zipped** format.
11. Finally, click on **Commit** to commit the changes in the destination branch.

### Merge Conflict Inline Editor <a href="#merge-conflict-inline-editor" id="merge-conflict-inline-editor"></a>

The Merge inline editor helps users to resolve more complex merging conflicts directly from the ARM merge interface.

{% hint style="info" %}
**Important Note:** Files over **10 MB** may not be resolved using Merge Inline Editor, therefore, in such a scenario, download the conflicted files on your local machine, resolve, and upload them again.
{% endhint %}

1. Go to the **Commits** screen and search for your merge label that has conflict. Click on the **Resolve Conflict** icon.
2. The list of conflicted files or merged files will display on the next screen.&#x20;
3.  There is an easier method to resolve the conflicted files in one go. Select all the files and click on the 3 dots as shown in the image below and choose either of the criteria to resolve the files.

    * **Use Source:** This option retains the revisions located in the source branch
    * **Use Destination:** This option retains the revisions located in the destination branch

    <figure><img src="../../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="538"><figcaption></figcaption></figure>
4. Or, click on a conflicted file to see its related conflict blocks. This tab will display the number of insertions and deletions to each metadata file. The lines highlighted in **GREEN** color indicate those are updated (added/modified) in the source branch and for **RED** color indicates those are updated (added/modified) in the destination branch. The highlighted lines are the modified lines.

<figure><img src="../../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Navigate to other conflict blocks for the current conflict file by using the **Prev Conflict** or **Next Conflict** icon.
6.  Now, select the criteria by which you want to resolve the merge conflicts:

    * **Dest. file**: This option retains the revisions located in the Destination Branch.
    * **Src. file**: This option retains the revisions located in the Source Branch.
    * **Block**: Select this option to resolve using either Source or Destination block. Here, two options will be auto-populated and you need to select either of the options mentioned below:
      1. **Destination**: The changes in the destination block will be used in the resulting merged file.&#x20;
      2. **Source**: The changes in the source block will be used in the resulting merged file.
    * **Block from ‘Dest.’ before ‘Src.’**: This allows you to use both the blocks; first changes in the **destination** block and later **source** block. The changes are used in the resulting **Merged** file.
    * **Block from ‘Src.’ before ‘Dest.’**: This allows you to use both the blocks; first changes in the **source** block and later **destination** block. The changes are used in the resulting **Merged** file.

    <figure><img src="../../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. **Troubleshooting:** Do I have a provision to edit the inline code if the above merge criteria fail to resolve the merge conflicts?
   * In rare circumstances, your merge conflict may not be resolved by the merge criteria that ARM offers. Additionally, inline editing of the code is not supported by ARM. In such a case, we advise initiating the merge operation while keeping the checkbox for **Review Artifacts** enabled on the **EZ-Merge** screen.
   * Choose any of the merging criteria that ARM offers on the **Resolve Conflicts** screen. You will next be redirected to the **Review Artifacts** tab, where you can see a list of the changed files staged for commit. Here, you have the ability to preview the changes, review them, or edit the files before pushing them into your version control.
   * When starting a merge process in ARM, we recommend always enabling the **Review Artifacts** checkbox. It not only offers a workaround for manual code editing, but it also allows you to compare the code from the source branch and the destination branch before merging them.
8. Click on **Next Conflict** and repeat the steps until all the conflicts are resolved. The data for each conflict gets auto-saved once the user proceeds to either the **Prev** or **Next** conflict.
9. **Scenarios when the conflict blocks may not be saved:** The user is working on a conflict block and chooses the appropriate option to resolve it, but before clicking on either **Prev** or **Next Conflict** to autosave the data, the user selects another option, let's say the option to show 100/200/300/400/500 lines before and after the conflict. In such a case, the conflict block data will be automatically erased and the user will need to resolve such conflict block once again.
10. Click on the **Resolve conflict** option to resolve the conflicted file.

<figure><img src="../../../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

11. Repeat the steps for all other conflicted files in order to resolve them before you proceed to commit.
12. You can find the conflicted files moved to the **Merged Files** section. Here **CR** indicates **Conflicted Resolved** file&#x73;**, A** indicates **Added Files** to the destination branch and **M** denotes **Modified Files**.

<figure><img src="../../../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="371"><figcaption></figcaption></figure>

13. You will be directed to the next tab, **Profile Duplicates**.

### Profile Duplicates <a href="#profile-duplicates" id="profile-duplicates"></a>

This tab will list all duplicate entries for your profile/permission sets and you want to resolve them before resolving the conflict. For multiple entries, you have a provision to delete the entry that you no longer require (using the **X** icon) or to keep all entries as they are by default.

<figure><img src="../../../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Points to Note:**

1. If you receive the following error as highlighted below for duplicate entry, we suggest you download the file locally in such a case and search for any duplicity. Or, you can continue to commit directly by resolving the conflicting files (using the **Resolve Duplicates** button).



<img src="../../../../../.gitbook/assets/image (51) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original">

2. There can also be a situation where the files are improperly solved while resolving the conflicted files. This can lead to the malformation of the conflicted files. To resolve those, you need to download the file locally, work on the conflicted files using your merge tool, and make necessary changes to it. Then upload the same.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/image (52) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Review Artifacts <a href="#review-artifacts" id="review-artifacts"></a>

The **Review Artifacts** tab will appear in the merge conflict screen only if you enabled the **Review Artifacts** checkbox while creating the merge operation.

Under the **Review Artifacts** tab, you can see a list of the conflict resolved files staged for commit. This gives you the ability to preview the changes, review them or edit the files before pushing them into your version control. You can switch to the diff mode (using![](<../../../../../.gitbook/assets/image (53) (1) (1) (1) (1) (1) (1) (1).png>)icon) where you can compare the code from the source to the target branch before you merge them.

<figure><img src="../../../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (55) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Finally, click on the **Commit** button to commit the necessary changes to your target branch.

{% hint style="info" %}
**Important Note:** If there are multiple revisions as part of the merge, and if the same metadata file exists in more than 2 revisions, then such metadata will be displayed under **Review Artifact** regardless of conflicts. This is expected behavior from ARM.
{% endhint %}
