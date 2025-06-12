# Salesforce Authentication Using OAuth

Connecting AutoRABIT (ARM) to Salesforce requires a secure handshake based on the **OAuth 2.0 Authorization Framework**.  
By creating a **connected app** in Salesforce and supplying its **Client ID** and **Client Secret** to ARM, you grant the platform scoped access—no passwords stored, and you can revoke tokens anytime from Salesforce.

> **Applies to**: *self-hosted* and *dedicated-hosted* ARM deployments  
> **Not needed for**: *shared-cloud* customers (a pre-configured connected app is already in place).

If you’re on shared cloud, skip the steps below and follow **Adding a Salesforce Org connection via OAuth** in the shared-cloud guide.

---

## Generate Client ID and Client Secret <a href="#to-get-the-salesforce-clientid-and-clientsecret-values" id="to-get-the-salesforce-clientid-and-clientsecret-values"></a>

1. **Log in to Salesforce** with an **administrator** account.  
2. Click **Setup** (gear icon, upper-right).  
3. In the sidebar: **App Setup › Create › Apps**.  
4. Under **Connected Apps**, click **New**.  
5. In **Basic Information** fill:  
   * **Connected App Name** / **API Name** – something like `AutoRABIT OAuth`.  
   * **Contact Email** – your admin address.  
6. In **API (Enable OAuth Settings)**:  
   * Check **Enable OAuth Settings**.  
   * **Callback URL** – `https://<ARM_URL>/oauth/_callback`  
     *Example: `https://preview.autorabit.com/oauth/_callback`*  
   * **Selected OAuth Scopes** – move these from *Available* to *Selected*:  
     * **Access and manage your data (api)**  
     * **Full access (full)**  
     * **Perform requests on your behalf at any time (refresh_token, offline_access)**  
7. Click **Save**.  
8. Back in **Connected Apps**, click **Manage** next to the app, then **Edit**.  
   * Under **OAuth Policies**, set **Permitted Users** to **All users may self-authorize**.  
   * Click **Save**.  
9. Open the app again; under **API (Enable OAuth Settings)** copy:  
   * **Consumer Key** → **clientId**  
   * Click **Click to reveal** next to **Consumer Secret** → **clientSecret**  
10. Edit `rabit/org/oauth.properties` (on-prem ARM only) and insert:  

    ```properties
    clientId=<Consumer Key>
    clientSecret=<Consumer Secret>
    redirecturl=<ARM_URL>/oauth/_callback
    hosturl=<ARM_URL>
    ```

---

## FAQ

### Why can’t I register my Salesforce org with OAuth? <a href="#why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection" id="why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection"></a>

| Issue | How to Fix |
| ----- | ---------- |
| **Connected app is blocked** | In Salesforce Setup › *Connected Apps OAuth Usage*, ensure the AutoRABIT app status is **Not Blocked**. |
| **Missing scopes or profile access** | Verify the three scopes listed above are still selected and the user profile has **Connected App Access**. |
| **Mismatched credentials** | Double-check `clientId`, `clientSecret`, and `redirecturl` in `oauth.properties`. |
| **Proxy error: “Username may not be null”** | If ARM sits behind a proxy, ensure the proxy username/password are set; null values trigger this error. |
