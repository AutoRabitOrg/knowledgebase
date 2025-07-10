# Creating and Configuring Proxy Servers

{% hint style="info" %}
**Note:** The proxy configuration settings apply to **on-premise users** only. This feature is currently **not supported for shared instance users**.
{% endhint %}

### Introduction <a href="#introduction" id="introduction"></a>

This guide details how to configure a proxy server within Vault. It explains how to forward requests from Vault to proxied servers across various protocols and how to modify request headers sent to these servers.

Vault includes proxy details in the request headers when connecting to external customer networks.

### Permissions <a href="#permissions" id="permissions"></a>

- Applicable **only for on-premise users**. Not supported for shared instance users.
- Only **System Admins** can configure proxy settings.
- Proxy can be set up **only for AWS storage environments**.

### How to Configure Proxy <a href="#how-to-configure-proxy" id="how-to-configure-proxy"></a>

Follow these steps to configure a proxy server:

1. Log in to your Vault account.
2. Navigate to **Settings > Proxy Configuration Settings**.
3. Click **Create New Proxy**.
4. In the dialog box, fill in the following proxy details:

    - **Proxy Name**: A name to reference the proxy.
    - **Proxy Host**: The hostname of the HTTP proxy server (e.g., `127.0.0.1`).
    - **Proxy Port**: The HTTP proxy server's port number (e.g., `3128`).
    - Choose your **AWS storage environment**: either **AWS-S3** or **AWS-KMS** to establish the storage connection.
    - Enter the **Proxy URL**, then click **Add**. You can configure multiple URLs for a single proxy.

<figure><img src="../../../.gitbook/assets/image (139).png" alt="Dialog box for creating a new proxy server in Vault" width="434"><figcaption>Proxy configuration form</figcaption></figure>

5. Click **Submit**. You'll be redirected to the **Proxy Configuration Settings** homepage. The newly created proxy appears at the top of the list.

6. Use the **Edit** icon (![Edit icon](../../../.gitbook/assets/image (66) (1) (1) (1) (1) (1) (1) (1) (1) (1).png)) to modify proxy settings, or the **Delete** icon (![Delete icon](../../../.gitbook/assets/image (67) (1) (1) (1) (1) (1) (1) (1) (1) (1).png)) to remove a proxy configuration.

<figure><img src="../../../.gitbook/assets/image (140).png" alt="List of configured proxies in Vault" width="563"><figcaption>Configured proxies list</figcaption></figure>
