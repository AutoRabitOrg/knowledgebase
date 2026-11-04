---
description: >-
  Install the CodeScan CLI, sign in, check the connection and run your first
  review.
---

# Connect the CLI

The CodeScan CLI (`codescan`) runs the same scan as the web app from your terminal. It is also what runs CodeScan in CI and what AI coding agents use. This article takes you from installing it to your first review.

### Before You Start

You need:

* **Node.js 20 or later, with npm.** Check with `node --version` and `npm --version`.
* **git.** Check with `git --version`. Only git-tracked files are scanned.
* **Network access** to your CodeScan URL, `https://<your-codescan-url>`.
* **An API key**, or a CodeScan username and password. Ask your administrator for a key. See Create and Manage API Keys.
* **A registered repository**, so your results use your team's settings. See Register a Repository.
* **helm**, only if your repository contains Helm charts.

### Step 1: Install the CLI

Your CodeScan instance provides the CLI, so it always matches your instance. The download needs no sign-in.

**macOS, Linux and Windows:**

```bash
npm install -g https://<your-codescan-url>/api/sca/cli/codescan.tgz
```

**Or download the file first.** In the web app, open **`Help`** → **`Download CodeScan CLI`**, then install it from the folder you saved it to:

```bash
npm install -g ./codescan.tgz
```

{% hint style="info" %}
**Note:** To download from a terminal on Windows PowerShell, use `curl.exe`, not `curl`. In PowerShell, `curl` is a different command.

```powershell
curl.exe -o codescan.tgz "https://<your-codescan-url>/api/sca/cli/codescan.tgz"
npm install -g .\codescan.tgz
```
{% endhint %}

#### If the Install Fails

| Problem                             | What to do                                                                                                                                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Permissions error on macOS or Linux | Don't use `sudo`. Set a user-level folder with `npm config set prefix ~/.npm-global`, add `~/.npm-global/bin` to your `PATH`, open a new terminal and install again. |
| `codescan` is not recognised        | Open a new terminal. On Windows, check that `%AppData%\npm` is on your `PATH`.                                                                                       |

### Step 2: Sign In

```bash
codescan config
```

The command asks for:

1. **Your CodeScan URL.** Enter the address only, with no path after the host, for example `https://<your-codescan-url>`.
2. **How to sign in.** Choose an API key, or a username and password.
3. **Your secret.** Paste it. It is hidden as you type.

Your secret is stored in your operating system's keychain. Only the URL is saved to `~/.codescan/configuration`. The VS Code extension uses the same sign-in, so you won't need to sign in there again.

### Step 3: Check the Connection

```bash
codescan --version
codescan auth status
```

`codescan auth status` shows the URL and credential in use, and whether CodeScan accepts them:

| Exit code | Meaning                                                                       |
| --------- | ----------------------------------------------------------------------------- |
| `0`       | Connected                                                                     |
| `1`       | The credential is missing or was rejected. Run `codescan config` again.       |
| `2`       | The check could not finish, for example because CodeScan could not be reached |

### Step 4: Run Your First Review

1. Open a terminal at the root of your repository.
2. Add `.codescan/` to your `.gitignore`. The CLI writes reports and a debug trace there, and the trace contains source code.
3. Run:

```bash
codescan review
```

The CLI uploads your workspace, starts the scan and shows progress. When it finishes, it prints a summary and the scan ID, for example `SCA-42`. The same scan is in the web app.

To check only your work, rather than the whole repository:

| To check                                 | Run                                              |
| ---------------------------------------- | ------------------------------------------------ |
| Uncommitted changes, staged and unstaged | `codescan review --local`                        |
| The committed work on your branch        | `codescan review --pr --base-branch origin/main` |

Run `git fetch origin main` first, so the base branch is in your clone. `git add` new files first too: the CLI skips untracked files and tells you how many.

For a report you can open in a browser, add `--html`. Reports are saved in `.codescan/reports/`.

### Keeping the CLI Up to Date

When your CodeScan instance is upgraded, run:

```bash
codescan update
```

The CLI warns you, at most once a day, if it has fallen behind your instance.

### Next Steps

* Run CodeScan in your pipeline: Run CodeScan in CI
* Let Claude Code check its own work: Use CodeScan With AI Coding Agents
* Every command and flag: CLI Reference
* Back to Getting Started, step 10

### Related Articles

* Connect VS Code
* Troubleshooting
