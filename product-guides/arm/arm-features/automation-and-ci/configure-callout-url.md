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
4. Enter the endpoint in the **URL** field.
5. Select an **Authorization** type:
   - **Basic**: Standard username and password.

     <figure><img src="../../../../.gitbook/assets/image (1192).png" alt=""></figure>

   - **Custom**: Uses `username: API Token`. Prefix the token with the keyword `token`.

     <figure><img src="../../../../.gitbook/assets/Screenshot 2024-10-31 at 12.18.51 PM.png" alt="" width="563"></figure>

   - **OAuth**: Supports **Client Credentials** grant type. Required fields:
     - **URL** (OAuth 2.0 provider)
     - **Client ID**
     - **Client Secret** (hidden when editing an existing CI job)
     - **Access Token URL**
     - **Scope** (optional)
     - **Grant Type**: Defaults to **Client Credentials**

6. The **Content-Type** header defines the request body format (e.g., JSON or XML):
   - Use `application/json` for JSON requests.
   - Use `application/xml` for XML requests.

   <figure><img src="../../../../.gitbook/assets/image (1194).png" alt=""></figure>

7. To add custom headers, click **Add Header** and define key-value pairs. You can add multiple.

   - Default headers include:  
     `"Accept": "application/json", "Content-Type": "application/json"`

   <figure><img src="../../../../.gitbook/assets/image (1195).png" alt=""></figure>

8. Click **Save**.

### Dynamic Parameters <a href="#dynamic-parameters" id="dynamic-parameters"></a>

| Parameter     | Description                 |
| ------------- | --------------------------- |
| `{projectName}` | Name of your CI Job         |
| `{buildNumber}` | Build Number of your CI Job |
| `{sforgName}`   | Name of your Salesforce Org |

{% hint style="info" %}
**Note:** You must specify values for dynamic parameters before executing the query, and their types must match expected formats.
{% endhint %}

### Viewing the Log Report <a href="#viewing-the-log-report" id="viewing-the-log-report"></a>

#### Callout Type: Pre-Deployment <a href="#callout-type-predeployment" id="callout-type-predeployment"></a>

View detailed logs under the **Build Log** section.

<figure><img src="../../../../.gitbook/assets/image (1196).png" alt=""></figure>

<figure><img src="../../../../.gitbook/assets/image (1197).png" alt=""></figure>

#### Callout Type: Post-Deployment <a href="#callout-type-postdeployment" id="callout-type-postdeployment"></a>

Logs are available under the **Deployment Log** section.

<figure><img src="../../../../.gitbook/assets/image (1198).png" alt=""></figure>

<figure><img src="../../../../.gitbook/assets/image (1199).png" alt=""></figure>
