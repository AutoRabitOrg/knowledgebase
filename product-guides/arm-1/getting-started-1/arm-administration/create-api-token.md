# API Token Manager

Important Note: This article is for **Org Administrators** in particular. The actions discussed in the article are not available to general users. &#x20;

### Overview <a href="#overview" id="overview"></a>

An API token is a unique identifier of an application requesting access to your service. API tokens are used to authenticate requests to the ARM APIs.&#x20;

### Obtaining your Access Token  <a href="#obtaining-your-access-token" id="obtaining-your-access-token"></a>

You must have a unique personal access token to interact with the API. This is used to authenticate yourself in the API.&#x20;

Important Note: The token is the equivalent of the user name and password pair. Once generated, it identifies your account. So it's best to be careful and not disclose it to any untrusted party or application.

To generate your access token, you should:

1.  Hover your mouse over the **`Settings`** tile and select the option: **`API Token Manager.`**<br>

    <figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

\
<br>

2.  Click on the **`Create API Token`** button to generate a new token.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
3. Enter the API **`Token Name`** on the next screen.&#x20;
4. Click **`Create`**.\
   \
   ![](<../../../../.gitbook/assets/image (2).png>)<br>
5.  Write down your newly generated token as you will need it soon.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** For security reasons, viewing the token after closing the creation dialog is not possible. If necessary, create a new token. A maximum of 10 tokens are permitted for each user license. It is best to store the token securely, as with any password.
{% endhint %}

### Token Deactivation <a href="#token-deactivation" id="token-deactivation"></a>

If an ARM user account is deactivated, the API Token will be deactivated simultaneously. In some cases, ARM needs to revoke or invalidate tokens, for example, when a user logs out of the ARM application. If you revoke a token, it can be reapproved any time before it expires.\
<br>

<figure><img src="../../../../.gitbook/assets/image (2395).png" alt=""><figcaption></figcaption></figure>
