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
9.  Click on the <img src="../../../../../.gitbook/assets/image (24) (1).png" alt="" data-size="line"> icon to observe the options

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



