# Connecting a Salesforce Org to CodeScan using local ECA flow

{% hint style="info" %}
As of release 26.0.4, CodeScan has adopted the External Client App (ECA) flow for Salesforce, replacing our existing Connected Apps flow.

Key points:

1. If you have an existing Salesforce org registered, you are using the existing Connected App flow. No action is required at this time, and your analyses will run as expected.
2. Please note that any new Salesforce org that you wish to register in CodeScan must use the new local ECA flow.
3. Please note that if your existing Salesforce orgs need to be reattached, if your tokens expire, or after Sandbox refresh, your Connected App flow will no longer work, and you will need to re-register your org using the local ECA flow. Please note that in these circumstances, your comparison branches in Salesforce will need to be set up again.
{% endhint %}

This is a step-by-step guide on how to implement the local ECA flow to establish a new connection with CodeScan.

### 1) Pre-requisite: get your Callback URL (redirect URI) <a href="#id-1-pre-req-get-your-callback-url-redirect-uri" id="id-1-pre-req-get-your-callback-url-redirect-uri"></a>

For AutoRABIT’s CodeScan ECA setup, you need **the callback URL**

Callback URL depends on the instance:

_{$isntancename}/\_codescan/oauth2/authorize_

Example:

_https://perf.codescan.io/\_codescan/oauth2/authorize_

### 2) Create the External Client App (ECA) in your Salesforce Org <a href="#id-2-create-the-external-client-app-eca-in-your-salesforce-org" id="id-2-create-the-external-client-app-eca-in-your-salesforce-org"></a>

1. Login into Salesforce

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

1. In **Salesforce**, go to **Setup**.
2. In **Quick Find**, search **External Client Apps**.
3. Open **External Client App Manager** (or the External Client Apps area).

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Click **New External Client App**.
3. Fill in the basics:
   * **Name / Label ( e.g. AR\_Local)**
   * **API Name** (auto-filled)
   * **Contact Email**
   * **Distribution State**:
     * **Local** (only for this org)

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### 3) Enable OAuth + set callback URL + scopes <a href="#id-3-enable-oauth--set-callback-url--scopes" id="id-3-enable-oauth--set-callback-url--scopes"></a>

1. Click **Enable OAuth** (or expand **API (Enable OAuth Settings)** and check **Enable OAuth**).
2.  Set \*_Callback URL_

    The URL you collected in step 1.
3. Choose **OAuth Scopes**:
   * Access the identity URL service (id, profile, email, address, phone)
   * Manage user data via APIs (api)
   * Manage user data via Web browsers (web)
   * Perform requests at any time (refresh\_token, offline\_access)

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

### 4) Flow Enablement <a href="#id-4-turnment" id="id-4-turnment"></a>

1. In **Flow Enablement**, select **Enable Authorization Code and Credentials Flow**.
2. **User credentials are required in the POST body** (Salesforce shows this option when you choose that flow) should be disabled.

<figure><img src="../../../.gitbook/assets/image (2449).png" alt=""><figcaption></figcaption></figure>

### 5) Security toggles (common defaults) <a href="#id-5-security-toggles-common-defaults" id="id-5-security-toggles-common-defaults"></a>

In the **Security** section the next options should be enabled:

* **Require secret for Web Server Flow**
* **Require secret for Refresh Token Flow**

### 6) Create the app and capture Client ID / Secret <a href="#id-6-create-the-app-and-capture-client-id-secret" id="id-6-create-the-app-and-capture-client-id-secret"></a>

1. Click **Create**.
2. Open the app’s **Settings** tab and locate **Consumer Key and Secret**:
   * **Consumer Key** = **Client ID**
   * **Consumer Secret** = **Client Secret**

<figure><img src="../../../.gitbook/assets/image (2450).png" alt=""><figcaption></figcaption></figure>

When you click the button for Consumer Key and Secret, a code will be sent to the registered email for the user creating the configuration:

<figure><img src="../../../.gitbook/assets/image (2451).png" alt=""><figcaption></figcaption></figure>

After receiving the code and verifying in Salesforce, the Consumer Key (Client ID) and Consumer Secret (Client Secret) will be displayed:

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Store these values in a safe place and make sure you can access them as needed
{% endhint %}

### 7) Configure Policies <a href="#id-7-configure-policies-very-important" id="id-7-configure-policies-very-important"></a>

After creating the ECA, open the **Policies** tab and adjust as needed (exact options vary by org/security posture), commonly:

* **Permitted Users**: often set to **Admin approved users are pre-authorized** for controlled rollouts.
* Add the required **profiles/permission sets** (or approved users) for who is allowed to authorize.

### 8) What you’ll use in AutoRABIT <a href="#id-8-what-youll-use-in-autorabit" id="id-8-what-youll-use-in-autorabit"></a>

Once created, the set of values you’ll reference in your CodeScan configuration are:

* **Client ID**
* **Client Secret**

Also, the internal direction is to be clear that **one ECA per customer org** can be used across products (rather than creating one per AR product).

After the configuration in Salesforce is complete, and you have obtained the ClientID and Client Secret, we can go to CodeScan to create the connection.

In Project analysis, click on Add Analysis Project

<figure><img src="../../../.gitbook/assets/image (2452).png" alt=""><figcaption></figcaption></figure>

If no previous connections are found or the required org is not present in the Connection list, a message to navigate to the Salesforce Connections page is displayed.

<figure><img src="../../../.gitbook/assets/image (2453).png" alt=""><figcaption></figcaption></figure>

If that is the case, move the Salesforce Connections page, click on the existing connection, or select the Create connection button

<figure><img src="../../../.gitbook/assets/image (2454).png" alt=""><figcaption></figcaption></figure>

Create the connection by entering the required information obtained from Salesforce.

<figure><img src="../../../.gitbook/assets/image (2455).png" alt=""><figcaption></figcaption></figure>

Once the connection is created, go back and add a new Analysis. Please click on Add Analysis Project and select the desired connection:

<figure><img src="../../../.gitbook/assets/image (2456).png" alt=""><figcaption></figcaption></figure>

Once confirmed, the Salesforce login page will be shown. Please log in again.

<figure><img src="../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

A message from Salesforce will appear. Click "Allow":

<figure><img src="../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

Then, you will be redirected to configure the new Analysis. Fill in the details:

<figure><img src="../../../.gitbook/assets/image (2459).png" alt=""><figcaption></figcaption></figure>

Then the analysis with the connection will be added to the list:

<figure><img src="../../../.gitbook/assets/image (2460).png" alt=""><figcaption></figcaption></figure>

At this point, the setup for local ECA flow has been completed; your Salesforce analyses will now run as expected.
