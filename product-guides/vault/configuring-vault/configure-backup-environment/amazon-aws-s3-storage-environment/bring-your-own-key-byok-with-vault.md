# Bring your own Key (BYOK) with AutoRABIT Vault

## **Overview** <a href="#overview" id="overview"></a>

Using AutoRABIT Vault, you can implement **Bring Your Own Key (BYOK)** by importing encryption keys from **Amazon Web Services Key Management Service (AWS KMS)**. This feature is ideal for customers who want enhanced control over their encryption process — particularly for meeting internal security policies and regulatory requirements.

BYOK allows you to:

* Maintain ownership and lifecycle control over encryption keys.
* Leverage AWS KMS for encryption but retain exclusive control over key material.
* Enforce data sovereignty by managing keys independently of data storage.

## **Before You Begin** <a href="#before-you-begin" id="before-you-begin"></a>

Before configuring BYOK in AutoRABIT Vault, you must create a **Customer Master Key (CMK)** in your AWS account.

### Steps to create an AWS KMS CMK:

1. Log in to your [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to **Key Management Service (KMS)**.
3. Click **Create a Key** and follow the wizard to generate your CMK.
4. For detailed guidance, refer to the AWS documentation:\
   [Getting Started with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)

***

## **Using Key to Configure AWS-KMS in** AutoRABIT Vault <a href="#using-key-to-configure-awskms-in-vault" id="using-key-to-configure-awskms-in-vault"></a>

To use the key within AutoRABIT Vault:

1. Log in to your **AutoRABIT Vault** account.
2. Go to **Settings > Backup Environment**.
3. Under **Storage Environment**, select **AWS S3** as the storage type.
4. Choose the **Region** — this must match the region used during key creation in AWS KMS.
5. Enable the checkbox: **Automatically Encrypt data stored in AutoRABIT Vault.**
6. Select **AWS-KMS** as the encryption method.
7. Enter your **Master Key** (CMK ARN) from AWS KMS.
8. Enable the checkbox for **AR Vault Hosted Backup Environment**.
9. Click **Save Settings**.

<figure><img src="../../../../../.gitbook/assets/image (97) (1).png" alt="Vault BYOK AWS-KMS Configuration Screen" width="563"><figcaption><p>Vault configuration for AWS-KMS BYOK setup</p></figcaption></figure>
