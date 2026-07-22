# Create an Azure Storage Account

An Azure storage account contains all your Azure Storage data objects—blobs, files, queues, and tables. It provides a globally accessible namespace for your data over HTTP or HTTPS.

{% hint style="info" %}
**Note:** If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/) before proceeding.
{% endhint %}

## Steps to Create a Storage Account

1. Go to the [Azure Portal](https://login.microsoftonline.com/).
2. From the left menu, select **Storage accounts**, or use the search bar to find it.

<figure><img src="../../../../.gitbook/assets/image (107) (1).png" alt="Accessing Storage Accounts in Azure portal" width="563"><figcaption><p>Accessing Storage Accounts</p></figcaption></figure>

3. On the **Storage accounts** page, click **Create**.

<figure><img src="../../../../.gitbook/assets/image (108) (1).png" alt="Creating a new storage account in Azure"><figcaption><p>Create Storage Account</p></figcaption></figure>

4. Fill in the details across the following tabs:

### Basics

* Add **Storage account name**
* Select desired **Region**
* Choose **Performance** as **Standard**

<figure><img src="../../../../.gitbook/assets/image (110) (1).png" alt="Basics tab in storage account creation" width="563"><figcaption><p>Basics Tab</p></figcaption></figure>

### Advanced

* Enable **secure transfer for REST API**
* Enable **blob public access**
* Enable **storage account key access**

<figure><img src="../../../../.gitbook/assets/image (111) (1).png" alt="Advanced tab configuration" width="563"><figcaption><p>Advanced Settings</p></figcaption></figure>

### Networking

* Choose **Public Endpoints (all networks)**

<figure><img src="../../../../.gitbook/assets/image (112) (1).png" alt="Networking tab settings" width="563"><figcaption><p>Networking Configuration</p></figcaption></figure>

### Data Protection

* Enable **soft delete** for:
  * Blobs
  * Containers
  * File shares

<figure><img src="../../../../.gitbook/assets/image (113) (1).png" alt="Data protection options" width="563"><figcaption><p>Data Protection Settings</p></figcaption></figure>

### Tags

* Add **Name**, **Value**, and **Resource** for organization

<figure><img src="../../../../.gitbook/assets/image (114) (1).png" alt="Tag configuration screen" width="563"><figcaption><p>Tag Setup</p></figcaption></figure>

### Review + Create

* If validation passes, click **Create**
* If validation fails, follow prompts to correct errors

<figure><img src="../../../../.gitbook/assets/image (115) (1).png" alt="Review and create tab" width="563"><figcaption><p>Validation and Final Review</p></figcaption></figure>

5. After validation, click **Create**.

<figure><img src="../../../../.gitbook/assets/image (116) (1).png" alt="Final step to create account" width="563"><figcaption><p>Create Storage Account</p></figcaption></figure>

6. Your Azure storage account is now created.

## Post-Creation: Get Access Keys

1. Navigate to the new **Storage account**.
2. From the left panel, select **Access keys**.
3. Click **Unhide keys**.
4. Copy the **Storage account name** and **Access keys (Key1 & Key2)**.
   * You can regenerate keys if needed.

<figure><img src="../../../../.gitbook/assets/image (117) (1).png" alt="Accessing storage account keys" width="563"><figcaption><p>Access Keys for Storage Account</p></figcaption></figure>
