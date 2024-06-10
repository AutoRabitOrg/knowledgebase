# Using Data Loader with Lookups

### What is a Lookup? <a href="#what-is-a-lookup" id="what-is-a-lookup"></a>

Lookup is a type of Salesforce relationship that connects two objects together without affecting security and deletion properties. Creating an intermediary relationship between objects is possible by adding lookup relationships to standard, custom and external objects.

### When should I use Lookups in Data Loader? <a href="#when-should-i-use-lookups-in-dataloader" id="when-should-i-use-lookups-in-dataloader"></a>

Lookups are useful when a user likes to associate two records in a relationship. For example, a user can associate a quote record to another record by using a lookup field that points to another object, including custom objects.

### Where can I use the Lookups in Data Loader? <a href="#where-can-i-use-the-lookups-in-dataloader" id="where-can-i-use-the-lookups-in-dataloader"></a>

You can use Lookups to **Insert**, **Update**, or **Upsert** data in Data Loader.

### Apply Lookups <a href="#apply-lookups" id="apply-lookups"></a>

Assuming you create an **Insert** task, and have uploaded the CSV file to import, and, when you reach the **Fields Mapping** step, you will be able to find the **"Lookup via"** checkbox.

**For example:** To map the **Account Name** to the **AccountID** in Salesforce, click on the **"Lookup via"** checkbox and select the field you want to use to search the ID. In this example, you have selected **'Account Name'**, which is the field you want to use to search the ID. So, when you run the task, ARM dataloader will go and search for the **Account ID** using the **Account Name** on each case, and send the IDs that Salesforce is expecting.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-M6ZL3C6Q.png" alt=""><figcaption></figcaption></figure>

### More Lookup Options <a href="#more-lookup-options" id="more-lookup-options"></a>

**Use first match in multiple results**

Data Loader will pick the first value if more than one match is found for the selected non-unique field. In the above example, there might be more than one Account under the name **'GenePoint'**, in such a case, the data loader will just use the ID of the first occurrence of those Accounts.\
\


**Mark record with an error if more than one match is found**

ARM Data Loader will mark the row with an error message saying more than one match is found for your non-unique field. You can later pick the errors file and fix this problem either in Salesforce or by passing the ID directly and re-uploading the file.
