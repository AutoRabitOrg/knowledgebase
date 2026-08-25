# Salesforce Client Credentials Configuration

## Customer Configuration Guide

### Configure Salesforce Client Credentials for ARVault

Create and secure a Salesforce External Client App for server-to-server integration with ARVault.

{% hint style="info" %}
**Purpose:** This guide explains how to configure the OAuth 2.0 Client Credentials flow, authorize the dedicated integration user, retrieve the application credentials, and verify the setup before registering the Salesforce organization in ARVault.
{% endhint %}

## Before you begin

* Confirm that a dedicated Salesforce integration user is active and uses the Salesforce Integration license with the Salesforce API Only System Integrations profile.
* Confirm that the ARVault Integration Access permission set uses the Salesforce API Integration license and is assigned to the integration user.
* Use a monitored customer administrator mailbox for the External Client App contact email.
* Confirm that My Domain is active for the Salesforce organization.

## Configuration overview

{% stepper %}
{% step %}
### Create the External Client App and enable OAuth
{% endstep %}

{% step %}
### Configure OAuth policies and select the Run As user
{% endstep %}

{% step %}
### Pre-authorize the ARVault permission set
{% endstep %}

{% step %}
### Retrieve the Consumer Key and Consumer Secret
{% endstep %}

{% step %}
### Record the Salesforce My Domain URL and complete the verification checklist
{% endstep %}
{% endstepper %}

## Create the External Client App

{% stepper %}
{% step %}
### Open the External Client App Manager

In Salesforce Setup, go to External Client App Manager and select New External Client App.
{% endstep %}

{% step %}
### Enter basic information

| **Field**                | **Value**                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| External Client App Name | ARVault Integration                                                                                            |
| API Name                 | ARVault\_Integration (populated automatically)                                                                 |
| Contact Email            | A monitored customer administrator mailbox. Salesforce sends the credential verification code to this address. |
| Distribution State       | Local for use with a single Salesforce organization.                                                           |
{% endstep %}

{% step %}
### Configure OAuth settings

Select Enable OAuth. The OAuth configuration fields expand.

In Callback URL, enter a valid HTTPS URL. Client Credentials does not use this value, but Salesforce requires it. Suggested value: https://localhost/no-redirect.
{% endstep %}

{% step %}
### Select OAuth scopes

| **OAuth scope**                                                      | **Guidance**                                                                     |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Manage user data via APIs (api)                                      | Required.                                                                        |
| Access the identity URL service (id, profile, email, address, phone) | Required so that /services/oauth2/userinfo returns the username used by ARVault. |
| Access unique user identifiers (openid)                              | Optional.                                                                        |
| Perform requests at any time (refresh\_token, offline\_access)       | Do not select. Client Credentials does not use refresh tokens.                   |
| Full access (full)                                                   | Optional and broader than api. Select only when a specific endpoint requires it. |

{% hint style="warning" %}
**Critical setting:** Scroll to OAuth Flow Enablement and select Enable Client Credentials Flow. Token requests fail when this option is not enabled.
{% endhint %}
{% endstep %}

{% step %}
### Save the External Client App

Select Save to create the External Client App.
{% endstep %}
{% endstepper %}

## Configure OAuth policies

From the saved External Client App, open OAuth Policies from the left navigation or the available tab.

{% stepper %}
{% step %}
### Set permitted users

Set Permitted Users to Admin approved users are pre-authorized.
{% endstep %}

{% step %}
### Configure IP relaxation

Set IP Relaxation to Relax IP restrictions for the initial configuration. After ARVault outbound IP addresses are known, select Enforce IP restrictions and add the addresses as Trusted IPs.
{% endstep %}

{% step %}
### Keep the default refresh token policy

Leave Refresh Token Policy at its default value because Client Credentials does not use refresh tokens.
{% endstep %}

{% step %}
### Set the Run As user

Under Client Credentials Flow, set Run As to the dedicated ARVault integration user.
{% endstep %}

{% step %}
### Save the OAuth policies

Select Save.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
**Important:** The Run As user is required. If it is blank, Salesforce returns invalid\_grant: user hasn't approved this consumer.
{% endhint %}

### Session and security settings

| **Setting**            | **Guidance**                                                                                                                                                                                                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-token lifetime  | The default is approximately two hours. The Integration User profile session timeout can be reviewed under Setup > Profiles > Salesforce API Only System Integrations > Session Settings > Session Times Out After. The organization-wide setting is under Setup > Session Settings > Timeout Value. |
| High Assurance / MFA   | Not applicable to Client Credentials because there is no interactive user session. Ensure the integration profile is exempt if the organization applies stepped-up authentication policies.                                                                                                          |
| PKCE                   | Not applicable. PKCE applies to the Authorization Code flow.                                                                                                                                                                                                                                         |
| Single Logout          | Not applicable because Client Credentials does not establish an interactive user session.                                                                                                                                                                                                            |
| Refresh Token Rotation | Leave disabled because Client Credentials does not use refresh tokens.                                                                                                                                                                                                                               |

{% hint style="info" %}
**Salesforce UI variation:** Some organizations display a separate Policies or Security tab. If present, verify the selected scopes and leave Permission Sets and Profiles unchanged until completing the pre-authorization steps below.
{% endhint %}

## Pre-authorize the integration user

Because Permitted Users is set to Admin approved users are pre-authorized, access must be granted through a profile or permission set. Permission-set-based authorization is recommended because it limits access to the dedicated integration user.

{% stepper %}
{% step %}
### Locate App Policies

Open the External Client App detail page and locate App Policies.
{% endstep %}

{% step %}
### Select the ARVault permission set

Under Select Permission Sets, locate ARVault Integration Access in Available Permission Sets.
{% endstep %}

{% step %}
### Add the permission set

Move ARVault Integration Access to Selected Permission Sets.
{% endstep %}

{% step %}
### Leave profiles empty

Leave Select Profiles empty. Profile-based pre-authorization would authorize every user assigned to that profile.
{% endstep %}

{% step %}
### Save the changes

Select Save at the top of the page.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Older Salesforce UI:** If the organization displays the older Connected App interface, use Permission Sets > Manage Permission Sets, add ARVault Integration Access, and save.
{% endhint %}

## Retrieve the application credentials

{% stepper %}
{% step %}
### Open the External Client App

Go to Setup > External Client App Manager and open ARVault Integration.
{% endstep %}

{% step %}
### Manage consumer details

Open Settings > OAuth Settings > Consumer Key and Secret > Manage Consumer Details.
{% endstep %}

{% step %}
### Enter the verification code

Enter the verification code sent by Salesforce to the External Client App Contact Email.
{% endstep %}

{% step %}
### Copy the credentials

Copy the Consumer Key and Consumer Secret.
{% endstep %}

{% step %}
### Store the credentials securely

Store both values securely. They are required when registering the Salesforce organization in ARVault.
{% endstep %}
{% endstepper %}

{% hint style="danger" %}
**Security:** Treat the Consumer Secret as confidential. Do not include it in tickets, email messages, screenshots, or shared documentation.
{% endhint %}

## Record the My Domain URL

{% stepper %}
{% step %}
### Open My Domain settings

Go to Setup > My Domain.
{% endstep %}

{% step %}
### Copy the Current My Domain URL

Copy Current My Domain URL without a trailing slash.
{% endstep %}
{% endstepper %}

| **Environment** | **URL format**                       |
| --------------- | ------------------------------------ |
| Production      | https://.my.salesforce.com           |
| Sandbox         | https://--.sandbox.my.salesforce.com |

{% hint style="warning" %}
**Required endpoint:** Use the My Domain URL for Client Credentials. Do not use login.salesforce.com or test.salesforce.com as the token endpoint.
{% endhint %}

## Verification checklist

* [ ] My Domain is active and Current My Domain URL is available.
* [ ] The integration user is Active and uses User License = Salesforce Integration and Profile = Salesforce API Only System Integrations.
* [ ] ARVault Integration Access uses License = Salesforce API Integration, not --None--, and is assigned to the integration user.
* [ ] Modify All Data, Modify Metadata Through Metadata API Functions, and Author Apex are enabled. Manage Profiles and Permission Sets is enabled when Profile or PermissionSet metadata is included.
* [ ] The External Client App is created, OAuth is enabled, and a callback URL is present.
* [ ] OAuth scopes include api and id, profile, email. refresh\_token and offline\_access are not selected.
* [ ] Enable Client Credentials Flow is selected.
* [ ] Permitted Users is set to Admin approved users are pre-authorized.
* [ ] Run As is set to the dedicated integration user.
* [ ] ARVault Integration Access appears under Selected Permission Sets, and Select Profiles remains empty.
* [ ] The Consumer Key and Consumer Secret have been retrieved and stored securely.
* [ ] The My Domain URL has been recorded without a trailing slash.

{% hint style="success" %}
**Ready for ARVault:** When every item above is complete, use the Consumer Key, Consumer Secret, and My Domain URL to register the Salesforce organization in ARVault.
{% endhint %}

## Troubleshooting

| **Symptom**                                                                        | **Likely cause**                                                                                              | **Resolution**                                                                                                                  |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Permission-set assignment fails with The user license doesn't allow the permission | The permission set was created with License = --None-- or contains unsupported permissions.                   | Delete and recreate the permission set with License = Salesforce API Integration. The license cannot be changed after creation. |
| API Enabled is not visible                                                         | Expected behavior for the Salesforce API Integration permission-set license.                                  | Continue without selecting API Enabled; the license grants API access automatically.                                            |
| Metadata calls return INSUFFICIENT\_ACCESS                                         | Modify Metadata Through Metadata API Functions is missing or the active token predates the permission change. | Enable the permission and request a new Client Credentials token.                                                               |
| Apex metadata or Tooling API calls return INVALID\_TYPE                            | Author Apex is missing.                                                                                       | Enable Author Apex and request a new token.                                                                                     |
| unsupported\_grant\_type                                                           | Enable Client Credentials Flow is not selected.                                                               | Open OAuth Flow Enablement, select Enable Client Credentials Flow, and save.                                                    |
| invalid\_grant: user hasn't approved this consumer                                 | Run As is blank or the permission set is not pre-authorized.                                                  | Select the integration user under Run As and add ARVault Integration Access to Selected Permission Sets.                        |
| Permission error remains after a permission change                                 | The existing token contains the earlier permissions.                                                          | Request a new token from /services/oauth2/token.                                                                                |
| 404 or an HTML response from the token endpoint                                    | The login.salesforce.com or test.salesforce.com endpoint is being used.                                       | Use the organization's My Domain URL.                                                                                           |
| invalid\_client                                                                    | The Consumer Secret is incorrect, expired, or contains whitespace.                                            | Retrieve the credential again and remove any unintended whitespace.                                                             |

## Salesforce resources

* [OAuth 2.0 Client Credentials Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess%5Foauth%5Fclient%5Fcredentials%5Fflow.htm)
* [Configure an External Client App for OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=xcloud.meta%5Fconfigure%5Fclient%5Fcredentials%5Fflow%5Ffor%5Fexternal%5Fclient%5Fapps.htm)
* [Configure External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure%5Fexternal%5Fclient%5Fapp%5Foauth%5Fsettings.htm)
* [Salesforce Integration User License](https://help.salesforce.com/s/articleView?id=sf.users%5Fintegration%5Fusers.htm)
* [Configure a Connected App for Client Credentials](https://help.salesforce.com/s/articleView?id=xcloud.connected%5Fapp%5Fclient%5Fcredentials%5Fsetup.htm)
