# IAM Role Support

{% hint style="info" %}
**Points to Note:**

1. This article is applicable for enterprise users (dedicated/on-premises) only.
2. Not applicable for shared instance users.
{% endhint %}

## Introduction <a href="#introduction" id="introduction"></a>

Vault supports AWS S3 as a storage environment to back up your metadata and data objects. Traditionally, users had to provide:

* AWS S3 Bucket Name
* Access Key
* Secret Key
* AWS Region

However, Vault now supports **IAM Roles**, allowing users to connect to S3 buckets **without manually entering access or secret keys**.

***

## About IAM Role <a href="#about-iam-role" id="about-iam-role"></a>

An **IAM Role** in AWS is an identity with specific permissions policies. Unlike IAM users, roles do not require long-term credentials and are used to delegate access securely.

IAM Roles are ideal for:

* Temporary credentials
* Access control delegation
* Enhanced security practices

For more information, refer to [AWS IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html).

***

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To configure IAM Role support in Vault:

* An active AWS account with access to S3 buckets
* An IAM user with permissions to assume roles and access S3

***

## Configuring in Vault <a href="#configuring-in-vault" id="configuring-in-vault"></a>

1. Log in to your **Vault** account.
2. Navigate to **Settings > Backup Environment**.
3. Set **Storage Type** to **AWS S3**.
4. Enter a **Label Name** (this is a user-defined reference name).
5. Enable the checkbox:\
   &#xNAN;**"Role-based control for dedicated/On-Prem Instance"**

<figure><img src="../../../../../.gitbook/assets/image (99) (1).png" alt="IAM Role configuration in Vault settings" width="377"><figcaption><p>Selecting IAM role option for S3 access</p></figcaption></figure>

6. Enter the **S3 Bucket Name** in the corresponding field.
7. Select an **encryption method**: either **AES-256** or **AWS-KMS**.
8. Click **Save Settings** to complete the configuration.
