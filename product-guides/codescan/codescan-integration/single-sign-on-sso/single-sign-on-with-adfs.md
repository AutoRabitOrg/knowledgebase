# Single Sign-On with ADFS

## **Overview**

This article describes configuring a self-hosted Active Directory Federation Services (ADFS) server to act as a SAML 2.0 identity provider (IDP) in your CodeScan account.

## **Prerequisites**

To get started, you need the following items:

1. Administrator-level access to CodeScan and ADFS to configure SSO.
2. Enable Single Sign-On in CodeScan.

## **Instructions**

### **Step 1: Enabling Single Sign-On in CodeScan**

Before configuring SSO in ADFS, you must enable SSO in CodeScan.

1. In **CodeScan**, click on the **Profile** icon on the right corner of the screen and select your organization (under **My Organizations**).
2. Go to **Administration > SAML Connections**.
3. Click on **Create Connection**.
4. In the **Connection name** field, enter the identity provider name as you want to appear (use only Latin characters without spaces or any special characters).\
   **Example-**_**CodeScan**_
5. Enter a valid domain name for the organization in the **Corporate domain** field that can be authenticated in the Identity Provider. _**This property cannot be updated after SAML Connection creation.**_\
   **Example**-_In the case of_ [_abc@autorabit.com,_](mailto:abc@autorabit.com) _the **corporate domain** will be autorabit.com._
6. Keep the **Enforce SSO checkbox** unchecked for now. You can enable this option later when your domain has been confirmed. Once enabled, only SSO authentication will be allowed for email addresses of your corporate domain.

{% hint style="info" %}
**Point to Note:**

1. Enforcing SSO affects both login and signup. Existing _Auth0_ users won't be able to log in.
2. Signup with an email domain the same as the corporate domain won't be allowed.
3. If the **Enforce SSO** checkbox is enabled prematurely, it will prohibit all **users in their organization** from accessing CodeScan. Consider enforcing SSO only after admins have logged in to CodeScan using SSO.
{% endhint %}

7. Keep the **SAML Connection status** checkbox as **Enabled** and click on the **Create** button.

<figure><img src="../../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1).png" alt="" width="383"><figcaption></figcaption></figure>

8. You can see the **Metadata URL** generated for your SSO configuration. Copy the **Metadata URL** in a new browser tab to download the XML file on your local device.

<figure><img src="../../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Step 2: Setting up Single Sign-On using Active Directory with ADFS and SAML 2.0**

**2.1  Adding a Relying Party Trust**

To set up the ADFS connection with CodeScan using a Relying Party Trust (RPT), follow the below steps:

1. Log in to the **ADFS Server**.
2. Go to **Tools > AD FS Management** to launch the **ADFS Management Console**.
3. Click on **Add Relying Party Trust…** from the **Actions** sidebar on the right.

<figure><img src="../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the **Welcome** screen, select the **Claims aware** option and click **Start**.

<figure><img src="../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. On the **Select Data Source** screen, select the second option: **Import data about the relying party from a file**.
6. Browse for the **metadata XML** file from your local computer and upload it in the **Federation**  **metadata file location**.

<figure><img src="../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

7. On the next screen, enter a **display name** that you will recognize in the future.

<figure><img src="../../../../.gitbook/assets/image (48) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

8. On the next screen, leave the defaults.

<figure><img src="../../../../.gitbook/assets/image (49) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

9.  On the **Configure URL** screen:

    * Select the checkbox labeled: **Enable support for the SAML 2.0 WebSSO protocol** .
    * In the **Relying party SAML 2.0 SSO service URL** , enter the _service URL_ in the below format: _**{instance\_url}/\_codescan/saml2/metadata/{connection\_id}**_\
      **For example:** If your **instance URL** is _**https://app.codescan.io**_ and the **connection\_id** is _**CodeScan**_, your service URL would be _**https://app.codescan.io/\_codescan/saml2/metadata/CodeScan**_

    <figure><img src="../../../../.gitbook/assets/image (50) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Where can I find my connection\_id?**

Your connection\_id will be available in the **Metadata URL** generated inside CodeScan.

**For example:**

**Metadata URL-**_https://app.codescan.io/\_codescan/saml2/metadata/<mark style="background-color:yellow;">CodeScan</mark>_ **Connection\_Id-**_CodeScan_
{% endhint %}

10. Click **Next**.
11. On the next screen, add a **Relying party trust identifier** . This should be the name of your SAML connection in CodeScan. In this case, it is _**CodeScan.**_
12. Click **Add**.

<figure><img src="../../../../.gitbook/assets/image (51) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

13. On the next screen, leave the defaults.

<figure><img src="../../../../.gitbook/assets/image (52) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

14. The wizard will display an overview of your settings on the next screen. Click **Next**.

<figure><img src="../../../../.gitbook/assets/image (53) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

15. On the final screen, keep the **Configure claims issuance policy for this application** checkbox selected, and click on the **Close** button to open the Claim Rules editor.

<figure><img src="../../../../.gitbook/assets/image (54) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### **2.2 Creating Claim Rules**

Once the Relying Party Trust exists, you can create the claim rules and update the Relying Party Trust with minor changes that the wizard does not set.

1. By default, the Claim Rules editor opens once you create the trust.
2. To create a new rule, click on **Add Rule**.

<figure><img src="../../../../.gitbook/assets/image (55) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

3. Select **Send LDAP Attributes as Claims** as the claim rule template.

<figure><img src="../../../../.gitbook/assets/image (56) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. On the next screen, give the claim rule a unique **name**.
5. Using **Active Directory** as your attribute store, enter the following details:

| **LDAP Attribute**  | **Outgoing Claim Type** |
| ------------------- | ----------------------- |
| E-Mail-Addresses    | E-Mail Address          |
| Display-Name        | Name                    |
| User-Principal-Name | Name ID                 |

<figure><img src="../../../../.gitbook/assets/image (57) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **Finish** to save the new rule and then **OK** again to finish creating rules.
7. Under **ADFS Management Console** , navigate to **Service > Endpoints** and find the metadata URL. Copy and paste the URL to open the XML file on your browser. Keep the tab open; you will need certain information from here to add to the CodeScan application.

<figure><img src="../../../../.gitbook/assets/image (58) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (59) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8.  To download the **X509 Signing Certificate**, navigate to **Service > Certificates** under the ADFS Management Console.&#x20;

    * Export the Token-signing certificates from ADFS and add them to the CodeScan SAML configuration. When using the certificate exporting wizard, select **Base-64 encoded X.509 (.CER)** for the encoding format.
    * Open the exported file in a text editor to get the certificate value.

    <figure><img src="../../../../.gitbook/assets/image (60) (1) (1) (1).png" alt="" width="374"><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (61) (1) (1) (1).png" alt="" width="419"><figcaption></figcaption></figure>

### **Step 3: Configuring in CodeScan SAML Connection**

Now that your ADFS SSO implementation is set up, you must follow a few more steps to configure SSO in your CodeScan account.

1. In **CodeScan**, on the **SAML** page, go to **Actions** and click on **Edit**.
2. Go to the tab of your browser where you have kept the metadata XML certificate open.
3.  In the **Edit SAML Connection** dialog box on **CodeScan**, enter the following values:

    * **Provider Entity Id:** Copy the **entityID** value from the ADFS Metadata XML file and paste it into **Provider Entity Id** inside CodeScan. \
      The entity Id format would be in _**https://\<ADFS\_DOMAIN\_NAME>/adfs/services/trust.**_

    <figure><img src="../../../../.gitbook/assets/image (63) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    * **Sign In URL:** Copy the **SingleSignOnService Location** value and paste it into the **Sign-In URL** inside CodeScan.

    <figure><img src="../../../../.gitbook/assets/image (64) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. Open the **Certificate (.CER)** you downloaded from ADFS in your text editor, copy the entire content, and paste it into the **X509 Signing Certificate** field of the CodeScan SAML connection.

<figure><img src="../../../../.gitbook/assets/image (65) (1) (1) (1).png" alt="" width="419"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (66) (1) (1) (1).png" alt="" width="398"><figcaption></figcaption></figure>

5. Set up the SAML attributes in **CodeScan** in accordance with the **Active Directory** attributes (refer to [_**Section 2.2**_](https://knowledgebase.autorabit.com/codescan/docs/single-sign-on-with-adfs#22-creating-claim-rules)_**, Point 5**_):

<figure><img src="../../../../.gitbook/assets/image (67) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **Update** on the CodeScan page.
7. The next step is to confirm your corporate domain to get the SSO working. You can confirm the domain by raising a request to CodeScan support at [http://mailto:support@autorabit.com/](http://mailto:support@autorabit.com/).

### **Step 4: Testing the Single Sign-On Configuration**

1. Log out of the **CodeScan Console**, and then log back in using the **Log in with SAML2**  option.
2. Enter the corporate domain name you have configured when enabling SSO inside CodeScan in the **Your Company email** field. _**For example - autorabit.com**_
3. You should now successfully redirect to the CodeScan **Organization** page after authentication.
