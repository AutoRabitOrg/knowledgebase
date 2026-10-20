# CodeScan CLI - Install and Run

This guide explains how to install the CodeScan CLI (`codescan`), point it at your CodeScan instance, and run a review. The download needs no sign-in. An API key, or a username and password, is used only when a command talks to CodeScan.

## Before you start <a href="#before-you-start" id="before-you-start"></a>

Please check prerequisites:

* **Node.js 20 or later** and **npm**. The published package is installed with npm.
* **git**. A scan runs on a git checkout. Only git-tracked files are scanned.
* **Network access** to the CodeScan host.
* A **CodeScan API key**, or a username and password, for any command that calls CodeScan. An administrator creates a key under **API Keys**. The key is sent as the `X-API-Key` header.
* **helm**, only if the repository contains Helm charts. Without it, those charts are reported as not scanned.

Check the local tools:

`node --version`&#x20;

`npm --version`&#x20;

`git --version`

## 1. Install the package <a href="#id-1.-install-the-package" id="id-1.-install-the-package"></a>

Your CodeScan instance serves the CLI. The download needs no API key. Install it straight from the instance so the CLI matches that environment.

{% hint style="info" %}
Replace `CUSTOM_URL` with your instance URL
{% endhint %}

**macOS / Linux (bash or zsh)**

`npm install -g CUSTOM_URL/api/sca/cli/codescan.tgz`

**Windows PowerShell**

`npm install -g CUSTOM_URL/api/sca/cli/codescan.tgz`

Or download the file first.&#x20;

In the web app, open **CodeScan Help** and choose **Download CodeScan CLI**.&#x20;

**macOS / Linux**

`curl -o codescan.tgz "CUSTOM_URL/api/sca/cli/codescan.tgz" npm install -g ./codescan.tgz`

**Windows PowerShell**

PowerShell’s `curl` alias is `Invoke-WebRequest`. Call `curl.exe` so the download is saved as written.

`curl.exe -o codescan.tgz "CUSTOM_URL/api/sca/cli/codescan.tgz" npm install -g .\codescan.tgz`

A successful download leaves a non-empty `codescan.tgz` in the current folder.

## 2. Connect to CodeScan <a href="#id-2.-connect-to-codescan" id="id-2.-connect-to-codescan"></a>

CodeScan needs two values: the application URL and a credential. On your own machine, store them once. In CI, pass them as environment variables.

### On your own machine <a href="#on-your-own-machine" id="on-your-own-machine"></a>

`codescan config`

The command asks which credential to use (API key, or username and password) and for the URL, then prompts for the secret with the input hidden. The secret goes into the OS keychain: macOS Keychain, Windows credential store, or libsecret on Linux. Only the URL is written to `~/.codescan/configuration`. The VS Code extension uses the same keychain entry, so signing in once covers both.

The URL is the site origin only.&#x20;

Other commands you will use:

| Command                | What it does                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `codescan auth login`  | Sign in without the setup questions. `--api-key` prompts for a key. `--username <name>` signs in with a password. |
| `codescan auth status` | Shows the URL and credential in use, where they came from, and whether CodeScan accepts them.                     |
| `codescan auth logout` | Removes the stored credential.                                                                                    |

### In CI, containers, and servers <a href="#in-ci-containers-and-servers" id="in-ci-containers-and-servers"></a>

There is usually no keychain, so set both variables. Without a URL, the CLI falls back to a local development address and the scan fails.

**macOS / Linux (current terminal session)**

`export CODESCAN_APP_URL="CUSTOM_URL" export CODESCAN_API_KEY="<YOUR_API_KEY>"`

**Windows PowerShell (current terminal session)**

`$env:CODESCAN_APP_URL = "CUSTOM_URL" $env:CODESCAN_API_KEY = "<YOUR_API_KEY>"`

These assignments last for the current terminal. To keep them for later sessions:

* **bash:** add the two `export` lines to `~/.bashrc` (or `~/.zshrc` on zsh), then open a new terminal.
* **Windows:** set User environment variables named `CODESCAN_APP_URL` and `CODESCAN_API_KEY`, then open a new terminal. You can also run:

`setx CODESCAN_APP_URL "CUSTOM_URL" setx CODESCAN_API_KEY "<YOUR_API_KEY>"`

`setx` updates future terminals. The current window still needs the `$env:` assignments above. Prefer `codescan config` on a laptop so the key stays in the keychain rather than in a profile file.

How the CLI picks its settings, first match wins:

| Setting    | Order                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------- |
| URL        | `--url` flag, then `CODESCAN_APP_URL`, then the URL saved by `codescan config`                                  |
| Credential | `--api-key` flag, then `CODESCAN_API_KEY`, then the API key in the keychain, then a saved username and password |

## 3. Confirm the install <a href="#id-3.-confirm-the-install" id="id-3.-confirm-the-install"></a>

`codescan --version codescan auth status`

`codescan --version` prints the CLI version and exits 0. If the shell says the command is not recognized, open a new terminal so it picks up npm’s global bin directory, then run it again.

`codescan auth status` exits `0` when CodeScan accepts the credential, `1` when it is missing or rejected, and `2` when the check could not be completed (for example, the host is unreachable).

## 4. Review a folder <a href="#id-4.-review-a-folder" id="id-4.-review-a-folder"></a>

From the root of the git checkout you want reviewed, run:

`codescan review`

You can pass another folder, for example `codescan review ./force-app`. The CLI uploads the workspace, starts the scan on CodeScan, streams progress, and prints a summary. The scan is recorded in the web app as `SCA-n`.

What happens:

1. The CLI authenticates with the keychain credential, or with `CODESCAN_API_KEY` when that variable is set.
2. It uploads git-tracked files. Paths in `.gitignore` and in the project’s **Sources Exclusions** are left out, as are binaries and files larger than 2 MiB. Dependency manifests and lockfiles are still uploaded.
3. A file you never `git add` is skipped. The CLI tells you how many.
4. CodeScan scans on the server. It does not run your build or your tests.

For a machine-readable result, add `--json`. Progress and warnings go to standard error, so you can redirect standard output:

`codescan review --json > review.json`

The object includes:

| Field                 | Meaning                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `violationsWereFound` | `true` when the quality gate blocked the scan. A finding that is accepted, suppressed, or flagged as a likely false positive does not block. |
| `findingCount`        | Number of findings                                                                                                                           |
| `uploadedScanId`      | The scan id, for example `SCA-42`                                                                                                            |
| `executiveSummary`    | Short summary, when one was produced                                                                                                         |
| `details`             | Each finding: rule, file, line, severity, reason, recommendation, `suggestedFixes`, and `aiSuspectedFP` when the reviewer doubts it          |
| `scanScope`           | `emptyReason` is set when nothing was scanned. That result is unknown, not clean.                                                            |

Other useful flags:

| Flag                                       | Effect                                                                                        |
| ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `--html`, `--sarif`, `--junit`, `--gitlab` | Writes a report under `.codescan/reports/`                                                    |
| `--progress`                               | Live dashboard on a terminal                                                                  |
| `--check-tests`                            | Keeps test files for test-quality analysis. Test folders still stay out of the rule scan.     |
| `--verify-secrets`                         | Checks detected secrets against their providers with read-only calls. Off unless you pass it. |
| `--local`                                  | Reviews uncommitted changes against `HEAD`. Not with `--pr`.                                  |
| `--pr`                                     | Reviews committed changes against the base branch. See the next sections.                     |

Example with an HTML report:

`codescan review --json --html`

The CLI writes a `.codescan/` folder in the repository: reports under `.codescan/reports/`, and a debug trace under `.codescan/debug/`. The trace contains source code and prompts. Add `.codescan/` to `.gitignore`. Old runs are cleaned up automatically: the last 5 runs are kept, and anything older than 30 days is removed.

## 5. Review uncommitted changes <a href="#id-5.-review-uncommitted-changes" id="id-5.-review-uncommitted-changes"></a>

To check what you have not committed yet, staged and unstaged:

`codescan review --local`

`git add` new files first. A file that is not tracked is skipped. This mode cannot be combined with `--pr`.

## 6. Review a pull request <a href="#id-6.-review-a-pull-request" id="id-6.-review-a-pull-request"></a>

Pull-request mode reviews committed work on the branch, not the working tree. Use `--local` for uncommitted edits.

`git fetch origin master codescan review --pr --base-branch origin/master`

On Windows PowerShell the review command is the same:

`git fetch origin master codescan review --pr --base-branch origin/master`

Add `--json` when you need the structured result on standard output:

`codescan review --pr --base-branch origin/master --json`

The base branch is chosen in this order:

1. `--base-branch`
2. The pull request’s target branch, read from the CI environment
3. The project’s **Default Comparison Base Branch** in CodeScan
4. The clone’s `origin/HEAD`
5. `origin/main`, then `origin/master`

If none resolves, the scan stops and tells you what it tried. In a shallow CI clone the CLI fetches the missing history itself. A full clone is more reliable.

On a CI pull-request job you can omit `--base-branch` when the provider sets the matching variable:

| Variable                              | Typical environment |
| ------------------------------------- | ------------------- |
| `GITHUB_BASE_REF`                     | GitHub Actions      |
| `BITBUCKET_PR_DESTINATION_BRANCH`     | Bitbucket Pipelines |
| `CI_MERGE_REQUEST_TARGET_BRANCH_NAME` | GitLab CI           |
| `SYSTEM_PULLREQUESTTARGETBRANCH`      | Azure DevOps        |
| `CHANGE_TARGET`                       | Jenkins multibranch |

AWS CodeBuild does not provide the base branch. Pass `--base-branch` there. Locally, pass `--base-branch` as well. You do not need to export `GITHUB_BASE_REF` on your own machine.

The whole workspace is still uploaded, so rules that look across files keep their context. Only the files reported on are narrowed to the change. A pull-request scan also computes the blast radius of that change.

## Exit codes <a href="#exit-codes" id="exit-codes"></a>

| Code | Meaning                                                                                                                                                                         |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`  | The scan finished, with or without findings, and even when the quality gate blocked it. Also: nothing was in scope to scan.                                                     |
| `1`  | The command failed before a completed scan: authentication, the host was unreachable, the base branch was not found, the upload was too large, or the scan failed or timed out. |

`codescan review` exits 0 even when the scan is blocked. The gate is enforced by CodeScan. To fail a pipeline, read `violationsWereFound` from the JSON:

`mkdir -p .codescan codescan review --pr --json > .codescan/result.json node -e 'process.exit(JSON.parse(require("fs").readFileSync(".codescan/result.json","utf8")).violationsWereFound ? 1 : 0)'`

## Update and uninstall <a href="#update-and-uninstall" id="update-and-uninstall"></a>

`codescan update`

This downloads the CLI that matches your CodeScan instance. Run it after the instance is upgraded. If a command you expect is missing (`Command sbom not found`), the CLI is older than the instance.

To remove it:

`codescan auth logout npm uninstall -g @autorabit/codescan`

## Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

#### `codescan` **is not recognized**

Open a new terminal after `npm install -g`. Confirm the global npm bin directory is on `PATH` (`npm prefix -g` on macOS/Linux, `%AppData%\npm` on Windows).

#### **Authentication required**

No credential is available in this terminal. Run `codescan config`, or set `CODESCAN_API_KEY` and `CODESCAN_APP_URL`. Check what is in use with:

`codescan auth status`

#### **The scan tries to reach localhost**

`CODESCAN_APP_URL` is not set, and `codescan config` has not saved a URL. Set the URL to `CUSTOM_URL` with no extra path.

#### **CodeScan rejected the API key**

The key is missing, wrong, expired, or revoked. Create or rotate it under **API Keys**, then run `codescan auth login --api-key` or export `CODESCAN_API_KEY` again.

#### `--pr` **cannot resolve the base branch**

The base branch is not in this clone, or no CI variable names it. Fetch it and pass it:

`git fetch origin master codescan review --pr --base-branch origin/master`

#### **N untracked file(s) were NOT scanned**

Those files were never added to git. Run `git add` on the ones you want scanned, or ignore them in `.gitignore`.

#### **Nothing was scanned**

The scope was empty: no changes, or everything excluded. The result is unknown, not a clean scan. Read `scanScope.emptyReason` in the JSON.

#### **Corporate TLS inspection**

For a dev host that presents a certificate the machine does not trust:

`codescan review --json --trust-all-certificates`

Use `--trust-all-certificates` only in local or dev environments.

#### **The pipeline is green but the scan was blocked**

The CLI exits 0 on findings by design. Add the `violationsWereFound` check from Exit codes.
