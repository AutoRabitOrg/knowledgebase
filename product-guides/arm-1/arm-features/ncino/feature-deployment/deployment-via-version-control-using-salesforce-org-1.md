# Deployment via Version Control using Salesforce Org

This section covers the deployment of **nCino metadata and data** through **version control**, leveraging the **Salesforce dataset** for streamlined and traceable delivery.

1. The "Feature Deployment" can be triggered in the following way
   1.  Click on the "Create" drop-down to observe the options to select the "Feature Deployment" as option

       <figure><img src="../../../../../.gitbook/assets/1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
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
   7. **VC Fetch Type**: Select the option to perform the deployment.
      1. The following options are available at "VC Fetch Type":
         1. Entire Branch
         2.  Single Revision

             <figure><img src="../../../../../.gitbook/assets/2.0 - Deploy Using SF and VC (1).png" alt=""><figcaption></figcaption></figure>
      2.  **Entire Branch**: This option will fetch the feature migration templates configured on your branch. You'll be asked to choose the **feature/template** and **version when selecting** the entire branch option.

          <figure><img src="../../../../../.gitbook/assets/3- Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
      3.  **Single Revision**: This option will pull all of the versions from your repo, allowing you to choose which revision to use in the deployment.

          <figure><img src="../../../../../.gitbook/assets/4 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>

          <figure><img src="../../../../../.gitbook/assets/4.0 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
      4.  Observe the values selected at the revision

          <figure><img src="../../../../../.gitbook/assets/4.1 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
6.  In the nCino Deployment **Source** step, users can sort the **Feature** and **Version** lists for the selected repository and branch.

    1.  The user opens the **Feature** dropdown and clicks the **Sort** icon beside **Search**.

        <figure><img src="../../../../../.gitbook/assets/1 (35).png" alt=""><figcaption></figcaption></figure>
    2.  The user selects the required sort order:

        | Option                 | Description                                   |
        | ---------------------- | --------------------------------------------- |
        | **Newest**             | Displays the newest items first.              |
        | **Oldest**             | Displays the oldest items first.              |
        | **Alphabetical - A-Z** | Sorts names in ascending alphabetical order.  |
        | **Alphabetical - Z-A** | Sorts names in descending alphabetical order. |
    3.  After selecting a feature, the user opens the **Version** dropdown and uses its **Sort** icon to arrange the available versions.

        <figure><img src="../../../../../.gitbook/assets/2 (35).png" alt=""><figcaption></figcaption></figure>

    A checkmark indicates the selected sort option.
7. Based on the selected revisions, the respective "feature versions" will be displayed.
8. **`NOTE`:**
   1. **`No manual merge conflict resolution is supported.`**` `` ``In case of data conflicts, the dataset collected from the source environment will be committed by default, even if corresponding data already exists in the target branch. `
   2. **`Destructive changes are currently not supported.`**` `` ``If a record is deleted in the source environment after being committed to Version Control, subsequent commits will not remove that record from the branch. The previously committed record will remain intact. `
9.  Click on the "Next" to continue to the "Destination" section of the Feature Deployment flow

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2026-02-27 at 5.54.35 PM.png" alt=""><figcaption></figcaption></figure>
10. You can configure several options for your objects before proceeding with a deployment or commit, including:

    * **External Id Mappings**
    * **Applied Filters**

    <figure><img src="../../../../../.gitbook/assets/2 - FD Using VC SF.png" alt=""><figcaption></figcaption></figure>
11. **External ID Mappings**

    This section allows you to use an **External ID** instead of a Salesforce **Record ID** to establish relationships between records during an **Upsert** operation.\
    For example, if **Object B** has a lookup to **Object A**, you can reference a field on Object A marked as an _External ID_ to relate Object B records to the correct Object A records.

    * **Source Field**: Select the source field whose values will be used to match and populate the destination’s External ID field.
    * **Destination Field**: Choose a field from the destination org that is marked as an External ID and holds **unique values** across all records.

    <figure><img src="../../../../../.gitbook/assets/3 - FD Using VC SF.png" alt=""><figcaption></figcaption></figure>



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

{% hint style="info" %}
#### **Important Note on External ID Mappings**

When deploying via **Template** or **Version Control**, the **source** is a **CSV file**, not a Salesforce Org. As a result:

* **All fields** from the CSV—regardless of External ID designation—will appear in the **Source** column.
* In contrast, only **valid External ID fields** from the **Salesforce destination org** will be shown in the **Destination** column for selection.

Please note that **AutoRABIT-defined External ID fields** are **not supported** for the **Upsert** operation.
{% endhint %}

{% hint style="info" %}
**Note:**

* **No manual merge conflict resolution is supported.** In case of data conflicts, the dataset collected from the source environment will be committed by default, even if corresponding data already exists in the target branch.
* **Destructive changes are currently not supported.** If a record is deleted in the source environment after being committed to Version Control, subsequent commits will not remove that record from the branch. The previously committed record will remain intact.
{% endhint %}

10. **Applied Filters**: If any filters have been applied to the objects, they will be displayed in this section. You can modify an existing filter at any time by selecting **Edit Filter**.

    <figure><img src="../../../../../.gitbook/assets/4 - FD Using VC SF.png" alt=""><figcaption></figcaption></figure>
11. On completing the required selection click next to continue to the "Job Settings" section of the "Feature Deployment" flow.
12. Observe the following screenshot for the "Deployment Options" available on this section:

    <figure><img src="../../../../../.gitbook/assets/7 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>

* **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
* **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in a go from the source and destination org.
* **Use UTF-8 file encoding for file read and write operations:** Use **UTF-8** as the internal representation for all string data. Text is automatically transcoded between the local encoding and UTF-8 when reading from or writing to files.
  * **Enable UTF-8** if your data contains **only English alphabets**.
  * **Disable UTF-8** if your data includes **non-English characters** to avoid encoding issues.
  * UTF-8 should be **enabled by default**, aligning with Salesforce’s recommended encoding standards.
* **Automap User/Owner Data:**
* **Disable Validation Rules:** Select this option to temporarily deactivate validation rules on objects included in the deployment. This helps ensure smoother deployments without interruptions caused by rule enforcement.
* **Insert/Update with Null Values:** When enabled, this option allows fields with `null` values in the source org to be inserted or updated as `null` in the destination org. It ensures data consistency by reflecting blank or cleared values during migration.
* **Enable Rollback:** Enable this option to allow rollback of the deployment, if needed. Only components explicitly marked for **“Rollback”** during deployment will be eligible for rollback after completion.

13. Based on your destination selection, you will have different deployment options to choose from:
    1. **Create Dataset:** Create a dataset from your Salesforce Org
    2. **Create Dataset Commit & Deploy:** Create a dataset and proceed for both commit and deployment.
14. Clicking on ether of the deployment options available "**Create Dataset" or "Create Dataset Commit & Deploy"**, the flow will be redirected to the "Deployment History" page.

    <figure><img src="../../../../../.gitbook/assets/8 - Deploy Using SF and VC.png" alt=""><figcaption></figcaption></figure>
