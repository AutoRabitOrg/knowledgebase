# Create a Feature Migration Template

### Overview <a href="#overview" id="overview"></a>

This details the step-by-step process to create a standard/community nCino migration template.

### Procedure <a href="#procedure" id="procedure"></a>

1. Hover your mouse over the **nCino** module and click on the option: **Feature Management.**

<figure><img src="../../../../../.gitbook/assets/image (1294).png" alt="" width="197"><figcaption></figcaption></figure>

2. Click on **New Feature Migration Template** button.

<figure><img src="../../../../../.gitbook/assets/image (1295).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, click **Create New** to create a fresh template and include objects of your choice.

<figure><img src="../../../../../.gitbook/assets/image (1296).png" alt=""><figcaption></figcaption></figure>

4. You'll be taken to the record-based configuration section, where you will find three tabs that need completed to proceed ahead:
   * **Metadata Configuration**
   * **Record Configuration and**
   * **Preview and Save**

#### Metadata Configuration <a href="#metadata-configuration" id="metadata-configuration"></a>

You need to provide basic information on this tab to create a feature migration template.

Under **Feature Details**, enter the items below:

1. **Name:** Provide a feature migration template name.
2. **Associated Partner:** The default associate partner would be nCino, which you can change if necessary.
3. **Version:** Enter the version number here. If you're creating the feature template for the first time, it is recommended to keep the version number as 1.0.

<figure><img src="../../../../../.gitbook/assets/image (1297).png" alt=""><figcaption></figcaption></figure>

Under the **Salesforce Org** **Details** section, do the following:

4. Choose your **Salesforce Org**.
5. Click **Fetch Objects** to retrieve all available objects in the selected Source Org.
6. By default, only nCino objects available in the Source Org will be auto-populated. To view all the objects available, click on **Show All** **Objects**.&#x20;
7. Using![](<../../../../../.gitbook/assets/image (1298).png>)/![](<../../../../../.gitbook/assets/image (1299).png>)button, you can select/deselect all the objects for your template. Or, use the **Ctrl** key and select multiple objects of your choice and move them to the selected tab using![](<../../../../../.gitbook/assets/image (1300).png>)/![](<../../../../../.gitbook/assets/image (1301).png>)button. Once you have selected the object, [ARM](https://www.autorabit.com/) will retrieve the fields included in that object behind the scenes.

<figure><img src="../../../../../.gitbook/assets/image (1302).png" alt=""><figcaption></figcaption></figure>

8. Click on **Next** to go to the **Record Configuration** Tab.

{% hint style="info" %}
**Important Note:** Only those objects will be considered nCino objects if their related prefix is included in the **Plugins** section under the [**My Account**](../../../arm-administration/user-management/manage-users-account-settings.md) page.
{% endhint %}

#### &#x20;Record Configuration <a href="#record-configuration" id="record-configuration"></a>

This tab is where you apply filters for the entry objects. Also, on the left side of the screen, you can see the list of items that are segregated into:&#x20;

1. **Selected List:** This will include a list of all objects that are part of your selected template and objects that you have chosen to add later on.
2. **Related List:** This section will only be displayed in the Attachment Object as your migration template feature is included.
3. **Required List**: This contains mandatory objects which you cannot exclude,
4. **Excluded List:** This section lists non-required data objects you could permanently exclude while creating a template so that the template does not contain data object information. Some of the objects are auto-selected depending on the selected template, and you have the option to de-select them as well.

<figure><img src="../../../../../.gitbook/assets/image (1303).png" alt="" width="210"><figcaption></figcaption></figure>

Based on the relationship between the objects, the AutoRABIT application will segregate the object sets, and applying a filter to each bucket is mandatory. By default, AutoRABIT will denote an object in a bucket as an entry point, which can be applied filter. This is not mandatory, but as a best practice, AutoRABIT recommends applying filters to the entry point object rather than any other object.

The **entry object** is selected by default, and the user can apply a filter. The entry object is denoted by **“E”**.

<figure><img src="../../../../../.gitbook/assets/image (1304).png" alt=""><figcaption></figcaption></figure>

**Applying the Filters**

Apply the filter(s) using the steps as shown below:

<figure><img src="../../../../../.gitbook/assets/image (1305).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1306).png" alt=""><figcaption></figcaption></figure>

Click **Add**.

<figure><img src="../../../../../.gitbook/assets/image (1307).png" alt=""><figcaption></figcaption></figure>

The filter query is added and displayed in the filter box. You can edit the query if any modification is required. Nevertheless, multiple queries can be added based on your requirements. **Validate** your query to see whether the query entered is stable. Additionally, you'll be able to view several records that will get fetched.

<figure><img src="../../../../../.gitbook/assets/image (1308).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1309).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. All records that get fetched will be in order by "ASC nFORCE\_\_lookupKey\_\_c." Nevertheless, if "nFORCE\_\_lookupKey\_\_c" is unavailable, then using order by "ASC Id," the records will be fetched.
2. For the **Attachment** object, the filter cannot be applied.
{% endhint %}

You can also use the **Query Editor** to execute a SOQL query on the selected Source Org. Results are displayed in a **Query Results** grid.

<figure><img src="../../../../../.gitbook/assets/image (1310).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1311).png" alt="" width="563"><figcaption></figcaption></figure>

Similar steps are to be followed for objects in other buckets as well.

<figure><img src="../../../../../.gitbook/assets/image (1312).png" alt=""><figcaption></figcaption></figure>

Once done, click **Next** to proceed to the **Preview and Save** screen.

{% hint style="info" %}
**Important Note:**

1. If your nCino objects include an Attachment object, users must confirm whether they want to fetch the Attachment dataset.
2. Check the number of attachments pulled for the job once the attachment object is selected for the data deployment. For each API call, Salesforce returns at least one and a maximum of five attachments based on the size of the attachments. More APIs calls will get triggered for more attachments, which may result in the APIs limit being exceeded and the application reporting an error.
{% endhint %}

#### Preview and Save <a href="#preview-and-save" id="preview-and-save"></a>

This is the summary page for the Feature Migration template you're about to create. You can view the features details, and filters you have applied for the last time before the template is created. Any change log information that needs to be added can be mentioned in the **Change Log** box.

<figure><img src="../../../../../.gitbook/assets/image (1313).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** **Related List** section will display only if the **Attachment** object is part of the Feature Migration Template.&#x20;
{% endhint %}

Click **Save,** and you will be redirected to the [Feature Migration Summary](feature-migration-summary-page.md) screen, where you can track your template recently created.
