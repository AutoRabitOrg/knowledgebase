---
description: The project settings to choose before your first scan, and why.
---

# Project Configuration

A few settings change what your first scan shows. Set them now, so the first results your team sees are accurate and readable.&#x20;

Open **`Repositories`**, select the repository you registered, and edit it.

### 1. Exclusions and Test Folders

Add your test paths under **Repositories** ⇒ **Select a repository** ⇒ **`Exclusions`** ⇒ **`Tests Folders`**, for example `/test/` or `**/*.spec.ts`. Tests are then kept out of the rule scan, and CodeScan can show which tests a change affects.

Add generated or vendored code that your team cannot change under **`Sources Exclusions`**, for example `/vendor/`.

See Exclusions and Test Folders.

### 2. Keep the Quality Gate on Blocker

**`Severities that fail the gate`** is set to **Blocker** by default. Keep it there for now. Once your team has worked through the first results, you can add Critical.

### 3. Decide on AI Features

AI features use AI credits. The scan itself never does.

| Setting                                | Switch it on if you want                                                           | Our suggestion for the first scan          |
| -------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------ |
| **`AI finding review`**                | Likely false positives flagged with a reason, so your team reads real issues first | On, for Blocker and Critical               |
| **`Severities included in AI review`** | To limit which findings the AI reviews                                             | Blocker and Critical                       |
| **`Advanced AI Suggestions`**          | Suggested fixes, as patches or PR fixes                                            | On, if AI finding review is on             |
| **`AI test quality review`**           | A score for each of your tests                                                     | Later, once the main results are in hand   |
| **`AI pull request review`**           | AI review comments on pull requests                                                | Later, when you set up pull-request review |

### 5. Switch On the Coverage Estimate

Turn on **`Test coverage estimate (no AI)`**. It shows which code your tests can reach, uses no credits, and needs a full scan, which you're about to run.

Save your changes.

### Next Step

### Set the Base Branch

After your first full scan, set **`Default Comparison Base Branch`** to the branch your team merges into, usually `main`. Pull-request and branch scans compare against it, to tell new findings from old ones.

### Related Articles

* Project Settings
* AI Credits
