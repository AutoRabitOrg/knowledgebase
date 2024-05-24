# Archival Configuration

### Step 4: Archive Configuration <a href="#step-4-archive-configuration" id="step-4-archive-configuration"></a>

The archive configuring is all about viewing the components that are available in your Salesforce org and choosing the components for which you want to define the archival policy.

1. In the **Salesforce Registration** summary screen, look for your Salesforce Org and click on **Add Archival Config**.

<figure><img src="../../../../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

2. Select the components that you need to archive on the next screen.

<figure><img src="../../../../.gitbook/assets/image (220).png" alt=""><figcaption></figcaption></figure>

3. You can define the criteria for which the records will be fetched using **Filter**.\
   **For example**, if you can define criteria to fetch case records that are older than 1,000 days and are in a closed state.Validate your query to see whether the criteria set is correct and view the number of records that will be fetched. You can even set the record count limit for your data being fetched. Click on **Apply** to set the criteria and close the Filter dialog box. The filter icon is highlighted for easy identification of objects on which the filter is applied.

<figure><img src="../../../../.gitbook/assets/image (221).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure>

4. The **Hierarchy** option will allow you to view your selected object's corresponding child objects. These child objects will also be archived once you archive their parent object. Such a hierarchy schema view can be seen using the **Hierarchy** option.\
   You may notice in the schema view that some of the objects are auto-selected by default and cannot be unchecked. These are the child objects of its parent object that will be deleted for sure if its parent object is selected for archival policy. However, for other objects which are related to the selected object in some other way, you may have the option to choose them manually for archival.

<figure><img src="../../../../.gitbook/assets/image (223).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (224).png" alt="" width="563"><figcaption></figcaption></figure>

5. Once done, click **Save** to close the hierarchy-schema screen. Similar to **Filter** criteria addition, the hierarchy icon gets highlighted corresponding to the object for which the hierarchy is selected.

<figure><img src="../../../../.gitbook/assets/image (225).png" alt=""><figcaption></figcaption></figure>

6. Click on **Next** which will take you to the schedule archival screen to plan the archive operation.&#x20;

### **Schedule Archive** <a href="#schedule-archive" id="schedule-archive"></a>

1.  On the schedule archive screen, do the following:

    * Give the process a **name**.
    * Select the **email notification** checkbox to receive an email notification whenever objects are being deleted from your Salesforce Org. If unchecked, data will automatically be deleted without any prior notification.
    * Select the date and time interval for the archival process to run under the **Schedule Archive** section. You can set the policy to run either daily, weekly, or monthly or input any duration manually.
    * You can specify how long you want to retain the archived data under the **Archive Retention period** section.
    * Specify the **batch size** for components to retrieve records. The max batch size you can set per batch is **10,000** records. This option is useful for running large jobs exceeding normal processing limits. Per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using batch size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records in batches is your best solution.
    * **Enable serial mode for Bulk API:** Serial mode processes batch one at a time; however, it increases the processing time for a load.

    <figure><img src="../../../../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>
2. Click **Save Config**.
3. A summary of all the objects, filters, and criteria selected or applied will be displayed before your archive policy is configured. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>
