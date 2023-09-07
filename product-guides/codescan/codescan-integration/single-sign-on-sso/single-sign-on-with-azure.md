# Single sign-On with Azure

### Overview <a href="#overview" id="overview"></a>

This step-by-step guide explains how to set up Single Sign-On in CodeScan with Microsoft Azure Active Directory (AD) as your SAML 2.0 Identity Provider (IdP).

When you integrate CodeScan with Azure AD, you can:

1. Control in Azure AD who has access to CodeScan
2. Enable your users to be automatically signed in to CodeScan with their Azure AD accounts
3. Manage your accounts in one central location - the Azure portal.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To get started, you need the following items:

1. Microsoft Azure account with Azure AD Premium activated.
2. Administrator level access to CodeScan and Azure AD to configure SSO.
3. Enable Single sign-on in CodeScan.
4. Add **CodeScan** as a non-gallery application in Azure.

### Instructions <a href="#instructions" id="instructions"></a>

#### Step 1: Enabling Single Sign-On in CodeScan <a href="#step-1-enabling-single-signon-in-codescan" id="step-1-enabling-single-signon-in-codescan"></a>

Before configuring SSO in Azure AD, you must enable SSO in CodeScan.

1. In **CodeScan**, click on the **`Profile`** icon on the right corner of the screen and select your organization (under **`My Organizations`**).\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CMD0MROI.png)
2. Go to **`Administration > SAML Connections`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-G3278TSO.png)
3. Click on **`Create Connection`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0MWSWQEB.png)
4. In the **`Connection name`** field, enter the _identity provider_ name as you want to appear (use only Latin characters without spaces and any special characters).\
   **Example-** `AD-SAML`
5. Enter a valid domain name of the organization in the **`Corporate domain`** field that can be authenticated in the Identity Provider. _**This property cannot be updated after SAML Connection creation.**_\
   **Example**- _In case of `abc@autorabit.com,` the **corporate domain** will be `autorabit.com.`_
6.  Keep the **`Enforce SSO`** checkbox unchecked for now. You can enable Enforce SSO later when your domain has been confirmed. Once enabled, only SSO authentication will be allowed for email addresses of your corporate domain.

    Point to Note:

    1. Enforcing SSO affects both login and signup. Existing _Auth0_ users won't be able to login.
    2. Signup with email domain same as corporate domain won't be allowed.
    3. If the **`Enforce SSO`** checkbox is enabled prematurely, it will prohibit all **users in their organisation** from accessing CodeScan. Consider enforcing SSO only after admins have logged in to CodeScan using SSO.
7. Keep the **`SAML Connection status`** checkbox as **`Enabled`** and click on **`Create`** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZC6B0N7X.png)
8. You will be able to see the **`Metadata URL`** generated for your SSO configuration. Keep the current page open while you continue to add the CodeScan app to Azure AD.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-DWM74YCM.png)

#### Step 2: Configuring Azure <a href="#step-2-configuring-azure" id="step-2-configuring-azure"></a>

1. Log in to the Azure portal (https://portal.azure.com/). In the left-hand menu, click **`Azure Active Directory > Enterprise applications`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-D91UT3DX.png)
2. Select **`All applications`** under the **`Manage`** section.
3. Click **`+ New application`** at the top of the screen.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-LB3FDZF2.png)
4. On the next screen, click on the **`+ Create your own application`** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-4S3GGYVI.png)
5. Enter the name of the app as **`CODESCAN`** and choose the third option i.e., **`Integrate any other application you don't find in the gallery (Non-gallery)`**. Click **`Create`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-8V3ACKID.png)
6. Once the CodeScan application is created, click on **`Single sign-on`** under the **`Manage`** section.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-20MHTNN3.png)
7. On the **`Select a Single sign-on method`** dialog, select **`SAML`** mode to enable single sign-on.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YDKGLEDG.png)
8. On the **`Set up Single Sign-On with SAML`** page, click the **`Edit (pencil)`** icon for **`Basic SAML Configuration`** to edit the settings.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-8WPFYYNK.png)
9.  On the **`Basic SAML Configuration`** section, perform the following steps:

    1. In the **`Identifier (Entity ID)`** field, enter the **`connection_id`** in this field. **Example:** `AD-SAML`

    Where can I find my **`connection_id`**?

    Your _connection\_id_ will be available in the **`Metadata URL`** generated inside CodeScan.

    **For example:**\
    _Metadata URL-_ `https://app.codescan.io/_codescan/saml2/metadata/AD-SAML`\
    _Connection\_Id-_ `AD-SAML`

    2. In the **`Reply URL`** field, enter the **`URL`** in the below format: _`{instanceurl}/codescan/login/saml2/sso/{connection_id}`_\
       \
       **For example:** If your **instance URL** is `https://app.codescan.io` and the **connection\_id** is `AD-SAML,` your **Reply URL** would be _`https://app.codescan.io/_codescan/login/saml2/sso/OKTA-SAML`_\
       ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JP279SGX.png)
    3. Click **`Save`** and close the dialog box.
10. Click the **`Edit (pencil)`** icon for **`Attributes & Claims`** to edit the attributes settings.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GNL1HSKH.png)
11. On the **`Attributes & Claims`** section, delete the auto-generated claims available in the **`Additional claims`** section.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-5BFRAI2A.png)
12. Next, click on **`+ Add New Claim`**.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-VVTLLNX6.png)
13. In the **`Manage Claim`** page, fill in the below details:

    | Name        | Source    | Source Attribute |
    | ----------- | --------- | ---------------- |
    | saml\_email | Attribute | user.mail        |
14. Click **`Save`**.
15. Follow similar steps to add two more claims as mentioned in the below table:

    | Name           | Source    | Source Attribute |
    | -------------- | --------- | ---------------- |
    | saml\_username | Attribute | user.mail        |
    | saml\_name     | Attribute | user.displayname |

    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GNMPKJUP.png)
16. Close the dialog box and navigate to **`Users and groups`** section. Click on **`+ Add user/group`** button to assign users and groups to app-roles for the CodeScan application.
17. Click on **`Single sign-on`** to navigate back to the **`Set up Single Sign-On with SAML`** page.
18. In the **`SAML Certificate`** section, find **`Certificate (Base64)`** and select **`Download`** to download the certificate and save it on your computer.

    Point to Note:

    Open the above downloaded certificate into your **Notepad++**, you will need to copy and paste the certificate into the CodeScan application while carrying out SAML configuration.
19. In the **`SAML Certificate`** section, find **`Federation Metadata XML`** and select **`Download`** to download the certificate and save it on your computer.

#### Step 3: Configuring in CodeScan SAML Connection <a href="#step-3-configuring-in-codescan-saml-connection" id="step-3-configuring-in-codescan-saml-connection"></a>

Now that your Azure SSO implementation is set up, you’ll need to follow just a few more steps to configure SSO in your CodeScan account.

1. In **CodeScan**, on the **`SAML`** page, go to **`Actions`** and click on **`Edit`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-VMIRBLEQ.png)
2. Open the **`Federation Metadata XML`** certificate that you have earlier downloaded from Azure in a new tab of your browser.
3. In the **`Edit SAML Connection`** dialog box on CodeScan, enter the following values:
   1. **`Provider Entity Id`**: Copy the **entityID** value from the _Federation Metadata XML certificate_ and paste it into **`Provider Entity Id`** inside CodeScan.\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-4ZD0JEAS.png)
   2. **`Sign In URL`**: Copy the **SingleSignOnService Location** value and paste it into the **`Sign In URL`** inside CodeScan.\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Q94OUXNS.png)
   3. Open the **Certificate (Base64)** that you have downloaded from Azure in your Notepad++, copy the entire content and paste into the **`X509 Signing Certificate`** field of the CodeScan SAML connection.\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Z6FNAD80.png)
4. Click **`Update`** on the CodeScan page.
5. The next step is to confirm your corporate domain to get the SSO working. You can confirm domain via raising a request to [Codescan Support](https://mailto:support@autorabit.com/).

#### Step 4: Testing the Single Sign-On Configuration <a href="#step-4-testing-the-single-signon-configuration" id="step-4-testing-the-single-signon-configuration"></a>

1. Log out of the CodeScan Console, and then log back in using the **`Log in with SAML2`** option.
2. Enter the corporate domain name you have configured when enabling SSO inside CodeScan in the **`Your Company email`** field. **For example-** _autorabit.com_
3. You should successfully redirect to the CodeScan **`Organization`** page after authentication.
