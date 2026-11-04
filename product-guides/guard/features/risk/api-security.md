# API Security

### Overview

AutoRABIT Guard’s API Security monitors Salesforce connected applications across the Salesforce orgs. It aggregates usage signals and a simple security posture per app, highlighting apps that are unverified, over-permissive (broad OAuth self-authorization), or secure, so that teams can spot integration risk early and prioritize remediation.

### Key Capabilities

* **Cross-org connected app inventory**

AutoRABIT Guard discovers connected apps in use across registered orgs and presents a single inventory.&#x20;

* **Portfolio summary and distribution**

The Total Connected Apps panel shows how many distinct connected apps were found. When any apps are unverified or over-permissive, a pie chart summarizes the split among Secured, Over permissive, and Unverified apps, with numeric callouts:

1. Unverified apps — Apps not installed in at least one org, so admin controls (including access and session policies) cannot be enforced consistently.
2. Over-permissive apps — Installed apps whose OAuth is configured so “All Users May Self-Authorize,” allowing users to grant access without admin oversight.
3. Secure apps — Apps that are properly installed and use safe OAuth settings across the relevant org scope.

* **Top orgs by exposure**

Top 5 Orgs by App Security Exposure ranks orgs with the highest counts of uninstalled or over-permissioned connected apps so you can prioritize those orgs. The table includes Unverified apps and Over-permissive apps per org.&#x20;

* **All Connected Apps table**

The main grid lists every connected app discovered across orgs, with:

1. Connected app name
2. Last usage and total usage
3. Orgs using this app (multi-org chips/names)
4. Counts of orgs in each posture bucket
5. Org filter

* **Export**

An Export action runs `createApiSecurityExport` with an optional org filter (`orgIds`), matching the same org subset you use for analysis—useful for evidence, audits, or offline review (export is scheduled via the platform’s export job pattern).

* **Per-app detail page**

Selecting an app opens a detail view (breadcrumb uses the app name) with summary metrics:

1. Last usage, total usage, total active users
2. Orgs using this app, plus counts for unverified orgs and orgs with over permissions

### Why It Matters?

* Connected apps are API and data boundaries:

&#x20;Each installation or authorization can represent exfiltration paths, shadow IT, or weak OAuth if not governed.

* Self-authorization widens blast radius:

Over-permissive OAuth means users can approve integrations without centralized review, which conflicts with many security and compliance programs.

* Unverified apps bypass standard controls:&#x20;

When an app is not properly installed or verified in an org, policy enforcement is inconsistent, which complicates access reviews and incident response.

* Multi-org tenants need a portfolio lens:

The dashboard and Top 5 list answer “where is our exposure concentrated?” without logging into each org separately.

### Getting Started

1. Open API Security.
2. Wait for the All Apps query to complete; review totals, Top 5 orgs, and the All Connected Apps table.
3. Optionally restrict orgs with the multi-select, then export if you need a filtered report.
4. Select each app to review details

### Benefits

* Visibility

One place to see which apps touch which orgs and how heavily they are used.

* Prioritization

Top 5 orgs and sortable risk counts focus on remediation.

* Operational fit

Filtering, drill-down, and export support recurring reviews and audits.

### Conclusion

API Security in AutoRABIT Guard gives organizations a dashboard-first view of Salesforce connected applications across orgs, with usage metrics, posture classification, org-level prioritization, and actionable explanations in the per-org security dialog. Together, these capabilities make integration risk easier to see, explain, and reduce without treating each org in isolation.

&#x20;
