# Azure Blob Storage Environment

### Customer Hosted Storage Environment <a href="#customer-hosted-storage-environment" id="customer-hosted-storage-environment"></a>

To use Azure Blob as your storage environment to back up your metadata and data objects, you need to configure it in the Vault application first.

1. Head to the **Backup Environment** tab under the **Settings** module.
2. Select [**Azure Blob**](https://knowledgebase.autorabit.com/vault/docs/microsoft-azure-blob-retention-policy) as the Storage Type.
3. Enter the **Label Name** of your choice.&#x20;
4. **Naming Rules**: A blob name must conform to the following **naming rules**:&#x20;
   * A blob name can contain any combination of characters.&#x20;
   * A blob name must be at least one character long and cannot be more than 1,024 characters long, for blobs in Azure Storage.&#x20;
   * The Azure Storage emulator supports blob names up to 256 characters long.&#x20;
   * Blob names are case-sensitive.&#x20;
   * Reserved URL characters must be properly escaped.&#x20;
   * The number of path segments comprising the blob name cannot exceed 254. A path segment is a string between consecutive delimiter characters (e.g., the forward slash '/') that corresponds to the name of a virtual directory.&#x20;
   * Avoid blob names that end with a dot (.), a forward slash (/), or a sequence or combination of the two. No path segments should end with a dot (.).
5. Enter your Azure storage **Account Name**. To create a new storage account, refer to the following article: [Create Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json\&tabs=azure-portal).
6. Next, enter the **Access Key** for the above-selected storage account. For every storage account, you get two keys - **primary** and **secondary**. Specify either. You have two so you can give one out to someone (such as giving the secondary key to a third-party monitoring company) and revoke it by changing the key, without impacting you (assuming you're using the primary key for yourself).

<figure><img src="../../../../.gitbook/assets/image (118) (1).png" alt="" width="563"><figcaption></figcaption></figure>

6. Click on **Save Settings**.

### Vault Hosted Backup Environment <a href="#vault-hosted-backup-environment" id="vault-hosted-backup-environment"></a>

Reach out to the **AutoRABIT CloudOps** team to configure [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) as your default hosted backup environment. Submit a request [HERE](https://support.autorabit.com/portal/en/newticket?departmentId=241415000000006907\&layoutId=241415000000074011)
