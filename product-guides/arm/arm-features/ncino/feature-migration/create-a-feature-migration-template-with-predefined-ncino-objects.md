# Create a Feature Migration Template with Predefined nCino Objects

### Overview <a href="#overview" id="overview"></a>

This article deals with the step-by-step procedure to create a standard/community template by picking a feature with nCino predefined objects.

### Procedure <a href="#procedure" id="procedure"></a>

1. Hover your mouse over the **`nCino`** module and click on the option: **`Feature Management`.**

<figure><img src="../../../../../.gitbook/assets/image (1314).png" alt="" width="239"><figcaption></figcaption></figure>

2. Click on **`New Feature Migration Template`** button.

<figure><img src="../../../../../.gitbook/assets/image (1315).png" alt=""><figcaption></figcaption></figure>

3. Choose one of the features from the list. _**For example,**_ select the **`Spreads Schedule Template`** tile to include the **Spreads Schedules** feature predefined objects in a template.

<figure><img src="../../../../../.gitbook/assets/image (1316).png" alt=""><figcaption></figcaption></figure>

4. You'll be navigated to **`Record Based Configuration`** section, where you will find _three tabs_ that need to fill in to proceed ahead:
   * _Metadata Configuration_
   * _Record Configuration and_
   * _Preview and Save_

#### Metadata Configuration <a href="#metadata-configuration" id="metadata-configuration"></a>

To create a feature migration template, you must provide basic details on this tab.

Under **`Feature Details`** section, fill in the below details:

1. **`Name:`** Provide a feature migration template name.
2. **`Associated Partner:`** The default associate partner would be nCino, which you can change if necessary.
3. **`Version:`** Enter the version number here. If you're creating the feature template for the first time, it is recommended to keep the version number as **1.0**.

<figure><img src="../../../../../.gitbook/assets/image (1317).png" alt=""><figcaption></figcaption></figure>

Under the **`Salesforce Org Details`** section, do the following:

4. Choose your **`Salesforce Org`**.
5. Click **`Fetch Objects`** to retrieve all available objects in the selected source org. Predefined objects will be auto chosen based on your selected feature. By default, only nCino objects available in the source org will get auto-populated. To view all the objects available, click on **`Show All`** objects.
6. Using![](<../../../../../.gitbook/assets/image (1298).png>)/![](<../../../../../.gitbook/assets/image (1299).png>)button, you can select/deselect all the objects for your template. Or, use the **Ctrl** key and select multiple objects of your choice and move them to the selected tab using![](<../../../../../.gitbook/assets/image (1300).png>)/![](<../../../../../.gitbook/assets/image (1301).png>)button. Once you have selected the object, ARM will retrieve the fields included in that object behind the scenes.

<figure><img src="../../../../../.gitbook/assets/image (1318).png" alt=""><figcaption></figcaption></figure>

7. Click **`Next`** to go to the **`Record Configuration`** tab.

#### &#x20;Record Configuration <a href="#record-configuration" id="record-configuration"></a>

This tab is where you apply filters for the entry objects. Also, on the left side of the screen, you can see the list of items that are segregated into:&#x20;

1. **`Selected List:`** This will include a list of all objects that are part of your selected template and objects that you have chosen to add later.
2. **`Related List:`** This section will only be displayed in the Attachment Object for your migration template feature is included.
3. **`Required List:`** This contains mandatory objects, and you cannot exclude them,
4. **`Excluded List:`** This section lists non-required data objects you could permanently exclude while creating a template so that the template does not contain data object information. Depending on the selected template, some objects are auto-selected, and you can deselect them.

<figure><img src="../../../../../.gitbook/assets/image (1319).png" alt="" width="250"><figcaption></figcaption></figure>

Based on the object's relationship, the AutoRABIT application will segregate the object sets, and applying a filter on each bucket is mandatory. By default, AutoRABIT will denote an object in a bucket as an entry point, which can be applied filter. This is not mandatory, but as a best practice, AutoRABIT recommends applying filters to the entry point object rather than any other object.

The entry object is selected by default, and the user can apply a filter. The entry object is denoted by **`“E”`**.

<figure><img src="../../../../../.gitbook/assets/image (1320).png" alt=""><figcaption></figcaption></figure>

**Applying the Filters**

Apply the filter(s) using the steps as shown below:

<figure><img src="../../../../../.gitbook/assets/image (1321).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1322).png" alt=""><figcaption></figcaption></figure>

Click **`Add`**. The filter query gets added and gets displayed in the filter box. You can edit the query if any modification is required. Nevertheless, multiple queries can be added based on your requirement. **`Validate`** your query to see if the query entered is stable or not. Additionally, you'll be able to view several records that will get fetched.

<figure><img src="../../../../../.gitbook/assets/image (1323).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1324).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. All records that get fetched will be in order by **"ASC nFORCE\_\_lookupKey\_\_c."** Nevertheless, if **"nFORCE\_\_lookupKey\_\_c"** is unavailable, then using order by **"ASC Id,"** the records will be fetched.
2. For the **Attachment** object, the filter cannot be applied.
{% endhint %}

You can also use the **`Query Editor`** to execute a SOQL query on the selected source org. Results are displayed in a **`Query Results`** grid.

<figure><img src="../../../../../.gitbook/assets/image (1325).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1326).png" alt="" width="563"><figcaption></figcaption></figure>

Similar steps are to be followed for objects in other buckets as well. Once done, click **`Next`** to proceed to the **`Preview and Save`** screen.

{% hint style="info" %}
**Important Note:**

1. If your nCino objects include an **Attachment** object, the users must confirm whether they want to fetch the **Attachment** dataset.
2. Please check the number of attachments pulled for the job once the attachment object is selected as part of the data deployment. For each API call, Salesforce returns at least one and a maximum of five attachments based on the size of the attachments. For more attachments, more APIs call will get triggered, which may result in the APIs limit exceeding and the application to throw an error.&#x20;
{% endhint %}

#### Preview and Save <a href="#preview-and-save" id="preview-and-save"></a>

This is the summary page for the feature migration template you're about to create. You can view the features details, and filters you have applied for the last time before the template is created. Any change log information that needs to be added can be mentioned in the **`Change Log`** box.

<figure><img src="../../../../../.gitbook/assets/image (1327).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:`Related List`** section will display only if the **`Attachment`** object is a part of the Feature Migration Template.&#x20;
{% endhint %}

Click **`Save,`** and you will be redirected to the [Feature Migration Summary](feature-migration-summary-page.md) screen, where you can track your template recently created.
