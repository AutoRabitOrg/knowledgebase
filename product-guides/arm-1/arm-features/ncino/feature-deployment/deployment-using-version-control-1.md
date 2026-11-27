# Deployment Using Version Control

This article describes the process of deploying nCino data via Version Control.

1. Feature Deployments can be triggered in the two following ways:
   1.  Click on the "Create" drop-down to see the options and select the "Feature Deployment" as an option.

       <figure><img src="../../../../../.gitbook/assets/1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
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
   6.  **VC Fetch Type**: Select the option to perform the deployment.

       1. The following options are available at "VC Fetch Type":
          1. Entire Branch
          2. Single Revision
          3.  Revision Range

              <figure><img src="../../../../../.gitbook/assets/4 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
       2.  **Entire Branch**: This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **feature/template** and **version** when selecting the entire branch option.

           <figure><img src="../../../../../.gitbook/assets/5 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
       3.  **Single Revision**: This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

           <figure><img src="../../../../../.gitbook/assets/5.1 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
       4. **Revision Range**: This option allows you to specify a commit range from which the revisions are to be deployed.

       ```
       <figure><img src="../../../../../.gitbook/assets/5.2 - Deployment From Version Control.png" alt=""><figcaption></figcaption></figure>
       ```
6.  In the nCino Deployment **Source** step, users can sort the **Feature** and **Version** lists for the selected repository and branch.

    1.  The user opens the **Feature** dropdown and clicks the **Sort** icon beside **Search**.

        <figure><img src="../../../../../.gitbook/assets/1 (33).png" alt=""><figcaption></figcaption></figure>
    2.  The user selects the required sort order:

        | Option                 | Description                                   |
        | ---------------------- | --------------------------------------------- |
        | **Newest**             | Displays the newest items first.              |
        | **Oldest**             | Displays the oldest items first.              |
        | **Alphabetical - A-Z** | Sorts names in ascending alphabetical order.  |
        | **Alphabetical - Z-A** | Sorts names in descending alphabetical order. |
    3.  After selecting a feature, the user opens the **Version** dropdown and uses its **Sort** icon to arrange the available versions.

        <figure><img src="../../../../../.gitbook/assets/2 (33).png" alt=""><figcaption></figcaption></figure>

    A checkmark indicates the selected sort option.
7. **Destination:** Select the destinations onto which the data can be deployed to.
   1. **Deploy To:** lists the ORGs that can be selected for deployment.
   2. **Commit To:** Lists the branches selected for deployment to "Version Control".
8.

```
<figure><img src="../../../../../.gitbook/assets/FD - Deploy from temp config.png" alt=""><figcaption></figcaption></figure>
```

{% hint style="info" %}
**Note**: The dataset is already prepared at the time of the commit, so you can’t edit it at this point. However, if you like to edit the filter, use the feature: [Deployment via Version Control using Salesforce org](../../../../arm/arm-features/ncino/feature-deployment/deployment-via-version-control-using-salesforce-org.md)
{% endhint %}

{% hint style="info" %}
**Note:**

* **No manual merge conflict resolution is supported.** In case of data conflicts, the dataset collected from the source environment will be committed by default, even if corresponding data already exists in the target branch.
* **Destructive changes are currently not supported.** If a record is deleted in the source environment after being committed to Version Control, subsequent commits will not remove that record from the branch. The previously committed record will remain intact.
{% endhint %}

9. The Object Configuration section dynamically displays the selected objects and applies the corresponding filters and mappings based on the selections.
10. The "External Id Mappings" can be configured accordingly.

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2026-02-27 at 4.15.40 PM 2.png" alt=""><figcaption></figcaption></figure>
11. In this section, you can use an external ID in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values in a field marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).

    In the **Source** field: Select your source field whose values will be populated in the destination External Id field.

    In the **Destination** field: Select the required field from the destination org whose values will remain unique for all the records.

    <figure><img src="../../../../../.gitbook/assets/3 - External ID.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note (About Applied Mappings):**

1. If there is no Lookup key and the name is set to External ID, AutoRABIT is still supported.
2. Because the source for this is a CSV extract and not a Salesforce org, all fields from the source sandbox will be fetched, regardless of the External ID in the **Source** column, whereas the source for Destination is a Salesforce org.
{% endhint %}

{% hint style="info" %}
## Preserve nCino RBC lookup relationships during deployment

In AutoRABIT ARM, an nCino Record-Based Configuration (RBC) deployment can link a child record to a parent record that already exists in the destination Salesforce org, even when the parent is outside the deployment dataset. This applies to Feature Deployments and CI Jobs that use templates, Version Control, or a Salesforce source org.

### How ARM resolves parent lookups

* **Parent included in the dataset.** ARM resolves the lookup as part of the deployment’s dependency handling.
* **Parent outside the dataset.** ARM uses the available lookup reference information to match the parent in the destination org. When ARM finds a unique match, it sets the lookup on the child record to that parent.
* **Parent cannot be matched.** Review the deployment results for unresolved lookups. Check the referenced parent in the destination org and verify the External ID field and value used to match it.

### Known limitations

#### Templates and Version Control versions without saved lookup references

Some existing templates and Version Control versions lack the saved lookup references needed to match parents outside the dataset. A deployment that relies on one of these stored datasets can leave the affected child lookup fields blank, even when the parent records already exist in the destination org. When the deployment uses Salesforce to retrieve source data, ARM can capture the lookup references from the source org.

#### External ID mappings for stored lookup references

During feature template creation, ARM captures lookup references using the default nCino External ID field. Custom External ID mappings are unavailable at that stage. If deployment uses a different External ID field for the parent object, the stored reference may lack the value needed for that mapping. The affected lookup field can remain blank if ARM cannot match the parent.

When ARM captures lookup references in a workflow where an External ID mapping is already selected, it uses the selected field. When no mapping is selected, ARM uses the default field.

### Checks before deployment

1. If the stored dataset lacks lookup references, use a newly prepared dataset or a deployment that retrieves source data from Salesforce to capture the lookup references.
2. For a deployment that relies on saved lookup references, verify that the parent object’s External ID mapping uses the field captured in those references.
3. Confirm that the destination org contains a single matching parent record. After deployment, verify that the child lookup points to that record.
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
* **Automap User/Owner Data:**
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
