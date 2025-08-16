# Salesforce Org

You must register the organization to use any Salesforce Org functionality inside ARM. When you register your Salesforce organization in ARM, ARM connects to your organization with the required permissions.

By default, ARM connects to orgs using the secure OAuth method (our recommended approach). You can also connect to orgs using username/password connections if you need to.

### Adding a Salesforce Org connection via OAuth <a href="#adding-a-salesforce-org-connection-via-oauth" id="adding-a-salesforce-org-connection-via-oauth"></a>

1. Log in to your ARM account.&#x20;
2.  Go to the **`Settings > SF Org Mgmt.`** page.\


    <figure><img src="../../../../../.gitbook/assets/image (1942).png" alt="" width="231"><figcaption></figcaption></figure>
3.  From the **`SF Org Mgmt.`** screen, click on the **`Register Salesforce Org`** button.\


    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 9.13.41 PM.png" alt=""><figcaption></figcaption></figure>
4. Enter the **`Salesforce Org Name`**.
5. Select the **`Salesforce Org Type`** from the drop-down (_Developer_, _Integration_, _QA_, _UAT_, _Production_).
6. Select the **`Environment`** from the drop-down (_Production or Development Edition_, _Sandbox_, _Pre-Release_, _Custom URL_).
7. **`Salesforce Org URL`** is predefined based on the Environment selected.
8. Select **`Access type`** as **`OAuth`** as the authentication method.
9.  Click **`Validate & Save`** to proceed through the OAuth flow and allow ARM to connect to your Salesforce Org.\


    <figure><img src="../../../../../.gitbook/assets/image (1943).png" alt="" width="375"><figcaption></figcaption></figure>
10. Click **`Allow`** when prompted to grant ARM access to the Salesforce Org.
11. The org will now be added to your list of saved connections. It will appear in the list of available orgs via the dropdown for future comparisons and automation jobs.

{% hint style="info" %}
**Important Note:** If your Salesforce Org is configured with nCino objects, you can select the **`Is nCino Installed`** checkbox. The nCino logo is added for each nCino configured Salesforce Org for easier identification from other Salesforce Org.
{% endhint %}

### Connecting to a Salesforce Org using username/password <a href="#connecting-to-a-salesforce-org-using-usernamepassword" id="connecting-to-a-salesforce-org-using-usernamepassword"></a>

1. Go to the **`Settings > SF Org Mgmt.`** page.
2. From the **`SF Org Mgmt.`** screen, click on the **`Add`** button.
3. Enter the **`Salesforce Org Name`**.
4. Select the **`Salesforce Org Type`** from the drop-down (_Developer_, _Integration_, _QA_, _UAT_, _Production_).
5. Select the **`Environment`** from the drop-down (_Production or Development Edition_, _Sandbox_, _Pre-Release_, _Custom URL_).
6. Select **`Access Type`** as **`Standard`** as the authentication method.
7. Enter the **`User Name`** and **`Password`**.
8. Enter the **`Security Token`**&#x20;
9.  Click **`Validate & Save`** to proceed through the OAuth flow and allow ARM to connect to your Salesforce Org.\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1944).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** If your Salesforce Org is configured with nCino objects, you can select the **`Is nCino Installed`** checkbox. The nCino logo is added for each nCino configured Salesforce Org for easier identification from other Salesforce Org.
{% endhint %}

### What is Salesforce Security Token, and How Do I Find It? <a href="#what-is-salesforce-security-token-and-how-do-i-find-it" id="what-is-salesforce-security-token-and-how-do-i-find-it"></a>

Your Salesforce security token is a case-sensitive alphanumeric key used with a password to access Salesforce via API. The token aims to improve the security between Salesforce users and Salesforce.com in the case of a compromised account. It ensures, among other things, that if a user’s account credentials are compromised, a third party cannot access Salesforce.

#### Losing the security token <a href="#losing-the-security-token" id="losing-the-security-token"></a>

If you can’t remember your security token and have deleted the email containing the token, the only way to retrieve it is by resetting the token. Salesforce does not provide an option to view your token within the web application; the only option is resetting it.

#### Getting the Security Token for Your Salesforce Account <a href="#getting-the-security-token-for-your-salesforce-account" id="getting-the-security-token-for-your-salesforce-account"></a>

When you create a Salesforce account, Salesforce sends an email message from support@salesforce.com with the subject: _salesforce.com security token confirmation_ to the email address associated with the account. This email message contains the Security Token for the account and is the only place where you can find the Security Token value. When you change the account password, the security token is regenerated (the previous one expires), and a similar email is sent.

To get the security token for your Salesforce account, In the mailbox for the email address associated with the Salesforce account, look for the latest email message received from _support@salesforce.com_ with the subject: _salesforce.com security token confirmation_.&#x20;

If you cannot find the latest email with the security token, reset the security token:&#x20;

1. Log in to Salesforce using the Salesforce account.
2. In the User Menu, select **`Setup`**.
3. In the menu on the left, under **`Personal Setup`**, expand **`My Personal Information`**, then click **`Reset My Security Token`**. Follow the instructions on the screen.
4. A new email message will be sent.
5. Open the message and then copy the **`Security Token value`**.

{% hint style="info" %}
**Important Note:** We recommend saving this email in a secure location, so you don’t have to reset your security token whenever needed.
{% endhint %}

### Edit Salesforce Org details after registration <a href="#edit-salesforce-org-details-after-registration" id="edit-salesforce-org-details-after-registration"></a>

You can change the **`Environment`** type, the **`Access Type`**, or both.

1. From the screen, choose the desired environment and access types from the respective dropdown fields.
2. To edit the **`User Name`**, ensure that the **`Access type`** is set as **`Standard`**.
3. Click **`Save`** or **`Test Connection`**, and you will see one of the following confirmation messages:
   * If you change the **`Environment type`**  or **`Access Type`**
   * If you change the **`Environment`** type and also the **`Access Type`**\
     \
     \


<figure><img src="../../../../../.gitbook/assets/image (1945).png" alt="" width="375"><figcaption></figcaption></figure>

4. Click **`Change`** to complete the request. Click **`Keep Current`** to close the confirmation message without changing the details.

### **FAQ**

### How do I update or change the username in all of the Salesforce Orgs specified in AutoRABIT? <a href="#how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au" id="how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au"></a>

To update the username on all registered orgs, re-authenticate the orgs in **Admin > SF Org Management** page.
