# SSO Configuration

### Configuring Single Sign-On (SSO) <a href="#configuring-single-signon-sso" id="configuring-single-signon-sso"></a>

SSO is an authentication process that allows users to access multiple applications after only signing in once. Vault supports SSO integration for any identity provider that adheres to the OASIS SAML 2.0 protocol.

### Permissions <a href="#permissions" id="permissions"></a>

Only **System Admins** can configure SSO settings for your organization.&#x20;

To check your admin access in Vault, go to **Manage Users > Users** and verify if your "Type" is set to **Admin**.

<figure><img src="../../../../.gitbook/assets/image (1584).png" alt=""><figcaption></figcaption></figure>

### How to enable SSO <a href="#how-to-enable-sso" id="how-to-enable-sso"></a>

To enable SSO for Vault, you need to perform the below steps:

1. Configure SSO settings in your identity provider.
2. Login to your Vault account.
3. Go to **Settings > SSO Configuration.**
4. Fill out the SSO fields:
   1. Give a unique name that identifies your instance in the **Single Sign-on** field.
   2. Choose how you would like to configure the SSO:
      * **Metadata URL:** The URL that Vault can access to obtain SSO configuration data from your identity provider. This is a URL specific to your identity provider.
      * **Metadata File:** Upload the metadata file obtained from your identity provider.
5. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### How to log in when SSO is enabled <a href="#how-to-log-in-when-sso-is-enabled" id="how-to-log-in-when-sso-is-enabled"></a>

When SSO is enabled, you can sign in by going to the Vault log-in page, click on **Login with SSO**, and providing your custom domain.

<figure><img src="../../../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>
