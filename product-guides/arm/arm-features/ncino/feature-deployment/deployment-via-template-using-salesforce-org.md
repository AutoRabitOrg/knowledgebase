# Deployment via Template using Salesforce Org

This section is all about deploying the [nCino](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) data via the salesforce org dataset.

1. Hover your mouse over the **nCino** module and click on the **Deployment History** option.

<figure><img src="../../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="202"><figcaption></figcaption></figure>

2. Click on the **Feature Deployment** button.

<figure><img src="../../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, give the process a **name** and a brief **description**.
4. In the **SOURCE** section, select **Deployment From** as **Template using Salesforce Org**.
5. Select the template **Feature Type** i.e, Standard or Community Template.
6. Select your **Template** and its **Version** of it.
7. Select your **Source Salesforce Org**.
8. The object configuration section will render the selected objects and apply filters and mappings based on your template selection.

<figure><img src="../../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Choose your **Destination Environment**. It can be your target salesforce org or commit to your version control branch.
10. To deploy into a salesforce org, select the **Deploy To** checkbox and choose your **Destination Org**. To commit to a branch, select the **Commit To** box, enter your **Repository/Branch** details, and **comment** (if any).

<figure><img src="../../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: For commits, the features will get committed to the default location in your version control branch. By default, the location is set to the dataset.
{% endhint %}

11. There are various options that you can configure to your objects before you proceed with deployment or commit:

    * Applied Mappings
    * Sorting (only if the 'Commit to' checkbox is selected)
    * Applied Filters

    <figure><img src="../../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Mappings <a href="#applied-mappings" id="applied-mappings"></a>

In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values in a field marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

* In the **Source** field: Select your source field whose values will be populated in the destination External Id field.
* In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

<figure><img src="../../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** (About Applied Mappings):

1. Since the source for Deployment via **Template** or **Version Control** is a CSV file rather than a Salesforce Org, all fields, regardless of the External ID supported, will be fetched and displayed in the **Source** column. However, the relevant fields will be shown under the Destination column since the target org is a salesforce org.
2. AutoRABIT External ID fields are not supported for the **Upsert** operation.
{% endhint %}

#### Sorting <a href="#sorting" id="sorting"></a>

This new feature allows you to sort fields for nCino objects while committing. Based on the sorting order set, the record order in the JSON files will get fetched. The users will be provided a default sorting order that can be changed. **XXXXX\_lookupkey\_\_c** is the most preferred field for sorting, and that would be the default field. If this field is not present, the **Name** for _custom settings_ and **Id** for _non-custom settings_ would be selected.

<figure><img src="../../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

For the objects with sorting fields opted, the sorting icon gets changed.

<figure><img src="../../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Filters <a href="#applied-filters" id="applied-filters"></a>

Such filters will be displayed here if any filter is applied to the objects. You can edit the already applied filter (if required) using **Edit Filter.**

<figure><img src="../../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Deployment Option <a href="#deployment-option" id="deployment-option"></a>

Based on your destination selection, you will have different deployment buttons to choose from:

1. **Create Dataset:** Create a dataset from your Salesforce Org
2. **Create Dataset & Deploy:** Create a dataset and deploy it to your Salesforce Org
3. **Create Dataset & Commit:** Create a dataset and commit to a Version Control Branch
4. **Create Dataset Commit & Deploy:** Create a dataset and proceed for both commit and deployment.

<figure><img src="../../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For deploying to the destination org, you will find the list of deployment criteria you can opt for before proceeding.&#x20;

**Deployment Filters**

1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
2. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment
3. **Insert/update with Null Values:** This will either insert or update record field values with null in the destination org (if the value is null in the source org)
4.  **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.

    <figure><img src="../../../../../.gitbook/assets/Feature Deployment - Via Temp Using SF ORG.png" alt=""><figcaption></figcaption></figure>

Click **OK** to complete the feature deployment process.

You'll be redirected to the [Feature Deployment Summary](feature-deployment-summary.md) page, where you can view detailed deployment reports or re-deploy the nCino objects to your Salesforce Org/Version Control once again.
