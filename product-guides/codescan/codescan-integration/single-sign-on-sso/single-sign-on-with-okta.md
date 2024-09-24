# Single Sign-On with OKTA

This article explains configuring Single Sign-On (SSO) in CodeScan with Okta as your SAML 2.0 Identity Provider.

To allow users to log in via SAML SSO, CodeScan must be able to trust and rely on Okta to authenticate users wanting to log in. To establish this trust relationship, you must configure Okta and CodeScan so both parties can exchange authentication information.

When SSO is enabled, users and groups logging into CodeScan are redirected to the Okta login page. After successful authentication, they are redirected to the AutoRABIT Dashboard.

**Who can use this feature**

1. Only Organization Admins can set up SAML SSO.
2. You will need an existing Okta account to set up SAML SSO with Okta.

### Step 1: Enabling Single Sign-On in CodeScan <a href="#step-1-enabling-single-signon-in-codescan" id="step-1-enabling-single-signon-in-codescan"></a>

Before configuring SSO in OKTA, you must enable SSO in CodeScan.

1. In **CodeScan**, click on the **`Profile`** icon on the right corner of the screen and select your organization (under **`My Organizations`**).

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Go to **`Administration > SAML Connections`**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Click on **`Create Connection`**.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. In the **`Connection name`** field, enter the identity provider name as you want to appear (use only Latin characters without spaces and any special characters).\
   **Example-** `OKTA-SAML`
5. Enter a valid domain name of the organization in the **`Corporate domain`** field that can be authenticated in the Identity Provider. _**This property cannot be updated after SAML Connection creation.**_\
   **Example**- _In case of `abc@autorabit.com`, the **corporate domain** will be `autorabit.com`_.
6.  Keep the **`Enforce SSO`** checkbox unchecked for now. You can enable _Enforce SSO_ later when your domain has been confirmed. Once enabled, only SSO authentication will be allowed for email addresses of your corporate domain.

    Point to Note:

    * Enforcing SSO affects both login and signup. Existing _Auth0_ users won't be able to login.
    * Signup with email domain same as corporate domain won't be allowed.
    * If the **`Enforce SSO`** is enabled prematurely, it will prevent all **users in their organisation** from accessing CodeScan. Consider enforcing SSO only after admins have logged in to CodeScan using SSO.
7. Keep the **`SAML Connection status`** checkbox as **`Enabled`** and click on **`Create`** button.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="394"><figcaption></figcaption></figure>

8. You will be able to see the **`Metadata URL`** generated for your SSO configuration. Keep the current page open while you continue to add the CodeScan app to OKTA.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Step 2: Adding CodeScan as an App in OKTA <a href="#step-2-adding-codescan-as-an-app-in-okta" id="step-2-adding-codescan-as-an-app-in-okta"></a>

Set up the CodeScan application to provide necessary configuration information for CodeScan.

1. Sign in to Okta. You must have the Applications **`Admin`** permission.
2. If you don’t have an Okta organization, you can create a free Okta Developer Edition organization here: [https://developer.okta.com/signup/](https://developer.okta.com/signup/)
3. Navigate to the **`Admin`** dashboard.
4. From the main menu, go to **`Applications > Applications`**.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="252"><figcaption></figcaption></figure>

5. Click on **`Create App Integration`**.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="471"><figcaption></figcaption></figure>

6. In the next auto-populated dialog box, select the second option, i.e., **`SAML 2.0`**, and click on **`Next`**.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

7. In the **`General Settings`**, enter **`CodeScan`** in the App name field, upload the **`CodeScan logo`** and click on the **`Next`** button.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

8.  In the **`Configure SAML`** tab, do the following:

    * **`Single sign on URL`**: Enter the same **`URL`** in the below format: _`{instanceurl}/_codescan/login/saml2/sso/{connection_id}`_\
      **For example:** If your _instance URL_ is `https://app.codescan.io` and the _connection\_id_ is `OKTA-SAML`, your SSO URL would be _`https://app.codescan.io/_codescan/login/saml2/sso/OKTA-SAML`_
    * **`Audience URI (SP Entity ID)`**: Enter your _connection\_id_ in this field. **Example:** `OKTA-SAML`

    <figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Where can I find my Connection ID?**

Your connection id will be available in the **Metadata URL** generated inside CodeScan.

**For example:** _Metadata URL_- https://app.codescan.io/\_codescan/saml2/metadata/OKTA-SAML\
_Connection Id_: OKTA-SAML
{% endhint %}

9. On the same screen, in the **`Attribute Statements`** panel, add the following attributes (mandatory) and map to corresponding OKTA properties:

| Name            | Name format   | Value            |
| --------------- | ------------- | ---------------- |
| `saml_email`    | `Unspecified` | `user.email`     |
| `saml_username` | `Unspecified` | `user.login`     |
| `saml_name`     | `Unspecified` | `user.firstName` |

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

10. Click **`Next`** to continue.
11. Under the **`Feedback`** section, select the option: **`I'm an Okta customer adding an internal app`** and click the checkbox next to the text **`"This is an internal application that we created"`**, and click on the **`Finish`** button.

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

12. Navigate your mouse to the **`Assignment`** tab, and click **`Assign > Assign to People`**.

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="546"><figcaption></figcaption></figure>

13. Next, select the listed **`users`** and click on **`Assign`**.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="544"><figcaption></figcaption></figure>

14. After you assign the user, click **`Save and Go Back`** and then click **`Done`**.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="544"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="450"><figcaption></figcaption></figure>

### Step 3: Configuring SAML Connection in CodeScan <a href="#step-3-configuring-saml-connection-in-codescan" id="step-3-configuring-saml-connection-in-codescan"></a>

Once the application is created, you will need to enter the identity provider data from OKTA into CodeScan.

1. In **OKTA**, go to the **`Sign On`** tab and navigate to the **`SAML Signing Certificates`** section.
2. For **SHA-2**, click on **`Actions > Download Certificate`**.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Open the downloaded certificate in Notepad. You will need to copy the content of the certificate into the **`X509 Signing Certificate`** field of CodeScan SAML connection \[_**Step 7.c** below_].
4. Click on the **`Actions > View IdP metadata`**.

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

5. A new tab will open, which displays the IdP metadata file in XML format.
6. In **CodeScan**, on the **`SAML`** page, go to **`Actions`** and click on **`Edit`**.

<figure><img src="../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7.  Enter the following values:

    * **`Provider Entity Id`**: Copy the **entityID** value and paste it into **`Provider Entity Id`** inside CodeScan.
    * **`Sign In URL`**: Copy the **SingleSignOnService Location** value and paste it into the **`Sign In URL`** inside CodeScan.

    <figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * Copy the content of the downloaded certificate \[_refer to **Step 2** above to download the certificate_] into the **`X509 Signing Certificate`** field of Codescan SAML connection.\


    <figure><img src="../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="396"><figcaption></figcaption></figure>
8. Click **`Update`** on the CodeScan page.
9. The next step is to confirm your corporate domain to get the SSO working. You can confirm domain by raising a request via [Codescan Support](https://mailto:support@autorabit.com/).

### Step 4: Testing the Single Sign-On Configuration <a href="#step-4-testing-the-single-signon-configuration" id="step-4-testing-the-single-signon-configuration"></a>

1. Log out of the CodeScan Console, and then log back in using the **`Log in with SAML2`** option.

<figure><img src="../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Enter the corporate domain name you have configured when enabling SSO inside CodeScan in the **`Your Company email`** field. **For example**- _`autorabit.com`_
3. You should successfully redirect to the CodeScan **`Organization`** page after authentication.
