---
description: >-
  Accept a false positive or a risk your team has decided to live with, and
  reverse it later.
---

# Accept a Finding

Accept a finding when it is a false positive, or a risk your team has decided to live with. An accepted finding drops out of the quality gate and stays accepted on later scans of the same repository, in the web app, in CI and in VS Code.

## Accepting Findings in the Web App

| To accept                           | Do this                                                                            |
| ----------------------------------- | ---------------------------------------------------------------------------------- |
| One finding                         | Open the menu on the finding, or select **`Accept Issue`** in the finding details. |
| Every finding of a rule or category | Use the **`Actions`** menu on the rule or category, or **`Bulk Update`**.          |
| All likely false positives          | Select **`Accept all AI-filtered`**, after you have read the reasons.              |

{% hint style="info" %}
**Note:** In the web app you can accept and restore findings only on scans from the last day. If the buttons are disabled, run a new scan.
{% endhint %}

## Accepting Findings in VS Code

Select **`Accept Finding`** on the finding row. The squiggle disappears and the finding stays accepted on later scans, including in CI.

Accepting in VS Code needs a git remote, so CodeScan knows which repository the decision belongs to.

## Reversing an Acceptance

Select **`Restore`** in the web app, or **`Restore Finding`** in VS Code. The finding counts toward the quality gate again.

## How CodeScan Recognises the Same Finding

An accepted finding is identified by the rule, the file and the code itself, not by the line number. It stays accepted when edits elsewhere in the file move it up or down.

## Accepting Is Not the Same as an AI Flag

|                           | AI flag (likely false positive) | Accepted                 |
| ------------------------- | ------------------------------- | ------------------------ |
| Who decides               | The AI reviewer                 | Your team                |
| Remembered on later scans | **No**                          | Yes, for this repository |
| Counts toward the gate    | No                              | No                       |

Both stay visible, so you can always check what was set aside and why.

## Recommendations

* Accept findings one by one when you can, so each decision is deliberate.
* Before accepting a whole rule or category, consider whether to lower the rule's severity or switch it off instead. See [Exclusions and Test Folders](/broken/pages/b34368acc65d5a91c52d4fe449c256b290a96d4c#which-option-to-use).
* Review accepted findings from time to time. A risk your team accepted last year may not be acceptable today.

## Related Articles

* [Understanding a Finding](/broken/pages/3b5141990cce2576d610360f3a7f5130169e2e23)
* [How the Quality Gate Works](/broken/pages/b4754d4e4824f1f1fb18918b24901997b0e512a3)
