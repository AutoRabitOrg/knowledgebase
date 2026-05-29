# Configuring Bitbucket Token Authentication and Email Support

### Introduction

Bitbucket is deprecating App Password authentication effective **June 9, 2026**. To ensure uninterrupted connectivity and support for Bitbucket API operations, AutoRABIT supports Token-based authentication and provides an Email Address field for Bitbucket credentials.

This guide explains how to configure and update Bitbucket credentials in AutoRABIT.

***

### Prerequisites

Before proceeding, ensure that:

* You have access to your Bitbucket account.
* A Bitbucket App Token has been generated.
* You know the email address associated with your Bitbucket account.

***

### When Is an Email Address Required?

An email address is required for Bitbucket API-based operations such as:

* Pull Request Creation
* Other Bitbucket REST API operations

The email address is not required for Git operations such as:

* Clone
* Fetch
* Push

***

### Configuring a New Bitbucket Credential

#### New UI

1. Navigate to **Settings → Credentials**.
2. Click **Create Credential**.
3. Select **Bitbucket** as the repository type.
4. Enter the following information:
   * Username
   * Token
   * Email Address (Optional)
5. Click **Save**.

<figure><img src="../../../../../../.gitbook/assets/image (2518).png" alt=""><figcaption></figcaption></figure>



### Updating an Existing Bitbucket Credential

1. Navigate to **Settings → Credentials**.
2. Locate the Bitbucket credential.
3. Click **Edit**.
4. Enter or update the **Email Address** field.
5. Save the changes.

<figure><img src="../../../../../../.gitbook/assets/image (2520).png" alt="" width="375"><figcaption></figcaption></figure>

***

### Repository Registration

When registering a Bitbucket repository:

1. Select the Bitbucket credential.
2. Verify that the credential contains:
   * Username
   * Token
   * Email Address (recommended)
3. Complete repository registration.

***

### Updating Version Control Mappings (New UI)

1. Navigate to **My Profile → Version Control Mappings**.
2. Select the Bitbucket credential.
3. Verify the Email Address is configured.
4. Save the mapping.

<figure><img src="../../../../../../.gitbook/assets/image (2521).png" alt=""><figcaption></figcaption></figure>

***



### Best Practices

* Migrate from App Passwords to Tokens before June 9, 2026.
* Configure an Email Address for all Bitbucket credentials used for Pull Request workflows.
* Periodically review and update repository credentials.

***

<br>
