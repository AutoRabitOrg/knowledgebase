# Archive Best Practices

This article illustrates many of the key best practices for the **archive** process on the Vault platform:

1. Archiving parent objects will result in the deletion of all the child objects related through mandatory lookups and master-detail relationships recursively as it is an expected behavior of Salesforce. For the children related through a lookup(which is not mandatory), the reference to the parent will be removed from the child object before performing deletion of the parent.
2. Ensure that only one object is chosen for archival at a time in an org to avoid hitting issues with rowlocks and interdependencies during the deletion of the records from Salesforce.
3. Always select the option to **`Notify before deleting data from Salesforce`** to avoid auto-deletion of the records without consent and review of the records that are going to be deleted as part of the job.
4. Use limit and offset or an auto-increment field on the object to chunk the data for deletion into smaller batches to help understand the impact and to strategize the deletion of subsequent batches based on the errors experienced in the initial batches
5. Provide a smaller **Bulk API batch size** when triggering the archival to avoid errors arising out of Salesforce processing capabilities.
6. Run the archive job in **serial mode** to avoid hitting errors like row locks or any other issues arising out of parallel processing in Salesforce. This is recommended only if you experience errors due to parallel mode as running the job in serial mode will impact the time taken to execute the job.
7. Ensure that the options to **disable workflows, validation rules, and triggers** are **enabled** during the initiation of the archive job to ensure the deletion of records won’t result in hitting salesforce processing limitations and allocations.
