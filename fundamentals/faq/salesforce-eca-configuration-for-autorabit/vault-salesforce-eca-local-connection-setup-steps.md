---
description: >-
  This is a step by step on how to implement the Local ECA solution to establish
  a new connection with Guard.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Vault: Salesforce ECA (Local) Connection Setup Steps

### Pre-req: get your Callback URL (redirect URI) <a href="#id-1-pre-req-get-your-callback-url-redirect-uri" id="id-1-pre-req-get-your-callback-url-redirect-uri"></a>

For AutoRABIT’s Vault ECA setup, you need **the callback URL**

Callback URL is depending on the instance:

```
{$isntancename}/dashboard/setup/addSfOrg
```

Example:

```
https://vault-qa.autorabit.com/dashboard/setup/addSfOrg
```

{% stepper %}
{% step %}
### Create the External Client App (ECA) in your Salesforce Org

1. Login into Salesforce

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

2. In **Salesforce**, go to **Setup**.
3. In **Quick Find**, search **External Client Apps**.
4. Open **External Client App Manager** (or the External Client Apps area).

<figure><img src="../../../.gitbook/assets/cdn.webp" alt=""><figcaption></figcaption></figure>

5. Click **New External Client App**.
6. Fill in the basics:

* **Name / Label ( e.g. AR\_Local)**
* **API Name** (auto-filled)
* **Contact Email**
* **Distribution State**:
  * **Local** (only for this org)

<figure><img src="../../../.gitbook/assets/f306f55b-5110-4872-bbec-20b722c50b29.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### &#x20;Enable OAuth + set callback URL + scopes <a href="#arm-3-enableoauthsetcallbackurlscopes" id="arm-3-enableoauthsetcallbackurlscopes"></a>

1. Click **Enable OAuth** (or expand **API (Enable OAuth Settings)** and check **Enable OAuth**).
2.  Set \*_Callback URL_

    The URL you collected in step 1.
3. Choose **OAuth Scopes**:
   1. Access the Identity URL service (id, profile, email, address, phone)
   2. Manage user data via APIs
   3. Manage user data via web browsers (web)
   4. Full access (full)
   5. Perform requests at any time (refresh\_token, offline\_access.

<figure><img src="../../../.gitbook/assets/87d2dfba-10dd-4045-919b-555c15d1092f.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Turnment <a href="#arm-4-turnment" id="arm-4-turnment"></a>

1. In **Flow Enablement**, select **Enable Authorization Code and Credentials Flow**.
2. **user credentials are required in the POST body** (Salesforce shows this option when you choose that flow) should be disabled.

<figure><img src="../../../.gitbook/assets/619e40a3-3cab-4c4d-a1ff-a2580e7ba452.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Security toggles (common defaults) <a href="#arm-5-securitytoggles-commondefaults" id="arm-5-securitytoggles-commondefaults"></a>

In the **Security** section the next options should be enabled:

* **Require secret for Web Server Flow**
* **Require secret for Refresh Token Flow**
{% endstep %}

{% step %}
### &#x20;Create the app and capture Client ID / Secret <a href="#arm-6-createtheappandcaptureclientid-secret" id="arm-6-createtheappandcaptureclientid-secret"></a>

1. Click **Create**.
2. Open the app’s **Settings** tab and locate **Consumer Key and Secret**:

* **Consumer Key** = **Client ID**
* **Consumer Secret** = **Client Secret**

<figure><img src="../../../.gitbook/assets/37254284-9b62-4fd6-940f-df5576eb0718.png" alt=""><figcaption></figcaption></figure>

When you click the button for Consumer Key and Secret a code will be sent to the registered email for the user creating the configuration

<figure><img src="../../../.gitbook/assets/b5d12e36-9af7-4655-998e-b1cbbd0aa7b6.png" alt=""><figcaption></figcaption></figure>

After getting the code and verify in Salesforce the Consumer Key (CliendID) and Consumer Secret (Client Secret) will be displayed.

**IMPORTANT: STORE THIS VALUES IN A SAFE PLACE WHERE CAN BE EASILY USED FOR FUTURE REFERECES.**

<figure><img src="../../../.gitbook/assets/d6f4ece7-0cd4-4ae3-8c8f-bb1322d472dd.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Configure Policies (very important) <a href="#arm-7-configurepolicies-veryimportant" id="arm-7-configurepolicies-veryimportant"></a>

After creating the ECA, open the **Policies** tab and adjust as needed (exact options vary by org/security posture), commonly:

* **Permitted Users**: often set to **Admin approved users are pre-authorized** for controlled rollouts.
* Add the required **profiles/permission sets** (or approved users) for who is allowed to authorize.
{% endstep %}

{% step %}
### What you’ll use in AutoRABIT <a href="#arm-8-whatyoulluseinautorabit" id="arm-8-whatyoulluseinautorabit"></a>

Once created, the set of values you’ll reference in your Vault configuration are:

* **Client ID**
* **Client Secret**

Also, the internal direction is to be clear that **one ECA per customer org** can be used across products (rather than creating one per AR product).

***

After the configuration in Salesforce is complete, and you have obtained the ClientID and Client Secret, we can go to Vault to create the connection

In the menu Click Salesforce Org Integration

<figure><img src="../../../.gitbook/assets/8245333d-b8d7-49db-a774-c1c712a8cb2e.png" alt=""><figcaption></figcaption></figure>

Create the connections filling the required information.

<figure><img src="../../../.gitbook/assets/6d6574e8-2412-4b5b-bd33-edd0b762d4ef.png" alt=""><figcaption></figcaption></figure>

Enter the Client Id and Client Secret that you received from Salesforce

<figure><img src="../../../.gitbook/assets/4afab8d3-c577-4432-951e-2f02e69ffb42.png" alt=""><figcaption></figcaption></figure>

Once the continue button is clicked, a Salesforce login is shown for the user we intend to use with the connection.

<figure><img src="../../../.gitbook/assets/2ee0edd6-fd45-4ca0-9114-356995ca5351.png" alt=""><figcaption></figcaption></figure>

A message from Salesforce will show to require granted permissions for the user to use the scopes defined in the ECA, Click Allow

<figure><img src="../../../.gitbook/assets/e6cc1945-e43c-4c68-802b-873dacaa0b2f.png" alt=""><figcaption></figcaption></figure>

Then you will be returned and the connection will be saved.

<figure><img src="../../../.gitbook/assets/841c3e49-3380-470a-b4f6-c19ee797a362.png" alt=""><figcaption></figcaption></figure>

Click finish and the success message will appear

<figure><img src="../../../.gitbook/assets/5caba430-fb77-494d-a717-1958d333d168.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

