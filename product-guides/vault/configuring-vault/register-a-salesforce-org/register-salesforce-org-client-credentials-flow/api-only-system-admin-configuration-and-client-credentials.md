# API Only System Admin Configuration and Client Credentials

## ARVault Salesforce Client Credentials Setup with System Administrator Service Account

This guide explains how to configure ARVault for Salesforce OAuth 2.0 Client Credentials flow using a dedicated Salesforce service account with the System Administrator profile. It also includes verification steps using Postman and curl.

### Why use the System Administrator profile?

In Salesforce, **User License** and **Profile** are separate concepts. The user license controls what a user can access, while the profile grants permissions. The System Administrator profile is available only under the standard Salesforce user license. It is not available under the free Salesforce Integration license.

Therefore, “use System Administrator” also means “use the Salesforce user license.” You are not necessarily buying a new license; you are using one of the paid Salesforce user license slots your org already owns.

#### License check before proceeding

Go to **Setup → Company Information** and review the Salesforce row in the User Licenses table.

* If **Remaining ≥ 1**, you can create the ARVault service account at no additional cost because it consumes one unused slot.
* If **Remaining = 0**, deactivate a departed user to free a slot or purchase one additional license.

#### System Administrator vs. Salesforce Integration license

| **Property**                                             | **Salesforce license + System Administrator profile** | **Salesforce Integration license + Salesforce API Only profile**          |
| -------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------- |
| Additional cost                                          | None if Remaining ≥ 1; otherwise one paid license     | Free, typically 5 per org                                                 |
| Access to newly created custom objects                   | **Automatic**                                         | Manual permission set update per object                                   |
| Access to new standard objects from Salesforce releases  | **Automatic**                                         | Manual                                                                    |
| Field-level access on new fields                         | **Automatic**                                         | Often manual                                                              |
| Metadata API operations                                  | Works                                                 | Works with explicit permissions                                           |
| View All Data / Modify All Data effective on all objects | **Yes**                                               | License filters some objects                                              |
| Ongoing maintenance after schema changes                 | None                                                  | Based on Least Privileged Selection, Per-object updates by customer admin |

**Bottom line:** If you have a spare Salesforce license slot, this path costs nothing extra and avoids ongoing permission maintenance. For automated backup, archive, and restore, where new objects and fields appear as the customer schema evolves, this is the right approach.

### Prerequisites

* Salesforce edition: **Enterprise, Performance, Unlimited, or Developer**. Client Credentials is not available on Group or Essentials.
* **My Domain active.** Setup → My Domain must show a Current My Domain URL. Orgs created after Winter ’22 usually have this enabled by default.
* **One available paid Salesforce user license**, preferably Salesforce. Check Setup → Company Information → User Licenses.
* Admin rights to create users, edit profiles or permission sets, configure External Client Apps, and modify Network Access settings.

### Salesforce configuration

{% stepper %}
{% step %}
#### Create the dedicated Salesforce service account

**Before you start:** Confirm that a free Salesforce user license slot exists. Go to Setup → Company Information → User Licenses → Salesforce row → Remaining ≥ 1.

Go to **Setup → Users → Users → New User**.

* **First Name:** ARVault
* **Last Name:** Service Account
* **Alias:** arvsvc
* **Email:** a monitored mailbox for password resets and admin notifications
* **Username:** arvault-service@.com, globally unique across all Salesforce orgs
* **Nickname:** arvault-service
* **User License:** Salesforce, not Salesforce Integration
* **Profile:** System Administrator
* **Time Zone / Locale / Language:** match the org defaults

Uncheck **Generate new password and notify user immediately**. This account does not need interactive login.

Save the user.

The user should now appear in Setup → Users with status **Active**. Do not use this user for UI login; treat it strictly as a machine identity.

**Optional: clone the System Administrator profile**

If your security team does not want to assign the literal System Administrator profile, clone it and remove only permissions that are truly irrelevant to ARVault. Do **not** remove the following permissions:

* View All Data
* Modify All Data
* View Setup and Configuration
* Customize Application
* Modify Metadata Through Metadata API Functions
* Author Apex
* View All Users
* View All Custom Settings
* Bulk API Hard Delete
* Schedule Jobs
* Object permissions required for backup, archive, and restore workloads

For most customers, the standard System Administrator profile is simpler and receives automatic Salesforce permission updates.
{% endstep %}

{% step %}
#### Lock the service account down to API-only

The service account should never authenticate through the Salesforce browser UI.

**Enable API Only User**

1. Create a permission set named ARVault API Only Lockdown.
2. Enable the API Only User system permission.
3. Assign the permission set to the ARVault service account.

{% hint style="info" %}
Use a permission set instead of editing the standard System Administrator profile. Editing the standard profile affects all admins who use that profile.
{% endhint %}

**Reset or freeze the password**

1. Go to Setup → Users and open **ARVault Service Account**.
2. Select **Reset Password**.
3. Use a strong, unguessable password and discard it after setup, or leave the user without an interactive password if your process allows it.

The Client Credentials flow does not use the user password.
{% endstep %}

{% step %}
#### Handle MFA for API access

For most orgs, Client Credentials flow does not require an MFA prompt because it is a server-to-server OAuth flow with no interactive login step. Test first before adding extra MFA configuration.

**Recommended option — Trusted IP Ranges**

* Go to **Setup → Network Access → New**.
* Add ARVault’s outbound IP range or ranges after they are provided.
* Use this for production when you want token requests to work only from known ARVault infrastructure.

**Practical option — test first**

* Run Postman Request 1 from the testing section.
* If the response is 200 with an access\_token, MFA is not blocking the flow.
* If the response includes an MFA-related invalid\_grant, configure Trusted IP Ranges or adjust the org-level MFA policy with the Salesforce admin.
{% endstep %}

{% step %}
#### Create the External Client App

1. Go to **Setup → External Client App Manager → New External Client App**.
   * **External Client App Name:** ARVault Integration
   * **Contact Email:** customer admin email
   * **Distribution State:** Local
2. Under OAuth Settings, check **Enable OAuth**.
3. Set **Callback URL** to https://localhost/no-redirect. It is required but unused for Client Credentials.
   * Manage user data via APIs (api) — required
   * Access the identity URL service (id, profile, email, address, phone) — required for userinfo
   * Access unique user identifiers (openid) — optional
   * Do **not** select Perform requests at any time (refresh\_token, offline\_access)
   * Full access (full) — optional
4. Under OAuth Flow Enablement, check **Enable Client Credentials Flow**.
5. Save.
{% endstep %}

{% step %}
#### Configure OAuth Policies and Run-As user

1. Open the saved External Client App detail page.
2. Open **OAuth Policies**.
3. Set **Permitted Users** to Admin approved users are pre-authorized.
4. Set **IP Relaxation** to Relax IP restrictions initially. Later, tighten this to Enforce IP restrictions after ARVault outbound IPs are known and added to Network Access.
5. Leave Refresh Token Policy at the default. It is not used by Client Credentials.
6. Under Client Credentials Flow, set **Run As** to ARVault Service Account.
7. Save.
{% endstep %}

{% step %}
#### Pre-authorize the app

1. In the External Client App detail page, open **App Policies**.
2. In **Select Profiles**, move System Administrator or your cloned profile to **Selected Profiles**.
3. If you created the ARVault API Only Lockdown permission set, add it under **Select Permission Sets** as well.
4. Save.

Pre-authorizing the profile allows the Run-As sysadmin service account to use the External Client App. Access still requires the Consumer Key and Consumer Secret.
{% endstep %}

{% step %}
#### Retrieve the Consumer Key and Consumer Secret

1. Go to Setup → External Client App Manager and open ARVault Integration.
2. Go to **Settings → OAuth Settings → Consumer Key and Secret → Manage Consumer Details**.
3. Enter the verification code sent to the Contact Email.
4. Copy the **Consumer Key** and **Consumer Secret**.
{% endstep %}

{% step %}
#### Note the My Domain URL

* **Production:** https://.my.salesforce.com
* **Sandbox:** https://--.sandbox.my.salesforce.com

Confirm the value at **Setup → My Domain → Current My Domain URL**. Do not include a trailing slash.
{% endstep %}
{% endstepper %}

### Configuration verification checklist

* My Domain is active and the Current My Domain URL is available.
* Service account user is created with User License = Salesforce.
* Service account profile is System Administrator or an approved clone.
* Service account status is **Active**.
* API Only User permission is enabled for the service account.
* Password is unguessable and discarded, or not used interactively.
* External Client App is created with OAuth enabled.
* OAuth scopes include api and identity/userinfo scopes.
* refresh\_token and offline\_access are not selected.
* Enable Client Credentials Flow is checked.
* OAuth Policies → Permitted Users is set to Admin approved users are pre-authorized.
* OAuth Policies → Client Credentials Flow → Run As is set to ARVault Service Account.
* App Policies include the System Administrator profile or approved clone.
* Optional Trusted IP Ranges are configured for ARVault outbound IPs.
* Consumer Key and Consumer Secret are retrieved.
* My Domain URL is recorded with no trailing slash.

### Expected userinfo response

Postman Request 2 should return user information for the ARVault service account. ARVault stores preferred\_username in SF\_NM\_USER.

```json
{
  "preferred_username": "arvault-service@<customer-domain>.com",
  "user_id": "005xx000000XYZ",
  "organization_id": "00Dxx0000000XXX",
  "name": "ARVault Service Account",
  "email": "<the monitored mailbox>",
  "user_type": "STANDARD"
}
```

This confirms that ARVault is connected as the machine identity rather than a human admin account.

### Common setup mistakes

| **Mistake**                                               | **Symptom**                                                            | **Fix**                                                                                               |
| --------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Used Salesforce Integration license instead of Salesforce | Object queries fail with INVALID\_TYPE on newly created custom objects | Recreate the user with paid Salesforce license and System Administrator profile                       |
| Forgot API Only User                                      | Service account can log into the UI, causing a security audit finding  | Enable API Only User through a permission set assigned to the service account                         |
| Pre-authorized only a permission set, not the profile     | Token mint returns invalid\_grant, user hasn't approved this consumer  | Add System Administrator or cloned profile to App Policies → Select Profiles                          |
| MFA enforced and no IP exemption                          | Token mint fails for an MFA-related reason                             | Add ARVault outbound IPs to Network Access, or verify whether Client Credentials already bypasses MFA |
| Forgot to enable Client Credentials Flow                  | error=unsupported\_grant\_type                                         | Enable Client Credentials Flow in OAuth Settings                                                      |
| Used login.salesforce.com as the token endpoint           | 404 or HTML error page                                                 | Use the org’s My Domain URL                                                                           |

### Comparison summary

| **Setup activity**                    | **Integration User path**                    | **Sysadmin path**                                                  |
| ------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| User license                          | Salesforce Integration, free                 | Salesforce, paid license slot                                      |
| Profile                               | Salesforce API Only System Integrations      | System Administrator or clone                                      |
| Permission set                        | Required and extensive                       | Optional, mainly for API-only lockdown                             |
| Object permission management          | Manual per object                            | Automatic for current and future objects                           |
| MFA handling                          | License may bypass MFA                       | Client Credentials generally bypasses MFA; Trusted IPs may be used |
| Maintenance after new object creation | Manual permission set updates                | None                                                               |
| Best fit                              | Narrow, read-only, fixed-schema integrations | Backup, archive, and restore products such as ARVault              |

### Consumer Key Configuration

Provide the following values to the person completing the ARVault registration:

* **Consumer Key**
* **Consumer Secret**
* **My Domain URL**, with no trailing slash

### Key Salesforce documentation

* [OAuth 2.0 Client Credentials Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess%5Foauth%5Fclient%5Fcredentials%5Fflow.htm)
* [Configure an External Client App for OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=xcloud.meta%5Fconfigure%5Fclient%5Fcredentials%5Fflow%5Ffor%5Fexternal%5Fclient%5Fapps.htm)
* [API Only User](https://help.salesforce.com/s/articleView?id=sf.users%5Fprofiles%5Fapi%5Fonly.htm)
* [Trusted IP Ranges](https://help.salesforce.com/s/articleView?id=sf.security%5Fnetworkaccess.htm)
* [Multi-Factor Authentication and API Access](https://help.salesforce.com/s/articleView?id=sf.security%5Fauth%5Fmfa%5Fapi.htm)
* [Using the UserInfo Endpoint](https://help.salesforce.com/s/articleView?id=sf.remoteaccess%5Fusing%5Fuserinfo%5Fendpoint.htm)
