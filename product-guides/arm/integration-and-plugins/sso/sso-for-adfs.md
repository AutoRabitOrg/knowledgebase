# SSO For ADFS

### Setting up Single Sign-On using Active Directory with ADFS and SAML 2.0 <a href="#setting-up-single-signon-using-active-directory-with-adfs-and-saml-20" id="setting-up-single-signon-using-active-directory-with-adfs-and-saml-20"></a>

#### Step 1 – Adding a Relying Party Trust <a href="#step-1-adding-a-relying-party-trust" id="step-1-adding-a-relying-party-trust"></a>

To set up the ADFS connection with AutoRABIT using a Relying Party Trust (RPT), follow the below steps:

1. Login to the **ADFS Server**.
2. Launch the **ADFS Management Console**.
3. Click on **“Add Relying Party Trust…”** from the **Actions** sidebar on the right.

<figure><img src="../../../../.gitbook/assets/image (56) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="488"><figcaption></figcaption></figure>

4. On the **Select Data Source** screen, select the last option: **Enter data about the relying party manually.**

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="465"><figcaption></figcaption></figure>

5. On the next screen, enter a **Display name** that you will recognize in the future.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. On the next screen, select **AD FS profile**.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="486"><figcaption></figcaption></figure>

7. On the next screen, leave the defaults.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="485"><figcaption></figcaption></figure>

8. On the next screen, check the box labeled: **Enable support for the SAML 2.0 WebSSO protocol**.
9. Enter the service URL. **For ex-** _pg.autorabit.com/saml/SSO_

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. Click **Next**.
11. On the next screen, add a Relying party trust identifier named **https://pg.autorabit.com/saml/metadata** and click **Add**.
12. On the next screen, leave the defaults.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="489"><figcaption></figcaption></figure>

13. On the next screen, select: **Permit all users to access this relying party**.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="485"><figcaption></figcaption></figure>

14. On the next screens, the wizard will display an overview of your settings. Click **Next**.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="479"><figcaption></figcaption></figure>

15. On the final screen use the **Close** button to exit and open the Claim Rules editor.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="488"><figcaption></figcaption></figure>

#### Step 2 – Creating Claim Rules <a href="#step-2-creating-claim-rules" id="step-2-creating-claim-rules"></a>

Once the Relying Party Trust exists, you can create the claim rules and update the Relying Party Trust with minor changes that are not set by the wizard.

1. By default, the Claim Rules editor opens once you created the trust.
2. To create a new rule, click on **Add Rule**.

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="386"><figcaption></figcaption></figure>

3. Select: **Send LDAP Attributes as Claims rule**.

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="485"><figcaption></figcaption></figure>

4.  On the next screen, using **Active Directory** as your attribute store, do the following:

    * From the LDAP Attribute column, select **E-Mail Addresses**.
    * From the Outgoing Claim Type, select **E-Mail Address**.

    <figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="378"><figcaption></figcaption></figure>
5. Click **OK** to save the new rule.
6. Create another new rule by clicking **Add Rule**.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="386"><figcaption></figcaption></figure>

7. Select: **Transform an Incoming Claim as the template**.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

8.  On the next screen:

    * Select **E-mail Address** as the Incoming Claim Type.
    * For Outgoing Claim Type, select **Name ID**.
    * For Outgoing Name ID Format, select **Email**.
    * Leave the rule to the default of **Pass through all claim values**.

    <figure><img src="../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="377"><figcaption></figcaption></figure>
9. Finally, click **OK** to create the claim rule, and then **OK** again to finish creating rules.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

10. Under **ADFS Management Console**, navigate to **Services > Endpoints** and find the URL to download the metadata XML file. See the screenshot attached.

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### Step 3: Configuring SSO in AutoRABIT <a href="#step-3-configuring-sso-in-autorabit" id="step-3-configuring-sso-in-autorabit"></a>

Now that your ADFS SSO implementation is set up, you’ll need to follow just a few more steps to configure SSO in your AutoRABIT account.

1. Log in to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **My Account**
3. On the **My Account** page, go to the **SSO Configuration** section.
4. Browse for the metadata XML file that you have downloaded previously in your local machine and upload them.

<figure><img src="../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Sign out from your AutoRABIT account.
6. Go to the AutoRABIT login page. This time you need to login via SSO, so, therefore, click on the option: **Single Sign On.**

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Enter the domain name and click on **Go**.
8. Next, you will be redirected to your custom domain URL where you need to enter the **username** and **password** to access the AutoRABIT.
