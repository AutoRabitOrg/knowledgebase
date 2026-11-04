---
description: >-
  Have the AI write review comments on pull requests, and decide whether they
  count toward the gate.
---

# AI Pull Request Review

AI pull request review writes review comments on each pull request, like a reviewer on your team would. It is a separate switch from AI finding review, and it uses AI credits.

### Switching It On

1. Open **`Repositories`** and select the repository.
2. Click **`Edit`** and turn on **`AI pull request review`**.

Pull requests are reviewed by webhook or from CI.

### How Large Pull Requests Are Handled

For a large pull request, CodeScan first maps every changed file: its language, what changed, and whether the change is logic, tests, generated code, a rename or formatting only. It then picks the files that most deserve a close review and reviews those in depth. Small pull requests skip this step.

The review always states how much of the pull request it covered, for example how many files were reviewed out of the total, so a partial review is never presented as complete.

### What You See

* **On the pull request:** the AI's review comments.
* **On the scan page:** a **Comments** tile and a **Pull Requests** section listing the comments, grouped by category and severity.

### Comments and the Quality Gate

AI review comments can count toward the quality gate. When comments match the project's blocking severities, the scan page shows a red **Fails the quality gate** banner.

Each comment can be accepted or restored like a finding. Accepted comments are not posted again and do not fail the gate.

### Related Articles

* Pull-Request Review Overview
* How the Quality Gate Works
* AI Credits
