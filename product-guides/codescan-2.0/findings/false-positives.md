---
description: >-
  Review the findings the AI reviewer flagged as likely false positives, and
  restore any you disagree with.
---

# False Positives

When AI finding review is on, the AI reviewer checks findings and flags the ones it can show are safe. Those findings move to the **`False Positives`** tab of the scan, each with the AI's reason. Nothing is deleted, and you can move any of them back.

Findings in this tab don't count toward the quality gate.

### Why a Finding Is Flagged

The AI reviewer tries to prove each finding wrong. It flags a finding only when it finds evidence that the code is safe, such as validation further up the call chain, or code that can never run. For a security finding, the reason must point to the file and line that shows it. Without that evidence, the finding stays in **`New Findings`**.

The AI reviews only the severities chosen in **`Severities included in AI review`**: Blocker and Critical by default. Findings from your custom rules are never flagged.

See [The AI Reviewer](../ai-features/ai-reviewer.md).

### Reading the False Positives Tab

Open a scan and select the **`False Positives`** tab. The number on the tab is how many findings were flagged.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 17.35.19.png" alt=""><figcaption></figcaption></figure>

Findings are grouped by category, such as **Security**, then by rule. Each rule row shows:

* the severity, for example **Blocker**
* the rule, for example `codescan/apex/crud-fls-not-checked`
* the **AI Suggested** badge
* how many occurrences were flagged, and in how many files

Expand a rule to see each occurrence:

| Item             | What it shows                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File and line    | Where the finding is, for example _AccountCreation.cls, line 9_                                                                                                                                                     |
| Message          | What the rule reported                                                                                                                                                                                              |
| **AI rationale** | Why the AI considers the finding safe, with the date and time of the review. The reason points to the code that shows it, for example _Loop iterates an empty list and never adds records (AccountCreation.cls:4)_. |
| **`History`**    | Shows the audit trail of the issue                                                                                                                                                                                  |
| **`Restore`**    | Moves the finding back to **`New Findings`**                                                                                                                                                                        |

### Checking a Flag

For each flagged finding:

1. Read the **AI rationale**.
2. Open the file at the line the rationale points to, and check that the code really does what the AI says.
3. Decide:
   * **You agree:** leave the finding in **`False Positives`**. <mark style="color:red;">**\[TO CONFIRM: whether to accept the finding as well, so the decision is kept on later scans, and how to do that from this tab]**</mark>
   * **You disagree:** select **`Restore`**. The finding moves back to **`New Findings`** and counts toward the quality gate again.

{% hint style="info" %}
**Note:** A flag is a strong hint, not a verdict. Check Blocker and Critical security findings yourself before you rely on a flag, especially the first few times you use AI review on a repository.
{% endhint %}

### Restoring Several Findings at Once

| To restore                          | Select                                                     |
| ----------------------------------- | ---------------------------------------------------------- |
| One finding                         | **`Restore`** on the occurrence                            |
| Every flagged occurrence of a rule  | **`Restore All`** on the rule row                          |
| Every flagged finding in a category | **`Bulk Update`** → **`Bulk Restore All`** on the category |

In the web app you can restore findings only on scans from the last day. If the buttons are disabled, run a new scan.

### When the Tab Is Empty

The **`False Positives`** tab is empty when:

* the AI reviewer checked the findings and found none it could disprove
* **`AI finding review`** is off for the project
* the findings are of severities not included in AI review
* AI credits had run out, or the AI service was unavailable. The scan still completes with the full results.

### On Later Scans

AI verdicts are cached. Re-scanning code that hasn't changed gives the same verdict and uses no credits. When the code, your rules or the AI model change, the finding is reviewed again. <mark style="color:red;">**\[TO CONFIRM: whether a restored finding stays restored on later scans]**</mark>

### Outside the Web App

Flagged findings also stay visible, marked, in VS Code, the CLI's JSON output and every report format. See The AI Reviewer.

### Related Articles

* The AI Reviewer
* Accept a Finding
* How the Quality Gate Works
