# Parallel Processor

The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.

### About Parallel Processor <a href="#about-parallel-processor" id="about-parallel-processor"></a>

The **Parallel Processor** feature allows you to configure POST requests to be fired before or after a deployment request is triggered to Salesforce. For example, to send notifications to the slack channel post a CI Job is triggered.

### Where can I find this feature in the AutoRABIT application? <a href="#where-can-i-find-this-feature-in-the-autorabit-application" id="where-can-i-find-this-feature-in-the-autorabit-application"></a>

When you're triggering a new CI job, look for the **Configure Parallel Processor** function under the **Deploy > On Successful Deployment** section.

<figure><img src="../../../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**&#x20;

This feature is currently available for the following CI Jobs:

1. Deploy from Salesforce Org
2. Deploy from Salesforce Org with a Version Control backup
3. Deploy from Version Control
4. Deploy SFDX source from Version Control
5. Install an Unlocked Package from a Version Control Branch
{% endhint %}

### Configuring Parallel Processor <a href="#configuring-parallel-processor" id="configuring-parallel-processor"></a>

1. Select the checkbox: **Configure Parallel Processor**
2. Next, fill in the below details:
   * **URL Path (required):** The target URL endpoint of the HTTP request&#x20;
   * **Client Id (required):** The client ID that your callout service uses to identify the AutoRABIT application
   * **Client Secret (required):** The client secret that your callout service uses to authenticate the identity of the AutoRABIT applicationThe **Client Secret** field is hidden during the editing of your current CI job, preventing you from updating the secret key. But you can insert a new secret key (if required).
   * **Access token URL (required):** The URL that the client uses to obtain an access token given an authorization code
   * **Scope (optional):** Specifies the level of access that the AutoRABIT application is requesting
   * **Grant Type (required)**: Client Credentials auto-selected by default
   * **Version (required):** Enter the version here
3. Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
4.  The **Content-Type** header describes the format in the body of your request is being sent in. For example, the body of your requests can be sent as **JSON** or **XML**.

    * To send **JSON** in a request, use **application/json** and add your content in the body provided
    * To send **XML** in a request, use **application/xml** and add your content in the body provided

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
5. **Dynamic URL Parameters:** AutoRABIT allows you to include the various variables from your AutoRABIT organization, for example, the name of the CI job, build number, etc

**Dynamic Parameters:**

| Parameter                | Description                            |
| ------------------------ | -------------------------------------- |
| <p>{projectName}<br></p> | <p>Name of the CI Job<br></p>          |
| <p>{buildNumber}<br></p> | <p>Build Number of your CI Job<br></p> |
| <p>{sforgName}<br></p>   | <p>Name of your Salesforce Org<br></p> |

{% hint style="info" %}
**Note:** You must specify values for dynamic parameters before executing the query, and the types of the specified values must match the expected types.
{% endhint %}

6. **Request API Version (required):** Enter the API versions
7. To add a custom header, click on the **Add Header** button and enter the keys and the value to it. Multiple adding of keys and values are allowed.&#x20;

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Default headers is set as _**"Accept" :"application/json", "Content-Type":"application/json"**_&#x20;

8. **Poll Duration (Mins):** This allows you to define the polling duration in minutes for the job execution. This field is mandatory. AutoRABIT will perform the HTTP request based on the poll duration chosen and if a 200 OK is returned, it will continue with the next step. If the 200 response code is not seen within the given time frame, You will be shown a timeout message in the log file.
9. **Poll Interval (Mins):** Time-bound between two consecutive API calls, for example, 1minute, 5minute. This field is mandatory.&#x20;
10. Click on **Save**.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
