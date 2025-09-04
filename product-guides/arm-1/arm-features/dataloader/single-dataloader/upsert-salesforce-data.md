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
18. **Run Job**
    * From the Dataloader **Basic** page, select the **Run** (play) icon under **Actions** for the required job.
    *   The **Run Configuration** window opens to adjust run options before execution.

        <figure><img src="../../../../../.gitbook/assets/20 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Click **Run** to start the job or **Cancel** to exit without running.
19. **Run Configuration**

    *   The **Run Configuration** window allows toggling options such as:

        * **Disable workflow rules**
        * **Disable validation rules**
        * **Insert/update with null values**
        * **Use UTF-8 encoding for file operations**

        <figure><img src="../../../../../.gitbook/assets/21 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Optionally, choose a different data CSV file if required.
    * Confirm with **Run** to execute the job.
    * Dataloader Configuration Options

    | Configuration                      | Description                                                                      |
    | ---------------------------------- | -------------------------------------------------------------------------------- |
    | **Batch Size**                     | Applies if Bulk API is disabled. Based on SOAP and better for smaller datasets.  |
    | **Disable workflow rules**         | Deactivates workflows during operation and reactivates post-process.             |
    | **Disable Validation Rules**       | Deactivates validation rules during the process and re-enables afterward.        |
    | **Insert/Update with null values** | Allows null value updates in destination org.                                    |
    | **Use UTF-8 file encoding**        | Required for data containing English alphabets. Disable for non-English content. |
20. **Upload New Data File**
    * Select **Choose Different Data CSV File** to upload an alternate dataset.
    *   The file upload section allows drag-and-drop or file selection.

        <figure><img src="../../../../../.gitbook/assets/22 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Upon successful upload, a confirmation message displays the number of records impacted.
21. **Job In Progress**
    *   After execution begins, the job status updates to **In Progress** on the Dataloader Basic page.



        <figure><img src="../../../../../.gitbook/assets/23 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This indicates that processing has started but is not yet complete.
22. **Abort Job**
    *   While a job is **In Progress**, select the **Abort** button under **Actions**.

        <figure><img src="../../../../../.gitbook/assets/24 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This immediately halts the job execution.
    * Aborting should only be used if the run was triggered incorrectly or requires stopping due to issues.
23. **Edit Configuration**
    *   From the Dataloader Basic page, select the ellipsis (three dots) next to the desired job.

        <figure><img src="../../../../../.gitbook/assets/33 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Choose **Edit** to modify the existing configuration.
    * Update object selections, field mappings, or process details as required.
24. **Edit Process – Select Object**
    *   In the Edit upsert process page, log in to the Salesforce Org and fetch available objects.

        <figure><img src="../../../../../.gitbook/assets/34 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Select the object to be used for the process.
    * Proceed to update field mappings or schedule settings.
25. **Schedule Configuration (Screen 35)**
    *   From the Dataloader Basic page, select the ellipsis (three dots) next to a job.

        <figure><img src="../../../../../.gitbook/assets/35 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Choose **Schedule** to define when the process should run automatically.
26. **Schedule Process (Screen 36)**
    *   In the scheduling window, select the preferred type: **No Schedule, Daily, or Weekly**.

        <figure><img src="../../../../../.gitbook/assets/36 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Confirm the schedule by clicking **Schedule**.
27. **Delete Configuration (Screen 37)**
    * From the Dataloader Basic page, select the ellipsis (three dots) for a specific job.
    *   Choose **Delete** to remove the selected configuration permanently.

        <figure><img src="../../../../../.gitbook/assets/37 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This action cannot be undone and should only be used when the process is no longer required.
28. **Delete Process Confirmation (Screen 38)**
    *   A confirmation dialog appears before deleting the process.

        <figure><img src="../../../../../.gitbook/assets/38 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Click **Delete** to proceed or **Cancel** to stop the action.
29. **Clone Configuration (Screen 39)**
    * From the Dataloader Basic page, select the ellipsis (three dots) next to the desired job.
    *   Choose **Clone** to duplicate the selected configuration.

        <figure><img src="../../../../../.gitbook/assets/39 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Review the process details and optionally choose a different data CSV file.
    * Click **Clone** to create the duplicate job.
30. **Clone Process (Screen 40)**
    *   The Clone window displays process details including operation type, object name, and source sandbox.

        <figure><img src="../../../../../.gitbook/assets/40 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Enter or update the process name if needed.
    * Select an alternate data CSV file if applicable.
    * Confirm the duplication by clicking **Clone**.
31. **Validation / Workflow Rules Access**
    *   From the **Dataloader Basic** page, select the **Validation Rules / Workflow Rules** icon under the _VR/WFR_ column for a specific job.

        <figure><img src="../../../../../.gitbook/assets/26 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This opens a detailed view of validation and workflow rules configured for the selected Salesforce object.
    * Use this option to verify if any rules may impact the execution of the job.
32. **Validation Rules**
    *   The **Validation Rules** tab lists all validation rules for the selected object.

        <figure><img src="../../../../../.gitbook/assets/27 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Each rule displays its _name, previous state, current state, enable status,_ and any associated _errors_.
    * This view ensures data consistency by confirming whether validation rules are active or disabled during job execution.
33. **Workflow Rules**
    *   The **Workflow Rules** tab provides details of all workflow rules for the selected object.

        <figure><img src="../../../../../.gitbook/assets/28 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Each workflow rule displays its _name, previous state, current state,_ and _enable status_.
    * Reviewing these rules allows proper alignment with business automation before running or scheduling jobs.
34. **View Job Results**
    *   From the **Dataloader Basic** page, select the **magnifying glass icon** under _Results of Last Run_ for the required job.

        <figure><img src="../../../../../.gitbook/assets/29 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This opens the results view for the most recent execution.
    * Use this option to quickly validate both success and failure counts before downloading detailed logs.
35. **CSV Result View**
    *   The **CSV Result** window displays record-level details from the last job execution.



        <figure><img src="../../../../../.gitbook/assets/30 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Each row shows Salesforce fields such as _ID, AccountId, FirstName, LastName,_ and other mapped fields.
    * This view helps confirm which records were processed successfully and identify any errors or mismatches.
36. **View Failed Records**
    *   From the **Dataloader Basic** page, select the **magnifying glass icon** under the _Failure_ column for the required job.

        <figure><img src="../../../../../.gitbook/assets/31 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * This opens the result view specifically for failed records in the last run.
    * Use it to investigate why certain records failed while others succeeded.
37. **CSV Failed Records**
    *   The **CSV Result** window displays detailed information for failed records.

        <figure><img src="../../../../../.gitbook/assets/32 - Upsert.png" alt=""><figcaption></figcaption></figure>
    * Fields such as _Id, AccountId, LastName, FirstName,_ and others are shown with their corresponding values.
    * This view helps identify the root cause of failures by examining data values and constraints against validation or workflow rules.





































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

###

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
