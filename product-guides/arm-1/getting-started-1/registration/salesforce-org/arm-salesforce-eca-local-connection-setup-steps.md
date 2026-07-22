---
description: >-
  This is a step by step on how to implement the Local ECA solution to establish
  a new connection with ARM.
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
  actions:
    visible: true
---

# ARM: Salesforce ECA Connection Setup Steps

{% stepper %}
{% step %}
### Pre-req: get your Callback URL (redirect URI)

For AutoRABIT’s ARM ECA setup, you need **the callback URL**

Callback URL is depending on the instance:

```
{$instancename}/oauth/_callback
```

Example:

```
https://arm-qan5.autorabit.com/oauth/_callback
```
{% endstep %}

{% step %}
### Create the External Client App (ECA) in your Salesforce Org

1. Login into Salesforce

<figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. In **Salesforce**, go to **Setup**.
3. In **Quick Find**, search **External Client Apps**.
4. Open **External Client App Manager** (or the External Client Apps area).

<figure><img src="../../../../../.gitbook/assets/cdn.webp" alt=""><figcaption></figcaption></figure>

5. Click **New External Client App**.
6. Fill in the basics:

* **Name / Label ( e.g. AR\_Local)**
* **API Name** (auto-filled)
* **Contact Email**
* **Distribution State**:
  * **Local** (only for this org)

<figure><img src="../../../../../.gitbook/assets/f306f55b-5110-4872-bbec-20b722c50b29.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
{% hint style="info" %}
**Important Note**: After creating the ECA in Salesforce, there may be a replication delay on the Salesforce side. If you encounter the error error=invalid\_client\_id\&error\_description=client%20identifier%20invalid while attempting to connect or register the org, please wait 30 minutes, then try again to allow the Salesforce configuration to sync completely
{% endhint %}
{% endstep %}

{% step %}
### Enable OAuth + set callback URL + scopes <a href="#arm-3-enableoauthsetcallbackurlscopes" id="arm-3-enableoauthsetcallbackurlscopes"></a>

1. Click **Enable OAuth** (or expand **API (Enable OAuth Settings)** and check **Enable OAuth**).
2. Set \*_Callback URL_

The URL you collected in step 1.

3. Choose **OAuth Scopes**:

* Access the identity URL service (id, profile, email, address, phone)
* Manage user data via APIs (api)
* Full access (full)
* Access Connect REST API resources (chatter\_api)
* Perform requests at any time (refresh\_token, offline\_access)
* Access custom permissions (custom\_permissions)

<figure><img src="../../../../../.gitbook/assets/image (2672).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Flow Enablement <a href="#arm-4-turnment" id="arm-4-turnment"></a>

1. In **Flow Enablement**, select **Enable Authorization Code and Credentials Flow**.
2. **user credentials are required in the POST body** (Salesforce shows this option when you choose that flow) should be disabled.

<figure><img src="../../../../../.gitbook/assets/image (2673).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Security toggles (common defaults) <a href="#arm-5-securitytoggles-commondefaults" id="arm-5-securitytoggles-commondefaults"></a>

In the **Security** section the next options should be enabled:

* **Require secret for Web Server Flow**
* **Require secret for Refresh Token Flow**
* **Enable Refresh Token Rotation(Auto Selected)**
* **Limit Idle Refresh Token Time-to0Live (TTL) to 30 days(Auto Selected)**

**Note:** If this Salesforce Org remains inactive for **30 days**, the refresh token will expire. You must manually re-authenticate the registered Org from the ARM application before it can be used again.
{% endstep %}

{% step %}
### Create the app and capture Client ID / Secret <a href="#arm-6-createtheappandcaptureclientid-secret" id="arm-6-createtheappandcaptureclientid-secret"></a>

1. Click **Create**.
2. Open the app’s **Settings** tab and locate **Consumer Key and Secret**:

* **Consumer Key** = **Client ID**
* **Consumer Secret** = **Client Secret**

<figure><img src="../../../../../.gitbook/assets/d27e1bed-b3fa-4eaf-8853-49349a61c8d1.png" alt=""><figcaption></figcaption></figure>

When you click the button for Consumer Key and Secret a code will be sent to the registered email for the user creating the configuration

<figure><img src="../../../../../.gitbook/assets/5117773e-24dc-490e-bd4a-bfb39742eb18.png" alt=""><figcaption></figcaption></figure>

After getting the code and verify in Salesforce the Consumer Key (CliendID) and Consumer Secret (Client Secret) will be displayed.

**IMPORTANT: STORE THIS VALUES IN A SAFE PLACE WHERE CAN BE EASILY USED FOR FUTURE REFERECES.**

<figure><img src="../../../../../.gitbook/assets/d6f4ece7-0cd4-4ae3-8c8f-bb1322d472dd.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Configure Policies (very important) <a href="#arm-7-configurepolicies-veryimportant" id="arm-7-configurepolicies-veryimportant"></a>

After creating the ECA, open the **Policies** tab and adjust as needed (exact options vary by org/security posture), commonly:

* **Permitted Users**: often set to **Admin approved users are pre-authorized** for controlled rollouts.
* Add the required **profiles/permission sets** (or approved users) for who is allowed to authorize.
{% endstep %}

{% step %}
### What you’ll use in AutoRABIT <a href="#arm-8-whatyoulluseinautorabit" id="arm-8-whatyoulluseinautorabit"></a>

Once created, the set of values you’ll reference in your ARM configuration are:

* **Client ID**
* **Client Secret**

Also, the internal direction is to be clear that **one ECA per customer org** can be used across products (rather than creating one per AR product).

***

After the configuration in salesforce is complete, and you have obtained the ClientID and Client Secret, we can go to ARM to create the connection

In the menu Click in Salesforce org and click in register Salesforce org

<figure><img src="../../../../../.gitbook/assets/45539562-22e5-43c8-a071-1c4c8c29187c.png" alt=""><figcaption></figcaption></figure>

Create the connections filling the required information obtained from Salesforce.

<figure><img src="../../../../../.gitbook/assets/5202c6a0-6bef-4a59-a0d0-9e108b4ca0e0.png" alt=""><figcaption></figcaption></figure>

Important Note: After creating the ECA in Salesforce, there may be a replication delay on the Salesforce side. If you encounter the error error=invalid\_client\_id\&error\_description=client%20identifier%20invalid while attempting to connect or register the org, please wait 30 minutes, and try again to allow the Salesforce configuration to sync completely.

Once the Validate and save button is clicked a salesforce login is shown to login with the user we intend to use for the Connection.

<figure><img src="../../../../../.gitbook/assets/2ee0edd6-fd45-4ca0-9114-356995ca5351.png" alt=""><figcaption></figcaption></figure>

A message from Salesforce will show to require granted permissions for the user to use the scopes defined in the ECA, Click Allow

<figure><img src="../../../../../.gitbook/assets/8a32ee01-7c38-48fd-9325-ec712724d6c7.png" alt=""><figcaption></figcaption></figure>

Then, you will be returned to ARM and the connection will be saved.

<figure><img src="../../../../../.gitbook/assets/ca4660be-2228-4c3a-acb0-3ef154c56c91.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Important:** This setup is **Salesforce org-specific**. You must repeat this process **for each customer Salesforce org** you want to connect, since the External Client App is created inside (and scoped to) that org and produces org-specific credentials.
{% endhint %}
