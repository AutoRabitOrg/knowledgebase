# Delete Salesforce Data

The following articles provide guidance on using **Single Dataloader** to delete data from Salesforce. Deletion requires a **CSV file** that contains the record IDs of the objects targeted for removal. Once the CSV file is prepared, the Single Dataloader can process the file and perform the deletions in bulk, ensuring accuracy and efficiency.

Step-By-Step Guide

1. **Delete Job – Login and Select Object**
   *   From the **Basic** tab in Dataloader, select **Create new job** and choose **Delete**.

       <figure><img src="../../../../../.gitbook/assets/1 - Delete.png" alt=""><figcaption></figcaption></figure>
   *   The **Create delete process** window opens, prompting to log in and select the Salesforce Org.

       <figure><img src="../../../../../.gitbook/assets/2 - Delete.png" alt=""><figcaption></figcaption></figure>
2. **Delete Job – Provide Salesforce Org Details**
   *   Enter the **Salesforce Org** details to establish the connection.

       <figure><img src="../../../../../.gitbook/assets/3 - Delete.png" alt=""><figcaption></figcaption></figure>
   * Provide the following fields:
     * **Salesforce Org**: Select from the available dropdown.
     * **Environment**: Specify the Salesforce environment (e.g., ProdDev, Sandbox).
     * **Login URL**: Enter the Salesforce login endpoint.
     * **Username**: Provide the Salesforce username.
   * Click **Login and Fetch Objects** to retrieve the list of objects available for deletion.
3. **Delete Job – Select Object**
   *   Once logged in successfully, the system fetches Salesforce objects for deletion.

       <figure><img src="../../../../../.gitbook/assets/4 - Delete.png" alt=""><figcaption></figcaption></figure>
   * Use the **Search bar** or scroll through the list to locate the required object.
   * Select the target object (e.g., **Contact**) for the delete operation.
   * Click **Next** to proceed with field mapping.
4. Delete Process
   *   Upload a CSV file for field mapping by selecting **Choose File** or dragging and dropping the file into the upload area.

       <figure><img src="../../../../../.gitbook/assets/6 - Delete.png" alt=""><figcaption></figcaption></figure>
   * The CSV file should contain the Salesforce record IDs of the objects to be deleted.
5. #### Delete Process
   *   Once uploaded, the file will be displayed in the **Upload file for fields mapping**, ready for mapping.

       <figure><img src="../../../../../.gitbook/assets/7 - Delete.png" alt=""><figcaption></figcaption></figure>
   * The file name, size, and format are displayed along with an option to remove it if required.
   * At this stage, the system is ready to process the uploaded file for mapping.
6. #### Delete Process
   *   Once the CSV file is validated, a success message confirms the file upload.

       <figure><img src="../../../../../.gitbook/assets/8 - Delete.png" alt=""><figcaption></figcaption></figure>
   * The system also displays the number of records that will be impacted by the operation.
   * This ensures visibility into the scope of the delete process before proceeding.
7. #### Delete Process
   * The uploaded file’s contents are displayed with source headers and sample data.
   * Each column from the CSV file can be mapped to a corresponding Salesforce field.
   *   The **AutoMap** feature may be toggled to automatically match source headers with Salesforce fields.

       <figure><img src="../../../../../.gitbook/assets/9 - Delete.png" alt=""><figcaption></figcaption></figure>
   * Once mapping is complete, select **Next** to proceed with scheduling or executing the delete process.
8. Delete Process
   * From the **Schedule** step of the delete process, select the desired scheduling type.
   *   By default, **No Schedule** is selected, meaning the process will run only once when executed.

       <figure><img src="../../../../../.gitbook/assets/10 - Delete.png" alt=""><figcaption></figcaption></figure>
   * Alternative scheduling options (**Daily** or **Weekly**) can be chosen to automate recurring delete operations.
9. #### Delete Process
   * When **Daily** is selected, define the scheduling start date and time.
   *   Choose whether the delete process should run at a **specific time** or at a fixed time interval.

       <figure><img src="../../../../../.gitbook/assets/11 - Delete.png" alt=""><figcaption></figcaption></figure>
   * Select when the scheduling should end:
     * **Never** (continues indefinitely),
     * **After X occurrences**, or
     * **On a specific date**.
   * This configuration enables recurring daily deletion of records as per the defined schedule.
10. #### Delete Process
    *   When **Weekly** is selected, specify the scheduling start date.

        <figure><img src="../../../../../.gitbook/assets/12 - Delete.png" alt=""><figcaption></figcaption></figure>
    * Select the desired day(s) of the week for the delete process to run.
    * Enter the time of execution for the scheduled deletion.
    * Choose when the scheduling should end:
      * **Never**,
      * **After X occurrences**, or
      * **On a specific date**.
    * This option is suitable for weekly recurring delete processes aligned with business or operational cycles.
11. Delete Process
    *   From the **Process Details** step, review the configuration summary, including the object name, type of operation, and the number of records selected for deletion.

        <figure><img src="../../../../../.gitbook/assets/13 - Delete.png" alt=""><figcaption></figcaption></figure>
    * Input a Process Name.
    * Optionally, assign the process to a **Job Group** for easier categorization and tracking.
    * Enable the **Hard Delete Records** option to permanently remove the records from Salesforce.
      * If enabled, records will not be moved to the Recycle Bin and cannot be restored.
      * This action should only be used when permanent deletion is necessary.
    * Once all details are confirmed, select **Save** to finalize the delete process configuration.
12.





























The following articles describe using **Single Dataloader** to delete data from Salesforce. To delete data, you need a CSV file containing the IDs of the objects to delete. Follow the steps below:

1. Log in to your ARM account.
2. Hover your mouse over the **`Dataloader`** module and choose the **`Dataloader`** option.
3. Click **`Delete`** on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (79) (1) (1).png" alt="Delete option on Dataloader page"><figcaption></figcaption></figure>

4. Choose your [**`Salesforce Org`**](broken-reference) and select your org environment (**`Production or Development Edition`**, **`Sandbox`**, or **`Pre-Release`**).
5. The corresponding **`URL`** and **`Username`** are auto-generated based on the selection.
6. Click **`Login and Fetch Objects`** to load all objects from your Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (80) (1) (1).png" alt="Login and Fetch Objects screen"><figcaption></figcaption></figure>

7. Select the object (e.g., **`Account`**, **`Contact`**, **`Lead`**). Use **`search`** and **`filter`** options to find standard/custom objects.
8. Click **`Next`**.

<figure><img src="../../../../../.gitbook/assets/image (81) (1) (1).png" alt="Object selection screen in Dataloader"><figcaption></figcaption></figure>

9. Upload your **CSV** file by clicking **`Upload`**.

<figure><img src="../../../../../.gitbook/assets/image (82) (1) (1).png" alt="CSV upload screen"><figcaption></figcaption></figure>

10. Confirm the number of impacted records in the popup. Click **`OK`**.

<figure><img src="../../../../../.gitbook/assets/image (83) (1) (1).png" alt="Notification showing impacted records"><figcaption></figcaption></figure>

11. Prepare field mappings to match your CSV fields with Salesforce fields.
12. Use **`Automap`** to auto-match fields by name.

<figure><img src="../../../../../.gitbook/assets/image (84) (1) (1).png" alt="Automap field mapping UI"><figcaption></figcaption></figure>

13. View the number of mapped vs. total fields below the Automap checkbox.
14. Use **`search`** to locate fields and **`Filter`** to narrow down:
    * **All** – Displays all fields.
    * **Mapped** – Only mapped fields.
    * **Unmapped** – Only unmapped fields.
15. Ensure all required fields are mapped, then click **`Next`**.
16. On the **`Process Summary`** screen:

<figure><img src="../../../../../.gitbook/assets/image (85) (1) (1).png" alt="Dataloader Process Summary screen"><figcaption></figcaption></figure>

* Name the process/job.
* Select or create a **Category**.
* Review the Object, Type (**Delete**), and impacted Records.
* Enable **Use Bulk API** for large datasets. This uses REST principles and parallelism for better performance.

17. Schedule tasks as **Daily**, **Weekly**, or **On-demand**.
18. Click **`Save`** to save and run later.
19. Your job appears at the top in the **`Dataloader Summary`** screen.
20. Click **`Run`** to execute the job manually.

<figure><img src="../../../../../.gitbook/assets/image (86) (1) (1).png" alt="Run button in Dataloader Summary"><figcaption></figcaption></figure>

21. Choose criteria for running the Dataloader job:

| Configurations   | Descriptions                                                                                                                                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use Bulk API** | Optimized for high-volume operations. Supports parallel and serial execution. For delete operations on the same org, **Serial Mode** is recommended. |
| **Batch Size**   | Used when Bulk API is not selected. Ideal for small-volume real-time processing.                                                                     |
| **Use UTF-8**    | Use UTF-8 encoding unless data contains non-English alphabets.                                                                                       |

22. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/image (87) (1) (1).png" alt="Run confirmation screen"><figcaption></figcaption></figure>

23. The **`Results of Last Run`** section shows live updates of successful and failed record deletions. You can view/download records in CSV format.

<figure><img src="../../../../../.gitbook/assets/image (88) (1) (1).png" alt="Run results summary showing deleted records"><figcaption></figcaption></figure>

24. The number of impacted records is updated dynamically in the **Records** section.

***

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (78) (1) (1).png" alt="More options menu"><figcaption></figcaption></figure>

1. **Edit** – Modify job details.
2. **Abort** – Stop a running process.
3. **Schedule** – Set job run schedule.
4. **Delete** – Delete the configured job.
5. **Log** – View execution logs.
6. **VR/WFR** – Review and re-enable validation/workflow rules. See [Validation/ Workflow Rules](../../../../arm/arm-features/dataloader/validation-workflow-rules.md).

<figure><img src="../../../../../.gitbook/assets/image (76) (1) (1).png" alt="Validation/Workflow Rules list UI"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (77) (1) (1).png" alt="Sample validation rule execution log"><figcaption></figcaption></figure>

7. **Clone** – Duplicate a process. You can upload a new CSV and select another Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (74) (1) (1) (1).png" alt="Cloning an existing dataloader process"><figcaption></figcaption></figure>
