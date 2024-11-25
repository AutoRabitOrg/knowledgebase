# SSO for OKTA

This article explains how to configure Single Sign-On (SSO) in VAULT with Okta as your SAML 2.0 Identity Provider. When SSO is enabled, by default users and groups logging into VAULT are redirected to the Okta login page. After successful authentication, they are redirected to the VAULT Dashboard.

### Add VAULT Application to Okta <a href="#add-vault-application-to-okta" id="add-vault-application-to-okta"></a>

First, configure Okta to provide the sign-on information for the [VAULT](https://www.autorabit.com/products/vault-data-backup-recovery/) environment.

To add the VAULT application to Okta:

1. Sign in to Okta. You must have the Applications **Admin** permission.
2. If you don’t have an Okta organization, you can create a free Okta Developer Edition organization here: [https://developer.okta.com/signup/](https://developer.okta.com/signup/)
3. The home page will appear when you log in to Okta.

<figure><img src="../../../../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

4. From the main menu, go to **Applications > Add Application.**

<figure><img src="../../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

5. Click on the **Create App Integration** button.

<figure><img src="../../../../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

6. In the next auto-populated dialog box, select the second option i.e., **SAML 2.0,** and click on the **Next** button.

<figure><img src="../../../../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

7. In the **General Settings**, enter **"VAULT"** in the **App name** field, upload the **VAULT logo** and click on the **Next** button.

<figure><img src="../../../../.gitbook/assets/image (157).png" alt="" width="500"><figcaption></figcaption></figure>

8.  In the **Configure SAML** tab,&#x20;

    * **Single sign on URL:** Enter the URL in the following format: **\<instanceURL>/ARVault/saml/SSO**. For example, if your instance is **https://vault-qa.autorabit.com**, then the payload URL would be: **https://vault-qa.autorabit.com/ARVault/saml/SSO**
    * **Audience URI (SP Entity ID):** Enter the URL in the following format: **\<instanceURL>/ARVault/saml/metadata**

    <figure><img src="../../../../.gitbook/assets/image (158).png" alt="" width="560"><figcaption></figcaption></figure>
9. On the same screen, in the **Attribute Statements (optional)** panel, configure the following:

| Name                       | Value                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| firstname                  | user.firstName                                                                                                                                                                                                                                                                                                                                                                                              |
| lastname                   | user.lastName                                                                                                                                                                                                                                                                                                                                                                                               |
| customerid                 | Enter your Vault's Customer Id. (You'll find your customer id under the **Profile** section in your Vault account; refer to Step 23 for sample image attachment)                                                                                                                                                                                                                                            |
| restrictAutoCreationOfUser | <p>For <strong>Yes</strong>, a new user account won't be created within Vault even if the user is already registered with the OKTA service provider. The user is not permitted access to Vault if the account is not created in Vault.<br><br>For <strong>No</strong>, the restriction is revoked, and a new user account gets created in Vault, and the user will be able to access the Vault feature.</p> |



<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664778866036.png" alt="" width="563"><figcaption></figcaption></figure>

10. Click **Next** to continue.
11. Under the **Feedback** section, select the option: **"I'm an Okta customer adding an internal app"** and **"This is an internal application that we created"**, and click on the **Finish** button.

<figure><img src="../../../../.gitbook/assets/image (161).png" alt="" width="497"><figcaption></figcaption></figure>

12. Navigate your mouse to the **Assignment** tab, and click **Assign > Assign to People**.

<figure><img src="../../../../.gitbook/assets/image (162).png" alt="" width="477"><figcaption></figcaption></figure>

13. Next, select the listed **users** and click on **Assign**. After you assign the user click **"Save and Go Back"** and then click **Done**.

<figure><img src="../../../../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (166).png" alt="" width="443"><figcaption></figcaption></figure>

14. Here, you can see the assignment status.

<figure><img src="../../../../.gitbook/assets/image (167).png" alt="" width="497"><figcaption></figcaption></figure>

15. Go to the **Sign On** tab and click on **Identity Provider Metadata**.

<figure><img src="../../../../.gitbook/assets/image (168).png" alt="" width="478"><figcaption></figcaption></figure>

16. This will open up a new tab with some data. You must save this data in XML format on your own system. When you press **CTRL + S**, the data is downloaded in XML format.

<figure><img src="../../../../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

17. You can also use the Identity Provider metadata URL link and use it to configure SSO with Vault instead of downloading the metadata XML file. To do so, right-click on the **Identity Provider** [**metadata**](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) and choose the **Copy link address** from the list.

<figure><img src="../../../../.gitbook/assets/image (171).png" alt=""><figcaption></figcaption></figure>

18. Now, login into your **VAULT** account.
19. Hover your mouse over the Setting, go to the **SSO Configuration** sectio&#x6E;**.**
20. &#x20;Give a name for the SSO configuration and select how you would like to configure the metadata

    * For **Metadata URL**, you need to enter the URL link that you captured earlier (Refer to _Step 17_)
    * For **Metadata File**, browse for the metadata XML file you saved on your local machine and upload it. Click **Activate**.

    <figure><img src="../../../../.gitbook/assets/image (172).png" alt="" width="524"><figcaption></figcaption></figure>
21. SML configuration for OKTA is successfully configured in [VAULT](https://knowledgebase.autorabit.com/vault/docs/vault). Now, the user can log in to VAULT using SSO.Disable Login with Vault credentialsTurn the slide toggle to the left to use SSO for login to your Vault application instead of the default username and password. This will allow you to access your Vault account via SSO.
22. On your login screen, click **Login with SSO**.

<figure><img src="../../../../.gitbook/assets/image (173).png" alt="" width="364"><figcaption></figcaption></figure>

23. Enter your **Customer ID**. You'll find your Customer ID under the **Profile** section in your Vault account.

<figure><img src="../../../../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (175).png" alt=""><figcaption></figcaption></figure>

24. Finally, click on **Sign in.**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1625143930301.png" alt="" width="375"><figcaption></figcaption></figure>

25. This concludes SSO configuration with the Vault.
26. &#x20;Go to your OKTA dashboard page and click on the Vault icon to access the account.

<figure><img src="../../../../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Troubleshooting**:

Vault throws the following error when a user tries to log into Vault via SSO: _"Your user is not available in the account with provided customer id. Please contact the administrator to create a user for you in the account"_

The error usually occurs if:

1. The user details are not assigned inside OKTA to login into the Vault application.
2. The administrator has set the **restrictAutoCreationOfUser** to **Yes** inside **Attribute Statements** while configuring OKTA SSO. If it is set to Yes, the user is not permitted access to Vault if the account is not created in Vault.&#x20;
{% endhint %}
