---
description: >-
  Each AWS account is onboarded as an organisation with the source AWS. The
  regions you govern become the organisation's environments.
---

# Onboard an AWS Account

{% hint style="info" %}


* Create the IAM access key before onboarding - [IAM Access Key](iam-access-key.md)
* A tenant can onboard any number of AWS accounts. Each account gets its own organisation and its own environments
{% endhint %}

#### Onboard the account <a href="#onboard-the-account" id="onboard-the-account"></a>

1. Navigate to main menu **`Organization`** -> **`My Organizations`** and click on **`Onboard Organization`**
2. Enter the following details -
   1. **`Organization Name`** - A name for the account in IZ Suite, for example `Payments Production`
   2. **`Source`** - Select **`AWS`**
   3. **`AWS Account ID`** - The 12-digit AWS account id
   4. **`Access Key ID`** - The access key id of the IAM user
   5. **`Secret Access Key`** - The secret access key of the IAM user
   6. **`Regions`** - Optional. Comma-separated list of the regions to govern, for example `eu-west-2,us-east-1`
3. Click on **`OK`** to onboard the organisation

The secret access key is encrypted at rest and is always shown masked after it is saved.

#### Environments <a href="#environments" id="environments"></a>

The **`AWS Sync`** job turns the organisation into environments - see [Schedule Configuration](schedule-configuration.md). On each run, for every AWS organisation, it:

1. Checks that the access key belongs to the entered **`AWS Account ID`**. If it does not, the account is not synced and the job log says why.
2. Creates one environment per region:
   * When **`Regions`** is filled in, exactly those regions are used.
   * When **`Regions`** is left blank, IZ Suite checks every region enabled on the account and keeps only the regions that contain at least one supported resource.
3. Creates a **`global`** environment for resources that do not belong to a region. CloudFront distributions are listed under **`global`**.
4. Grants the organisation's administrator roles the AWS permissions, so the AWS menus and applications are visible straight away.

An organisation without a secret access key is skipped by the sync and reported in the job log, so an account can be created before its credential is ready.

To view the environments, navigate to **`Organization`** -> **`My Organizations`** and click on **`View Environments`** for the AWS organisation.

#### Edit or rotate the credential <a href="#edit-or-rotate-the-credential" id="edit-or-rotate-the-credential"></a>

The credential can be corrected or rotated without onboarding the account again.

1. Navigate to **`Organization`** -> **`My Organizations`**
2. Open the actions of the AWS organisation and click on **`Edit Organization`**
3. The **`AWS Account ID`**, **`Access Key ID`** and **`Regions`** are shown as saved, and **`Secret Access Key`** is shown masked
4. Enter the new values:
   * To rotate the key, enter both the new **`Access Key ID`** and the new **`Secret Access Key`**
   * To keep the stored secret, leave the masked value unchanged
5. Save the organisation. The next run of the **`AWS Sync`** job uses the new values; regions added to **`Regions`** become new environments.



{% hint style="warning" %}
The **`Source`** of an organisation cannot be changed after it is onboarded.
{% endhint %}
