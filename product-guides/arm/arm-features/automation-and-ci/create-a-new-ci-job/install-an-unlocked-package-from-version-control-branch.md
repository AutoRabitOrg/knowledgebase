---
description: How to Install an Unlocked Package from a Version Control Branch
---

# Installing an Unlocked Package from VC Branch

{% hint style="info" %}
The **CI Jobs** screen is best viewed at **80%** zoom in Chrome/Firefox browsers.
{% endhint %}

## Installing an Unlocked Package from a Version Control Branch

### Overview

Leverage ARM CI intelligence to build using the SFDX project structure from a Version Control Branch and install the package in the destination org of your choice.

### About Unlocked Packages

Salesforce provides various package types (unmanaged, managed, and unlocked). Unlocked packages are ideal for internal business applications, supporting modular development. They are suitable unless the goal is AppExchange distribution. Use them to:

* Organize existing metadata
* Package or extend apps
* Package new metadata

Unlocked packages support tracking of metadata changes and simplify app upgrades. They can be installed in multiple orgs and even modified in production.

### How to Install an Unlocked Package from a Branch

1. Log in to your AutoRABIT account.
2. Navigate to **Create New > New CI Job**.
3. Select **Install an Unlocked Package from a Version Control Branch**.

#### Build

Retrieve the SFDX project JSON file from your version control branch.

1. Select **Version Control System** as **GIT**.
2. Choose the **Repository** and **Branch**.
3. Under **Build Using**, choose from:
   * **Baseline Revision:** Enter or select from a list.
   * **Time Range:** Define a time period to fetch revisions.
4. Select the **Source Folder** from the **Package Directory** dropdown (optional).

{% hint style="info" %}
If using an externally created SFDX repository, ensure the source folder is declared under **packageDirectories** in the `sfdx-project.json` file.
{% endhint %}

**Additional Options:**

* **Status Check API**: Monitor API statuses for the job.
* **Pull Request**/**Merge Request**: Initiate as needed.
* **Map ALM Project**: Integrate work items (e.g., Jira, Azure DevOps).
* **Trigger Build on Commit**: Auto-trigger builds on code commits.
* **Process Commit Revision via Hook Only**: Ensures no commits are skipped.
* **Incremental Build**: Optimizes build time by only packaging changes since the last successful build.

{% hint style="info" %}
**Note:** Incremental Build also supports Deployment Jobs validation.
{% endhint %}

#### Deploy

Deploy the package to a target Salesforce org or a new scratch org.

* **Deploy only the latest version**: Installs only the latest package version.
* **Run Apex Compile**: Compile all or managed Apex classes.
* **Security Type**: Set access level (admin/all users).
* **Upgrade Type**: Upgrade installed package if a new version exists.
* **Publish Wait**: Set wait time for version availability.
* **Installation Key**: Secure the package using a key.
* **Rollback**: Enable rollback on failure.
* **On Successful Deployment**: Configure post-deployment actions such as:
  * Run Skuid Pages
  * Trigger another CI Job
  * Run Environment Provisioning Template
  * Execute DataLoader Process or Group
  * Initiate Merge Process
  * Trigger Jenkins Job
  * Configure Parallel Processor
  * Set Sequence for Post Activities

{% hint style="info" %}
**Note:** Sequence setting allows chaining post-deployment actions based on success/failure of each.
{% endhint %}

#### Dependency Analyzer

Query and analyze metadata dependencies to prevent deployment issues. Results can be viewed in the **Deployment Report** or exported as JSON or XLS.

#### Tests

Run functional test cases pre-deployment. Fetch options include:

* **Version Control**: Select test framework (Selenium Maven/Non-Maven).
* **AccelQ**: Provide project/test job and parameters.
* **Provar**: Configure path to `.testproject` and execution path.

**Additional Options:**

* **Stop Deployment if Tests Fail to Compile**
* **Run Tests even if Deployment Fails**
* **Cross-Browser Testing**: Select preferred browsers

#### Callout URL

Configure external HTTP callouts from AutoRABIT. Ensure correct parameter setup. ([Learn more](../configure-callout-url.md))

#### Notifications

Send email alerts to selected recipients on build success/failure.

#### Schedule

Schedule job execution:

* **Daily**: Run every day at a set time.
* **Weekly**: Run on specific weekdays and times.
* **No Schedule**: Job must be manually triggered.
