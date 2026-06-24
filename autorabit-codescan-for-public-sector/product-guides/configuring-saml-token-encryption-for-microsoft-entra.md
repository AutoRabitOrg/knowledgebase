# Configuring SAML Token Encryption for Microsoft Entra

### Objective&#x20;

Implement SAML token encryption for CodeScan to enhance the security of SAML assertions in alignment with FedRAMP Moderate requirements. This setup involves retrieving the public key certiﬁcate from CodeScan’s SAML metadata and storing it in Microsoft Entra ID, enabling Entra ID to encrypt SAML assertions sent to CodeScan for authentication.

### Prerequisites

* Single Sign-On with Microsoft Entra ID already conﬁgured in CodeScan for the organization.
* CodeScan user with Org Admin access to view SAML connection settings.

### Obtaining a Public Key Certificate from CodeScan&#x20;

1. Access CodeScan as an Org Admin
   * In CodeScan, click the **Profile** icon on the right corner of the screen and select your organization.
2. Navigate to SAML Connections
   * In the menu, go to **Administration > SAML Connections**.
3. Retrieve the Metadata URL:
   * Locate the conﬁgured SAML connection and copy the Metadata URL.
4. Download or Access the Metadata XML Document
   * Open the Metadata URL in your browser.
   * Depending on your browser settings, the XML document may either be displayed directly in the browser or downloaded as a ﬁle.
   * If it displays in the browser, locate the `<md:KeyDescriptor use="encryption">` section and copy the content within the `<ds:X509Certiﬁcate>` tags. If it downloads automatically, open the XML ﬁle and ﬁnd the same section to copy the certificate content.
5. Extract the Certiﬁcate Content
   * The copied text from the `<ds:X509Certiﬁcate` tag is your Base64-encoded certiﬁcate.
   * This is the public key certiﬁcate you’ll need for conﬁguring SAML token encryption in Entra ID.

### Formatting the Certificate for Use&#x20;

1. To ensure compatibility with Microsoft Entra ID, format the certiﬁcate as an X.509 `.cer` file.
2. You can easily format the certiﬁcate using the online tool at [X.509 Certificate Format Online Tool | SAMLTool.com](https://www.samltool.com/format_x509cert.php).
   1. Paste the copied certiﬁcate content into the "X.509 cert" ﬁeld.
   2. Click the "Format X.509 Certiﬁcate" button.
   3. The tool will present the certiﬁcate in the required format, enclosed with `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` headers and footers.
   4. Select and copy the entire formatted certiﬁcate, including these headers and footers.
   5. Open a text editor, paste the formatted certiﬁcate content, and save the ﬁle with a `.cer` extension.
3. Your `.cer` ﬁle is now prepared for use in Entra ID to conﬁgure SAML token encryption for CodeScan.

### Importing the Encryption Certificate into Microsoft Entra ID&#x20;

To conﬁgure SAML token encryption, import the formatted `.cer` certiﬁcate into Microsoft Entra ID and ensure the correct signing settings are selected.

1. Log in to the Microsoft Entra Admin Center.
2. Navigate to your Enterprise Application.
3. On the application's page, select **Token encryption**.
4.  On the **Token encryption** page, select **Import Certiﬁcate** to import the `.cer` ﬁle created.<br>

    <figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption><p>Import Certificate screenshot</p></figcaption></figure>


5. Once the certiﬁcate is imported, activate encryption by selecting the ... next to the thumbprint status, and then select **Activate token encryption** from the options in the dropdown menu.
6. Select **Yes** to conﬁrm activation of the token encryption certiﬁcate.

### Configuring Certificate Signing Options in a SAML Token&#x20;

1. On the left pane of the application overview page, select **Single Sign-On**.
2. On the **Set Up Single Sign-On with SAML** page, ﬁnd the **SAML Signing Certiﬁcate** heading and select the **Edit** icon (pencil). The **SAML Signing Certiﬁcate** page will appear.
3. In the **Signing Option** drop-down list, choose **Sign SAML response and assertion**.
4. Select **Save** to apply the new SAML signing certiﬁcate settings.

### &#x20;(Optional) Confirming SAML Assertions Are Encrypted&#x20;

To conﬁrm the SAML assertions for the application are encrypted, perform the following steps:

1. Open a browser with developer tools and access CodeScan using your Entra ID credentials.
2. In the Developer Tools, go to the **Network** tab to capture network traﬃc during login.
3.  Look for a network request with `POST` data to the **application's ACS URL** (where the SAML assertion is sent).<br>

    <figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>


4. Go to the **Payload** section to view the SAML response.
5.  Look for the `SAMLResponse` ﬁeld, which contains the Base64-encoded SAML response.<br>

    <figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
6. Decode the SAML Response
   * Copy the `SAMLResponse` value and decode it using a Base64 decoder (many online tools, like SAMLTool, can decode the SAML response).
7. Verify Encryption
   * In the decoded SAML response, check for the presence of the `<EncryptedAssertion>` element. If assertions are encrypted, they will appear within this tag, and you won’t see the plain assertion content.<br>
