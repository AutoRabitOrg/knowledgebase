# Salesforce ECA Configuration for AutoRABIT

How AutoRABIT products (CodeScan, Guard, and Vault) connect to a customer Salesforce org using a Salesforce External Client App (ECA). Follow the product-specific guides to create or reuse an ECA, capture the Client ID and Client Secret, and complete the connection setup and user authorization required for that product.

<details>

<summary>ARM: Salesforce ECA (Local) Connection Setup</summary>



#### This is a step by step on how to implement the Local ECA solution to establish a new connection with ARM.

### 1) Pre-req: get your Callback URL (redirect URI) <a href="#arm-1-pre-req-getyourcallbackurl-redirecturi" id="arm-1-pre-req-getyourcallbackurl-redirecturi"></a>

For AutoRABIT’s ARM ECA setup, you need **the callback URL**

Callback URL is depending on the instance:

{$isntancename}/oauth/\_callback

Example:

https://arm-qan5.autorabit.com/oauth/\_callback

### 2) Create the External Client App (ECA) in your Salesforce Org <a href="#arm-2-createtheexternalclientapp-eca-inyoursalesforceorg" id="arm-2-createtheexternalclientapp-eca-inyoursalesforceorg"></a>

1\.     Login into Salesforce

<p align="center"><img src="../../.gitbook/assets/unknown.png" alt="" data-size="original"></p>

2\.     In **Salesforce**, go to **Setup**.

3\.     In **Quick Find**, search **External Client Apps**.

4\.     Open **External Client App Manager** (or the External Client Apps area).

![](<../../.gitbook/assets/unknown (1).png>)

5\.     Click **New External Client App**.

6\.     Fill in the basics:

o   **Name / Label ( e.g. AR\_Local)**

o   **API Name** (auto-filled)

o   **Contact Email**

o   **Distribution State**:

§  **Local** (only for this org)

![](<../../.gitbook/assets/unknown (2).png>)

***

### 3) Enable OAuth + set callback URL + scopes <a href="#arm-3-enableoauthsetcallbackurlscopes" id="arm-3-enableoauthsetcallbackurlscopes"></a>

1\.     Click **Enable OAuth** (or expand **API (Enable OAuth Settings)** and check **Enable OAuth**).

2\.     Set \*_Callback URL_

The URL you collected in step 1.

3\.     Choose **OAuth Scopes**:

·       Access the identity URL service (id, profile, email, address, phone)

·       Manage user data via APIs (api)

·       Full access (full)

·       Access Connect REST API resources (chatter\_api)

·       Perform requests at any time (refresh\_token, offline\_access)

·       Access custom permissions (custom\_permissions)

![](<../../.gitbook/assets/unknown (3).png>)

***

### 4) Turnment <a href="#arm-4-turnment" id="arm-4-turnment"></a>

1\.     In **Flow Enablement**, select **Enable Authorization Code and Credentials Flow**.

2\.     **user credentials are required in the POST body** (Salesforce shows this option when you choose that flow) should be disabled.

![](<../../.gitbook/assets/unknown (4).png>)

***

### 5) Security toggles (common defaults) <a href="#arm-5-securitytoggles-commondefaults" id="arm-5-securitytoggles-commondefaults"></a>

In the **Security** section the next options should be enabled:

·       **Require secret for Web Server Flow**

·       **Require secret for Refresh Token Flow**

***

### 6) Create the app and capture Client ID / Secret <a href="#arm-6-createtheappandcaptureclientid-secret" id="arm-6-createtheappandcaptureclientid-secret"></a>

1\.     Click **Create**.

2\.     Open the app’s **Settings** tab and locate **Consumer Key and Secret**:

o   **Consumer Key** = **Client ID**

o   **Consumer Secret** = **Client Secret**

![](<../../.gitbook/assets/unknown (5).png>)

When you click the button for Consumer Key and Secret a code will be sent to the registered email for the user creating the configuration

![](<../../.gitbook/assets/unknown (6).png>)

After getting the code and verify in Salesforce the Consumer Key (CliendID) and Consumer Secret (Client Secret) will be displayed.

**IMPORTANT: STORE THIS VALUES IN A SAFE PLACE WHERE CAN BE EASILY USED FOR FUTURE REFERECES.**

![](<../../.gitbook/assets/unknown (7).png>)

***

### 7) Configure Policies (very important) <a href="#arm-7-configurepolicies-veryimportant" id="arm-7-configurepolicies-veryimportant"></a>

After creating the ECA, open the **Policies** tab and adjust as needed (exact options vary by org/security posture), commonly:

·       **Permitted Users**: often set to **Admin approved users are pre-authorized** for controlled rollouts.

·       Add the required **profiles/permission sets** (or approved users) for who is allowed to authorize.

***

### 8) What you’ll use in AutoRABIT <a href="#arm-8-whatyoulluseinautorabit" id="arm-8-whatyoulluseinautorabit"></a>

Once created, the set of values you’ll reference in your CodeScan configuration are:

·       **Client ID**

·       **Client Secret**

Also, the internal direction is to be clear that **one ECA per customer org** can be used across products (rather than creating one per AR product).

***

After the configuration in salesforce is complete, and you have obtained the ClientID and Client Secret, we can go to ARM to create the connection

In the menu Click in Salesforce org and click in register Salesforce org

![](<../../.gitbook/assets/unknown (8).png>)

Create the connections filling the required information obtained from Salesforce.

![](<../../.gitbook/assets/unknown (9).png>)

Once the Validate and save button is clicked a salesforce login is shown to login with the user we intend to use for the Connection.

![](<../../.gitbook/assets/unknown (10).png>)

A message from Salesforce will show to require granting the permissions for the user to use the scopes we defined in the ECA, Click in Allow

![](/broken/files/zeWFycK7i1THHE54AMLV)

Then, you will be returned to ARM and the connection will be saved.

![](<../../.gitbook/assets/unknown (11).png>)

</details>

<details>

<summary>CodeScan: Salesforce ECA (Local) Connection Setup</summary>



</details>

<details>

<summary>Vault: Salesforce ECA (Local) Connection Setup</summary>



</details>

<details>

<summary>Guard: Salesforce ECA (Local) Connection Setup</summary>



</details>

