# SSO with Microsoft Entra ID for Vault

## Overview <a href="#overview" id="overview"></a>

This guide details how to configure **Single Sign-On (SSO)** in Vault using **Microsoft Entra ID** (formerly Azure AD) as a **SAML 2.0 Identity Provider**.

Benefits:

* Centralized access control via Entra ID
* Seamless user authentication into Vault
* Simplified account management from the Azure portal

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* An active **Entra ID** subscription
* Admin privileges in both Vault and Entra ID
* Vault added as a **non-gallery application**

## Configure Entra ID <a href="#in-azure-a-d" id="in-azure-a-d"></a>

### Steps:

1. Sign in to [Azure Portal](https://portal.azure.com).
2. Go to **Entra ID > Enterprise Applications > New Application**
3. Click **+ Create your own application**
4. Name it `VAULT`, select **Non-gallery application**, and click **Create**

<figure><img src="../../../../.gitbook/assets/image (181).png" alt="Create non-gallery application in Azure"><figcaption></figcaption></figure>

5. After creation, click **Set up single sign on** > **SAML**
6. In **Basic SAML Configuration**:
   * **Identifier (Entity ID):** `<instanceURL>/ARVault/saml/metadata`
   * **Reply URL:** `<instanceURL>/ARVault/saml/SSO`

<figure><img src="../../../../.gitbook/assets/image (185).png" alt="Basic SAML Configuration" width="527"><figcaption></figcaption></figure>

7. In **User Attributes & Claims**:
   * Delete all **Additional claims**
   * Add these claims manually:

| Name                       | Source    | Source Attribute                                     |
| -------------------------- | --------- | ---------------------------------------------------- |
| firstname                  | Attribute | `user.givenname`                                     |
| lastname                   | Attribute | `user.surname`                                       |
| customerid                 | Attribute | Vault Customer ID (from your Vault Profile section)  |
| restrictAutoCreationOfUser | Attribute | `Yes` or `No` (controls auto user creation in Vault) |

<figure><img src="../../../../.gitbook/assets/image (190).png" alt="Claims configuration"><figcaption></figcaption></figure>

8. In **SAML Signing Certificate**, download the **Federation Metadata XML**

<figure><img src="../../../../.gitbook/assets/image (191).png" alt="Download SAML Metadata"><figcaption></figcaption></figure>

## Configure Vault <a href="#in-vault" id="in-vault"></a>

1. Log in to Vault
2. Navigate to **Settings > SSO Configurations**
3. Enter your Azure username
4. Choose **Metadata File**, upload the XML file from Azure
5. Click **Update** and then **Activate**

<figure><img src="../../../../.gitbook/assets/image (192).png" alt="Upload metadata in Vault"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (193).png" alt="Activate SSO in Vault"><figcaption></figcaption></figure>

6. Sign out and test login via SSO:
   * On the login page, click **Login with SSO**
   * Enter your **Customer ID** and click **Sign In**

<figure><img src="../../../../.gitbook/assets/image (194).png" alt="SSO Login screen" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (195).png" alt="Customer ID prompt" width="563"><figcaption></figcaption></figure>

## Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

**Error**:\
&#xNAN;_"Your user is not available in the account with provided customer ID. Please contact the administrator to create a user for you in the account."_

**Causes**:

1. User not assigned in Azure to the Vault app
2. `restrictAutoCreationOfUser` claim is set to `Yes` and user not pre-created in Vault
