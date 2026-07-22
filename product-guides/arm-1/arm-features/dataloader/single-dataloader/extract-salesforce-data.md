# Extracting Salesforce Data

#### **Data Extraction Overview**

Basic DataLoader offers a convenient feature to extract data from Salesforce by defining filter criteria using queries during job creation. The query specified at this stage determines which records are retrieved when the job is executed. This ensures that only the relevant dataset is fetched based on the configured query conditions, enabling targeted and efficient data extraction.

**Step-By-Step Guide:**

1. Open the Basic application by logging in to the application.
2. Expand the "Dataloader" option to click on the "Basic" option.
3.  This will open the basic dataloader application.

    <figure><img src="../../../../../.gitbook/assets/1 - Extract.png" alt=""><figcaption></figcaption></figure>
4. Click on the "Create new job" button to initiate the creation of an "Extract" job.
5. On clicking on the "Extract" job, the flow will navigate to the "Login and select object" step.
6.  ### Select the source object

    The Create Dataloader Job flow starts in the Login and select object step. After selecting the required source org and destination org, Login and fetch objects retrieves the available objects.

    The required object is selected from the object list. This selected object is used as the master object in the Schema step.

    <figure><img src="../../../../../.gitbook/assets/image (2605).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Login and select object step with the object list available for selection.</p>
7.  ### Open the filter configuration

    The Schema step displays the selected master object and provides access to Filters and Mappings. Selecting Filters opens the Filter panel for the object.

    Upload CSV File is selected under Input Options. This option allows filter values to be loaded from a CSV file instead of entering each value manually.

    <figure><img src="../../../../../.gitbook/assets/image (2606).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Schema step with Filters available for the selected master object.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2607).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Filter panel with Upload CSV File selected.</p>
8.  ### Upload the CSV file

    The field and operator are selected before uploading the CSV file. The file upload control opens the local file picker, where the CSV file containing filter values is selected.

    After the file is uploaded, Vault displays a success notification. The uploaded file name appears in the upload field, confirming that the file is attached to the filter configuration.

    If the uploaded file format or content is not valid for the selected filter setup, Vault displays a validation message so the file can be corrected before continuing.

    <figure><img src="../../../../../.gitbook/assets/image (2608).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Field, operator, and upload action available for the CSV filter.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2609).png" alt=""><figcaption></figcaption></figure>

    <p align="center">CSV file selected from the local file picker.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2610).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Success notification after the CSV file is uploaded.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2611).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Validation message displayed for upload-related issues.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2612).png" alt=""><figcaption></figcaption></figure>

    &#x20;                                   Action menu showing available options after file upload.
9.  ### Auto-populate and review the query

    Auto populate reads the uploaded CSV values and generates the corresponding query in the query editor. The generated query uses the selected object and field, then inserts the uploaded values into the filter condition.

    Order By can be configured to define the sort order for the query output. Record Count can be used when the job must limit the number of records returned by the query.

    <figure><img src="../../../../../.gitbook/assets/image (2613).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Generated query populated from the uploaded CSV file.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2614).png" alt=""><figcaption></figcaption></figure>

    &#x20;                                   Record Count area available for limiting returned records.
10. ### Validate and apply the filter

    Validate checks whether the generated query is valid before the filter is applied. If the query is valid, Vault displays a success notification.

    Apply saves the filter configuration for the selected master object. During processing, Vault applies the CSV-based filter and then returns to the Schema step with the filter configured for the object.

    <figure><img src="../../../../../.gitbook/assets/image (2615).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Validate action available after the query is generated.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2616).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Processing state while validation or apply action is in progress.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2617).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Success notification after the query is validated.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2618).png" alt=""><figcaption></figcaption></figure>

    <p align="center">Apply action available after validation.</p>

    <figure><img src="../../../../../.gitbook/assets/image (2619).png" alt=""><figcaption></figcaption></figure>

    &#x20;                            Schema step showing the configured filter after the panel closes.
11. Multiple schedule options are available to schedule the job

    <figure><img src="../../../../../.gitbook/assets/14 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/15 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/16 - Extract.png" alt=""><figcaption></figcaption></figure>
12. On completing the scheduling, click "Next" to move to the "Process Details".

    <figure><img src="../../../../../.gitbook/assets/17 - Extract.png" alt=""><figcaption></figcaption></figure>
13. Select a "Job Group" to assign the job to a group.

    <figure><img src="../../../../../.gitbook/assets/18 - Extract.png" alt=""><figcaption></figcaption></figure>
14. Click on "Save" to save the extract job created.

    <figure><img src="../../../../../.gitbook/assets/19 - Extract.png" alt=""><figcaption></figcaption></figure>
15. Clicking "Save" will redirect to the job list screen of the dataloader basic.

    <figure><img src="../../../../../.gitbook/assets/20 - Extract.png" alt=""><figcaption></figcaption></figure>
16. Click on "Save" to run the job.
17. Clicking save will redirect to the "Run Configuration" screen.

    <figure><img src="../../../../../.gitbook/assets/21 - Extract.png" alt=""><figcaption></figcaption></figure>
18. Clicking "Run" on the configuration sceen will redirect to the job list screen with the job "in-progress" and the "Abort" options on the job.

    <figure><img src="../../../../../.gitbook/assets/22 - Extract.png" alt=""><figcaption></figcaption></figure>
19. Click on the Eclipse icon to observe the options
20. Click on the "Edit" option to initiate the edit flow of the job

    <figure><img src="../../../../../.gitbook/assets/23 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/24 - Extract.png" alt=""><figcaption></figcaption></figure>
21. Click the **Schedule** option to view any existing schedule configured during job creation. A new schedule can also be set at this stage, which will apply specifically to the current job.

    <figure><img src="../../../../../.gitbook/assets/25 - Extract (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/26 - Extract.png" alt=""><figcaption></figcaption></figure>
22. To delete the job, click on the "Delete" option.

    <figure><img src="../../../../../.gitbook/assets/27 - Extract.png" alt=""><figcaption></figcaption></figure>
23. A confirmation prompt is displayed to ensure the deletion action is intentional and acknowledged, helping prevent accidental removal of the process.

    <figure><img src="../../../../../.gitbook/assets/28 - Extract.png" alt=""><figcaption></figcaption></figure>
24. Click on the "Clone" option to initiate the clone operation of the job.

    <figure><img src="../../../../../.gitbook/assets/29 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/30 - Extract.png" alt=""><figcaption></figcaption></figure>
25. Once the clone operation is completed, a cloned job can be observed on the job list page.

    <figure><img src="../../../../../.gitbook/assets/31 - Extract.png" alt=""><figcaption></figcaption></figure>
26. Click on the "Log" option to observe the job details of the job.

    <figure><img src="../../../../../.gitbook/assets/32 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/33 - Extract.png" alt=""><figcaption></figcaption></figure>
27. The success and the failure of the records can be observed under the "Result of Last Run".

    <figure><img src="../../../../../.gitbook/assets/34 - Extract.png" alt=""><figcaption></figcaption></figure>
28. Click on the "Success" icon to observe the success records

    <figure><img src="../../../../../.gitbook/assets/35 - Extract.png" alt=""><figcaption></figcaption></figure>

