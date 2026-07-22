# API Access

To interact with the API, you need to have a unique, personal access token. This will be used to authenticate yourself within the API.

The token is the equivalent of the user name & password pair. Once generated, it identifies your own account. So you should be careful with it and not disclose it to any untrusted party (or application).

### Generate your API Access Token <a href="#generate-your-api-access-token" id="generate-your-api-access-token"></a>

To generate your access token, you should:

1. Go to the **API Tokens** screen under the **Admin** module.
2. Click on the **Create API Token** button to generate a new token.

<figure><img src="../../../.gitbook/assets/image (750).png" alt=""><figcaption></figcaption></figure>

3. Enter the **API token name** on the next screen.
4.  Note down your newly generated token - you are going to need it soon.

    <figure><img src="../../../.gitbook/assets/image (752).png" alt=""><figcaption></figcaption></figure>

    * For security reasons, it is not possible to view the token after closing the creation dialog. If necessary, create a new token. Max of **10 tokens** is permitted for each user license.
    * You should store the token securely, as with any password.

### Token Deactivation <a href="#token-deactivation" id="token-deactivation"></a>

If a user account gets deactivated in AutoRABIT, the API Token will get deactivated at the same time. In some cases, AutoRABIT will need to revoke or invalidate tokens.

**For example**, when a user logs out of an ARM application. If you revoke a token, it can be reapproved any time before it expires.

<figure><img src="../../../.gitbook/assets/image (753).png" alt=""><figcaption></figcaption></figure>
