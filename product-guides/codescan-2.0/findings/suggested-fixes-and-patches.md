---
description: Review and apply the exact code changes the AI writes for findings.
---

# Suggested Fixes and Patches

When AI finding review is on, the AI reviewer writes a suggested fix for findings it keeps. A suggested fix is an exact code change your developer reviews and applies. It is never applied without a person choosing to.

{% hint style="info" %}
**Note:** Suggested fixes are written only when **`Advanced AI Suggestions`** is switched on for the repository. An administrator sets this per repository. When it is off, scans still produce findings, without fixes.
{% endhint %}

## What a Fix Contains

Each fix is a precise edit:

* the file path
* the exact line range
* the original lines
* the replacement lines

A fix can span several files, for example a call in one file and a helper in another, and it can create or delete a file.

Every Blocker and Critical finding the reviewer keeps gets a fix, or an explicit reason why none applies. Lower severities get a fix when the reviewer can write a good one.

{% hint style="info" %}
**Note:** The finding details also show **How to fix it**: the rule's general guidance. That is different from the suggested fix, which is a concrete edit to your file.
{% endhint %}

## Where You Get Fixes

| Where                      | How                                                                                                                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web app, one finding       | **`Suggested Fixes`** in the finding details shows each change as a red and green diff. **`Download Patch`** saves `finding-<id>.patch`.                 |
| Web app, whole scan        | **`Download Scan Patch`** saves `scan-<id>.patch`. Shown only when the scan has suggested fixes.                                                         |
| Web app, as a pull request | **`Create PR`** lets you review, edit and turn fixes into a pull request. See [Create a PR Fix](/broken/pages/f24c62f869c68dbb046cf80ccad97d0b4a88ddf1). |
| VS Code                    | The lightbulb on the squiggle, or **Ctrl+.** / **Cmd+.**, then **`CodeScan: Apply Suggested Fix`**.                                                      |
| CLI                        | `codescan review --json` returns each finding's `suggestedFixes`.                                                                                        |
| HTML report                | A collapsible section on each finding shows the fix before and after.                                                                                    |

## Applying a Patch

Apply a patch on your own branch, following your team's usual conventions:

```bash
git switch -c fix/PROJ-123-sql-injection
git apply --check scan-<id>.patch
git apply scan-<id>.patch
git diff
```

Then run your tests, commit, and open the pull request the way your team normally does.

{% hint style="warning" %}
**Important Note:** Patches are matched to your code as it was at scan time. If `git apply --check` fails, or VS Code says the fix no longer fits, the code has changed since the scan. Nothing is changed. Run a new scan to get a fresh fix.
{% endhint %}

## Related Articles

* [Create a PR Fix](/broken/pages/f24c62f869c68dbb046cf80ccad97d0b4a88ddf1)
* [The AI Reviewer](/broken/pages/7da61efcb22971d0f056a22950e9db0f24c371f9)
