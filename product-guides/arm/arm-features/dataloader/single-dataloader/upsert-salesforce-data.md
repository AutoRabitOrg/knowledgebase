# Upsert Salesforce Data

**Upsert** is a combination of Updating and Inserting. If a record in a file matches an existing record, the existing record is updated with the values in your file. The record is created as a new entity if no match is found.

**Limitation on Record ID Availability**\
Except for the **Upsert** operation in a single DataLoader job, when errors occur during data operations, Salesforce imposes a limitation where **record ID information is not available** in the error details.

The following articles describe using **Single DataLoader** to upsert data into Salesforce via a CSV file.

1. Log in to your ARM account.
2. Hover your mouse over the **`DataLoader`** module and select **`DataLoader`**.
3. Click **`Upsert`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (63) (1) (1) (1) (1).png" alt="Upsert option in Dataloader UI"><figcaption></figcaption></figure>

4. Choose your **`Salesforce Org`** and your org environment (**`Production or Development Edition`**, **`Sandbox`**, or **`Pre-Release`**).
5. The corresponding **`URL`** and your **`Username`** are automatically generated based on the above selection.
6. Click **`Login and Fetch Objects`**.

<figure><img src="../../../../../.gitbook/assets/image (64) (1) (1) (1) (1).png" alt="Login and fetch Salesforce objects"><figcaption></figcaption></figure>

7. Select the object you wish to upsert data into (e.g., **`Account`**, **`Contact`**, **`Lead`**). Use the **`search`** function and **`filter`** button for convenience.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (65) (1) (1) (1) (1).png" alt="Object selection page" width="563"><figcaption></figcaption></figure>

9. Upload your CSV file by clicking the **`Upload`** button.

<figure><img src="../../../../../.gitbook/assets/image (66) (1) (1) (1).png" alt="CSV upload screen"><figcaption></figcaption></figure>

10. Click **`OK`** on the notification popup showing impacted records.

<figure><img src="../../../../../.gitbook/assets/image (67) (1) (1) (1).png" alt="Notification on number of records affected"><figcaption></figcaption></figure>

11. Prepare field mappings: Match CSV columns to Salesforce fields.
12. Use **`Automap`** to match fields automatically if names align.

<figure><img src="../../../../../.gitbook/assets/image (68) (1) (1) (1).png" alt="Field mapping with Automap"><figcaption></figcaption></figure>

13. Confirm all required fields are mapped, then click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/6 (4) (1).png" alt="Process summary screen"><figcaption></figcaption></figure>

### Process Summary Options

* **Name:** Assign a name to the job.
* **Category:** Organize processes by categories (create new or use existing).
* **External ID Field:** Specify unique identifier other than Salesforce ID (e.g., ERP ID).
* **Object:** Displays the object being upserted.
* **Operation Type:** Displays **Upsert**.
* **Impacted Records:** Shows record count.

You can also schedule tasks as **Daily**, **Weekly**, or **On-demand**. Click **`Save`** to store and run later.

14. The task appears in the **DataLoader Summary** list.
15. Click **`Run`** to execute the task immediately.

<figure><img src="../../../../../.gitbook/assets/image (70) (1) (1).png" alt="Run Dataloader job" width="563"><figcaption></figcaption></figure>

### DataLoader Configuration Options

| Configuration                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Batch Size**                     | <p>Salesforce Batch API is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process large numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In those cases, Bulk API is the best option. Batch API processes data in smaller batches than Bulk API, resulting in a higher API call usage per operation on large volumes of data.<br><br><strong>Note:</strong> <em>When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</em></p> |
| **Disable workflow rules**         | Deactivates workflows during operation and reactivates post-process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Disable Validation Rules**       | Deactivates validation rules during the process and re-enables afterward.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Insert/Update with null values** | Allows null value updates in destination org.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Use UTF-8 file encoding**        | Required for data containing English alphabets. Disable for non-English content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

22. Click **`Run`** to begin.

<figure><img src="../../../../../.gitbook/assets/7 (3).png" alt="Click Run to initiate upsert job" width="375"><figcaption></figcaption></figure>

### Results Monitoring

* **Results of Last Run:** Shows success/failure record count dynamically.
* **Records:** Displays the total records affected.

<figure><img src="../../../../../.gitbook/assets/image (72) (1) (1).png" alt="Results of last run" width="563"><figcaption></figcaption></figure>

### More Options

<figure><img src="../../../../../.gitbook/assets/image (62) (1) (1) (1) (1).png" alt="More options menu" width="563"><figcaption></figcaption></figure>

1. **Edit:** Update job configuration.
2. **Abort:** Stop a running job.
3. **Schedule:** Set periodic execution.
4. **Delete:** Remove the job.
5. **Log:** View execution logs.
6. **VR/WFR:** View validation/workflow rules. See [Validation/ Workflow Rules](../validation-workflow-rules.md).
7. **Clone:** Create a copy of the process with an option to choose a different data file.

<figure><img src="../../../../../.gitbook/assets/image (59) (1) (1) (1) (1).png" alt="Clone a dataloader job" width="398"><figcaption></figcaption></figure>
