# API Security

### Overview

API Security shows every connected app and external client app across your Salesforce orgs, checks how each one is set up and tells you what to fix first. It also helps you prepare for Salesforce's move from connected apps to external client apps.

API Security helps you answer three questions quickly:

* Which apps are risky?
* Why do they matter in Salesforce?
* Which apps are still connected apps and need to move?

Each app is checked for risky OAuth settings, weak authorisation controls and weak network, session and certificate settings. Problems are raised as findings with a severity of Critical, High, Medium or Low. Every finding explains what the setting means in Salesforce, why Guard flagged it, the evidence Guard read and what to do next.

{% hint style="info" %}
API Security 2.0 replaces the old Secured, Over-permissive and Unverified statuses. Apps are now assessed through individual findings with a severity.
{% endhint %}

### Why it matters

Connected apps and external client apps are the doors through which integrations reach your Salesforce data. A weak OAuth setting, a wildcard callback URL or a long-lived refresh token can give an attacker a way in without a password. API Security shows you where these gaps are across every org, so you can close the most serious ones first.

Salesforce is also retiring connected apps. API Security shows you exactly which ones are left, so you can plan the move to external client apps.

### Navigation path

`Guard → Risk → API Security`

### Before you start: Salesforce permissions

Before a scan starts, Guard checks which permissions the Salesforce user connected to Guard has. If any are missing, Guard still runs the checks it can and tells you what it skipped.

| Permission                                                         | Needed for                                                                                          | What happens if it is missing                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| API Enabled                                                        | Everything                                                                                          | The scan cannot run. Guard tells you which permission is missing.                                                                   |
| View Setup and Configuration                                       | Everything                                                                                          | The scan cannot run. Guard tells you which permission is missing.                                                                   |
| View All External Client Apps                                      | External client app checks                                                                          | Connected app checks still run. External client app checks show as Not assessed.                                                    |
| Customize Application                                              | Connected app checks, and app usage data such as last used date and active users for both app types | Connected app checks and usage data show as Not assessed.                                                                           |
| View All Profiles                                                  | Showing which profiles have admin-approved access to an app                                         | Guard cannot show the profile behind an admin-approved access finding.                                                              |
| Modify Metadata Through Metadata API Functions, or Modify All Data | Optional. Unlocks the checks marked Metadata below.                                                 | All read-only checks still run. Checks that need the Metadata API show as Not assessed. Risk Assessment already needs one of these. |

For the full list of permissions Guard needs, see [Integration User](../../getting-started-with-guard/integration-user-license.md).

#### Permission banner

If Guard is missing a permission, a banner at the top of the page tells you:

* Which permission is missing
* Which checks or data it affects, for example "Connected app checks were not run" or "Some checks need Metadata API access"
* How to fix it, usually by asking a Salesforce admin to add the permission to the integration user

Checks Guard skipped show as **Not assessed**.&#x20;

{% hint style="info" %}
This module only uses the Metadata API to read information. API Security never uses it to change, restrict or disable anything in your org.
{% endhint %}

### Getting started

1. Check the Salesforce user connected to Guard has the permissions listed above.
2. Open Risk, then API Security.
3. If a permission banner appears, ask your Salesforce admin to add the missing permissions.
4. Review the summary and the Recommended actions panel.
5. Use the All apps table to find the apps and orgs you want to look at first.
6. Open an app to review its findings and follow the recommended actions.
7. Deal with Critical risks first. If you cannot resolve one, uninstall the app or contact the app's provider.
8. Plan the move from connected apps to external client apps using the Migrate connected apps group.

### API Security overview

#### Summary

The top of the page shows:

* Connected apps: how many connected apps Guard found. Salesforce is retiring connected apps, so every one of these needs to migrate.
* External client apps: how many apps already use the newer Salesforce model.
* Open risks: the number of open risks across all apps. A risk found on more than one app is only counted once.

#### Recommended actions

The Recommended actions panel shows the actions that will reduce risk the most. It has up to three groups:

* **Fix the top risks:** up to three risks, ranked by severity and then by how many orgs are affected. Each one shows the risk, its severity, the app and the orgs affected. Select an org to open the risk detail.&#x20;
* **Migrate connected apps:** every connected app that needs to move to an external client app, with the number of orgs using it and its open risks. Select an app to open its detail view.
* **Review apps not used recently:** apps with no usage in the last 90 days. This group only appears when there is at least one. Select an app to review it before you deactivate it in Salesforce.&#x20;

#### All apps table

The **All apps** table shows one row per app across all the orgs Guard can see. Each row shows:

* App name. Select it to open the app's detail view.
* Last usage
* Total usage across orgs
* Orgs using this app. Select the count to see each org and the connected user in that org.
* Connection type: Connected app or External client app
* Open risks, or No open risks when there are none

An app used in several orgs appears once, with its usage and risks combined. Guard only groups apps when it can confidently see they are the same app.&#x20;

### App detail view

Select an app to see its findings. Each finding explains itself in plain Salesforce terms:

* What this means in Salesforce: a short explanation of the setting, policy or scope
* Why Guard flagged it: the exact reason for the finding
* Recommended action: what the admin should change or review

The detail view also lists any checks Guard could not run for this app, and why.

You can sort and filter findings by severity.

#### Needs migration

Every connected app shows a Needs migration note, because Salesforce is retiring connected apps. The note links to Salesforce's guidance on moving to external client apps.

### Severity levels

| Severity | What it means                                                                                                   | Used for                                                                                                                             |
| -------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Critical | Directly allows account takeover, privilege escalation or exposure of data to people who should not see it.     | Unmanaged or highly exposed OAuth paths, such as unverified app usage, broad scopes with self-authorisation or unsafe callback URLs. |
| High     | Removes a key defence or gives a broad group the power to do damage, but needs another failure to be exploited. | Broad access controls, relaxed network controls, client credentials and expired certificates.                                        |
| Medium   | A hardening control that weakens defence in depth when missing.                                                 | Token lifetime, PKCE, token exchange, session hardening and certificates close to expiry.                                            |
| Low      | Good hygiene with limited impact on its own.                                                                    | Missing ownership or support details, such as a contact email.                                                                       |

{% hint style="danger" %}
Critical risks need action straight away. Follow the recommended action for the finding. If you cannot resolve the risk yourself, uninstall the app or contact the app's provider to have it fixed.
{% endhint %}

### What Guard checks

Guard runs the same checks on connected apps and external client apps wherever Salesforce exposes the same setting. Read-only checks run with the standard permissions above. Metadata checks need Metadata API access and show as Not assessed without it.

| Check                                                                   | Severity | Connected apps | External client apps | What to do                                                                                                                          |
| ----------------------------------------------------------------------- | -------- | -------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Unverified app has OAuth tokens in use                                  | Critical | Read-only      | Does not apply       | Review the token activity. If you do not recognise or approve the app, revoke its tokens and require users to use a registered app. |
| Broad OAuth access (full or refresh token scope) can be self-authorised | Critical | Metadata       | Read-only            | Narrow the scopes where possible and require admin-approved users.                                                                  |
| Callback URL uses a wildcard or `http://`                               | Critical | Metadata       | Metadata             | Replace it with exact HTTPS URLs owned by the app.                                                                                  |
| Client credentials flow is enabled                                      | High     | Metadata       | Read-only            | Confirm a trusted service needs it. If so, keep scopes narrow and limit who can use it.                                             |
| IP restrictions are relaxed or bypassed                                 | High     | Metadata       | Read-only            | Enforce IP restrictions unless the app has a documented need to run from changing locations.                                        |
| Any user can authorise the app                                          | High     | Read-only      | Read-only            | Switch to admin-approved users and assign only the users, profiles or permission sets that need it.                                 |
| Admin-approved access is granted to broad profiles or permission sets   | High     | Read-only      | Read-only            | Replace broad access with smaller groups. Guard shows which profile or permission set caused the finding.                           |
| JWT certificate has expired                                             | High     | Metadata       | Metadata             | Replace the certificate and check the integration still authenticates.                                                              |
| Refresh tokens are valid until revoked                                  | Medium   | Read-only      | Read-only            | Set a refresh token expiry period that fits the app and revoke old tokens.                                                          |
| Refresh token rotation is turned off                                    | Medium   | Metadata       | Metadata             | Turn on refresh token rotation unless the app cannot support it.                                                                    |
| PKCE is not required                                                    | Medium   | Metadata       | Metadata             | Require PKCE for OAuth flows that support it.                                                                                       |
| Token exchange is enabled                                               | Medium   | Read-only      | Read-only            | Turn it off unless the app has a real need for it.                                                                                  |
| JWT certificate expires within 30 days                                  | Medium   | Metadata       | Metadata             | Rotate the certificate before it expires.                                                                                           |
| High assurance session is not required                                  | Medium   | Read-only      | Read-only            | Require high assurance sessions for apps that reach sensitive data or privileged functions.                                         |
| Session timeout is longer than 8 hours                                  | Medium   | Metadata       | Read-only            | Shorten the session timeout unless there is a documented need.                                                                      |
| No contact email is set                                                 | Low      | Metadata       | Read-only            | Add a contact email or owner group so admins know who to contact before changing the app.                                           |

External client apps are never flagged as unverified.

#### Not assessed

A check shows as Not assessed when Guard could not run it. The reason is shown with the check and could be one of:

* The connected Salesforce user does not have Metadata API access. Ask a Salesforce admin to add Modify Metadata Through Metadata API Functions or Modify All Data to the integration user.
* Salesforce did not return metadata for this connected app. This can happen with packaged or Salesforce-owned apps, so they may only get the read-only checks.
* The connected Salesforce user does not have View All External Client Apps.
* The connected Salesforce user does not have Customize Application.

### Scan times

Checks that use the Metadata API take longer than read-only checks, so scans of large orgs may take longer than before.

### Export

Use Export to download API Security results for all orgs or a filtered set of orgs. This is useful for audits, evidence or offline review. You will receive an email when the export is ready.
