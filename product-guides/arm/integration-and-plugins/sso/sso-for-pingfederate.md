# SSO For PingFederate

**PingFederate** is a federation server that provides identity management, web single sign-on, and API security on your own premises. PingFederate supports all of the current identity standards including SAML, WS-Federation, WS-Trust, OAuth, and OpenID Connect, so users can securely access any applications they require with a single identity using any device.

### Setting up Single Sign-On using PingFederate <a href="#setting-up-single-signon-using-pingfederate" id="setting-up-single-signon-using-pingfederate"></a>

#### Step 1: Creating a SP connection <a href="#step-1-creating-a-sp-connection" id="step-1-creating-a-sp-connection"></a>

1. Log in to PingFederate.
2. Go to the **Identity Provider** page in PingFederate, then click **Create New** under SP Connections.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582776753.png" alt=""><figcaption></figcaption></figure>

3. Check the **Browser SSO Profiles** connection template on the **Connection Type** page and click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582791982.png" alt=""><figcaption></figcaption></figure>

4.  Check the **Browser SSO** option on the **Connection Options** page and click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582807454.png" alt=""><figcaption></figcaption></figure>
5. Select File as the method for importing metadata and click Choose file to choose the SSO metadata on the **Import Metadata** tab. Click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582821335.png" alt=""><figcaption></figcaption></figure>

6.  Enter the subdomain (including the https://protocol handler) in the **Partner’s Entity ID (Connection ID)** field, your desired **Connection Name**, and enter the SAML Endpoint URL into the **Base URL** field, then scroll down to the bottom of the page and click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582834611.png" alt=""><figcaption></figcaption></figure>
7.  Click **Configure Browser SSO** on the Browser SSO page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582852167.png" alt=""><figcaption></figcaption></figure>
8. Check the **IdP-Initiated SSO** and **SP-Initiated SSO** options on the SAML Profiles page, then click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582864953.png" alt=""><figcaption></figcaption></figure>

9. Enter your desired **Assertion Lifetime** and click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582878102.png" alt=""><figcaption></figcaption></figure>

10. Click **Configure Assertion Creation** on the **Assertion Creation** page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582892006.png" alt=""><figcaption></figcaption></figure>
11. Choose the **Standard Identity Mapping** option and click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582907681.png" alt=""><figcaption></figcaption></figure>
12. Change the **Subject Name Format** for the **SAML\_SUBJECT** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**. Add the **Attribute Name Format** for the **Email** as **urn:oasis:names:tc:SAML:2.0:attrname-format:basic**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582922222.png" alt=""><figcaption></figcaption></figure>
13. Click **Next**.
14. Click **Map New Adapter Instance** on the Authentication Source Mapping page.
15. Choose your desired **Adapter Instance** and click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582937470.png" alt=""><figcaption></figcaption></figure>

16. Under the **Mapping Method**, select the option as shown below.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582950892.png" alt="" width="563"><figcaption></figcaption></figure>
17. Click **Add Attribute Source** under **Attribute Sources & User Lookup.**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582966175.png" alt=""><figcaption></figcaption></figure>
18. Specify the attribute store's details to use it in your configuration and click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582978562.png" alt=""><figcaption></figcaption></figure>
19. Configure your directory search under the **LDAP Directory Search** heading. Click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623582991368.png" alt=""><figcaption></figcaption></figure>
20. Select **Attribute Encoding Type** as **"Base64"** for **Mail Attribute**. Click **Next**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583006377.png" alt=""><figcaption></figcaption></figure>
21. Select a filter for extracting data from your directory.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583018424.png" alt="" width="563"><figcaption></figcaption></figure>

22. Under **Attribute Contract Fulfillment**, enter the below source and values for **Email** and **SAML\_SUBJECT attribute contracts.**
    1. For **Email** attribute contract, source as **LDAP** and Value as **mail.**
    2.  For **SAML\_SUBJECT** attribute contract, source as **LDAP** and Value as **Subject DN.**

        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583034237.png" alt=""><figcaption></figcaption></figure>
23. Click **Next**.
24. View the **Attribute source** summary page on the next screen.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583047427.png" alt="" width="563"><figcaption></figcaption></figure>
25. On the next screen, leave the defaults.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583059333.png" alt=""><figcaption></figcaption></figure>

26. On the next screen, select: **SEND USER TO SP USING DEFAULT LIST OF ATTRIBUTES**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583072503.png" alt=""><figcaption></figcaption></figure>
27. Under **Attribute Contract Fulfillment**, enter the below source and values for **Email** and **SAML\_SUBJECT** attribute contracts.
    1. For **Email** attribute contract, source as **Adapter** and Value as **mail.**
    2.  For **SAML\_SUBJECT** attribute contract, source as **Adapter** and Value as **username.**

        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583086985.png" alt=""><figcaption></figcaption></figure>
28. On the next screen, view the **IDP Adapter Mapping** summary.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583101416.png" alt=""><figcaption></figcaption></figure>
29. On the next screen, leave the defaults.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583114624.png" alt=""><figcaption></figcaption></figure>

31. View the summary information for your **Assertion Creation** configuration on the next screen.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583127963.png" alt=""><figcaption></figcaption></figure>
32. On the next screen, leave the defaults.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583141083.png" alt=""><figcaption></figcaption></figure>

33. On the next screen, click **Configure Protocol Settings**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583154548.png" alt=""><figcaption></figcaption></figure>

34. Enter the **Protocol settings** as shown.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583169810.png" alt=""><figcaption></figcaption></figure>

35. On the next screen, select the **SAML bindings** as shown below.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583273415.png" alt=""><figcaption></figcaption></figure>
36. Select the **Artifact lifetime** as 60 seconds.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583287490.png" alt=""><figcaption></figcaption></figure>

37. On the next screen, enter the remote party URL. For ex- [https://pg.autorabit.com/saml/](https://pg.autorabit.com/saml/SSO)

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583302142.png" alt=""><figcaption></figcaption></figure>
38. Click **Next**.
39. On the next screen, select: **Always Sign Assertion**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583316887.png" alt=""><figcaption></figcaption></figure>

40. Select **Encryption policy** as None. Click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583330178.png" alt=""><figcaption></figcaption></figure>

41. View the summary information for your protocol settings configuration.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583553731.png" alt="" width="563"><figcaption></figcaption></figure>
42. On the next screen, leave the defaults.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583574233.png" alt="" width="563"><figcaption></figcaption></figure>

43. &#x20;View the summary information for your **browser SSO** configuration.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583587001.png" alt="" width="563"><figcaption></figcaption></figure>
44. &#x20;Click **Configure Browser SSO**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583599750.png" alt=""><figcaption></figcaption></figure>

45. &#x20;On the next screen, click **Configure Credentials.**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583624557.png" alt=""><figcaption></figcaption></figure>

46. &#x20;Click **Next**.
47. On the next screen, click **Configure** beside **Send to your partner** section.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583643399.png" alt=""><figcaption></figcaption></figure>
48. On the next screen, select the below checkboxes:
    1. **HTTP BASIC**&#x20;
    2.  **PERFORM VALIDATION ON PARTNERS SSL SERVER CERTIFICATE WHEN SSL USED**

        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583657558.png" alt=""><figcaption></figcaption></figure>
49. On the next screen, specify the **username** and **password** to use to authenticate your partner's SOAP endpoint.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583670253.png" alt=""><figcaption></figcaption></figure>

50. View the summary of SOAP authentication on the next screen. Click **Done**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583682307.png" alt=""><figcaption></figcaption></figure>
51. Click on **Configure** beside **Receive from your partner** section.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583690786.png" alt=""><figcaption></figcaption></figure>
52. On the next screen, select the below checkboxes:

    * **HTTP BASIC**
    * **REQUIRE SSL**



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583712161.png" alt=""><figcaption></figcaption></figure>
53. On the next screen, specify the **username** and **password** to use to authenticate your partner's SOAP endpoint.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583725710.png" alt=""><figcaption></figcaption></figure>

54. View the summary of SOAP authentication on the next screen. Click **Done**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583738614.png" alt=""><figcaption></figcaption></figure>
55. On the next screen, click **Done**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583750255.png" alt=""><figcaption></figcaption></figure>

56. Select the key/certificates for your **digital signature** settings. Click **Done**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583764706.png" alt=""><figcaption></figcaption></figure>
57. View the summary information for your Credentials configuration on the next screen. Click **Done**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583777638.png" alt=""><figcaption></figcaption></figure>

58. On the next screen, leave the defaults. Click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583791002.png" alt=""><figcaption></figcaption></figure>

59. Under the **Activation & Summary** screen, view the summary information for your SP connection. Click **Done**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583804316.png" alt=""><figcaption></figcaption></figure>

60. Find your recently created SP connection in the **Identity Provider** screen.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583818297.png" alt=""><figcaption></figcaption></figure>
61. Click on **Manage All**.
62. Click on **Select Action** and choose **Export Metadata** for your SP connection.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583832675.png" alt=""><figcaption></figcaption></figure>
63. From the list of certificates on the next screen, choose the certificate to use for signing the connection. Click **Next**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583847005.png" alt=""><figcaption></figcaption></figure>

64. On the next screen, click on **Export**. The metadata XML file will get downloaded to your local machine.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583861102.png" alt="" width="563"><figcaption></figcaption></figure>

#### Step 2: Configuring SSO in AutoRABIT <a href="#step-2-configuring-sso-in-autorabit" id="step-2-configuring-sso-in-autorabit"></a>

Now that your PingFederate SSO implementation is set up, you’ll need to follow just a few more steps to configure SSO in your AutoRABIT account.

1. Now, login into your AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **My Account**
3. On the My Account page, go to the **SSO Configuration** section.
4. Browse for the metadata XML file that you have downloaded previously in your local machine and upload them.
5.  Sign out from your AutoRABIT account. On the login page, click on **Single Sign On** button.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619513303123.png" alt=""><figcaption></figcaption></figure>
6. Enter the domain name and click on **Go**.
7.  Next, you will be redirected to your custom domain URL where you need to enter the **PingFederate's** credentials i.e., username and password to access the AutoRABIT.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623583905973.png" alt="" width="375"><figcaption></figcaption></figure>
