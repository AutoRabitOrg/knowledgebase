# CodeScan 2.0

### Market Overview

Salesforce runs core business processes and holds some of an organisation's most sensitive data: customer records, financial information and operating data. Much of who can see and change that data is defined in metadata, such as profiles, permission sets, sharing settings, guest-user access and connected apps. A small mistake in code or metadata can expose data or take an org down. A single unchecked query inside a loop, for example, can hit governor limits in production.

Salesforce teams also no longer work in Salesforce alone. A typical estate includes other languages, infrastructure as code, CI pipelines, containers and third-party packages, and a growing share of code is written with the help of AI assistants. More change means more to review.

Traditional static analysis tools are accurate but noisy. A team opens a report, sees hundreds of findings, and the few issues that matter sit in the same pile as naming conventions. Even when a finding is real, someone still has to work out the fix.

### What CodeScan Does

CodeScan by AutoRABIT reads your source code and tells you what is wrong with it before it reaches production: security vulnerabilities, bugs, performance problems, weak tests and risky third-party libraries. It is a cloud service, built for Salesforce teams, and covers the rest of your stack as well.

Every scan has two stages:

1. **Deterministic scan.** A rule engine runs more than 5,100 rules across 49 languages and file types. The same code and the same rules always produce the same findings. No AI decides what gets reported.
2. **AI review (optional).** If AI review is switched on for your project, an AI reviewer checks the findings you choose. It tries to prove each one wrong, flags the ones it can disprove with evidence as likely false positives, and writes a suggested fix. It never deletes a finding.

Suggested fixes reach your developers in two ways: as a patch they apply themselves, or as a pull request created from CodeScan. CodeScan never raises a pull request on its own. A developer reviews the AI-generated fixes, can edit them or leave files out, and then chooses to create the pull request.

### Why CodeScan

| What teams live with today                                            | What CodeScan changes                                                                                                                                                               |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One unchecked query inside a loop can take an org down.               | Every in-scope file is checked on a full scan, a pull request or a local change. CodeScan follows calls across files, so a query inside a helper called from a loop is still found. |
| Scanners are accurate but noisy, so reports go unread.                | Noise is reduced automatically before any AI is involved. The AI reviewer then flags findings it can disprove, with a reason, so your team reads the real issues first.             |
| Even when a finding is right, a developer still has to write the fix. | The AI writes an exact fix: file, lines, before and after. A developer reviews and edits it, then applies it as a patch or creates a pull request from CodeScan.                    |
| One tool per language means several tools and several dashboards.     | One service covers Salesforce, other languages, infrastructure as code, CI pipelines, containers, secrets and dependencies.                                                         |
| Every codebase has house rules no off-the-shelf scanner knows.        | Your team writes rules in plain language, or uploads a standards document, and reviews each draft rule before it runs.                                                              |

### Benefits of Using CodeScan

#### Lower Security Risk

* Tracks untrusted input across files, from where it enters your code to where it could cause damage, and shows the path step by step.
* Checks Salesforce metadata that controls access: permission sets, profiles, sharing, guest-user access, connected apps, and CSP and remote site settings.
* Finds hardcoded secrets, vulnerable and malicious third-party packages, and misconfigured infrastructure.
* Security findings reference CWE identifiers where they apply.&#x20;

#### Problems Caught Earlier

* Developers see findings in VS Code and from the CLI before they commit.
* Every pull request can be reviewed automatically, with or without a CI pipeline.
* For a change, the blast radius shows which code, entry points and tests it affects.
* The quality gate stops a change that fails your standards before it is merged.

#### Less Noise, More Trust

* Deterministic results: the same code gives the same findings, so scans can be compared.
* Duplicate findings are merged, and conventions your team has never followed are lowered to Info.
* Findings the AI doubts are flagged with a reason, never deleted, and never fail the quality gate.
* Accepted findings stay accepted across the web app, CI and VS Code.

#### Faster Fixes

* Suggested fixes are exact edits, not general advice.
* Fixes are checked against the current file before they are applied, so a fix that no longer fits is never forced in.
* A developer can review all fixes from a scan side by side, edit them, leave files out, and create a pull request from CodeScan in one step.
* Your team merges that pull request the way it merges any other, with your usual reviews and checks.

#### Your Standards, Enforced

* Write custom rules in plain language, or turn a coding standard or security policy PDF into draft rules.
* Describe a governance policy, and CodeScan maps it to well-known regulations and drafts the rules that enforce it.
* Each project chooses which severities fail its quality gate.

#### Predictable AI Cost

* The deterministic scan uses no AI credits.
* Each AI feature is switched on per project.
* Administrators see credit usage by feature and by user, with a warning at 80% of the monthly limit.
* If credits run out, scans still complete with the full deterministic results.

#### One Tool Across Your Stack

* More than 5,100 rules across 49 languages and file types. See Supported Languages and File Types.
* Infrastructure as code, containers, CI pipelines and third-party dependencies, with an SBOM in CycloneDX or SPDX format.

### Where You Use It

| Where                                                 | What happens                                                                                                                                                                     |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web app                                               | Scan any connected branch, review and accept findings, tune rules, view dashboards and export reports.                                                                           |
| Pull requests                                         | A GitHub, GitLab or Bitbucket webhook starts a review with no pipeline needed. Results come back on the pull request as a commit status and, if switched on, AI review comments. |
| CI/CD                                                 | The CodeScan CLI runs in your pipeline. The quality gate decides whether the scan passes. Reports are written in SARIF, JUnit, GitLab and HTML formats.                          |
| Terminal                                              | The CodeScan CLI scans a whole repository, your uncommitted changes, or the committed work on your branch.                                                                       |
| VS Code                                               | The **AutoRABIT CodeScan** extension shows findings on the lines they belong to and in the **Problems** panel, and applies suggested fixes.                                      |
| <mark style="color:$warning;">AI coding agents</mark> | <mark style="color:$warning;">A skill teaches Claude Code to run a scan before a commit and before a pull request.</mark>                                                        |
