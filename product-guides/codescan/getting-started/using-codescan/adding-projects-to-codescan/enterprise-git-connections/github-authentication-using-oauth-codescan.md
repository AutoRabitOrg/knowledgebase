# GitHub Authentication using OAuth (CodeScan)

Connecting AutoRABIT (Codescan) to GitHub Enterprise requires a secure handshake based on the OAuth 2.0 Authorization Framework.

**Applies To**

* Self-hosted and dedicated-hosted Codescan deployments.

**Generate Client ID and Client Secret**

1. Log in to your GitHub Enterprise Server with an admin account.
2. Click your profile section (upper-right) and select **Developer settings**.
3. In the left sidebar, click **OAuth Apps**.
4. Click **New OAuth App** (or **Register a new application**).
5. Fill in:
   * **Application name**: e.g., Codescan GitHub OAuth
   * **Homepage URL**: e.g., \<https://git.enterprise.local.com>
   * **Application description** (optional)
   * **Authorization callback URL**: \<https://\<Codescan\_URL>>/\_codescan/oauth2/authorize
6. Click **Register application**.
7. On the app’s settings page, copy the **Client ID** and click **Reveal** next to **Client Secret** to copy it.

**FAQ:**

| **Issue**              | **How to Fix**                                        |
| ---------------------- | ----------------------------------------------------- |
| Mismatched credentials | Double-check clientId, clientSecret, and redirecturl. |
