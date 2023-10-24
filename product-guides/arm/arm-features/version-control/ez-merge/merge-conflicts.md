# Merge Conflicts

### About Merge Conflicts <a href="#about-merge-conflicts" id="about-merge-conflicts"></a>

When you work in a team, you may come across a situation when somebody commits changes to a file you are currently working on. If these changes do not overlap (i.e. changes were made to different lines of code), the conflicting files are merged automatically. However, if the same lines were affected, your [version control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) system cannot randomly pick one side over the other and asks you to resolve the conflict.

### Resolving Merge Conflicts <a href="#resolving-merge-conflicts" id="resolving-merge-conflicts"></a>

There are 2 ways to resolve the conflicted files:

1. Download conflicted files locally or
2. Using merge conflict Inline editor.

#### Download Conflicted Files Locally <a href="#download-conflicted-files-locally" id="download-conflicted-files-locally"></a>

ARM has given a provision to the user to download the conflicted files in their local machine, resolve them locally and upload the same.

To do so,

1. Go to the **Commits** screen.&#x20;
2.  Search for your merge label that has a conflict. Click on the **Resolve Conflict** button.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777406311.png" alt=""><figcaption></figcaption></figure>
3.  The list of **conflicted files** or **merged files** will display on the next screen.&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777550676.png" alt="" width="563"><figcaption></figcaption></figure>
4.  To sort all listed items in ascending or descending order, click on![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777792566.png)icon.

    * ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777827272.png) will sort the listed items in ascending order
    * ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777869118.png) will sort the items in descending order

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628777746750.png" alt="" width="563"><figcaption></figcaption></figure>
5.  The **File Path view** displays a dynamic, hierarchical list of conflicted/merged items. The **Tree view** displays the parent-child relationships of the conflicted/merged files.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778067956.png" alt="" width="563"><figcaption></figcaption></figure>
6.  Now, select the conflicted files that you want to resolve and click on the **Download** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778197497.png)) icon.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778169370.png" alt="" width="375"><figcaption></figcaption></figure>
7.  Important Note:If there is a conflict related to file tree, then GIT shows that the file does not have any conflicts.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678949484102.png" alt="" width="375"><figcaption></figcaption></figure>
8. To proceed further, select the check box for the respective conflict, click on the **3 dots**, and then select if you want to use the **source** changes or the **destination** changes. Then you can go ahead and proceed with the next step to resolve the conflict.
9. When you click on the **Download** icon, a confirmation message box to include **.git** or **.svn folder** with **"Yes"** and **"No"** buttons will be displayed. If you select the **'Yes'** button only, then the conflicted files including the **.git** or **.svn folder** will be downloaded to your local machine in **zip** format.
10.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778254640.png" alt="" width="563"><figcaption></figcaption></figure>
11. Now, work on the conflicted files using your merge tool (example- TortoiseSVN, TortoiseGit) and make necessary changes to it.&#x20;
12. Click on the **Upload** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778295416.png)) icon and upload the resolved files. Make sure the file uploaded is in **zipped** format.
13. Finally, click on **Commit** to commit the changes in the destination branch.

#### Merge Conflict Inline Editor <a href="#merge-conflict-inline-editor" id="merge-conflict-inline-editor"></a>

The Merge inline editor helps users to resolve more complex merging conflicts directly from the ARM merge interface.

Important Note:Files over **10 MB** may not be resolved using Merge Inline Editor, therefore, in such a scenario, download the conflicted files on your local machine, resolve, and upload them again.

1. Go to the **Commits** screen and search for your merge label that has conflict. Click on the **Resolve Conflict** icon.
2. The list of conflicted files or merged files will display on the next screen.&#x20;
3. There is an easier method to resolve the conflicted files in one go. Select all the files and click on the 3 dots as shown in the image below and choose either of the criteria to resolve the files.
   1. **Use Source:** This option retains the revisions located in the source branch
   2.  **Use Destination:** This option retains the revisions located in the destination branch

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628778630379.png" alt="" width="563"><figcaption></figcaption></figure>
4. Or, click on a conflicted file to see its related conflict blocks. This tab will display the number of insertions and deletions to each metadata file. The lines highlighted in **GREEN** color indicate those are updated (added/modified) in the source branch and for **RED** color indicates those are updated (added/modified) in the destination branch. The highlighted lines are the modified lines.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1643980962843.png" alt="" width="563"><figcaption></figcaption></figure>

1. Navigate to other conflict blocks for the current conflict file by using the **Prev Conflict** or **Next Conflict** icon.
2.  Now, select the criteria by which you want to resolve the merge conflicts:

    1. **Dest. file**: This option retains the revisions located in the Destination Branch.
    2. **Src. file**: This option retains the revisions located in the Source Branch.
    3. **Block**: Select this option to resolve using either Source or Destination block. Here, two options will be auto-populated and you need to select either of the options mentioned below:
       1. **Destination**: The changes in the destination block will be used in the resulting merged file.&#x20;
       2. **Source**: The changes in the source block will be used in the resulting merged file.
    4. **Block from ‘Dest.’ before ‘Src.’**: This allows you to use both the blocks; first changes in the **destination** block and later **source** block. The changes are used in the resulting **Merged** file.
    5. **Block from ‘Src.’ before ‘Dest.’**: This allows you to use both the blocks; first changes in the **source** block and later **destination** block. The changes are used in the resulting **Merged** file.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1643981055335.png" alt=""><figcaption></figcaption></figure>
3. **Troubleshooting:**\
   A. Do I have a provision to edit the inline code if the above merge criteria fail to resolve the merge conflicts?\
   In rare circumstances, your merge conflict may not be resolved by the merge criteria that ARM offers. Additionally, inline editing of the code is not supported by ARM. In such a case, we advise initiating the merge operation while keeping the checkbox for **Review Artifacts** enabled on the **EZ-Merge** screen.\
   \
   Choose any of the merging criteria that ARM offers on the **Resolve Conflicts** screen. You will next be redirected to the **Review Artifacts** tab where you can see a list of the changed files staged for commit. Here, you have the ability to preview the changes, review them or edit the files before pushing them into your version control.\
   \
   When starting a merge process in ARM, we recommend always enabling the **Review Artifacts** checkbox. It not only offers a workaround for manual code editing, but it also allows you to compare the code from the source branch and the destination branch before merging them.
4. Click on **Next Conflict** and repeat the steps until all the conflicts are resolved. The data for each conflict gets auto-saved once the user proceeds to either the **Prev** or **Next** conflict.**Scenarios when the conflict blocks may not be saved:**The user is working on a conflict block and chooses the appropriate option to resolve it, but before clicking on either **Prev** or **Next Conflict** to autosave the data, the user selects another option, let's say the option to show 100/200/300/400/500 lines before and after the conflict. In such a case, the conflict block data will be automatically erased and the user will need to resolve such conflict block once again.
5.  Click on the **Resolve conflict** option to resolve the conflicted file.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1643981097580.png" alt="" width="563"><figcaption></figcaption></figure>
6. Repeat the steps for all other conflicted files in order to resolve them before you proceed to commit.
7. You can find the conflicted files moved to the **Merged Files** section. Here **CR** indicates **Conflicted Resolved** files**, A** indicates **Added Files** to the destination branch and **M** denotes **Modified Files**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628779923271.png" alt="" width="375"><figcaption></figcaption></figure>

1. You will be directed to the next tab, **Profile Duplicates**.

#### Profile Duplicates <a href="#profile-duplicates" id="profile-duplicates"></a>

This tab will list all duplicate entries for your profile/permission sets and you want to resolve them before resolving the conflict. For multiple entries, you have a provision to delete the entry that you no longer require (using the **X** icon) or to keep all entries as they are by default.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628780524891.png" alt="" width="563"><figcaption></figcaption></figure>

**Important Points to Note:**&#x20;

1.  If you receive the following error as highlighted below for duplicate entry, we suggest you download the file locally in such a case and search for any duplicity. Or, you can continue to commit directly by resolving the conflicting files (using the **Resolve Duplicates** button).

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628783082099.png" alt="" width="375"><figcaption></figcaption></figure>
2. There can also be a situation where the files are improperly solved while resolving the conflicted files. This can lead to the malformation of the conflicted files. To resolve those, you need to download the file locally, work on the conflicted files using your merge tool, and make necessary changes to it. Then upload the same.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628783241779.png" alt="" width="563"><figcaption></figcaption></figure>

#### Review Artifacts <a href="#review-artifacts" id="review-artifacts"></a>

The **Review Artifacts** tab will appear in the merge conflict screen only if you enabled the **Review Artifacts** checkbox while creating the merge operation.

Under the **Review Artifacts** tab, you can see a list of the conflict resolved files staged for commit. This gives you the ability to preview the changes, review them or edit the files before pushing them into your version control. You can switch to the diff mode (using ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628781966199.png) icon) where you can compare the code from the source to the target branch before you merge them.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628781743757.png" alt="" width="563"><figcaption></figcaption></figure>

![switch to diff mode](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1628781922802.png)

Finally, click on the **Commit** button to commit the necessary changes to your target branch.

Important Note:

If there are multiple revisions as part of the merge, and if the same metadata file exists in more than 2 revisions, then such metadata will be displayed under **Review Artifact** regardless of conflicts. This is expected behavior from ARM.
