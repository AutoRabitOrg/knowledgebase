# SSO With Microsoft Azure AD

### Overview <a href="#overview" id="overview"></a>

This step-by-step guide explains how to set up **Single Sign-On** in AutoRABIT with **Microsoft Azure Active Directory (AD)** as your **SAML 2.0 Identity Provider (IdP)**.

When you integrate AutoRABIT with Azure AD, you can:

1. Control in Azure AD who has access to AutoRABIT
2. Enable your users to be automatically signed in to AutoRABIT with their Azure AD accounts
3. Manage your accounts in one central location - the Azure portal.
4. Test Pull Request Change

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To get started, you need the following items:

1. An **Azure AD** subscription.
2. You will need to be an **Administrator** in AutoRABIT and in Azure AD to configure SSO.
3. Add AutoRABIT as a **non-gallery** application.

### In Azure AD <a href="#in-azure-a-d" id="in-azure-a-d"></a>

1. Sign in to your Azure management portal.
2. Select the **Azure Active Directory** service from the left sidebar. Click **Enterprise applications**.
3. Select **All applications** from the **Application type** dropdown.
4. Click **New application** and, on the **Add from the gallery section**, type _autorabit,_ and press **Enter**.
5. From the results, select **AutoRABIT**, change the name if you wish, and click **Add**.
6. Go to the AutoRABIT app page and click on **Single sign-on**.
7. On the **Select a Single sign-on method** dialog, select **SAML** mode to enable single sign-on.
8. On the **Set up Single Sign-On with SAML** page, click the **Edit (pencil)** icon for Basic SAML Configuration to edit the settings.
9. On the **Basic SAML Configuration** section, perform the following steps:
   1. In the **Identifier (Entity ID)** field, enter the URL in the following format: **\<instanceURL>/saml/metadata**. _For example-_ If your instance is **https://xyz.com**, then the Identifier (Entity ID) would be: _**https://xyz.com/saml/metadata**_
   2. In the **Reply URL** field, enter the URL in the following format: **\<instanceURL>/saml/SSO.** _For example-_ If your instance is **https://xyz.com**, then the payload URL would be: _**https://xyz.com/saml/SSO**_
   3. In the **Sign on URL** field type the secure URL of your domain (i.e. starting with https://). For example- _**https://xyz.com**_
10. On the **Set up Single Sign-On with SAML** page, in the **SAML Signing Certificate** section, find **Federation Metadata XML** and select **Download** to download the certificate and save it on your computer.

### In AutoRABIT <a href="#in-autorabit" id="in-autorabit"></a>

Now that your Azure SSO implementation is set up, you’ll need to follow just a few more steps to configure SSO in your AutoRABIT account.

1. Login to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **My Account**
3. On the **My Account** page, go to the 3rd section: **SSO Configuration**
4. Browse for the metadata **XML** file you downloaded in your local machine and upload them.
5. Sign out from your **AutoRABIT** account.
6. Go to the AutoRABIT login page. This time you need to log in via SSO, so, therefore, click on the option: **Single Sign On**
7. Enter the domain name and click on **Go**.
