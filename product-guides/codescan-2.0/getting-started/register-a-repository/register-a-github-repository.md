---
description: >-
  Create a GitHub token, add the repository to CodeScan, and turn on automatic
  pull-request scans with a webhook.
---

# Register a GitHub Repository

This article takes you through registering a GitHub repository in three parts:

1. Create a GitHub access token.
2. Add the project in CodeScan.
3. Turn on automatic pull-request scans with a webhook (optional, recommended).

### Before You Start

You need:

* The <mark style="background-color:yellow;">**Tenant manager**</mark> or <mark style="background-color:yellow;">**ACA admin**</mark> role in CodeScan. See Users, Roles and Permissions.
* **Admin access** to the repository in GitHub. GitHub requires it to create webhooks.
* The repository's web address, for example `https://github.com/your-org/your-repo`.
*   Webhook payload URL:

    ```
    https://<your-codescan-url>/api/sca/webhooks/github/<tenant-id>
    ```

### Part 1: Create a GitHub Access Token

CodeScan uses the token to read the repository, report the quality gate result on pull requests, and post review comments.

#### Fine-Grained Token (Recommended)

1. In GitHub, open your profile menu → **`Settings`** → **`Developer settings`** → **`Personal access tokens`** → **`Fine-grained tokens`** → **`Generate new token`**.
2. Give the token a name, such as _CodeScan_, and choose an expiry date.
3. Under **`Resource owner`**, choose the organisation that owns the repository.
4. Under **`Repository access`**, choose **`Only select repositories`** and select the repository.
5.  Under **`Permissions`**, set:

    | Permission          | Access         |
    | ------------------- | -------------- |
    | **`Contents`**      | Read and write |
    | **`Pull requests`** | Read and write |
6. Select **`Generate token`** and copy it. GitHub shows it only once.

#### Classic Token

For a private repository, a classic token needs the **`repo`** scope.

For GitHub's own instructions, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

{% hint style="info" %}
**Note:** Create the token from an account your team controls, such as a service account, rather than a personal account. That way, access doesn't stop when one person leaves. Note the token's expiry date: when it expires, you'll need to replace it.
{% endhint %}

### Part 2: Add the Project in CodeScan

1. In the CodeScan sidebar, select **`Repositories`**. The **Project Properties** page lists your registered projects.
2. Select **`Add Project`**.
3. Fill in the **Add Project** window, section by section, as described:

{% hint style="success" %}
[**Review Project Configuration options here**](./)
{% endhint %}

#### Project

| Field                   | What to enter                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **`Project Name`**      | The name your team will see in CodeScan. Leave it blank to use the name from the URL.                                     |
| **`Repository URL`**    | The repository's web address, for example `https://github.com/your-org/your-repo`. Do not add `.git` or a trailing slash. |
| **`Repository Access`** | **`Private`** or **`Public`**. Based on your GitHub repo visibility: public repos do not require tokens.                  |

{% hint style="warning" %}
**Important Note:** CodeScan matches repositories by URL exactly. A URL that differs in upper and lower case, or ends in `.git`, is treated as a different repository, with its own settings and accepted findings.
{% endhint %}

### Part 3: Turn On Automatic Pull-Request Scans

With a webhook, GitHub tells CodeScan whenever a pull request is opened, reopened or updated, and CodeScan scans it straight away. No pipeline is needed.

#### Step 1: Create a Webhook Key

The webhook key is a secret that you create yourself. You enter the same value in two places, CodeScan and GitHub, so CodeScan can check that each event really came from your repository.

Create a long random value, for example with a password manager's generator, or in a terminal on macOS or Linux:

```bash
openssl rand -hex 32
```

Store it somewhere safe, such as your password manager.

If you didn't enter the key in Part 2, add it to the project now: in **`Repositories`**, select the project and choose **`Re-Authenticate`**, then paste the **`Access Token`** and the **`Webhook key`** together.

#### Step 2: Find Your Tenant ID

1. In the CodeScan sidebar, select your organisation name at the bottom.
2. Note the **`Tenant ID`**.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-10-16 at 12.18.32.png" alt="" width="235"><figcaption></figcaption></figure>

#### Step 3: Build Your Webhook URL

Your webhook URL has this form:

```
https://<your-codescan-url>/api/sca/webhooks/github/<tenant-id>
```

Replace `<your-codescan-url>` with the address you use to open CodeScan, and `<tenant-id>` with your **`Tenant ID`** in **lowercase**.

{% hint style="warning" %}
**Important Note:** The tenant ID in the webhook URL must be lowercase, even though CodeScan shows it in capitals. For example, if your **`Tenant ID`** is `ABC123`, use `abc123` in the URL.
{% endhint %}

For example: `https://<your-codescan-url>/api/sca/webhooks/github/abc123`

#### Step 4: Add the Webhook in GitHub

1. In GitHub, open the repository and select **`Settings`**.
2. In the left sidebar, select **`Webhooks`**, then **`Add webhook`**.
3. Fill in the form:

| Field                                                      | What to enter                                                            |
| ---------------------------------------------------------- | ------------------------------------------------------------------------ |
| **`Payload URL`**                                          | Your webhook URL from step 3                                             |
| **`Content type`**                                         | `application/json`                                                       |
| **`Secret`**                                               | Your webhook key: the same value you entered in CodeScan                 |
| **`SSL verification`**                                     | Leave **`Enable SSL verification`** selected                             |
| **`Which events would you like to trigger this webhook?`** | Choose **`Let me select individual events`**, select **`Pull requests`** |
| **`Active`**                                               | Selected                                                                 |

4. Select **`Add webhook`**.

For GitHub's own instructions, see [Creating webhooks](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks).

#### Step 5: Test It

1. Open a pull request in the repository, or push a commit to an open one.
2. In CodeScan, a new scan appears with the context **Pull Request**.
3. In GitHub, open **`Settings`** → **`Webhooks`**, select the webhook and open **`Recent Deliveries`**:
   * A `2xx` response means CodeScan received the event.
   * A `401` response means the **`Secret`** in GitHub does not match the **`Webhook key`** in CodeScan.

Each new commit on the pull request starts a fresh review. If GitHub delivers the same event twice, CodeScan does not create a second review or duplicate comments.

#### Optional: AI Review Comments

To have the AI write review comments on each pull request, turn on **`AI pull request review`** for the project. Comments count toward the quality gate. See AI Pull-Request Review.

### Troubleshooting

| Problem                                       | What to do                                                                                                                                                           |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Status`** is not **`Authenticated`**       | The token is wrong, expired, or lacks the permissions in Part 1. Create a new token and re-authenticate.                                                             |
| GitHub shows `401` in **`Recent Deliveries`** | The webhook secret and the **`Webhook key`** don't match. Enter the same value in both.                                                                              |
| No scan appears after opening a pull request  | Check that the **`Payload URL`** ends in `/github/<tenant-id>` with your tenant ID, that only **`Pull requests`** is selected, and that the webhook is **`Active`**. |
| Results on developers' computers don't match  | Their git remote doesn't match the **`Repository URL`** exactly. Check case, and remove any `.git` ending.                                                           |

### Next Step

Set Up Your Project

### Related Articles

* Register a Repository
* Block Merges With a Required Status Check
* Pull-Request Review Overview
