---
hidden: true
---

# Agentic Code Analysis User Guide

{% hint style="info" %}
**How to Use this Guide**

⁉️ Not sure what Agentic Code Analysis is? → Start [here](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-1.-what-is-agentic-code-analysis)

💻 Just want to know how to get setup? → Start [here](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-2.-api-keys)

💡 Already set up for your scans and want to learn about additional capabilities? → See what you can do with [your results](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-7.-viewing-results), and learn about [additional commands](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-9.-command-reference).
{% endhint %}

### What is Agentic Code Analysis? <a href="#id-1.-what-is-agentic-code-analysis" id="id-1.-what-is-agentic-code-analysis"></a>

Get actionable, high-quality insights on your Salesforce code.

#### Features: <a href="#features" id="features"></a>

* **Drag and drop rule creation.** Drop in a policy document. Guard extracts the requirements and translates them into rules.
* **Fully customisable.** Review, edit, and toggle each rule on or off before you run it.
* **Downloadable patches.** Get suggested code fixes and add them to your code base.
* **Transparent cost reporting.** Credit usage is displayed per scan.

### API Keys <a href="#id-2.-api-keys" id="id-2.-api-keys"></a>

The API Keys page lets tenant administrators create long-lived API keys used by automation (Bitbucket Pipelines, GitHub Actions, Jenkins, local CLI) to authenticate to Guard without an interactive Keycloak login. The CLI reads the key from the `GUARD_API_KEY` environment variable or the `--api-key` flag.

Only users with Guard administration permissions can access API Keys. Keys are tenant-scoped so one key works for all repositories registered within your tenant environment (unless your admin configures restrictions).

#### Page overview <a href="#page-overview" id="page-overview"></a>

| Area                | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| **Key list**        | Active keys with name, created date, last used (if shown), and status. |
| **Create key**      | Opens a dialog to name the key and generate a secret.                  |
| **Revoke / delete** | Immediately invalidates a compromised or rotated key.                  |

#### How to generate an API key <a href="#how-to-generate-an-api-key" id="how-to-generate-an-api-key"></a>

1. Sign in to **AutoRABIT Guard** (e.g. `https://fc-dev.autorabit.com` for dev).
2. Open **Settings** → **API Keys** (or **Integrations** → **API Keys**, per your build).
3. Click **Create API Key** (or **Generate key**).
4. Enter a **descriptive name** (e.g. `bitbucket-pipeline-prod`, `developer-laptop-jane`).
5. Confirm creation.
6. **Copy the secret immediately** — it is shown **once**. Store it in your CI secret store (Bitbucket repository variables, GitHub Secrets, Vault, etc.).

#### Recommended Security practices <a href="#recommended-security-practices" id="recommended-security-practices"></a>

* Use one key per environment (dev / staging / prod).
* Rotate on schedule or after personnel changes.
* Use CI secret variables over plain text in `bitbucket-pipelines.yml`.

### Repositories <a href="#id-3.-repositories" id="id-3.-repositories"></a>

The Repositories page links your source control repositories to AutoRABIT Guard so that:

* Scan results are attributed to the correct repo.
* PR-scoped reviews (`--pr`) can map CI environment variables to the registered repo.
* History, dashboards, and filters work by repository.

{% hint style="info" %}
Repositories are added to Guard automatically when a scan is first executed from the Guard CLI.
{% endhint %}

You can find your registered repositories under **Agentic Code Analysis** → **Repositories** in the navigation menu. This page manages registered repositories and repository-level Agentic Code Analysis settings.

Each entry shows the repository Name, URL, Provider (e.g. GitHub, Bitbucket Cloud), Created At date, Visibility (Public / Private), and Status, along with an Actions menu for managing the repository.

#### How to Manually Register a Repository (optional) <a href="#how-to-manually-register-a-repository-optional" id="how-to-manually-register-a-repository-optional"></a>

You **do not need to** manually register a repository before using the AutoRABIT Guard CLI. However, if you choose, you can do so by:

1. In AutoRABIT Guard, go to **Agentic Code Analysis** → **Repositories**.
2. Click **Add Repository**.
3.  Provide the following:

    * Repository Name

    A label for your reference (leave blank to derive the name automatically from the URL).

    * Repository URL

    The full URL, e.g. `https://github.com/org/repo`.

    * CLI Timeout

    The maximum time (in minutes) a Guard CLI execution can run. If a run exceeds this limit it will be automatically stopped (e.g. 30 minutes).

    * Visibility

    Set the repository to Private or Public.

    * Enable tests analysis: Toggle on to analyze test files. When enabled, you can configure Tests Folders — glob patterns whose files are treated as tests. These files are excluded from copy-paste detection and used for test analysis (e.g. `**/test/**`, `**/*.spec.*`, `**/*Test.java`).
    * Sources Exclusions

    Folder glob patterns excluded from all scans, additive to `.gitignore` (e.g. `**/node_modules/**`, `**/dist/**`, `**/build/**`).

    * Severities included in AI review

    Select which severities are reviewed by AI. Only selected severities will be reviewed by AI; unselected severities will be reported without AI review.

    * Authenticate Repository (Optional) → Access Token

    A personal or service account token from your provider (GitHub, GitLab, etc.). AutoRABIT Guard uses it to authenticate CLI calls and post recommendations as pull request comments on your behalf.
4. Save. The repository appears in the list.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-07-13 134723.png" alt="" width="374"><figcaption></figcaption></figure>

#### Repository Actions

Each repository has an **Actions** menu that lets you manage that specific repository and its Agentic Code Analysis settings:

| Action          | Description                                                                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit            | Edit the repository's registration details and scan settings (name, CLI timeout, visibility, tests analysis, exclusions, severities, access token, etc).                                                                                                                                          |
| Re-Authenticate | Update or refresh the access token used to authenticate.                                                                                                                                                                                                                                          |
| Rules           | View and customise the ruleset applied to this repository (edit or toggle Standard rules and create Custom Rules (see [Customise your Ruleset](https://app.gitbook.com/s/9vAxMuDrkUkB4OXlH9CL/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-4.-customise-your-ruleset)). |
| Analyse Rules   | Run AI-powered noisy rule detection.                                                                                                                                                                                                                                                              |
| Scan Branch     | Trigger a scan of a branch for this repository.                                                                                                                                                                                                                                                   |
| Delete          | Remove the repository.                                                                                                                                                                                                                                                                            |

### Customise your Ruleset <a href="#id-4.-customise-your-ruleset" id="id-4.-customise-your-ruleset"></a>

By default, Agentic Code Analysis uses a carefully created ruleset of best-practice security checks on your Salesforce code. But of course, we appreciate that every organisation has it’s own unique requirements, so the rule set is fully customisable.

Each rule from the Standard ruleset can be edited within AutoRABIT Guard or disabled. Within **Agentic Code Analysis** → **Repositories** → **Actions** → **Rules,** select a rule you would like to edit to open the editing pop-up. Click **Save Changes** to apply your edits.

In addition, you can create new Custom Rules either by uploading a pdf file or typing your rule in natural language. Go to **Agentic Code Analysis** → **Repositories** → **Actions** → **Rules** → **Custom Rules** and click the **Create Rule** button.

<figure><img src="../../../.gitbook/assets/image (2542).png" alt="" width="375"><figcaption></figcaption></figure>

1. **Create from text**. Type your rule or intention and get it validated by an AI agent.

<figure><img src="../../../.gitbook/assets/image (2543).png" alt="" width="375"><figcaption></figcaption></figure>

2. For the best results, be as specific as possible. For example, “Block any code that looks suspicious” is too generic, and the agent will not be able to suggest an improvement. But instead a good prompt could be “Block Apex code that uses dynamic SOQL without validation”.
3. After successful validation, the properties of the rule (Name, Type, Severity, Category and Framework) will be populated automatically. Please review these and edit if necessary - AI can make mistakes.
4.  **Generate from File.** Upload a PDF of your security policies or related documentation to bulk upload a set of rules.

    1. An AI agent will analyse the file and extract rules - depending on the size of the file this might take a few minutes.

    <figure><img src="../../../.gitbook/assets/image (2544).png" alt="" width="375"><figcaption></figcaption></figure>

b. You will then be taken through each extracted rule for review. Please check these carefully, along with the properties associated with each rule, as AI can make mistakes. The flow will first take you through rules that have an existing match within your rule set (across both standard and custom) - you can choose to remove one of the duplicates or keep both.

<figure><img src="../../../.gitbook/assets/image (2545).png" alt="" width="375"><figcaption></figcaption></figure>

Once you are happy with your rule set, you are ready to run a scan from the CLI. If you already have the Guard CLI set up, continue running Agentic Code Review.

### Analyse Rules (Noisy rules detection) <a href="#id-5.-download-and-install-the-cli" id="id-5.-download-and-install-the-cli"></a>

Over time, some rules generate a high volume of low-value findings for a given codebase, stylistic or convention-based rules that a team is unlikely to act on. **Analyse Rules** uses AI to inspect the rules enabled for a repository against a branch's code and suggest which ones are likely noise, so you can disable them for that repository.

To run it, go to **Agentic Code Analysis** → **Repositories**, open the **Actions** menu for the repository, and select **Analyse Rules:**

1. Pick a branch.
2. Wait for analysis.
3.  Review the suggested rules. The AI presents the rules it identified as likely noise for the repository, with:

    * Rule — the rule identifier (e.g. `sonar:S103`).
    * Name — the rule name (where available).
    * Reason — an explanation of why the rule is considered noisy for this codebase.
    * Confidence — the AI's confidence in the suggestion (e.g., High).

    All suggested rules are checked by default. Checked rules will be disabled for this repository only. Uncheck any rules you want to keep enabled.
4. Click Disable selected to apply.

The selected rules will be disabled for this repository (other repositories are unaffected).

### Test Quality

Agentic Code Analysis can assess the quality of your tests, not just your source code. Test analysis must be enabled for the repository (turn on **Enable tests analysis** in the repository's settings **Agentic Code Analysis** → **Repositories** → **Actions** → **Edit**), where you can also configure the Tests Folders glob patterns that tell AutoRABIT Guard which files to treat as tests.

Once enabled, tests are analyzed automatically on future scans (and can also be run from the CLI with `--check-tests`).

When a scan includes test analysis, the scan detail view shows a Test Quality section giving you an at-a-glance view of how well your tests are written. It summarises an overall Avg score across all scored tests, a breakdown by severity band (Critical, Major, Minor, Info), and results grouped by test files.

If a repository doesn't have test analysis enabled, scans still run normally, and the scan simply shows _No tests analyzed in this scan_.

### Download and install the CLI <a href="#id-5.-download-and-install-the-cli" id="id-5.-download-and-install-the-cli"></a>

Agentic scans are currently only supported from the CLI interface. Agentic Code Analysis uses the Guard CLI distributed as a Salesforce CLI plugin (`sf guard …`). This requires a bit of technical setup - so if you don’t have these installed already, you need Node.js, the global Salesforce CLI, and the plugin bundle from your Guard instance.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

| Requirement | Notes                                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Node.js** | Node **20+** required (22+ recommended); the Salesforce CLI bundles its own runtime for plugin install.                                                                    |
| **Access**  | Access to your Guard host (e.g. `https://fc-dev.autorabit.com`) and `npm` registry for `@salesforce/cli`.                                                                  |
| **API key** | `GUARD_API_KEY` set within Guard (see [API Keys](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-2.-api-keys)). |

#### Installation: Salesforce CLI plugin <a href="#installation-salesforce-cli-plugin" id="installation-salesforce-cli-plugin"></a>

In this option Guard runs as a Salesforce plugin. This is the recommended option for most users.

1. In your terminal, run `npm install -g @salesforce/cli`. This installs the Salesforce CLI globally.
2. Insert your API Key (YOUR\_GUARD\_API\_KEY) and Guard URL (YOUR\_GUARD\_URL e.g. [https://na1.autorabit.com](https://na1.autorabit.com/)) into the following command
   1. `curl -kSL -H "X-API-Key: YOUR_GUARD_API_KEY" \`\
      `-o /tmp/sf-guard-cli.tgz \`\
      `YOUR_GUARD_URL/cli/sf-guard-cli.tgz`
3. Install the downloaded file as a Salesforce plugin. Run `echo y | sf plugins install file:///tmp/sf-guard-cli.tgz`

### Run an Agentic Code Review <a href="#id-6.-run-an-agentic-code-review" id="id-6.-run-an-agentic-code-review"></a>

Once you’ve completed steps 1-5, you’re ready to use Agentic Code Analysis on your repository. This is performed from your terminal.

{% hint style="info" %}
The ruleset applied to the scan will reflect the currently enabled rules on your Rules page within Guard (both Standard and Custom).
{% endhint %}

Here we outline suggested commands to run your first code review. Please speak to your Technical team to refine the command. A full list of commands is available here.

The Guard CLI is invoked as `sf guard review`. Replace the placeholders in the following command with your Guard instance URL (e.g. `https://na1.autorabit.com`) and the workspace path to review (e.g. `$BITBUCKET_CLONE_DIR`):

* Salesforce CLI plugin:
  * `sf guard review --check-tests --progress --pr \`\
    `--url "YOUR_GUARD_URL" \`\
    `"YOUR_WORKSPACE"`

Additional commands:

* `export GUARD_API_KEY=...` in pipeline variables (required if not passed via `--api-key`).
* `--html` : write `.guard/reports/<stem>.html` as a build artifact.
* `--json` : machine-readable `GuardReviewResult` on stdout for downstream gates.
* `--no-upload` : local-only run (debugging).

For more commands to run in the CLI, see [Appendix 1](https://knowledgebase.autorabit.com/product-guides/guard/ai-interfaces/agentic-code-analysis-user-guide#id-9.-command-reference).

{% hint style="info" %}
All agentic code scan results are saved in the Guard platform under **Agentic Code Analysis** → **Analysis Findings**.
{% endhint %}

### Viewing results <a href="#id-7.-viewing-results" id="id-7.-viewing-results"></a>

#### Main entry: AutoRABIT Guard <a href="#main-entry-autorabit-guard" id="main-entry-autorabit-guard"></a>

All Agentic Code Analysis scan results are saved in the AutoRABIT Guard platform. From the navigation menu, open **Agentic Code Analysis** → **Analysis Findings** to explore detected issues across your codebase, review details, and apply recommended fixes.

#### Analysis Findings list

The Analysis Findings page lists every scan with the following columns:

| Column     | Description                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| Scan ID    | Unique identifier for the scan (e.g. `SCA-836`).                                                             |
| Repository | The repository the scan was run against.                                                                     |
| Findings   | Total number of findings detected in the scan.                                                               |
| Context    | The scope of the scan — a Full Scan (entire project) or a Pull Request (showing the source → target branch). |
| Date       | When the scan was run.                                                                                       |
| Status     | Outcome of the scan (e.g. Success, Blocked).                                                                 |

Use **Add Filter** to narrow the list. You can filter by:

* Context

Full Scan or Pull Request.

* Period

The time range of the scans.

* Repository

A specific registered repository.

* Status

Scan outcome.

#### Scan detail view

Open a scan to see a full breakdown of the run.

Summary cards at the top of the scan show:

| Card             | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| Total Findings   | Total findings detected, with a breakdown.                                         |
| Agents Succeeded | Number of analysis agents that completed successfully out of the total agents run. |
| Credits Consumed | AI credits used by the scan, alongside the number of findings produced.            |
| Cache Saved      | Percentage of work served from cache, with cached read/write detail.               |

Below the summary, the Findings section groups results and shows counts by type & severity. You can:

* Search findings using the search bar.
* Browse findings grouped by category (e.g. Code Quality, Security), each showing its finding count.
* Mark as **Accepted** to accept findings you have reviewed.
* Expand a category and drill into an individual finding to see the code context, rule details, and suggested fix.

Where no tests were analyzed, the scan indicates No tests analyzed in this scan.

Findings the AI considers low-confidence are grouped under Flagged by AI as likely false positives, with a count. You can review these separately or use Accept all AI-filtered to accept them in bulk.

#### Downloading patches

Download the patches for the whole scan or for each finding.

### Command reference <a href="#id-9.-command-reference" id="id-9.-command-reference"></a>

#### Positional argument <a href="#positional-argument" id="positional-argument"></a>

| Argument   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| `<folder>` | Workspace root to review. Defaults to current working directory. |

#### Guard connection flags <a href="#guard-connection-flags" id="guard-connection-flags"></a>

| Flag                       | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `--endpoint <url>`         | Override Guard GraphQL endpoint.                                 |
| `--url <url>`              | Override Guard application URL (bootstrap / Keycloak discovery). |
| `--api-key <key>`          | API key override (same as `GUARD_API_KEY`).                      |
| `--trust-all-certificates` | Disable TLS validation. Default `false`. Dev only.               |

#### Review-specific flags <a href="#review-specific-flags" id="review-specific-flags"></a>

| Flag                      | Description                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `--check-tests`           | Analyze test files with `test-quality-<framework>` agents; exclude tests from normal policy pass. Default `false`. |
| `--test-frameworks <csv>` | Restrict test agents: `apex`, `java`, `typescript`, `angular`. Only with `--check-tests`.                          |
| `--pr`                    | PR base from CI; **hard-restrict** scan to changed files only. Default `false`.                                    |
| `--progress`              | Live dashboard (phase, tokens, tool calls). Default `false`.                                                       |
| `--html`                  | Write HTML report to `.guard/reports/<stem>.html`. Default `false`.                                                |
| `--no-upload`             | Skip backend upload; local report still works with `--html`. Default `false`.                                      |

#### Built-in oclif flags <a href="#built-in-oclif-flags" id="built-in-oclif-flags"></a>

| Flag     | Description                              |
| -------- | ---------------------------------------- |
| `--json` | Emit `GuardReviewResult` JSON on stdout. |
| `--help` | Command help.                            |

#### Environment variables <a href="#environment-variables" id="environment-variables"></a>

| Variable                                 | Purpose                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `GUARD_API_KEY`                          | Auth token (same as `--api-key`).                                                                                        |
| `GUARD_APP_URL`                          | Guard application URL (same as `--url`; used for bootstrap / Keycloak discovery).                                        |
| `GUARD_GRAPHQL_ENDPOINT`                 | Guard GraphQL endpoint override (same as `--endpoint`).                                                                  |
| `GUARD_DEBUG`                            | When set, prints the path of the per-scan JSONL debug trace to stderr.                                                   |
| `GUARD_RULE_BUNDLES`                     | Set to `off` to skip downloading rule bundles from the backend and use the CLI’s embedded rules (offline runs).          |
| `GUARD_NO_UPDATE_CHECK`                  | Skip the plugin version-skew check that runs before a review.                                                            |
| `GUARD_MODEL_HINT`                       | Label stored on uploaded scan `llmModel`; does not change runtime model.                                                 |
| `GUARD_REVIEWER_MAX_INPUT_TOKENS`        | Reviewer batch input cap (default \~180,000).                                                                            |
| `GUARD_REVIEWER_MAX_SAMPLES_PER_CLUSTER` | Max sample findings per dedup cluster before summary (default `5`).                                                      |
| `GUARD_REVIEWER_MAX_FINDINGS_PER_BATCH`  | Max findings handed to a single reviewer batch (advanced tuning; default derived from the reviewer output-token budget). |
| `GUARD_REVIEWER_OUTPUT_TOKEN_LIMIT`      | Reviewer output-token budget used to size batches; must match the backend’s `max_tokens` (default `8192`). Advanced.     |

#### Example commands <a href="#example-commands" id="example-commands"></a>

**Full PR review in CI:**

`sf guard review --pr --check-tests --progress \ --url "https://fc-dev.autorabit.com" \ /path/to/repo`

**Local HTML report without upload:**

`sf guard review --html --no-upload ./my-sfdx-project`

**JSON for quality gate:**

`sf guard review --json --pr ./repo > guard-result.json`

#### Related `sf guard` commands <a href="#related-sf-guard-commands" id="related-sf-guard-commands"></a>

The `sf guard` Salesforce plugin ships two commands:

| Command | Purpose |
| ------- | ------- |

| Command           | Purpose                                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sf guard review` | Run an AI-powered Agentic Code Analysis review (the command documented throughout this guide).                                                                          |
| `sf guard update` | Re-download and reinstall the Guard plugin so it matches the version your backend currently serves. Use this to upgrade instead of repeating the manual `curl` install. |

{% hint style="info" %}
The `standards convert` / `standards violations` commands you may see elsewhere belong to the separate AutoRABIT Guard **Skill** package (a different distribution), not the `sf guard` Salesforce plugin described in this guide.
{% endhint %}
