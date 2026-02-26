# Salesforce Org

You must register the organization to use any Salesforce Org functionality inside ARM. When you register your Salesforce organization in ARM, ARM connects to your organization with the required permissions.

ARM Support 3 ways to connect your Salesforce Orgs(Standard, OAuth, OAuth ECA)

## Register Salesforce Org using OAuth via External Client App (ECA)

### Overview

This guide explains how to register a Salesforce org in ARM using OAuth via External Client App (ECA) and how to migrate an existing org to this authentication type.

***

## Part 1: Pre-Requisites in Salesforce

Before starting ARM registration, complete the following in Salesforce:

### Step 1: Create an External Client App

1. Navigate to **Salesforce Setup**
2. Search for **External Client Apps**
3. Click **New External Client App**
4. Enter required application details
5. Enable **OAuth Settings**
6. Add the **ARM Callback URL** (exactly as shown in ARM)
7. Select required OAuth scopes (API and refresh token access recommended)
8. Save and activate the app

### Step 2: Collect Credentials

After activation, copy:

* **Consumer ID (Consumer Key)**
* **Consumer Secret**

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-02-26 at 08.36.58.png" alt=""><figcaption></figcaption></figure>

### Step 3: Verify Permissions

Ensure:

* The authorizing user has **API access**
* OAuth policies allow **authorization and refresh tokens**

## Part 2: Register New Salesforce Org using OAuth via ECA

### Step 1: Open Salesforce Org Registration

Navigate to:

**Salesforce Org Management → Register Org**

### Step 2: Select Registration Type

Choose:

* **OAuth via External Client App**

(Other authentication options continue to follow existing flows.)

### Step 3: Enter Required Information

Provide the following details in this sequence:

1. **Name**
2. **Type**
3. **Login URL** (Production / Sandbox / Custom Domain)
4. **Consumer ID**
5. **Consumer Secret**

After entering all required details, click **Verify / Connect**.

### Step 4: Authorize in Salesforce

1. You will be redirected to the Salesforce login page
2. Log in and approve ARM access
3. Salesforce redirects back to ARM

### Step 5: Successful Registration

Upon successful authorization:

* The org is registered
* Tokens are securely encrypted and stored
* The org becomes visible across applicable ARM modules
* Connection status displays as **Connected**

## Important: Updating Consumer ID / Consumer Secret

When editing Consumer ID and Consumer Secret for an existing OAuth via ECA connection, the following behavior applies:

### Test Connection Behavior

If you update the Consumer ID or Consumer Secret and click **Test Connection** without completing OAuth authorization:

* The test may still display **Success**
* The system continues using previously authorized credentials stored in the backend
* The updated values are not applied until OAuth authorization completes successfully

### When Are New Credentials Applied?

New Consumer ID and Consumer Secret values take effect **only after completing the OAuth authorization flow**.

Until authorization is successfully completed:

* Existing tokens remain active
* Previous credentials remain in effect
* Backend values are not replaced

### Recommendation

After updating credentials:

1. Click **Authenticate / Connect**
2. Complete Salesforce authorization
3. Confirm the connection status updates successfully

Without completing authorization, the new credentials will not be validated or activated.

## Part 3: Re-Authentication

1. Navigate to **Org Details**
2. Click **Reauthenticate**
3. Update Consumer ID / ConsumerSecret (if required)
4. Click **Authenticate**
5. Complete Salesforce authorization

The connection status and last authenticated timestamp will update automatically.

## Part 4: Migrating Existing Org to OAuth via ECA

### Scenario

An org is already registered using:

* Standard authentication, or
* OAuth via Connected App

You want to migrate to OAuth via External Client App without re-registering.

### Step 1: Open Org Details

Navigate to:

**Salesforce Org Management → Select Org → Details**

### Step 2: Change Authentication Type

Select:

**Move to OAuth via ECA**

A right-side guided migration panel will open.

### Step 3: Create External Client App in Salesforce

Follow the guided steps displayed in ARM:

* Create External Client App
* Enable OAuth
* Add ARM callback URL
* Activate the app

### Step 4: Enter Client Credentials

Enter:

* Consumer**ID**
* Consumer **Secret**

Click **Connect**

### Step 5: Authorize in Salesforce

* You will be redirected to Salesforce
* Log in and approve access
* Redirect back to ARM

### Step 6: Migration Completion

Upon successful authorization:

* Authentication type updates to **OAuth via ECA**
* The same org record is retained
* Pipelines, jobs, and mappings remain unchanged
* No new org entry is created
* Connection status displays as **Connected**
* Last authenticated timestamp is updated

## Failure Handling

If authentication fails:

* A clear error message is displayed
* The existing connection remains unaffected
* You can retry without impacting current configurations

## Important: Dev Hub Registration

* Dev Hub registration is supported **only through OAuth authentication**.
* Dev Hub registration is **not supported** using Standard authentication.
* Dev Hub registration is **not supported** using OAuth via External Client App (ECA).
*   Dev Hub registration is available only under:

    **Settings → Salesforce Org**
* Dev Hub registration is no longer available in the **SFDX module**.

### Adding a Salesforce Org connection via OAuth <a href="#adding-a-salesforce-org-connection-via-oauth" id="adding-a-salesforce-org-connection-via-oauth"></a>

1. Log in to your ARM account.&#x20;
2.  Go to the **`Settings > Salesforce Org.`** page.<br>

    <figure><img src="../../../../.gitbook/assets/image (1942).png" alt="" width="231"><figcaption></figcaption></figure>
3.  From the **`SF Org Mgmt.`** screen, click on the **`Register Salesforce Org`** button.<br>

    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 9.13.41 PM.png" alt=""><figcaption></figcaption></figure>
4. Enter the **`Salesforce Org Name`**.
5. Select the **`Salesforce Org Type`** from the drop-down (_Developer_, _Integration_, _QA_, _UAT_, _Production_).
6. Select the **`Environment`** from the drop-down (_Production or Development Edition_, _Sandbox_, _Pre-Release_, _Custom URL_).
7. **`Salesforce Org URL`** is predefined based on the Environment selected.
8. Select **`Access type`** as **`OAuth`** as the authentication method.
9.  Click **`Validate & Save`** to proceed through the OAuth flow and allow ARM to connect to your Salesforce Org.<br>

    <figure><img src="../../../../.gitbook/assets/image (1943).png" alt="" width="375"><figcaption></figcaption></figure>
10. Click **`Allow`** when prompted to grant ARM access to the Salesforce Org.
11. The org will now be added to your list of saved connections. It will appear in the list of available orgs via the dropdown for future comparisons and automation jobs.

{% hint style="info" %}
**Important Note:** If your Salesforce Org is configured with nCino objects, you can select the **`Is nCino Installed`** checkbox. The nCino logo is added for each nCino configured Salesforce Org for easier identification from other Salesforce Org.
{% endhint %}

### Connecting to a Salesforce Org using username/password <a href="#connecting-to-a-salesforce-org-using-usernamepassword" id="connecting-to-a-salesforce-org-using-usernamepassword"></a>

1. Go to the **`Settings > SF Org Mgmt.`** page.
2. From the **`SF Org Mgmt.`** screen, click on the **`Add`** button.
3. Enter the **`Salesforce Org Name`**.
4. Select the **`Salesforce Org Type`** from the drop-down (_Developer_, _Integration_, _QA_, _UAT_, _Production_).
5. Select the **`Environment`** from the drop-down (_Production or Development Edition_, _Sandbox_, _Pre-Release_, _Custom URL_).
6. Select **`Access Type`** as **`Standard`** as the authentication method.
7. Enter the **`User Name`** and **`Password`**.
8. Enter the **`Security Token`**&#x20;
9.  Click **`Validate & Save`** to proceed through the OAuth flow and allow ARM to connect to your Salesforce Org.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (1944).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** If your Salesforce Org is configured with nCino objects, you can select the **`Is nCino Installed`** checkbox. The nCino logo is added for each nCino configured Salesforce Org for easier identification from other Salesforce Org.
{% endhint %}

### What is Salesforce Security Token, and How Do I Find It? <a href="#what-is-salesforce-security-token-and-how-do-i-find-it" id="what-is-salesforce-security-token-and-how-do-i-find-it"></a>

Your Salesforce security token is a case-sensitive alphanumeric key used with a password to access Salesforce via API. The token aims to improve the security between Salesforce users and Salesforce.com in the case of a compromised account. It ensures, among other things, that if a user’s account credentials are compromised, a third party cannot access Salesforce.

#### Losing the security token <a href="#losing-the-security-token" id="losing-the-security-token"></a>

If you can’t remember your security token and have deleted the email containing the token, the only way to retrieve it is by resetting the token. Salesforce does not provide an option to view your token within the web application; the only option is resetting it.

#### Getting the Security Token for Your Salesforce Account <a href="#getting-the-security-token-for-your-salesforce-account" id="getting-the-security-token-for-your-salesforce-account"></a>

When you create a Salesforce account, Salesforce sends an email message from support@salesforce.com with the subject: _salesforce.com security token confirmation_ to the email address associated with the account. This email message contains the Security Token for the account and is the only place where you can find the Security Token value. When you change the account password, the security token is regenerated (the previous one expires), and a similar email is sent.

To get the security token for your Salesforce account, In the mailbox for the email address associated with the Salesforce account, look for the latest email message received from _support@salesforce.com_ with the subject: _salesforce.com security token confirmation_.&#x20;

If you cannot find the latest email with the security token, reset the security token:&#x20;

1. Log in to Salesforce using the Salesforce account.
2. In the User Menu, select **`Setup`**.
3. In the menu on the left, under **`Personal Setup`**, expand **`My Personal Information`**, then click **`Reset My Security Token`**. Follow the instructions on the screen.
4. A new email message will be sent.
5. Open the message and then copy the **`Security Token value`**.

{% hint style="info" %}
**Important Note:** We recommend saving this email in a secure location, so you don’t have to reset your security token whenever needed.
{% endhint %}

### Edit Salesforce Org details after registration <a href="#edit-salesforce-org-details-after-registration" id="edit-salesforce-org-details-after-registration"></a>

You can change the **`Environment`** type, the **`Access Type`**, or both.

1. From the screen, choose the desired environment and access types from the respective dropdown fields.
2. To edit the **`User Name`**, ensure that the **`Access type`** is set as **`Standard`**.
3. Click **`Save`** or **`Test Connection`**, and you will see one of the following confirmation messages:
   * If you change the **`Environment type`**  or **`Access Type`**
   * If you change the **`Environment`** type and also the **`Access Type`**\
     \
     <br>

<figure><img src="../../../../.gitbook/assets/image (1945).png" alt="" width="375"><figcaption></figcaption></figure>

4. Click **`Change`** to complete the request. Click **`Keep Current`** to close the confirmation message without changing the details.

### **FAQ**

### How do I update or change the username in all of the Salesforce Orgs specified in AutoRABIT? <a href="#how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au" id="how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au"></a>

To update the username on all registered orgs, re-authenticate the orgs in **Admin > SF Org Management** page.
