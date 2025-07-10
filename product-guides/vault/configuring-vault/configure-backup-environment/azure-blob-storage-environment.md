# Azure Blob Storage Environment

### Customer-Hosted Storage Environment <a href="#customer-hosted-storage-environment" id="customer-hosted-storage-environment"></a>

To utilize Azure Blob as your storage medium for backing up metadata and data objects, follow these steps to configure it within the Vault application:

1. Navigate to the **Backup Environment** tab under the **Settings** module.
2. Select [**Azure Blob**](https://knowledgebase.autorabit.com/vault/docs/microsoft-azure-blob-retention-policy) as the **Storage Type**.
3. Enter a **Label Name** of your choice for easy identification.

4. **Naming Rules for Blob:**
   - Names can include any character combination.
   - Must be between 1 and 1,024 characters (256 for Azure Storage emulator).
   - Case-sensitive.
   - Reserved URL characters must be escaped properly.
   - Cannot exceed 254 path segments.
   - Avoid names ending with `.`, `/`, or their combinations.

5. Enter your Azure **Storage Account Name**. You can [create one here](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal).
6. Input your **Access Key** (either primary or secondary) for the selected storage account.
   - You are provided with two keys per account to enable rotation or delegated access.

<figure>
  <img src="../../../../.gitbook/assets/image (118) (1).png" alt="Azure Blob storage configuration screen in Vault" width="563">
  <figcaption>Azure Blob configuration in Vault</figcaption>
</figure>

7. Click **Save Settings** to complete the setup.

---

### Vault Hosted Backup Environment <a href="#vault-hosted-backup-environment" id="vault-hosted-backup-environment"></a>

To have AutoRABIT manage your backup environment:

- Contact the **AutoRABIT CloudOps** team to configure [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) as your default backup environment.
- Submit a support request [here](https://support.autorabit.com/portal/en/newticket?departmentId=241415000000006907&layoutId=241415000000074011).
