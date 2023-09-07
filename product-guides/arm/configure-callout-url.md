# Configure Callout URL

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The callout URL lets you call another service from the ARM application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly.

### Where can I find Configure Callout URL option? <a href="#where-can-i-find-configure-callout-url-option" id="where-can-i-find-configure-callout-url-option"></a>

A new section, i.e., **Callout URL**, is available for the following CI jobs:

* **Deploy from Salesforce org**
* **Deploy from Salesforce org with a version control backup**
* **Deploy from version control**
* **Deploy Salesforce-DX (SFDX) source from** [**version control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/)
* **Install an unlocked package from a version control branch**

### Configuring Callout URL <a href="#configuring-callout-url" id="configuring-callout-url"></a>

![Callout URL](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616337834894.png)

1. Select the **Configure Callout URL** checkbox under the **Callout URL** section.
2. Choose the **Callout Type**:
   1. **Pre-Deployment**: ARM will perform the HTTP request before the deployment begins, once the build is successful.&#x20;
   2. **Post-Deployment**: By default, ARM will perform the HTTP request after the deployment is completed, regardless of whether it is successful. To run the HTTP request based on whether the deployment is a success or a failure, select the respective option:
      * **On Success**
      *   **On Failure**\


          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1649920517262.png" alt=""><figcaption></figcaption></figure>
3. The callout URL method is selected as **Post** by default.
4. In the **URL** box, enter the target URL endpoint of the HTTP request.
5. Select the **Authorization** type:
   1.  **Basic**: Authenticate the target URL via standard method-username and password

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606249239527.png" alt=""><figcaption></figcaption></figure>
   2.  **Custom**: Authenticate the connection via **username: API Token**

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606249292080.png" alt=""><figcaption></figcaption></figure>
   3. **OAuth**: ARM supports the **Client Credentials** as a grant type for OAuth 2.0 authentication. To add an OAuth 2.0 provider, fill in the below details:
      * **URL (required):** OAuth 2.0 provider URL
      * **Client ID (required):** The client ID that your callout service uses to identify the ARM application
      * **Client Secret (required):** The client secret that your callout service uses to authenticate the identity of the ARM applicationThe **Client Secret** field is hidden during your current CI job editing, preventing you from updating the secret key. But you can insert a new secret key (if required).
      * **Access token URL (required):** The URL that the client uses to obtain an access token given an authorization code
      * **Scope (optional):** Specifies the level of access that the ARM application is requesting
      *   **Grant Type (required)**: The **Grant Type** is selected as **Client Credentials** by default

          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616337902322.png" alt=""><figcaption></figcaption></figure>
6. The **Content-Type** header describes the format in which the body of your request is being sent. For example, the body of your requests can be sent as **JSON** or **XML**.
   1. To send JSON in a request, use **application/json** and add your content in the field provided.
   2.  To send XML in a request, use **application/xml** and add your content in the field provided.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606249385222.png" alt=""><figcaption></figcaption></figure>
7. To add a custom header, click on the **Add Header** button and enter the keys and their value. Multiple adding of keys and values are allowed.

&#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606934340480.png" alt=""><figcaption></figcaption></figure>

Default headers is set as _**"Accept" :"application/json", "Content-Type":"application/json"**_&#x20;

1. Click on **Save**.

### Dynamic Parameters <a href="#dynamic-parameters" id="dynamic-parameters"></a>

| Parameter     | Description                 |
| ------------- | --------------------------- |
| {projectName} | Name of your CI Job         |
| {buildNumber} | Build Number of your CI Job |
| {sforgName}   | Name of your Salesforce Org |

{% hint style="info" %}
**Note:** You must specify values for dynamic parameters before executing the query, and the types of the specified values must match the expected types.
{% endhint %}

### Viewing the Log Report <a href="#viewing-the-log-report" id="viewing-the-log-report"></a>

#### Callout Type: Pre-Deployment  <a href="#callout-type-predeployment" id="callout-type-predeployment"></a>

You can view the detailed log report under the **Build Log** section.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606937200234.png)

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606937302112.png)

#### Callout Type: Post-Deployment  <a href="#callout-type-postdeployment" id="callout-type-postdeployment"></a>

View the detailed log report under the **Deployment Log** section.

![Deployment Log](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606937403377.png)

![Deploy Log](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1606937542566.png)
