# Deployment Using Feature Migration Template

This article will walk you through deploying nCino data using the Feature Migration template. If you're referring to this article for the first time, please navigate to [Feature Migration Template](../feature-migration/create-a-feature-migration-template.md), which deals with the step-by-step procedure of creating a fresh migration template in AutoRABIT.&#x20;

1. Hover your mouse over the [**nCino** module](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) and click on the **Deployment History** option.

<figure><img src="../../../../../.gitbook/assets/image (74) (1).png" alt="" width="202"><figcaption></figcaption></figure>

2. Click on the **Feature Deployment** button.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, give the process a **name** and a brief **description**.
4. In the **Source** section, select **Deployment From** as **Template**.
5. Select the template **Feature Type,** i.e., Standard or Community Template.
6. Select your **template** and its **version** of it.
7. Based on your template selection, the object configuration section will render the selected objects and apply filters and mappings.

<figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Choose your **destination environment**. It can be your target salesforce org or commit to your version control branch.
9. To deploy into a Salesforce Org, select the **Deploy To** checkbox and choose your **Destination Org**. To commit to a branch, select the **Commit To** box, enter your **Repository/Branch** details, and **comment** (if any).

<figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: For commits, the features will get committed to the default location in your version control branch. By default, the location is set to the dataset.
{% endhint %}

10. There are various options that you can configure to your objects before you proceed with deployment or commit:

    * Applied Mappings
    * Sorting (only if the 'commit' checkbox is selected)
    * Applied Filters

    <figure><img src="../../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Mappings <a href="#applied-mappings" id="applied-mappings"></a>

In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values contained in a field that's marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

* In the **Source** field: Select your source field whose values will be populated in the destination External Id field.
* In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

<figure><img src="../../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note (About Applied Mappings)**:

1. Since the source for Deployment via **Template** or **Version Control** is a CSV file rather than a Salesforce Org, all fields, regardless of the External ID supported, will be fetched and displayed in the **Source** column. However, the relevant fields will be shown under the Destination column since the target org is a salesforce org.
2. AutoRABIT External ID fields are not supported for the **Upsert** operation.
{% endhint %}

#### Sorting <a href="#sorting" id="sorting"></a>

This new feature allows you to sort fields for nCino objects while committing. Based on the sorting order set, the record order in the JSON files will get fetched. The users will be provided a default sorting order that can be changed. **XXXXX\_lookupkey\_\_c** is the most preferred field for sorting, and that would be the default field. If this field is not present, the **Name** for _custom settings_ and **Id** for _non-custom settings_ would be selected.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

For the objects with sorting fields opted, the sorting icon gets changed.

<figure><img src="../../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Filters <a href="#applied-filters" id="applied-filters"></a>

Such filters will be displayed here if any filter is applied to the objects.

<figure><img src="../../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: At the time of template creation, the filter is applied to your object, so it can't be edited.&#x20;
{% endhint %}

#### Deployment Option <a href="#deployment-option" id="deployment-option"></a>

Based on your destination selection, you will have different deployment buttons to choose from:

* **Deploy:** Deploying to the salesforce org only
* **Commit:** Committing to the version control branch only
* **Commit & Deploy:** Committing and deployment together.

<figure><img src="../../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For deploying to the destination org, you will find the list of deployment criteria you can opt for before proceeding.&#x20;

**Deployment Filters**

1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment.
2. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment.
3. **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in a go from the source and destination org.
4. **Insert/update with Null Values:** This will either insert or update record field values with null in the destination org (if the value is null in the source org).
5. **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.

<figure><img src="../../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="510"><figcaption></figcaption></figure>

Click **OK** to complete the feature deployment process.

You'll be redirected to the following:

* [Commit History](../feature-commits.md) page if you have opted for the commit process to run.
* [Feature Deployment Summary](feature-deployment-summary.md) page if you have opted for deployment. It is where you can view detailed deployment reports or re-deploy the nCino objects to your salesforce org/version control once again.
