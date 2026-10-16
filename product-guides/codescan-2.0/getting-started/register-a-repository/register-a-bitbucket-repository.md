---
description: >-
  Create a Bitbucket token, add the repository to CodeScan, and turn on
  automatic pull-request scans with a webhook.
---

# Register a Bitbucket Repository

{% hint style="danger" %}
**\[TO CONFIRM before publishing]** These steps are for Bitbucket Cloud. Confirm whether Bitbucket Data Center is supported.
{% endhint %}

This article takes you through registering a Bitbucket repository in three parts:

1. Create a Bitbucket access token.
2. Add the project in CodeScan.
3. Turn on automatic pull-request scans with a webhook (optional, recommended).

### Before You Start

You need:

* The <mark style="background-color:yellow;">**Tenant manager**</mark> or <mark style="background-color:yellow;">**ACA admin**</mark> role in CodeScan. See Users, Roles and Permissions.
* **Admin access** to the repository in Bitbucket. Only repository administrators can create webhooks.
* The repository's web address, for example `https://bitbucket.org/your-workspace/your-repo`.
*   Webhook payload URL:

    ```
    https://<your-codescan-url>/api/sca/webhooks/bitbucket/<tenant-id>
    ```

### Part 1: Create a Bitbucket Access Token

CodeScan uses the token to read the repository, report the quality gate result, and post review comments. Use a **repository access token**: it is tied to the repository rather than to a person, so access doesn't stop when someone leaves.

1. At bitbucket.org, open the repository.
2. Next to the repository name in the left sidebar, select **`…`** (**`More actions`**), then **`Settings`**.
3. Under **`Security`**, select **`Access tokens`**, then **`Create access token`**.
4. Give the token a name, such as _CodeScan_.
5. Under **`Expiry`**, choose an expiry date. Your workspace administrator may require one.
6. Select the permissions:

| Permission          | Access | Needed for                       |
| ------------------- | ------ | -------------------------------- |
| **`Repositories`**  | Write  | Reading your code                |
| **`Pull requests`** | Write  | Review comments on pull requests |

7. Select **`Create`**, then copy the token. Bitbucket shows it only once.

For Bitbucket's own instructions, see [Create an access token for a repository](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/).

{% hint style="info" %}
**Note:** Bitbucket app passwords no longer work. If you have an existing CodeScan setup that uses one, replace it with an access token. Note the token's expiry date: when it expires, you'll need to replace it.
{% endhint %}

### Part 2: Add the Project in CodeScan

Add the project in CodeScan by following Adding the Project in CodeScan. The steps and settings are the same for every git host.

For Bitbucket:

* In **`Repository URL`**, enter the repository's web address, for example `https://bitbucket.org/your-workspace/your-repo`.
* In **`Access Token`**, paste the token from Part 1.
* When you're done, check that the new row shows **Bitbucket** under **`Provider`** and **`Authenticated`** under **`Status`**.

### Part 3: Turn On Automatic Pull-Request Scans

With a webhook, Bitbucket tells CodeScan whenever a pull request is opened or updated, and CodeScan scans it straight away. No pipeline is needed.

#### Step 1: Create a Webhook Key

The webhook key is a secret that you create yourself. You enter the same value in two places, CodeScan and Bitbucket, so CodeScan can check that each event really came from your repository.

{% hint style="info" %}
**Important Note:** Bitbucket can generate the secret for you with **`Generate secret`**, but it can't show the secret again after you save. Copy it into CodeScan's **`Webhook key`** field before you select **`Save`**.
{% endhint %}

If you didn't enter the key in Part 2, add it to the project now: in **`Repositories`**, select the project and choose **`Re-Authenticate`**, then paste the **`Access Token`** and the **`Webhook key`** together.&#x20;

#### Step 2: Find Your Tenant ID

1. In the CodeScan sidebar, select your organisation name at the bottom.
2. Note the **`Tenant ID`**.

<figure><img src="../../../../.gitbook/assets/image (3043).png" alt="" width="235"><figcaption></figcaption></figure>

#### Step 3: Build Your Webhook URL

Your webhook URL has this form:

```
https://<your-codescan-url>/api/sca/webhooks/bitbucket/<tenant-id>
```

Replace `<your-codescan-url>` with the address you use to open CodeScan, and `<tenant-id>` with your **`Tenant ID`** in **lowercase**.

{% hint style="warning" %}
**Important Note:** The tenant ID in the webhook URL must be lowercase, even though CodeScan shows it in capitals. For example, if your **`Tenant ID`** is `ABC123`, use `abc123` in the URL.
{% endhint %}

#### Step 4: Add the Webhook in Bitbucket

1. In Bitbucket, open the repository.
2. Next to the repository name in the left sidebar, select **`…`** (**`More actions`**), then **`Settings`**.
3. Under **`Workflow`**, select **`Webhooks`**, then **`Add webhook`**.
4. Fill in the **Add new webhook** form:

| Field                               | What to enter                                                                                                                          |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **`Title`**                         | A short description, for example _CodeScan_                                                                                            |
| **`URL`**                           | Your webhook URL from step 3, ending in `/bitbucket/<tenant-id>` in lowercase                                                          |
| **`Secret`**                        | Your webhook key: the same value you entered in CodeScan                                                                               |
| **`Active`**                        | Selected                                                                                                                               |
| **`Skip certificate verification`** | Cleared                                                                                                                                |
| **`Triggers`**                      | Select **`Choose from a full list of triggers`**, then select **Repository: `Push`** and **Pull request: `Created`** and **`Updated`** |

5. Select **`Save`**.

For Bitbucket's own instructions, see [Manage webhooks](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/).

#### Step 5: Test It

1. Open a pull request in the repository, or push a commit to an open one.
2. In CodeScan, a new scan appears with the context **Pull Request**.
3. If no scan appears, check the webhook's delivery history in Bitbucket. A rejected signature means the secret in Bitbucket does not match the **`Webhook key`** in CodeScan.

#### Optional: AI Review Comments

To have the AI write review comments on each pull request, turn on **`AI pull request review`** for the project. Comments count toward the quality gate. See AI Pull-Request Review.

### Next Step

Set Up Your Project

### Related Articles

* Register a Repository
* Pull-Request Review Overview
