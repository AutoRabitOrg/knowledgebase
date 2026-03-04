# How to Set Up Guard via ECA

{% hint style="info" %}
Salesforce has introduced External Client Apps as the new standard for org connections. Learn more [here](https://knowledgebase.autorabit.com/fundamentals/announcements/salesforce-oauth-external-client-app-eca-transition).
{% endhint %}

Before registering your org in Guard, please complete the following configuration in Salesforce.

### Create an External Client App <a href="#step-1-create-an-external-client-app" id="step-1-create-an-external-client-app"></a>

1. Navigate to **Salesforce Setup**.
2. Search for **External Client Apps**.
3. Click **New External Client App**.

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

4. Enter the required details:

**Basic Information**

* **External Client App Name**
* **API Name** (auto-populated)
* **Contact Email**

**Enable OAuth Settings**

1. Select **Enable OAuth Settings**.
2. Provide the **Callback URL** in the format:&#x20;

_{$isntancename}/oauth/\_callback_

3. Add the following OAuth scopes:

* Access the identity URL service (id, profile, email, address, phone)
* Full access (full)
* Manage user data via APIs (api)
* Manage user data via Web browsers (web)
* Perform requests at any time (refresh\_token, offline\_access)

**Flow Enablement**

Enable the following:

* **Authorization Code and Credentials Flow** _(Sub-options are not required.)_

**Security Settings**

* Keep the first 2 options checked
* **Uncheck**: _Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows_

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**Save and Activate**

Save the application and activate it.

### Collect Client Credentials <a href="#step-2-collect-client-credentials" id="step-2-collect-client-credentials"></a>

After activation, copy the following credentials:

* **Consumer ID (Consumer Key)**
* **Consumer Secret**

{% hint style="info" %}
Newly generated credentials may take up to 10 minutes to become active. If verification fails, wait and retry.
{% endhint %}

### Register a New Salesforce Org Using OAuth via ECA <a href="#part-2-register-a-new-salesforce-org-using-oauth-via-eca" id="part-2-register-a-new-salesforce-org-using-oauth-via-eca"></a>

#### Step 1: Open Org Registration <a href="#step-1-open-org-registration" id="step-1-open-org-registration"></a>

Navigate to:

**Salesforce Orgs → Add New Org**

#### Step 2: Select Connection Type <a href="#step-2-select-authentication-type" id="step-2-select-authentication-type"></a>

Choose:

**External Client App**

#### Step 3: Enter Required Details <a href="#step-3-enter-required-details" id="step-3-enter-required-details"></a>

Provide the following information:

* Org Name
* Org Type
* Org Purpose (Production / Sandbox)
* Client ID
* Client Secret

Click **Login with Salesforce**.

#### Step 4: Authorize in Salesforce <a href="#step-4-authorize-in-salesforce" id="step-4-authorize-in-salesforce"></a>

* You will be redirected to the Salesforce login page.
* Log in and approve Guard access.
* Salesforce will redirect you back to Guard.

#### Step 5: Successful Registration <a href="#step-5-successful-registration" id="step-5-successful-registration"></a>

After successful authorization:

* The org is registered.
* Tokens are securely encrypted and stored.
* The org becomes available across applicable ARM modules.
* The connection status displays as **Connected**.
