---
hidden: true
---

# Copy of Extracting Salesforce Data

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
7.  The workflow opens at the initial step, where the Salesforce connection and object selection context are available. Selecting Next moves the process to the Add Filters step, where the query is configured.

    <figure><img src="../../../../../.gitbook/assets/image (2583).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Login and select object step</em></p>
8.  The selected object defines the available field list, filters, order-by options, and base query structure in the Add Filters step.

    <figure><img src="../../../../../.gitbook/assets/image (2584).png" alt=""><figcaption></figcaption></figure>

    _Add Filters step with the generated query_
9.  **Building the Query from Fields**

    The Fields panel lists the fields available for the selected object. Selecting fields adds them to the generated query. The query editor updates automatically as selections are made.

    <figure><img src="../../../../../.gitbook/assets/image (2585).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Fields panel in the Add Filters step</em></p>

    The Search option narrows the field list and helps locate the required field. The Select all option selects the displayed fields in the list.

    <figure><img src="../../../../../.gitbook/assets/image (2586).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Field search and field selection</em></p>

    The Show API Names option displays each field with its API name. This helps confirm the exact field reference used in the generated query.

    <figure><img src="../../../../../.gitbook/assets/image (2588).png" alt=""><figcaption></figcaption></figure>

    _API names displayed for selected fields_
10. **Adding and Managing Filter Conditions**

    The Filters section limits records returned by the query. A condition is configured by selecting the reference object, field, operator, and value. The Add Condition icon adds the condition to the filter grid.

    <figure><img src="../../../../../.gitbook/assets/image (2589).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Filter condition configuration</em></p>

    After a condition is added, the filter grid displays the condition details. The generated query updates to include the filter logic.

    <figure><img src="../../../../../.gitbook/assets/image (2590).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Filter condition added to the grid</em></p>

    Multiple filters can be added to the grid. Brackets and logical operators support grouped filter conditions when needed.

    <figure><img src="../../../../../.gitbook/assets/image (2591).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Multiple filter conditions added</em></p>

    A filter condition can be removed from the grid. Removing a condition updates the query and reflects the remaining filter logic only.
11. **Applying Order By and Record Count**

    The Order By section controls the sorting of extracted records. Selecting the object, field, and direction adds the order-by clause to the generated query.

    <figure><img src="../../../../../.gitbook/assets/image (2592).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Order By configuration</em></p>

    The Record Count field limits the number of records returned by the query. After a count is entered, the query updates with the corresponding limit.

    <figure><img src="../../../../../.gitbook/assets/image (2593).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Record Count applied to the query</em></p>
12. **Including Deleted Records**

    The Include deleted records option controls whether deleted records are considered during extraction. When enabled, the setting remains part of the query validation context.

    <figure><img src="../../../../../.gitbook/assets/image (2594).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Include deleted records option enabled</em></p>
13. **Validating the Query**

    Selecting Validate checks whether the generated query is valid. During validation, the screen displays a processing state while the query is evaluated.

    <figure><img src="../../../../../.gitbook/assets/image (2595).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (2596).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Query validation in progress</em></p>

    After successful validation, a confirmation notification appears and indicates that records are available for extraction. The validated query is ready for the next step in the extract process.

    <figure><img src="../../../../../.gitbook/assets/image (2597).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Query validation successful</em></p>
14. **Editing the Query Manually**

    Selecting Edit query starts manual query editing. Before switching to manual editing, the system displays a confirmation message explaining that query builder options will be disabled and the current query will remain available in the editor.

    <figure><img src="../../../../../.gitbook/assets/image (2599).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Edit query action</em></p>

    Selecting Ok confirms manual editing. The current query remains in the editor and can be updated directly. Query builder options are disabled to prevent conflicts between dynamic query generation and manual query changes.

    <figure><img src="../../../../../.gitbook/assets/image (2600).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Edit query confirmation message</em></p>

    In manual query mode, the query editor remains active for direct updates. The available actions are Switch to query builder and Validate.

    <figure><img src="../../../../../.gitbook/assets/image (2601).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Manual query editing mode</em></p>

    After the manual query is updated, selecting Validate validates the edited query. The query builder options remain disabled during manual query validation.

    <figure><img src="../../../../../.gitbook/assets/image (2602).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Manual query validation</em></p>
15. **Switching Back to Query Builder**

    Selecting Switch to query builder returns the workflow to field-based query creation. Before switching, the system displays a confirmation message explaining that the existing query will be cleared and query builder options will be enabled.

    <figure><img src="../../../../../.gitbook/assets/image (2598).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Switch to query builder confirmation</em></p>

    After the switch is confirmed, the existing query is cleared. Fields, filters, and order-by options are enabled again, and the Add Filters section returns to a blank query-building state.

    <figure><img src="../../../../../.gitbook/assets/image (2604).png" alt=""><figcaption></figcaption></figure>

    <p align="center"><em>Query builder options enabled after switching</em></p>
16. Multiple schedule options are available to schedule the job

    <figure><img src="../../../../../.gitbook/assets/14 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/15 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/16 - Extract.png" alt=""><figcaption></figcaption></figure>
17. On completing the scheduling, click "Next" to move to the "Process Details".

    <figure><img src="../../../../../.gitbook/assets/17 - Extract.png" alt=""><figcaption></figcaption></figure>
18. Select a "Job Group" to assign the job to a group.

    <figure><img src="../../../../../.gitbook/assets/18 - Extract.png" alt=""><figcaption></figcaption></figure>
19. Click on "Save" to save the extract job created.

    <figure><img src="../../../../../.gitbook/assets/19 - Extract.png" alt=""><figcaption></figcaption></figure>
20. Clicking "Save" will redirect to the job list screen of the dataloader basic.

    <figure><img src="../../../../../.gitbook/assets/20 - Extract.png" alt=""><figcaption></figcaption></figure>
21. Click on "Save" to run the job.
22. Clicking save will redirect to the "Run Configuration" screen.

    <figure><img src="../../../../../.gitbook/assets/21 - Extract.png" alt=""><figcaption></figcaption></figure>
23. Clicking "Run" on the configuration sceen will redirect to the job list screen with the job "in-progress" and the "Abort" options on the job.

    <figure><img src="../../../../../.gitbook/assets/22 - Extract.png" alt=""><figcaption></figcaption></figure>
24. Click on the Eclipse icon to observe the options
25. Click on the "Edit" option to initiate the edit flow of the job

    <figure><img src="../../../../../.gitbook/assets/23 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/24 - Extract.png" alt=""><figcaption></figcaption></figure>
26. Click the **Schedule** option to view any existing schedule configured during job creation. A new schedule can also be set at this stage, which will apply specifically to the current job.

    <figure><img src="../../../../../.gitbook/assets/25 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/26 - Extract.png" alt=""><figcaption></figcaption></figure>
27. To delete the job, click on the "Delete" option.

    <figure><img src="../../../../../.gitbook/assets/27 - Extract.png" alt=""><figcaption></figcaption></figure>
28. A confirmation prompt is displayed to ensure the deletion action is intentional and acknowledged, helping prevent accidental removal of the process.

    <figure><img src="../../../../../.gitbook/assets/28 - Extract.png" alt=""><figcaption></figcaption></figure>
29. Click on the "Clone" option to initiate the clone operation of the job.

    <figure><img src="../../../../../.gitbook/assets/29 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/30 - Extract.png" alt=""><figcaption></figcaption></figure>
30. Once the clone operation is completed, a cloned job can be observed on the job list page.

    <figure><img src="../../../../../.gitbook/assets/31 - Extract.png" alt=""><figcaption></figcaption></figure>
31. Click on the "Log" option to observe the job details of the job.

    <figure><img src="../../../../../.gitbook/assets/32 - Extract.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/33 - Extract.png" alt=""><figcaption></figcaption></figure>
32. The success and the failure of the records can be observed under the "Result of Last Run".

    <figure><img src="../../../../../.gitbook/assets/34 - Extract.png" alt=""><figcaption></figcaption></figure>
33. Click on the "Success" icon to observe the success records

    <figure><img src="../../../../../.gitbook/assets/35 - Extract.png" alt=""><figcaption></figcaption></figure>
