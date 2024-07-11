# Delete Salesforce Data

The following articles describe using **Single Dataloader** to delete data from Salesforce. To delete data, all you need is a CSV file that contains the IDs of the objects you want to delete in one of the columns. Once you have this, proceed with the instructions below.

1. Log in to your ARM account.
2. Hover your mouse over the **`Dataloader`** module and choose the **`Dataloader`** option.
3. Click **`Delete`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (79) (1).png" alt=""><figcaption></figcaption></figure>

4. Choose your [**`Salesforce Org`**](../../../arm-administration/registration/salesforce-org/) and your org environment (**`Production or Development Edition`**, **`Sandbox`**, or **`Pre-Release`**).
5. The corresponding **`URL`** and your **`Username`** are automatically generated based on the above selection.
6. Click **`Login and Fetch Objects`** to fetch all the objects from your Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (80) (1).png" alt=""><figcaption></figcaption></figure>

7. Select the object you wish to delete the data. For example, **`Account`**, **`Contact`**, **`Lead`**, etc. You can use the **`search`** function to search through your objects and the **`filter`** button to filter your standard/custom objects quickly.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (81) (1).png" alt=""><figcaption></figcaption></figure>

9. Import your file from your local directory on the next screen. Upload the **`CSV`** file you wish to import by clicking the **`Upload`** button.

<figure><img src="../../../../../.gitbook/assets/image (82) (1).png" alt=""><figcaption></figcaption></figure>

10. A notification pop-up will display the number of records that will be impacted. Click **`OK`**.

<figure><img src="../../../../../.gitbook/assets/image (83) (1).png" alt=""><figcaption></figcaption></figure>

11. The next step is to prepare your field mappings. Field mappings match columns in your CSV to fields in your Salesforce Org.
12. You can automatically map the members and the fields using **`Automap`**. It compares the destination fields with the fields available in uploaded CSV files, and if both match, the value is selected automatically.

<figure><img src="../../../../../.gitbook/assets/image (84) (1).png" alt=""><figcaption></figcaption></figure>

13. The number of fields mapped out of the total number of fields is displayed below the **`Automap`** checkbox.
14. Use the **`search`** option to look up a field by name from the long list to map it.
15. Use the **`Filter`** dropdown to choose which fields to display:
    * **`All:`** Displays all fields, whether they have been mapped or not.
    * **`Mapped:`** Displays only the fields which have been mapped yet.
    * **`Unmapped:`** Displays only the fields which haven't been mapped yet.\
      After selecting the filter, the list updates automatically as you map or unmap each field.
16. Make sure you have mapped all the required fields. Otherwise, you can't move forward. Click **`Next`**.
17. On the **`Process Summary`** screen, you can:

    <figure><img src="../../../../../.gitbook/assets/image (85) (1).png" alt="" width="563"><figcaption></figcaption></figure>

    * Give the process/job a **`Name`**.
    * Select the **`Category`**. Categories are used to classify and group similar processes having similar functionality. In simple terms, you are assigning similar processes to a category. You can either select an existing category or create a new category by clicking the **`+`** icon.
    * View the main **`Object`**.
    * View the operation **`Type`** (**`Delete`**).
    * View the number of impacted **`Records`**.
    * **`Use Bulk API`**.About Bulk APIThe Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets. You can use the Bulk API to process jobs in **serial** or **parallel** mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing better data throughput overall.
18. You can schedule your tasks so they start running regularly. You can choose between **`Daily`**, **`Weekly`**, or **`On-demand`** schedules.
19. Finally, click **`Save`** to save your task and run it later.
20. Your task is listed at the top in the **`Dataloader Summary`** screen.
21. Click **`Run`** to run the Dataloader immediately before the scheduled time.

<figure><img src="../../../../../.gitbook/assets/image (86) (1).png" alt="" width="563"><figcaption></figcaption></figure>

22. Select the criteria for the dataloader process to continue:

| Configurations                                                           | Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Use Bulk API (Batch API will be used if the option is not enabled)`** | <p>The Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets.<br><br>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously.<br><br>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.<br><br><strong>Note:</strong> When performing multiple delete operations into the same destination org while the ongoing jobs are still running, choosing the <strong><code>Serial Mode</code></strong> is recommended.</p> |
| **`Batch Size`**                                                         | <p>Whenever the Bulk API checkbox is left unchecked, the Batch API is used.<br><br>Salesforce Batch API is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process large numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In those cases, Bulk API is the best option. Batch API processes data in smaller batches than Bulk API, resulting in a higher API call usage per operation on large volumes of data.<br><br><strong>Note:</strong> <em>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</em></p>                                                                                                                                      |
| **`Use UTF-8 file encoding for file read and write operations`**         | Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled in your data exclusively containing English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default as per Salesforce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

23. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/image (87) (1).png" alt="" width="494"><figcaption></figcaption></figure>

24. The **`Results of Last Run`** section shows the number of successful or failed records deleted. The values in this field are updated dynamically while the job is still running. You can view the records or download them to your local system. The records are generated in CSV format.

<figure><img src="../../../../../.gitbook/assets/image (88) (1).png" alt="" width="563"><figcaption></figcaption></figure>

25. The number of impacted records can be seen in the **`Records`** section. The value in this field is updated dynamically while the job is still running.

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (78) (1).png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Edit:`** Modifies or updates the process details.&#x20;
2. **`Abort:`** Aborts the process while it is still running.
3. **`Schedule:`** Sets the schedule at which the process must run.
4. **`Delete:`** Deletes the delete process.
5. **`Log:`** Provides information about the execution of the deleted task.
6. **`VR/WFR:`** ARM lists all the validations/workflow rules that were set. The UI lists all the validation rules, and users must enable them for the disabled validation rules (if required). For more info, refer to the article: [Validation/ Workflow Rules](../validation-workflow-rules.md). Sample VR/WFR attached:

<figure><img src="../../../../../.gitbook/assets/image (76) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (77) (1).png" alt=""><figcaption></figcaption></figure>

7. **`Clone:`** Creates a copy (clone) of the insert process. Operation type and object name are displayed. Enter the **`Process Name`** in the field. The default **`Salesforce Org`** is automatically selected. To choose a different org, use the dropdown list. Select the **`Choose Different Data CSV File`** check box to upload a different CSV file. Finally, click **`Clone`**.

<figure><img src="../../../../../.gitbook/assets/image (74) (1).png" alt="" width="399"><figcaption></figcaption></figure>
