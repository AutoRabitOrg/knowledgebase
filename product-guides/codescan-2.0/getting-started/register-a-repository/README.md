---
description: >-
  What registering a repository means, and how to register one on GitHub, GitLab
  or Bitbucket.
---

# Register a Repository

Registering a repository tells CodeScan where your code is and how to reach it. A registered repository becomes a project, with its own settings, rules, accepted findings and quality gate.

Register a repository before your team scans it from the CLI or VS Code. Scans of an unregistered repository use default rules, so their results won't match CI.

### Choose Your Git Host

| Git host  | Article                         |
| --------- | ------------------------------- |
| GitHub    | Register a GitHub Repository    |
| GitLab    | Register a GitLab Repository    |
| Bitbucket | Register a Bitbucket Repository |

Each article has three parts:

1. **Create an access token** in your git host.
2. **Add the project** in CodeScan. This step is the same for every git host, and is described below.
3. **Turn on automatic pull-request scans** with a webhook. This is optional, but it's how CodeScan reviews every pull request without a pipeline.

### Adding the Project in CodeScan

The Add Project window is the same for every git host. Create your access token first, using Part 1 of your git host's article, then follow these steps.

1. In the CodeScan sidebar, select **`Repositories`**. The **Project Properties** page lists your registered projects.
2. Select **`Add Project`**.
3. Fill in the **Add Project** window, section by section, as described below.
4. Select **`Add Project`**.
5. Check that the new row shows your git host under **`Provider`** and **`Authenticated`** under **`Status`**.
6. Go back to your git host's article for Part 3, to turn on automatic pull-request scans.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-10-16 at 13.04.18.png" alt="" width="563"><figcaption></figcaption></figure>

#### Project

| Field                   | What to enter                                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Project Name`**      | Optional. The name your team will see in CodeScan. Leave it blank to use the name from the URL.                                                                                                                             |
| **`Repository URL`**    | The repository's web address, for example `https://github.com/your-org/your-repo`, `https://gitlab.com/your-group/your-project` or `https://bitbucket.org/your-workspace/your-repo`. Do not add `.git` or a trailing slash. |
| **`Repository Access`** | **`Private`** or **`Public`**. As per your repo visibility in the provider.                                                                                                                                                 |

{% hint style="warning" %}
**Important Note:** CodeScan matches repositories by URL exactly. A URL that differs in upper and lower case, or ends in `.git`, is treated as a different repository, with its own settings and accepted findings.
{% endhint %}

#### Scanning

| Field                                | What to enter                                                                                                                                                                                        |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Default Comparison Base Branch`** | When a scan arrives without an explicit base branch, comparison branches fall back to this one. **Only branches with a completed full scan are listed.** Add later after the full scan is completed. |
| **`CLI Timeout`**                    | The longest a CodeScan CLI scan of this project can run, in minutes. A scan that runs longer is stopped. Default: 30.                                                                                |

#### Quality Gate

| Field                               | What to choose                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Severities that fail the gate`** | Which severities fail a build or a pull request: **`Blocker`**, **`Critical`** or **`Major`**. Default: Blocker only. We suggest keeping the default for now. |

#### AI Review

AI features use AI credits. The scan itself never does.

| Field                                  | What it does                                                                                                                                                                                | Default              |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **`AI finding review`**                | Turns all AI features on or off for this project. The AI reviewer flags likely false positives and writes suggested fixes.                                                                  | On                   |
| **`AI pull request review`**           | Reviews pull requests with AI. With a webhook set up (Part 3), pull requests are reviewed automatically when they are opened or updated, and review comments count toward the quality gate. | Off                  |
| **`AI test quality review`**           | Reviews test classes for weak assertions and missing coverage.                                                                                                                              | Off                  |
| **`Severities included in AI review`** | Which severities the AI reviews. Other severities are still reported, without AI review.                                                                                                    | Blocker and Critical |

#### Insights

| Field                                | What it does                                                                                                                                                                        | Default |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **`Test coverage estimate (no AI)`** | On every full scan, estimates how much production code your tests can reach, and charts it on the Analysis Dashboard. A static estimate, not measured coverage. Uses no AI credits. | On      |

#### Authenticate Repository

| Field                        | What to enter                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **`Access Token`**           | The access token from Part 1 of your git host's article.                                                            |
| **`Webhook key (Optional)`** | Needed only for automatic pull-request scans. You can enter it now or later. See Part 3 of your git host's article. |

Select the eye icon next to a field to check what you pasted.

### Your Registered Projects

In the CodeScan sidebar, **`Repositories`** opens the **Project Properties** page. It lists every registered project, with:

| Column            | What it shows                                                                    |
| ----------------- | -------------------------------------------------------------------------------- |
| **`Project`**     | The project name                                                                 |
| **`URL`**         | The repository's web address                                                     |
| **`Provider`**    | The git host, for example GitHub                                                 |
| **`Created At`**  | When the project was registered                                                  |
| **`CLI Timeout`** | The longest a CLI scan of this project can run                                   |
| **`Status`**      | **`Authenticated`** when CodeScan can reach the repository with its access token |
| **`Visibility`**  | Whether the project is private or public                                         |

Use **`Search`** to find a project.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-10-16 at 13.06.30.png" alt=""><figcaption></figcaption></figure>

### Replacing a Token

When an access token expires or is rotated, select the project in **`Repositories`** and choose **`Re-Authenticate`**. Paste the new **`Access Token`** and the **`Webhook key`** together, then check that the row shows **`Authenticated`** again.

### How Scans Find the Registered Repository

The CLI and the VS Code extension send the repository's git remote with every scan, and CodeScan matches it to a registered project.

| Result          | What it means                                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Registered      | The project's rules, exclusions and accepted findings were applied. Results match CI.                                                                                     |
| Unregistered    | The git remote does not match a registered project, so default rules were used. Register the repository, or check that the URL matches exactly.                           |
| No remote found | The folder has no git remote. The scan used default rules and was recorded under the folder name. With the CLI, pass `--repo-url` to use a registered project's settings. |

If a developer scans an unregistered repository in VS Code, the extension also offers **`Register Repository`**.&#x20;

### Next Step

Set Up Your Project

### Related Articles

* Project Settings
* Block Merges With a Required Status Check
