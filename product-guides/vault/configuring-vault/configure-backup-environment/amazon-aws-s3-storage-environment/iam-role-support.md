# IAM Role Support

Point to Note:

* This article is applicable for enterprise users (dedicated/on-premise) only.
* Not applicable for shared instances users.

### Introduction <a href="#introduction" id="introduction"></a>

To use AWS S3 as your storage environment to backup your metadata and data objects, you will need to configure in the Vault application first. To configure, you will need to add the below details in Vault:

* _AWS S3 bucket name_
* _Access Key_
* _Secret Key_
* _AWS region_

Taking things further, we've implemented support for IAM role in our latest release. This will allow IAM users to connect to S3 bucket without need to input **access key** and **secret keys** in our Vault application.

### About IAM Role <a href="#about-iam-role" id="about-iam-role"></a>

Amazon's authentication system is incredibly flexible. That is, in addition to standard cloud credentials, Amazon allows users to create IAM roles. An IAM role, like a user, is an AWS identity with authorization policies that define what the identity can and cannot do in AWS.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* AWS Account with S3 buckets.
* IAM user with IAM role permissions. For more information on how to create IAM roles, refer to the article [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_create.html).

### Configuring in Vault <a href="#configuring-in-vault" id="configuring-in-vault"></a>

1. Once you logged into your Vault account, go to **Settings > Backup Environment**.
2. Select **AWS S3** as your **Storage Type**.
3. Provide a **label** of your choice (Need not be the same as your S3 Bucket name).
4. Select the **Role-based control for dedicated/On-Prem Instance** checkbox.

<figure><img src="../../../../../.gitbook/assets/image (99).png" alt="" width="377"><figcaption></figcaption></figure>

5. You will need to enter the name of your s3 bucket in the **Bucket Name** field.
6. Choose the default encryption method i.e., **AES-256** or **AWS-KMS**.
7. Click **Save Settings**.
