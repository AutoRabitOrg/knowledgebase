---
hidden: true
---

# \[DRAFT - Project - X] Create a Feature Migration Template

### Overview <a href="#overview" id="overview"></a>

This details the step-by-step process to create a standard/community nCino migration template.

### Step-By-Step Guide <a href="#procedure" id="procedure"></a>

1. The **“New Feature Migration”** template can be created through either of the highlighted options
   * Feature
   * Feature Management
2. Click on the “Feature” option under the "Create” drop-down to initiate a new feature migration template creation

<figure><img src="../../../../../.gitbook/assets/image (1639).png" alt=""><figcaption></figcaption></figure>

3. Click on the “Feature Management” section under the “NCINO” section to navigate to it.
4. Click on the “Create feature” button on the “Feature Management” screen

<figure><img src="../../../../../.gitbook/assets/image (1638).png" alt=""><figcaption></figcaption></figure>

5. Once the selection is made, the creation of the “Feature Migration Template” will be initiated by landing on the Feature page.
6. You'll be taken to the record-based configuration section, where you will find three tabs that need completed to proceed ahead:
   * **Metadata Configuration**
   * **Record Configuration and**
   * **Preview and Save**

#### Metadata Configuration <a href="#metadata-configuration" id="metadata-configuration"></a>

The following screen should be visible on clicking the "Feature" or the "Create Feature" option.

<figure><img src="../../../../../.gitbook/assets/image (1643).png" alt=""><figcaption></figcaption></figure>

Under **Feature Details**, enter the items below:

1. **Name:** Provide a feature migration template name.
2. **Associated Partner:** The default associate partner would be nCino, which you can change if necessary.
3. **Version:** Enter the version number here. If you're creating the feature template for the first time, it is recommended to keep the version number as 1.0.

Under the **Salesforce Org** **Details** section, do the following:

4. Select the required “Source ORG”
5. On selecting the required “Source ORG”, the related objects will be fetched automatically.
6. By default, only nCino objects available in the Source Org will be auto-populated. To view all the objects available, click on **Show All** **Objects**.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (1641).png" alt=""><figcaption></figcaption></figure>

4. Click on **Next** to go to the **Record Configuration** Tab.

{% hint style="info" %}
**Important Note:** Only those objects will be considered nCino objects if their related prefix is included in the **Plugins** section under the [**My Account**](../../../../arm/arm-administration/user-management/manage-users-account-settings.md) page.
{% endhint %}

#### &#x20;Record Configuration <a href="#record-configuration" id="record-configuration"></a>

1. The filters can be applied on the entry objects under this tab
2. The following can be observed under this tab:
   * The “Selected Objects” were displayed under the “Object Bucket List” with the columns “Entry Object”, “Object name” & “Query”
   * Bucket Exclusion Objects: Objects selected here will be excluded from further processing
   * Bucket Mandatory Objects: Objects displayed under this section are mandatory

<div align="right"><figure><img src="../../../../../.gitbook/assets/image (1644).png" alt=""><figcaption></figcaption></figure></div>

3. Based on the relationship between the objects, the AutoRABIT application will segregate the object sets, and applying a filter to each bucket is mandatory. By default, AutoRABIT will denote an object in a bucket as an entry point, which can be applied filter. This is not mandatory, but as a best practice, AutoRABIT recommends applying filters to the entry point object rather than any other object.

**Applying the Filters**

The filter criteria can be entered and the query can be built under this tab.

1. Click on the pencil icon beside the query

<figure><img src="../../../../../.gitbook/assets/image (1647).png" alt=""><figcaption></figcaption></figure>

2. On clicking the pencil icon, the ‘query builder’ will be opened

<figure><img src="../../../../../.gitbook/assets/image (1648).png" alt=""><figcaption></figcaption></figure>

3. Clicking on the ‘field’ drop-down will provide the list of fields from the ORG

<figure><img src="../../../../../.gitbook/assets/image (1649).png" alt=""><figcaption></figcaption></figure>

4. Clicking on the operator drop-down field the available list of operators can be observed

<figure><img src="../../../../../.gitbook/assets/image (1651).png" alt=""><figcaption></figcaption></figure>

5. On completing the field selection, click on the ‘ADD’ icon to add the query to the ‘query editor’ below

<figure><img src="../../../../../.gitbook/assets/image (1652).png" alt=""><figcaption></figcaption></figure>

6. Once the query is been added to the query editor, the query can be validated by clicking on the ‘Validate’ button.
7. An SOQL query can also be added to the query editor. After adding the query, the query can be validated

<figure><img src="../../../../../.gitbook/assets/image (1653).png" alt=""><figcaption></figcaption></figure>

8. On validating the query, the application will display a success message

<figure><img src="../../../../../.gitbook/assets/image (1654).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Important Note:

1. All records that get fetched will be in order by "ASC nFORCE\_\_lookupKey\_\_c." Nevertheless, if "nFORCE\_\_lookupKey\_\_c" is unavailable, then using order by "ASC Id," the records will be fetched.
2. For the Attachment object, the filter cannot be applied.
{% endhint %}

9. As the query has been validated, the same query can be saved by clicking on the ‘Save’ button on the ‘Query Builder’.

{% hint style="info" %}
**Important Note:**

1. &#x20;If your nCino objects include an Attachment object, users must confirm whether they want to fetch the Attachment dataset.
2. Check the number of attachments pulled for the job once the attachment object is selected for the data deployment. For each API call, Salesforce returns at least one and a maximum of five attachments based on the size of the attachments. More APIs calls will get triggered for more attachments, which may result in the APIs limit being exceeded and the application reporting an error.
{% endhint %}

11. The query should be added to all the buckets. Click on the Next to continue to the “Preview and Save” step of the “Feature Migration Creation”

#### Preview and Save <a href="#preview-and-save" id="preview-and-save"></a>

This is the summary of the “Feature Migration Template” that is being created. All of the feature details can be observed on the ‘preview and save’ page. On the ‘change log’, any change log information required can be added.

<figure><img src="../../../../../.gitbook/assets/image (1655).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** **Related List** section will display only if the **Attachment** object is part of the Feature Migration Template.&#x20;
{% endhint %}

1. On verifying all the details on the ‘preview and save’ page, save the template by clicking on the save button.
2. On clicking the save, you will be re-directed to the “Feature Management” page.

<figure><img src="../../../../../.gitbook/assets/image (1656).png" alt=""><figcaption></figcaption></figure>

&#x20;

&#x20;
