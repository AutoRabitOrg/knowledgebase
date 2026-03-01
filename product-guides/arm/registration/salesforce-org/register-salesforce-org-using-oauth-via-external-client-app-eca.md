# Register Salesforce Org using OAuth via External Client App (ECA)

### Overview

To use Salesforce Org functionality within ARM, you must first register your Salesforce organization. Registration allows ARM to securely connect to your Salesforce org with the required permissions.

ARM supports the following authentication methods:

* Standard Authentication
* OAuth via Connected App
* OAuth via External Client App (ECA)

This article explains:

* How to register a new Salesforce org using **OAuth via External Client App (ECA)**
* How to migrate an existing org to this authentication type
* Important considerations and limitations

***

## Part 1: Salesforce Prerequisites

Before registering your org in ARM, complete the following steps in Salesforce.

### Step 1: Create an External Client App

1. Navigate to **Salesforce Setup**
2. Search for **External Client Apps**
3. Click **New External Client App**
4. Enter the required details

#### Basic Information

* **External Client App Name**
* **API Name** (auto-populated)
* **Contact Email**

#### Enable OAuth Settings

1. Select **Enable OAuth Settings**
2. Provide the **Callback URL** exactly as shown in the ARM UI
3. Add the following OAuth scopes:

* Access the identity URL service (id, profile, email, address, phone)
* Manage user data via APIs (api)
* Full access (full)
* Access Connect REST API resources (chatter\_api)
* Perform requests at any time (refresh\_token, offline\_access)
* Access custom permissions (custom\_permissions)

#### Flow Enablement

Enable the following flows:

* Authorization Code and Credentials Flow
* Device Flow

#### Save and Activate

Save the application and activate it.

### Step 2: Collect Client Credentials

After activation, copy the following:

* **Consumer ID (Consumer Key)**
* **Consumer Secret**

> **Note:** Newly generated credentials may take up to 10 minutes to become active in Salesforce. If verification fails, wait and retry.

***

## Part 2: Register a New Salesforce Org Using OAuth via ECA

### Step 1: Open Org Registration

Navigate to:

**Salesforce Org Management → Register Org**

### Step 2: Select Authentication Type

Choose:

**OAuth via External Client App**

### Step 3: Enter Required Details

Provide the following information:

* Name
* Type
* Login URL (Production / Sandbox / Custom Domain)
* Consumer ID
* Consumer Secret

Click **Verify / Connect**.

### Step 4: Authorize in Salesforce

* You will be redirected to the Salesforce login page.
* Log in and approve ARM access.
* Salesforce redirects you back to ARM.

### Step 5: Successful Registration

After successful authorization:

* The org is registered.
* Tokens are securely encrypted and stored.
* The org is available across applicable ARM modules.
* Connection status displays as **Connected**.

## Part 3: Reauthentication

To reauthenticate an existing org:

1. Navigate to **Org Details**
2. Click **Reauthenticate**
3. Update Consumer ID / Consumer Secret (if required)
4. Click **Authenticate**
5. Complete Salesforce authorization

After successful completion:

* Connection status updates automatically
* Last authenticated timestamp is refreshed

***

## Part 4: Migrating an Existing Org to OAuth via ECA

### Scenario

You have an org registered using:

* Standard Authentication, or
* OAuth via Connected App

You want to migrate to **OAuth via External Client App (ECA)** without re-registering the org.

### Step 1: Open Org Details

Navigate to:

**Salesforce Org Management → Select Org → Details**

### Step 2: Change Authentication Type

Select:

**Move to OAuth via ECA**

A guided migration panel will open.

### Step 3: Create External Client App in Salesforce

Follow the guided instructions and create the External Client App as described in **Part 1**.

### Step 4: Enter Client Credentials

Enter:

* Consumer ID
* Consumer Secret

Click **Connect**.

### Step 5: Authorize in Salesforce

* You will be redirected to Salesforce.
* Log in and approve access.
* Salesforce redirects back to ARM.

### Step 6: Migration Completion

Upon successful authorization:

* Authentication type updates to **OAuth via ECA**
* The same org record is retained
* Pipelines, jobs, and mappings remain unchanged
* No new org entry is created
* Connection status displays as **Connected**
* Last authenticated timestamp is updated

### Failure Handling

If authentication fails:

* A clear error message is displayed
* The existing connection remains unaffected
* You can retry without impacting current configurations

***

## Important: Dev Hub Registration

Please note the following limitations:

* Dev Hub registration is supported **only through OAuth (Connected App)**.
* Dev Hub registration is **not supported** using:
  * Standard authentication
  * OAuth via External Client App (ECA)
* Dev Hub registration is available only under:
  * **Settings → Salesforce Org**
* Dev Hub registration is no longer available in the SFDX module.
* Existing Dev Hubs cannot be reauthenticated.
* New Dev Hubs can be created using OAuth (Connected App) without issues.

***

## Important: Updating Consumer ID and Consumer Secret

When updating credentials for an existing OAuth via ECA connection, the following behavior applies.

### Test Connection Behavior

If you:

* Update Consumer ID or Consumer Secret
* Click **Test Connection**
* Do not complete OAuth authorization

Then:

* The test may still show **Success**
* The system continues using previously authorized credentials stored in the backend
* The new values are not applied yet

***

### When Are New Credentials Applied?

New credentials take effect **only after completing the OAuth authorization flow successfully**.

Until authorization is completed:

* Existing tokens remain active
* Previous credentials remain in effect
* Backend values are not replaced

***

### Recommendation

After updating credentials:

1. Click **Authenticate / Connect**
2. Complete Salesforce authorization
3. Confirm the connection status updates successfully

Without completing authorization, the new credentials will not be validated or activated.
