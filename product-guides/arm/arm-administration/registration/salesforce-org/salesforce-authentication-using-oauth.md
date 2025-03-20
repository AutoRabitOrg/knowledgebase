# Salesforce Authentication using OAuth

The **Salesforce** platform implements the **OAuth 2.0 Authorization Framework**, so users can authorize applications to access **Force.com** resources. When configuring ARM and Salesforce source, you must know the **Client\_ID** and **Client\_Secret** token values for the Salesforce organization you want to index.

{% hint style="info" %}
**Important Points to Consider**:

* The following article is
  * **applicable for:** self-hosted and dedicated hosted users
  * **not applicable for:** shared cloud users
* For share cloud customers, ARM has a pre-configured connected app via salesforce; therefore, _client\_id_ and _client\_secret_ fields are not exposed in the user interface. For more information, please refer to the link: [Adding a Salesforce Org connection via OAuth](./)
{% endhint %}

#### To get the Salesforce Client\_ID and Client\_Secret values <a href="#to-get-the-salesforce-clientid-and-clientsecret-values" id="to-get-the-salesforce-clientid-and-clientsecret-values"></a>

1. Log in to Salesforce as an administrator.&#x20;
2. In the drop-down list of the account (in the upper-right corner), select **`Setup`**.
3. In the navigation menu on the left, under **`App Setup`**, expand **`Create`**, then click **`Apps`**.
4. On the **`Connected Apps`** page, click the **`New`** button.
5. On the **`New Connected App`** page, fill in the following required fields under **`Basic Information`**:
   * Enter meaningful names in the Connected App Name and API Name boxes.
   * Enter your email in the Contact Email box to receive messages from this application.
6. Go to **`API (Enable OAuth Settings)`**, and select **`Enable OAuth Settings`**.
   * In the **`Callback URL`** field, enter _https://\<ARM access URL>/oauth/\_callbac&#x6B;_&#x46;or example, _https://preview.autorabit.com/oauth/\_callback_\
     Depending on which OAuth flow you use, this is typically the URL that a user’s browser is redirected to after successful authentication.
   * In the **Available OAuth Scopes** list, select the following items:
     * Access and manage your data (API)
     * Full access (full)
     * Perform requests on your behalf at any time (refresh\_token, offline\_access)
     * and click **Add** for each to appear in the **Selected OAuth Scopes** list.
7. Click the **`Save`** button to save the new **`Connected App`**.
8. In the **`Connected Apps`** list, find the **`App`** you just created and click **`Manage`**.
   * On the page that opens, click the **`Edit`** button.
   * Under **`OAuth policies`**, select **`All users may self-authorize`** in the **`Permitted Users`** list, then click the **`Save`** button.
9. Return to the **`Connected Apps`** list, and click the app you created.
10. In the page that appears for your new connected app, in the **`API (Enable OAuth Settings)`**&#x73;ection:
    * Copy the **`Consumer Key`** value and paste it into a secure reference document of your choice. The Consumer Key is the _client\_id_.
    * Next to **`Consumer secret`**, click **`Click to reveal`**, copy the value that appears, and paste it into your secure reference document. The Consumer secret is the _client\_secret_.
11. Open the _oauth.properties_ file in the _.rabit/org/oauth.properties_ directory and update the _client\_id_ and _client\_secret_ token during on-premise installation.

    ```actionscript
    clientId=<Consumer Key>
    clientSecret=<Consumer Secret>
    redirecturl=<AutoRABIT application access URL>/oauth/_callback
    hosturl==<AutoRABIT application access URL>
    ```

### FAQ:

### Why am I unable to register my Salesforce Org using an OAuth connection? <a href="#why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection" id="why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection"></a>

1. Verify in the user Salesforce Org if the AutoRABIT Connected App is **“Blocked”** and unblock it.
2. Verify in user Salesforce Org if there are any specific permissions set for the Connected App.
3. Verify whether the redirect URL, client ID, and the secret key in **oauth.properties** file (path: .rabit/org/oauth.properties) are valid.

If the user is on a proxy-enabled server and receives an error such as **"Username may not be null"**, the proxy credentials must be validated. If the proxy username is set to **"null"**, the above error will occur.
