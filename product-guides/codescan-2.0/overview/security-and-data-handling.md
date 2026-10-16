---
description: >-
  This article explains what CodeScan reads from your code, where it goes, and
  what stays on your machines.
---

# Security and Data Handling

### What Is Uploaded

A scan uploads the git-tracked files in your workspace to your CodeScan instance, minus the exclusions listed in [How a Scan Works](how-a-scan-works.md). CodeScan does not run your build or tests, and it does not change your repository on its own. It writes to your repository only when a developer reviews a PR fix and selects **`Create PR`**. CodeScan then pushes a fix branch (named `codescan/fix-<scan>-<id>`) and opens a pull request against the target branch.

{% hint style="danger" %}
**\[TO CONFIRM before publishing]**

* Hosting region and data residency options
* Encryption in transit and at rest
* How long uploaded workspaces and scan results are kept, and how a customer can delete them
* Security certifications to reference, if any
{% endhint %}

### Repository Access

For webhook scans, commit statuses and PR fixes, CodeScan needs a repository access token. CodeScan uses this access to read code, post results and, when a developer creates a PR fix, push a fix branch and open a pull request.

On GitHub:

* A fine-grained token needs **`Pull requests: Read and write`** and **`Contents: Read`**.
* A classic token on a private repository needs the **`repo`** scope.

<mark style="color:red;">**\[TO CONFIRM: permissions needed for PR fixes (pushing a fix branch needs write access to contents), and equivalent permissions for GitLab and Bitbucket]**</mark>

### AI Processing

AI features run only when they are switched on, and they are switched on per project. When AI finding review runs, the reviewer reads the relevant code from the uploaded workspace with read-only tools. An administrator chooses which AI model backs each AI feature for your organisation.

{% hint style="danger" %}
**\[TO CONFIRM before publishing]**

* Which model providers are used, and where they process data
* Whether customer code or prompts are retained by model providers or used for training
{% endhint %}

### Credentials

The CodeScan CLI and the VS Code extension store your API key or password in your operating system's secret store: macOS Keychain, Windows Credential Manager or libsecret on Linux. Only the CodeScan URL is written to `~/.codescan/configuration`.

In CI, credentials are passed as environment variables.

### Files Written on Your Machine

The CodeScan CLI writes a `.codescan/` folder in your repository.

| Path                     | Contents                                                                 |
| ------------------------ | ------------------------------------------------------------------------ |
| `.codescan/reports/`     | SARIF, JUnit, GitLab and HTML reports                                    |
| `.codescan/debug/`       | A debug trace of each run. **This contains source code and AI prompts.** |
| `.codescan/helm-render/` | Helm charts rendered for scanning                                        |

{% hint style="warning" %}
**Important Note:** Add `.codescan/` to your `.gitignore` so debug traces are never committed.
{% endhint %}

Old runs are cleaned up automatically: the last five runs are kept, and anything older than 30 days is removed. To change this, set `CODESCAN_ARTIFACT_KEEP_LAST` and `CODESCAN_ARTIFACT_MAX_AGE_DAYS`. A value of `0` turns the clean-up off.

### Secret Verification

CodeScan detects secrets such as API keys and private keys in your code. It can also check whether a detected secret is still live, using read-only calls to 29 supported providers.

This check contacts third-party services, so it is off unless you pass `--verify-secrets` on a CLI scan.

### Related Articles

* [What Is CodeScan](../)
* [How a Scan Works](how-a-scan-works.md)
* [Users, Roles and Permissions](../getting-started/sign-up-and-sign-in/users-roles-and-permissions.md)
