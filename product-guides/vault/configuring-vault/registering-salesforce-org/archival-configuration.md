# Archival Configuration

## Step 4: Archive Configuration <a href="#step-4-archive-configuration" id="step-4-archive-configuration"></a>

This step allows you to view available components in your Salesforce Org and define an archival policy for selected components.

1. In the **Salesforce Registration** summary screen, find your Salesforce Org and click **Add Archival Config**.

<figure><img src="../../../../.gitbook/assets/image (219).png" alt="Add Archival Configuration button in Salesforce Registration summary screen"><figcaption><p>Launching archival configuration</p></figcaption></figure>

2. Select the components you want to archive.

<figure><img src="../../../../.gitbook/assets/image (220).png" alt="Component selection screen for archival"><figcaption><p>Selecting components for archival</p></figcaption></figure>

3. Use **Filter** to define criteria for fetching records.\
   &#xNAN;_&#x45;xample_: Fetch case records older than 1,000 days and in a closed state.
   * Validate the query to ensure accuracy.
   * Set a record count limit if needed.
   * Click **Apply** to confirm filter settings.

<figure><img src="../../../../.gitbook/assets/image (221).png" alt="Filter configuration modal showing criteria"><figcaption><p>Define and apply filter criteria</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (222).png" alt="Validation of filter results"><figcaption><p>Filter validation results</p></figcaption></figure>

4. Use the **Hierarchy** option to view child objects of selected parent objects.
   * Auto-selected child objects cannot be unchecked.
   * Manually choose other related objects if needed.

<figure><img src="../../../../.gitbook/assets/image (223).png" alt="Hierarchy schema view of objects"><figcaption><p>Hierarchy view of parent and child objects</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (224).png" alt="Example of hierarchy dependencies"><figcaption><p>Object dependencies displayed in schema view</p></figcaption></figure>

5. Click **Save** to close the hierarchy view. The icon is highlighted for objects where hierarchy is set.

<figure><img src="../../../../.gitbook/assets/image (225).png" alt="Hierarchy icon highlighted"><figcaption><p>Hierarchy enabled indicator</p></figcaption></figure>

6. Click **Next** to proceed to the archival schedule screen.

***

## Schedule Archive <a href="#schedule-archive" id="schedule-archive"></a>

1. On the schedule archive screen, complete the following:

* **Process Name**: Enter a name.
* **Email Notification**: Enable this to receive notifications before deletions.
* **Schedule**: Define the archival frequency (daily, weekly, monthly, or custom).
* **Archive Retention Period**: Set the duration for which data is retained.
* **Batch Size**: Maximum batch size is **10,000 records** per batch.
* **Enable Serial Mode for Bulk API**: Activates single-batch processing (slower but reliable).

<figure><img src="../../../../.gitbook/assets/image (226).png" alt="Archive scheduling options screen"><figcaption><p>Define schedule and performance settings</p></figcaption></figure>

2. Click **Save Config**.
3. Review the summary of your selected objects, filters, and policies.
4. Click **Save** to complete archival configuration.

<figure><img src="../../../../.gitbook/assets/image (227).png" alt="Summary screen of archival configuration"><figcaption><p>Final summary before saving archival settings</p></figcaption></figure>
