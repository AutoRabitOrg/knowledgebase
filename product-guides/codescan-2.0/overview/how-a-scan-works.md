---
description: >-
  The five steps every scan follows, what gets scanned, and what the AI reviewer
  is and isn't allowed to do.
---

# How a scan works

Every scan follows the same five steps, whether you start it from the web app, a pull request, the CLI or VS Code.

| Step                 | What happens                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Collect           | Your workspace is uploaded to CodeScan. A pull-request or local scan still uploads the whole workspace, so rules that look across files keep their context, but it reports only on the changed files. |
| 2. Understand        | Each file is parsed into a syntax tree, the same structure a compiler uses. Classes, methods and call chains are then indexed.                                                                        |
| 3. Scan              | The deterministic rules run. This step is fast and repeatable. Test folders are left out of it.                                                                                                       |
| 4. Review (optional) | If AI finding review is switched on, findings of the severities you selected go to the AI reviewer. This step uses AI credits.                                                                        |
| 5. Deliver           | You get findings, suggested fixes, reports, the blast radius of a change, and the quality gate result.                                                                                                |

### What Gets Scanned

CodeScan scans git-tracked files, except:

* paths in `.gitignore` and in the project's **`Sources Exclusions`**
* test folders, which are kept out of the rule scan but used for test-quality analysis, coverage estimates and blast radius
* generated and minified files
* binaries, operating-system files, and any file larger than 2 MiB (dependency manifests and lockfiles are scanned regardless of size)

{% hint style="info" %}
**Note:** Helm charts are scanned only if `helm` is installed where the scan runs. Otherwise they are reported as not scanned, not as clean.
{% endhint %}

### The Deterministic Engine

CodeScan does not search code as text. It parses each file into a syntax tree and runs its rules against that structure. A risky keyword inside a comment or a string does not trigger a finding, and a problem that spans several files can still be followed.

For Salesforce teams, this means that if a loop in one class calls a helper in another, and that helper runs a SOQL query, CodeScan follows the call chain and reports the query in the loop. For security issues, it tracks untrusted input from where it enters your code to where it could cause damage, and shows that path as numbered steps on the finding.

{% hint style="info" %}
**Note:** Static analysis reads code without running it, so it cannot see runtime values or configuration, or confirm that a custom helper really cleans its input. Where it is unsure, CodeScan reports a suspect rather than hide a real issue.
{% endhint %}

### Noise Control Before AI

Before any AI is involved, CodeScan reduces noise automatically, at no credit cost:

* It merges duplicate findings and findings with the same root cause.
* It lowers convention rules to Info when your project has never followed that convention.
* It runs framework rules only when that framework is present.

Security rules and Blocker or Critical findings are never lowered by this step.

### AI Review

AI finding review is switched on per project, and you choose which severities it examines. The reviewer's instruction is to try to prove each finding wrong, not to confirm it:

* If it finds evidence that the code is safe, such as validation further up the call chain, it marks the finding as a likely false positive with a short reason. For a security finding, the reason must point to the line of code that defends against it.
* If it cannot disprove the finding, the finding stands.
* In the same pass, it writes a suggested fix for the findings it keeps.

| Guarantee                    | What it means for you                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Nothing is deleted           | Likely false positives move to their own group, **`Flagged by AI as likely false positives`**, with the reason attached.         |
| Flagged findings never block | They do not count toward the quality gate.                                                                                       |
| Fail open                    | If AI is switched off, out of credits or unreachable, you get the full deterministic results.                                    |
| No hidden severity changes   | Style findings the reviewer keeps are lowered to Info. Otherwise, it changes a severity only when the scanner was clearly wrong. |
| Your rules are your policy   | Findings from your custom rules are never flagged as likely false positives.                                                     |

{% hint style="info" %}
**Note:** The deterministic scan uses no AI credits. AI verdicts are cached, so re-scanning code that has not changed costs nothing.
{% endhint %}
