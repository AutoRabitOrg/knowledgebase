# Comparing Two Backups

To compare two backup activities of a Salesforce org:

1. Log in to Vault and navigate to **COMPARE**.
2. Select the Salesforce org and any required configurations, then click **GET DETAILS**.
3. The list of available backups is displayed.\
   &#xNAN;_&#x4E;ote: Hierarchical and archival backups are not supported for compare operations._

#### Step-By-Step Guide:

1. Click on the “Job Configs” section under the “Compare” module to observer the list of backups available for compare operations.
2.  Select the required backup(s) from the list of backups available to perform a “Backup-to-Backup” compare operation.

    <figure><img src="../../../../.gitbook/assets/image (5) (9).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (1) (13).png" alt=""><figcaption></figcaption></figure>
3. On selecting the backups, observe the details of the Snapshot1 and Sanpahot2.
4. The Snapshot1 represents the older backup among the selected backups for the comparison to be performed.
5. The Snapshot 2 represents the latest among the backups selected.
6. The Snapshot 1 will be compared against the Snapshot2.
7. After selecting the required backup. Click “COMPARE” to initiate the compare operation.
8.  The compare operation will fetch and display the objects that are part of the backups in the next screen.

    <figure><img src="../../../../.gitbook/assets/image (2) (11).png" alt=""><figcaption></figcaption></figure>
9.  Choose the object to perform the compare operation on.

    <figure><img src="../../../../.gitbook/assets/image (3) (9).png" alt=""><figcaption></figcaption></figure>
10. Both the **Account** and **Fields to Compare** sections display the fields available for evaluation. These sections are reviewed to identify and confirm the fields included in the comparison.

    <figure><img src="../../../../.gitbook/assets/image (4) (8).png" alt=""><figcaption></figcaption></figure>
11. Click on the object to observe the fields in the object.

    <figure><img src="../../../../.gitbook/assets/image (5) (9) (1).png" alt=""><figcaption></figcaption></figure>
12. Click on the field “Fields To Compare” to observe the list of fields.

    <figure><img src="../../../../.gitbook/assets/image (6) (9).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (7) (8).png" alt=""><figcaption></figcaption></figure>
13. The “Clickable Object” and the “Fields To Compare” is useful to specify the fields that should be part of the compare operation.
    1. Only the fields selected under these will be part of the compare operation.
14. Click on the “COMPARE” button to initiate the compare operation.

    <figure><img src="../../../../.gitbook/assets/image (9) (7).png" alt=""><figcaption></figcaption></figure>
15. Clicking compare will show the “Compare -Save Config” screen.

    <figure><img src="../../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>
16. **Observe the following fields on the screen:**
    1. **Label(required field):** Enter a label for the job
    2. **Preserve the result for:** will specify the retention period for the compare results. _The minimum retention period is for “7 Days” and the maximum retention period for the compare results will be for “30 Days” only._
    3. **Description:** allows to enter a fitting description to the job.
17. Click “SAVE” on entering all the required details.
18. Clicking “SAVE” will show a pop-up saying, “Comparison is initiated successfully. Notification will be sent to your email once the comparison is completed.”
    1. &#x20;Once the compare job is completed, an email will be triggered to the user.
19. Click “OK” to be redirected to the “JOB HISTORY” page of the flow.

    <figure><img src="../../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>
20. Observe the list of jobs on the page.

    <figure><img src="../../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
21. The recently triggered job will be initially in progress, until the job run is completed.

    <figure><img src="../../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>
22. Once the jobs run is completed successfully, a blue tick”![Tick with solid fill](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAPCAYAAAAyPTUwAAAAAXNSR0IArs4c6QAAAHhlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAKgAgAEAAAAAQAAAAugAwAEAAAAAQAAAA8AAAAA0dUkjgAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAAPdJREFUKBVjYBgFJISA284X3A77/7OAtDDh05d87ru8jLDAfAXOT25gxQ3//zOFrrrKhq4p7sI36f8M/ycxMv2XZ2RjegBWfPfEc3U+JaXIpCOveWEa0s580mD+/X/W/3//Of//ZYycb8R7DSTHwsTGz/Xv3590Bk5uneRjH9t/szHp/2ZkbmRg/H+N4S9j6zwzjscwQ1i+GXFd4Dr9ZQIzw/8yRnb2/8z//+gxMPy/8+fP787F5gJwhSANjCAC5O4HJz7YMbNzdf7782sH059/E+da8b8DySEDsGKQAEjD4+sfZH/9FnizWJ/xK7IirGyQBqwSUEEAnmpeCMrHoKEAAAAASUVORK5CYII=)” will be displayed at the status of the triggered job.

    <figure><img src="../../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>
23. Click on the “Compare Label” to navigate to the compare results screen.

    <figure><img src="../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
24. **Compare Results – View All Records**
    1. Displays a consolidated list of comparison results for the selected object using the chosen snapshot pair.
    2. Shows _All_ records by default, including unchanged, modified, and deleted entries.
    3. Provides category filters – **All, No Changes, Modifications,** and **Deletions** – to refine the displayed results.
    4. Includes options such as **Select Field, Review and Restore, Fields to Compare, Compare, Change View,** and **Export** for further actions.
    5. Allows searching within displayed columns and navigating through paginated results using **Previous 100 Rows** and **Next 100 Rows**.
25. **Compare Results – No Changes Filter**
    1.  Displays only those records that have no differences between Snapshot1 and Snapshot2.

        <figure><img src="../../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
    2. Highlights the No Changes filter as selected, narrowing the view to stable or unaffected records.
    3. Provides quick access to view record-level details using the View Records icon.
    4. All action buttons, such as Fields to Compare, Compare, and Export, remain available for further analysis.
26. **Compare Results – Modifications Filter**
    1.  Shows only modified records where field-level differences exist between Snapshot1 and Snapshot2.

        <figure><img src="../../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
    2. Modified values are visually emphasized (highlighted in yellow) to help quickly identify field differences.
    3. Allows reviewing and restoring modified records through the Review and Restore option.
    4. Supports column-based analysis for changed fields and navigation through the filtered result set.
27. **Compare Results – Deletions Filter**
    1.  Displays only the deleted records identified between the compared snapshots.

        <figure><img src="../../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
    2. Highlights the Deletions filter as selected to isolate removed records.
    3. Deleted values are visually marked red for easy recognition.
    4. Allows opening individual record details using the View Records option.
    5. Retains access to export and comparison tools for audit or restoration purposes.
28. **Filtering Records by Column in Compare History**

    The Columns filter enables narrowing the displayed results to records that match a specific field value. This feature is useful when reviewing large comparison datasets or when focusing on particular attributes.

    <figure><img src="../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
29. **Selecting a Column for Filtering**

    A dropdown list provides all available fields for the selected object. A field is chosen from the list to define the basis of the filter.

    <figure><img src="../../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
30. **Viewing Filtered Results**

    1. After selecting the desired field, a value is entered in the Search box to locate matching records. Selecting GO initiates the filter and updates the results accordingly.
    2. Once the filter is applied, the results table displays only those records that match the specified value in the chosen field. Pagination controls at the bottom allow navigation through the filtered dataset as needed.

    <figure><img src="../../../../.gitbook/assets/image (23) (6).png" alt=""><figcaption></figcaption></figure>
31. **View Records**
    1. Displays a list of comparison results with a View Records icon for each row, allowing detailed inspection of the selected record.
    2.  Each icon opens a modal window showing a side-by-side comparison of Backup(s) Data for the corresponding object record.



        <figure><img src="../../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>



        <figure><img src="../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>
    3. Shows three columns:
       1. **Field** – the field name being compared
       2. **Snapshot1** – the oldest backup among the selected
       3. **Snapshot2** – the latest backup among the selected
    4.  Provides a clear view of individual field values, helping identify differences across snapshots.

        <figure><img src="../../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
    5. Highlights differences wherever applicable to assist in identifying modifications quickly.
    6. Allows users to validate record-specific changes without navigating away from the comparison results page.
32. **Fields to Compare**
    1. Displays the Fields to Compare option, allowing refinement of the comparison by selecting only specific fields from the chosen Salesforce object.
    2.  Opens a field-selection window listing all available fields for the selected object, including the field label and API name.

        <figure><img src="../../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>
    3. Provides a Filter search bar to quickly locate specific fields.
    4.  Allows enabling or disabling fields using checkboxes to customize the comparison criteria.

        <figure><img src="../../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>
    5. Ensures essential fields remain selected and non-editable when required \`(e.g., ID field).
    6. Includes Apply and Cancel actions to confirm or discard field-selection changes.
    7. Once applied, updates the comparison results grid to display and compare only the selected fields.
33. **Change View**
    1.  Provides an option to customize the visible columns in the comparison results.

        <figure><img src="../../../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>
    2.  Opens a dialog displaying the list of all available fields for the selected object.

        <figure><img src="../../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>
    3. Displays the count of currently selected fields and indicates the maximum allowed column limit.
    4. Click OK to apply the updated view or Cancel to discard changes.
34. **Export Records**
    1.  Click Export on the Compare History page to download the comparison results.

        <figure><img src="../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>
    2. An Export dialog appears with three export options:
       1. All Records – Exports every record involved in the comparison, regardless of what is currently visible.
       2. Records Displayed on the Current Page – Exports only the records shown on the active results page.
       3. Selected Records – Exports only the records manually selected using the row checkboxes.
    3.  Choose the preferred export option and click OK to generate the export file.

        <figure><img src="../../../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>
    4. Click Cancel to close the dialog without exporting.
35. **Re-Run Compare Job:** The Re-Run action allows an existing compare job to be executed again using updated field selections or the same configuration.
    1. **Access the Re-Run Option**
       1.  Navigate to Compare → Job History to view the list of completed compare jobs.

           <figure><img src="../../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>
       2. In the Actions column, click the Re-Run icon for the desired job.
    2. **Confirm Re-Run**&#x20;
       1.  A confirmation dialog appears. Select OK to continue or Cancel to abort.

           <figure><img src="../../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>
    3. **Select Fields to Compare**
       1.  The Select Fields window opens, displaying all available fields for the selected object

           <figure><img src="../../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>
       2. Modify the field selections as needed.
       3. Click COMPARE to initiate the new comparison.
    4. **Job Queued**
       1.  The job status updates to In Queue, indicating that the comparison is scheduled for execution.

           <figure><img src="../../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>
    5. **Job Initiation**
       1.  Once processed, the new run appears in the job history with a fresh timestamp and updated status

           <figure><img src="../../../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>
36.
37.
38.
39.
40.
41.
42.
43.
44.
45.
46.
47.
48.











<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Next,

* Select **one backup** from the list to compare the backup data with live data from Salesforce org or,

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Select **two backup activities** to compare them and show the metadata and data difference results.

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **COMPARE** or **LIVE COMPARISON** based on the backup selection.
7. On the next screen, view the **metadata/data comparisons** between two backups. Use the **Search** filter option to find any specific record.

<figure><img src="../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Click on the individual **object** to view the detailed line-level comparison report between two backups.

<figure><img src="../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. You can filter the comparison report based on the record types i.e., whether the records were modified, deleted or no changes happened to date.

<figure><img src="../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. You can even **search** for specific columns and text to filter and view the comparison record faster.

<figure><img src="../../../../.gitbook/assets/image (22) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

11.
12. Select the **Report** you want to compare, then click on **TRIGGER RESTORE.**

<figure><img src="../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

12. Follow the instructions on the Compare checklist.

<figure><img src="../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

13. Click **Got It** after you've gone through the checklist to close the pop-up screen.
