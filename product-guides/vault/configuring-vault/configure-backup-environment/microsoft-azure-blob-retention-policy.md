# Microsoft Azure Blob Retention Policy

## Overview <a href="#overview" id="overview"></a>

To manage Azure Blob retention policies via WebAPI, you must obtain the following credentials:

1. **Tenant ID**
2. **Client ID**
3. **Client Secret**
4. **Access Token**

These values are required to authenticate and interact with Azure endpoints for retention policy operations.

---

## What Is a Tenant and How to Get a Tenant ID in Azure? <a href="#what-is-tenant-and-how-to-get-a-tenant-id-in-azure" id="what-is-tenant-and-how-to-get-a-tenant-id-in-azure"></a>

A tenant represents your organization in Microsoft cloud services.

To get your **Tenant ID**:
1. Log in to the [Azure portal](https://portal.azure.com/).
2. Go to **Entra ID > Properties**.
3. Copy the value from the **Directory ID** field — this is your Tenant ID.

To create a new tenant:
1. Select **Create a resource**.
2. Search for and select **Entra ID**.
3. Provide a name for your new directory.
4. A **Tenant ID** will be auto-generated.

<figure>
  <img src="../../../../.gitbook/assets/image (121) (1).png" alt="Azure portal - create a new Entra ID tenant">
  <figcaption>Create New Tenant</figcaption>
</figure>

---

## What Is a Client ID and How to Create It? <a href="#what-is-client-id-and-how-to-create-it" id="what-is-client-id-and-how-to-create-it"></a>

A **Client ID** (or Application ID) identifies your app to Azure AD.

To generate it:
1. Go to your Azure directory.
2. Click **App registrations > New registration**.

<figure>
  <img src="../../../../.gitbook/assets/image (125) (1).png" alt="New App Registration" width="563">
  <figcaption>App Registration</figcaption>
</figure>

3. Select the **Single-tenant** option and click **Register**.

<figure>
  <img src="../../../../.gitbook/assets/image (126) (1).png" alt="Single tenant registration" width="544">
  <figcaption>Choose Single-Tenant</figcaption>
</figure>

4. Go to **Authentication**, select app type as **Web**, and configure redirect URI.

<figure>
  <img src="../../../../.gitbook/assets/image (127).png" alt="Authentication tab configuration" width="563">
  <figcaption>Configure Authentication</figcaption>
</figure>

<figure>
  <img src="../../../../.gitbook/assets/image (128).png" alt="Add redirect URI" width="563">
  <figcaption>Web Redirect URI</figcaption>
</figure>

5. The app will now show an **Application ID** — this is your **Client ID**.

<figure>
  <img src="../../../../.gitbook/assets/image (129).png" alt="Application ID shown in portal" width="563">
  <figcaption>Client ID (Application ID)</figcaption>
</figure>

---

## Add a Client Secret <a href="#add-a-client-secret" id="add-a-client-secret"></a>

To create a **Client Secret**:
1. Open your app under **App registrations**.
2. Go to **Certificates & secrets > New client secret**.

<figure>
  <img src="../../../../.gitbook/assets/image (130).png" alt="New Client Secret">
  <figcaption>Create Client Secret</figcaption>
</figure>

3. Enter a description, select a duration, and click **Add**.
4. Copy the **Client Secret ID** and **Value** — they are shown only once.

<figure>
  <img src="../../../../.gitbook/assets/image (131).png" alt="Secret ID and Value" width="563">
  <figcaption>Client Secret Values</figcaption>
</figure>

5. Go to **IAM** settings and assign roles to your app via **Add role assignment**.

<figure>
  <img src="../../../../.gitbook/assets/image (132).png" alt="Add IAM Role">
  <figcaption>Role Assignment</figcaption>
</figure>

---

## Generate Access Token <a href="#generate-access-token" id="generate-access-token"></a>

To generate an **Access Token**, follow these steps:

### Step 1: Request Authorization Code

Send a GET request:

```http
GET https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?
client_id=YOUR_CLIENT_ID
&response_type=code
&redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F
&response_mode=query
&scope=openid%20offline_access%20https%3A%2F%2Fgraph.microsoft.com%2Fmail.read
&state=12345
&code_challenge=YOUR_CODE_CHALLENGE
&code_challenge_method=S256
# Microsoft Azure Blob Retention Policy

## Overview <a href="#overview" id="overview"></a>

To manage Azure Blob retention policies via WebAPI, you must obtain the following credentials:

1. **Tenant ID**
2. **Client ID**
3. **Client Secret**
4. **Access Token**

These values are required to authenticate and interact with Azure endpoints for retention policy operations.

---

## What Is a Tenant and How to Get a Tenant ID in Azure? <a href="#what-is-tenant-and-how-to-get-a-tenant-id-in-azure" id="what-is-tenant-and-how-to-get-a-tenant-id-in-azure"></a>

A tenant represents your organization in Microsoft cloud services.

To get your **Tenant ID**:
1. Log in to the [Azure portal](https://portal.azure.com/).
2. Go to **Entra ID > Properties**.
3. Copy the value from the **Directory ID** field — this is your Tenant ID.

To create a new tenant:
1. Select **Create a resource**.
2. Search for and select **Entra ID**.
3. Provide a name for your new directory.
4. A **Tenant ID** will be auto-generated.

<figure>
  <img src="../../../../.gitbook/assets/image (121) (1).png" alt="Azure portal - create a new Entra ID tenant">
  <figcaption>Create New Tenant</figcaption>
</figure>

---

## What Is a Client ID and How to Create It? <a href="#what-is-client-id-and-how-to-create-it" id="what-is-client-id-and-how-to-create-it"></a>

A **Client ID** (or Application ID) identifies your app to Azure AD.

To generate it:
1. Go to your Azure directory.
2. Click **App registrations > New registration**.

<figure>
  <img src="../../../../.gitbook/assets/image (125) (1).png" alt="New App Registration" width="563">
  <figcaption>App Registration</figcaption>
</figure>

3. Select the **Single-tenant** option and click **Register**.

<figure>
  <img src="../../../../.gitbook/assets/image (126) (1).png" alt="Single tenant registration" width="544">
  <figcaption>Choose Single-Tenant</figcaption>
</figure>

4. Go to **Authentication**, select app type as **Web**, and configure redirect URI.

<figure>
  <img src="../../../../.gitbook/assets/image (127).png" alt="Authentication tab configuration" width="563">
  <figcaption>Configure Authentication</figcaption>
</figure>

<figure>
  <img src="../../../../.gitbook/assets/image (128).png" alt="Add redirect URI" width="563">
  <figcaption>Web Redirect URI</figcaption>
</figure>

5. The app will now show an **Application ID** — this is your **Client ID**.

<figure>
  <img src="../../../../.gitbook/assets/image (129).png" alt="Application ID shown in portal" width="563">
  <figcaption>Client ID (Application ID)</figcaption>
</figure>

---

## Add a Client Secret <a href="#add-a-client-secret" id="add-a-client-secret"></a>

To create a **Client Secret**:
1. Open your app under **App registrations**.
2. Go to **Certificates & secrets > New client secret**.

<figure>
  <img src="../../../../.gitbook/assets/image (130).png" alt="New Client Secret">
  <figcaption>Create Client Secret</figcaption>
</figure>

3. Enter a description, select a duration, and click **Add**.
4. Copy the **Client Secret ID** and **Value** — they are shown only once.

<figure>
  <img src="../../../../.gitbook/assets/image (131).png" alt="Secret ID and Value" width="563">
  <figcaption>Client Secret Values</figcaption>
</figure>

5. Go to **IAM** settings and assign roles to your app via **Add role assignment**.

<figure>
  <img src="../../../../.gitbook/assets/image (132).png" alt="Add IAM Role">
  <figcaption>Role Assignment</figcaption>
</figure>

---

## Generate Access Token <a href="#generate-access-token" id="generate-access-token"></a>

To generate an **Access Token**, follow these steps:

### Step 1: Request Authorization Code

Send a GET request:

```http
GET https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?
client_id=YOUR_CLIENT_ID
&response_type=code
&redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F
&response_mode=query
&scope=openid%20offline_access%20https%3A%2F%2Fgraph.microsoft.com%2Fmail.read
&state=12345
&code_challenge=YOUR_CODE_CHALLENGE
&code_challenge_method=S256
