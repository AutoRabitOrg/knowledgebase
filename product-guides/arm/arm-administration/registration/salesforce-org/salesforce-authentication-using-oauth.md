# Salesforce Authentication using OAuth

The **Salesforce** platform supports the **OAuth 2.0 Authorization Framework**, allowing ARM to request access to Force.com resources on your behalf. To connect ARM to a Salesforce organization, you need the organization’s **Client ID** and **Client Secret**.

{% hint style="info" %}
**Important points**

* **Applies to:** self-hosted and dedicated-hosted ARM deployments  
* **Does not apply to:** shared-cloud deployments  
  * Shared-cloud customers use a pre-configured Salesforce connected app, so **client\_id** and **client\_secret** fields are hidden. For those environments, follow: [Adding a Salesforce Org connection via OAuth](./)
{% endhint %}

---

#### To get the Salesforce Client\_ID and Client\_Secret values <a href="#to-get-the-salesforce-clientid-and-clientsecret-values" id="to-get-the-salesforce-clientid-and-clientsecret-values"></a>

1. Log in to Salesforce as an **administrator**.  
2. In the user menu (upper-right), select **`Setup`**.  
3. In the left sidebar, expand **`App Setup > Create`**, then click **`Apps`**.  
4. Under **`Connected Apps`**, click **`New`**.  
5. In **`Basic Information`**, provide:  
   * **Connected App Name** and **API Name** – descriptive, unique names.  
   * **Contact Email** – your address for app notifications.  
6. In **`API (Enable OAuth Settings)`**, select **`Enable OAuth Settings`** and enter:  
   * **Callback URL** – `https://<ARM access URL>/oauth/_callback`  
     *Example: `https://preview.autorabit.com/oauth/_callback`*  
   * **Available OAuth Scopes** – add these to **Selected OAuth Scopes**:  
     * *Access and manage your data (api)*  
     * *Full access (full)*  
     * *Perform requests on your behalf at any time (refresh_token, offline_access)*  
7. Click **`Save`**.  
8. In the **`Connected Apps`** list, find the app you just created and click **`Manage`**.  
   * Click **`Edit`**.  
   * Under **`OAuth Policies`**, set **`Permitted Users`** to **All users may self-authorize**, then click **`Save`**.  
9. Return to **`Connected Apps`** and click the app name again.  
10. In **`API (Enable OAuth Settings)`**:  
    * Copy **`Consumer Key`** – this is your **client\_id**.  
    * Click **`Click to reveal`** next to **Consumer Secret**, copy the value – this is your **client\_secret**.  
11. During an on-premises ARM installation, open the file `rabit/org/oauth.properties` and update the values:  

    ```actionscript
    clientId=<Consumer Key>
    clientSecret=<Consumer Secret>
    redirecturl=<AutoRABIT application access URL>/oauth/_callback
    hosturl=<AutoRABIT application access URL>
    ```

---

### FAQ

#### Why am I unable to register my Salesforce Org using an OAuth connection? <a href="#why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection" id="why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection"></a>

1. **Connected app blocked** – In Salesforce, ensure the *AutoRABIT* connected app is **not** marked **Blocked**.  
2. **Missing permissions** – Check that the connected app has the required OAuth scopes and that the user profile can access it.  
3. **Invalid configuration** – Confirm the redirect URL, client ID, and secret in `oauth.properties` match the values in Salesforce.  

If you run ARM behind a proxy and see **“Username may not be null”**, verify the proxy credentials. A null proxy username causes this error.
