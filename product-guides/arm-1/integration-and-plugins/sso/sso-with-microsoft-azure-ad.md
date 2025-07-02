---
description: How to configure Single Sign-On between AutoRABIT and Microsoft Entra ID
---

# SSO With Microsoft Entra ID

### Overview <a href="#overview" id="overview"></a>

This step-by-step guide shows you how to configure **Single Sign-On (SSO)** in AutoRABIT using **Microsoft Entra ID**—formerly Azure Active Directory (Azure AD)—as your **SAML 2.0 identity provider (IdP)**.

When you connect AutoRABIT to Entra ID, you can:

1. Control in Entra ID which users can access AutoRABIT.
2. Let users sign in to AutoRABIT automatically with their Entra ID credentials.
3. Manage all accounts centrally from the Azure portal.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you begin, make sure you have:

1. An active **Microsoft Entra ID** subscription.
2. **Administrator** permissions in both AutoRABIT and Entra ID.
3. AutoRABIT added to Entra ID as a **non-gallery application**.

***

## Configure SSO in Entra ID <a href="#in-azure-a-d" id="in-azure-a-d"></a>

1. Sign in to the **Microsoft Entra** admin center.
2. In the left pane, select **Entra ID ▸ Enterprise applications**.
3. Choose **All applications** from the **Application type** filter.
4. Click **New application**. In **Add from the gallery**, search for _autorabit_ and press **Enter**.
5. Select **AutoRABIT**, rename it if desired, then click **Add**.
6. Open the **AutoRABIT** app page and select **Single sign-on**.
7. In **Select a single sign-on method**, choose **SAML**.
8. On **Set up single sign-on with SAML**, click the **Edit** (pencil) icon in **Basic SAML Configuration**.
9.  Enter the following values and click **Save**:

    | Field                      | Value format                          | Example                         |
    | -------------------------- | ------------------------------------- | ------------------------------- |
    | **Identifier (Entity ID)** | `https://<instanceURL>/saml/metadata` | `https://xyz.com/saml/metadata` |
    | **Reply URL**              | `https://<instanceURL>/saml/SSO`      | `https://xyz.com/saml/SSO`      |
    | **Sign-on URL**            | `https://<instanceURL>`               | `https://xyz.com`               |
10. Under **SAML Signing Certificate**, click **Download** next to **Federation Metadata XML** and save the file locally.

***

## Complete the setup in AutoRABIT <a href="#in-autorabit" id="in-autorabit"></a>

1. Sign in to **AutoRABIT**.
2. From the navigation bar, hover over **Admin** and select **My Account**.
3. In **My Account**, scroll to **SSO Configuration**.
4. Upload the **metadata XML** file you downloaded from Entra ID.
5. Sign out of AutoRABIT.
6. Go to the AutoRABIT login page and click **Single Sign On**.
7. Enter your AutoRABIT domain, click **Go**, and sign in with your Entra ID credentials.

After completing these steps, users assigned to the AutoRABIT application in Entra ID can access AutoRABIT with seamless single sign-on.
