# Register a Repository

**Step 3 of Getting Started.**

Registering a repository tells CodeScan where your code is and how to reach it. A registered repository becomes a project, with its own settings, rules, accepted findings and quality gate. CodeScan works with GitHub, GitLab and Bitbucket.

Register a repository before your team scans it from the CLI or VS Code. Scans of an unregistered repository use default rules, so their results won't match CI.

### Before You Start

You need:

* The <mark style="background-color:yellow;">**Tenant manager**</mark> or <mark style="background-color:yellow;">**ACA admin**</mark> role. See Users, Roles and Permissions.
* The repository's web URL, for example `https://github.com/your-org/your-repo`.
* A repository access token, created in your git host. A private repository always needs one. A public repository needs a token, a webhook key, or both.

#### Token Permissions

| Git host                                      | Token permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub, fine-grained token                    | **`Contents: Read`** and **`Pull requests: Read and write`** <mark style="color:red;">**\[TO CONFIRM: whether**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`Commit statuses: Read and write`**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**is also needed for the commit status, and whether PR fixes need**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`Contents: Read and write`**</mark><mark style="color:red;">**]**</mark> |
| GitHub, classic token on a private repository | The **`repo`** scope                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| GitLab                                        | <mark style="color:red;">**\[TO CONFIRM: token type and scopes]**</mark>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bitbucket                                     | <mark style="color:red;">**\[TO CONFIRM: token type and permissions]**</mark>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

{% hint style="info" %}
**Note:** Create the token from an account your team controls, such as a service account, rather than a personal account. That way, access doesn't stop when one person leaves.
{% endhint %}

### Registering the Repository

1. In CodeScan, open **`Repositories`**.
2. Add a repository. <mark style="color:red;">**\[TO CONFIRM: exact button name]**</mark>
3. In **`Repository URL`**, enter the repository's web URL. Do not add `.git` or a trailing slash.
4. Under **`Authenticate`**, paste the **`Access Token`**.
5. If you plan to review pull requests by webhook, also enter a **`Webhook Key`**: a secret you create yourself and later enter in your git host. You can generate one with `openssl rand -hex 32`. You can also add it later, in step 10.
6. Save.
7. Check that the repository row shows **`Authenticated`**.

<mark style="color:red;">**\[SCREENSHOT: Repositories page with an authenticated repository]**</mark>

{% hint style="warning" %}
**Important Note:** CodeScan matches repositories by URL exactly. A URL that differs in upper and lower case, or ends in `.git`, is treated as a different repository, with its own settings and accepted findings.
{% endhint %}

### What the Token Is Used For

| With a token                                                                          | Without a token                                                               |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| CodeScan can read a private repository.                                               | Only public repositories can be scanned by webhook.                           |
| CodeScan reports the quality gate result back to the pull request as a commit status. | The quality gate result is informational only. It cannot block a merge.       |
| A developer can create a PR fix from a scan.                                          | PR fixes are not available. <mark style="color:red;">**\[TO CONFIRM]**</mark> |

### Registering From VS Code

If a developer scans an unregistered repository in VS Code, the extension shows **Unregistered** and offers **`Register Repository`**. <mark style="color:red;">**\[TO CONFIRM: what Register Repository does, and which roles can use it]**</mark>

### Replacing a Token

When a token expires or is rotated, open **`Repositories`**, select the repository and choose **`Re-Authenticate`**. Paste the new **`Access Token`** and the **`Webhook Key`** together, then check that the row shows **`Authenticated`** again.

### How Scans Find the Registered Repository

The CLI and the VS Code extension send the repository's git remote with every scan, and CodeScan matches it to a registered repository.

| Result          | What it means                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Registered      | The repository's rules, exclusions and accepted findings were applied. Results match CI.                                                                                     |
| Unregistered    | The git remote does not match a registered repository, so default rules were used. Register the repository, or check that the URL matches exactly.                           |
| No remote found | The folder has no git remote. The scan used default rules and was recorded under the folder name. With the CLI, pass `--repo-url` to use a registered repository's settings. |

### Next Step

Set Up Your Project

### Related Articles

* Project Settings
* Set Up Webhook-Triggered Review
