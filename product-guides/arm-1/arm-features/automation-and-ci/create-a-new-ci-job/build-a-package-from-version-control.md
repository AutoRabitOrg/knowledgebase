# Building a package from Version Control

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Convert and package your version control files to [Salesforce Metadata](https://www.autorabit.com/blog/how-salesforce-metadata-affects-compliance/) components based on a **Start Revision.** You can also configure an ALM project and sprint to include only revisions tied to a user story and its status.

## Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account.
2. From the top navigation pane, navigate to **Create New >** [**New CI Job**](../../../../arm/arm-features/automation-and-ci/ci-job-history.md).

<figure><img src="../../../../../.gitbook/assets/image (18) (1).png" alt=""><figcaption></figcaption></figure>

1. Choose the tile: **Package from** [**Version Control**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/).

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. Enter a descriptive **Job name**.
2. Add a brief **Description**.
3. (Optional) Choose a **Group** to organize the job, or click **`+`** to create one.
4. The configuration page is divided into sections explained below.

### Build <a href="#build" id="build"></a>

1. Select your [**Version Control**](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) **system** – ARM supports Git, SVN, and TFS.
2. Choose the **Repository** and **Branch**.
3.  Under **Build Using**, pick one option:

    * **Baseline Revision** – Enter a revision manually or click **Edit** (![edit icon](<../../../../../.gitbook/assets/image (90) (1).png>)) to select it from a list.

    <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Important Notes:

1. For the first CI job, you must choose a **Baseline Revision**.
2. **Get Latest HEAD** points to the last commit in the current branch.
{% endhint %}

* **Time Range** – Specify a period so ARM fetches only revisions in that window.

<figure><img src="../../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

#### Additional options in the Build section

1. **Status Check API** – Check the status of APIs running for the CI job.
2. [**Pull Request**](../../../../arm/arm-features/version-control/external-pull-request/) – Create a pull request for this job.
3. [**Merge Request**](../../../../arm/arm-features/version-control/ez-merge/merge-requests.md) – Create a merge request for this job.
4. **Map ALM Project** – Configure ALM (e.g., Jira) work item statuses to include in the build.

{% hint style="warning" %}
**Important note**: **Build Using – Baseline Revision/Time Range** and **Trigger Build on Commit** are unavailable when **Map ALM Project** is selected.
{% endhint %}

5. **Trigger Build on Commit** – Launch a build whenever changes are committed to the branch.
   * **Process commit revision via hook only** – Visible only for Git-type repos. When enabled, the build packages changes from the commit revision received via webhook up to the branch head, ensuring no commits are skipped.

{% hint style="warning" %}
<pre class="language-markup" data-overflow="wrap"><code class="lang-markup"><strong>Note: If you commit both _nCino record-based config_ and _Salesforce metadata_ files to the same branch, certain Git systems may trigger unnecessary builds. This happens when the **Build on commit** option is enabled and changes occur only in an irrelevant folder.
</strong><strong> 
</strong></code></pre>
{% endhint %}

6. **Incremental Build** – Fetch only metadata changed since the last successful deployment, dramatically reducing build time.

{% hint style="info" %}
**Important note**: Incremental Build also works when validating **Deployment Jobs**.
{% endhint %}

7. **Prepare Destructive Changes** – Delete unwanted metadata from the destination org before deployment.
8. **Run Static Analysis Report** – Identify code quality issues before production.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (3).png" alt=""><figcaption></figcaption></figure>

* **Apex PMD / Checkmarx** – Set criteria such as date range and **Priority**. If the priority threshold is not met, the build is marked unstable.

<figure><img src="../../../../../.gitbook/assets/image (7) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

* **CodeScan / SonarQube** – Choose to scan all metadata or only newly added components, then set a **Priority**.

<figure><img src="../../../../../.gitbook/assets/image (8) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

* **Run on all supported metadata types** – Scan every retrieved component.
* **Run on newly added supported metadata types** – Scan only newly added components.
*   **Run on all supported metadata types from the full source** – Scan the entire branch.

    <figure><img src="../../../../../.gitbook/assets/image (1225).png" alt="Scope options for supported metadata types"><figcaption><p>Scope options for supported metadata types</p></figcaption></figure>

For details on running **Static Code Analysis in CI jobs**, see [this guide](../../../../arm/arm-administration/static-code-analysis-in-ci-cd.md).

7. **Additional Profile Packaging Options**
   * **Remove Login IP Ranges** – Omit IP-range restrictions from profiles.
   * **Remove System and User Permissions** – Omit profile permissions from deployment.
8. **Exclude Metadata Types** – Skip metadata you don’t need in the build.

{% hint style="info" %}
{% code overflow="wrap" %}
```
**Important note**: To set exclusions globally, open **My Account > My Salesforce Settings**, choose **Exclude metadata types**, and select the types to skip.
```
{% endcode %}
{% endhint %}

### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications on build success or failure.

<figure><img src="../../../../../.gitbook/assets/image (2192).png" alt=""><figcaption></figcaption></figure>

### Schedule <a href="#schedule" id="schedule"></a>

* **Daily** – Run every day at the chosen time or interval.
* **Weekly** – Run on selected day(s) and time.
* **No schedule** – Save the job and trigger it manually.

For credential usage details across CI job types, see the [FAQs](../../../../arm/troubleshoot/arm-faqs/ci-jobs.md).

### What Next? <a href="#what-next" id="what-next"></a>

After saving the job, ARM redirects you to the [CI Job Results](../../../../arm/arm-features/automation-and-ci/ci-job-history.md) page, where you can trigger the first build.
