# Indexes

Indexes are critical in Salesforce for improving the performance of data retrieval, especially when dealing with large volumes of records. Salesforce uses multi-tenant architecture, meaning multiple customers share the same infrastructure, so query efficiency is extremely important. Indexes play a crucial role in databases for improving performance, especially in querying large datasets, by using Indexing on Salesforce objects we can achieve faster data retrieval, Improved query performance , Reduced load on large objects and enhanced sorting and filtering functionality.

By effectively using Indexes on Salesforce objects, we can achieve efficiency in Vault Back up, Compare operations and Live replication of Salesforce orgs.

Salesforce platform maintains default indexes on the following fields for most objects.

* RecordTypeId
* Division
* CreatedDate
* Systemmodstamp (LastModifiedDate)
* Name
* Email (for contacts and leads)
* Foreign key relationships (lookups and master-detail)
* The unique Salesforce record ID, which is the primary key for each object

Salesforce also supports custom indexes on custom fields, except for multi-select picklists, text areas (long), text areas (rich), non-deterministic formula fields, and encrypted text fields.

External IDs cause an index to be created on that field. The query optimizer then considers those fields; we can create External IDs only on the following fields.

* Auto Number
* Email
* Number
* Text

| Field Type             | Indexed by Default          | Custom Index Possible | Notes                                           |
| ---------------------- | --------------------------- | --------------------- | ----------------------------------------------- |
| Text                   | ✅                           |                ✅      | Most commonly indexed                           |
| Email                  | ✅                           | ✅                     | Indexed by default                              |
| Phone                  | ✅                           | ✅                     | Indexed by default                              |
| URL                    | ✅                           | ✅                     | Indexed by default                              |
| Number / Currency      | ❌                           | ✅                     | Can be indexed via support                      |
| Date / DateTime        | ❌                           | ✅                     | Can be indexed for filters or performance       |
| Picklist               | ❌                           | ✅ (limited use)       | Only if required in WHERE clauses               |
| Checkbox (Boolean)     | ❌                           | ✅                     | Usually used in filters                         |
| Lookup / Master-Detail | ❌ (only Name field indexed) | ✅ (Foreign Key Index) | For joins or filtering                          |
| Geolocation            | ❌                           | ❌                     | Not indexable for search                        |
| Long Text / Rich Text  | ❌                           | ❌                     | Not indexable (not searchable in Global Search) |
| Encrypted Fields       | ❌                           | ❌                     | Not searchable due to security                  |

To view if a Field is Indexed/Searchable: Home -> Search Manager -> Index Management -> Select an Object to view the Indexed Fields:

<figure><img src="../../../.gitbook/assets/image (1691).png" alt=""><figcaption><p>Searchability</p></figcaption></figure>

For creating Indexes manually on Big Objects in Salesforce, create custom fields (Mandatory Checkbox – Always requires a value in this field in order to save the record).

<figure><img src="../../../.gitbook/assets/image (1692).png" alt=""><figcaption><p>Index on Big Objects</p></figcaption></figure>

Navigate to Index Tab and click New

<figure><img src="../../../.gitbook/assets/image (1693).png" alt=""><figcaption><p>New Index Definition</p></figcaption></figure>

Once Indexes are created, Validate the Index on the Big Object.

<figure><img src="../../../.gitbook/assets/image (1694).png" alt=""><figcaption><p>Big Object Definition Detail</p></figcaption></figure>

Important criteria to ensure a good fit for a custom index:

1\. Record count for the indexed object must be greater than 1,000 rows (greater than 10,000 rows are recommended to be of significant benefit).

2\. Queries should take 5 seconds or more to process.

3\. Query must contain a WHERE clause with a value that somewhat unique (i.e., the custom index should be able to filter out \~ 90% of the records).

4\. Some commonly used fields, external id fields, and reference (lookup/master-detail) fields are already standard indexed. Formula fields and certain other fields cannot be custom indexed.

5\. For SOQL queries executed in Apex, it is common for developers to embed data binding variables to make the query dynamic; however, for analyzing the query for custom indexing, we need to know the typical values that will actually be used at runtime.

### Performance Results of Synthetic Backup using Indexes in Vault tool:

As noticed on our QA Org, the below is the Impact of creating Indexes on SF Big Objects and using synthetic back ups

SF Org Back up taken prior to Indexing and Synthetic Back up ([https://knowledgebase.autorabit.com/product-guides/vault/vault-features/backup/synthetic-backup](https://knowledgebase.autorabit.com/product-guides/vault/vault-features/backup/synthetic-backup)) took approximately 8 hours for 3.2 million records now complete 8.9 million records back up with additional metadata in 1.5 hours.

<figure><img src="../../../.gitbook/assets/image (1695).png" alt=""><figcaption><p>Backup Summary</p></figcaption></figure>

