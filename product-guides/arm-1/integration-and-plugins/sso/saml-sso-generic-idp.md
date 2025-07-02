# SAML SSO (Generic IdP)

## SAML SSO Integration (Generic Identity Provider)&#x20;

This guide explains how to set up Single Sign-On (SSO) in AutoRABIT with any Identity Provider (IdP) that supports SAML 2.0, such as SailPoint, Okta, Ping Identity, or others.&#x20;

When you integrate AutoRABIT with a SAML 2.0 IdP, you can:&#x20;

* Control access to AutoRABIT through your IdP&#x20;
* Enable users to sign in to AutoRABIT with their IdP credentials&#x20;
* Manage user permissions centrally in your IdP&#x20;

### Prerequisites&#x20;

To get started, you need the following:&#x20;

* An IdP that supports SAML 2.0&#x20;
* Administrator access to AutoRABIT and your IdP&#x20;
* The ability to configure a custom or non-gallery SAML application in your IdP&#x20;

**Step 1: Configure Your Identity Provider**&#x20;

Log in to your IdP management console and create a new custom SAML application. In the SAML configuration screen, use the following values:&#x20;

* Identifier (Entity ID): \
  https://\<your-instance-domain>/saml/metadata \
  (Example: [https://xyz.com/saml/metadata](https://xyz.com/saml/metadata))&#x20;
* Reply URL (Assertion Consumer Service URL): \
  https://\<your-instance-domain>/saml/SSO \
  (Example: [https://xyz.com/saml/SSO](https://xyz.com/saml/SSO))&#x20;
* Sign-on URL (optional): \
  https://\<your-instance-domain> \
  (This is the secure login page of your AutoRABIT instance)&#x20;

Once configured, locate and download the Federation Metadata XML or equivalent metadata file from your IdP.&#x20;

&#x20;**Step 2: Configure SSO in AutoRABIT**&#x20;

1. Log in to your AutoRABIT account as an administrator.&#x20;
2. Hover over the Admin module and select My Account.&#x20;
3. On the My Account page, scroll down to the SSO Configuration section.&#x20;
4. Upload the metadata XML file you downloaded from your IdP.&#x20;
5. Save your changes and sign out of your AutoRABIT account.&#x20;

&#x20;

**Step 3: Test SSO Access**&#x20;

1. Go to the AutoRABIT login page.&#x20;
2. Click the Single Sign-On option.&#x20;
3. Enter your configured domain name and click Go.&#x20;
4. You will be redirected to your Identity Provider to authenticate.&#x20;
5. After successful authentication, you will be directed back to AutoRABIT.&#x20;

&#x20;

**Troubleshooting Tips**&#x20;

* Ensure that the times on your IdP and AutoRABIT instance are synchronized.&#x20;
* The user’s email in the IdP must match the user record in AutoRABIT.&#x20;
* If the login fails, check the SAML response using a browser plugin like SAML-tracer or review your IdP's activity logs.&#x20;
