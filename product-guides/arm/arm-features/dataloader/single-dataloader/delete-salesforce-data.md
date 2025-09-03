# Delete Salesforce Data

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

<figure><img src="../../../../../.gitbook/assets/2 (1).png" alt="Dataloader Process Summary screen"><figcaption></figcaption></figure>

* Name the process/job.
* Select or create a **Category**.
* Review the Object, Type (**Delete**), and impacted Records.

17. Schedule tasks as **Daily**, **Weekly**, or **On-demand**.
18. Click **`Save`** to save and run later.
19. Your job appears at the top in the **`Dataloader Summary`** screen.
20. Click **`Run`** to execute the job manually.

<figure><img src="../../../../../.gitbook/assets/image (86) (1) (1).png" alt="Run button in Dataloader Summary"><figcaption></figcaption></figure>

21. Choose criteria for running the Dataloader job:

| Configurations | Descriptions                                                                     |
| -------------- | -------------------------------------------------------------------------------- |
| **Batch Size** | Used when Bulk API is not selected. Ideal for small-volume real-time processing. |
| **Use UTF-8**  | Use UTF-8 encoding unless data contains non-English alphabets.                   |

22. Click **`Run`**.

<figure><img src="../../../../../.gitbook/assets/3 (1).png" alt="Run confirmation screen" width="563"><figcaption></figcaption></figure>

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
6. **VR/WFR** – Review and re-enable validation/workflow rules. See [Validation/ Workflow Rules](../validation-workflow-rules.md).

<figure><img src="../../../../../.gitbook/assets/image (76) (1) (1).png" alt="Validation/Workflow Rules list UI"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (77) (1) (1).png" alt="Sample validation rule execution log"><figcaption></figcaption></figure>

7. **Clone** – Duplicate a process. You can upload a new CSV and select another Salesforce Org.

<figure><img src="../../../../../.gitbook/assets/image (74) (1) (1) (1).png" alt="Cloning an existing dataloader process"><figcaption></figcaption></figure>
