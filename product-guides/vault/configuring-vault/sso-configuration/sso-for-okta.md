# SSO for OKTA

This article explains how to configure Single Sign-On (SSO) in Vault using Okta as the SAML 2.0 Identity Provider. When SSO is enabled, users are redirected to Okta for authentication and, upon success, are taken to the Vault Dashboard.

## Add the Vault Application to Okta <a href="#add-vault-application-to-okta" id="add-vault-application-to-okta"></a>

### Steps:

1. Sign in to Okta as an admin. If you don’t have an Okta org, sign up at [https://developer.okta.com/signup/](https://developer.okta.com/signup/).
2. Go to **Applications > Add Application**.
3. Click **Create App Integration**.
4. Choose **SAML 2.0** and click **Next**.
5. In **General Settings**:
   * Name: **Vault**
   * Upload Vault logo
   * Click **Next**
6. In the **Configure SAML** tab:
   * **Single sign on URL:** `<instanceURL>/ARVault/saml/SSO`\
     &#xNAN;_&#x65;.g._: `https://vault-qa.autorabit.com/ARVault/saml/SSO`
   * **Audience URI (SP Entity ID):** `<instanceURL>/ARVault/saml/metadata`
7. Under **Attribute Statements**:

| Name                       | Value             |
| -------------------------- | ----------------- |
| firstname                  | `user.firstName`  |
| lastname                   | `user.lastName`   |
| customerid                 | Vault customer ID |
| restrictAutoCreationOfUser | `Yes` or `No`     |

> **Note**: Customer ID is available under the **Profile** section in your Vault account.

8. Click **Next**, then choose:
   * **"I'm an Okta customer adding an internal app"**
   * **"This is an internal application that we created"**
   * Click **Finish**
9. Go to the **Assignments** tab:
   * Click **Assign > Assign to People**
   * Assign users, click **Save and Go Back**, then **Done**
10. Go to the **Sign On** tab and click **Identity Provider Metadata**.
    * Save the file as XML or copy the metadata URL.

## Configure SSO in Vault <a href="#configure-sso-in-vault" id="configure-sso-in-vault"></a>

1. Log in to Vault
2. Navigate to **Settings > SSO Configuration**
3. Enter a name for the config and select:
   * **Metadata URL** (paste the copied link), or
   * **Metadata File** (upload the XML file)
4. Click **Activate**

> You may disable login with Vault credentials by toggling off that option.

## Logging in Using SSO <a href="#logging-in-using-sso" id="logging-in-using-sso"></a>

1. On the Vault login screen, click **Login with SSO**
2. Enter your **Customer ID**
3. Click **Sign in**

> You can also log in directly from your Okta dashboard by clicking on the Vault application icon.

## Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

**Error**:\
&#xNAN;_"Your user is not available in the account with provided customer id. Please contact the administrator to create a user for you in the account."_

**Causes**:

1. The user is not assigned to the Vault app in Okta.
2. `restrictAutoCreationOfUser` is set to **Yes** and the user has not been pre-created in Vault.
