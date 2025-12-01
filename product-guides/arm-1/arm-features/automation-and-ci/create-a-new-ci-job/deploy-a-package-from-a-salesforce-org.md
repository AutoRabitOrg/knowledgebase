# Deploy a package from a Salesforce Org

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### Why Does Salesforce Recommend Moving From SFDX to SFCLI?

Click [here](../../../../arm/troubleshoot/known-issues-limitations/salesforce-known-limitations.md#why-does-salesforce-recommend-moving-from-sfdx-to-sfcli) for more info.

### Overview <a href="#overview" id="overview"></a>

Backup your Salesforce metadata to version control and trigger a deployment to a Salesforce org based on a **Start Date**. This job can be further customized to run functional test cases from version control.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account.
2. From the top navigation pane, navigate to **Create New > New CI Job**.

<figure><img src="../../../../../.gitbook/assets/image (2193).png" alt=""><figcaption></figcaption></figure>

1. Choose the tile: **Deploy From Salesforce Org**

<figure><img src="../../../../../.gitbook/assets/image (2194).png" alt=""><figcaption></figcaption></figure>

1. Enter a descriptive **Job Name**.
2. Add a brief **Description**.
3. (Optional) Choose a **Group** to organize the job, or click **`+`** to create a new group.
4. The configuration page is divided into sections explained below.

#### Build <a href="#build" id="build"></a>

Under **Build**, provide:

1. **Source Salesforce Org** – The org to retrieve metadata from.
2.  **Package Type** – How ARM gathers metadata:

    * **Unpackaged Mode:** Retrieves metadata modified since the last ARM cycle (or since **Start Date**, if set).
    * **Unmanaged Packages:** Provides editable building blocks installed as application templates.
    * **Managed Packages:** Used by partners to distribute applications created in a **Developer Edition** org.

    For more information, see the [Salesforce help article](https://help.salesforce.com/HTViewHelpDoc?id=sharing_apps.htm\&language=en_US).

**Additional Options in the Build Section**

<figure><img src="../../../../../.gitbook/assets/image (2195).png" alt=""><figcaption></figcaption></figure>

1. **Auto Switch to Bulk Retrieve Service if Job Hits Metadata Governor Limit:** Use batch retrieval when a job approaches the 10,000 file or 39MB limit. Specify **Batch Size** (up to 10,000).
2. **Exclude Installed (Managed) Components and Changes:** Skip all managed package components.
   * **Exclude All Manually Created Components:** Also skip custom components in managed packages.
3. **Incremental Build:** Fetch only metadata changed since the previous successful deployment, improving build time.
4. **Include Picklist Modifications:** Always include picklist fields, even if the “last modified” date is unchanged (source = Salesforce org only).
5. **Prepare Destructive Changes:** Delete unwanted metadata in the destination org before deployment.
6. **Generate Code Coverage Report:** Include Apex test coverage details.
7. **Run Static Analysis Report:** Identify code quality issues before production.

<figure><img src="../../../../../.gitbook/assets/image (2196).png" alt=""><figcaption></figcaption></figure>

* **Apex PMD / Checkmarx:** Set scan criteria and **Priority**. If the threshold is not met, the build is marked unstable.

<figure><img src="../../../../../.gitbook/assets/image (2197).png" alt=""><figcaption></figcaption></figure>

* **CodeScan / SonarQube:** Choose to scan all metadata or only newly added components, then set a **Priority**.
  * **Run on All Supported Metadata Types:** Scan every retrieved component.
  *   **Run on Newly Added Supported Metadata Types:** Scan only newly added components.

      <figure><img src="../../../../../.gitbook/assets/image (1241).png" alt="Scope options for supported metadata types"><figcaption><p>Scope Options for Supported Metadata Types</p></figcaption></figure>

_For more information on running **Static Code Analysis in CI Jobs**, see_ [_this guide_](../../../../arm/arm-administration/static-code-analysis-in-ci-cd.md)_._

1. **Additional Profile Packaging Options:**
   * **Remove Login IP Ranges:** Omit IP-range restrictions from profiles.
   * **Remove System and User Permissions:** Omit profile permissions from deployment.
   * **Exclude Metadata Types:** Skip metadata you don’t need in the build.

{% hint style="info" %}
**Important Note:** To set exclusions globally, open **My Account > My Salesforce Settings**, choose **Exclude metadata types**, and select the types to skip. These settings apply to all future CI jobs.
{% endhint %}

#### Deploy <a href="#deploy" id="deploy"></a>

Deploy or validate the package in a destination org:

<figure><img src="../../../../../.gitbook/assets/image (2198).png" alt=""><figcaption></figcaption></figure>

* **Deployment Org:** Select the destination org.
* **Apex Test Level:** Choose the test scope:

<figure><img src="../../../../../.gitbook/assets/image (2199).png" alt=""><figcaption></figcaption></figure>

1. **Use Salesforce Defaults** – Default Salesforce behavior.
2. **No Test Run** – No tests unless deploying to production.
3. **Run Specified Tests** – Run only named tests; ARM checks coverage per class (75 % minimum).
4. **Run Local Tests** – Run all tests except those from managed packages.
5. **Run All Tests in Org** – Run every test, including managed-package tests.
6. **Run Tests Based on Changes** – Identify and run relevant test classes; optionally update the default test-class list.

{% hint style="info" %}
**Important Notes:**

* Specify test class names comma-separated in **runTests** when **Run Specified Tests** is selected.
* Ensure tests have run at least once before using **Run Tests Based on Changes**.
{% endhint %}

**Additional Deployment Options**

<figure><img src="../../../../../.gitbook/assets/image (2200).png" alt=""><figcaption></figcaption></figure>

1. **Validate Only:** Run validation without deploying.
   * **Prevent Deployment:** Disable deployment for validation-only jobs.

{% hint style="info" %}
**Important Note:** Test cases do not run when **Validate Only** is selected.
{% endhint %}

2. **Rollback:** Save a backup to allow rollback.
3. **Ignore Missing Visibility Settings if Package Contains Profiles or Permission Sets:** Deploy profiles/permission sets even if visibility settings differ.
4. **Ignore Installed (Managed) Components:** Skip managed package components.
   * **Ignore All Manually Created Components:** Also skip custom managed package components.
5. **Ignore Warnings:** Deploy even if warnings occur.
6. **Do Not Include 'Skip Members' During Deployment:** Override global skip settings for this deployment.
7. **Run Destructive Changes:** Choose pre- or post-destructive changes.
8. **Apply Search and Substitute Rules:** Apply custom find/replace rules during deployment.
9. **On Successful Deployment:** Trigger post-deployment actions (Skuid pages, CI jobs, environment templates, DataLoader processes, merge processes, Jenkins jobs, parallel processors, or a sequence of activities).

<figure><img src="../../../../../.gitbook/assets/image (2201).png" alt=""><figcaption></figcaption></figure>

_You can sequence multiple post-deployment actions:_

<figure><img src="../../../../../.gitbook/assets/image (2202).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2203).png" alt=""><figcaption></figcaption></figure>

#### Dependency Analyzer <a href="#dependency-analyzer" id="dependency-analyzer"></a>

Analyze metadata dependencies to avoid breaking changes:

<figure><img src="../../../../../.gitbook/assets/image (2204).png" alt=""><figcaption></figcaption></figure>

#### Tests <a href="#tests" id="tests"></a>

Run functional tests before deployment:

<figure><img src="../../../../../.gitbook/assets/image (2205).png" alt="" width="375"><figcaption></figcaption></figure>

* **Version Control:** Choose repository, branch, and test type (TAF, Selenium Maven, Selenium Non-Maven).

<figure><img src="../../../../../.gitbook/assets/image (2206).png" alt=""><figcaption></figcaption></figure>

* **AccelQ:** Enter **Project Name**, **Test Job Name**, and parameters.

<figure><img src="../../../../../.gitbook/assets/image (2207).png" alt=""><figcaption></figcaption></figure>

* **Provar:** Provide repository, branch, test-case root path, and execution path.

<figure><img src="../../../../../.gitbook/assets/image (2208).png" alt=""><figcaption></figcaption></figure>

#### Callout URL <a href="#callout-url" id="callout-url"></a>

Configure HTTP callouts to external services. See the [Callout URL guide](../../../../arm/arm-features/automation-and-ci/configure-callout-url.md).

#### Notifications <a href="#notifications" id="notifications"></a>

Send success or failure emails to selected recipients.

<figure><img src="../../../../../.gitbook/assets/image (2209).png" alt=""><figcaption></figcaption></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

* **Daily** – Run every day at the chosen time or interval.
* **Weekly** – Run on selected day(s) and time.
* **No Schedule** – Save the job and trigger it manually.

#### Save

Click **Save** to store the CI job settings.

If you deploy compiled **FlexCard** and **OmniScript** objects, verify both:

<figure><img src="../../../../../.gitbook/assets/image (1256).png" alt="Vlocity compilation settings"><figcaption><p>Vlocity Compilation Settings</p></figcaption></figure>

1. The destination org is registered via **OAuth** (not Standard).
2. **Local Compilation** is enabled in **My Account** and the correct **Access Key** is entered.

For credential usage details across CI job types, see the [FAQs](../../../../arm/troubleshoot/arm-faqs/ci-jobs.md).
