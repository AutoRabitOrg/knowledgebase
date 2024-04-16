# Single Sign-On with PingOne

**PingOne** is a service providing single sign-on (SSO) for web and mobile applications.

As a CodeScan administrator, you can implement **Security Assertion Markup Language (SAML) 2.0 SSO** when your company uses PingOne. Users can then log in to CodeScan without providing their authentication credentials since their identity was previously validated when logging in to their PingOne session.

This procedure involves the following steps:

1. Enabling Single Sign-On in CodeScan
2. Adding CodeScan as an App in PingOne
3. Entering PingOne- Identity Provider Data in CodeScan
4. Adding Attribute Mappings in PingOne
5. Testing the Single Sign-On Configuration

### Step 1: Enabling Single Sign-On in CodeScan <a href="#step-1-enabling-single-signon-in-codescan" id="step-1-enabling-single-signon-in-codescan"></a>

Before configuring SSO in PingOne, you must enable SSO in CodeScan.

1. In **CodeScan**, click on the **`Profile`** icon on the right corner of the screen and select your organization (under **`My Organizations`**).\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CMD0MROI.png)
2. Go to **`Administration > SAML Connections`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-G3278TSO.png)
3. Click on **`Create Connection`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0MWSWQEB.png)
4. In the **`Connection name`** field, enter the _identity provider_ name as you want to appear (use only Latin characters without spaces and any special characters).\
   **Example-** `PingOne-SAML`
5. Enter a valid domain name of the organization in the **`Corporate domain`** field that can be authenticated in the Identity Provider. _**This property cannot be updated after SAML Connection creation.**_\
   **Example**- _In case of `abc@autorabit.com`, the **corporate domain** will be `autorabit.com`_.
6. Keep the **`Enforce SSO`** checkbox unchecked for now. You can enable Enforce SSO later when your domain has been confirmed. Once enabled, only SSO authentication will be allowed for email addresses of your corporate domain.

Point to Note:

1. Enforcing SSO affects both login and signup. Existing _Auth0_ users won't be able to login.
2. Signup with email domain same as corporate domain won't be allowed.
3. If the **`Enforce SSO`** is enabled prematurely, it will prevent all **users in their organisation** from accessing CodeScan. Consider enforcing SSO only after admins have logged in to CodeScan using SSO.
4. Keep the **`SAML Connection status`** checkbox as **`Enabled`** and click on **`Create`** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-T0KTVATS.png)
5. You will be able to see the **`Metadata URL`** generated for your SSO configuration. Keep the current page open while you continue to add the CodeScan app to PingOne.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AMKE0X1Y.png)

### Step 2: Adding CodeScan as an App in PingOne <a href="#step-2-adding-codescan-as-an-app-in-pingone" id="step-2-adding-codescan-as-an-app-in-pingone"></a>

Set up the PingOne application to provide necessary configuration information for CodeScan.

1. Log in to your [PingOne Administrator](https://admin.pingone.com/web-portal/login) account.
2. Select the **`Environment`**.
3. Go to the **`Connections`** tab and select **`Applications`** as a sub-tab.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-H335BZYO.png)
4. Click on the ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-06PZ00R8.png) icon besides **`Applications`** to add a new app.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-HTQSTXBJ.png)
5. In the **`Add Application`** section,\
   a. Enter **`CodeScan`** for the application name and give a short description.\
   b. Choose **`Application Type`** as **`SAML Application`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-P1MG9V01.png)
6. Click **`Configure`**.
7. In the **`SAML Configuration`** section, select the **`Import From URL`** option.
8. Enter the same **`Metadata URL`** which you have generated inside CodeScan.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-REAAL6XD.png)
9. Click on the **`Import`** button. The metadata should be successfully imported, and you should see the parsed metadata values.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-J1KKV0EG.png)
10. Click **`Save`**.

### Step 3: Entering Identity Provider Data in CodeScan <a href="#step-3-entering-identity-provider-data-in-codescan" id="step-3-entering-identity-provider-data-in-codescan"></a>

Once the application is created, you will need to enter the identity provider data from PingOne into CodeScan.

1. In **CodeScan**, on the **`SAML`** page, go to **`Actions`** and click on **`Edit`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-873HQJIG.png)
2. You will need to paste the _mandatory/optional_ details below into CodeScan from PingOne Identity Provider.
   1. **Mandatory Settings**:
      1. Provider Entity ID
      2. Sign In URL
      3. X509 Signing Certificate
      4. SAML user email attribute
      5. SAML user name attribute
   2. **Optional Settings**:
      1. SAML user login attribute
      2. SAML group attribute\
         ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-I7R74IDO.png)
3. In **PingOne**, go to the **`Configuration`** tab.
4. Copy the following values:
   * **`Issuer ID`**: Copy **Issuer ID** value and paste it into **`Provider Entity Id`** inside Codescan.
   * **`Single Signon Service`**: Copy **Single Signon Service** value and paste it into **`Sign In URL`** inside Codescan.\
     ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-DDIGNFNT.png)
5. Click on the **`Edit`** icon in the top-right corner.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YRNS7C59.png)
6. Click on **`Download Signing Certificate`** in **X509 PEM (.crt)** format and copy the content of the file (certificate) into the **`X509 Signing Certificate`** field of Codescan SAML connection.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Y1PMS9WB.png)\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-9I832J14.png)
7. Click **`Update`** on the CodeScan page.
8. The next step is to confirm your corporate domain to get the SSO working. You can confirm domain via raising a request to [Codescan Support](https://mailto:support@autorabit.com/).

### Step 4: Adding Attribute Mappings in PingOne <a href="#step-4-optional-adding-attribute-mappings-in-pingone" id="step-4-optional-adding-attribute-mappings-in-pingone"></a>

It’s necessary to sync attributes of IDP users with properties of CodeScan users.

1. In **PingOne**, go to the **`Attribute Mappings`** tab of your SAML Application and click on the **`Edit`** icon.
2. Add these attributes and map to corresponding PingOne properties:

<table data-full-width="true"><thead><tr><th>CodeScan Attribute</th><th>PingOne Attribute</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td>saml_subject</td><td>User ID</td><td>Yes</td><td>User ID is a default required in PingOne</td></tr><tr><td>saml_username</td><td>Username</td><td>Yes</td><td>PingOne username will be used for newly created CodeScan users</td></tr><tr><td>saml_email</td><td>Email Address</td><td>Yes</td><td>PingOne email will be copied to user profile in CodeScan</td></tr><tr><td>saml_name</td><td>Formatted</td><td>Optional</td><td>PingOne formatted name will be copied to user profile in CodeScan</td></tr><tr><td>saml_groups</td><td>Group Names</td><td>Optional</td><td>PingOne user groups will be automatically created in CodeScan Organization, and user will be added to these groups</td></tr></tbody></table>

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-8RO2A5FG.png)\
3\. Click **`Save`**.\
4\. Enable the **`CodeScan`** app.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JPSPZIMG.png)

### Step 5: Testing the Single Sign-On Configuration <a href="#step-5-testing-the-single-signon-configuration" id="step-5-testing-the-single-signon-configuration"></a>

1. Log out of the CodeScan Console, and then log back in using the **`Log in with SAML2`** option.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RIVPFU59.png)
2. Enter the domain name of your organization in the **`Your Company email`** field. **For example**- _autorabit.com_.
3. You should successfully redirect to the CodeScan **`Organization`** page after authentication.
