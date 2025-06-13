---
hidden: true
---

# Copy of Deployment via Version Control using Salesforce Org

This section covers the deployment of **nCino metadata and data** through **version control**, leveraging the **Salesforce dataset** for streamlined and traceable delivery.

1. The "Feature Deployment" can be triggered in the following way
   1.  Click on the "Create" drop-down to observe the options to select the "Feature Deployment" as option



       <figure><img src="../../../../../.gitbook/assets/1 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>


2.  Click on the "Deployment History" under the nCino tab to access the "Create feature deployment"



    <figure><img src="../../../../../.gitbook/assets/1.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
3.  Upon clicking on the **"Create Feature Deployment" or** selecting the **"Feature Deployment," the** Source Type screen will appear—choose from the available options to proceed.

    <figure><img src="../../../../../.gitbook/assets/2 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
4.  Continue to input the fields on the screen with the required inputs

    <figure><img src="../../../../../.gitbook/assets/3- Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
5. The following fields are available on the screen to from:
   1. **Label name:** Input label name of the deployment here
   2. **Description:** Enter a description that suits the deployment
   3. **Source ORG**: Select the source org here
   4. **Version Control**: Select the version control type here
   5. **Repository**: Select the repository here
   6. **Branch**: Select the required branch here
   7. **VC Fetch Type**: Select the option to perform the deployment.&#x20;
      1. The following options are available at "VC Fetch Type":
         1. Entire Branch&#x20;
         2.  Single Revision

             <figure><img src="../../../../../.gitbook/assets/2.0 - Deploy Using SF and VC (1).png" alt=""><figcaption></figcaption></figure>
      2.  **Entire Branch**: This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **feature/template** and **version when selecting** the entire branch option.

          <figure><img src="../../../../../.gitbook/assets/3- Deploy Using SF and VC (2).png" alt=""><figcaption></figcaption></figure>
      3.  **Single Revision**: This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

          <figure><img src="../../../../../.gitbook/assets/4 - Deploy Using SF and VC (1).png" alt=""><figcaption></figcaption></figure>

          <figure><img src="../../../../../.gitbook/assets/4.0 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
      4.  Observe the values selected at the revision

          <figure><img src="../../../../../.gitbook/assets/4.1 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
6. Based on the selected revisions, the respective "feature versions" will be displayed.
7.  Click on the "Next" to continue to the "Destination" section of the Feature Deployment flow

    <figure><img src="../../../../../.gitbook/assets/5 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
8. You can configure several options for your objects before proceeding with a deployment or commit, including:
   * **External Id Mappings**
   * **Applied Filters**
9.  **External ID Mappings**

    This section allows you to use an **External ID** instead of a Salesforce **Record ID** to establish relationships between records during an **Upsert** operation.\
    For example, if **Object B** has a lookup to **Object A**, you can reference a field on Object A marked as an _External ID_ to relate Object B records to the correct Object A records.

    * **Source Field**: Select the source field whose values will be used to match and populate the destination’s External ID field.
    * **Destination Field**: Choose a field from the destination org that is marked as an External ID and holds **unique values** across all records.

    <figure><img src="../../../../../.gitbook/assets/5.0 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
#### **Important Note on External ID Mappings**

When deploying via **Template** or **Version Control**, the **source** is a **CSV file**, not a Salesforce Org. As a result:

* **All fields** from the CSV—regardless of External ID designation—will appear in the **Source** column.
* In contrast, only **valid External ID fields** from the **Salesforce destination org** will be shown in the **Destination** column for selection.

Please note that **AutoRABIT-defined External ID fields** are **not supported** for the **Upsert** operation.
{% endhint %}

10. **Applied Filters**: If any filters have been applied to the objects, they will be displayed in this section. You can modify an existing filter at any time by selecting **Edit Filter**.



    <figure><img src="../../../../../.gitbook/assets/6 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
11. On completing the required selection click next to continue to the "Job Settings" section of the "Feature Deployment" flow.
12. Observe the following screenshot for the "Deployment Options" available on this section:

    <figure><img src="../../../../../.gitbook/assets/7 - Deploy Using SF and VC (2).png" alt=""><figcaption></figcaption></figure>

* **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
* **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in a go from the source and destination org.
* **Use UTF-8 file encoding for file read and write operations:** Use **UTF-8** as the internal representation for all string data. Text is automatically transcoded between the local encoding and UTF-8 when reading from or writing to files.
  * **Enable UTF-8** if your data contains **only English alphabets**.
  * **Disable UTF-8** if your data includes **non-English characters** to avoid encoding issues.
  * UTF-8 should be **enabled by default**, aligning with Salesforce’s recommended encoding standards.
* **Automap User/Owner Data:**&#x20;
* **Disable Validation Rules:** Select this option to temporarily deactivate validation rules on objects included in the deployment. This helps ensure smoother deployments without interruptions caused by rule enforcement.
* **Insert/Update with Null Values:** When enabled, this option allows fields with `null` values in the source org to be inserted or updated as `null` in the destination org. It ensures data consistency by reflecting blank or cleared values during migration.
* **Enable Rollback:** Enable this option to allow rollback of the deployment, if needed. Only components explicitly marked for **“Rollback”** during deployment will be eligible for rollback after completion.

13. Based on your destination selection, you will have different deployment options to choose from:
    1. **Create Dataset:** Create a dataset from your Salesforce Org
    2. **Create Dataset Commit & Deploy:** Create a dataset and proceed for both commit and deployment.
14. Clicking on ether of the deployment options available above, you will be redirected to the "Deployment History" page.

    <figure><img src="../../../../../.gitbook/assets/8 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>



































































This section is about deploying the nCino metadata and data via version control using the Salesforce dataset.

1. Hover your mouse over the [nCino ](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/)module and click on the **Deployment History** option.   &#x20;

<figure><img src="../../../../../.gitbook/assets/image (38) (1) (1) (1) (1).png" alt="" width="202"><figcaption></figcaption></figure>

2. Click on the **Feature Deployment** button.

<figure><img src="../../../../../.gitbook/assets/image (39) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, give the process a **name** and a brief **description** of it.
4. In the **Source** section, select Deployment From as [**Version Control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) **using Salesforce Org**.
5. Select your **Version Control** type, **Repository**, and **Branch**.
6.  Select the **deployment type**.

    * **Entire Branch:** This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **template** and **template version** when you select the entire branch option.

    <figure><img src="../../../../../.gitbook/assets/image (40) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Single Revision:** This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

    <figure><img src="../../../../../.gitbook/assets/image (41) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (42) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. Select your **Source Salesforce Org**.
8. Based on your template selection, the object configuration section will render the selected objects and apply filters and mappings.

<figure><img src="../../../../../.gitbook/assets/image (43) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Choose your **Destination Environment**.

<figure><img src="../../../../../.gitbook/assets/image (44) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. There are various options that you can configure to your objects before you proceed with deployment or commit:

    * Applied Mappings
    * Applied Filters

    <figure><img src="../../../../../.gitbook/assets/image (45) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Applied Mappings <a href="#applied-mappings" id="applied-mappings"></a>

In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A** you can use the values contained in a field that's marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

In the **Source** field: Select your own source field whose values will get populated in the destination External Id field.

In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

<figure><img src="../../../../../.gitbook/assets/image (46) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note (About Applied Mappings)**:

1. Since the source for Deployment via **Template** or **Version Control** is a CSV file rather than a Salesforce Org, all fields, regardless of the External ID supported, will be fetched and displayed in the **Source** column. However, the relevant fields will be shown under the Destination column since the target org is a salesforce org.
2. AutoRABIT External ID fields are not supported for the **Upsert** operation.
{% endhint %}

#### Applied Filters <a href="#applied-filters" id="applied-filters"></a>

Such filters will be displayed here if any filter is applied to the objects. You can edit the already applied filter (if required) using **Edit Filter.**

<figure><img src="../../../../../.gitbook/assets/image (47) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Deployment Option <a href="#deployment-option" id="deployment-option"></a>

Based on your destination selection, you will have different deployment buttons to choose from:

1. **Create Dataset:** Create a dataset from your Salesforce Org. On selection, you will be redirected to the [Commits History](../../version-control/ez-commits/commits-summary.md) screen.
2. **Create Dataset & Deploy:** Create a dataset and deploy it to your Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (37) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For deploying to the destination org, you will find the list of deployment criteria you can opt for before proceeding.

**Deployment Filters**

1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
2. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment
3. **Use Bulk API** (Batch API will be used if the option is not enabled): You can transfer bulk records in a go from the source and destination org
4. **Insert/update with Null Values:** This will either insert or update record field values with null (if the value is null in Source Org) in Destination Org
5. **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.

<figure><img src="../../../../../.gitbook/assets/image (36) (1) (1) (1) (1).png" alt="" width="510"><figcaption></figcaption></figure>

Click **OK** to complete the feature deployment process. You'll be redirected to the [Feature Deployment Summary](feature-deployment-summary.md) page, where you can view detailed deployment reports or re-deploy the nCino objects to your Salesforce Org once again.
