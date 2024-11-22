# Microsoft Azure Blob Retention Policy

### Overview <a href="#overview" id="overview"></a>

Azure Blob retention policy management using WebAPI needs to be created using the following details to successfully hit an API endpoint and complete a retention policy update/create.&#x20;

1. **Tenant ID**
2. **Client ID**
3. **Client secret**
4. **Access Token**

### **What Is a Tenant and How Do I Get a Tenant ID in Azure?** <a href="#what-is-tenant-and-how-to-get-a-tenant-id-in-azure" id="what-is-tenant-and-how-to-get-a-tenant-id-in-azure"></a>

A tenant represents your organization and helps you manage a specific instance of Microsoft cloud services for your internal and external users.

Log in to the Azure portal and navigate to Entra ID and choose the properties on the left side pane. On the right side pane, you will get your account-related information along with a field named **Directory ID**. Under that field, you will have a text box with an alphanumeric value that can be copied from the text box. This is your Tenant ID.  In this case, the **Tenant ID** is the **Directory ID**.

If you are doing a new setup and do not have any existing tenant, then follow the steps below to create a new tenant:

1. Login to Azure portal
2. Select **Create a resource** from the portal.

<figure><img src="../../../../.gitbook/assets/image (121) (1).png" alt=""><figcaption></figcaption></figure>

3. Search & choose **Entra ID.**
4. Create a directory by providing a name.&#x20;
5. A **Tenant ID** is automatically created.

### **What is a client ID and how do I create one?** <a href="#what-is-client-id-and-how-to-create-it" id="what-is-client-id-and-how-to-create-it"></a>

Client ID is nothing but Application ID that uses to associate our application with Azure AD at runtime. To delegate Identity and Access Management functions to Entra ID, an application must be registered with an Azure AD tenant. When you register your application with Entra ID, you are creating an identity configuration for your application that allows it to integrate with Entra ID.

### **App Registration process** <a href="#app-registration-process" id="app-registration-process"></a>

1. Go to your directory and choose **App registrations** on the left pane and select **New registration** in the right pane.

<figure><img src="../../../../.gitbook/assets/image (125) (1).png" alt="" width="563"><figcaption></figcaption></figure>

2. Register an application by choosing the **single-tenant** option.

<figure><img src="../../../../.gitbook/assets/image (126) (1).png" alt="" width="544"><figcaption></figcaption></figure>

3. Click **Register**.&#x20;
4. Once the app is registered, choose **Authentication** on the left side pane and feed in-app type as a web app and configure the details in the right pane.

<figure><img src="../../../../.gitbook/assets/image (127).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (128).png" alt="" width="563"><figcaption></figcaption></figure>

5. **“MyTestAPP”** Application ID from the Azure portal is successfully created.

<figure><img src="../../../../.gitbook/assets/image (129).png" alt="" width="563"><figcaption></figcaption></figure>

### **Add a Client Secret** <a href="#add-a-client-secret" id="add-a-client-secret"></a>

The client secret, known also as an _application password_, is a string value your app can use in place of a certificate to identify itself.

1. Select your application in **App registrations** in the Azure portal.
2. Select **Certificates & secrets > New client secret**.

<figure><img src="../../../../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

3. Add a description for your client secret.
4. Select a duration.
5. Select **Add**.
6. Copy the Client Secret ID and Value- it's _never displayed again_ after you leave this page. The Key-Value along with the Secret ID is required for sign-in the application.

<figure><img src="../../../../.gitbook/assets/image (131).png" alt="" width="563"><figcaption></figcaption></figure>

7. Next, grant storage container access to the app. To do so, go to **IAM** and **“Add role assignment”** for the app.

<figure><img src="../../../../.gitbook/assets/image (132).png" alt=""><figcaption></figcaption></figure>

### Generate Access Token <a href="#generate-access-token" id="generate-access-token"></a>

To generate the access token, first, you need to get an authorization code. You need to provide all the above-acquired IDs and hit the API endpoint for generating the authorization code.

**Example:**

https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?

client\_id=6731de76-14a6-49ae-97bc-6eba6914391e

\&response\_type=code

\&redirect\_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F

\&response\_mode=query

\&scope=openid%20offline\_access%20https%3A%2F%2Fgraph.microsoft.com%2Fmail.read

\&state=12345

\&code\_challenge=YTFjNjI1OWYzMzA3MTI4ZDY2Njg5M2RkNmVjNDE5YmEyZGRhOGYyM2IzNjdmZWFhMTQ1ODg3NDcxY2Nl

\&code\_challenge\_method=S256

#### Request for Access Token <a href="#request-for-access-token" id="request-for-access-token"></a>

Once you acquire an authorization code and have been granted permission by the user, you can redeem the code for an access token to the desired resource. Do this by sending a POST request to the token endpoint.

For more information, please visit the following link and see the documentation provided by Microsoft at [https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id).
