---
description: >-
  Create a GitLab token, add the repository to CodeScan, and turn on automatic
  pull-request scans with a webhook.
---

# Register a GitLab Repository

This article takes you through registering a GitLab repository in three parts:

1. Create a GitLab access token.
2. Add the project in CodeScan.
3. Turn on automatic pull-request scans with a webhook (optional, recommended).

### Before You Start

You need:

* The <mark style="background-color:yellow;">**Tenant manager**</mark> or <mark style="background-color:yellow;">**ACA admin**</mark> role in CodeScan. See Users, Roles and Permissions.
* Permission in GitLab to create access tokens and webhooks for the repository.&#x20;
* The repository's web address, for example `https://gitlab.com/your-group/your-project`.

### Part 1: Create a GitLab Access Token

CodeScan uses the token to read the repository, report the quality gate result, and post review comments. Use a **project access token**: it belongs to the project rather than to a person, so access doesn't stop when someone leaves.

In GitLab, what a token can do depends on two things: the **role** you give it and the **scopes** you select.

1. In GitLab, open the project.
2. Select **`Settings`** → **`Access tokens`**, then **`Add new token`**.
3. Enter a **token name**, such as _CodeScan_, and an **expiration date**.
4. Under **role**, select **`Developer`**.
5. Under **scopes**, select:

| Scope                  | What it allows                                          | Needed for                                                                                                                         |
| ---------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **`read_repository`**  | Read access (pull) to the repository                    | Reading your code                                                                                                                  |
| **`api`**              | Read and write access to the project's API              | Review comments and the quality gate status on merge requests. GitLab has no narrower scope for this: **`read_api`** is read-only. |
| **`write_repository`** | Read and write access (pull and push) to the repository | Only if you use PR fixes, so CodeScan can push the fix branch                                                                      |

6. Select **`Create project access token`**, then copy the token. GitLab shows it only once.

For GitLab's own instructions, see [Project access tokens](https://docs.gitlab.com/user/project/settings/project_access_tokens/).

{% hint style="info" %}
**Note:** The **`api`** scope is broad, but a project access token only reaches the one project it belongs to. Note the token's expiry date: when it expires, you'll need to replace it.
{% endhint %}

### Part 2: Add the Project in CodeScan

Add the project in CodeScan by following Adding the Project in CodeScan. The steps and settings are the same for every git host.

For GitLab:

* In **`Repository URL`**, enter the repository's web address, for example `https://gitlab.com/your-group/your-project`.
* In **`Access Token`**, paste the token from Part 1.
* When you're done, check that the new row shows **GitLab** under **`Provider`** and **`Authenticated`** under **`Status`**.

### Part 3: Turn On Automatic Pull-Request Scans

With a webhook, GitLab tells CodeScan whenever a pull request is opened or updated, and CodeScan scans it straight away. No pipeline is needed.

#### Step 1: Find Your Tenant ID

1. In the CodeScan sidebar, select your organisation name at the bottom.
2. Note the **`Tenant ID`**.

<figure><img src="../../../../.gitbook/assets/image (3044).png" alt="" width="235"><figcaption></figcaption></figure>

#### Step 2: Build Your Webhook URL

Your webhook URL has this form:

```
https://<your-codescan-url>/api/sca/webhooks/gitlab/<tenant-id>
```

Replace `<your-codescan-url>` with the address you use to open CodeScan, and `<tenant-id>` with your **`Tenant ID`** in **lowercase**.

{% hint style="warning" %}
**Important Note:** The tenant ID in the webhook URL must be lowercase, even though CodeScan shows it in capitals. For example, if your **`Tenant ID`** is `ABC123`, use `abc123` in the URL.
{% endhint %}

#### Step 3: Create the Webhook in GitLab

1. In GitLab, open the project, then **`Settings`** → **`Webhooks`**, and add a new webhook.&#x20;
2. **URL:** your webhook URL from step 3, ending in `/gitlab/<tenant-id>`.
3. **Secret token:** create a unique random **`secret token`** in GitLab, paste this value in CodeScan.
4. **Trigger:** select **Merge request events** only.
5. Leave SSL verification on, and save.

#### Step 4: Test It

1. Open a pull request in the repository, or push a commit to an open one.
2. In CodeScan, a new scan appears with the context **Pull Request**.
3. If no scan appears, check the webhook's delivery history in GitLab. A rejected signature means the secret in GitLab does not match the **`Webhook key`** in CodeScan.

#### Optional: AI Review Comments

To have the AI write review comments on each pull request, turn on **`AI pull request review`** for the project. Comments count toward the quality gate. See AI Pull-Request Review.

### Next Step

Set Up Your Project

### Related Articles

* Register a Repository
* Pull-Request Review Overview
