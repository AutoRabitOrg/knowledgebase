# GitLab Authentication using OAuth (CodeScan)

Connecting AutoRABIT (Codescan) to GitLab Enterprise requires a secure handshake based on the OAuth 2.0 Authorization Framework.

**Applies To**

* GitLab Enterprise Server (self-managed); not applicable to [GitLab](http://gitlab.com/) .

**Generate Client ID and Client Secret**

1. Log in to your GitLab Enterprise Server with an admin account.
2. Navigate to the **Admin Area** (click **Main menu › Admin**).
3. In the left sidebar, click **Applications**.
4. Click **New application**.
5. Configure:
   * **Name**: e.g., Codescan GitLab OAuth
   * **Redirect URI**: `<https://<Codescan_URL>>/_codescan/oauth2/authorize`
   * Check **Trusted** to bypass user consent.
   * Check **Confidential** to protect the client secret.
6. Select the **api** scope under Authorized Applications.
7. Click **Save application**.
8. Copy the **Application ID** (Client ID) and click **Copy** on the **Secret** field to get the Client Secret.

**FAQ**

| Issue                  | How to Fix                                            |
| ---------------------- | ----------------------------------------------------- |
| Mismatched credentials | Double-check clientId, clientSecret, and redirecturi. |
