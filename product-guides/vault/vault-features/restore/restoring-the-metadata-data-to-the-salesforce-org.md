# Restoring the Metadata/Data to the Salesforce Org

### Overview <a href="#overview" id="overview"></a>

This article discusses the procedure for restoring metadata and data to your Salesforce organization and the menu options available for restoring information in Vault.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

* Salesforce Org registered with Vault.&#x20;
* Backup configured for your Salesforce Org. \[[Learn More](../../configuring-vault/registering-salesforce-org/setup-backup-configuration-for-salesforce-org.md)]
* At least one backup operation is triggered for your Salesforce Org in Vault.

### How to do it? <a href="#how-to-do-it" id="how-to-do-it"></a>

1. Login to your Vault account.
2. Click **`Restore`** from the Vault dashboard page and click on **`Restore Now`**.

<figure><img src="../../../../.gitbook/assets/image (25) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, select your source [**`Salesforce Org`**](../../configuring-vault/registering-salesforce-org/).

<figure><img src="../../../../.gitbook/assets/image (26) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. Next, select the **`restore source`** and its **`configuration`** from the drop-down.

<figure><img src="../../../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

5. Click **`Get Details`**.
6.  The configured list will be displayed based on the restore source and configuration selection.

    * To restore the **source** as **`backup`**, select multiple backups for restoration.

    <figure><img src="../../../../.gitbook/assets/image (28) (1).png" alt=""><figcaption></figcaption></figure>

    * For **`hierarchical backup`** and **`archival`**, you can choose only one from the list.

    <figure><img src="../../../../.gitbook/assets/image (29) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (30) (1).png" alt=""><figcaption></figcaption></figure>
7. Click on either **`EZ Restore`** or **`Selective Restore`**.Important Note:Restore Source as **`nCino features`** will be displayed only for Salesforce Orgs configured with nCino objects. For detailed nCino restore features, refer to the article: [nCino Restore Features](../knowledge-articles/ncino/restoring-ncino-features.md).

#### EZ-Restore <a href="#ezrestore" id="ezrestore"></a>

EZ-Restore copies everything from the source to the destination, including new, updated, and existing data.

**EZ-Restore Steps:**

1. Select the backup(s) from the list and click on the **`EZ Restore`** button.

<figure><img src="../../../../.gitbook/assets/image (31) (1).png" alt=""><figcaption></figcaption></figure>

2. The **restore checklists** are displayed on the next pop-up screen, which must be considered before proceeding with the restoration operation. Once you're done, click the **`Got It`** button.&#x20;

<figure><img src="../../../../.gitbook/assets/image (32) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen:
   * Enter the **`label`** of your choice or leave the auto-generated default label.
   * Specify the **`batch size`** for components to retrieve records. The max batch size that you can set per batch is **10K**. This option helps run large jobs exceeding normal processing limits. Per the Salesforce governor limit, you can deploy or retrieve up to **10,000 files** at once or a max size of **40 MB**. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is your best solution.
   * Choose the **recipients** from the **`Email notification`** dropdown who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be checked by default.
4. Next, you can select the **criteria** for the restore to be performed:
   * **`Disable Workflows:`** On selection, all the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the restore is completed, workflows are reactivated.
   * **`Disable Validation Rules:`** Validation rules verify that the data a user enters in a record meets your specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data will be transferred from the source to the destination sandbox. Once the restore is done, validation rules are reactivated.
   * **`Enable serial mode for Bulk API:`** Serial mode processes batch one at a time; however, it increases the processing time for a load.
   * **`Disable Relationship Mapping:`** The child objects related to selected objects will not be fetched on selection.
   * **`Disable Triggers:`** To ensure a successful recovery when working with data and metadata, you may wish to disable any triggers you have set. _This feature disables Salesforce triggers only.  Any managed package triggers will not be disabled._
5. The list of **metadata** and **data** objects replicated will be displayed for the last time before the restore process begins. You will not have options to select individual objects as it is an entire restore process.
6. Click **`Restore Now`**.

<figure><img src="../../../../.gitbook/assets/image (33) (1).png" alt="" width="547"><figcaption></figcaption></figure>

#### Selective Restore <a href="#selective-restore" id="selective-restore"></a>

This option allows you to select specific metadata or data that gets restored only to the target organization.&#x20;

Select the backup(s) from the list and click on the **`Selective Restore`** button.

<figure><img src="../../../../.gitbook/assets/image (34) (1).png" alt=""><figcaption></figcaption></figure>

The next screen displays the metadata and data objects that will be replicated. From the list of **`Metadata`** and **`Data`** type components, the user needs to select the components (along with their members) that will be restored.

1. Under the **`Metadata`** tab, choose the metadata members for each metadata type.

<figure><img src="../../../../.gitbook/assets/image (35) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (36) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (37) (1).png" alt=""><figcaption></figcaption></figure>

2. Under the **`Data`** tab, you have multiple configurations to choose from:

<figure><img src="../../../../.gitbook/assets/image (38) (1).png" alt=""><figcaption></figcaption></figure>

* **`Schema:`** The schema will allow you to view your selected object's corresponding child objects. With the most recent **Vault 23.1** release, we improved the schema representation by showing one level of the child/parent objects at a time. The tree can now be expanded based on your selection rather than the entire tree, which speeds up the download of the schema data and improves the UI.

<figure><img src="../../../../.gitbook/assets/image (39) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (40) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. You may notice in the _schema_ view that some objects are auto-selected by default and cannot be unchecked. These are child objects of a parent object, which will be restored if its parent object is selected. However, for other objects related to the selected object in some other way, you can choose them manually.
2. When you click the **`Save`** button, a warning popup appears, stating that you must select the appropriate hierarchy for the restore procedure or the process will fail. Click **`OK`** to dismiss the popup notification and return to the previous screen.

<img src="../../../../.gitbook/assets/image (46) (1).png" alt="" data-size="original">
{% endhint %}

* **`Selected Records:`** By default, all the records available in the objects will be auto-selected. To choose specific records, click **`All`** under **`Selected Records,`** which will lead you to a popup box where you can select the record. Post-selection, the summary table should show the number of records set.

<figure><img src="../../../../.gitbook/assets/image (47) (1).png" alt=""><figcaption></figcaption></figure>

You also have the option of importing records from a CSV file. To upload the CSV from your local system, click the **`Choose File`** button in the top right corner of the screen.

<figure><img src="../../../../.gitbook/assets/image (48) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (49) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (50) (1).png" alt=""><figcaption></figcaption></figure>

* **`Selected Fields:`** By default, all the fields will be chosen for the objects selected. Clicking **`“All”`** under the **`Selected Fields`** column will open a popup window with all the fields listed for the selected objects. You can also use the **search** filter to search for a specific field faster. Here, you can map your source field with the destination field. The destination field should default be mapped based on the source field name.

<figure><img src="../../../../.gitbook/assets/image (51) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. The mandatory fields are auto-selected, so you do not have the option to disable them. For example, the **`ID`** field.
2. It is mandatory to select at least one field; if no field is selected and you try to proceed further, a warning popup will be displayed stating, **`“Select at least one field to proceed.”`**
3. The unchecked fields will have a null value in the record.
{% endhint %}

Based on your selection, the restore will happen only for selected fields. Post selection, the summary table should show the number of fields selected.

<figure><img src="../../../../.gitbook/assets/image (52) (1).png" alt=""><figcaption></figcaption></figure>

3. Click on **`Trigger Restore`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1644318580634.png" alt=""><figcaption></figcaption></figure>

* The restore checklists are displayed on the next pop-up screen, which must be considered before proceeding with the restoration operation. Click **`Got It`** to dismiss the popup.&#x20;

<figure><img src="../../../../.gitbook/assets/image (53) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen:
   * Enter the **`label`** of your choice or leave the auto-generated default label.
   * Specify the **`batch size`** for components to retrieve records. The max batch size that you can set per batch is **10K**. This option helps run large jobs exceeding normal processing limits. Per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40 MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is your best solution.
   * Choose the recipients from the **`Email notification`** dropdown who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be checked by default.
   * Next, select the criteria for the restore to be performed:
     1. **`Disable Workflows:`** On selection, all the workflows of the Salesforce objects are deactivated, and the data will be transferred from the source to the destination sandbox. Once the restore is completed, workflows are reactivated.
     2. **`Disable Validation Rules:`** Validation rules verify that the data a user enters in a record meets your specified criteria before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data will be transferred from the source to the destination sandbox. Once the restore is done, validation rules are reactivated.
     3. **`Enable serial mode for Bulk API:`** Serial mode processes batch one at a time; however, it increases the processing time for a load.
     4. **`Disable Relationship Mapping:`** The child objects related to selected objects are not fetched on selection.
     5. **`Disable Triggers:`** To ensure a successful recovery when working with data and metadata, you may disable any triggers you have set. _This feature disables Salesforce triggers only. Any managed package triggers are not disabled._
5. Click **`Restore Now`**.

<figure><img src="../../../../.gitbook/assets/image (54) (1).png" alt="" width="563"><figcaption></figcaption></figure>

6. You'll be taken to the **`Restore Summary`** screen, which will display the status of the recently triggered restore activity.

### Restore Summary <a href="#restore-summary" id="restore-summary"></a>

For each restore activity triggered in Vault, you will find the details below:

<figure><img src="../../../../.gitbook/assets/image (55) (1).png" alt=""><figcaption></figcaption></figure>

| Attribute        | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Label`          | <p>The label name you assigned for your restore activity.<br>Click on the label to find the list of successful/failed metadata and data members that are part of the restore operation. Also, you can <strong>export</strong> to save the restored metadata/data info in CSV format locally. </p>                                                                                              |
| `Backup Info`    | Get a snapshot of your restore operation                                                                                                                                                                                                                                                                                                                                                       |
| `Date/Time`      | Date and time stamp for your restore operation                                                                                                                                                                                                                                                                                                                                                 |
| `Duration`       | Total time to complete the restore operation                                                                                                                                                                                                                                                                                                                                                   |
| `MetaSuccess`    | The total count of metadata objects successfully restored                                                                                                                                                                                                                                                                                                                                      |
| `MetaFailure`    | Total count of metadata objects that failed to restore                                                                                                                                                                                                                                                                                                                                         |
| `SuccessRecords` | The total count of data objects successfully restored                                                                                                                                                                                                                                                                                                                                          |
| `FailedRecords`  | Total count of data objects that was unable to restore                                                                                                                                                                                                                                                                                                                                         |
| `Status`         | Restore status (success or failure)                                                                                                                                                                                                                                                                                                                                                            |
| `Actions`        | <p>Additional actions:</p><ul><li><strong><code>Restore summary:</code></strong> View the restore summary report</li><li><strong><code>Log:</code></strong> Find the log details for your restore operation</li><li><strong><code>Abort:</code></strong> For an ongoing replicate operation, you can abort the process in between using the <strong><code>Abort</code></strong> icon</li></ul> |
