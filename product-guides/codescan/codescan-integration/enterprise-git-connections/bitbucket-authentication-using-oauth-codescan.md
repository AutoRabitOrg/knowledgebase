# Bitbucket Authentication using OAuth (CodeScan)

Connecting AutoRABIT (Codescan) to Bitbucket Data Center requires a secure handshake based on the OAuth 2.0 Authorization Framework.

**Applies To**

* Bitbucket Data Center (self-managed) with Atlassian Application Links enabled.

**Generate Client ID and Client Secret**

1. Log in to your Bitbucket Data Center instance with an admin account.
2. Go to **Main menu › Admin**, then **Administration › Applications › Application links**.
3. Click **Create link**, choose **External application**, and set **Direction** to **Incoming**.
4. Name the link (e.g., Codescan Bitbucket OAuth) and enter the **Redirect URL**: `<https://<Codescan_URL>>/_codescan/oauth2/authorize`.
5. Select **Repositories - Admin** under application permissions.
6. Click **Save**.
7. Copy the generated **Client ID** and **Client Secret** immediately.

**FAQ**

| Issue                  | How to Fix                                            |
| ---------------------- | ----------------------------------------------------- |
| Mismatched credentials | Double-check clientId, clientSecret, and redirecturl. |
