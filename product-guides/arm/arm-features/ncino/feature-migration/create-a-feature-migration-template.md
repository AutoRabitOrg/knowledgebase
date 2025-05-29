# Create a Feature Migration Template

## Overview <a href="#overview" id="overview"></a>

This details the step-by-step process to create a standard/community nCino migration template.

## What is a Feature Migration Template?&#x20;

A Feature Migration Template in AutoRABIT is essentially a blueprint that helps you manage and automate the process of moving features from one environment to another. It’s like a checklist that defines exactly what should be moved, how it should be transferred, and in what order — ensuring everything gets to the new environment correctly, without missing any critical steps.&#x20;

The template saves time and effort by letting you set up migration rules once and use them repeatedly for consistent, error-free deployments. Whether you're moving configurations, customizations, or entire features, the template streamlines the whole process, making it much smoother and more predictable.&#x20;

## Standard vs Community Templates&#x20;

**Standard Feature Templates**: These are templates that are pre-defined and ready to be used by customers/partners. Such templates are updated regularly as nCino releases changes to any configurations. AutoRABIT provides several default templates to be directly used by our community for migrating Record-Based Configurations (RBCs). &#x20;

**Community Feature Templates**: Community templates are non-standard templates. In other words, users can define their own migration templates that are not already published by AutoRABIT. Community templates are useful if there are any customizations in nCino users want to migrate that are not listed as part of the default Standard templates. &#x20;

Community templates, just like the Standard ones, are designed to be long-lasting. They need to be created once, and then can be used multiple times as a template.&#x20;

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

### Metadata Configuration <a href="#metadata-configuration" id="metadata-configuration"></a>

Metadata in the context of nCino is the same as that of Salesforce. It includes a collection of nCino customizations and configurations that together form a blueprint for your lending processes, e.g., Page Layout, Custom Field, Workflows and Automation.

Under **Feature Details**, enter the items below:

1. **Name:** Provide a feature migration template name.
2. **Associated Partner:** The default associate partner would be nCino, which you can change if necessary.
3. **Version:** Enter the version number here. If you're creating the feature template for the first time, it is recommended to keep the version number as 1.0.

<figure><img src="../../../../../.gitbook/assets/image (1297).png" alt=""><figcaption></figcaption></figure>

Under the **Salesforce Org** **Details** section, do the following:

4. Choose your **Salesforce Org**.
5. Click **Fetch Objects** to retrieve all available objects in the selected Source Org.
6. By default, only nCino objects available in the Source Org will be auto-populated. To view all the objects available, click on **Show All** **Objects**.&#x20;
7. Using![](<../../../../../.gitbook/assets/image (1298).png>)/![](<../../../../../.gitbook/assets/image (1299).png>)button, you can select/deselect all the objects for your template. Or, use the **Ctrl** key and select multiple objects of your choice and move them to the selected tab using the![](<../../../../../.gitbook/assets/image (1300).png>)/![](<../../../../../.gitbook/assets/image (1301).png>)button. Once you have selected the object, [ARM](https://www.autorabit.com/) will retrieve the fields included in that object behind the scenes.

<figure><img src="../../../../../.gitbook/assets/image (1302).png" alt=""><figcaption></figcaption></figure>

8. Click on **Next** to go to the **Record Configuration** Tab.

{% hint style="info" %}
**Important Note:** Only those objects will be considered nCino objects if their related prefix is included in the **Plugins** section under the [**My Account**](../../../arm-administration/user-management/manage-users-account-settings.md) page.
{% endhint %}

### Record Configuration <a href="#record-configuration" id="record-configuration"></a>

This section allows users to configure nCino records. The nCino platform that will be available to your end users solely depends on how the records are configured. Every record of nCino that the end user interacts with, you can configure a different outcome for the same. The entire platform’s behavior lies on these Record-Based Configurations (RBCs).&#x20;

1.  **Selected List**&#x20;

    This list shows the objects that you have explicitly picked to include in your migration. These are the features or configurations you actually want to move, like specific custom objects that are part of the change you're working on.&#x20;
2.  **Related List**&#x20;

    Objects in this list are automatically identified by AutoRABIT as being related to your selected objects. For example, if your selected object has lookup relationships or dependencies, those related objects will appear here. This ensures all necessary dependent data is considered during migration.&#x20;
3.  **Required List**&#x20;

    These are objects that AutoRABIT identifies as essential for the integrity of the migration. They are mandatory and cannot be removed from the template. This typically includes standard Salesforce objects or configurations that are foundational to the selected features.&#x20;
4.  **Excluded List**&#x20;

    This list comprises objects that are not required and have been explicitly excluded from the migration. You might place objects here to prevent unnecessary data from being migrated, especially if it's irrelevant to the current feature or could cause conflicts in the target environment. Note that such objects in the excluded list are still available for user selection (case-by-case basis).&#x20;

    &#x20;

    AutoRABIT automatically groups related objects into different buckets based on how they’re connected. While it’s not required, you’ll need to apply at least one filter to each bucket. By default, AutoRABIT marks one object in each bucket as the "entry point" — that’s the object the filter will apply to. Although you can choose any object, it’s generally a best practice to apply the filter to the entry point itself, since that helps keep things clean and consistent.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (1303).png" alt="" width="210"><figcaption></figcaption></figure>

Based on the relationship between the objects, the AutoRABIT application will segregate the object sets, and applying a filter to each bucket is mandatory. By default, AutoRABIT will denote an object in a bucket as an entry point, which can be applied by a filter. This is not mandatory, but as a best practice, AutoRABIT recommends applying filters to the entry point object rather than any other object.

The **entry object** is selected by default, and the user can apply a filter. The entry object is denoted by **“E”**.

<figure><img src="../../../../../.gitbook/assets/image (1304).png" alt=""><figcaption><p>Entry Object </p></figcaption></figure>

**Applying the Filters**

Apply the filter(s) using the steps as shown below:

<figure><img src="../../../../../.gitbook/assets/image (1305).png" alt=""><figcaption><p>Applying the Filters</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1306).png" alt=""><figcaption><p>Filter Selection</p></figcaption></figure>

Click **Add**.

<figure><img src="../../../../../.gitbook/assets/image (1307).png" alt=""><figcaption><p>Add the Filter</p></figcaption></figure>

The filter query is added and displayed in the filter box. You can edit the query if any modification is required. Nevertheless, multiple queries can be added based on your requirements. **Validate** your query to see whether the query entered is stable. Additionally, you'll be able to view several records that will get fetched.

<figure><img src="../../../../../.gitbook/assets/image (1308).png" alt=""><figcaption><p>Validate Your Query</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1309).png" alt=""><figcaption><p>Success Notification</p></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. All records that get fetched will be in order by "ASC nFORCE\_\_lookupKey\_\_c." Nevertheless, if "nFORCE\_\_lookupKey\_\_c" is unavailable, then using order by "ASC Id," the records will be fetched.
2. For the **Attachment** object, the filter cannot be applied.
{% endhint %}

You can also use the **Query Editor** to execute an SOQL query on the selected Source Org. Results are displayed in a **Query Results** grid.

<figure><img src="../../../../../.gitbook/assets/image (1310).png" alt=""><figcaption><p>Query Editor</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1311).png" alt="" width="563"><figcaption><p>Query Results</p></figcaption></figure>

Similar steps are to be followed for objects in other buckets as well.

<figure><img src="../../../../../.gitbook/assets/image (1312).png" alt=""><figcaption><p>Selecting Additional Objects</p></figcaption></figure>

Once done, click **Next** to proceed to the **Preview and Save** screen.

{% hint style="info" %}
**Important Note:**

1. If your nCino objects include an Attachment object, users must confirm whether they want to fetch the Attachment dataset.
2. Check the number of attachments pulled for the job once the attachment object is selected for the data deployment. For each API call, Salesforce returns at least one and a maximum of five attachments based on the size of the attachments. More APIs calls will get triggered for more attachments, which may result in the APIs limit being exceeded and the application reporting an error.
{% endhint %}

#### Preview and Save <a href="#preview-and-save" id="preview-and-save"></a>

This is the summary page for the Feature Migration template you're about to create. You can view the features details, and filters you have applied for the last time before the template is created. Any change log information that needs to be added can be mentioned in the **Change Log** box.

<figure><img src="../../../../../.gitbook/assets/image (1313).png" alt="" width="563"><figcaption><p>Summary Page</p></figcaption></figure>

{% hint style="info" %}
**Important Note:** **Related List** section will display only if the **Attachment** object is part of the Feature Migration Template.&#x20;
{% endhint %}

Click **Save,** and you will be redirected to the [Feature Migration Summary](feature-migration-summary-page.md) screen, where you can track your template recently created.
