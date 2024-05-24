# Create a Azure Storage Account

An Azure storage account contains all of your Azure Storage data objects: blobs, files, queues, and tables. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS.

{% hint style="info" %}
**Note:** If you don't have an Azure subscription, please create a [free account](https://azure.microsoft.com/) before you begin.
{% endhint %}

To create an Azure storage account with the Azure portal, follow the steps below:

1. Log in to the Azure portal at, [https://login.microsoftonline.com/](https://login.microsoftonline.com/)
2. From the left portal menu, select **Storage accounts** (or) use the search box to find storage accounts.

<figure><img src="../../../../.gitbook/assets/image (107) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. On the Storage accounts page, select **Create**.

<figure><img src="../../../../.gitbook/assets/image (109) (1).png" alt=""><figcaption></figcaption></figure>

4. On the **Create a storage account page**, the options for your new storage account are now organized into tabs. Fill out the required information in the following tabs to create a new storage account in Azure.
   * **Basics**: On the Basics tab, provide the essential information for your storage account. After you complete the Basics tab, you can choose to further customize your new storage account by setting options on the other tabs, or you can select Review + create to accept the default options and proceed to validate and create the account.
     * Add the **Storage account name**
     * Select the desired **Region**
     * Select the **Performance** as **Standard**

<figure><img src="../../../../.gitbook/assets/image (110) (1).png" alt="" width="563"><figcaption></figcaption></figure>

*   **Advanced**: On the Advanced tab, you can configure additional options and modify default settings for your new storage account.

    * Select, **Require secure transfer for REST API operations**
    * Select, **Enable blob public access**
    * Select, **Enable storage account key access**

    <figure><img src="../../../../.gitbook/assets/image (111) (1).png" alt="" width="563"><figcaption></figcaption></figure>
*   **Networking**: On the Networking tab, you can configure network connectivity and routing preference settings for your new storage account.

    * Select, **Public Endpoints (all networks)** as connectivity method

    <figure><img src="../../../../.gitbook/assets/image (112) (1).png" alt="" width="563"><figcaption></figcaption></figure>
*   **Data protection**: On the Data Protection tab, you can configure data protection options for blob data in your new storage account.

    * Select, **Enable soft delete for blobs**
    * Select, **Enable soft delete for containers**
    * Select, **Enable soft delete for file shares**

    <figure><img src="../../../../.gitbook/assets/image (113) (1).png" alt="" width="563"><figcaption></figcaption></figure>
*   **Tags**: On the Tags tab, you can specify Resource Manager tags to help organize your [Azure](https://knowledgebase.autorabit.com/docs/azure-devops) resources.

    * Add, **Name**, **Value**, and **Resource** for your tag

    <figure><img src="../../../../.gitbook/assets/image (114) (1).png" alt="" width="563"><figcaption></figcaption></figure>
*   **Review + create**: When you navigate to the Review + create tab, Azure runs validation on the storage account settings that you have chosen.

    * **If validation passes**, you can proceed to create the storage account.
    * **If validation fails**, then the portal indicates which settings need to be modified.

    <figure><img src="../../../../.gitbook/assets/image (115) (1).png" alt="" width="563"><figcaption></figcaption></figure>

5. Once the validation passed, click on the **Create** button at the bottom.

<figure><img src="../../../../.gitbook/assets/image (116) (1).png" alt="" width="563"><figcaption></figcaption></figure>

6. Your **Azure storage account** is now ready to use.
7.  Now, go to the newly created Azure storage account and do the following steps:

    * Click on the **Access keys** on the left navigation menu.
    * Click on **unhide keys** at the top left.
    * Copy the **Storage account name** and the **Access keys (1&2)**
    * If necessary, the keys can be changed.

    <figure><img src="../../../../.gitbook/assets/image (117) (1).png" alt="" width="563"><figcaption></figcaption></figure>
