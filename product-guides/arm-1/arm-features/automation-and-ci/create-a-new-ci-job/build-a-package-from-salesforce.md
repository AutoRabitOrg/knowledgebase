# Build a Package from Salesforce

{% hint style="info" %}
The **CI JOBS** screen is best viewed at **80%** zoom in Chrome or Firefox.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

Create a package from a Salesforce org based on a **Start date** and deploy or validate that package in a different [Salesforce org](../../../../arm/arm-administration/registration/salesforce-org/). You can also configure the job to run functional test cases stored in version control.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to ARM.
2.  From the top navigation bar, select **`Create New > New CI Job`**.

    <figure><img src="../../../../../.gitbook/assets/image (1208).png" alt="Create New > New CI Job menu option"><figcaption><p>Create New ➜ New CI Job menu option</p></figcaption></figure>
3.  Click the **Package from Salesforce** tile.

    <figure><img src="../../../../../.gitbook/assets/image (1209).png" alt="Package from Salesforce job tile"><figcaption><p>Package from Salesforce job tile</p></figcaption></figure>
4. Enter a descriptive **Job name**.
5. Add a brief **Description**.
6. (Optional) Choose a **Group** to organize the job, or click **`+`** to create a new group.
7. The configuration page has several sections explained below.

#### Build <a href="#build" id="build"></a>

Under **Build**, provide:

1. **Source Salesforce org** – The org to package.
2.  **Package type** – How ARM gathers metadata:

    * **Unpackaged mode** – Retrieves metadata changed since the last ARM cycle (or since **Start date**, if set).
    * **Unmanaged package** – Retrieves components from an unmanaged package so you can edit them.
    * **Managed package** – Retrieves components from a managed package created in a partner dev org.

    <figure><img src="../../../../../.gitbook/assets/image (1210).png" alt="Package type selection list"><figcaption><p>Select the package type for metadata retrieval</p></figcaption></figure>

**Additional build options**

<figure><img src="../../../../../.gitbook/assets/image (1211).png" alt="Additional build options panel"><figcaption><p>Additional build options</p></figcaption></figure>

1. **Auto switch to bulk retrieve service if job hits metadata governor limit** – Automatically uses batch retrieval when a job approaches Salesforce limits. Specify **Batch size** (up to 10 000 items).
2. **Exclude installed (managed) components and changes** – Skip all managed-package components.
   * **Exclude all manually created components** – Also skip custom components in managed packages.
3. **Include picklist modifications** – Always include picklist fields, even if Salesforce did not update the “last modified” date (source = Salesforce org only).
4. **Generate code coverage report** – Include Apex test-coverage details.
5.  **Run static analysis report** – Run an SCA tool before the build proceeds.

    *   **Apex PMD / Salesforce Scanner** – Choose whether to scan all Apex classes or only those modified after a given date, and set a **Priority** threshold.

        <figure><img src="../../../../../.gitbook/assets/image (1212).png" alt="Criteria configuration for Apex PMD and Salesforce Scanner"><figcaption><p>Criteria configuration for Apex PMD and Salesforce Scanner</p></figcaption></figure>
    *   **CodeScan / SonarQube** – Choose to scan all supported metadata types or only newly added ones, and set a **Priority** threshold.

        <figure><img src="../../../../../.gitbook/assets/image (1213).png" alt="Criteria configuration for CodeScan and SonarQube"><figcaption><p>Criteria configuration for CodeScan and SonarQube</p></figcaption></figure>

        * **Run on all supported metadata types** – Scan every retrieved component.
        *   **Run on newly added supported metadata types** – Scan only components added in the current retrieval.

            <figure><img src="../../../../../.gitbook/assets/image (1214).png" alt="Scope options for supported metadata types"><figcaption><p>Scope options for supported metadata types</p></figcaption></figure>

    For details on running **static code analysis in CI jobs**, see [this guide](../../../../arm/arm-administration/registration/static-code-analysis-in-ci-cd.md).
6. **Additional profile packaging options**
   * **Remove login IP ranges** – Omit IP-range settings from profiles.
   * **Remove system and user permissions** – Omit profile permissions from deployment.
7. **Exclude metadata types** – Globally omit specific metadata types from all CI jobs.

{% hint style="info" %}
To set global exclusions, open **My Account > My Salesforce Settings**, select **Exclude metadata types**, and choose the types to skip. These settings apply to all future CI jobs.
{% endhint %}

#### Notifications <a href="#notifications" id="notifications"></a>

Send success or failure emails to selected recipients.

<figure><img src="../../../../../.gitbook/assets/image (1215).png" alt="Notification recipient list"><figcaption><p>Select notification recipients for build status</p></figcaption></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

Run the job automatically:

* **Daily** – Run every day at the chosen time or interval.
* **Weekly** – Run on selected day(s) and time.
* **No schedule** – Save the job and run it manually when needed.

For credential-usage details across CI job types, see the [FAQ](../../../../../fundamentals/faq/arm-faqs/ci-jobs.md).

### What next? <a href="#what-next" id="what-next"></a>

After saving the job, ARM redirects you to the [CI job results](../../../../arm/arm-features/automation-and-ci/ci-job-history.md) page, where you can start the first build.

### What next? <a href="#what-next" id="what-next"></a>

After saving the job, ARM redirects you to the [CI job results](../../../../arm/arm-features/automation-and-ci/ci-job-history.md) page, where you can start the first build.
