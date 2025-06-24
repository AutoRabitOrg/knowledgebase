# Data Loader Configuration

### Data Loader Configuration: Overview <a href="#dataloader-configuration-overview" id="dataloader-configuration-overview"></a>

The Data Loader module in ARM is key to migrating data between Salesforce orgs. To prevent duplicate record creation during migration, ARM supports data synchronization using an **external ID**. This ensures consistent, reliable data movement between source and destination environments.

---

### Creating a New Data Loader Configuration <a href="#creating-a-new-dataloader-configuration" id="creating-a-new-dataloader-configuration"></a>

1. Log in to your **ARM** account.
2. Navigate to the **Dataloader** module and select **Data Loader Configuration**.

<figure><img src="../../../../.gitbook/assets/image (1106).png" alt="Navigation menu showing Data Loader Configuration option" width="341"></figure>

3. Click on **New Configuration** to begin creating a data migration setup.

<figure><img src="../../../../.gitbook/assets/image (1107).png" alt="New Configuration button in Data Loader Configuration screen"></figure>

4. On the configuration screen:
   - Enter a **Name** for the process.
   - Choose the **Source Org** and **Destination Org**.
   - Click **Login and Fetch Objects** to retrieve all source org objects.

<figure><img src="../../../../.gitbook/assets/image (1108).png" alt="Screen showing source and destination org selection"></figure>

5. Select the required **Objects** and their corresponding **Fields**. Use the **search filter** for quick lookup.

<figure><img src="../../../../.gitbook/assets/image (1109).png" alt="Object and field selection interface with search filter"></figure>

6. Click **Save** to store the configuration or **Save and Run** to execute the job immediately.

<figure><img src="../../../../.gitbook/assets/image (1110).png" alt="Save and Save and Run options for Data Loader jobs"></figure>

7. In the **Job Details** section:
   - View the configured objects and field mappings.
   - See success/failure status for each record.
   - Use the **Search** icon to locate record IDs:

<figure><img src="../../../../.gitbook/assets/image (1111).png" alt="Search icon to view destination record IDs"></figure>

   - Use the **Download** icon to export success/failure record logs:

<figure><img src="../../../../.gitbook/assets/image (1112).png" alt="Download icon for record ID reports"></figure>

<figure><img src="../../../../.gitbook/assets/image (1113).png" alt="Job details section with object mappings and record status"></figure>

<figure><img src="../../../../.gitbook/assets/image (1114).png" alt="Detailed job execution report view"></figure>

---

#### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (1115).png" alt="Action menu with edit, delete, clone, and log options"></figure>

1. **Edit:** Modify the configuration settings.
2. **Delete:** Remove the configuration.
3. **Clone:** Duplicate the configuration for reuse.
4. **Log:** Access detailed execution logs.
