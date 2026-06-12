# Agentic Code Analysis

### Overview <a href="#overview" id="overview"></a>

**Agentic Code Analysis** in AutoRABIT Guard reviews your code with AI-powered agents, achieving more accurate and reliable results than pattern-based scanning alone. It runs in your CI/CD pipeline via the **Guard CLI** , uploads structured results to Guard and recommends code patches.

### Key Capabilities <a href="#key-capabilities" id="key-capabilities"></a>

#### Easy rule definition <a href="#easy-rule-definition" id="easy-rule-definition"></a>

Users can define and extend policies through multiple options:

* **PDF upload**: Directly drop-in your security policy pdf file. AI extracts and normalizes your coding standards into rules.
* **Natural language**: Type in your intent and get AI-powered feedback.
* **Prebuilt / standard rules**: framework-aligned rules maintained by AutoRABIT.

Examples of added standard rules include:

* **apex-database-result-unchecked** — DML with `allOrNone=false` and discarded `SaveResult[]` silently hides per-record failures.
* **apex-callout-after-dml** — HTTP callout after DML in the same method triggers “uncommitted work pending.”
* **lwc-innerhtml-assignment** — Direct `.innerHTML` / `.outerHTML` / `.srcdoc` assignment in LWC bypasses Locker/LWS sanitization and raises XSS risk with user-controlled content.

#### Centralized policy store <a href="#centralized-policy-store" id="centralized-policy-store"></a>

* Standard rule set, AI-generated custom rules, and editable, version-controlled policies in one place.
* New rules are validated and compared with existing rules before activation.

#### AI-powered analysis <a href="#ai-powered-analysis" id="ai-powered-analysis"></a>

The CLI orchestrates specialized agents:

* **Language-specific analysis agents** (Apex, Java, TypeScript, Angular, etc.).
* **Framework-aware scanning** and optional **test-quality** agents when `--check-tests` is enabled.
* **Reviewer agent** — validates and deduplicates findings for lower noise.

Output options include structured JSON, reports (`.guard/reports/`), and upload to Guard for review on the UI.

### Getting Started <a href="#getting-started" id="getting-started"></a>

1. Under **Settings**, create an **API key** and store it securely.
2. Install the **Salesforce CLI** and the **Guard plugin** (see User Guide).
3. Add a pipeline step: `sf guard review --pr --check-tests --progress --url <your-guard-url> <workspace>`.
4. In Guard, open **Analysis Findings** to review detected issues, policies, and scan history.

See the User Guide for more details on getting set up, and for the full range of commands available in the CLI.
