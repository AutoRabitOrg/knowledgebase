---
description: >-
  What the built-in rules cover, by area, and how rule categories and severities
  work.
---

# Rules

CodeScan ships with more than 5,100 built-in rules across 49 languages and file types. This article describes what they cover. For the list of languages, see Supported Languages and File Types.

### Severities and Categories

Every rule has a severity: Blocker, Critical, Major, Minor or Info. The scale matches what most teams already use, so results compare with other tools. See Understanding a Finding for how to treat each one.

Rules are grouped into categories, including security, code quality, performance, structure, exceptions, tests, strings, naming and style.

### What the Rules Cover

| Area                              | Focus                                                                                                                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Apex                              | Governor limits (SOQL, SOSL and DML in loops, including across method calls), injection, CRUD and FLS, hard-coded credentials, insecure cryptography, unescaped output, SSRF, test discipline, complexity and dead code                           |
| Salesforce metadata               | Profiles, permission sets, sharing and sessions, Flows, guest-user access, connected apps, CSP and remote sites, OmniStudio, Agentforce and GenAI prompts, Experience Cloud, API version currency, formula quality, and Visualforce accessibility |
| Lightning Web Components and Aura | LWC JavaScript and templates are checked as their own surfaces, with security, accessibility and Salesforce-specific rules                                                                                                                        |
| MuleSoft                          | Reliability, security, governance, DataWeave, database access including SQL injection across flows, and MUnit coverage                                                                                                                            |
| Java                              | Design, reliability, security and cryptography, Spring and Spring Security, concurrency and performance                                                                                                                                           |
| JavaScript and TypeScript         | Security (injection, XSS, SSRF, path traversal), performance, accessibility, Angular and React                                                                                                                                                    |
| Python                            | Injection (SQL, command, path, template), Django and Flask configuration, cryptography, complexity and performance                                                                                                                                |
| Other languages                   | Language-specific security and correctness rules. See Supported Languages and File Types.                                                                                                                                                         |
| Infrastructure as code            | Open security groups, wildcard IAM, plaintext secrets, public storage, unencrypted storage, privileged containers, missing resource limits and unpinned image tags                                                                                |
| Containers                        | Dockerfiles checked instruction by instruction, and every base image checked for known vulnerabilities                                                                                                                                            |
| CI pipelines                      | Pipeline files for GitHub Actions and GitLab CI                                                                                                                                                                                                   |
| Secrets                           | API keys, tokens, private keys and connection strings in any text file                                                                                                                                                                            |
| Dependencies                      | Known vulnerabilities, licences, malicious packages, typosquatting and reachability. See Dependency, Supply-Chain and Container Analysis.                                                                                                         |

### Checks That Run Across Languages

* **Copy-paste detection** finds duplicated code, ignoring formatting, comments and variable names.
* **ReDoS analysis** finds regular expressions that could freeze a server, and shows the input that would trigger it.
* **Accessibility** checks HTML, Visualforce, Aura and LWC templates for missing alternative text, missing labels and keyboard-inaccessible controls.
* **Test rules**: more than 70 rules check test code, such as a test with no assertion, an Apex class with no matching test class, or a MuleSoft flow with no MUnit coverage. They appear as ordinary findings in the **Tests** category and count toward the quality gate like any other finding.

### Related Articles

* Tune Built-In Rules
* Custom Rules
* Supported Languages and File Types
