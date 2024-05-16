# Bring your own Key (BYOK) with Vault

### **Overview** <a href="#overview" id="overview"></a>

When you create a key, you might want to "bring your own key" (BYOK) if you need more control over the source of the key material or if you want to use the same keys that you already use for encryption purposes. Using [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/), you can bring your own encrypted keys from Amazon Web Services Key Management Services (AWS KMS).

You will be able to further protect your data by securely creating and managing your own encryption keys, separated from the AWS KMS provider where your sensitive data are being hosted.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

To bring your own key, you must first create an AWS KMS customer master key (CMK) from your AWS account. To do so,

1. Login to your AWS account.
2. Go to the **Key Management Service (KMS)**.
3. Click on **Create a Key** to create your own key.
4. For more information, refer to the article: [https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)

### Using Key to configure AWS-KMS in Vault <a href="#using-key-to-configure-awskms-in-vault" id="using-key-to-configure-awskms-in-vault"></a>

1. Log in to your Vault account.
2. Go to the **Settings** module and click on the **Backup Environment** tab.
3. Under **Storage Environment**, select the Storage Type as **AWS S3**.
4. Select the **Region**. Make sure the region in Vault matched the region selected in AWS KMS while creating the key.
5. Select the checkbox: **Automatically Encrypt data stored in Vault**.
6. Choose the second option i.e., **AWS-KMS**.
7. Enter the **Master Key** detail that you have created earlier.
8. Select the **AR Vault hosted backup environment** checkbox.
9. Click **Save** **Settings**.

<figure><img src="../../../../../.gitbook/assets/image (97).png" alt="" width="563"><figcaption></figcaption></figure>

***

\
