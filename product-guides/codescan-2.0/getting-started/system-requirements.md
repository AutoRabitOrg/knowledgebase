---
description: >-
  What you need to use CodeScan in the web app, on pull requests, in CI, from
  the CLI and in VS Code.
---

# System Requirements

**Step 1 of Getting Started.**

CodeScan is a cloud service, so there is nothing to install on a server. This article lists what you need for each way of using it.

In the examples, `https://<your-codescan-url>` stands for your CodeScan application URL. <mark style="color:red;">**\[TO CONFIRM: production URL format to show customers]**</mark>

### Web App

| Requirement | Details                                                                            |
| ----------- | ---------------------------------------------------------------------------------- |
| Browser     | <mark style="color:red;">**\[TO CONFIRM: supported browsers and versions]**</mark> |
| Account     | A CodeScan username and password. See Sign Up and Sign In.                         |

### Git Hosts

| Requirement     | Details                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supported hosts | GitHub, GitLab and Bitbucket. <mark style="color:red;">**\[TO CONFIRM: cloud only, or also GitHub Enterprise Server, GitLab Self-Managed and Bitbucket Data Center]**</mark>             |
| Access token    | A repository access token, needed for private repositories, commit statuses and PR fixes. See Register a Repository.                                                                     |
| Webhook         | Only for pull-request review without a pipeline. Your git host must be able to reach your CodeScan URL. <mark style="color:red;">**\[TO CONFIRM: IP addresses to allow, if any]**</mark> |

### CI/CD

The CodeScan CLI runs in any CI system that can run Node.js. It reads the pull request's target branch automatically from these providers:

| Provider              | Base branch detected automatically |
| --------------------- | ---------------------------------- |
| GitHub Actions        | Yes                                |
| GitLab CI             | Yes                                |
| Bitbucket Pipelines   | Yes                                |
| Azure DevOps          | Yes                                |
| Jenkins (multibranch) | Yes                                |
| AWS CodeBuild         | No. Pass `--base-branch`.          |

### CodeScan CLI

| Requirement      | Details                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Operating system | macOS, Linux or Windows                                                                             |
| Node.js          | Version 20 or later, with npm                                                                       |
| git              | Required. Scans run on a git checkout, and only git-tracked files are scanned.                      |
| Network          | Access to your CodeScan URL                                                                         |
| Credential       | An API key, or a CodeScan username and password. See Create and Manage API Keys.                    |
| helm             | Only if your repository contains Helm charts. Without it, those charts are reported as not scanned. |

To check your local tools:

```bash
node --version
npm --version
git --version
```

### VS Code Extension

| Requirement    | Details                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| VS Code        | Version 1.134 or later. Check it in **`Help → About`**.                                                                                        |
| Workspace      | A git repository opened as the workspace                                                                                                       |
| Credential     | An API key, or a CodeScan username and password                                                                                                |
| `code` command | Only if you install the extension from a terminal. On macOS, run **`Shell Command: Install 'code' command in PATH`** from the Command Palette. |

{% hint style="info" %}
**Note:** On Remote SSH, WSL and containers there is no system keychain, so the CLI and the extension cannot share a sign-in. Sign in inside the environment where you run the scan.
{% endhint %}

### Limits

| Limit            | Value                                                                                                                                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File size        | Files larger than 2 MiB are skipped. Dependency manifests and lockfiles are scanned regardless of size.                                                                                                                                                 |
| CLI scan timeout | A CLI scan stops after 5 minutes with no progress, or after one hour by default. Each project also has a **`CLI Timeout`** of 1 to 120 minutes (default 30). <mark style="color:red;">**\[TO CONFIRM: which timeout applies when both are set]**</mark> |
| VS Code scan     | The notification closes after 900 seconds by default, but the scan keeps running and the findings load when it finishes.                                                                                                                                |

### Next Step

Sign Up and Sign In

### Related Articles

* Getting Started
* Create and Manage API Keys
* Supported Languages and File Types
