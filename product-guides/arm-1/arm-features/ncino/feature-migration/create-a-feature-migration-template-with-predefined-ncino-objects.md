# Create a Feature Migration Template with Predefined nCino Objects

## Overview <a href="#overview" id="overview"></a>

This article deals with the step-by-step procedure to create a standard/community template by picking a feature with nCino predefined objects.

## What is a Feature Migration Template?&#x20;

A Feature Migration Template in AutoRABIT is essentially a blueprint that helps you manage and automate the process of moving features from one environment to another. It’s like a checklist that defines exactly what should be moved, how it should be transferred, and in what order — ensuring everything gets to the new environment correctly, without missing any critical steps.&#x20;

The template saves time and effort by letting you set up migration rules once and use them repeatedly for consistent, error-free deployments. Whether you're moving configurations, customizations, or entire features, the template streamlines the whole process, making it much smoother and more predictable.&#x20;

## Standard vs Community Templates&#x20;

**Standard Feature Templates**: These are templates that are pre-defined and ready to be used by customers/partners. Such templates are updated regularly as nCino releases changes to any configurations. AutoRABIT provides several default templates to be directly used by our community for migrating Record-Based Configurations (RBCs). &#x20;

**Community Feature Templates**: Community templates are non-standard templates. In other words, users can define their own migration templates that are not already published by AutoRABIT. Community templates are useful if there are any customizations in nCino users want to migrate that are not listed as part of the default Standard templates. &#x20;

Community templates, just like the Standard ones, are designed to be long-lasting. They need to be created once, and then can be used multiple times as a template.&#x20;

## Procedure <a href="#procedure" id="procedure"></a>

1. Hover your mouse over the **`nCino`** module and click on the option: **`Feature Management`.**

<figure><img src="../../../../../.gitbook/assets/image (1314).png" alt="" width="239"><figcaption><p>Feature Management</p></figcaption></figure>

2. Click on **`New Feature Migration Template`** button.

<figure><img src="../../../../../.gitbook/assets/image (1315).png" alt=""><figcaption><p>New Feature Migration Template</p></figcaption></figure>

3. Choose one of the features from the list. _**For example,**_ select the **`Spreads Schedule Template`** tile to include the **Spreads Schedules** feature predefined objects in a template.

<figure><img src="../../../../../.gitbook/assets/image (1316).png" alt=""><figcaption><p>Create New Feature Migration</p></figcaption></figure>

4. You'll be directed to the **`Record Based Configuration`** section, where you will find _three tabs_ that you'll need to fill out to proceed:
   * _Metadata Configuration_
   * _Record Configuration_
   * _Preview and Save_

### Metadata Configuration <a href="#metadata-configuration" id="metadata-configuration"></a>

Metadata in the context of nCino is the same as that of Salesforce. It includes a collection of nCino customizations and configurations that together form a blueprint for your lending processes, e.g., Page Layout, Custom Field, Workflows and Automation.

Under the **`Feature Details`** section, enter the following details:

1. **`Name:`** Provide a feature migration template name.
2. **`Associated Partner:`** The default associate partner would be nCino, which you can change if necessary.
3. **`Version:`** Enter the version number here. If you're creating the feature template for the first time, it is recommended to keep the version number as **1.0**.

<figure><img src="../../../../../.gitbook/assets/image (1317).png" alt=""><figcaption><p>Feature Details</p></figcaption></figure>

Under the **`Salesforce Org Details`** section, do the following:

4. Choose your **`Salesforce Org`**.
5. Click **`Fetch Objects`** to retrieve all available objects in the selected source org. Predefined objects will be auto chosen based on your selected feature. By default, only nCino objects available in the source org will get auto-populated. To view all the objects available, click on **`Show All`** objects.
6. Using![](<../../../../../.gitbook/assets/image (1298).png>)/![](<../../../../../.gitbook/assets/image (1299).png>)button, you can select/deselect all the objects for your template. Or, use the **Ctrl** key and select multiple objects of your choice and move them to the selected tab using![](<../../../../../.gitbook/assets/image (1300).png>)/![](<../../../../../.gitbook/assets/image (1301).png>)button. Once you have selected the object, ARM will retrieve the fields included in that object behind the scenes.

<figure><img src="../../../../../.gitbook/assets/image (1318).png" alt=""><figcaption><p>Fetch Objects</p></figcaption></figure>

7. Click **`Next`** to go to the **`Record Configuration`** tab.

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

<figure><img src="../../../../../.gitbook/assets/image (1319).png" alt="" width="250"><figcaption><p>List Selections</p></figcaption></figure>

Based on the object's relationship, the AutoRABIT application will segregate the object sets, and applying a filter on each bucket is mandatory. By default, AutoRABIT will denote an object in a bucket as an entry point, which can be applied as a filter. This is not mandatory, but as a best practice, AutoRABIT recommends applying filters to the entry point object rather than any other object.

The entry object is selected by default, and the user can apply a filter. The entry object is denoted by **`“E”`**.

<figure><img src="../../../../../.gitbook/assets/image (1320).png" alt=""><figcaption><p>Selection</p></figcaption></figure>

**Applying the Filters**

Apply the filter(s) using the steps as shown below:

<figure><img src="../../../../../.gitbook/assets/image (1321).png" alt=""><figcaption><p>Query Selections</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1322).png" alt=""><figcaption><p>Add Dates</p></figcaption></figure>

Click **`Add`**. The filter query gets added and gets displayed in the filter box. You can edit the query if any modification is required. Nevertheless, multiple queries can be added based on your requirement. **`Validate`** your query to see if the query entered is stable or not. Additionally, you'll be able to view several records that will get fetched.

<figure><img src="../../../../../.gitbook/assets/image (1323).png" alt=""><figcaption><p>Validate Query</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1324).png" alt=""><figcaption><p>Success Notification</p></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. All records that get fetched will be in order by **"ASC nFORCE\_\_lookupKey\_\_c."** Nevertheless, if **"nFORCE\_\_lookupKey\_\_c"** is unavailable, then using order by **"ASC Id,"** the records will be fetched.
2. For the **Attachment** object, the filter cannot be applied.
{% endhint %}

You can also use the **`Query Editor`** to execute an SOQL query on the selected source org. Results are displayed in a **`Query Results`** grid.

<figure><img src="../../../../../.gitbook/assets/image (1325).png" alt=""><figcaption><p>Query Editor</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1326).png" alt="" width="563"><figcaption><p>Execute Query</p></figcaption></figure>

Similar steps are to be followed for objects in other buckets as well. Once done, click **`Next`** to proceed to the **`Preview and Save`** screen.

{% hint style="info" %}
**Important Note:**

1. If your nCino objects include an **Attachment** object, the users must confirm whether they want to fetch the **Attachment** dataset.
2. Please check the number of attachments pulled for the job once the attachment object is selected as part of the data deployment. For each API call, Salesforce returns at least one and a maximum of five attachments based on the size of the attachments. For more attachments, more APIs call will get triggered, which may result in the APIs limit exceeding and the application to throw an error.&#x20;
{% endhint %}

#### Preview and Save <a href="#preview-and-save" id="preview-and-save"></a>

This is the summary page for the feature migration template you're about to create. You can view the features details, and filters you have applied for the last time before the template is created. Any change log information that needs to be added can be mentioned in the **`Change Log`** box.

<figure><img src="../../../../../.gitbook/assets/image (1327).png" alt=""><figcaption><p>Summary Page</p></figcaption></figure>

{% hint style="info" %}
**Important Note:`Related List`** section will display only if the **`Attachment`** object is a part of the Feature Migration Template.&#x20;
{% endhint %}

Click **`Save,`** and you will be redirected to the [Feature Migration Summary](../../../../arm/arm-features/ncino/feature-migration/feature-migration-summary-page.md) screen, where you can track your recently created template .
