# Latest

### **Release Notes 26.4.1** <a href="#release-notes-26.4.1" id="release-notes-26.4.1"></a>

**Release Date:** 7 Oct 2026

***

This release extends IZ Suite governance to AWS, adds Java code scanning, replaces the token-based sign-in with a hardened user login, and protects every stored credential at rest. It includes:

* AWS governance across 16 AWS services: inventory in IZ Eye and configuration scanning in IZ Scan, backed by 765 built-in rules
* CloudFormation and SAM template scanning, both for deployed stacks and as a shift-left check on the template itself
* **Java** as a new scan language: 143 built-in rules covering correctness, security, tests, Spring and Spring Boot configuration, 49 of them with auto-fix
* Python code scanning for Lambda functions, PySpark as a new scan language, and PEP 8 style checks for Python
* IZ User Auth: email and password sign-in with lockout, password expiry, self-service reset and optional multi-factor authentication
* Cloud credentials, agent secrets and secure settings encrypted at rest; IZ Scan tokens stored as one-way hashes
* Languages and platforms delivered as seed data, so a new language can be added without a code release
* IZ Lens platform pages that answer "what needs fixing, what loses support next, where do problems compound"

IZ Suite continues to ship as a **single certified release**: the server, the agent and all in-suite modules are built, tested and signed off together under one version. The component versions it contains are listed at the end.

### 1. AWS Governance <a href="#id-1.-aws-governance" id="id-1.-aws-governance"></a>

An AWS account is onboarded as an organisation, and each governed region becomes an environment. IZ Suite then keeps an inventory of the account's resources and evaluates each one against a built-in rule pack.

* **Onboarding:** create an organisation with source _AWS_ and enter the account id, an access key pair and the regions to govern. Each region becomes an environment, and a synthetic _global_ environment holds region-agnostic resources such as CloudFront distributions. A tenant can onboard any number of accounts, and the credential can be corrected or rotated later from Edit Organisation without re-onboarding.
* **Inventory (IZ Eye):** Lambda functions, CloudFormation stacks (including stacks in failed states), Step Functions state machines, API Gateway APIs, ECS task definitions, RDS and Aurora databases, load balancers, Secrets Manager secrets, CloudFront distributions, DynamoDB tables, SQS queues, SNS topics, EventBridge buses, and CodePipeline, CodeBuild and CodeDeploy definitions. Discovery runs on the standard recurring sync jobs with per-service pattern matchers, so noisy resources can be excluded.
* **Configuration scanning (IZ Scan):** every discovered resource's definition is scanned against its service rule pack, ported from Checkov, Prowler and the AWS Well-Architected Framework and covering security, reliability and cost posture. Lambda rules carry auto-fix suggestions. Findings appear in the same issue views, quality gates and reports as every other language.
* **Code scanning:** Lambda functions on Python runtimes have their deployment package scanned with the Python scanner, so a single Lambda scan reports both configuration and code findings. Container-image functions are configuration-scanned only.
* **Infrastructure as code:** CloudFormation and SAM templates are scanned against the CloudFormation rule pack, either as the template a deployed stack was created from or directly from source before deployment, including from the IZ Scan CLI in a build pipeline.
* **Permissions and licensing:** two new permission categories, _Falcon Eye AWS_ and _Falcon Scan AWS_, control access per service. Onboarding an AWS organisation grants its administrator the AWS permissions automatically. Each AWS service is a licence module and must be granted on the tenant's licence to appear.

| Service        | Rules | Service         | Rules |
| -------------- | ----- | --------------- | ----- |
| CloudFormation | 69    | Secrets Manager | 50    |
| Lambda         | 61    | CodeBuild       | 50    |
| ECS            | 57    | CloudFront      | 49    |
| API Gateway    | 51    | EventBridge     | 43    |
| Step Functions | 51    | CodeDeploy      | 42    |
| RDS / Aurora   | 51    | CodePipeline    | 37    |
| Load Balancer  | 50    | DynamoDB        | 36    |
| SQS            | 34    | SNS             | 34    |

### 2. Java Code Scanning <a href="#id-2.-java-code-scanning" id="id-2.-java-code-scanning"></a>

IZ Scan now scans Java repositories, from the agent and from the IZ Scan CLI, with a new **Java Apps** menu under IZ Scan (ISB-298).

* **Rule pack:** 143 built-in rules in four areas — correctness and reliability (resource leaks, null handling, equality and concurrency mistakes), security (injection, deserialisation of untrusted data, weak cryptography, permissive CORS, hard-coded credentials), maintainability, and tests (JUnit 4 and 5). Every rule description carries a compliant and a non-compliant example and links the OWASP Top 10 2021 and CWE entries it maps to.
* **Auto-fix:** 49 rules offer an automatic fix that rewrites the source, for example redundant imports, simplifiable Spring annotations and needlessly public JUnit 5 tests.
* **Spring and Spring Boot:** controller rules check request mappings that accept every HTTP method, `@PathVariable` names that do not match the URI template, entities bound directly from a request (mass assignment) and user input from `@RequestParam`, `@PathVariable`, `@RequestHeader` and `@RequestBody` reaching SQL, command, file-path and redirect sinks. `application*` and `bootstrap*` `.properties` and `.yml` files are scanned for insecure configuration: Actuator endpoints exposed without restriction, secrets in plain text, debug information or error details exposed, the H2 console enabled, weak TLS or insecure session cookies, database connections without transport encryption, and schema auto-generation outside development. Development, local and test profiles are exempt.
* **Accuracy first:** the scanner resolves types against the JDK and the project's own sources and never reports a finding it cannot prove, so code that depends on unresolved library types is skipped rather than guessed at. Generated sources are excluded, and findings can be suppressed in code with `@SuppressWarnings` or a `NOSONAR` comment.
* Every Java language level is supported, up to Java 25. Multi-module Maven and Gradle builds are scanned from the repository root.
* One rule, _Method parameter reassigned_, ships disabled in the default profile and can be enabled per profile.
* Java is scanned from source repositories. Java Lambda functions and Azure Function Apps deploy compiled bytecode and are not code-scanned.

### 3. IZ User Auth <a href="#id-3.-iz-user-auth" id="id-3.-iz-user-auth"></a>

The IZ Token login for the web application is replaced by **IZ User Auth**, a conventional email and password sign-in with the controls an auditor expects. Federated sign-in through Anypoint, Azure and Google is unchanged, and IZ Scan service tokens continue to authenticate the CLI as before.

* **Password policy:** minimum 12 characters with at least one digit and one special character. Passwords are stored as salted scrypt hashes.
* **Password expiry:** the Login Setting _IZ User Auth Password Max Age_ (default 90 days) forces a reset on the next sign-in once a password is older than the limit.
* **Account lockout:** _Max Failed Login Attempts_ (default 5) and _Account Lockout Minutes_ (default 15), configurable per tenant.
* **Self-service and invitations:** forgot-password and user-invitation emails carry single-use, time-limited links. A used link and every earlier link for the same user stop working.
* **Multi-factor authentication:** when the Login Setting _MFA Enabled_ is on, users enrol an authenticator app (Google Authenticator, Microsoft Authenticator or any RFC 6238 TOTP app) by QR code on their first sign-in and receive one-time recovery codes. Wrong codes count towards the lockout policy, and an administrator can clear a user's enrolment so they can re-enrol.
* **Break-glass access:** an _IZ Support User_ licence administrator exists on every tenant for recovery when the provider is disabled or all administrators are locked out.

### 4. Credentials Protected at Rest <a href="#id-4.-credentials-protected-at-rest" id="id-4.-credentials-protected-at-rest"></a>

A database dump no longer hands over any usable credential.

* **IZ Scan security tokens** are stored as SHA-256 digests. A token is shown once when it is generated and cannot be retrieved afterwards. Tokens issued before this release keep working: they were hashed in place during the upgrade.
* **Cloud credentials** (AWS secret keys, Salesforce private keys, Anypoint client secrets), secure global settings, agent secrets and MFA secrets are encrypted with AES-256-GCM under a server-side key. Every user-facing query returns them masked, and saving a form that still shows the mask leaves the stored secret unchanged.
* **Agent bootstrap secret** is supplied by the deployment rather than built into the agent image.

### 5. Languages and Platforms as Seed Data <a href="#id-5.-languages-and-platforms-as-seed-data" id="id-5.-languages-and-platforms-as-seed-data"></a>

Every language and platform IZ Suite governs is now described by a **language manifest**: its scanner, rule and metric packs, permissions, global settings, sync job types, quality gate, menu placement and icon. Manifests are delivered as seed data alongside rules and vulnerability feeds.

* Adding or updating a language is a seed-data refresh from the Seed Data screen, not a code release. All 16 AWS services, PySpark and Java arrive this way.
* A language added after a tenant was onboarded now inherits the tenant's own role grants from its reference language, on every one of the tenant's organisations, so existing roles see the new language's applications without manual permission changes.
* The Seed Data screen shows the installed version of each language and pack.
* **PySpark** is a new scan language with its own parser and a 48-rule pack.
* **Python PEP 8:** 28 new style rules covering indentation, whitespace, blank lines, import placement and naming conventions, validated against `pycodestyle` and `pep8-naming`. The Python parser now also accepts the walrus operator, positional-only parameters, underscores in numeric literals and parenthesised `with` statements, so files using them are scanned instead of skipped.

### 6. IZ Lens Platform Pages <a href="#id-6.-iz-lens-platform-pages" id="id-6.-iz-lens-platform-pages"></a>

IZ Lens gains an Overview and a page per platform family, all derived from the language manifests so a new platform gets its page automatically.

* **Overview:** an advisory triage queue, a deprecation runway (Lambda runtimes and RDS engine versions approaching end of support), where problems compound across an application, and the vulnerable and deprecated application lists.
* **Platform pages** for AWS, Anypoint Platform, Azure and Others: census and Lens coverage, version spread, environment drift, secrets hygiene, and the single points of failure that many applications depend on.
* **Relationships:** lineage between Lambda functions and the databases, secrets, queues, topics, event buses, state machines and APIs they use, plus Mule, Function App and Logic App relationships.
* **Where is this used?** searches a secret, image or connector and lists every asset that references it. **Version spread** shows a component's version fragmentation across applications.
* **User-entered dependencies and metrics:** from an IZ Eye application version's actions, a user with edit permission can record that the application _depends on_ or _invokes_ another application, or add a named metric value, for relationships and facts that discovery cannot see. Re-adding the same name updates it.

### 7. Licensing and Administration <a href="#id-7.-licensing-and-administration" id="id-7.-licensing-and-administration"></a>

* **Licence limit banner:** when a licensed IZ Scan, IZ Eye or IZ Pulse quota is used up, every page shows which module and attribute reached its limit (for example 50/50 applications), before new applications or scans are refused.
* The Jobs screen lists only jobs whose job type is enabled on the tenant's licence.

### 8. Agent <a href="#id-8.-agent" id="id-8.-agent"></a>

* **Consolidated job jars:** the per-job scheduler and executor modules are folded into four platform jars (Anypoint Platform, Azure Integration Services, Salesforce Platform and AWS Platform). An agent downloads far fewer artefacts and a new job type on an existing platform needs no new download.
* Job types are updated automatically during the upgrade; no agent configuration changes.

### Upgrade Notes <a href="#upgrade-notes" id="upgrade-notes"></a>

* **Required before start:** the server needs a 32-byte hex encryption key in `SECRETS_ENCRYPTION_KEY` and refuses to start without one. Store it in the deployment's secret store and never rotate it in place: stored credentials cannot be decrypted under a different key and would have to be re-entered.
* **Required on server and agents:** `AGENT_WRAPPER_SECRET` replaces the agent's built-in bootstrap secret.
* Schema and data updates apply automatically, including hashing existing IZ Scan tokens and encrypting existing credentials. Existing CLI tokens keep working.
* Upload the release seed data and run Trigger Seed Data so the language manifests, AWS rule packs, PySpark, Java and the Python PEP 8 rules are registered. AWS services and Java appear once seeded and licensed; refetch the licence after the upgrade.
* **Java** is licensed per tenant as the module `falcon_scan_java`. On server start, every existing role that holds Python scan permissions on an organisation receives the matching Java permissions there; users see Java Apps after signing in again.
* Agents download the consolidated job jars on their next job; no manual step.



### Component Versions in This Release <a href="#component-versions-in-this-release" id="component-versions-in-this-release"></a>

IZ Suite is released and certified as one set. The server and agent images are built together from the same source and share the release version; the exact build artefacts are recorded immutably at release time.

| Component | Version | Notes |
| --------- | ------- | ----- |

| Component                   | Version | Notes                                                                                                                                           |
| --------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| IZ Suite Server (web + API) | 26.4.1  | Anchor of the release; version enforced at startup                                                                                              |
| IZ Suite Agent              | 26.4.1  | Built and certified as a pair with the server; ships the aws-platform job jar                                                                   |
| IZ Scan CLI                 | 26.4.1  | Built on the 26.4.1 scan core and language parsers; scans Java, CloudFormation/SAM templates, Lambda and PySpark projects from the command line |
| VS Code Extension           | 26.4.1  | Built on 26.4.1 core scanner to support AWS and Java                                                                                            |
| IZ Suite Seeding            | 26.4.1  | Independent seeding repository enables fixes and updates to be released independently, without requiring changes to the Server or Agent code.   |

## Other Improvements <a href="#other-improvements" id="other-improvements"></a>

* **MCP pagination:** Added pagination support to MCP tools, making it easier to navigate large result sets.
* **View all issues:** Added a new screen to browse issues across all applications in one place.
* Minor performance enhancements, bug fixes, and security improvements are included throughout the release.

