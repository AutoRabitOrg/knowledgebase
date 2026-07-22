# S3 IAM Policy Permissions

<h2 align="center">Modifying an Existing IAM Policy to Add S3 Bucket Versioning Permissions</h2>

<p align="center">s3:GetBucketVersioning  |  s3:PutBucketVersioning  |  s3:ListBucketVersions</p>

## 1. Overview

This guide shows how to modify an existing IAM policy in the AWS Management Console by adding the following Amazon S3 permissions to it:

1. s3:GetBucketVersioning  — read the versioning state of a bucket
2. s3:PutBucketVersioning  — enable or suspend versioning on a bucket
3. s3:ListBucketVersions  — list object versions in a bucket

{% hint style="info" %}
Note: The screenshots in this document are illustrative recreations of the AWS console. Names such as my-s3-access-policy and my-example-bucket are placeholders — replace them with your actual policy and bucket names.
{% endhint %}

## 2. Step-by-Step Instructions

### Step 1 — Sign in and open the IAM service

Sign in to the AWS Management Console and open the IAM service (search for “IAM” in the Services search bar).

### Step 2 — Go to Access management → Policies

In the left navigation pane, expand Access management and choose Policies.

<figure><img src="../../../../.gitbook/assets/image (2577).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>IAM left navigation — Access management → Policies (illustrative)</em></p>

### Step 3 — Search for and select the policy

In the search box, type the policy name and select it from the results list by clicking the policy name.

<figure><img src="../../../../.gitbook/assets/image (2578).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Policies list — search for the policy and click its name (illustrative)</em></p>

### Step 4 — Open the Permissions tab and click Edit

On the policy detail page, make sure the Permissions tab is selected, then click Edit.

<figure><img src="../../../../.gitbook/assets/image (2580).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Policy detail page — Permissions tab → Edit (illustrative)</em></p>

### Step 5 — Switch to the JSON tab

In the policy editor, switch from Visual to JSON using the toggle at the top of the editor. The editor shows the policy's current JSON.

### Step 6 — Add the S3 versioning permissions to the existing policy

Do not create a new policy — edit the JSON that is already in the editor. Locate the existing S3 statement and add the following three actions inside its "Action" array (remember to keep the commas between entries valid):

<table data-header-hidden><thead><tr><th valign="top"></th></tr></thead><tbody><tr><td valign="top"><p>"s3:GetBucketVersioning",</p><p>"s3:PutBucketVersioning",</p><p>"s3:ListBucketVersions"</p></td></tr></tbody></table>

The example below shows an existing policy after the change — the highlighted lines are the only ones added; everything else stays exactly as it was:

<figure><img src="../../../../.gitbook/assets/image (2581).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>JSON editor — the three actions added into the existing Action array (illustrative)</em></p>

These three are bucket-level actions, so make sure the statement's Resource includes the bucket ARN itself (arn:aws:s3:::my-example-bucket) — not only the /\* object ARN.

Choose Next, review the summary, and click Save changes. IAM saves the update as a new default version of the same policy, and it takes effect immediately for every user, group, and role the policy is attached to.

<figure><img src="../../../../.gitbook/assets/image (2582).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Review and save — the change becomes the default policy version (illustrative)</em></p>

