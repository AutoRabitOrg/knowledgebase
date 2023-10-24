# Dataloader

### Single Dataloader: Overview <a href="#single-dataloader-overview" id="single-dataloader-overview"></a>

ARM **Dataloader** allows you to configure your data loading operations in convenient, user-friendly GUI wizards. It also allows you to import, export, and delete unlimited amounts of Salesforce data without typing a single line of code. Its powerful yet easy-to-understand scheduling settings enable you to specify almost any schedule quickly. You can schedule any data loading operation for automatic execution.

#### When to use Single Dataloader <a href="#when-to-use-single-dataloader" id="when-to-use-single-dataloader"></a>

1. You need to load 50,000 to 5,000,000 records. [Dataloader](https://www.autorabit.com/blog/10-benefits-of-salesforce-data-loader/) is supported for loads of up to 5 million records. If you need to load more than 5 million records, we recommend you work with a Salesforce partner or visit the **AppExchange** for a suitable partner product.
2. You need to load into an object that the import wizards do not support yet.
3. You want to schedule regular data loads, such as nightly imports.
4. You want to export your data for backup purposes.

#### Features of Single Dataloader <a href="#features-of-single-dataloader" id="features-of-single-dataloader"></a>

1. [Extracting Data from Salesforce](single-dataloader/extract-salesforce-data.md)
2. [Importing Data into Salesforce](single-dataloader/insert-salesforce-data.md)
3. [Deleting Data from Salesforce](single-dataloader/delete-salesforce-data.md)
4. [Updating Data in Salesforce](single-dataloader/update-salesforce-data.md)
5. [Upserting Data into Salesforce](single-dataloader/upsert-salesforce-data.md)

### Dataloader Pro: Overview <a href="#dataloader-pro-overview" id="dataloader-pro-overview"></a>

**Dataloader Pro** is an advanced feature ARM provides for transferring data from the source sandbox to the destination sandbox more conveniently while automatically handling the parent-child relationship. Migrating the [Salesforce data](single-dataloader/update-salesforce-data.md)/objects to more than one object-supporting hierarchy can easily be achieved using the **Dataloader Pro** feature in ARM.

#### Features of Dataloader Pro <a href="#features-of-dataloader-pro" id="features-of-dataloader-pro"></a>

* Cloud-based dataloader with scheduling capabilities
* Supports circular references
* Objects are extracted from the source sandbox and transferred to the destination in one step.
* Data integrity check: Checks for data integrity between the source and the destination.
* Error reporting: Detailed reporting of any failure during dataloading operations.
* History of dataloading operations: The results are retained for future reference.
* Supports owner ID transfer
* Supports user lookup transfer
* Supports chatter data migration
* Preserves the parent-child relationship

### Salesforce/ARM Dataloader Comparison Matrix <a href="#salesforcearm-dataloader-comparison-matrix" id="salesforcearm-dataloader-comparison-matrix"></a>

[Salesforce Dataloader](https://www.autorabit.com/blog/addressing-the-salesforce-data-loader-log4j-issue-with-autorabit/) vs. ARM Dataloader vs. ARM Dataloader Pro

| **Category**                    | **SFDC Dataloader**                                            | **AR Dataloader**                                                                       | **AR Dataloader Pro**                                                                                                                                                          |
| ------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ease of use                     | Wizard interface                                               | Simple, easy steps to create a Dataloader job                                           | Simple, easy steps to create a Dataloader pro job                                                                                                                              |
| Data/records Supported          | Supports up to 5 million records                               | Supports unlimited data                                                                 | Supports unlimited data                                                                                                                                                        |
| Field mapping                   | Drag-and-drop field mapping                                    | Auto field mapping                                                                      | Auto field mapping                                                                                                                                                             |
| Schedule                        | Does not support scheduling                                    | Supports scheduling                                                                     | Supports scheduling                                                                                                                                                            |
| Pre/post-migration operations   | No built-in mechanism                                          | Built-in handling mechanism for validation and workflow rules while migrating data      | Built-in handling mechanism for validation and workflow rules while migrating data                                                                                             |
| Dataloader operations supported | Supports export, insert, update, upsert, and delete operations | Supports export, insert, update, upsert, and delete operations                          | Automatically and dynamically supports insert, update, and upsert operations, based on destination org data, for multiple objects, while preserving parent/child relationships |
| Multi-object migration support  | Does not support multi-object migration                        | Does not support multi-object migration                                                 | Supports multiple object data migration                                                                                                                                        |
| Ease of admin                   | Supports results download                                      | User-friendly results data, downloadable in CSV format                                  | User-friendly Object and results data, downloadable in CSV format                                                                                                              |
| Grouping of jobs                | Does not support job grouping                                  | The user can group sets of dataloader jobs                                              | The user can group sets of dataloader jobs                                                                                                                                     |
| Masking rules                   | Limited masking rules                                          | Multiple masking rules                                                                  | Multiple masking rules                                                                                                                                                         |
| Data migration                  | Slower data migration                                          | Much faster data migration using ARM external ID, which also helps eliminate duplicates | Much faster data migration using ARM external ID, which also helps eliminate duplicate                                                                                         |
