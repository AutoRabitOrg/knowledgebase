# Deployment via Template using Salesforce Org

This article describes the process of deploying the nCino data via the Salesforce ORG dataset

1. A Feature Deployment can be triggered in the following ways:
   1. Click on the "Create" button to observe the options to select the "Feature Deployment" as an option.
2. Click on the "Deployment History" under the nCino tab to access "Create feature deployment."

<figure><img src="../../../../../.gitbook/assets/1.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

1. Upon clicking on **"Create Feature Deployment"** or selecting the **"Feature Deployment**,**"** a Source Type screen will appear. Choose "**Deploy using Salesforce template**" to proceed.

<figure><img src="../../../../../.gitbook/assets/2 - Feature Deployment (1).png" alt=""><figcaption></figcaption></figure>

2. Continue to input the fields on the screen with the required inputs.

<figure><img src="../../../../../.gitbook/assets/3 - Feature Deployment (1).png" alt=""><figcaption></figcaption></figure>

3. The following fields are available on the screen to input the data:
   1. **Label name:** Input label name of the deployment here.
   2. **Description:** Enter a description that suits the deployment.
   3. **Source Org:** Select the source Org.
   4. **Feature Type:** Select the feature type from the available list. The following are the available values:
      * Standard
      * Community
   5. **Feature:** Select the required feature
   6. **Version**: Select the version based on the feature selection.
4.  In the nCino Deployment **Source** step, users can sort the **Feature** and **Version** lists to locate the required item.

    1.  The user opens the **Feature** dropdown and clicks the **Sort** icon beside **Search**.

        <figure><img src="../../../../../.gitbook/assets/1 (18).png" alt=""><figcaption></figcaption></figure>
    2.  The user selects a sort option:

        | Option                 | Sort order                              |
        | ---------------------- | --------------------------------------- |
        | **Newest**             | Newest items first.                     |
        | **Oldest**             | Oldest items first.                     |
        | **Alphabetical - A-Z** | Names in ascending alphabetical order.  |
        | **Alphabetical - Z-A** | Names in descending alphabetical order. |
    3.  After selecting a feature, the user opens the **Version** dropdown and uses its **Sort** icon to arrange the available versions.

        <figure><img src="../../../../../.gitbook/assets/2 (32).png" alt=""><figcaption></figcaption></figure>

    A checkmark indicates the selected sort option.
5. After entering all the details, click on '**Next**' to continue to the "**Destination**" screen.

<figure><img src="../../../../../.gitbook/assets/4 - Feature Deployment (1).png" alt=""><figcaption></figcaption></figure>

5. Enable "Deploy To" and "Commit To" options on the destination screen. To deploy to a Salesforce org, select the **Deploy To** checkbox and choose your **Destination Org**. To commit to a branch, select the **Commit To** box, enter your **Repository/Branch** details, and **comment** (if any).

{% hint style="info" %}
**Important Note**: For commits, the features will get committed to the default location in your version control branch. By default, the location is set to the dataset.
{% endhint %}

6. The following options can be observed on the data selected for deployment or committing the data:
   1. Object: The object selected
   2. ExternalId mappings
   3. Sorting Criteria (only if the 'Commit to' checkbox is selected)
   4. Applied Filters
7.  ExternalId Mappings:

    1. This external ID can be used in place of a related record's Salesforce record ID to relate or associate records to each other as you process an Upsert operation. For example, if **Object B** has a lookup field to another **Object A,** you can use the values in a field marked as an External ID on **Object A** to relate the two (**Object B** to **Object A** records).
       1. **Source**: Select your source field whose values will be populated in the destination External Id field.
       2. **Destination**: Select the required field from the destination org whose values will remain unique for all the records.

    <figure><img src="../../../../../.gitbook/assets/5 - Feature Deployment (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/5.0 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/5.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>



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
## **Important Note:** (ExternalIdMappings):

1. Since the source for Deployment via **Template** or **Version Control** is a CSV file rather than a Salesforce Org, all fields, regardless of the External ID supported, will be fetched and displayed in the **Source** column. However, the relevant fields will be shown under the Destination column since the target org is a Salesforce org.
2. AutoRABIT External ID fields are not supported for the **Upsert** operation.
{% endhint %}

9. Sorting Criteria: This new feature is useful for sorting the fields of nCino objects while committing. Based on the sort order set, the record order in the JSON files will get fetched. There is a provision to input a default sort order that can be changed. **XXXXX\_lookupkey\_\_c** is the most preferred field for sorting, and that would be the default field. If this field is not present, the **Name** for _custom settings_ and **Id** for _non-custom settings_ would be selected.

<figure><img src="../../../../../.gitbook/assets/5.2 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/5.3 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

9. **Applied filters**: Such filters will be displayed here if any filter is applied to the objects. You can edit the already applied filter (if required) using **Edit Filter.**

<figure><img src="../../../../../.gitbook/assets/6 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/6.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

10. After completing the required selections in the "Destination" section, click on "Next" to continue.
11. **Job settings:** This section provides multiple deployment options to help you configure how changes are pushed to the destination org. You can select from various deployment criteria to tailor the process before initiating the deployment.

<figure><img src="../../../../../.gitbook/assets/7 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

12. **Deployment Filters**
    1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment.
    2. **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records all at one time from the source and destination org.
    3. **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.
    4. **Automap User/Owner Data**: Enabling this ensures that the user data will be compared between the two environments and will be mapped based on the value before the "@" symbol in the email. On finding the matches, the same user name value will be populated into the fields in the destination. If the user data is sent empty, the user value will be populated with the user registered with our application.
    5. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment.
    6. **Insert/update with Null Values:** This will either insert or update record field values with null in the destination org (if the value is null in the source org).
    7. **Enable Rollback**: Enabling this ensures that the user can roll back the deployment to the previous state before the deployment is initiated.
13. **Preview**: All the configurations made during the deployment creation can be observed here, with different deployment options.

<figure><img src="../../../../../.gitbook/assets/8 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

13. Based on your destination selection, you will have different deployment buttons to choose from:
    1. **Create Dataset:** Create a dataset from your Salesforce Org.
    2. **Create Dataset Commit & Deploy:** Create a dataset and proceed for both commit and deployment.
14. Clicking on ether of the deployment options available above, you will be redirected to the "Deployment History" page.

<figure><img src="../../../../../.gitbook/assets/9 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
