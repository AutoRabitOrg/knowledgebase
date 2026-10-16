---
description: >-
  What the quality gate checks, what it ignores, and how to choose the right
  setting.
---

# Quality Gate

The quality gate is the pass/fail check on every scan. It turns CodeScan from a report into a control: a change that fails your standards can be stopped before it is merged.

### What the Gate Checks

Each project chooses which severities fail the gate: any of **Blocker**, **Critical** and **Major**.

* A scan that contains a finding of one of those severities is **blocked**.
* Otherwise it is **successful**.
* An empty list means **report-only**: nothing blocks.

The default is **Blocker** only.

On a comparison or pull-request scan, the gate looks only at **new** findings: the ones the change introduced. A change is not blocked by problems that were already there. To gate on every finding, turn off **`Gate comparison branches on new code`** in Project Settings.

When AI pull request review is on, AI review comments that match the blocking severities also fail the gate. See AI Pull-Request Review.

### What the Gate Ignores

Whatever severities you choose, these never count:

| Finding                         | Why                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------- |
| Accepted findings               | Your team has already decided about them.                                                     |
| Findings the scanner suppressed | For example, a vendor has formally stated that a vulnerability does not affect their package. |
| Likely false positives          | The AI reviewer found evidence the code is safe.                                              |

So the gate works on the same list a person would call real, which is why your team can trust what it blocks.

### Choosing a Setting

{% hint style="info" %}
**Note:** Start on **Blocker** only. Add **Critical** once the existing backlog is under control, then **Major** if your team wants it. A gate your team doesn't trust gets bypassed.
{% endhint %}

| Setting                     | Good for                                                       |
| --------------------------- | -------------------------------------------------------------- |
| Report-only (empty)         | A short trial period, while your team gets used to the results |
| Blocker                     | Most teams, from day one                                       |
| Blocker and Critical        | Teams with a clean backlog, or regulated code                  |
| Blocker, Critical and Major | Mature teams with strict standards                             |

### Making the Gate Stop a Merge

CodeScan decides whether a scan is blocked. To stop a merge or a build, connect that decision to your git host or pipeline:

* Block Merges With a Required Status Check
* Fail a CI Build on a Blocked Scan

### Related Articles

* Project Settings
* Accept a Finding
* Scan Types and Branches
