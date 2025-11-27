# Live Compare

To compare a backup with live Salesforce data:

1. Log in to Vault and navigate to **COMPARE**.
2. Select the Salesforce org and any required configurations, then click **GET DETAILS**.
3. The available backups are displayed.\
   &#xNAN;_&#x4E;ote: Hierarchical and archival backups are not supported for compare operations._

### **Step-By-Step Guide: Live Compare**

1. Click on the “Job Configs” section under the “Compare” module to observer the list of backups available for compare operations.
2.  Select a backup to perform a “Live Compare” operation.



    ![](<../../../../.gitbook/assets/Unknown image>)
3. On selecting the object, observe the details of the Snapshot1 and Sanpahot2.
4. The Snapshot1 represents the backup selected for the comparison to be performed against the “LIVE ORG”.
5. The label Snapshot2 will not display any data in it until the live compare is initiated.
6. After selecting the required backup. Click “LIVE COMPARE” to initiate the compare operation.
7. The live compare operation will fetch and display the objects in the next screen.
8. Observe the Snapshot2 which says **“Live Data”**.
9.  Choose the object to perform the compare operation on.



    ![](<../../../../.gitbook/assets/Unknown image (1)>)
10. Click on the object to observe the fields in the object.



    ![](<../../../../.gitbook/assets/Unknown image (2)>)
11. Click on the field, “Fields To Compare”, to observe the list of fields.

    ![](<../../../../.gitbook/assets/Unknown image (3)>)

    ![](<../../../../.gitbook/assets/Unknown image (4)>)
12. **The “Clickable Object” and the “Fields To Compare” is useful to specify the fields that should be part of the compare operation.**
    1. **Only the fields selected under these will be part of the compare operation.**&#x43;lick on the “COMPARE” button to initiate the compare operation.
13.

    ![](<../../../../.gitbook/assets/Unknown image (5)>)
14. Clicking compare will show the **“Compare -Save Config”** screen.



    ![](<../../../../.gitbook/assets/Unknown image (6)>)
15. Observe the following fields on the screen:
    1. **Label(required field):** Enter a label for the job
    2. **Preserve the result for:** will specify the retention period for the compare results. _**The minimum retention period is for “7 Days” and the maximum retention period for the compare results will be for “30 Days” only.**_
    3. Description: allows to enter a fitting description to the job.
16. Click **“SAVE”** on entering all the required details.
17. Clicking “SAVE” will show a pop-up saying, “Comparison is initiated successfully. Notification will be sent to your email once the comparison is completed.”
18. Once the compare job is completed, an email will be triggered to the user.
19. Click “OK” to be redirected to the **“JOB HISTORY”** page of the flow.
20. Observe the list of jobs on the page.



    ![](<../../../../.gitbook/assets/Unknown image (7)>)
21. The recently triggered job will be initially in progress, until the job run is completed.
22. Once the jobs run is completed successfully, a blue tick”![Tick with solid fill](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAPCAYAAAAyPTUwAAAAAXNSR0IArs4c6QAAAHhlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAKgAgAEAAAAAQAAAAugAwAEAAAAAQAAAA8AAAAA0dUkjgAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAAPdJREFUKBVjYBgFJISA284X3A77/7OAtDDh05d87ru8jLDAfAXOT25gxQ3//zOFrrrKhq4p7sI36f8M/ycxMv2XZ2RjegBWfPfEc3U+JaXIpCOveWEa0s580mD+/X/W/3//Of//ZYycb8R7DSTHwsTGz/Xv3590Bk5uneRjH9t/szHp/2ZkbmRg/H+N4S9j6zwzjscwQ1i+GXFd4Dr9ZQIzw/8yRnb2/8z//+gxMPy/8+fP787F5gJwhSANjCAC5O4HJz7YMbNzdf7782sH059/E+da8b8DySEDsGKQAEjD4+sfZH/9FnizWJ/xK7IirGyQBqwSUEEAnmpeCMrHoKEAAAAASUVORK5CYII=)” will be displayed at the status of the triggered job.



    ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (9)>)
23. Click on the “Compare Label” to navigate to the compare results screen.



    ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (10)>)
24. **Compare Results – View All Records**
    1. Displays a consolidated list of comparison results for the selected object using the chosen snapshot pair.
    2. Shows _All_ records by default, including unchanged, modified, and deleted entries.
    3. Provides category filters – **All**, **No Changes**, **Modifications**, and **Deletions** – to refine the displayed results.
    4. Includes options such as **Select Field**, **Review and Restore**, **Fields to Compare**, **Compare**, **Change View**, and **Export** for further actions.
    5. Allows searching within displayed columns and navigating through paginated results using **Previous 100 Rows** and **Next 100 Rows**.
25. **Compare Results – No Changes Filter**
    1.  Displays only those records that have no differences between Snapshot1 and Snapshot2.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (11)>)
    2. Highlights the No Changes filter as selected, narrowing the view to stable or unaffected records.
    3. Provides quick access to view record-level details using the View Records icon.
    4. All action buttons, such as **Fields to Compare, Compare, and Export**, remain available for further analysis.
26. **Compare Results – Modifications Filter**
    1.  Shows only modified records where field-level differences exist between Snapshot1 and Snapshot2.

        <figure><img src="../../../../.gitbook/assets/image (2266).png" alt=""><figcaption></figcaption></figure>
    2. Modified values are visually emphasized (**highlighted in yellow**) to help quickly identify field differences.
    3. Allows reviewing and restoring modified records through the Review and Restore option.
    4. Supports column-based analysis for changed fields and navigation through the filtered result set.
27. **Compare Results – Deletions Filter**
    1.  Displays only the deleted records identified between the compared snapshots.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (13)>)
    2. Highlights the Deletions filter as selected to isolate removed records.
    3. Deleted values are **visually marked red** for easy recognition.
    4. Allows opening individual record details using the View Records option.
    5. Retains access to export and comparison tools for audit or restoration purposes.
28. **View Records**
    1. Displays a list of comparison results with a View Records icon for each row, allowing detailed inspection of the selected record.
    2.  Each icon opens a window showing a side-by-side comparison of Backup Data and Live Data for the corresponding object record.

        <figure><img src="../../../../.gitbook/assets/image (2268).png" alt=""><figcaption></figcaption></figure>
    3. Shows three columns:
       1. Field – the field name being compared
       2. Backup Data – the value captured in the selected snapshot
       3. Live Data – the current value from the source org
    4.  Provides a clear view of individual field values, helping identify differences across snapshots.

        <figure><img src="../../../../.gitbook/assets/image (2269).png" alt=""><figcaption></figcaption></figure>
    5. Highlights differences wherever applicable to assist in identifying modifications quickly.
    6. Allows users to validate record-specific changes without navigating away from the comparison results page.
29. **Fields to Compare**
    1. Displays the Fields to Compare option, allowing refinement of the comparison by selecting only specific fields from the chosen Salesforce object.
    2.  Opens a field-selection window listing all available fields for the selected object, including the field label and API name.

        <figure><img src="../../../../.gitbook/assets/image (2270).png" alt=""><figcaption></figcaption></figure>
    3. Provides a Filter search bar to quickly locate specific fields.
    4.  Allows enabling or disabling fields using checkboxes to customize the comparison criteria.

        <figure><img src="../../../../.gitbook/assets/image (2271).png" alt=""><figcaption></figcaption></figure>
    5. Ensures essential fields remain selected and non-editable when required (e.g., ID field).
    6. Includes Apply and Cancel actions to confirm or discard field-selection changes.
    7. Once applied, updates the comparison results grid to display and compare only the selected fields.
30. **Change View**
    1.  Provides an option to customize the visible columns in the comparison results.

        <figure><img src="../../../../.gitbook/assets/image (2272).png" alt=""><figcaption></figcaption></figure>
    2. Opens a dialog displaying the list of all available fields for the selected object.
    3. Displays the count of currently selected fields and indicates the maximum allowed column limit.
31. **Change Visible Columns**
    1. Click Change View to open the field-selection panel.
    2.  Review the list of available fields and enable or disable specific columns using the checkboxes.

        <figure><img src="../../../../.gitbook/assets/image (2273).png" alt=""><figcaption></figcaption></figure>
    3. Use the Search bar to quickly locate fields by name.
    4. The system enforces a maximum of 20 columns visible at once; additional selections are restricted.
    5. Click OK to apply the updated view or Cancel to discard changes.
32. **Export Records**
    1.  Click Export on the Compare History page to download the comparison results.

        <figure><img src="../../../../.gitbook/assets/image (2274).png" alt=""><figcaption></figcaption></figure>
    2. **An Export dialog appears with three export options:**
       1. **All Records** – Exports every record involved in the comparison, regardless of what is currently visible.
       2. **Records Displayed on the Current Page** – Exports only the records shown on the active results page.
       3. **Selected Records** – Exports only the records manually selected using the row checkboxes.
    3.  Choose the preferred export option and click OK to generate the export file.

        <figure><img src="../../../../.gitbook/assets/image (2275).png" alt=""><figcaption></figcaption></figure>
    4. Click Cancel to close the dialog without exporting.
33. **Select Field**
    1. Enables refinement of the comparison by selecting specific fields to include in the record-level analysis.
    2. Selecting a record and clicking **Select Field** opens the field mapping window.
    3. Displays all available **Source Fields** with checkboxes to include or exclude fields from the comparison.
    4. Shows corresponding **Mapping Fields** side-by-side, allowing the user to align source fields with their appropriate target fields in the destination snapshot.
    5. Provides a **Search** option for quickly locating fields by name.
    6. Includes **RESET** to restore the default field mapping and **APPLY** to save the updated selection and mapping configuration.
    7. Allows cancellation of the action, returning to the Compare History view without making changes.
34. **Review and Restore Flow**
    1.  **When Review and Restore is selected**, a brief pre-restore guidance window is displayed. This prompt highlights important considerations before proceeding. After acknowledging the information, the **Restore Summary** window opens, allowing configuration of the restore operation.

        <figure><img src="../../../../.gitbook/assets/image (2276).png" alt=""><figcaption></figcaption></figure>
    2.  **The Restore Summary** includes the restore label, batch size, and notification email. It also provides a set of toggle-based options to control automation and data behavior during the restore—such as disabling workflows, triggers, validation rules, and flows, along with controls for duplicate handling, failed records, blank value overrides, and serial mode execution.

        <figure><img src="../../../../.gitbook/assets/image (2277).png" alt=""><figcaption></figcaption></figure>
    3.  **A short data overview** lists the objects involved, the number of fields, and the number of records included. Once the settings are reviewed, selecting Restore Now initiates the restore. Choosing Cancel closes the window without proceeding.

        <figure><img src="../../../../.gitbook/assets/image (2278).png" alt=""><figcaption></figcaption></figure>
35. **Restore Job Creation**After selecting records and clicking **Restore Now**, the process transitions automatically to the **Restore** module, where the newly initiated restore job becomes visible.
    1. The system loads the Restore dashboard filtered to the org and restore source used during the compare flow.
    2. The newly created restore job appears in the results list with key details such as label, date/time, duration, metadata counts, record counts, and job status.
    3. Standard restore job actions—view details, download logs, or delete—become available as soon as the job is listed.
    4. The job executes based on the restore settings configured in the Restore Summary window.
36. **Re-Run Compare Job**:The **Re-Run** action allows an existing compare job to be executed again using updated field selections or the same configuration.
37. **Access the Re-Run Option** 1.&#x20;
    1.  Navigate to Compare → Job History to view the list of completed compare jobs.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (25)>)
    2. In the **Actions** column, click the **Re-Run** icon for the desired job.
38. **Confirm Re-Run**
    1.  A confirmation dialog appears. Select **OK** to continue or **Cancel** to abort.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (26)>)
39. **Select Fields to Compare**
    1.  The Select Fields window opens, displaying all available fields for the selected object.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (27)>)
    2. Modify the field selections as needed.
    3. Click **COMPARE** to initiate the new comparison.
40. **Job Queued**
    1.  The job status updates to **In Queue**, indicating that the comparison is scheduled for execution.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (28)>)
41. **Job Initiation**
    1.  Once processed, the new run appears in the job history with a fresh timestamp and updated status.



        ![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (29)>)
