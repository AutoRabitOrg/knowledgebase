# Configure Multi-Proxy

{% hint style="info" %}
This article is for the **Org Administrators** in particular. The actions discussed in this article are not available to general users. This article is only applicable if your system is running behind a proxy.
{% endhint %}

ARM sends the proxy details in the request headers whenever connected to an outside customer network.

1. Log in to ARM with your credentials.
2. Go to **Admin** > **My Account** > **Proxy Settings Configuration**.
3. Click on **Create New Proxy** button.
4. A new dialog box appears where you are required to fill in the proxy-related details such as:
   * **Proxy Name:** Enter the proxy name. This will be used as a reference.
   * **Proxy Host:** Enter the proxy address in this field.
   * **Proxy Port:** Give the Proxy Port of the mail server. If unspecified, Port 25 will be used as a default.
   * **Credential:** If your Proxy server is configured with your credential, you can select it from the dropdown field or leave it blank by default. Also, if you like to add a new credential that you like to configure with the proxy server, you can do so by using the **Create Credential** button.
5. Click on the![](<../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon to enter the proxy URL. Multiple URLs can be configured for the same proxy server.
6. Save the proxy configuration steps using the![](<../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon. Failing to do so will make you repeat the above steps.
7. You can add multiple proxy details in this section. To add another proxy server details, click on **Create New Proxy** and repeat steps 4 to 6. To add another proxy server details based on already configured proxy settings, you can use the **Clone** (![](<../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon. To delete a proxy setting configured earlier, use the **Delete** (![](<../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon.
