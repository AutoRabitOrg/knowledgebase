# Extract Salesforce Data

#### **Data Extraction Overview**

Basic DL offers a convenient feature to extract data from Salesforce by defining filter criteria using queries during job creation. The query specified at this stage determines which records are retrieved when the job is executed. This ensures that only the relevant dataset is fetched based on the configured query conditions, enabling targeted and efficient data extraction.

**Step-By-Step Guide:**

1. Open the Basic application by logging in to the application.
2. Expand the "Dataloader" option to click on the "Basic" option.
3.  This will open the basic dataloader application.

    <figure><img src="../../../../../.gitbook/assets/1 - Extract.png" alt=""><figcaption></figcaption></figure>
4. Click on the "Create new job" button to initiate the creation of an "Extract" job.
5. On clicking on the "Extract" job, the flow will navigate to the "Login and select object" step.
6.  Select an object from the available list of objects.

    <figure><img src="../../../../../.gitbook/assets/2 - Extract.png" alt=""><figcaption></figcaption></figure>
7.  On selecting the objects, click on "LOGIN AND FETCH OBJECTS" button to fetch the object list.

    <figure><img src="../../../../../.gitbook/assets/3 - Extract.png" alt=""><figcaption></figcaption></figure>
8.  Select the required object on which the data extraction has to be performed and click on "Next" to add filters for specifying the filter criteria.

    <figure><img src="../../../../../.gitbook/assets/6 - Extract.png" alt=""><figcaption></figcaption></figure>
9. Under the filters, select the following to set the filter criteria:
   1. **Reference object**: Select the objects related to the object selection made earlier
   2. **Select field**: Select the field associated with the reference object selected.
   3. **Select Operator**: Select an operator from the available list.
   4. **Value**: Enter the required value as per the filter criteria being built.
10. Observe the "Fields" section on the left-hand side of the screen.

    1. Enabling this will make the field's information visible.

    <figure><img src="../../../../../.gitbook/assets/6.1 - Extract.png" alt=""><figcaption></figcaption></figure>
11. Click on the "v" icon to collapse the section and observe the rest of the available objects.

    <figure><img src="../../../../../.gitbook/assets/6.2 - Extract.png" alt=""><figcaption></figcaption></figure>
12. Observe the collapsed list on the left side of the screen.
13. Click on the "+" icon to add the prepared query to the query area

    <figure><img src="../../../../../.gitbook/assets/7 - Extract.png" alt=""><figcaption></figcaption></figure>
14. On clicking the "+" icon, the query will be added to the query section.

    <figure><img src="../../../../../.gitbook/assets/8 - Extract.png" alt=""><figcaption></figcaption></figure>
15. Use the **"+"** icon to add multiple conditions across different objects, enabling the construction of complex queries with precision.

    <figure><img src="../../../../../.gitbook/assets/8.1 - Extract.png" alt=""><figcaption></figcaption></figure>
16. Fields can be added from the leftside "Fields" section at any point of the query building.

    <figure><img src="../../../../../.gitbook/assets/9 - Extract (1).png" alt=""><figcaption></figcaption></figure>
17. IIn the **Order By** section, specify whether the extracted records should be sorted in ascending or descending order based on the selected field, enabling structured and meaningful data output.
    * Select a **`field`** to be your sorting criteria.
    * Select your sorting order: **`Ascending`** or **`Descending`**.
18. Click on the "Enable Text Editor" button to make the query editor window editable.

    <figure><img src="../../../../../.gitbook/assets/10 - Extract.png" alt=""><figcaption></figcaption></figure>
19. Observe the editable query editor. Now, the query can be manually entered.

    <figure><img src="../../../../../.gitbook/assets/11 - Extract.png" alt=""><figcaption></figcaption></figure>
20. Once the query editor is enabled for editing rest of the options to select the fields will be dissabled or grayed out.
21. To go back to building the query using the field selection, click on the "Reset Text Editor" button.
22. Clicking this option reverts all manual changes made to the query. A confirmation prompt appears before restoring the original field selection used for building the query.

    <figure><img src="../../../../../.gitbook/assets/12 - Extract.png" alt=""><figcaption></figcaption></figure>
23. After building the query—whether manually or via field selection—use the **Validate** option to confirm its accuracy before proceeding with the **Extract** job configuration.

    <figure><img src="../../../../../.gitbook/assets/13 - Extract.png" alt=""><figcaption></figcaption></figure>
24. On validating the query, a success message will be displayed with the number of records to be extracted.
25. On successfully  validating the query, click on "Next" to continue to the "Schedule" option
26. Multiple schedule options are available to schedule the job

    <figure><img src="../../../../../.gitbook/assets/14 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/15 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/16 - Extract.png" alt=""><figcaption></figcaption></figure>
27. On completing the scheduling, click "Next" to move to the "Process Details".

    <figure><img src="../../../../../.gitbook/assets/17 - Extract.png" alt=""><figcaption></figcaption></figure>
28. Select a "Job Group" to assign the job to a group.

    <figure><img src="../../../../../.gitbook/assets/18 - Extract.png" alt=""><figcaption></figcaption></figure>
29. Click on "Save" to save the extract job created.

    <figure><img src="../../../../../.gitbook/assets/19 - Extract.png" alt=""><figcaption></figcaption></figure>
30. Clicking "Save" will redirect to the job list screen of the dataloader basic.

    <figure><img src="../../../../../.gitbook/assets/20 - Extract.png" alt=""><figcaption></figcaption></figure>
31. Click on "Save" to run the job.
32. Clicking save will redirect to the "Run Configuration" screen.

    <figure><img src="../../../../../.gitbook/assets/21 - Extract.png" alt=""><figcaption></figcaption></figure>
33. Clicking "Run" on the configuration sceen will redirect to the job list screen with the job "in-progress" and the "Abort" options on the job.

    <figure><img src="../../../../../.gitbook/assets/22 - Extract.png" alt=""><figcaption></figcaption></figure>
34. Click on the Eclipse icon to observe the options
35. Click on the "Edit" option to initiate the edit flow of the job

    <figure><img src="../../../../../.gitbook/assets/23 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/24 - Extract.png" alt=""><figcaption></figcaption></figure>
36. Click the **Schedule** option to view any existing schedule configured during job creation. A new schedule can also be set at this stage, which will apply specifically to the current job.

    <figure><img src="../../../../../.gitbook/assets/25 - Extract (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/26 - Extract.png" alt=""><figcaption></figcaption></figure>
37. To delete the job, click on the "Delete" option.

    <figure><img src="../../../../../.gitbook/assets/27 - Extract.png" alt=""><figcaption></figcaption></figure>
38. A confirmation prompt is displayed to ensure the deletion action is intentional and acknowledged, helping prevent accidental removal of the process.

    <figure><img src="../../../../../.gitbook/assets/28 - Extract.png" alt=""><figcaption></figcaption></figure>
39. Click on the "Clone" option to initiate the clone operation of the job.

    <figure><img src="../../../../../.gitbook/assets/29 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/30 - Extract.png" alt=""><figcaption></figcaption></figure>
40. Once the clone operation is completed, a cloned job can be observed on the job list page.

    <figure><img src="../../../../../.gitbook/assets/31 - Extract.png" alt=""><figcaption></figcaption></figure>
41. Click on the "Log" option to observe the job details of the job.

    <figure><img src="../../../../../.gitbook/assets/32 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/33 - Extract.png" alt=""><figcaption></figcaption></figure>
42. The success and the failure of the records can be observed under the "Result of Last Run".

    <figure><img src="../../../../../.gitbook/assets/34 - Extract.png" alt=""><figcaption></figcaption></figure>
43. Click on the "Success" icon to observe the success records

    <figure><img src="../../../../../.gitbook/assets/35 - Extract.png" alt=""><figcaption></figcaption></figure>













The following articles describe using **Single Dataloader** to extract data from Salesforce. The information is stored in CSV format.

1. Log in to your ARM account.
2. Hover your mouse over the [**`Dataloader`**](https://www.autorabit.com/blog/10-benefits-of-salesforce-data-loader/) module and select **`Dataloader`**.The **Dataloader** screen is best viewed when the zoom setting is **75%** on your Chrome/Firefox browser.
3. Click **`Extract`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Choose your [**`Salesforce org`**](../../../../arm/arm-administration/registration/salesforce-org/) and your org **`Environment`** (_Production_ or _Development_ edition, _Sandbox_, or _Pre-Release_).
5. The corresponding **`URL`** and your **`Username`** are automatically generated based on the above selection.
6. Click **`Login and Fetch objects`** to fetch all the objects from your Salesforce org.
7. Select the object from which you wish to extract the data. For example, **Account**, **Contact**, **Lead**, etc. You can use the **`Search`** function to search through your objects and  **`filter`** to filter your standard/custom objects quickly.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. On the left, you will be provided with an option to select related objects and their fields. Each object will be displayed as a collapsible unit, under which you can select either all of the fields or required fields. Use the **`Quick Find`** search function to search through your fields quickly.

<figure><img src="../../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="319"><figcaption></figcaption></figure>

10. Select the checkbox before each field to include for the extraction process.

<figure><img src="../../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="320"><figcaption></figcaption></figure>

11. On the right, you can add **`Filters`** to your query. Specifying the filter criteria will extract records within a specified limit. To add filters to your query:

    * For your object _(example- Account)_ selected, choose a **`field`** _(example- CreatedDate)._
    * Select the **`operator`**.
    * Enter the **`filter value`** _(example- Date Literals, Last\_week)_.
    * Click on the **+** icon to add the filter.&#x20;
    * To delete a filter, click on the **x** icon.

    <figure><img src="../../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
12. In the **`Order By`** section, you can assign the order in which the record is generated, i.e., ascending or descending order.

    * Select a **`field`** to be your sorting criteria.
    * Select your sorting order: **`Ascending`** or **`Descending`**.

    <figure><img src="../../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
13. You can verify your query using the **`Validate Query`** button to ensure it will work properly before running your task. The number of records being extracted is shown as a notification pop-up.

<figure><img src="../../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (22) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

14. On the **`Process Summary`** screen, you can:
    * Give the process/job a **`Name`**.
    * Select the **`Category`**. Categories are used to classify and group similar processes having similar functionality. In simple terms, you are assigning similar processes to a category. You can select an existing category or create a new one by clicking the **`+`** icon.
    * View the main **`Object`**.
    * View the operation **`Type`** (**`Extract`**).
    * View the number of extracted **`Records`**.
    * **`Limit`** the export row count. Use this option to retrieve some rows from your export results.&#x20;
    * **`Use Bulk API`**.About Bulk APIThe **Bulk API** is based on REST principles and is optimized for inserting, updating, and deleting large data sets. You can use the **Bulk API** to process jobs in **serial** or **parallel** mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously. When you run a bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, providing better overall data throughput.
15. You can schedule your tasks so they start running regularly. You can choose between **`Daily`**, **`Weekly`**, or **`On-demand`** schedules.
16. Finally, click **`Save`** to save your task and run it later.

<figure><img src="../../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

17. Your task is shown on top of the lists on the **`Dataloader Summary`** screen.
18. Click **`Run`** to start the dataloader immediately before the scheduled time.

<figure><img src="../../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

19. Select the configurations here:
    * **Use Batch Size** whenever the Bulk API checkbox is left unchecked, the Batch API is used.
    * **Salesforce Batch API** is based on SOAP principles and is optimized for real-time client applications that update small numbers of records at a time. Although SOAP API can also process larger numbers of records, it becomes less practical when the data sets contain hundreds of thousands of records. In such cases, **Bulk API** is the best option. **Batch API** processes data in smaller batches than bulk API, resulting in a higher API call usage per operation on large volumes of data.
    * **Limit** the export row count.
    * **Use UTF-8 file encoding for file read and write operations**.
20. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/image (25) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="413"><figcaption></figcaption></figure>

21. The **`Results of Last Run`** section shows the number of successful or failed records extracted. You can view the records or download them to your local system. The records are generated in ZIP format.

<figure><img src="../../../../../.gitbook/assets/image (26) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (27) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

1. **`Edit:`** Modifies or updates the process details.&#x20;
2. **`Abort:`** Aborts the process while it is still running.
3. **`Schedule:`** Sets the schedule at which the process must run.
4. **`Delete:`** Deletes the extract process.
5. **`Log:`** Provides information about the execution of the extracted task.
6. **`VR/WFR:`** ARM lists all the validations/workflow rules that were set. The UI lists all the validation rules, and users must enable them for the disabled validation rules (if required). For more info, refer to the article: [Validation/ Workflow Rules](../../../../arm/arm-features/dataloader/validation-workflow-rules.md). Sample VR/WFR attached:

<figure><img src="../../../../../.gitbook/assets/image (28) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (29) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. **`Clone:`** Creates a copy (clone) of the extract process. Operation type and object name are displayed. Enter the **`Process Name`** in the field. The default **`Salesforce Org`** is automatically selected. To choose a different org, use the dropdown list. Use the **`Edit`** button to change the query filter, then click **`Validate`**. Finally, click **`Clone`**.

<figure><img src="../../../../../.gitbook/assets/image (30) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="399"><figcaption></figcaption></figure>
