# Deployment Using Version Control



This article describes the process of deploying nCino data via Version Control.

1. Feature Deployments can be triggered in the two following ways:
   1.  Click on the "Create" drop-down to see the options and select the "Feature Deployment" as an option.

       <figure><img src="../../../../../.gitbook/assets/1 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
2.  Click on the "Deployment History" under the nCino tab to access "Create feature deployment."



    <figure><img src="../../../../../.gitbook/assets/1.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
3.  Upon clicking on the **"Create Feature Deployment"** or selecting the **"Feature Deployment,"** the Source Type screen will appear—choose from the available options to proceed.

    <figure><img src="../../../../../.gitbook/assets/2 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
4.  Continue to input the fields on the screen with the required inputs

    <figure><img src="../../../../../.gitbook/assets/3 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
5. The following fields are available on the screen to from:
   1. **Label name:** Enter a label name for the deployment.
   2. **Description:** Enter a description that suits the deployment.
   3. **Version Control**: Select the version control type.
   4. **Repository**: Select the repository.
   5. **Branch**: Select the required branch.
   6. **VC Fetch Type**: Select the option to perform the deployment.&#x20;
      1. The following options are available at "VC Fetch Type":
         1. Entire Branch&#x20;
         2. Single Revision
         3.  Revision Range



             <figure><img src="../../../../../.gitbook/assets/4 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
      2.  **Entire Branch**: This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **feature/template** and **version** when selecting the entire branch option.

          <figure><img src="../../../../../.gitbook/assets/5 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
      3.  **Single Revision**: This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

          <figure><img src="../../../../../.gitbook/assets/5.1 - Deployment From Version Control (1).png" alt=""><figcaption></figcaption></figure>
      4. **n Range**: This option allows you to specify a commit range from which the revisions are to be deployed.
      5.

          <figure><img src="../../../../../.gitbook/assets/5.2 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
      6.
      7. "Deploy To" field
6.

    <figure><img src="../../../../../.gitbook/assets/6 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Change hint typeCommentShare feedback on the editor**Important Note**: The dataset is already prepared at the time of the commit, so you can’t edit it at this point. However, if you like to edit the filter, use the feature: [Deployment via Version Control using Salesforce or](https://app.gitbook.com/o/vIHQCTOOUDcNoPic3AQi/s/9vAxMuDrkUkB4OXlH9CL/~/changes/2715/product-guides/arm/arm-features/ncino/feature-deployment/deployment-via-version-control-using-salesforce-org)
{% endhint %}

9. The Object Configuration section dynamically displays the selected objects and applies the corresponding filters and mappings based on the selections.
10. The "External Id Mappings" can be configured accordingly.

    <figure><img src="../../../../../.gitbook/assets/6.0 - Deployment From Version Control (1).png" alt=""><figcaption></figcaption></figure>
11. In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values in a field marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

    In the **Source** field: Select your source field whose values will be populated in the destination External Id field.

    In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

    <figure><img src="../../../../../.gitbook/assets/6.1 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note (About Applied Mappings):**

1. If there is no Lookup key and the name is set to External ID, AutoRABIT is still supported.
2. Because the source for this is a CSV extract and not a Salesforce org, all fields from the source sandbox will be fetched, regardless of the External ID in the **Source** column, whereas the source for Destination is a Salesforce org.
{% endhint %}

12. On completing the required selection, click 'Next' to continue to the "Job Settings" section of the "Feature Deployment" flow.
13. Observe the following screenshot for the "Deployment Options" available on this section:

    <figure><img src="../../../../../.gitbook/assets/7 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>

* **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment.
* **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records all at one time from the source and destination org.
* **Use UTF-8 file encoding for file read and write operations:** Use **UTF-8** as the internal representation for all string data. Text is automatically transcoded between the local encoding and UTF-8 when reading from or writing to files.
  * **Enable UTF-8** if your data contains **only English alphabets**.
  * **Disable UTF-8** if your data includes **non-English characters** to avoid encoding issues.
  * **UTF-8** should be **enabled by default**, aligning with Salesforce’s recommended encoding standards.
* **Automap User/Owner Data:**&#x20;
  * **Disable Validation Rules:** Select this option to temporarily deactivate validation rules on objects included in the deployment. This helps ensure smoother deployments without interruptions caused by rule enforcement.
  * **Insert/Update with Null Values:** When enabled, this option allows fields with `null` values in the source org to be inserted or updated as `null` in the destination org. It ensures data consistency by reflecting blank or cleared values during migration.
  * **Enable Rollback:** Enable this option to allow rollback of the deployment, if needed. Only components explicitly marked for **“Rollback”** during deployment will be eligible for rollback after completion.

14. **Preview**: All the configurations made during the deployment creation can be seen here, with different deployment options.

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-05-09 at 8.52.09 PM.png" alt=""><figcaption></figcaption></figure>
15. Based on your destination selection, you will have different deployment options to choose from:
    1. **Create Dataset:** Create a dataset from your Salesforce Org.
    2. **Create Dataset Commit & Deploy:** Create a dataset and proceed for both commit and deployment.
16. Clicking on ether of the deployment options available above, you will be redirected to the "Deployment History" page.

    <figure><img src="../../../../../.gitbook/assets/9 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>







