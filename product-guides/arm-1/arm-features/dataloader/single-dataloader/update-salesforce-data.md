# Update Salesforce Data

The basic DL provides a potent yet easy-to-use application to update data into Salesforce seamlessly.&#x20;

**Step-By-Step Guide:**

1.  On logging into the nCIno application, navigate to the Dataloader to initiate the creation of the "Update" job.

    <figure><img src="../../../../../.gitbook/assets/Update - 1.png" alt=""><figcaption></figcaption></figure>
2.  On the "Login and select object" section of the flow login to the ORGs and select the required objects.

    <figure><img src="../../../../../.gitbook/assets/Update - 2.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 3.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 4 (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 5.png" alt=""><figcaption></figcaption></figure>
3. After selecting the required object, click **Next** to proceed to the **Field Mapping** section.
4. Upload the appropriate CSV file at this step to update data into Salesforce seamlessly
5.  Either click on "Choose File" or "Drop the file" to upload the CSV.

    <figure><img src="../../../../../.gitbook/assets/Update - 6.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 7.png" alt=""><figcaption></figcaption></figure>
6.  After adding the file, proceed to upload it to enable the necessary field mappings.

    <figure><img src="../../../../../.gitbook/assets/Update - 8.png" alt=""><figcaption></figcaption></figure>
7.  On successful file upload a success message will be displayed

    <figure><img src="../../../../../.gitbook/assets/Update - 9.png" alt=""><figcaption></figcaption></figure>
8. Click on "AutoMap" option to map the fields from the source against the destination.
9.  Click on the <img src="../../../../../.gitbook/assets/image.png" alt="" data-size="line"> icon to observe the options

    <figure><img src="../../../../../.gitbook/assets/Update - 9.1.png" alt=""><figcaption></figcaption></figure>
10. The lookup field will have the "Look up" option against it at the "Salesforce field" column. This mapping is useful for mapping different fields.

    <figure><img src="../../../../../.gitbook/assets/Update - 10.png" alt=""><figcaption></figcaption></figure>
11. Selecting "Look via" option will provide a drop-down to select the required fields.

    <figure><img src="../../../../../.gitbook/assets/Update - 11.png" alt=""><figcaption></figcaption></figure>
12. For the selected fields, the further action can be specified using the two radio button options available.

    <figure><img src="../../../../../.gitbook/assets/Update - 12.png" alt=""><figcaption></figcaption></figure>

    1. **Use first match in multiple results:**\
       If multiple records match the selected non-unique field (e.g., several accounts named _GenePoint_), the Data Loader selects the first match automatically.
    2. **Mark record with an error if more than one match is found:**\
       If enabled, ARM Data Loader flags the row with an error stating multiple matches exist. You can resolve this by fixing the data in Salesforce or by manually providing the correct ID in the CSV and re-uploading.
13. On successful field mapping, click "Next" to move to the "Schedule" section of the flow.

    <figure><img src="../../../../../.gitbook/assets/Update - 13.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 14.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 15 (3).png" alt=""><figcaption></figcaption></figure>
14. On setting up the required schedule, click on "Next" to move to the "Process Details" section of the flow

    <figure><img src="../../../../../.gitbook/assets/Update - 16 (2).png" alt=""><figcaption></figcaption></figure>
15. To assign a job to a group, select a group from the list or create a new group by clicking on the "+" icon
16. For faster processing of the records, use the "BULK API" option.

    <figure><img src="../../../../../.gitbook/assets/Update - 17.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 18.png" alt=""><figcaption></figcaption></figure>
17. Click the **"Save"** button to save the job configuration. Upon saving, the flow will automatically redirect to the **Job List** page, where the newly created job will be displayed along with existing jobs.
18. Click on the "Run" option to run the job.

    <figure><img src="../../../../../.gitbook/assets/Update - 19.png" alt=""><figcaption></figcaption></figure>
19. Clicking the **"Run"** button directs the flow to the **Run Configuration** screen, where the available automation options for the job can be reviewed and configured as needed.

    <figure><img src="../../../../../.gitbook/assets/Update - 20.png" alt=""><figcaption></figcaption></figure>
20. Select the criteria you can set for the data loader process to continue:

| Configurations                                                     | Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Bulk API (Batch API will be used if the option is not enabled) | <p>The Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets.<br><br>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously.<br><br>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.<br><br><strong>Note:</strong> When performing multiple insert operations into the same destination org while the ongoing jobs are still running, choosing the <strong><code>Serial Mode</code></strong> is recommended.</p> |
| Batch Size                                                         | <p>Whenever the Bulk API checkbox is left unchecked, the Batch API is used.<br><br>Salesforce Batch API is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process large numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In those cases, Bulk API is the best option. Batch API processes data in smaller batches than Bulk API, resulting in a higher API call usage per operation on large volumes of data.<br><br><strong>Note:</strong> <em>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</em></p>                                                                                                                                      |
| Disable workflow rules                                             | All the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Disable Validation Rules                                           | Validation rules verify that the data a user enters in a record meets the specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Insert/Update with null values.                                    | This will either insert or update record field values with null (if the value is null in source org) in destination org.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Use UTF-8 file encoding for file read and write operations         | Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled in your data exclusively containing English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default as per Salesforce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

23. Click **`Run`**.
24. A new CSV file can also be input using the "﻿Choose Different Data CSV File" option.

    <figure><img src="../../../../../.gitbook/assets/Update - 20.1.png" alt=""><figcaption></figcaption></figure>
25. Click on the "Run" button to run the job.

    <figure><img src="../../../../../.gitbook/assets/Update - 22.png" alt=""><figcaption></figcaption></figure>
26. Once the job run is completed, the results can be observed under the "Success" & "Failure" of the "Results of Last Run".

    <figure><img src="../../../../../.gitbook/assets/Update - 23.png" alt=""><figcaption></figcaption></figure>
27. Cick on the magnifying glass icon under the respective "Success & Failure" sections to observe the actual "Success & Failure" records.

    <figure><img src="../../../../../.gitbook/assets/Update - 23 (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 24.png" alt=""><figcaption></figcaption></figure>
28. Click on the ellipses icon to observe the job optoins.

    <figure><img src="../../../../../.gitbook/assets/Update - 25.png" alt=""><figcaption></figcaption></figure>
29. Click on the "Edit" option to edit the job created

    <figure><img src="../../../../../.gitbook/assets/Update - 26.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 27.png" alt=""><figcaption></figcaption></figure>
30. Click on "Schedule" to observe the set schedule and create any schedules

    <figure><img src="../../../../../.gitbook/assets/Update - 28.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 29.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/Update - 30.png" alt=""><figcaption></figcaption></figure>


31.



























The following article describes using **Single Dataloader** to update data in Salesforce. The data is updated via a CSV file.

1. Log in to your ARM account.
2. Hover your mouse over the [**`Dataloader`**](https://www.autorabit.com/blog/10-benefits-of-salesforce-data-loader/) module and select **`Dataloader`**.
3. Click **`Update`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Choose your **`Salesforce Org`** and your org environment (**`Production or Development Edition`**, **`Sandbox`**, or **`Pre-Release`**).
5. The corresponding **`URL`** and your **`Username`** are automatically generated based on the above selection.
6. Click **`Login and Fetch Objects`** to fetch all the objects from your Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Select the object for which you wish to update the data. For example, **`Account`**, **`Contact`**, **`Lead`**, etc. You can use the **`Search`** function to search through your objects and the **`filter`** button to filter your standard/custom objects quickly.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (51) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Import your file from your local directory on the next screen. Upload the **`CSV`** file you wish to import by clicking the **`Upload`** button.

<figure><img src="../../../../../.gitbook/assets/image (52) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. A notification pop-up will display the number of records that will be impacted. Click **`OK`**.

<figure><img src="../../../../../.gitbook/assets/image (53) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

11. The next step is to prepare your field mappings. Field mappings match columns in your CSV to fields in your Salesforce Org.
12. You can automatically map the members and the fields using **`Automap`**. It compares the destination fields with the fields available in uploaded CSV files, and if both match, the value is selected automatically.

<figure><img src="../../../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

13. The number of fields mapped out of the total number of fields is displayed below the **`Automap`** checkbox.
14. Use the **`search`** option to look up a field by name from the long list to map it.
15. Use the **`Filter`** dropdown to choose which fields to display:
    * **`All:`** Displays all fields, whether they have been mapped or not.
    * **`Mapped:`** Displays only the fields which have been mapped yet.
    * **`Unmapped:`** Displays only the fields which haven't been mapped yet.\
      After selecting the filter, the list updates automatically as you map or unmap each field.
16. Make sure you have mapped all the required fields. Otherwise, you can't move forward. Click **`Next`**.
17. On the **`Process Summary`** screen, you can:

    <figure><img src="../../../../../.gitbook/assets/image (55) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

    * Give the process/job a **`Name`**.
    * Select the **`Category`**. Categories are used to classify and group similar processes having similar functionality. In simple terms, you are assigning similar processes to a category. You can either select an existing category or create a new category by clicking the **`+`** icon.
    * View the main **`Object`**.
    * View the operation **`Type`** (**`Update`**).
    * View the number of impacted **`Records`**.
    * **`Use Bulk API`**.About Bulk APIThe Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets. You can use the Bulk API to process jobs in **serial** or **parallel** mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing better overall data throughput.
18. You can schedule your tasks so they start running regularly. You can choose between **`Daily`**, **`Weekly`**, or **`On-demand`** schedules.
19. Finally, click **`Save`** to save your task and run it later.
20. Your task is listed on top of the lists in the **`Dataloader Summary`** screen.
21. Click **`Run`** to run the Dataloader immediately before the scheduled time.

<figure><img src="../../../../../.gitbook/assets/image (56) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

22. Select the criteria you can set for the dataloader process to continue:

| Configurations                                                           | Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Use Bulk API (Batch API will be used if the option is not enabled)`** | <p>The Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets.<br><br>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously.<br><br>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.<br><br><strong>Note:</strong> When performing multiple update operations into the same destination org while the ongoing jobs are still running, choosing the <strong><code>Serial Mode</code></strong> is recommended.</p> |
| **`Batch Size`**                                                         | <p>Whenever the Bulk API checkbox is left unchecked, the Batch API is used.<br><br>Salesforce Batch API is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process large numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In those cases, Bulk API is the best option. Batch API processes data in smaller batches than Bulk API, resulting in a higher API call usage per operation on large volumes of data.<br><br><strong>Note:</strong> <em>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</em></p>                                                                                                                                      |
| **`Disable workflow rules`**                                             | All the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **`Disable Validation Rules`**                                           | Validation rules verify that the data a user enters in a record meets the specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **`Insert/Update with null values`**                                     | This will either insert or update record field values with null (if the value is null in source org) in destination org.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **`Use UTF-8 file encoding for file read and write operations`**         | Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled in your data exclusively containing English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default as per Salesforce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

23. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/image (57) (1) (1) (1) (1).png" alt="" width="491"><figcaption></figcaption></figure>

24. The number of successful or failed records updated can be seen in the **`Results of Last Run`** section. The values in this field are updated dynamically while the job is still running. You can view the records or download them to your local system. The records are generated in CSV format.

<figure><img src="../../../../../.gitbook/assets/image (58) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

25. The number of impacted records can be seen in the **`Records`** section. The value in this field is updated dynamically while the job is still running.

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Edit:`** Modifies or updates the process details.&#x20;
2. **`Abort:`** Aborts the process while it is still running.
3. **`Schedule:`** Sets the schedule at which the process must run.
4. **`Delete:`** Deletes the update process.
5. **`Log:`** Provides information about the execution of the updated task.
6. **`VR/WFR:`** ARM lists all the validations/workflow rules that were set. The UI lists all the validation rules, and users must enable them for the disabled validation rules (if required). For more info, refer to the article: [Validation/ Workflow Rules](../../../../arm/arm-features/dataloader/validation-workflow-rules.md). Sample VR/WFR attached:

<figure><img src="../../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. **`Clone:`** Creates a copy (clone) of the insert process. Operation type and object name are displayed. Enter the **`Process Name`** in the field. The default **`Salesforce Org`** is automatically selected. To choose a different org, use the dropdown list. Select the **`Choose Different Data CSV File`** check box to upload a different CSV file. Finally, click **`Clone`**.

<figure><img src="../../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="398"><figcaption></figcaption></figure>
