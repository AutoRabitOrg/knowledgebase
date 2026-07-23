# Synthetic Salesforce Data & Agentforce Test Generation

## 1. Introduction

DataGen is AutoRABIT's platform for generating realistic, schema-aware synthetic data for Salesforce orgs, and for producing test cases for Salesforce Agentforce agents — without ever touching real customer data. It combines fast, pattern-based data generation (Faker) with AI-assisted generation (via large language models) so that generated records are both quick to produce and contextually realistic.

This guide walks through every screen a regular DataGen user works with day to day: connecting a Salesforce org, analyzing an Agentforce agent, generating synthetic records (Record Factory), generating test cases (Test Case Factory), and managing your account. A separate section at the end covers screens that only Administrators and Super Admins can see.

{% hint style="info" %}
A note on scope:\*\*Some features described in the product's menus are still under development and are not yet usable — these are called out explicitly wherever they appear so you don't spend time looking for a button that isn't wired up yet.
{% endhint %}

## 2. Getting Started — The Dashboard

After logging in, you land on the Dashboard — a home screen that gives an at-a-glance summary of your workspace's activity: total data-generation runs, agent analyses performed, synthetic records generated, and test cases produced. It also has shortcut cards straight into the platform's three core workflows, and a “Recent Activity” feed linking back to specific analyses, test-case jobs, or datasets.

If your workspace is brand new and has no activity yet, the Dashboard instead shows a welcome screen prompting you to connect a Salesforce org and run your first agent analysis.

![](<../../.gitbook/assets/Unknown image (426)>)

#### How to use it

* Log in — you'll land on the Dashboard automatically.
* Review the stat tiles at the top (Runs, Analyses, Records Generated, Test Cases).
* Click a module card (“Start Analysis,” “Generate Tests,” or “Generate Data”) to jump directly into that workflow.
* Click any row under “Recent Activity” to reopen that specific analysis, test-case job, or dataset run.

{% hint style="info" %}
Output: This is a navigation/overview screen only — there is nothing to download here.
{% endhint %}

## 3. Connections

Connections is where you link DataGen to your Salesforce org(s), so that every other feature — Agent Analyzer and Record Factory — has an org to read metadata from and generate or push data into. Salesforce is currently the only supported platform (Snowflake and Databricks appear as “Coming Soon” placeholders). You authenticate to each org via OAuth, and connected orgs then appear in a table showing the org ID, environment (Production / Sandbox / Developer), username, and connection health.

![](<../../.gitbook/assets/Unknown image (427)>)

#### How to use it

* From the Connections landing page, click the Salesforce tile.
* Click “Connect Salesforce Org,” which redirects you to Salesforce's OAuth login/consent screen.
* Approve access — DataGen returns you to the org list with the new connection registered.
* Use the row actions to Reauthenticate (refresh expired tokens), Edit the org's display name/type, Update Connected App Credentials (if the Consumer Key/Secret were rotated in Salesforce Setup), or Delete the connection.

\*\*Output:\*\*No file output — this screen manages the org credentials/connections used by the rest of the platform.

{% hint style="info" %}
Caution: Connecting a Production org is discouraged and triggers a warning dialog — DataGen is built for test-data use cases, not for generating or pushing data into live production orgs.
{% endhint %}

## 4. Agent Analyzer

Agent Analyzer reads an existing Agentforce agent directly from a connected Salesforce org and reverse-engineers its complete structure: every topic (sub-agent), the actions and instructions inside each topic, any top-level “direct” actions, and the Salesforce objects the agent likely reads from or writes to. The result is a clear map of what an agent can do and which data it touches — so you can generate realistic test data or test cases that actually exercise the agent's real capabilities, instead of guessing.

![](<../../.gitbook/assets/Unknown image (428)>)

#### How to use it

* Click “New Analysis,” then pick the Salesforce org containing the agent.
* Select the specific Agentforce agent to analyze from a list pulled live from that org.
* Click “Analyze Agent” — a progress timeline shows each metadata-reading step (topics, actions, instructions) as it completes.
* Review the Agent Structure screen: expandable sections for Sub-agents/Topics, Direct Actions, Identified Objects (with a CRUD summary and confidence level), and any Scenario Stories.
* Save the analysis, then use “Generate Data” or “Generate Test Cases” (available from the results screen and from the saved-analyses list) to hand this analysis straight into Record Factory or Test Case Factory.
* Revisit saved analyses anytime from the Agent Analyzer home screen, or delete ones you no longer need.

{% hint style="info" %}
**Output:** No file download from this screen itself — the analysis is saved in-app and consumed by Record Factory (Agent-Aware mode) and Test Case Factory (Agent-Aware mode).
{% endhint %}

## 5. Record Factory (Synthetic Data Generation)

Record Factory is DataGen's core synthetic-data engine. It generates realistic, schema-aware Salesforce records — with correct parent-child relationships — that you can use to populate sandboxes or drive Agentforce testing, without touching real customer data. You pick a Salesforce org and one or more objects, define how many records you need (including per-parent counts for child objects, e.g. “5 Contacts per Account”), and choose how each field's value should be generated.

![](<../../.gitbook/assets/Unknown image (429)>)

### Faker vs. AI field generation

Faker: fast, deterministic, pattern-based values (names, emails, addresses, phone numbers) that respect the field's data type and, where relevant, locale.

AI (LLM): slower but smarter — values that better respect field context, picklist meaning, and coherence across related fields on the same record. AI generation only runs while your tenant is within its configured monthly AI token budget; once that budget is reached, AI-selected fields automatically and silently fall back to Faker so generation never simply fails.

### Two usable generation modes

Schema-First: you manually pick objects, build the parent-child hierarchy, and configure fields — best when you already know which objects/fields you need.

Agent-Aware: you pick a previously saved Agent Analyzer analysis; DataGen's AI proposes an object hierarchy and record-count strategy (marking objects as Primary, Supporting, or Reference) based on what the agent actually reads/writes, which you then review and can adjust before generating.

{% hint style="info" %}
**Coming soon:** Two other modes shown in the “how do you want to generate” dialog — “AI Schema Builder” (free-text prompt) and “Guided Wizard” — are marked Coming Soon in the product and are not yet functional.
{% endhint %}

#### How to use it

* From Record Factory home, click “Generate Dataset” → choose “Schema-First” (or “Agent-Aware” and pick a saved analysis).
* Pick the Salesforce org, then search and add an object — it becomes a root of the hierarchy.
* Set the number of records for that object; optionally click “Add Children” to attach related child objects and set records-per-parent.
* Click “Fields” on any object to review or override each field's generation strategy (Faker vs. AI) and locale — grouped fields (like a compound Address) share one strategy.
* Click “Generate” — name the dataset, review any active Salesforce validation rules that will be respected, and confirm.
* Track progress on the run's detail page (per-object progress bars), then download each object's data as CSV, or push the generated records into a Salesforce org.

\*\*Output:\*\*A CSV download per object, plus a JSON “generation metadata” file per object recording which fields were AI-generated vs. Faker-generated. After pushing to an org, a downloadable ID map (linking generated record IDs to the real Salesforce IDs created) and a push activity log are also available.

{% hint style="info" %}
**Dataset expiry:** Generated datasets have an expiry date shown on the run and are automatically deleted if not downloaded, used, or pushed within that window.
{% endhint %}

## 6. Test Case Factory

Test Case Factory generates AI-authored test-case scenarios formatted for Salesforce's Agentforce Test Center, giving QA teams ready-to-import test coverage for an agent without hand-writing test scripts. Generation is driven from a saved Agent Analyzer analysis (Agent-Aware mode): the AI reads the agent's topics, actions, and instructions and produces realistic conversational test scenarios with expected outcomes that map to what the agent actually does.

![](<../../.gitbook/assets/Unknown image (430)>)

#### How to use it

* Click “Generate Tests,” then select “Agent-Aware” in the mode dialog.
* Pick a previously saved Agent Analyzer analysis from the list.
* Set generation parameters (e.g., number/type of test cases) and start generation — a progress step shows the job formatting output for Agentforce Test Center.
* Review the generated test cases in the results view, then download them.

\*\*Output:\*\*The generated test case set as CSV or JSON, formatted for direct import into Agentforce Test Center. Past generation jobs remain listed with a per-job CSV download.

{% hint style="info" %}
Coming soon: A second mode, “Prompt-Based” (describe your agent/tests in plain English, no prior analysis needed), appears in the mode dialog but is currently disabled and labeled Coming Soon — it is not yet clickable.
{% endhint %}

## 7. Account & Settings

Settings is your personal account-management screen. You can update your display name, change your password, and toggle email-based multi-factor authentication (MFA) at login (always on for admin accounts). It also includes an “AI Usage” panel showing your workspace's monthly AI-token consumption for Record Factory's AI-based field generation, with a progress bar toward the admin-configured monthly cap — once that cap is reached, AI generation automatically falls back to Faker rather than failing.

![](<../../.gitbook/assets/Unknown image (431)>)

#### How to use it

* Navigate to Settings from the user/profile menu.
* Update Display Name and click “Save Changes” (email is fixed/read-only).
* To change your password, fill in current/new/confirm password and submit.
* Toggle “Email verification at login (MFA)” on or off (admins cannot disable it).
* Review “AI Usage” to see tokens used this month, tokens remaining, and total AI-generated records this month.

{% hint style="info" %}
Output: No downloads — this page is entirely account configuration.
{% endhint %}

## 8. Audit Logs

Audit Logs is a searchable, chronological record of user actions and system events across your workspace — logins, connection changes, dataset generation/push events, credential updates, and more — each entry capturing the acting user, IP address, browser, and timestamp. Every logged-in user can see this page; regular users see only their own actions, while admins see the entire workspace's activity.

![](<../../.gitbook/assets/Unknown image (432)>)

#### How to use it

* Open Audit Logs from the sidebar.
* Filter by Entity Type and/or Action using the dropdowns.
* Click a row to expand and see full details, including a raw CEF-formatted security event string.
* Click “Export CEF” to download the log in Common Event Format for ingestion into external SIEM/security tooling.

{% hint style="info" %}
**Output:** A CEF-format export file of audit events, for security/compliance tooling.
{% endhint %}

## 9. API Tokens & Developer Access

For users who want to call DataGen programmatically — for example, from a CI pipeline or an internal script — the platform offers personal API tokens and a small developer hub.

### API Tokens

Lets you create scoped API tokens (Bearer tokens), choosing which modules the token can access (Record Factory, Connections, Schema discovery, Push, Datasets, Runs, Recipes) and an optional expiry, for programmatic access to DataGen outside the web UI.

![](<../../.gitbook/assets/Unknown image (433)>)

#### How to use it

* Click “Generate Token,” name it, select the module scopes it needs, and choose an expiry (30/90/180 days, 1 year, or never).
* Click “Generate Token” — the raw token value is shown exactly once in a copy-to-clipboard dialog and cannot be retrieved again after closing.
* The token then appears in the list showing its prefix, granted scopes, status (Active/Revoked/Expired), and last-used date.
* Click “Revoke” on any active token to immediately invalidate it.

{% hint style="info" %}
**Output:** The generated API token string, shown once — copy and store it securely.
{% endhint %}

### Developer hub

A small hub for integrating with DataGen's API, organized into three tabs: API Tokens (same screen as above), API Docs (an interactive Swagger UI plus the raw OpenAPI 3.0 spec, for browsing and testing every DataGen API endpoint), and Getting Started (a step-by-step integration guide covering token generation, required headers/auth, available scopes, and example API calls).

![](<../../.gitbook/assets/Unknown image (434)>)

{% hint style="info" %}
**Navigation caveat:** Both of these pages are currently reachable only by navigating directly to their URL — they are not yet linked from the main sidebar navigation or user menu.
{% endhint %}

## 10. For Administrators

The following screens are only visible to Admin and Super Admin accounts. They control workspace-wide (tenant-level) settings that apply to every user in that tenant.

### 10.1 Tenants

The Tenants screen is where Super Admins manage every workspace (“tenant”) on the platform: activation status, Production access, AI Access, and each tenant's monthly AI token limit. Both Production access and AI Access are off by default for a new tenant.

\*\*AI Access:\*\*a per-tenant on/off switch. While it's off, that tenant's users can still use Record Factory, but every field generates via Faker only — AI-based generation and every other AI-powered feature (Agent Analyzer's deep analysis, Test Case Factory, etc.) is blocked for that tenant.

\*\*Max AI Tokens:\*\*the tenant's monthly AI token budget. This field only becomes editable once AI Access is turned on for that row. Enter a new value and click the checkmark to save — this is the actual, enforced limit: once a tenant's combined AI usage for the month reaches this number, AI-based generation across every feature for every user in that tenant automatically falls back to Faker (or is blocked, for features that require AI) until the next month or until an admin raises the limit. Click the reset icon next to a custom limit to return that tenant to the platform's global default instead.

![](<../../.gitbook/assets/Unknown image (435)>)

#### How to use it

* Open Tenants from the Administration section of the sidebar (Super Admin only).
* Use the status dropdown to filter by Pending Activation, Awaiting Verification, or Activated.
* Click a tenant's Production or AI Access button to toggle that access on/off.
* Once AI Access is on, edit the Max AI Tokens field and click the checkmark to save.
* Click “Configure” to set an Additional AI Configuration override for that tenant (display-only today).
* For Pending Activation tenants, click “Activate” or “Resend Activation Mail” to manually activate the tenant and (re-)send its activation email.

### 10.2 Generation Config

Sets the platform-wide default AI generation behavior — the same monthly token cap used as the fallback default for any tenant that hasn't been given a custom Max AI Tokens value on the Tenants screen, plus limits like maximum AI-generated records and guardrail settings.

![](<../../.gitbook/assets/Unknown image (436)>)

### 10.3 Properties

System-level configuration keys/values used by the backend (API credentials and similar platform properties).

![](<../../.gitbook/assets/Unknown image (437)>)

### 10.4 Prompt Registry

Manages the library of AI prompt templates used across every AI-powered feature (Record Factory field classification, Agent Analyzer, Test Case Factory, and more) — admins can view, edit, and version these prompts without a code deployment.

![](<../../.gitbook/assets/Unknown image (438)>)

### 10.5 Token Usage

A workspace-wide dashboard of AI token consumption — broken down by user for visibility into who is generating the most AI usage — while the limit and remaining-budget figures shown reflect the tenant's actual configured cap from the Tenants screen.

![](<../../.gitbook/assets/Unknown image (439)>)

### 10.6 Data Pools

A read-only, admin-facing view into the cache of previously AI-generated field values that DataGen reuses to speed up future generation runs and reduce AI token spend.

![](<../../.gitbook/assets/Unknown image (440)>)

## Glossary

| **Term**                | **Meaning**                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tenant / Workspace**  | An organization's isolated account on DataGen. Every user, connection, dataset, and setting belongs to exactly one tenant.                                                                                            |
| **Faker**               | Fast, deterministic, pattern-based synthetic value generation (e.g. realistic names, emails, addresses) that doesn't call an AI model.                                                                                |
| **AI / LLM generation** | Field values produced by a large language model for better contextual realism and cross-field coherence, gated by the tenant's AI Access toggle and monthly token budget.                                             |
| **Agentforce**          | Salesforce's platform for building conversational AI agents; Agent Analyzer and Test Case Factory are both built around understanding and testing these agents.                                                       |
| **Agent-Aware mode**    | A generation mode (in both Record Factory and Test Case Factory) that uses a saved Agent Analyzer analysis to automatically propose a relevant object hierarchy or test scenarios, instead of requiring manual setup. |
| **Dataset run**         | One execution of Record Factory — a named batch of generated records across one or more objects, downloadable and optionally pushable to a Salesforce org.                                                            |
| **Push**                | Sending a generated dataset's records into a real Salesforce org via the Composite/Bulk API, producing a downloadable ID map of generated-to-real record IDs.                                                         |
