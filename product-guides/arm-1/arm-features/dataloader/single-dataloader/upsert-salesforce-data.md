# Upsert Salesforce Data

**Upsert** is a combination of Updating and Inserting. If a record in a file matches an existing record, the existing record is updated with the values in your file. The record is created as a new entity if no match is found.

Step-By-Step Guide:

1. **Create Upsert Job**
   * From the **Dataloader – Basic** page, select **Create new job**.
   *   Choose **Upsert** as the operation type.

       <figure><img src="../../../../../.gitbook/assets/1 - Upsert.png" alt=""><figcaption></figcaption></figure>
2. #### Choose Sandbox
   * In the **Create upsert process** window, select a **Salesforce Org**.
   *   Provide details such as **Environment, Login URL, and Username**.

       <figure><img src="../../../../../.gitbook/assets/2 - Upsert.png" alt=""><figcaption></figcaption></figure>
3. #### Fetch Objects
   * After entering the sandbox details, click **Login and Fetch Objects**.
   *   This retrieves the list of objects available for the upsert operation.

       <figure><img src="../../../../../.gitbook/assets/3 - Upsert.png" alt=""><figcaption></figcaption></figure>
4. #### Select Object&#x20;
   * From the fetched list, choose the required object (e.g., **Contact**).
   *   Click **Next** to proceed with field mapping.

       <figure><img src="../../../../../.gitbook/assets/4 - Upsert (1).png" alt=""><figcaption></figcaption></figure>
5. **Upload File for Upsert**
   *   In the **Create upsert process** screen, select **Choose File** or drag and drop to upload a CSV file.

       <figure><img src="../../../../../.gitbook/assets/5 - Upsert.png" alt=""><figcaption></figcaption></figure>
   * The file will be used for field mapping against Salesforce objects.
6. #### Upload in Progress
   *   The uploaded CSV file appears with a **Pending** status.

       <figure><img src="../../../../../.gitbook/assets/6 - Upsert.png" alt=""><figcaption></figcaption></figure>
   * Additional files can be uploaded, or existing ones removed if required.
7. #### Upload Completed
   *   Once processed, the file shows a **Completed** status.

       <figure><img src="../../../../../.gitbook/assets/7 - Upsert.png" alt=""><figcaption></figcaption></figure>
   * A confirmation message indicates the number of impacted records.
8. #### Field Mapping with AutoMap
   *   Uploaded file fields appear under **Source header** with sample data.

       <figure><img src="../../../../../.gitbook/assets/8 - Upsert.png" alt=""><figcaption></figcaption></figure>
   * Enable **AutoMap** to automatically align fields with Salesforce.
   * Manually select fields if AutoMap does not resolve all mappings.
9. #### Field Mapping Filters
   *   Use the filter option to view **All**, **Mapped**, or **Unmapped** fields.

       <figure><img src="../../../../../.gitbook/assets/9 - Upsert.png" alt=""><figcaption></figcaption></figure>
   * This helps quickly validate field mappings before proceeding.
10. **Lookup Mapping Initiation**
    *   In **Fields Mapping**, select **Lookup via** for fields such as `AccountId`.

        <figure><img src="../../../../../.gitbook/assets/10 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This enables referencing related Salesforce records using specific field values.
11. **Configure Lookup Options**
    *   After enabling **Lookup via**, select the Salesforce object and field to be used for matching records (e.g., Account → LastName).

        <figure><img src="../../../../../.gitbook/assets/11 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Additional conditions can be set:
      * **Use first match if multiple results** – prioritizes the first match when more than one record is found.
      * **Insert if not found** – creates a new record if no matching record exists.
    * These options provide flexibility in handling relationships and data consistency during the upsert process.
12. #### Select Lookup Field
    *   A dropdown displays available Salesforce fields for the selected object.

        <figure><img src="../../../../../.gitbook/assets/12 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Pick the desired field (e.g., `LastName`, `FirstName`) to complete the lookup mapping.
13. #### Completed Lookup Mapping
    *   The field is now mapped with **Lookup via** enabled.

        <figure><img src="../../../../../.gitbook/assets/13 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * The selected Salesforce field is shown, along with the applied lookup conditions.
14. **Schedule Configuration – No Schedule**
    *   In the **Schedule** step, select **No Schedule** to run the upsert job manually.



        <figure><img src="../../../../../.gitbook/assets/15 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * The job will only execute when triggered directly.
15. #### Schedule Configuration – Daily
    *   Select **Daily** to schedule the job for execution every day.

        <figure><img src="../../../../../.gitbook/assets/16 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Configure the **start date** and choose to run at a **specific time** or at a **fixed interval**.
    * Set the **end condition**: Never, a fixed number of occurrences, or a specific end date.
16. #### Schedule Configuration – Weekly
    *   Select **Weekly** to schedule the job on specific days of the week.

        <figure><img src="../../../../../.gitbook/assets/17 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Configure the **start date** and define the execution time.
    * Set the **end condition** similar to daily scheduling.
17. **Process Details**
    *   Review the object, type of operation, and number of records to be processed.

        <figure><img src="../../../../../.gitbook/assets/18 - Upsert (1).png" alt=""><figcaption></figcaption></figure>
    * Confirm the Salesforce connection and enter a process name
    * Optionally, assign the process to a **Job Group** for better organization.
18.





































**Upsert** is a combination of Updating and Inserting. If a record in a file matches an existing record, the existing record is updated with the values in your file. The record is created as a new entity if no match is found.

The following articles describe using **Single Dataloader** to upsert data into Salesforce via a CSV file.

1. Log in to your ARM account.
2. Hover your mouse over the **`Dataloader`** module and select **`Dataloader`**.
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

11. Prepare field mappings: match CSV columns to Salesforce fields.
12. Use **`Automap`** to match fields automatically if names align.

<figure><img src="../../../../../.gitbook/assets/image (68) (1) (1) (1).png" alt="Field mapping with Automap"><figcaption></figcaption></figure>

13. Confirm all required fields are mapped, then click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (69) (1) (1).png" alt="Process summary screen" width="563"><figcaption></figcaption></figure>

### Process Summary Options

* **Name:** Assign a name to the job.
* **Category:** Organize processes by categories (create new or use existing).
* **External ID Field:** Specify unique identifier other than Salesforce ID (e.g., ERP ID).
* **Object:** Displays the object being upserted.
* **Operation Type:** Displays **Upsert**.
* **Impacted Records:** Shows record count.
* **Use Bulk API:** Enable for large datasets for improved throughput.

You can also schedule tasks as **Daily**, **Weekly**, or **On-demand**. Click **`Save`** to store and run later.

20. The task appears in the **Dataloader Summary** list.
21. Click **`Run`** to execute the task immediately.

<figure><img src="../../../../../.gitbook/assets/image (70) (1) (1).png" alt="Run Dataloader job" width="563"><figcaption></figcaption></figure>

### Dataloader Configuration Options

| Configuration                      | Description                                                                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Use Bulk API**                   | Optimized for large datasets; supports serial or parallel processing. Recommended to use **Serial Mode** if other jobs are in progress. |
| **Batch Size**                     | Applies if Bulk API is disabled. Based on SOAP and better for smaller datasets.                                                         |
| **Disable workflow rules**         | Deactivates workflows during operation and reactivates post-process.                                                                    |
| **Disable Validation Rules**       | Deactivates validation rules during the process and re-enables afterward.                                                               |
| **Insert/Update with null values** | Allows null value updates in destination org.                                                                                           |
| **Use UTF-8 file encoding**        | Required for data containing English alphabets. Disable for non-English content.                                                        |

22. Click **`Run`** to begin.

<figure><img src="../../../../../.gitbook/assets/image (71) (1) (1).png" alt="Click Run to initiate upsert job" width="494"><figcaption></figcaption></figure>

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
6. **VR/WFR:** View validation/workflow rules. See [Validation/ Workflow Rules](../../../../arm/arm-features/dataloader/validation-workflow-rules.md).
7. **Clone:** Create a copy of the process with an option to choose a different data file.

<figure><img src="../../../../../.gitbook/assets/image (59) (1) (1) (1) (1).png" alt="Clone a dataloader job" width="398"><figcaption></figcaption></figure>
