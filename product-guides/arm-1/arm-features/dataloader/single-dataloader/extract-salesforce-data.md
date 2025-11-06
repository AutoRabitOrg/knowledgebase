# Extract Salesforce Data

#### **Data Extraction Overview**

Basic DataLoader offers a convenient feature to extract data from Salesforce by defining filter criteria using queries during job creation. The query specified at this stage determines which records are retrieved when the job is executed. This ensures that only the relevant dataset is fetched based on the configured query conditions, enabling targeted and efficient data extraction.

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

