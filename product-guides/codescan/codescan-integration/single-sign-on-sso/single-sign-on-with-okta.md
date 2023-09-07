# Single Sign-On with OKTA

This article explains configuring Single Sign-On (SSO) in CodeScan with Okta as your SAML 2.0 Identity Provider.

To allow users to log in via SAML SSO, CodeScan must be able to trust and rely on Okta to authenticate users wanting to log in. To establish this trust relationship, you must configure Okta and CodeScan so both parties can exchange authentication information.

When SSO is enabled, users and groups logging into CodeScan are redirected to the Okta login page. After successful authentication, they are redirected to the AutoRABIT Dashboard.\
\


> **Who can use this feature**

> 1. Only Organization Admins can set up SAML SSO.
> 2. You will need an existing Okta account to set up SAML SSO with Okta.

### Step 1: Enabling Single Sign-On in CodeScan <a href="#step-1-enabling-single-signon-in-codescan" id="step-1-enabling-single-signon-in-codescan"></a>

Before configuring SSO in OKTA, you must enable SSO in CodeScan.

1. In **CodeScan**, click on the **`Profile`** icon on the right corner of the screen and select your organization (under **`My Organizations`**).\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CMD0MROI.png)
2. Go to **`Administration > SAML Connections`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-G3278TSO.png)
3. Click on **`Create Connection`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0MWSWQEB.png)
4. In the **`Connection name`** field, enter the identity provider name as you want to appear (use only Latin characters without spaces and any special characters).\
   **Example-** `OKTA-SAML`
5. Enter a valid domain name of the organization in the **`Corporate domain`** field that can be authenticated in the Identity Provider. _**This property cannot be updated after SAML Connection creation.**_\
   **Example**- _In case of `abc@autorabit.com`, the **corporate domain** will be `autorabit.com`_.
6.  Keep the **`Enforce SSO`** checkbox unchecked for now. You can enable _Enforce SSO_ later when your domain has been confirmed. Once enabled, only SSO authentication will be allowed for email addresses of your corporate domain.

    Point to Note:

    1. Enforcing SSO affects both login and signup. Existing _Auth0_ users won't be able to login.
    2. Signup with email domain same as corporate domain won't be allowed.
    3. If the **`Enforce SSO`** is enabled prematurely, it will prevent all **users in their organisation** from accessing CodeScan. Consider enforcing SSO only after admins have logged in to CodeScan using SSO.
7. Keep the **`SAML Connection status`** checkbox as **`Enabled`** and click on **`Create`** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AVLTJU1P.png)
8. You will be able to see the **`Metadata URL`** generated for your SSO configuration. Keep the current page open while you continue to add the CodeScan app to OKTA.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0RFFDEHC.png)

### Step 2: Adding CodeScan as an App in OKTA <a href="#step-2-adding-codescan-as-an-app-in-okta" id="step-2-adding-codescan-as-an-app-in-okta"></a>

Set up the CodeScan application to provide necessary configuration information for CodeScan.

1. Sign in to Okta. You must have the Applications **`Admin`** permission.
2. If you don’t have an Okta organization, you can create a free Okta Developer Edition organization here: [https://developer.okta.com/signup/](https://developer.okta.com/signup/)
3. Navigate to the **`Admin`** dashboard.
4. From the main menu, go to **`Applications > Applications`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-A9SBNWB1.png)
5. Click on **`Create App Integration`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RHB4WLPG.png)
6. In the next auto-populated dialog box, select the second option, i.e., **`SAML 2.0`**, and click on **`Next`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AACOCTO7.png)
7. In the **`General Settings`**, enter **`CodeScan`** in the App name field, upload the **`CodeScan logo`** and click on the **`Next`** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-L0ZJV3VG.png)
8. In the **`Configure SAML`** tab, do the following:
   1. **`Single sign on URL`**: Enter the same **`URL`** in the below format: _`{instanceurl}/codescan/login/saml2/sso/{connection_id}`_\
      \
      **For example:** If your _instance URL_ is `https://app.codescan.io` and the _connection\_id_ is `OKTA-SAML`, your SSO URL would be _`https://app.codescan.io/_codescan/login/saml2/sso/OKTA-SAML`_\
      \

   2. **`Audience URI (SP Entity ID)`**: Enter your _connection\_id_ in this field. **Example:** `OKTA-SAML`\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-MJC4QFNR.png)

Where can I find my **`Connection ID`**?

Your connection id will be available in the **`Metadata URL`** generated inside CodeScan.

**For example:**\
_Metadata URL_- `https://app.codescan.io/_codescan/saml2/metadata/OKTA-SAML`\
_Connection Id_: `OKTA-SAML`

9. On the same screen, in the **`Attribute Statements`** panel, add the following attributes (mandatory) and map to corresponding OKTA properties:

| Name            | Name format   | Value            |
| --------------- | ------------- | ---------------- |
| `saml_email`    | `Unspecified` | `user.email`     |
| `saml_username` | `Unspecified` | `user.login`     |
| `saml_name`     | `Unspecified` | `user.firstName` |

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-EHTHZHAB.png)

10. Click **`Next`** to continue.
11. Under the **`Feedback`** section, select the option: **`I'm an Okta customer adding an internal app`** and click the checkbox next to the text **`"This is an internal application that we created"`**, and click on the **`Finish`** button.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-J3OU5FEN.png)
12. Navigate your mouse to the **`Assignment`** tab, and click **`Assign > Assign to People`**.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-NWCSAMK7.png)
13. Next, select the listed **`users`** and click on **`Assign`**.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-BOCYVWZG.png)
14. After you assign the user, click **`Save and Go Back`** and then click **`Done`**.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-A4KFW431.png)\
    \
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-NHTIRNQO.png)

### Step 3: Configuring SAML Connection in CodeScan <a href="#step-3-configuring-saml-connection-in-codescan" id="step-3-configuring-saml-connection-in-codescan"></a>

Once the application is created, you will need to enter the identity provider data from OKTA into CodeScan.

1. In **OKTA**, go to the **`Sign On`** tab and navigate to the **`SAML Signing Certificates`** section.
2. For **SHA-2**, click on **`Actions > Download Certificate`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-2MXV2EAY.png)
3. Open the downloaded certificate in Notepad. You will need to copy the content of the certificate into the **`X509 Signing Certificate`** field of CodeScan SAML connection \[_**Step 7.c** below_].
4. Click on the **`Actions > View IdP metadata`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-3ZNG9G91.png)
5. A new tab will open, which displays the IdP metadata file in XML format.
6. In **CodeScan**, on the **`SAML`** page, go to **`Actions`** and click on **`Edit`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-DIZHBCOC.png)
7. Enter the following values:
   1. **`Provider Entity Id`**: Copy the **entityID** value and paste it into **`Provider Entity Id`** inside CodeScan.
   2. **`Sign In URL`**: Copy the **SingleSignOnService Location** value and paste it into the **`Sign In URL`** inside CodeScan.\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XWLK0DZY.png)
   3. Copy the content of the downloaded certificate \[_refer to **Step 2** above to download the certificate_] into the **`X509 Signing Certificate`** field of Codescan SAML connection.\
      ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AAGXTM6Q.png)
8. Click **`Update`** on the CodeScan page.
9. The next step is to confirm your corporate domain to get the SSO working. You can confirm domain by raising a request via [Codescan Support](https://mailto:support@autorabit.com/).

### Step 4: Testing the Single Sign-On Configuration <a href="#step-4-testing-the-single-signon-configuration" id="step-4-testing-the-single-signon-configuration"></a>

1. Log out of the CodeScan Console, and then log back in using the **`Log in with SAML2`** option.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RIVPFU59.png)
2. Enter the corporate domain name you have configured when enabling SSO inside CodeScan in the **`Your Company email`** field. **For example**- _`autorabit.com`_
3. You should successfully redirect to the CodeScan **`Organization`** page after authentication.
