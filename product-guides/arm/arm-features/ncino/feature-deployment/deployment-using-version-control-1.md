---
hidden: true
---

# Copy of Deployment Using Version Control

This article describes the process of deploying the nCino data via the Salesforce ORG dataset

1. Feature Deployment can be triggered in the following ways:
   1. Click on the "Create" button to observe the options to select the "Feature Deployment" as option
2.  Click on the "Deployment History" under the nCino tab to access the "Create feature deployment"



    <figure><img src="../../../../../.gitbook/assets/1.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
3.  Upon clicking on the **"Create Feature Deployment" or** selecting the **"Feature Deployment,"** a Source Type screen will appear—choose from the available options to proceed.

    <figure><img src="../../../../../.gitbook/assets/2 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
4.













































































This section is all about deploying the nCino data using [Version Control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/)

1. Hover your mouse over the [**nCino** module](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) and click on the **Deployment History** option.

<figure><img src="../../../../../.gitbook/assets/image (22) (1) (1) (1) (1).png" alt="" width="202"><figcaption></figcaption></figure>

2. Click on the **Feature Deployment** button.

<figure><img src="../../../../../.gitbook/assets/image (24) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, give the process a **name** and a brief **description**.
4. In the **SOURCE** section, select **Deployment From** as **'Version Control.'**
5. Select your **version control** type.
6. Select your **repository** and **branch**.
7.  Select the deployment type. There are three options to choose from:

    * **Entire Branch:** This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **template** and **version when selecting** the entire branch option.

    <figure><img src="../../../../../.gitbook/assets/image (25) (1) (1) (1) (1).png" alt="" width="470"><figcaption></figcaption></figure>

    * **Single Revision:** This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

    <figure><img src="../../../../../.gitbook/assets/image (26) (1) (1) (1) (1).png" alt="" width="454"><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (28) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Revision Range:** This option allows you to specify a commit range from which the revisions are to be deployed.

    <figure><img src="../../../../../.gitbook/assets/image (29) (1) (1) (1).png" alt="" width="434"><figcaption></figcaption></figure>
8. The object configuration section will render the selected objects and apply filters and mappings based on your selection.

<figure><img src="../../../../../.gitbook/assets/image (30) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Choose your **target org**.

<figure><img src="../../../../../.gitbook/assets/image (31) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. There are various options that you can configure to your objects before you proceed with deployment:

    * Applied Mappings
    * Applied Filters

    <figure><img src="../../../../../.gitbook/assets/image (32) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Mapping <a href="#applied-mapping" id="applied-mapping"></a>

In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values in a field marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

In the **Source** field: Select your source field whose values will be populated in the destination External Id field.

In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

<figure><img src="../../../../../.gitbook/assets/image (33) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note (About Applied Mappings):**

1. If there is no Lookup key and the name is set to External ID, AutoRABIT is still supported.
2. Because the source for this is a CSV extract and not a salesforce org, all fields from the source sandbox will be fetched, regardless of the External ID in the **Source** column, whereas the source for Destination is a salesforce org.
{% endhint %}

#### Applied Filters <a href="#applied-filters" id="applied-filters"></a>

Such filters will be displayed here if any filter is applied to the objects.

<figure><img src="../../../../../.gitbook/assets/image (34) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: The dataset is already prepared at the time of the commit, so you can’t edit it at this point. However, if you like to edit the filter, use the feature: [Deployment via Version Control using Salesforce org](deployment-via-version-control-using-salesforce-org.md)
{% endhint %}

Click on **Deploy** to proceed to the next screen. The next screen will display the list of deployment criteria that you can opt for before proceeding with deployment.

#### Deployment Settings <a href="#deployment-settings" id="deployment-settings"></a>

1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
2. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment
3. **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in a go from the source and destination org.
4. **Insert/update with Null Values:** This will either insert or update record field values with null (if the value is null in source org) in destination org.
5. **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.

<figure><img src="../../../../../.gitbook/assets/image (35) (1) (1) (1).png" alt="" width="510"><figcaption></figcaption></figure>

Click **OK** to complete the feature deployment process.

You'll be redirected to the [Feature Deployment Summary](feature-deployment-summary.md) screen, where you can view detailed deployment reports or re-deploy the nCino objects to your Salesforce Org once again.
