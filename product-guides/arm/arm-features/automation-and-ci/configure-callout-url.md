# Configure Callout URL

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The callout URL lets you call another service from the ARM application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly.

### Where can I find Configure Callout URL option? <a href="#where-can-i-find-configure-callout-url-option" id="where-can-i-find-configure-callout-url-option"></a>

A new section, i.e., **Callout URL**, is available for the following CI jobs:

- **Deploy from Salesforce org**
- **Deploy from Salesforce org with a version control backup**
- **Deploy from version control**
- **Deploy Salesforce-DX (SFDX) source from** [**version control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/)
- **Install an unlocked package from a version control branch**

### Configuring Callout URL <a href="#configuring-callout-url" id="configuring-callout-url"></a>

<figure><img src="../../../../.gitbook/assets/image (1190).png" alt=""></figure>

1. Select the **Configure Callout URL** checkbox under the **Callout URL** section.
2. Choose the **Callout Type**:
   - **Pre-Deployment**: ARM performs the HTTP request before the deployment starts (after a successful build).
   - **Post-Deployment**: By default, ARM performs the HTTP request after the deployment completes. You can further specify:
     - **On Success**
     - **On Failure**

     <figure><img src="../../../../.gitbook/assets/image (1191).png" alt=""></figure>

3. The callout method defaults to **POST**.
4. Enter the endpoint i
