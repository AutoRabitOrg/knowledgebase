# Creating and Configuring Proxy Servers

Point to Note:

The proxy configuration settings is applicable for **on-premise users** only. Currently not supported for shared instance users.

### Introduction <a href="#introduction" id="introduction"></a>

This article describes the basic configuration of a proxy server. You will learn how to pass a request from Vault to proxied servers over different protocols, and modify request headers that are sent to the proxied server.

Vault sends the proxy details in the request headers whenever getting connected to an outside customer network.

### Permissions <a href="#permissions" id="permissions"></a>

* The proxy configuration settings is for **on-premise users** only. Support for shared instances users are currently not applicable.
* Only **System Admins** can configure the proxy settings for your organization.
* The proxy can be configured for **AWS storage environment** only.

### How to configure Proxy <a href="#how-to-configure-proxy" id="how-to-configure-proxy"></a>

Follow the steps given below to configure a proxy server:

1. Log in to the Vault account.
2. Go to **Settings** > **Proxy Configuration Settings**.
3. Click on **Create New Proxy**.
4. A new dialog box appears where you are required to fill in the proxy related details such as:
   * **Proxy Name**: Enter the proxy name. This will be used as a reference.
   * **Proxy Host**: The hostname of the HTTP proxy server. _Ex- 127.0.0.1_
   * **Proxy Port**: The port number of the HTTP proxy server. _Ex- 3128_
   * Select your AWS storage environment (AWS-S3 or AWS-KMS ) to create a storage connection with them.
   *   Enter the **Proxy URL**. Click **Add**. Multiple URLs can be configured for the same proxy server.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-SEJIREF2.png" alt=""><figcaption></figcaption></figure>
5. Click **Submit**. You'll redirected to the **Proxy Configuration Settings** homepage where you can find your recently created proxy on the top of the list.
6.  Using the **Edit** (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-PLXWIV5X.png)) icon, you can later edit the proxy setups or **Delete** (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZITSKUBN.png)) any proxy that is no longer needed.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-3Q4C35QU.png" alt=""><figcaption></figcaption></figure>
