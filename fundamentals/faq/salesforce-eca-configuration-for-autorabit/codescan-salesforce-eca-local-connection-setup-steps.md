---
description: >-
  This is a step by step on how to implement the Local ECA solution to establish
  a new connection with CodeScan.
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

# CodeScan: Salesforce ECA (Local) Connection Setup Steps

{% stepper %}
{% step %}
### Pre-req: get your Callback URL (redirect URI)

For AutoRABIT’s CodeScan ECA setup, you need **the callback URL**

Callback URL is depending on the instance:

```
{$isntancename}/_codescan/oauth2/authorize
```

Example:

```
https://perf.codescan.io/_codescan/oauth2/authorize
```
{% endstep %}

{% step %}
### Create the External Client App (ECA) in your Salesforce Org

1. Login into Salesforce

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

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
   * Access the identity URL service (id, profile, email, address, phone)
   * Manage user data via APIs (api)
   * Manage user data via Web browsers (web)
   * Perform requests at any time (refresh\_token, offline\_access)

<figure><img src="../../../.gitbook/assets/d23c0990-d25a-435e-8329-64bd9ea4386b.png" alt=""><figcaption></figcaption></figure>
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

<figure><img src="../../../.gitbook/assets/d27e1bed-b3fa-4eaf-8853-49349a61c8d1.png" alt=""><figcaption></figcaption></figure>

When you click the button for Consumer Key and Secret a code will be sent to the registered email for the user creating the configuration

<figure><img src="../../../.gitbook/assets/5117773e-24dc-490e-bd4a-bfb39742eb18.png" alt=""><figcaption></figcaption></figure>

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

Once created, the set of values you’ll reference in your CodeScan configuration are:

* **Client ID**
* **Client Secret**

Also, the internal direction is to be clear that **one ECA per customer org** can be used across products (rather than creating one per AR product).

***

After the configuration in salesforce is complete, and you have obtained the ClientID and Client Secret, we can go to CodeScan to create the connection

In Project analysis click on Add Analysis Project

<figure><img src="../../../.gitbook/assets/8957f101-9fc8-4e97-8b57-0df899e97f44.png" alt=""><figcaption></figcaption></figure>

If no previous connections are found or the required org is not present in the Connection list, a message to go into the Salesforce Connections page is displayed.

<figure><img src="../../../.gitbook/assets/bda30074-12d4-4207-b244-81e5beb7b0e5.png" alt=""><figcaption></figcaption></figure>

If that is the case, go in the Salesforce Connections page, click on the existing connection or click on the Create connection button

<figure><img src="../../../.gitbook/assets/06389ed9-efbc-4028-b2c3-61cd21a68a90.png" alt=""><figcaption></figcaption></figure>

Create the connections filling the required information obtained from Salesforce.

<figure><img src="../../../.gitbook/assets/c3d24865-2b45-4520-ba63-6931425cb9d1.png" alt=""><figcaption></figcaption></figure>

Once the connection is created, go back into adding a new Analysis page and click again in Add Analysis Project and select the desired connection.

<figure><img src="../../../.gitbook/assets/f31bb32c-70bb-4b6a-a9d9-4dd046495c2d.png" alt=""><figcaption></figcaption></figure>

Once the Confirm button is clicked a salesforce login is shown to login with the user we intend to use for the analysis.

<figure><img src="../../../.gitbook/assets/2ee0edd6-fd45-4ca0-9114-356995ca5351.png" alt=""><figcaption></figcaption></figure>

A message from Salesforce will show to require granted permissions for the user to use the scopes defined in the ECA, Click Allow

<figure><img src="../../../.gitbook/assets/e6cc1945-e43c-4c68-802b-873dacaa0b2f.png" alt=""><figcaption></figcaption></figure>

Then, you will be returned to configure the new Analysis, fill up the form.

<figure><img src="../../../.gitbook/assets/6cc352f8-dea6-402b-ada4-d941b15ac8a8.png" alt=""><figcaption></figcaption></figure>

Then the analysis with the connection will be added to the list.

<figure><img src="../../../.gitbook/assets/12a84570-c4ba-4104-bbd0-9e6a9ddd4c98.png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
**Important:** This setup is **Salesforce org-specific**. You must repeat this process **for each customer Salesforce org** you want to connect, since the External Client App is created inside (and scoped to) that org and produces org-specific credentials.
{% endhint %}
{% endstep %}
{% endstepper %}
