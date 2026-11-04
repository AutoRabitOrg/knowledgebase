---
description: >-
  How the AI reviewer checks findings, what it can and cannot do, and how to
  switch it on.
---

# AI Reviewer

The AI reviewer does the first triage pass that a person would otherwise have to do. It checks the findings the scanner produced, flags the ones it can show are safe, and writes suggested fixes. The scanner still decides what is a finding.

### Switching It On

AI finding review is switched on per project. In Project Settings:

1. Under **`Repository`**, click **`Edit`** and turn on **`AI finding review`**.
2. In **`Severities included in AI review`**, choose which severities the reviewer examines.
3. To get suggested fixes, make sure **`Advanced AI Suggestions`** is on for the repository.

When AI finding review is off, scans still run in full and use no credits.

### How It Decides

The reviewer is instructed to try to prove each finding wrong, not to confirm it. Asking "can I confirm this?" would approve anything that looks plausible.

* **If it finds evidence the code is safe**, such as validation, a sanitiser or a guard further up the call chain, it marks the finding as a **likely false positive** with a short reason. For a security finding, the reason must point to the file and line of the defence. Without that evidence, the finding stands.
* **If it cannot disprove the finding**, the finding stays as it was.

It reads the code before deciding. It has read-only access to the uploaded code: it can read specific lines, search the repository, find where a method is used, look at what changed, check your custom rules, and see how similar findings were judged before. It cannot change anything.

A likely false positive is a strong hint, not a verdict. It tells you which findings to read last, not which to ignore.

### What It Is Not Allowed to Do

| Guarantee                    | What it means                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Nothing is deleted           | A likely false positive moves to its own group, with the reason attached. You can always read it.                     |
| Flagged findings never block | They do not fail the quality gate.                                                                                    |
| The scanner comes first      | The AI judges findings the scanner produced. It does not run its own scan or replace the scanner.                     |
| Fail open                    | If AI is off, unavailable or out of credits, you get the full scanner results. A scan is never lost.                  |
| No hidden severity changes   | Style findings it keeps are lowered to Info. Otherwise it changes a severity only when the scanner was clearly wrong. |
| Your rules are your policy   | Findings from your custom rules are never flagged as false positives.                                                 |

### Suggested Fixes

In the same pass, the reviewer writes suggested fixes. Every Blocker and Critical finding it keeps gets a fix, or a reason why none applies. See Suggested Fixes and Patches.

### Where Likely False Positives Appear

| Where               | How it appears                                           |
| ------------------- | -------------------------------------------------------- |
| Web app             | The **`False Positives`** tab, with the reason           |
| VS Code             | Its own **Likely false positives** group                 |
| CLI JSON            | `aiSuspectedFP` and `aiSuspectedFpReason` on the finding |
| SARIF               | An "under review" suppression                            |
| JUnit               | A skipped test case                                      |
| GitLab Code Quality | A `[Likely false positive: …]` prefix                    |
| HTML report         | An AI-FP badge                                           |

After reading the reasons, you can accept the whole group with **`Accept all AI-filtered`**, so the decision is remembered for the repository.&#x20;
