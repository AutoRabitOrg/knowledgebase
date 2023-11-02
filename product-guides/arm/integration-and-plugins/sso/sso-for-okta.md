# SSO for OKTA

This article explains how to configure Single Sign-On (SSO) in AutoRABIT with Okta as your **SAML 2.0** Identity Provider. When SSO is enabled, by default users and groups logging into AutoRABIT are redirected to the Okta login page. After successful authentication, they are redirected to the AutoRABIT Dashboard.

### Add AutoRABIT Application to Okta <a href="#add-autorabit-application-to-okta" id="add-autorabit-application-to-okta"></a>

First, configure Okta to provide the sign-on information for the AutoRABIT environment.

To add the AutoRABIT application to Okta:

1. Sign in to Okta. You must have the Applications **Admin** permission.
2. If you don’t have an Okta organization, you can create a free Okta Developer Edition organization here: [https://developer.okta.com/signup/](https://developer.okta.com/signup/)
3. Navigate to the **Admin** dashboard.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622987685703.png" alt=""><figcaption></figcaption></figure>

4. From the main menu, go to **Applications > Applications.**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622987800866.png" alt=""><figcaption></figcaption></figure>

5. Click on **Create App Integration.**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1630071778168.png" alt="" width="375"><figcaption></figcaption></figure>

6. In the next auto-populated dialog box, select the second option i.e., **SAML 2.0,** and click on **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1630073732851.png" alt="" width="563"><figcaption></figcaption></figure>

7. In the **General Settings**, enter **"AutoRABIT"** in the **App name** field, upload the **AutoRABIT logo** and click on the **Next** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622988525880.png" alt="" width="375"><figcaption></figcaption></figure>

8. In the **Configure SAML** tab, do the following:
   1. **Single sign on URL:** Enter the URL in the following format: **\<instanceURL>/saml/SSO**. For example, if your instance is **https://pilot.autorabit.com/**, then the payload URL would be: _**https://pilot.autorabit.com/saml/SSO**_
   2. **Audience URI (SP Entity ID)**: Enter the URL in the following format: **\<instanceURL>/saml/metadata**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622989115676.png" alt="" width="375"><figcaption></figcaption></figure>

9. On the same screen, in the **Attribute Statements (optional)** panel, configure the following:

| Name  | Value      |
| ----- | ---------- |
| Email | user.email |

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1630078331670.png" alt="" width="563"><figcaption></figcaption></figure>

10. Click **Next** to continue.
11. Under **the Feedback** section, select the option: **I'm an Okta customer adding an internal app** and click the checkbox next to the text **"This is an internal application that we created"**, and click on the **Finish** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622989529850.png" alt="" width="563"><figcaption></figcaption></figure>

12. Navigate your mouse to the **Assignment** tab, click **Assign > Assign to People.**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990662547.png" alt="" width="563"><figcaption></figcaption></figure>
13. Next, select the listed **users** and click on **Assign**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990744508.png" alt="" width="375"><figcaption></figcaption></figure>

14. After you assign the user, click on **Save and Go Back** and then click  **Done**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990800814.png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990859106.png" alt="" width="375"><figcaption></figcaption></figure>

15. Go to the **Sign On** tab and click on **Identity Provider Metadata.**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990375044.png" alt="" width="375"><figcaption></figcaption></figure>
16. This will open up a new tab with some data. You must save this data in XML format on your own system. When you press **CTRL + S**, the data is downloaded in XML format.&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1630078468447.png" alt="" width="563"><figcaption></figcaption></figure>
17. You can also use the Identity Provider metadata URL link and use it to configure SSO with AutoRABIT instead of downloading the metadata XML file. To do so, right-click on the **Identity Provider metadata** and choose the **Copy link address** from the list.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622990558629.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1622991210813.png" alt="" width="563"><figcaption></figcaption></figure>

1. Now, login into your AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **My Account**
3. On the **My Account** page, go to the 3rd section: **SSO Configuration**
4. Browse for the metadata XML file that you have downloaded previously in your local machine and upload them.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616320872662.png" alt="" width="563"><figcaption></figcaption></figure>

1. SML configuration for OKTA is successfully configured in AutoRABIT. Now, the user can log in to AutoRABIT using OKTA. To do so, first sign out from your current AutoRABIT account.
2.  On your login screen, click on the **Single Sign On** button.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616320995956.png" alt="" width="563"><figcaption></figcaption></figure>
3. Enter your company's domain name. Click **Go**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616321064362.png" alt="" width="563"><figcaption></figcaption></figure>

4. This concludes SSO configuration with the AutoRABIT. You can now log in to the AutoRABIT from your Okta dashboard page directly.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1630074152773.png" alt="" width="375"><figcaption></figcaption></figure>
