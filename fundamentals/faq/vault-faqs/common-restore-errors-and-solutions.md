# Common Restore Errors & Limitations

## Vault FAQs

### Common Restore/Replicate Errors & Solutions

### RESTORE/REPLICATE

#### How can I filter backup data by specific dates and use it as the source to Restore/Replicate?

To filter data based on specific dates from a backup using a CSV file and Excel, follow these steps:

1. **Download CSV File**: Download the CSV file corresponding to the object on which the date needs to be filtered from the backup.
2. **Filter Dates Using Excel**: Open the downloaded CSV file in Excel. Use Excel's filtering features to filter out the IDs for which the dates match the required criteria.
3. **Create Final CSV File**: Save the filtered data in a new CSV file. This file should contain only the filtered IDs.
4. **Upload and Filter Backup**: Use the final CSV file with the filtered IDs as the source. In the restore/replicate module, use the file upload option in the filters to filter the backup data accordingly.

#### **CANNOT\_INSERT\_UPDATE\_ACTIVATE\_ENTITY**

This error is a result of an issue stemming from a trigger in the Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Use the option to disable the triggers in the job configuration. For the triggers that cannot be disabled via metadata API, manually disable the triggers in Salesforce and re-run the job.



#### CANNOT\_EXECUTE\_FLOW\_TRIGGER

* Typical error message - We can't save this record because the ‘Online Applicant Validation’ process failed. Give your Salesforce admin these details. An error occurred when executing a flow interview. Error ID: 1545064308-45750 (1670083917)
* This error typically indicates that there is a Process Builder process / Flow in place which is causing the upsert operation to fail.

**Resolution steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Locate the process builder process / flow that caused the error. Temporarily disable the automation and rerun the job to restore/replicate failed records.
3. Alternatively, the job can be retried by specifying a lower batch size in the job config which prevents the process builders/flows from hitting the parallel processing limits in Salesforce.



#### INACTIVE\_OWNER\_OR\_USER

This error is due to the owner of the records about to be inserted into the destination Org is inactive in the destination Org.

**Resolution Steps:**

1. Click on Replicate/Restore job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Enable "Set Audit Fields upon Record Creation" and "Update Records with Inactive Owners" permissions in Salesforce settings.
3. Enable these permissions in the permission set corresponding to the dataloading user in the destination Org.
4. To access details on how to do this in Salesforce, click on this link: [https://help.salesforce.com/articleView?id=000334870\&type=1\&mode=1](https://help.salesforce.com/articleView?id=000334870\&type=1\&mode=1)



#### FIELD\_CUSTOM\_VALIDATION\_EXCEPTION

This error is due to validation rules applied to certain fields.

**Resolution Steps:**

1. Click on Restore/Replicate job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Disable validation rules in the restore modal in the final step of the restore process.



#### INVALID\_OR\_NULL\_FOR\_RESTRICTED\_PICKLIST

This error occurs when the destination Org doesn't have the value enabled that is selected in the source Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Sync the values in the restricted picklist between the source and destination.
3. Alternatively, use the mappings for restricted picklist to cross-map a value in the restricted picklist from the source to another value in the destination Org as part of the replicate job configuration.



#### REQUIRED\_FIELD\_MISSING

This error occurs due to a failure of a required parent record (related through master-detail/required).

**Resolution Steps:**

1. Click on Replicate/Restore job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Such errors occur when failure of a required parent record (related through master-detail/required  lookup) leads to the failure of its associated child records.
3. Check the fields that failed. Review the error corresponding to the failure of the referencing parent record(s), rectify them, and restore the corresponding failed parent records first, then restore failed related child records.



#### INVALID\_CROSS\_REFERENCE\_KEY

This error is caused by the Parent record not being included in the job or permission issue(s) on the parent object or a lookup relationship is not included in the job.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Verify the parent object is included in the job.
3. Review the authenticated user to ensure the user has access to the parent record that is referenced within the error.
4. If it is a lookup relationship then ensure the parent object is included in the job.



#### CANNOT\_UPDATE\_CONVERTED\_LEAD

This error is due to a Lead record once converted (to a contact) becomes read only which prevents you from updating the lead.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. You can check to ensure that the lead is converted by checking the isConverted field.



#### FIELD\_INTEGRITY\_EXCEPTION

This error typically occurs when upsert tried to populate a lookup field with a wrong ID either because the parent failed or Vault is unable to recognize the parent record Id.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Need to pass the correct Id for a lookup field.



#### INVALID\_OPERATION: Too many files in zip

* Typical error message - Metadata deployment error...com.sforce.ws.SoapFaultException
* This error is generated when there are more than 10,000 files in the .zip file which violates the governor limit.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on logs-> view error the 'Error' column.
2. Reduce the number of metadata components restored/replicated in each job to less than 10,000 files.



**RECORD-TYPE ACCESS ISSUE**

This error indicates that the Salesforce user authenticated on Vault doesn’t have access to some record types of an object(s).

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Give appropriate access using profiles and permissions to the Salesforce user authenticated on Vault.



#### UNKNOWN USER PERMISSION

This error is generated when the required user permissions are missing in Salesforce.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Assign user to the desired permission set in Salesforce.



#### INVALID\_CROSS\_REFERENCE\_KEY

* Typical error message - Record Type ID: this ID value isn't valid for the user: 012D0000000BfaLIAS:RecordTypeId --
* This error is generated when the Salesforce user authenticated on Vault doesn’t have access to some record types of an object(s).

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Give appropriate access using profiles and permissions to the Salesforce user authenticated on Vault.



#### CANNOT\_INSERT\_UPDATE\_ACTIVATE\_ENTITY

* Typical error message - SFSSDupeCatcher.SSDupeCatcherContactTrigger: System.LimitException: Apex CPU time limit exceeded
* Error is generated by Triggers preventing the records from getting loaded in the destination Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Disable the triggers on the destination Org either by using the option to disable triggers in Vault or by performing the same in the Salesforce Org.
3. Alternately, try lowering the batch size of the operation to avoid more records from getting inserted/updated in parallel which may result in a CPU time limit exception.



#### UNABLE\_TO\_LOCK\_ROW

* Typical error message - unable to obtain exclusive access to this record or 126 records.
* Error is caused by Dependent records causing the load of records from populating in the destination Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Execute the job in serial mode instead of parallel mode to help prevent records in different batches having dependency with each other getting inserted into Salesforce in parallel and causing the error.



#### TooManyLockFailure

* Typical error message - Too many lock failure 200 Trying again later.
* Error is caused by Dependent records causing the load of records from populating in the destination Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Decrease the batch size or execute the job in serial mode instead of parallel mode to help prevent records in different batches having dependency with each other getting inserted into Salesforce in parallel and causing the error.
3. For more information, go to this link  [![](file:///C:/Users/shannan.zerance/AppData/Local/Packages/oice\_16\_974fa576\_32c1d314\_278d/AC/Temp/msohtmlclip1/01/clip\_image001.png)Feed Item Detail | Salesforce Trailblazer Community](https://developer.salesforce.com/forums/?id=906F0000000D9CuIAK)&#x20;

***

### REPLICATE

#### DUPLICATE\_VALUE

Such failures occurs when such records are already present in the destination

**Resolution Steps:**

1. Click on Replicate job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. An existing automation is blocking the upsert operation. Try disabling the automation if necessary.
3. If you would like Vault to recognize the existing records in the destination that are created/transferred outside of Vault, you can configure the unique identifier for the object and enable the option ‘Prevent duplicate record creation using unique identifiers in replicate job config to avoid Vault from attempting to recreate an existing record matching the value in the unique identifier specified.
4. For steps on how to configure unique identifiers, go to this link:

&#x20;[Unique Identifier (UID) | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/vault/configuring-vault/registering-salesforce-org/unique-identifier-uid)

***

### LIMITATIONS

* **Restoration of System-Generated Chatter-Feed Items**
  * **Issue**: Salesforce does not allow the restoration of chatter-feed items generated by the system.
  * **Details**: Only feed items manually added by users to the chatter feed can be restored.
  * **Error Message**: Attempting to restore system-generated chatter-feed items will result in the error: "Required field missing: Body."
* **Restoration of Shared Objects Data**
  * **Issue**: Salesforce does not permit the restoration of data in shared objects generated by sharing rules.
  * **Details**: Only manually added share-related records in the shared object can be restored.
