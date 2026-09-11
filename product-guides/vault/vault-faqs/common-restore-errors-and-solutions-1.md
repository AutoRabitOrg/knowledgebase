# Common Error Messages

## AutoRABIT Vault FAQs - Common Error Messages + Resolutions

### Backup

#### "Entity named '\<member\_name>' cannot be found" for Enhanced LWR Sites

#### Issue

During a Vault backup, customers may notice that **Enhanced LWR sites** are listed under `ExperienceBundle`and the retrieval fails with the following error:

> **Entity named '\<member\_name>' cannot be found**

Because of this retrieval error, Vault may show the overall backup status as **Completed** and display the failure counts.

This can lead customers to believe that the Enhanced LWR site was not backed up successfully.

#### Cause

Salesforce provides multiple metadata types for Digital Experiences, including **DigitalExperience**, **DigitalExperienceBundle**, and **DigitalExperienceConfig**. These are separate Metadata API types. Salesforce's Metadata Coverage Report lists each of them independently.

For **Enhanced LWR sites**, Salesforce uses `DigitalExperienceBundle` and `DigitalExperienceConfig` as the appropriate metadata types.

In some scenarios, Salesforce may also expose the site under `ExperienceBundle`. When Vault attempts to retrieve the site through `ExperienceBundle`, Salesforce may return:

> **Entity named '\<member\_name>' cannot be found**

Even though Salesforce displays the data, it does not allow us to retrieve the data available under the “Experience Bundle”. Vault therefore records this as a retrieval failure and displays the overall backup as Completed.

However, if the same Enhanced LWR site is successfully retrieved under `DigitalExperienceBundle`, the site has been backed up successfully.

#### Important

**The Completed status is expected in this scenario and does not indicate that the Enhanced LWR site was missed from the backup.**

The `ExperienceBundle` retrieval failure is a non-impacting warning when the site is successfully available under `DigitalExperienceBundle`.

**Note:-** Sites built on enhanced LWR (Winter '23 / API 56.0+) aren't retrievable as `ExperienceBundle` at all — they come back as `DigitalExperienceBundle`

***

#### Metadata Types by Digital Experience Framework

| Salesforce Digital Experience Framework | Primary Metadata to Retrieve                     | Supporting Site Metadata                   | Common Dependencies                                                                                                                                                                                                    |
| --------------------------------------- | ------------------------------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aura-based Experience Builder           | ExperienceBundle                                 | Network, CustomSite                        | NavigationMenu, AuraDefinitionBundle, LightningComponentBundle, ApexClass, ApexPage, CustomObject, CustomField, profiles, permission sets, static resources, documents, custom labels, and other referenced components |
| Salesforce Tabs + Visualforce           | Network, CustomSite                              | Applicable ApexPage and ApexClass metadata | CustomTab, ApexComponent, StaticResource, CustomObject, CustomField, profiles, permission sets, documents, custom labels, and other referenced components                                                              |
| LWR—standard/non-enhanced               | ExperienceBundle                                 | Network, CustomSite                        | NavigationMenu, LightningComponentBundle, ApexClass, CustomObject, CustomField, profiles, permission sets, static resources, custom labels, and other referenced components                                            |
| Enhanced LWR                            | DigitalExperienceBundle, DigitalExperienceConfig | Network, CustomSite                        | NavigationMenu, LightningComponentBundle, ApexClass, CustomObject, CustomField, profiles, permission sets, static resources, custom labels, and other referenced components                                            |

> **Note:** The dependencies listed above are examples and should not be considered mandatory for every site. The actual dependencies depend on the configuration and components used by the individual Digital Experience site.

For example, an Aura site using a custom Apex controller would require the relevant `ApexClass`, whereas a site without custom Apex functionality would not.

***

#### How to Validate the Backup

When an Enhanced LWR site results in a **Completed** status:

1. Open the Vault backup details.
2. Check the retrieval results for `DigitalExperienceBundle`.
3. Confirm that the Enhanced LWR site was successfully retrieved under `DigitalExperienceBundle`.
4. Verify that `DigitalExperienceConfig` was also successfully retrieved, where applicable.
5. If the only failure is the `ExperienceBundle` retrieval with the error **"Entity named '\<member\_name>' cannot be found"**, the backup can be considered successful for the Enhanced LWR site.

#### Example

**ExperienceBundle**

`Entity named '<member_name>' cannot be found` → **Failed**

**DigitalExperienceBundle**

Enhanced LWR site → **Successfully Retrieved**

**Result:** The site is backed up successfully, and the overall **Completed** status is expected due to the unsuccessful `ExperienceBundle` retrieval.

***

#### Resolution / Customer Guidance

No action is required if the Enhanced LWR site is successfully backed up under `DigitalExperienceBundle`.

Customers should use the following metadata types for Enhanced LWR sites:

* `DigitalExperienceBundle`
* `DigitalExperienceConfig`
* `Network`
* `CustomSite`

Additional dependencies should be included based on the actual site configuration.

**Vault currently does not provide an option to suppress or ignore this specific** `ExperienceBundle` **retrieval warning.**

#### Summary

Under the current Vault behaviour, the backup may display a **Completed** status with a failure count when an Enhanced LWR site cannot be retrieved through `ExperienceBundle`. Enhanced LWR sites must be retrieved through `DigitalExperienceBundle` and their associated metadata types. If `DigitalExperienceBundle`, `DigitalExperienceConfig`, `Network`, `CustomSite`, and the applicable dependencies are retrieved successfully, the `ExperienceBundle` failure can be treated as a non-impacting warning and does not indicate that the Enhanced LWR site metadata was omitted.

### Restore/Replicate

#### **CANNOT\_INSERT\_UPDATE\_ACTIVATE\_ENTITY**

This error is a result of an issue stemming from a trigger in the Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in the 'Error' column.
2. Use the option to disable the triggers in the job configuration. For the triggers that cannot be disabled via metadata API, manually disable the triggers in Salesforce and re-run the job.

#### CANNOT\_EXECUTE\_FLOW\_TRIGGER

* Typical error message - We can't save this record because the ‘Online Applicant Validation’ process failed. Give your Salesforce admin these details. An error occurred when executing a flow interview. Error ID: 1545064308-45750 (1670083917)
* This error typically indicates that there is a Process Builder process / Flow in place that is causing the upsert operation to fail.

**Resolution steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Locate the process builder process / flow that caused the error. Temporarily disable the automation and rerun the job to restore/replicate failed records.
3. Alternatively, the job can be retried by specifying a lower batch size in the job config, which prevents the process builders/flows from hitting the parallel processing limits in Salesforce.

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

This error occurs when the failure of a required parent record (related through master-detail/required lookup) leads to the failure of its associated child records.

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
4. If it is a lookup relationship, then ensure the parent object is included in the job.

#### CANNOT\_UPDATE\_CONVERTED\_LEAD

This error is due to a Lead record once converted (to a contact) becomes read only, which prevents you from updating the lead.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. You can check to ensure that the lead is converted by checking the isConverted field.

#### FIELD\_INTEGRITY\_EXCEPTION

This error typically occurs when upsert tried to populate a lookup field with a wrong ID, either because the parent failed or AutoRABIT Vault is unable to recognize the parent record ID.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Need to pass the correct ID for a lookup field.

#### INVALID\_OPERATION: Too many files in zip

* Typical error message - Metadata deployment error...com.sforce.ws.SoapFaultException
* This error is generated when there are more than 10,000 files in the .zip file, which violates the governor limit.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on logs-> view error in the 'Error' column.
2. Reduce the number of metadata components restored/replicated in each job to less than 10,000 files.

#### **RECORD-TYPE ACCESS ISSUE**

This error indicates that the Salesforce user authenticated on AutoRABIT Vault doesn’t have access to some record types of an object(s).

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Give appropriate access using profiles and permissions to the Salesforce user authenticated on AutoRABIT Vault.

#### UNKNOWN USER PERMISSION

This error is generated when the required user permissions are missing in Salesforce.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> view error in 'Error' column.
2. Assign user to the desired permission set in Salesforce.

#### INVALID RECORD TYPE ID FOR THE USER

* Typical error message - Record Type ID: this ID value isn't valid for the user: 012D0000000BfaLIAS:RecordTypeId --
* This error is generated when the Salesforce user authenticated on AutoRABIT Vault doesn’t have access to some record types of an object(s).

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Give appropriate access using profiles and permissions to the Salesforce user authenticated on AutoRABIT Vault.

#### CANNOT\_INSERT\_UPDATE\_ACTIVATE\_ENTITY

* Typical error message - SFSSDupeCatcher.SSDupeCatcherContactTrigger: System.LimitException: Apex CPU time limit exceeded
* Error is generated by Triggers preventing the records from getting loaded in the destination Org.

**Resolution Steps:**

1. Click on Replicate/restore job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. Disable the triggers on the destination Org either by using the option to disable triggers in AutoRABIT Vault or by performing the same in the Salesforce Org.
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
3. For more information, go to[![](file:///C:/Users/shannan.zerance/AppData/Local/Packages/oice_16_974fa576_32c1d314_278d/AC/Temp/msohtmlclip1/01/clip_image001.png)Feed Item Detail | Salesforce Trailblazer Community](https://developer.salesforce.com/forums/?id=906F0000000D9CuIAK)&#x20;

***

### Replicate

#### DUPLICATE\_VALUE

Failures occur when such records are already present in the destination.

**Resolution Steps:**

1. Click on Replicate job summary-> Click on Failure records-> download details-> view error in 'Error' column.
2. An existing automation is blocking the upsert operation. Try disabling the automation if necessary.
3. If you would like AutoRABIT Vault to recognize the existing records in the destination that are created/transferred outside of AutoRABIT Vault, you can configure the unique identifier for the object and enable the option ‘Prevent duplicate record creation using unique identifiers' in replicate job config to avoid AutoRABIT Vault from attempting to recreate an existing record matching the value in the unique identifier specified.
4. For steps on how to configure unique identifiers, go to this link:

&#x20;[Unique Identifier (UID) | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/vault/configuring-vault/registering-salesforce-org/unique-identifier-uid)

***

### Limitations

#### **Restoration of System-Generated Chatter-Feed Items**

* **Issue**: Salesforce does not allow the restoration of chatter-feed items generated by the system.
* **Details**: Only feed items manually added by users to the chatter feed can be restored.
* **Error Message**: Attempting to restore system-generated chatter-feed items will result in the error: "Required field missing: Body."

#### **Restoration of Shared Objects Data**

* **Issue**: Salesforce does not permit the restoration of data in shared objects generated by sharing rules.
* **Details**: Only manually added share-related records in the shared object can be restored.

#### **Installed Packages**

* **MuleSoft** operates as an installed package component in Salesforce. Consequently, it cannot be backed up, restored, or replicated using API calls.&#x20;
* Installed packages, which includes **MuleSoft** or anything related to Mule, cannot be backed up directly; they must be obtained from the Salesforce AppExchange platform and installed.

**File Size Limits**

* **Issue:** If the metadata zip file exceeds the **file size limit of 39 MB**, then AutoRABIT Vault cannot restore the file to the destination Org.&#x20;
* **Details**: Use the workbench to restore larger files.&#x20;
* **Error Message in the UI logs**: "Metadata ZIP file exceeds the maximum allowed size of 39 MB. Please refer to the [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/) for more details.”&#x20;
* **Additional Info**: Refer to this [Salesforce article](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_metadata.htm) for more information on file size limitations.
