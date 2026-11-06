# IZ Suite Release Notes 26

## IZ Suite 26.4.2

**Release date:** 4 November 2026

#### Overview

IZ Suite 26.4.2 moves IZ Suite onto its new modern experience, makes Code Analysis pull-request aware with a quality gate that respects approved exceptions, brings AI reviews under governed budgets, profiles and access rules, extends Service Health to cloud resources and runtimes, and adds Change Assurance and Compliance to the suite.

This release includes:

* The modern IZ Suite experience: new theme and app frame, Home, Explore, a guided Setup checklist and a sign-in landing page
* Consolidated Platform Analysis and Code Analysis workspaces with shared filters, saved filters, remediation effort and one default version per application
* A cross-product **Findings** workspace and a shared **Assigned work** page
* Code Analysis issue lifecycle and pull requests: new, existing, reopened and fixed findings, webhook-triggered pull request scans and a new-code gate
* Governed false-positive and accepted-risk exceptions, and one quality gate decided by IZ Suite for every scanner, which can now also fail on vulnerable dependencies and deprecated assets
* Security standards: CWE, OWASP and AWS Foundational Security Best Practices references on every rule
* AI reviews with provider connections (Amazon Bedrock, OpenAI and Anthropic, with optional custom endpoints), budgets, alerts, review profiles, AI access rules and source storage
* Service Health resource monitoring, saved sign-ins, OAuth 2.0 and mTLS monitors, service objectives and status page subscriptions
* Dashboards with 16 starter dashboards for every role, new data subjects and attribute filters, export and import of dashboard configurations, a modern Schedules screen, notifications with a delivery log
* Change Assurance and Compliance with shared standards, a risk matrix and treatment plans

#### The Modern IZ Suite Experience

IZ Suite opens in a new modern experience with one navigation across Platform Analysis, Code Analysis, Dependency Insights, Service Health, Change Assurance, Compliance, Quality Control and administration.

* **New theme and app frame:** a refreshed visual theme, one shell with product navigation, and consistent forms, drawers and tables on every screen. A drawer opened from another drawer replaces it instead of stacking, and **Esc** closes the topmost drawer.
* **Sign-in landing page:** the sign-in page explains what IZ Suite does before a user signs in, names the workspace it signs in to, and explains how to apply a licence when the workspace has none.
* **Home and My preferences:** a personal home page with the user's preferences, including saved filters that can be reopened or shared as a link.
* **Explore:** product value by persona, use cases with live screens on sample data or the workspace's own data, and quick navigation.
* **Setup checklist:** a licence-driven checklist that walks an administrator through organizations, repositories, platforms, schedules, email, report storage, AI and Service Health, using the same configuration drawers wherever setup is opened from.
* **Consistent tables:** every table has search, a result count, **Refresh**, **Columns** and **Export** in one row, sortable columns, page sizes from 10 to 200, and icon buttons with tooltips for row actions.
* **Assigned work:** one page, next to **Findings** in the navigation, for the upgrade, maintenance, review and acknowledgment work assigned to people, with a **Remediation** tab for Change Assurance remediation tasks. **My open work** on the home page opens it on the user's own open items.

#### Platform Analysis and Code Analysis Workspaces

* **Overview, Applications and Findings:** Platform Analysis opens on three tabs, and the Code Analysis overview matches it: status cards, an asset type chart and a **Top rules** chart of the most frequent Critical and Blocker findings. Selecting a rule opens the affected applications.
* **Findings across products:** the new **Findings** workspace lists findings from Platform Analysis and Code Analysis together, filtered by product and asset type. Each row opens the application in its own product.
* **Filter bar and saved filters:** organization, platform, environment, attention, severity, category and rule filters sit in one bar with a side drawer for the rest. Every count on the page follows the filters. Filters can be saved, reopened and copied as a link.
* **Attribute filters:** the side drawer can filter applications by the facts recorded for them, such as runtime, region or components. Values are offered for the chosen attribute only.
* **Application page:** fewer, clearer tabs; findings grouped by rule or by file; a **Security standards** card; separate **Dependencies** and **Risk & lifecycle** tabs on Platform Analysis and Code Analysis; and a version comparison. The **AI focus report** tab is offered on Code Analysis as on Platform Analysis, and explains how to request a review when none exists.
* **Remediation effort:** the **Findings** tab estimates the effort to fix the open findings of the latest assessment from each rule's remediation cost, by severity, rule and application, and shows how much can be fixed automatically. Findings under an approved exception are left out.
* **Current version and lifecycle stages:** an application's current version can be marked by hand or detected from production, and one application can be followed across its lifecycle stages.
* **Grouped lists:** lists can show one row per application or every branch and version. Pull requests are labelled with their source and target branch.
* **One default version per application:** each application has exactly one default branch or version. It is the row the grouped lists show and the version reports and dashboards count.
  * Bitbucket, GitHub and Design Center applications follow the repository's default branch.
  * Applications scanned from a pipeline or workstation keep the first branch scanned.
  * Other platforms make a newly discovered version the default.
  * A user can choose the default in **Manage application** with **Make default**. After that, syncs and scans no longer change it. If the default version is deleted, the most recently changed version takes over.

#### Code Analysis: Issue Lifecycle and Pull Requests

Code Analysis now follows each finding from one scan to the next and understands pull requests.

* **Issue lifecycle:** every finding gets a stable fingerprint, so each scan reports what is new, still open, reopened and fixed on that branch.
* **Pull request discovery:** Bitbucket pull requests are discovered with their source and target branches, and each scan records the commit it analysed.
* **Webhook-triggered scans:** a new Bitbucket pull request is scanned as soon as the webhook reports it. Merged and declined pull requests are kept for 30 days.
* **Target branch first:** a pull request is compared with its target branch's latest scan. When the target branch has never been scanned, it is scanned first and the pull request follows as soon as that scan completes, even when **Scan all branches** is off.
* **Pipeline pull requests:** the command-line scanner and the Maven plugin take a new `pullRequestTargetBranch` parameter, so a pull request scanned from a pipeline is compared with its target branch. A pull request whose target branch has not been scanned is judged on all its findings, like a branch, and its gate details say so.
* **Connected repositories:** Bitbucket repositories can be registered and approved for scanning from a connection, with a step-by-step repository setup guide. Anypoint Design Center projects sync one job per business group.
* **Tasks from findings:** findings can be turned into tracked tasks that close automatically when a rescan shows them fixed.
* **Source upload message:** when the workspace keeps source files for review, the scanner says it is uploading them after the quality gate line, so a long upload no longer looks like a stalled scan.

#### Governed Exceptions and the Quality Gate

A finding can be marked a false positive or an accepted risk, approved by someone other than the requester, and kept out of the quality gate until it expires.

* **Exceptions:** an exception covers one finding on every branch and pull request of the application, expires after 1 to 365 days (90 by default) and needs approval by another person with edit access. Approval, revocation and expiry take effect without a rescan.
* **Where excepted findings appear:** they are left out of the findings list and of every current count (application cards, the **Issues** column, workspace counts, **Top rules**). They are listed from the **Exceptions** panel. The assessment history keeps what each scan found.
* **One quality gate, decided by IZ Suite:** the gate is calculated by IZ Suite for every scanner: the command-line scanner, the Maven plugin, the Code Analysis agent, Platform Analysis scans, API Manager and Kubernetes. Each language is judged by its own gate and the scan passes only when every language passes.
* **What the gate judges:** a branch or version is judged on all its open findings with the gate's overall conditions, so a gate only turns green when findings are fixed. A pull request is judged on the findings it introduces with the gate's new-code conditions, or with its overall conditions when it has none.
* **New-code conditions:** the gate editor has an **Overall code** section and a **New code** section. New-code conditions use the issue counts per severity, **Vulnerable Dependencies** and **Deprecated Assets**.
* **Vulnerable dependencies and deprecated assets:** two new gate conditions count the application's own vulnerable components and the deprecation and lifecycle rules that apply to it, as shown on its **Risk & lifecycle** tab. They are optional: only a language whose gate uses them is checked, and existing gates are unchanged. IZ Suite matches the application's components when it judges the gate, so a pipeline does not wait for the scheduled matching, and records the counts with the assessment. Matches reviewed as Fixed, Won't fix or Exception are left out. As new-code conditions they count only what a pull request adds over its target branch. A failed condition names what was found, for example the component and its CVE.
* **Why a gate failed:** each language's row lists the failed conditions, with the section, the metric, the limit and the actual value.
* **Quality Control lists:** quality gates, quality and metric rules and their profiles open with the most recently changed first and have a sortable **Last updated** column.
* **Build pipelines:** with `abortOnQualityGateFailure`, the scanner waits for IZ Suite's gate, so exceptions and new-code conditions decide the build, and the scanner exits with code `1` when the gate fails, so the pipeline step fails. If the gate cannot be obtained the build fails with a clear message. A 26.4.2 scanner against an older server falls back to the previous local calculation; older scanners keep working unchanged.

#### Security Standards

* **References on rules:** built-in rules are mapped to CWE, OWASP Top 10 categories and AWS Foundational Security Best Practices controls (368 controls across the 16 AWS rule packs). OWASP mappings are derived from the CWEs each category lists.
* **Quality Control › Security standards:** a new screen lists each standard's references with the number of mapped rules. Custom rules can be mapped in the rule editor; built-in mappings are shown read-only.
* **Posture card:** the application page shows findings per security standard and drills down to them.
* The previous `cwe-` and `owasp-` rule tags are replaced by these mappings. Other tags are kept.

#### AI Reviews

* **Provider connections:** Amazon Bedrock with the server's own AWS identity (**Auto Discover AWS Bedrock**), Amazon Bedrock with an API key, OpenAI and Anthropic. An OpenAI or Anthropic connection can use a custom endpoint, for example a company AI gateway in front of the provider; the endpoint must be a public HTTPS address. **Check access** explains provider errors and finds the regions that work.
* **One AI setting:** dashboards, reporting, product pages, the assistant and reviews all use the same provider settings, with a workspace switch and one per schedule, off by default.
* **AI access:** a workspace default decides whether applications may use AI, and exceptions per organization, environment or application change it: full access, or AI with findings only and no source. The most specific exception decides. When source is not allowed, no source file or code excerpt reaches the AI provider.
* **Budgets and alerts:** monthly budgets with a usage ledger, and notifications at 80% and 95% of a budget and when a request is refused.
* **Review profiles:** one global profile plus profiles per platform (AWS, Azure, Anypoint Platform) and per asset type, managed under Quality Control. A review combines the matching profiles, the most specific guidance winning.
* **Automatic reviews:** when AI is on, a budget is available and a profile matches, platform scans are reviewed in the same job right after the scan, and code scans from the scanner or CI start an AI evidence investigation. Review summaries open with the assessment's recorded totals.
* **Long model calls:** reviews no longer fail when the AI provider takes longer than a minute to answer. A model call that does not finish within 10 minutes marks the review as failed with a message; the scan itself is not failed.
* **Source storage:** off, excerpts or complete source, stored encrypted in IZ Suite, in Amazon S3 or in Google Cloud Storage, with credentials from the workload identity or a saved sign-in.

#### Service Health

* **Resource monitoring:** monitors for AWS resources and MuleSoft runtimes, with discovery, bulk setup and policy-managed status pages. A setup guide on the **Monitors** tab walks through agent, first monitor, schedule and first check.
* **Monitor sign-in:** HTTP monitors support no sign-in, Basic, client secret, OAuth 2.0 client credentials, mutual TLS, bearer token and API key.
* **Saved sign-ins:** credentials are saved once per workspace and picked by name in monitors and storage settings. Secrets are encrypted and never shown again after saving. Saved sign-ins can also hold AWS access keys and Google service accounts for source storage.
* **Service objectives:** objectives with a free rolling window (days, months or years), monitors attached from the **Monitors** tab, and overview charts in plain status language: meeting target, below target, no data yet.
* **Coverage:** one list of monitoring suggestions, filtered by **All**, **Linked** and **Gaps**.
* **Status page subscriptions:** visitors can subscribe by email with double opt-in. Administrators see and remove subscribers, and subscribers are notified of status changes and maintenance. Maintenance windows are now checked every minute instead of every hour.

#### Operations, Notifications and Dashboards

* **Schedules:** a redesigned **Schedules** screen with **Active** and **Disabled** tabs, one shared frequency picker, one-time platform scans, and internal system jobs hidden. One schedule can cover a whole connected AWS, Anypoint or Azure organization. Execution history uses the same layout.
* **Notifications:** the bell marks notifications read when opened, **Mark all read**, a delivery log with resend, and Change Assurance email.
* **Workspace email:** a workspace either sends through the platform's email settings or, when its email is managed by the workspace, through its own, including a test email from Setup.
* **Dashboards:** AI-assisted dashboards and scheduled reports with PDF generation. Sixteen starter dashboards cover operations, leadership, engineering, Mule runtime and capacity, Change Assurance, compliance and service status, plus one per role: customer trust (sales and account executives), account health, product quality story (marketing), team weekly review (team leads), developer feedback loop, developer productivity, security posture, service reliability and compliance readiness. Starter dashboards are delivered as content updates, so new ones arrive without an upgrade.
* **New dashboard data:** widgets and queries can use security standard findings, scan progression (new and fixed issues per assessment), service incidents, service objectives, IDE developer scans and IDE licences. Dashboard filters can also use the attributes recorded on applications.
* **Export and import dashboards:** a dashboard's configuration (name, description, widgets and report) can be exported to a file and imported in another workspace with **New dashboard** › **An exported dashboard file**. Filters are not exported; the importing workspace applies its own.
* **Dashboards count the default version:** the built-in application, organization, environment and IZ Suite dashboards count each application's default version unless **Show all applications** is chosen.
* **Report storage:** Google Cloud Storage is available alongside the existing providers.

#### Change Assurance and Compliance

* **IZ Suite as a source:** Change Assurance reads this IZ Suite in place, with one asset identity, posture-aware gating and targeted rescans.
* **Release readiness and ticket lineage:** release readiness opens with a drillable summary, and ticket lineage has a story view.
* **Risk matrix:** rank what to fix first by likelihood and impact from real evidence, switch between inherent and residual risk, and assign tracked work from it.
* **Treatment plans:** a treatment plan decides every risk it covers at once; the risk register shows which plan decided each risk.
* **Compliance standards:** 13 supplied standards with their control mappings, kept up to date by IZ Suite; a workspace can switch mappings off or add its own. Control rule counts follow the active mappings.
* **Asset journey and remediation actions:** a plain-language view of related assets on each asset, and actions on findings from the assurance pages.
* **Connections:** per-connection dashboards, consistent reconciliation across connectors, a first sync right after a connection is created, environment promotion chains, and a live frameworks measurement view.
* **Lifecycle rules:** custom lifecycle rules in Dependency Insights can be deleted; AWS deprecation is driven through Dependency Insights.
* **Dependency Insights layout:** **Actions** (upgrade waves and risk review notes) is now a tab of **Updates & maintenance**, and applications without relationship evidence are found with the **Missing relationship evidence** filter of **Asset exposure**.
* **Scale:** the governance pipeline, reachability, evidence ledger and page loads are bounded for large estates.

#### Agent, Scanner and Integrations

* The agent loads every job type it is assigned, and job types added by a licence or a new asset type reach agents that are already running.
* The agent runs AI reviews and uploads source files after a scan, and skips operations an older server does not support.
* The agent and the scanner give up on an unreachable server after 10 seconds and retry the connection twice, instead of hanging for over a minute per call.
* Apex parsing moves to ANTLR 4.13.2 and apex-parser 5.2.0, with the affected Apex rules rewritten.
* **MCP server:** the HTTP headers are now `x-iz-service-url` and `x-iz-access-token`; the previous header names are still accepted. The generated configuration names the server `iz-suite-mcp-server`.
* **VS Code extension:** the Java **Install** button downloads a Java runtime for the machine's operating system and processor and reports download errors.

#### Fixes

* On a new workspace, vulnerabilities and deprecations are available from the start.
* Dependency Insights recomputes deprecations and vulnerabilities only when their inputs change.
* Governance syncs receive their own connection, the governance pipeline schedule no longer fails on a new workspace, and its signing key is generated correctly.
* The assurance snapshot and auditor pack load on large estates, and the frameworks drill-down shows the matching issues.
* The issues report loads faster on large estates.
* Service Health, AI review and dependency labels use the workspace's product names.
* A component removed from an application's code no longer stays in its recorded dependencies, and a component upgraded to a safe version no longer stays listed as vulnerable.
* On a new workspace, content that needs a licence (deprecations and vulnerabilities) waits for the licence and is added on the next content update, instead of being reported as an error.



#### Component Versions in This Release

| Component                                  | Version | Notes                                               |
| ------------------------------------------ | ------- | --------------------------------------------------- |
| IZ Suite server and web                    | 26.4.2  | Modern experience and the features above            |
| Agent and job executors                    | 26.4.2  | Change Assurance, AI reviews and job fixes          |
| Command-line scanner and Maven plugin      | 26.4.2  | Adds `pullRequestTargetBranch`;                     |
| IZ Suite Seed (rules, standards, starters) | 26.4.2  | Adds compliance standards and 16 starter dashboards |
