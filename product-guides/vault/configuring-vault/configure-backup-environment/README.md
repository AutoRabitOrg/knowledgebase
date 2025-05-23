# Configure Backup Environment

### Overview <a href="#overview" id="overview"></a>

The administrator must first set up the vault environment before working on backup/restore or other Vault features. This helps you to create a backup of the data/metadata in the storage environment and restore it if necessary. Vault supports a variety of environments, including Amazon AWS, Google Cloud Platform, Azure Blob, and Vault's default hosted environment.

### Where can I find the option to configure the Vault storage environment? <a href="#where-can-i-find-the-option-to-configure-the-vault-storage-environment" id="where-can-i-find-the-option-to-configure-the-vault-storage-environment"></a>

You can configure the storage environment under the **Settings > Backup Environment** tab.

### How to configure Vault Environment? <a href="#how-to-configure-vault-environment" id="how-to-configure-vault-environment"></a>

1. Log in to your **Vault** account.
2. Go to the **Settings** module and click on the **Backup Environment** tab.
3. Under **Storage Environment**, select the **Storage Type** from the drop-down. As of now, Vault supports the following storage types:
   * [Amazon AWS S3 Storage](amazon-aws-s3-storage-environment/)
   * [NFS](broken-reference)
   * [Azure Blob](azure-blob-storage-environment.md)
   * [GCP (Google Cloud Platform)](google-cloud-platform.md), and&#x20;
   * [SAN (Storage Area Network) environments](broken-reference).
