# Using Data Loader with Lookups

### What is a Lookup? <a href="#what-is-a-lookup" id="what-is-a-lookup"></a>

A lookup is a type of Salesforce relationship that connects two objects without impacting their security or deletion behavior. It enables linking standard, custom, and external objects through intermediary relationships.

### When Should I Use Lookups in Data Loader? <a href="#when-should-i-use-lookups-in-dataloader" id="when-should-i-use-lookups-in-dataloader"></a>

Lookups are ideal when associating two records. For example, to link a Quote to an Account, a lookup field can point to the related Account object (including custom objects).

### Where Can I Use Lookups in Data Loader? <a href="#where-can-i-use-the-lookups-in-dataloader" id="where-can-i-use-the-lookups-in-dataloader"></a>

Lookups can be applied during **Insert**, **Update**, or **Upsert** operations in ARM Data Loader.

### Apply Lookups <a href="#apply-lookups" id="apply-lookups"></a>

When performing an **Insert** task and you’ve uploaded your CSV file, proceed to the **Fields Mapping** step. There, you'll find a **"Lookup via"** checkbox.

**Example:**\
To map **Account Name** to **Account ID** in Salesforce:

* Click the **"Lookup via"** checkbox.
* Select **'Account Name'** as the field to search by.

ARM Data Loader will search for the **Account ID** using the provided **Account Name** and populate the correct IDs expected by Salesforce.

<figure><img src="../../../../../.gitbook/assets/image (89) (1) (1).png" alt="Lookup via field mapping in Data Loader"><figcaption></figcaption></figure>

### More Lookup Options <a href="#more-lookup-options" id="more-lookup-options"></a>

* **Use first match in multiple results:**\
  If multiple records match the selected non-unique field (e.g., several accounts named _GenePoint_), the Data Loader selects the first match automatically.
* **Mark record with an error if more than one match is found:**\
  If enabled, ARM Data Loader flags the row with an error stating multiple matches exist. You can resolve this by fixing the data in Salesforce or by manually providing the correct ID in the CSV and re-uploading.
