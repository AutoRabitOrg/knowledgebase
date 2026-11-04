---
description: Create an API key for the CLI, VS Code and CI pipelines, and keep it safe
---

# Create and Manage API Keys

An API key lets the CodeScan CLI, the VS Code extension and your CI pipelines connect to CodeScan without a username and password. This article explains how to create a key, use it and replace it.

{% hint style="info" %}
**Note:** Only administrators can create API keys: <mark style="background-color:yellow;">**Tenant manager**</mark> and <mark style="background-color:yellow;">**ACA admin**</mark>. If **`API Keys`** is not visible in your account, ask an administrator to create a key and send it to you securely.
{% endhint %}

### Creating an API Key

1. Open **`CodeScan API Keys`**.&#x20;
2. Select **`Create CodeScan API Key`**.
3. Create **`Name`**, select **`Expiry Period`**, click **`Create`**.
4. Copy the key and store it somewhere safe, such as your password manager or your CI system's secret store.

{% hint style="warning" %}
**Important Note:** The key is shown only once. If you lose it, create a new key.
{% endhint %}

CodeScan API keys start with `codescan_`.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-10-16 at 10.14.30.png" alt="" width="375"><figcaption></figcaption></figure>

To check which credential is in use and whether CodeScan accepts it, run:

```bash
codescan auth status
```

### Rotating a Key

Rotate a key before it expires, on a regular schedule, or whenever you think it may have been exposed. Rotating creates a new key for the same entry.&#x20;

1. On the **`CodeScan API Keys`** page, find the key and select **`Rotate`**.
2. Choose when the new key expires: pick a preset in **`Expires In`**, such as _1 week_, or pick any future date in **`Expiration Date`**.
3. Select **`Rotate`**.
4. The window shows **CodeScan API Key Rotated** and the new key. Select **`Copy Key`**, store the key safely, then select **`Close`**.
5. Update every place that uses the key: developers' CLI and VS Code sign-ins, and your CI secret store.

{% hint style="warning" %}
**Important Note:** As with a new key, the rotated key is shown only once. Copy it before you close the window.
{% endhint %}

### Revoking a Key

Revoke a key when it is no longer needed, for example when a pipeline is retired or a developer leaves the team.

1. On the **`CodeScan API Keys`** page, find the key and select **`Revoke`**.
2. Confirm.

A revoked key stops working, and anything still using it is rejected.

### When a Key Expires

Every key has an expiry date, shown in the **`Expires`** column. After that date, CodeScan rejects the key. To keep a pipeline or a developer connected, rotate the key before it expires.&#x20;

### Recommendations

* Create a separate key for each pipeline, integration or developer, and name it clearly. You can then rotate or revoke one without affecting the others.
* Check **`Last Used At`** from time to time. A key that hasn't been used in months is a candidate for revoking.
* Use shorter expiry periods for personal keys, and rotate pipeline keys on a regular schedule.
* Store keys in your CI system's secret store, never in your repository or pipeline files.
* On laptops, prefer `codescan config`, which keeps the key in the keychain rather than in a shell profile.

### Troubleshooting

| Problem                              | What to do                                                                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`API Keys`** is not in the web app | Your account is not an administrator. Ask an administrator to create the key.                                                                          |
| CodeScan rejected the API key        | The key is missing, wrong, expired or revoked. Create a new key, then sign in again with `codescan auth login --api-key` or update `CODESCAN_API_KEY`. |
| The scan tries to reach `localhost`  | `CODESCAN_APP_URL` is not set and no URL has been saved with `codescan config`. Set your CodeScan URL.                                                 |

### Next Step

Connect VS Code

### Related Articles

* Sign Up and Sign In
* Users, Roles and Permissions
* System Requirements
