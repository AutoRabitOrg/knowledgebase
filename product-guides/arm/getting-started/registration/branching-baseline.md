# Branching Baseline

{% hint style="info" %}
**Note:** This article is for the **Org Administrator** in particular. The actions discussed in the article will not be available to general users. &#x20;
{% endhint %}

### Branching Baseline: Overview <a href="#branching-baseline-overview" id="branching-baseline-overview"></a>

Components are retrieved and committed from a Salesforce org to a version control branch using **Branching Baseline**. This helpful feature can deal with a lot of metadata and is ideal for (but not limited to) the following two scenarios:

* Branching Baseline will sync the branch to its mapped Salesforce org so that they are in sync.
* If a user creates a new branch and wishes to update it with an existing Salesforce Org, they can do so.

### Execute a Branching Baseline commit <a href="#execute-a-branching-baseline-commit" id="execute-a-branching-baseline-commit"></a>

1. Log into your ARM account.
2. Hover your mouse over the **`Admin`** module and click on **`Branching Baseline`**.

<figure><img src="../../../../.gitbook/assets/image (25) (3).png" alt="" width="217"><figcaption></figcaption></figure>

3. From the **`Branching Baseline`** screen, click on **`New Branching Baseline`**.

<figure><img src="../../../../.gitbook/assets/image (26) (3).png" alt="" width="563"><figcaption></figcaption></figure>

4.  The **`Branching Baseline`** screen appears where you need to fill in the details listed below:

    * Give a **`Label Name`**.
    * Select your **`Salesforce Org`** as the source of the commit.
    * Select your **`Repository`** and **`Branch`** to which you like to commit code.

    <figure><img src="../../../../.gitbook/assets/image (27) (3).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: For Version Control registered in the **SFDX** structure, specify the **Source Folder** from where the metadata will get fetched. If you cannot view the source folder in the drop-down, the source folder is not listed in the **Package Directory** under the **sfdx-project.json** file in your local directory. For a detailed procedure of adding the source folder in the Package Directory, do refer to the article: [Salesforce DX metadata format](../../salesforce-dx-metadata-format.md)
{% endhint %}

5. **`Exclude baseline managed package changes:`** This option will ensure that only unpackaged components are retrieved into your version control branch.&#x20;

{% hint style="info" %}
**Important Note**: If a managed package is installed in a Salesforce org on a date, but a different date is given on the CI Job created, then the installed managed package numbers are also loaded. We can exclude baseline managed package changes to skip those installed managed packages. As all installed packages in a Salesforce org come from a Managed source (AppExchange, etc.), such managed components can be excluded from a baseline operation.
{% endhint %}

6. **`Delete existing metadata and commit new changes:`** This option will delete all existing metadata and commit all the metadata members from the Salesforce org to the Version Control repository, thereby deleting the existing contents of a branch before the Baseline operation. In short, if you want zero components in your repository, then this option will allow you to delete all the existing metadata and commit all the metadata members from the salesforce org to the version control repository.
7. **`Use Bulk Retrieve:`** This option retrieves the components in batches. The users need to specify the batch size for Profile components and other components in which they will get retrieved.
8. **`Specify the batch size for both profile and remaining components to retrieve records:`** You need to specify for profile components and other components in which ARM will retrieve. So the default size for the profile is **`500,`** and for other components is **`2000`**. You can modify it as per your requirement. Bulk retrieval helps run large jobs that would exceed normal processing limits – you can deploy up to 10000 files at once or a maximum size of 14Mb. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is the best option.
9. Click **`OK`**. A notification pops up displaying that the branching baseline operation is initiated.
10. You will be redirected to the **`Branching Baseline`** summary page, where you can find the status of your branching baseline operation recently created. The status column will indicate whether your baseline operation has been completed or failed.

{% hint style="info" %}
**Point to Note**: Branching baseline commits for the **SVN repository** may take **10 minutes** to complete.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (28) (3).png" alt="" width="334"><figcaption></figcaption></figure>

#### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (29) (3).png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Info:`** This will give the info about the Salesforce Org and the Version Control Repository/ Branch selected for the Branching Baseline operation.
2. **`Revision:`** View the revision generated at the Version Control along with the filename status. You can even download the report if required.
3. **`Log:`** View the execution log of the Branching Baseline operation.&#x20;
4. **`Status:`** View the status of the Branching Baseline operation

| Status                                                                                 | Description                                     |
| -------------------------------------------------------------------------------------- | ----------------------------------------------- |
| <img src="../../../../.gitbook/assets/image (30) (3).png" alt="" data-size="original"> | The branching baseline operation is in progress |
| ![](<../../../../.gitbook/assets/image (31) (3).png>)                                  | The branching baseline is completed             |
| ![](<../../../../.gitbook/assets/image (32) (3).png>)                                  | The baseline operation got failed               |

5. **`Run:`** This option allows you to run your branching baseline operation at a later stage. It iterates a new baseline operation to update your branch with the latest metadata from your Salesforce Org.
6. **`Delete:`** Deletes the branching baseline operation when you don’t require one, like older ones. Once deleted, this cannot be undone.
