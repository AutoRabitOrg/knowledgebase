# Refreshing a Salesforce Sandbox

#### Take care when refreshing a Sandbox org

A full Salesforce sandbox refresh creates a new Org ID, so Guard cannot re-link the existing connection. Plan before refresh to reduce instability and configuration loss.

#### Before the refresh

1. Export or document your policies
   * Record policy name, scope, rules and notification settings
   * Use `guard get baseline-policy` and `guard get policy-intent` to capture definitions programmatically using the Guard CLI
2. Export any historical data you need to retain
3. Note the Guard connection details
   * Org display name, purpose, enabled features, connection type (OAuth vs External Client App)
   * Login URL and connected user
4. Do not delete the Guard org entry yet
   * Deletion is irreversible for Guard-held data
   * Keep the entry until you are ready to reconnect

#### During the refresh

Complete the Salesforce sandbox refresh as normal. Expect a new Salesforce Org ID when the refresh finishes.

#### After the refresh: reconnecting in Guard

Step 1 — Wait before making changes

Allow 15–30 minutes after the Salesforce refresh completes before modifying Guard connections. This gives async cleanup and sync jobs time to settle if a prior delete was attempted.

Step 2 — Choose your path

| Scenario                          | Action                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Token expired only, same Org ID   | Use Reauthenticate on the org detail page                                                              |
| Full sandbox refresh (new Org ID) | Delete old entry, then register refreshed sandbox                                                      |
| Unsure                            | Check Salesforce Setup → Company Information for the Org ID. If it changed, you must delete and re-add |

Step 3 — Delete the old Guard entry (if Org ID changed)

1. Open Salesforce Orgs → select the pre-refresh org
2. Review the delete warning and confirm you have documented policies
3. Click Delete Org
4. Wait for the success toast before proceeding

Step 4 — Register the refreshed sandbox

1. Add a new Salesforce org connection with the same display name and purpose as before
2. Complete OAuth or External Client App authentication against the refreshed sandbox
3. Enable the same Guard features (Change Monitoring, Permission Explorer, etc.)

Step 5 — Recreate configuration

| Configuration                        | How to restore                                                     |
| ------------------------------------ | ------------------------------------------------------------------ |
| Authorization policies               | Recreate manually, or via Guard CLI `admin baseline-policy create` |
| Change Monitoring notification rules | Recreate, or apply from template                                   |
| Permission Explorer queries          | Recreate saved queries                                             |

#### What cannot be transferred today

* Change Monitoring historical records
* Authorization Policy violation history
* Classification analysis history
* Any other data tied to the pre-refresh Guard identification

Policies can be recreated with the same rules, but they are new objects linked to the new Guard identification.

#### Reducing post-refresh instability

* Avoid deleting and immediately re-adding multiple orgs in quick succession
* Complete one org reconnect before starting the next
* If the Salesforce Orgs page hangs, wait 30 minutes and retry
* Ensure only one admin performs the delete/re-add
