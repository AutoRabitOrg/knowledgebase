# Data Loader Pro

**Data Loader Pro** is an advanced feature ARM provides for transferring data from the source sandbox to the destination sandbox more conveniently and automatically handles the parent-child relationship. Migrating the Salesforce data/objects to more than one object-supporting hierarchy can be easily achieved using the **Data Loader Pro** feature in ARM.&#x20;

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

While performing **Data Loader Pro** on the objects for the first time, ensure you perform [Data Loader Configuration](dataloader-configuration.md) among the same orgs on all the objects included in your Data Loader Pro job. This is a one-time operation.

Data Loader plays an essential role in data migration from source sandbox to destination sandbox. However, in this data migration process, the chances of duplicate records being created always exist. To avoid this, ARM has developed a new feature that allows synchronizing between the orgs with the help of the ARM external ID **AutorabitExtid\_\_c** field.

### How to Perform a Data Loader Pro Operation <a href="#how-to-perform-a-dataloader-pro-operation" id="how-to-perform-a-dataloader-pro-operation"></a>

1. Log in to your ARM account.
2. Hover your mouse over the **`Data Loader`** module and select **`Data Loader Pro`**.
3. Click on **`Create New Job.`**

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, choose the **`Source Org`** and the **`Destination Org`** that automatically populate the selected sandbox's details.
5. Click **`Login and Fetch Objects`**.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Next, **`Select Master Object`**.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt="" width="353"><figcaption></figcaption></figure>

7. View the relationship between child objects/ancestor objects and the master object in the **`Schema (Grid View)`** section.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Change the grid view to a graph view by clicking the **`Switch to Graph View`** button. Click on the![](<../../../../.gitbook/assets/image (5) (1) (1) (1).png>) icon to view the graphical representation on full screen.

<figure><img src="../../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

## Filters and Mappings <a href="#filters-and-mappings" id="filters-and-mappings"></a>

For each object displayed, users can view the list of fields related to the corresponding object.

<figure><img src="../../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

### **Filters**

You can extract records within a specified limit using specifying criteria in the **`Filters`** section. You can even filter the details via **`Date`** or **`Date Literals`**. A date literal is a fixed expression representing a relative range of time, such as last month, this week, or next year. (Refer [here](https://developer.salesforce.com/docs/atlas.en-us.soql\_sosl.meta/soql\_sosl/sforce\_api\_calls\_soql\_select\_dateformats.htm) for the list of data literals supported).

Upload the **`CSV`** file (if required) if there is a large amount of data and it requires the filter for those records. The max file size supported is **10 MB**. Once the CSV is uploaded, click **`Auto-Populate`**. The filters are autopopulated for the selected field and operator based on the values of the chosen field in the uploaded CSV file.

Format for CSV file to filter records:

* ARM Data Loader Pro accepts CSV (comma-separated values) files. Use a spreadsheet program such as Microsoft Excel to create your CSV file.
* Ensure you have a column header and rows of data populated for all system-required fields, such as **`Account Name`** or **`Contact Last Name`**.
* There can be only one column header.&#x20;

For more information, see [Preparing the CSV file for Data Loader](preparing-the-csv-file-for-arm-dataloader.md).

<figure><img src="../../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

The **`Record Count Limit`** box limits the number of records extracted from the source, giving a value in this field.

Click **`Validate`** to fetch the number of records transferred from the source sandbox to the destination sandbox. Finally, click **`Apply`**.

### Skip Records

‘Skip Records’ can be enabled by entering a ‘0’ on the record count section under the filters or by selecting the ‘checkbox’ under the ‘Skip Records’ section.

To ‘Skip Records' using the filters, click on 'Filters.' ‘Skip Records’ will omit migrating an object to the destination.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Enter ‘0’ on the ‘Record Count’ field of the ‘Apply Filters’ page pop-up and click on ‘Validate’ to validate the query.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Upon completing the validation, click on ‘Apply’ to apply the inputs.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Select the checkbox to 'Skip Records' from migrating to the destination.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;Upon selecting the checkbox, a pop-up will ask for confirmation.

<figure><img src="../../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

Upon confirming, the checkbox will be selected to skip migrating those records to the destination with the following notification on filters applied.

<figure><img src="../../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

Click on the filters section of the object on which the 'Skip Records' is applied to observe the query builder and the Record Count.

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

When ‘Skip Records’ is selected, the record count is set to ‘0’ and the records from the selected object will not be migrated to the destination.

<figure><img src="../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

When unchecking the ‘checkbox’, skip records will be disabled on the object. The following message will ask for confirmation.

<figure><img src="../../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Upon clicking 'confirm,' the records from that particular object will be migrated to the destination. The following notification will be displayed when unchecking the checkbox.

<figure><img src="../../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

When ‘Skip Records’ is disabled, the record count that was set to ‘0’ in the filters and the query will be reset to blank and the records will be migrated to the destination.

### **Mappings**

Map the object fields between the source and destination sandboxes.

Using the **`Automap`** feature, you can map the fields automatically based on fetched object fields with destination fields. To set up manual mappings, automapping needs to be disabled. Click on **`Clear Mappings`** to remove the automapping and set up the desired manual mappings.

<figure><img src="../../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### **External ID Field Mapping**

In this section, you can use an external ID instead of a related record's Salesforce record ID to relate or associate records to each other as you process the Data Loader Pro operation. For example, if Object B has a lookup field to another Object A, you can use the values in a field marked as an **`External ID`** on Object A to relate the two (Object B to Object A records).

In the **`Source`** field, select the source whose values will be populated in the destination external ID field.

In the **`Destination`** field, select the required destination org whose values will remain unique for all the records.

<figure><img src="../../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** ARM does not support the automatic creation of an ExternalUniqueID. The user has to create this manually on both the Source Org and Destination Org.
{% endhint %}

### Process Details <a href="#process-details" id="process-details"></a>

Here in this section, fill in the process details listed below:&#x20;

1. Enter a **`Name`**  for the job.
2. Select the category in the **`Job Group`** field. This is important if you'd like to group related jobs into a single category. You can also create a new group and assign your job to this group.
3. **`Master Object`** and **`External ID`** are auto-populated.
4. Enter the **`User Name Suffix`** for the **`Source Org`** and the **`Destination Org`**. Below are some examples of usernames and the corresponding suffixes:

| Case 1      | User Name                                       | User Name Suffix |
| ----------- | ----------------------------------------------- | ---------------- |
| Source      | [jsmith@ar.com.src](mailto:jsmith@ar.com.src)   | src              |
| Destination | [jsmith@ar.com.dest](mailto:jsmith@ar.com.dest) | <p>dest<br></p>  |

| Case 2      | User Name                                     | User Name Suffix |
| ----------- | --------------------------------------------- | ---------------- |
| Source      | [jsmith@ar.qan.com](mailto:jsmith@ar.qan.com) | qan.com          |
| Destination | [jsmith@ar.aws.com](mailto:jsmith@ar.aws.com) | aws.com          |

| Case 3      | User Name                                       | User Name Suffix       |
| ----------- | ----------------------------------------------- | ---------------------- |
| Source      | [jsmith@ar.com](mailto:jsmith@ar.com)           | Empty (leave it blank) |
| Destination | [jsmith@ar.com.dest](mailto:jsmith@ar.com.dest) | dest                   |

| Case 4      | User Name                                     | User Name Suffix       |
| ----------- | --------------------------------------------- | ---------------------- |
| Source      | [jsmith@ar.com.src](mailto:jsmith@ar.com.src) | src                    |
| Destination | [jsmith@ar.com](mailto:jsmith@ar.com)         | Empty (leave it blank) |

5. Additionally, users can ignore certain records related to community users by selecting the **`Ignore Community Users`** checkbox.

<figure><img src="../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

### Masking Wizard <a href="#masking-wizard" id="masking-wizard"></a>

Data masking refers to changing certain data elements within a data store so the structure remains similar while the information is altered to protect sensitive information. It ensures sensitive customer information is unavailable beyond the permitted production environment.

Under the **`Masking Wizard`** section, click on **`New`** to add a masking rule.

<figure><img src="../../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

In the **`Masking Form`** screen, do the following:

<figure><img src="../../../../.gitbook/assets/image (19).png" alt="" width="426"><figcaption></figcaption></figure>

1. **`Select Object`** for masking and choose the **`Field Type`**.
2. Choose the **`Masking Style`**:
   * **`Prefix`**: This option adds the character before the selected field name. For example, if the field value in source org is ABC, and the prefix masking value is kept as 123, then the final field value being deployed will be 123.ABC.
   * **`Suffix`**: This option adds the character after the selected field name. For example, if the field value in source org is ABC, and the suffix masking value is kept as 123, then the final field value being deployed will be ABC.123.
   * **`Replace`**: This option replaces the selected field name with the character you enter in the **`Masking Value`** field. For example, if the field value in source org is ABC, and the replace masking value is kept as 123, then the final field value being deployed will be 123.
   * **`Shuffle`**: Shuffles the data in the column (like a deck of cards) and leaves the other columns untouched. For example, if the field value in source org is ABCDE, then the final field value being deployed will be DCBEA.
   * **`Generate Random`**: This option helps mask the original value with a random value within a specified range. For example, if the field value in source org is ABC, and the random string length value is set to 7, then the deployed field value would be similar to 15d3aRG.

{% hint style="info" %}
**Important Note:** Masking is not applicable if the field value for the record is empty.
{% endhint %}

#### Process Schedule <a href="#process-schedule" id="process-schedule"></a>

In the Scheduling procedure, the user can schedule the process it must run.

1. **`Daily:`** The process will run every day at the scheduled or set time interval.
2. **`Weekly:`** The process will run weekly on the scheduled day and time.
3. **`No schedule:`** The process is only saved; you can run it when required.

<figure><img src="../../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

Finally, click on **`Save`** to complete the initial process. You will be redirected to the **`Dataloader Pro Summary`** page, where the Data Loader process initiated can be seen at the top of the list.

<figure><img src="../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### Job Configuration Settings

1. This feature will allow the user to select the required job settings to disable workflow rules, disable validation rules etc., as required during the job creation.

<figure><img src="../../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

2. Once the job is saved the selected job configuration settings will be saved.
3. On running the job, the retained job settings will be displayed on the pop-up, “Run Configuration”.

<figure><img src="../../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

4. Any changes made during the run of the job will only affect that individual job run.
5. To permanently change the configured settings during the job creation, the user has to edit the created job and change the settings and save the job.

### Running the Data Loader Pro Job

Select your job from the **`Data Loader Pro Summary`** screen and click on **`Run`**. This option allows you to run the processes created in the selected category.

<figure><img src="../../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (25).png" alt="" width="533"><figcaption></figcaption></figure>

The table below lists the configurations to choose from, along with their descriptions:

| Serial Number | Configurations                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1             | **`Disable workflows`**                                                    | The workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                   |
| 2             | **`Disable validation rules`**                                             | Validation rules verify that the data a user enters in a record meets the criteria you specify before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                               |
| 3             | **`Use Bulk API`**                                                         | <p>The Bulk API is based on REST principles and optimized for inserting, updating, and deleting large data sets.</p><p>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. </p><p><strong>Note</strong>: When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing your overall run better data throughput.</p> |
| 4             | **`Insert/update with null values`**                                       | Insert/update with null values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 5             | **`Minimize multiple references between the same objects`**                | When there are multiple references between the same objects, unnecessary API calls are not triggered upon selecting this option.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 6             | **`Automatically apply master object filter on other dependency objects`** | All objects in the hierarchy are calculated based on the Master Object filters; this option avoids extra records addition due to self-references and multiple references.                                                                                                                                                                                                                                                                                                                                                                                     |
| 7             | **`Data encryption for data files`**                                       | Data encryption for data files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 8             | **`Incremental data migration`**                                           | After a data-loading process is done, only the newly added records are transferred into the destination sandbox.                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### More Options <a href="#more-options" id="more-options"></a>

1. **`Edit:`** Edits the processes in the selected category to rerun them.
2. **`Abort:`** Aborts the process.
3. **`Schedule:`** Schedules the data-loading process for the selected category.
4. **`Clone:`** Clones the respective Data Loader Pro job.
5. **`Log:`** Provides information about the process execution.

<figure><img src="../../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

#### Schema (Grid View) <a href="#schema-grid-view" id="schema-grid-view"></a>

This section lets you view the master object and its related information for the test environment setup job. For the setup run with disabled validation/workflow rules, ARM lists all the validation rules set under **`VR/WFR`** section. The UI lists all the workflow/validation rules; users must enable them for the disabled rules (if required).

<figure><img src="../../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>
