---
description: >-
  Start a scan from the web app, the CLI, VS Code, a pull request or CI, and
  follow it to the result.
---

# Start a Scan

This article explains how to start a scan, from your first full scan in the web app to scans from the CLI, VS Code, pull requests and CI.

### Your First Scan: a Full Scan of Your Main Branch

Start with a full scan of the branch your team merges into, usually `main`. It gives you a baseline of where your code stands today. It also lets later pull-request scans tell new findings from findings that were already there. Until the base branch has been scanned, those findings show as unclassified.

### Starting a Scan in the Web App

1. Open **`Analysis Findings`** and select the project.
2. Select **`Run Analysis`**.
3. Choose the branch to scan.
4. Leave **`Compare Against`** empty for a full scan. To label each finding as new or pre-existing against another branch, set **`Compare Against`** to that branch.
5. Start the scan.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 15.27.30.png" alt="" width="563"><figcaption></figcaption></figure>

#### While It Runs

* Progress updates live. On the project card, a pulsing yellow pill means a scan is running.
* You can close the window. The scan keeps running.
* To stop it, select **`Cancel Analysis`**.

Each scan gets a number, such as `SCA-1`, whichever way it was started.

#### When It Finishes

The scan shows one of these statuses:

| Status     | Meaning                                                                      |
| ---------- | ---------------------------------------------------------------------------- |
| Successful | Finished, with no findings of the severities that fail the gate              |
| Blocked    | Finished, with at least one finding of a severity that fails the gate        |
| Partial    | <mark style="color:red;">**\[TO CONFIRM: what a partial scan means]**</mark> |
| Failed     | Could not finish                                                             |
| Cancelled  | Someone cancelled it                                                         |

A blocked first scan is normal: it shows your existing backlog. Open the scan to read the results. See Reading Scan Results.

### Other Ways to Start a Scan

Every scan is recorded in the web app, whichever way it starts.

| Where         | You want to check                       | How to start it                                                                        |
| ------------- | --------------------------------------- | -------------------------------------------------------------------------------------- |
| Web app       | A whole branch                          | **`Run Analysis`**, with **`Compare Against`** empty                                   |
| Web app       | A branch, compared with another         | **`Run Analysis`**, with **`Compare Against`** set                                     |
| VS Code       | The whole workspace                     | **`CodeScan: Scan Workspace`**                                                         |
| VS Code       | Your uncommitted changes                | **`CodeScan: Scan Changed Files`**                                                     |
| VS Code       | The committed work on your branch       | **`CodeScan: Scan Branch Changes`**                                                    |
| CLI           | The whole repository                    | `codescan review`                                                                      |
| CLI           | Your uncommitted changes                | `codescan review --local`                                                              |
| CLI           | The committed work on your branch       | `codescan review --pr`                                                                 |
| CLI           | A whole branch, compared with another   | `codescan review --base-branch main`                                                   |
| Pull requests | Every pull request, automatically       | A webhook from your git host. See Set Up Webhook-Triggered Review.                     |
| CI            | Every pull request and your main branch | `codescan review --pr` and `codescan review` in your pipeline. See Run CodeScan in CI. |

To cancel: **`Cancel Analysis`** in the web app, the progress notification in VS Code, or **Ctrl+C** in the CLI.

For what each scan type covers and how branches are compared, see Scan Types and Branches.

### If Your First Scan Looks Wrong

| What you see                                                  | What to do                                                                                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Nothing was scanned                                           | The scope was empty, for example because everything was excluded. Check **`Sources Exclusions`**.                         |
| A wall of style findings                                      | Normal on a first scan of a large codebase. Run Review Noisy Rules after reading the Blockers.                            |
| Many findings in test code                                    | Add your test paths under **`Tests Folders`**, then scan again.                                                           |
| Results differ between the web app and a developer's computer | The developer's scan used default rules. Check that their git remote matches the registered **`Repository URL`** exactly. |
| Helm charts reported as not scanned                           | Install `helm` where the scan runs.                                                                                       |

### Next Step

Reading Scan Results

### Related Articles

* Scan Types and Branches
* Troubleshooting
