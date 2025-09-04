# Data Loader Configuration

### Data Loader Configuration: Overview <a href="#dataloader-configuration-overview" id="dataloader-configuration-overview"></a>

The Data Loader module in ARM is key to migrating data between Salesforce orgs. To prevent duplicate record creation during migration, ARM supports data synchronization using an **external ID**. This ensures consistent, reliable data movement between source and destination environments.

### Step-By-Step Guide

1. **Create New Configuration**
   *   From the **Dataloader Configuration** page, click **New Configuration** to initiate a new setup.

       <figure><img src="../../../../.gitbook/assets/1 - Configuring Dataloader (1).png" alt=""><figcaption></figcaption></figure>
   * This action opens the **New Configuration** page where Salesforce Org details must be defined.
   * Configuration creation allows establishing connections between source and destination orgs for data migration.
2. **Enter Salesforce Org Details**
   *   On the **New Configuration** page, enter a **Name** for the configuration.

       <figure><img src="../../../../.gitbook/assets/2 - Configuring Dataloader (1).png" alt=""><figcaption></figcaption></figure>
   * Select the **Source Org** from the dropdown menu.
   * Select the **Destination Org** from the dropdown menu.
   * Click **Login and fetch objects** to proceed with retrieving available objects.
3. **Provide Configuration Information**&#x20;
   *   Input a meaningful configuration name in the **Name** field for easy identification.

       <figure><img src="../../../../.gitbook/assets/3 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * Confirm that the correct **Source Org** and **Destination Org** are selected.
   * This ensures the data transfer is mapped between the right Salesforce environments.
4. **Verify Configuration Details**
   *   Review the **Name**, **Source Org**, and **Destination Org** entries.

       <figure><img src="../../../../.gitbook/assets/4 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * Once verified, click **Login and fetch objects** to load available objects for configuration.
   * This step is essential before proceeding to object and field selection.
5. **Select Objects and Fields**
   *   A list of available Salesforce objects is displayed with their **Label Name** and **API Name**.

       <figure><img src="../../../../.gitbook/assets/5 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * Select the required objects by marking the checkbox next to each entry.
   * Use the search bar if needed to quickly locate a specific object.
6. **Choose Object Fields**&#x20;
   *   Expand the selected object to display its available fields.

       <figure><img src="../../../../.gitbook/assets/6 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * Select the fields required for the configuration (e.g., **Annual Revenue**, **Billing Address**, **Billing City**).
   * Fields marked with “Is Unique” provide uniqueness constraints that can be applied if necessary.
   * Click **Save** to store the configuration or **Save and Run** to execute it immediately.
7. **Run Configuration**
   *   From the Dataloader Configuration page, locate the desired configuration.

       <figure><img src="../../../../.gitbook/assets/7 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * Select the **Run** icon under the Actions column.
   * This triggers execution of the chosen configuration.
8. **Execution in Progress**
   *   Once initiated, the configuration run shows a progress indicator.

       <figure><img src="../../../../.gitbook/assets/8 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * The status updates dynamically to reflect the ongoing execution.
9. **In Progress Status**
   *   During execution, the **Status** column displays **In Progress**.

       <figure><img src="../../../../.gitbook/assets/9 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
   * This indicates that the configuration is actively processing.
10. **Abort Execution**
    *   While a configuration is running, select the **Abort** option.

        <figure><img src="../../../../.gitbook/assets/10 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * Aborting stops the execution immediately.
    * This action is useful if the run was triggered in error or needs to be halted.
11. **Completed Execution**
    *   After successful execution, the **Status** column updates with a green check.

        <figure><img src="../../../../.gitbook/assets/11 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * The configuration run is marked as completed.
    * Results can then be reviewed or re-run as required.
12. **View Job Results**
    * From the **Dataloader Configuration** page, select the ellipsis (three dots) for the desired job.
    *   Choose **Job Results** from the dropdown menu.

        <figure><img src="../../../../.gitbook/assets/12 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * This opens the configuration details page, displaying the objects, unique fields, and execution results.
13. **Copy Unique Field Set**
    *   Within the **Dataloader Configuration Details** page, locate the **Unique Fields Set** column.

        <figure><img src="../../../../.gitbook/assets/13 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * Select the **Copy** icon next to the listed unique field.
    * The field is copied to the clipboard for reuse in other configurations or references.
14. **Copy Confirmation**
    *   After copying, a **Success** message appears at the top right of the screen.

        <figure><img src="../../../../.gitbook/assets/13.1 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * The notification confirms that the **Unique Fields Set** has been successfully copied.
15. #### View Success Results
    *   From the **Dataloader Configuration Details** page, locate the **Results of Last Run** section.



        <figure><img src="../../../../.gitbook/assets/14 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * Select the **Success count** link (e.g., “Success: 623”) to review detailed results of successfully processed records.
    * This opens a detailed view of the success log.
16. #### Review Success Log
    *   A **CSV Result** view is displayed, listing each **Destination Record Id** along with its **Status** (e.g., “Item Updated”).

        <figure><img src="../../../../.gitbook/assets/15 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * Navigate through the pages to review all processed records.
    * This provides a complete audit trail of records updated or inserted successfully.
17. **Edit Configuration**
    * From the Dataloader Configuration page, select the ellipsis (three dots) for a specific configuration.
    *   Choose **Edit** from the dropdown menu.

        <figure><img src="../../../../.gitbook/assets/16 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * This opens the Dataloader Configuration Edit page, allowing updates to Salesforce Org details and object/field selections.
18. **Modify Configuration**
    *   The Dataloader Configuration Edit page displays the previously saved configuration details.

        <figure><img src="../../../../.gitbook/assets/16.1 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * Objects and fields can be adjusted as required to reflect the updated configuration.
    * Once changes are made, they can be saved to update the existing configuration.
19. **Delete Configuration**
    * From the Dataloader Configuration page, open the ellipsis (three dots) menu for the selected configuration.
    *   Choose **Delete** to initiate removal of the configuration.

        <figure><img src="../../../../.gitbook/assets/17 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * A confirmation dialog appears, displaying the configuration name for verification.
    *   Select **Delete** to permanently remove the configuration, or **Cancel** to abort the action.

        <figure><img src="../../../../.gitbook/assets/18 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * This operation cannot be undone and should only be performed when the configuration is no longer needed.
20. #### Clone Configuration
    * From the **Dataloader Configuration** page, select the ellipsis (three dots) corresponding to the job that needs to be cloned.
    *   Choose **Clone** from the dropdown menu to duplicate the existing configuration.

        <figure><img src="../../../../.gitbook/assets/19 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * A **Clone Configuration** dialog will appear, prefilled with the original job name appended with “-Copy.”
    * Verify or update the **Name**, **Source Sandbox**, and **Destination Sandbox** values as needed.
    *   Select **Clone** to finalize the process.

        <figure><img src="../../../../.gitbook/assets/20 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * The cloned configuration will be created and displayed in the Dataloader Configuration list, ready for execution or modification.
21. **View Logs**
    * From the Dataloader Configuration page, select the ellipsis (three dots) for a specific job.
    *   Choose **Log** to open the detailed execution log for that configuration.

        <figure><img src="../../../../.gitbook/assets/22 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    *   The log provides complete step-by-step information about the process, including record fetch details, field mappings, execution progress, and success or failure counts.

        <figure><img src="../../../../.gitbook/assets/23 - Configuring Dataloader.png" alt=""><figcaption></figcaption></figure>
    * This feature is useful for troubleshooting and auditing the data operation.
