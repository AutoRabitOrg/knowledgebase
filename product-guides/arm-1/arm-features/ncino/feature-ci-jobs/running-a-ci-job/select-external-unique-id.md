# Select External Unique ID

## Select External Unique ID

### **Select External Unique Identifier During nCino Feature Deployment**

This provision allows you to go through the list of external unique IDs available and will allow you to select the external unique ID of your choice.

1. By default, the ID, Name, and a unique field will be populated in the dropdown.
2. If the name is auto generated, then that name will not be considered a unique field.

The external unique ID field is available in the “Deploy” page.

<figure><img src="../../../../../../.gitbook/assets/image (4728).png" alt=""><figcaption></figcaption></figure>

If the source for the deployment is a CSV file, then all the fields will be displayed in the dropdowns.

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
