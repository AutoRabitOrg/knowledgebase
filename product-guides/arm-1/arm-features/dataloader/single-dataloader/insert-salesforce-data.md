# Insert Salesforce Data

**The "Basic DL" feature offers a user-friendly and efficient way to insert data into Salesforce using a CSV file.** It simplifies the data load process while maintaining accuracy and speed, making it ideal for quick and straightforward data uploads.

**Step-By-Step Guide:**

1. Navigate to the Basic DL application by loging into the nCino application
2.  Click on the Create button to observe the **"Insert"** option to initiate the creation of the **"Basic DL"** job.

    <figure><img src="../../../../../.gitbook/assets/1 - Insert.png" alt=""><figcaption></figcaption></figure>
3.  Clicking on "Insert" will navigate the flow to the "Login and select object" section.

    <figure><img src="../../../../../.gitbook/assets/2 - Insert (3).png" alt=""><figcaption></figcaption></figure>
4.  Click on login to fetch the object details

    <figure><img src="../../../../../.gitbook/assets/3 - Insert.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/4 - Insert.png" alt=""><figcaption></figcaption></figure>
5.  Choose an object anb move to the next screen to choose the file to inset the data.

    <figure><img src="../../../../../.gitbook/assets/5 - Insert.png" alt=""><figcaption></figcaption></figure>
6.  After uploading the file, click on the "Upload File" option to upload the file into the system.

    <figure><img src="../../../../../.gitbook/assets/6 - Insert.png" alt=""><figcaption></figcaption></figure>
7.  On successful upload of a file, the success message will be displayed

    <figure><img src="../../../../../.gitbook/assets/7 - Insert.png" alt=""><figcaption></figcaption></figure>
8.  The application will read the header of the uploaded file and populates the same information on the screen in the section below.

    <figure><img src="../../../../../.gitbook/assets/8 - Insert.png" alt=""><figcaption></figcaption></figure>
9.  An "Automap" option will appear as the field details get populated on the screen. Enabling this option maps the fields from the source against the fields on the destination ORG.

    <figure><img src="../../../../../.gitbook/assets/9 - Insert (1).png" alt=""><figcaption></figcaption></figure>
10. Specify the criteria for matching fields to fetch records from the source system. This setting determines how the data should be identified and retrieved during processing.
11. Click on the drop-down beside the object name and select the required field from the list.

    <figure><img src="../../../../../.gitbook/assets/10 - Insert (1).png" alt=""><figcaption></figcaption></figure>
12. Observe the <img src="../../../../../.gitbook/assets/image (1868).png" alt="" data-size="line"> icon beside the "Automap" option, clicking that will provide the options:

    1. All: Will display all of the fields existing from the mapping
    2. Mapped: will display the fields mapped through the "Automap" option
    3. Unmapped: will display the fields that remain unmapped after enabling the "Automap" option.

    <figure><img src="../../../../../.gitbook/assets/10.1 - Insert.png" alt=""><figcaption></figcaption></figure>
13. Click "Next" to continue to the "Schedule" section of the flow.
14. Observe the various scheduling options available under "Schedule" section.

    <figure><img src="../../../../../.gitbook/assets/11 - Insert.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/12 - Insert.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/13 - Insert.png" alt=""><figcaption></figcaption></figure>
15. On completing the scheduling, click on "Next"  to continue to "Process Details".

    <figure><img src="../../../../../.gitbook/assets/14 - Insert.png" alt=""><figcaption></figcaption></figure>
16. Input a name for the job and click on  "Save" to save the job.

    <figure><img src="../../../../../.gitbook/assets/15 - Insert.png" alt=""><figcaption></figcaption></figure>
17. **Use Bulk API**\
    The Bulk API, built on REST principles, is designed for high-volume operations such as inserting, updating, or deleting large data sets. It supports both serial and parallel processing modes:

    * **Serial Mode:** Processes batches one after another in sequence.
    * **Parallel Mode:** Processes multiple batches simultaneously to increase throughput.

    Enabling this option allows the system to execute the job more efficiently by leveraging concurrent batch processing where possible, thereby improving overall performance for large-scale data operations.
18. On saving the job, the flow will navigate to the job list page.
19. Observe and click on the "Run" button to initiate the job run

    <figure><img src="../../../../../.gitbook/assets/16 - Insert.png" alt=""><figcaption></figcaption></figure>













































The following articles describe using the **Single Dataloader** to insert data into Salesforce. The data is inserted via a CSV file.

1. Log in to your ARM account.
2. Hover your mouse over the [**`Dataloader`**](https://www.autorabit.com/blog/10-benefits-of-salesforce-data-loader/) module and select **`Dataloader`**. The **Dataloader** screen is best viewed when the zoom setting is **75%** on your Chrome/Firefox browser.
3. Click **`Insert`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (31) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Choose your **`Salesforce Org`** and your org **Environment** (_Production_ or _Development &#x65;_&#x64;ition, _Sandbox_, or _Pre-Release_).
5. The corresponding **`URL`** and your **`Username`** are automatically generated based on the above selection.
6. Click **`Login and Fetch Objects`** to fetch all the objects from your Salesforce org.

<figure><img src="../../../../../.gitbook/assets/image (32) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Select the object in which you wish to insert the data. For example, **Account**, **Contact**, **Lead**, etc. You can use the **`search`** function to search through your objects and the **`filter`** button to filter your standard/custom objects quickly.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (33) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

9. You can import your file from your local directory on the next screen. Upload the **`CSV`** file you wish to import by clicking the **`Upload`** button.
10. A notification pop-up will display the number of records that will be impacted. Click **`OK`**.
11. The next step is to prepare your field mappings. Field mappings match columns in your CSV to fields in your Salesforce org. When clicking on a salesforce field, use the **"Quick Search"** function to search through those and the quick filter tabs to find your _Required_, _Unmapped_, _IDs_ and _Custom fields_.

<figure><img src="../../../../../.gitbook/assets/image (34) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="415"><figcaption></figcaption></figure>

12. You can automatically map the members and the fields using **`Automap`**. It compares the destination fields with the fields available in uploaded CSV files, and if both match, the value is selected automatically.

<figure><img src="../../../../../.gitbook/assets/image (35) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

13. The number of fields mapped out of the total number of fields is displayed below the **`Automap`** checkbox.
14. Use the **`search`** option to look up a field by name from the long list to map it.
15. Use the **`Filter`** dropdown to choose which fields to display:
    * **`All:`** Displays all fields, whether they have been mapped or not.
    * **`Mapped:`** Displays only the fields which have been mapped yet.
    * **`Unmapped:`** Displays only the fields which haven't been mapped yet.\
      After selecting the filter, the list updates automatically as you map or unmap each field.
16. Make sure you have mapped all the required fields. Otherwise, you can't move forward. Click **`Next`**.Lookup Reference ObjectsIf you need an object ID but don't have it, you can use the lookup function to retrieve it dynamically. For example, if you're importing Contacts with the **"Account name"** but not the **"ID,"** you can use the [lookup feature](../../../../arm/arm-features/dataloader/single-dataloader/using-data-loader-with-lookups.md) to find it.

<figure><img src="../../../../../.gitbook/assets/image (36) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="448"><figcaption></figcaption></figure>

17. On the **`Process Summary`** screen, you can:

    * Give the process/job a **name**.
    * Select the **`Category`**. Categories are used to classify and group similar processes having similar functionality. In simple terms, you are assigning similar processes to a category. You can select an existing category or create a new one by clicking the **`+`** icon.
    * View the main object.
    * View the operation **`Type`** _(Insert)_.
    * View the number of impacted **records**.
    * Use **Bulk API**.About Bulk APIThe **Bulk API** is based on REST principles and is optimized for inserting, updating, and deleting large data sets. You can use the **Bulk API** to process jobs in **serial** or **parallel** mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. When you run a bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing your overall run with better data throughput.

    <figure><img src="../../../../../.gitbook/assets/image (37) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
18. You can schedule your tasks so they start running regularly. You can choose between **`Daily`**, **`Weekly`**, or **`On-demand`** schedules.
19. Finally, click **`Save`** to save your task and run it later.
20. Your task is listed at the top of the list on the **`Dataloader Summary`** screen.
21. Click **`Run`** to start Dataloader immediately before the scheduled time.

<figure><img src="../../../../../.gitbook/assets/image (38) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

22. Select the criteria you can set for the data loader process to continue:

| Configurations                                                     | Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use Bulk API (Batch API will be used if the option is not enabled) | <p>The Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets.<br><br>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously.<br><br>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput. When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.<br><br><strong>Note:</strong> When performing multiple insert operations into the same destination org while the ongoing jobs are still running, choosing the <strong><code>Serial Mode</code></strong> is recommended.</p> |
| Batch Size                                                         | <p>Whenever the Bulk API checkbox is left unchecked, the Batch API is used.<br><br>Salesforce Batch API is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process large numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In those cases, Bulk API is the best option. Batch API processes data in smaller batches than Bulk API, resulting in a higher API call usage per operation on large volumes of data.<br><br><strong>Note:</strong> <em>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</em></p>                                                                                                                                      |
| Disable workflow rules                                             | All the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Disable Validation Rules                                           | Validation rules verify that the data a user enters in a record meets the specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Insert/Update with null values.                                    | This will either insert or update record field values with null (if the value is null in source org) in destination org.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Use UTF-8 file encoding for file read and write operations         | Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled in your data exclusively containing English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default as per Salesforce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

23. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/image (39) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="494"><figcaption></figcaption></figure>

24. The **`Results of Last Run`** section shows the number of successful or failed records. The values in this field are updated dynamically while the job is still running. You can view the records or download them to your local system. The records are generated in CSV format.

<figure><img src="../../../../../.gitbook/assets/image (40) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

25. The number of impacted records can be seen in the **`Records`** section. The value in this field is updated dynamically while the job is still running.

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (41) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Edit:`** Modifies or updates the process details.&#x20;
2. **`Abort:`** Aborts the process while it is still running.
3. **`Schedule:`** Sets the schedule at which the process must run.
4. **`Delete:`** Deletes the insert process
5. **`Log:`** Provides information about the execution of the inserted task.
6. **`VR/WFR:`** ARM lists all the validations/workflow rules that were set. The UI lists all the validation rules, and users must enable them for the disabled validation rules (if required). For more info, refer to the article: [Validation/ Workflow Rules](../../../../arm/arm-features/dataloader/validation-workflow-rules.md). Sample VR/WFR attached:

<figure><img src="../../../../../.gitbook/assets/image (42) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. **`Clone:`** Creates a copy (clone) of the insert process. Operation type and object name are displayed. Enter the **`Process Name`** in the field. The default **`Salesforce Org`** is automatically selected. To choose a different org, use the dropdown list. Select the **`Choose Different Data CSV File`** check box to upload a different CSV file. Finally, click **`Clone`**.

<figure><img src="../../../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="399"><figcaption></figcaption></figure>
