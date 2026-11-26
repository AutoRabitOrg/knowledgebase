---
description: 25 November 2026
---

# Salesforce SOAP API login(): Authentication Changes and Configuration Guide

### 1. What is changing?

From December 1, 2026, Salesforce requires the **Use Any API Auth** permission for users authenticating through SOAP login(). This applies to production and sandbox orgs. Authentication can fail with **INSUFFICIENT\_ACCESS** if the permission is missing. SOAP API operations authenticated through OAuth are not affected by this specific requirement.

{% hint style="info" %}
**Important:** The SOAP API login() method is unavailable in **API version 65.0 and later**. Enabling the SOAP API login() setting or granting the Use Any API Auth permission does not restore the operation in those versions.
{% endhint %}

AutoRABIT is responsible for removing its dependency on SOAP login(). Until a compatible product version is deployed, affected customers may need to apply a temporary Salesforce permission change to maintain service continuity. Your Salesforce administrator performs this change with assistance from AutoRABIT Support.

### 2. Determine whether you need to act

Start with your deployment: identify your AutoRABIT product, deployment type (SaaS, Dedicated or On-Prem), installed version if available, and connected Salesforce production and sandbox orgs.

**If AutoRABIT has confirmed your deployed version is unaffected:** no permission change is required for this issue.

**If AutoRABIT has confirmed your version or operation is affected:** follow the configuration steps below for the identified integration users.

**If your status is unknown:** contact AutoRABIT Support now, before December 1. Provide the deployment details above and the Salesforce usernames used by AutoRABIT, if known. Support will help determine the affected operations, users and available upgrade or mitigation path. You are not expected to know the internal authentication implementation.

### 3. Optional check in Salesforce Login History

As a Salesforce administrator, open **Setup**, search for **Login History**, and review or download recent login records for the integration users. Look for API login activity and, where available, SOAP-related login subtype or API details. Record the username, timestamp, login type, subtype and status. Share relevant sanitized records with Support.

API activity alone does not prove that AutoRABIT uses SOAP login(). Other integrations may use the same account, and infrequent operations may not appear in recent history. Do not use a lack of matching records or a successful OAuth connection as proof that you are unaffected. Support should confirm applicability before you grant permissions.

### Configure the temporary mitigation

_For confirmed affected Salesforce orgs and users._

#### Step 1 | Confirm the affected user

With AutoRABIT Support, identify the exact Salesforce account used by the affected operation. In **Setup**, search for **Users**, open the account and confirm it is active. Obtain your security administrator's approval before changing permissions. Test in a sandbox first where possible.

#### Step 2 | Check SOAP login availability

In **Setup**, search for **User Interface** and locate **Enable SOAP API login()**. If already enabled, leave it enabled. If disabled, stop and consult your security administrator and AutoRABIT Support before enabling it. Do not disable the restriction requiring Use Any API Auth.

#### Step 3 | Create or select a permission set

In **Setup**, search for **Permission Sets** and click **New**. Enter the label **AutoRABIT SOAP API Authentication** (suggested API name: AutoRABIT\_SOAP\_API\_Authentication). Leave the license as None if appropriate for the user, then Save. An existing approved permission set can also be used.

#### Step 4 | Enable the permission

Open the permission set. Select **System Permissions**, then **Edit**. Find **Use Any API Auth**, select it, click Save and confirm any prompt. The user license must support this permission. If unavailable, contact Support before proceeding.

#### Step 5 | Assign the permission

From the permission set, select **Manage Assignments**, then **Add Assignments**. Select the confirmed integration user, click Next, then Assign. Verify the user appears in the assignment list. Repeat only for other confirmed affected users. Do not grant this permission to all users.

#### Step 6 | Validate the affected operation

In an approved sandbox, go to **Setup > Release Updates** and locate **Assign Use Any API Auth Permission for SOAP login()**. Follow the available test-run controls. Coordinate a fresh authentication attempt through the affected AutoRABIT operation with Support. A cached session or generic connection test is not sufficient. Confirm success and review Login History. Repeat for affected production orgs under your change process.

### Validation and next steps

_Working with AutoRABIT Support._

#### If validation fails

Contact AutoRABIT Support with the product, deployment type, version if known, org ID, environment, affected operation, integration username, time of failure and sanitized error message. Include relevant Login History records if available.

**Never send passwords, security tokens, session IDs or OAuth tokens.**

#### When is the temporary change complete?

Your administrator has assigned the permission to the confirmed affected users, and the affected operation has successfully completed using fresh authentication. AutoRABIT Support can assist in confirming the outcome and identifying any remaining affected environments.

#### Permanent resolution

This permission is an interim measure, not a permanent solution. Salesforce plans to retire legacy SOAP login() in Summer 2027. AutoRABIT is responsible for addressing its product dependency.

Support will help identify the applicable product version and upgrade path for your deployment. Once the dependency has been removed and validated, review removal of the temporary permission with your security administrator, taking into account any other integrations that may still require it.

Customers should assess migrating to **OAuth with a Salesforce External Client App (ECA)**.

For ARM configuration, refer to the [ARM Salesforce ECA local connection setup guide](https://knowledgebase.autorabit.com/product-guides/arm-1/getting-started-1/registration/salesforce-org/arm-salesforce-eca-local-connection-setup-steps).

Customers should coordinate the migration and, if needed, contact AutoRABIT Support for assistance.

### Official Salesforce references

* [Salesforce Release Update – Assign Use Any API Auth Permission for SOAP login()](https://help.salesforce.com/s/articleView?id=release-notes.rn_api_soap_login.htm\&language=en_US\&type=5)
* [Salesforce SOAP API login() Developer Guide](https://developer.salesforce.com/docs/platform/api/guide/sforce-api-calls-login.html)
* [Salesforce Knowledge Article 005132110](https://help.salesforce.com/s/articleView?id=005132110\&language=en_US\&type=1)
