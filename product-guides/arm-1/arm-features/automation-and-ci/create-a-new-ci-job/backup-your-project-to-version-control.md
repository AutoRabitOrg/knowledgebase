# Backup your project to Version Control

{% hint style="info" %}
The **CI JOBS** screen is easiest to read at **80 %** zoom in Chrome or Firefox.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

Use ARM to back up changes from your Salesforce org to your [version-control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) system. You can also map commits to specific Salesforce users.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to ARM.
2.  From the top navigation bar, select **`Create New > New CI Job`**.

    <figure><img src="../../../../../.gitbook/assets/image (1216).png" alt="Create New > New CI Job menu option"><figcaption><p>Create New CI Job</p></figcaption></figure>
3.  Click the **Backup to Version Control** tile.

    <figure><img src="../../../../../.gitbook/assets/image (1217).png" alt="Backup to Version Control job tile"><figcaption><p>Backup to Version Control</p></figcaption></figure>
4. Enter a descriptive **Job name**.
5. Add a short **Description**.
6. (Optional) Assign the job to a **Group** for easier filtering, or click **`+`** to create a new group.
7. The configuration page is divided into several sections. The key sections are explained below.

#### Build <a href="#build" id="build"></a>

Under **Build**, provide:

1. **Source Salesforce org** – The org to back up.
2.  **Package type** – How ARM collects metadata:

    * **Unpackaged mode** – Retrieves metadata changed since the last ARM cycle (or since **Start date**, if specified).
    * **Unmanaged package** – Retrieves components from an unmanaged package so you can edit them.
    * **Managed package** – Retrieves components from a managed package created in a partner dev org.

    <figure><img src="../../../../../.gitbook/assets/image (1218).png" alt="Package type selection list"><figcaption><p>Build</p></figcaption></figure>

**Additional build options**

1. **Auto switch to bulk retrieve service if job hits metadata governor limit** – Automatically switches to batch retrieval if the job exceeds Salesforce limits. Specify **Batch size** (up to 10,000 items).
2. **Exclude installed (managed) components and changes** – Skip all managed-package components.
   * **Exclude all manually created components** – Also skip custom components inside managed packages.
3. **Incremental build** – Fetch only the metadata changed since the last successful deployment, greatly reducing build time.
4. **Include picklist modifications** – Always include picklist fields, even if Salesforce did not update their “last modified” date. (Source = Salesforce org only.)
5. **Generate code coverage report** – Include Apex test coverage details.
6. **Run static analysis report** – Run an SCA tool before committing.
   *   **Apex PMD / Checkmarx** – Choose whether to scan all Apex classes or only those modified after a given date, and set a **Priority** threshold that causes the build to be marked unstable if not met.

       <figure><img src="../../../../../.gitbook/assets/image (1219).png" alt="Apex PMD and Checkmarx criteria configuration"><figcaption><p>Apex PMD / Checkmarx</p></figcaption></figure>
   *   **CodeScan / SonarQube** – Choose to scan all supported metadata types or only newly added ones, and set a **Priority** threshold.

       <figure><img src="../../../../../.gitbook/assets/image (1220).png" alt="CodeScan and SonarQube criteria configuration"><figcaption><p>CodeScan / SonarQube</p></figcaption></figure>

       * **Run on all supported metadata types** – Scan every retrieved component.
       *   **Run on newly added supported metadata types** – Scan only components added in the current retrieval.

           <figure><img src="../../../../../.gitbook/assets/image (1221).png" alt="Run-scope options for supported metadata types"><figcaption><p>Components in Current Retrieval</p></figcaption></figure>
7. **Additional profile packaging options**
   * **Remove login IP ranges** – Omit IP range settings from profiles.
   * **Remove system and user permissions** – Omit profile permissions from deployment.
8. **Exclude metadata types** – Globally omit specific metadata types from all CI jobs.

{% hint style="info" %}
To set global exclusions in advance, open **My Account > My Salesforce Settings**, choose **Exclude metadata types**, and select the types to skip. These settings apply to all future CI jobs.
{% endhint %}

#### Backup to Version Control (auto-commit) <a href="#backup-to-version-control-auto-commit" id="backup-to-version-control-auto-commit"></a>

Enable **Auto commit** to push changes directly to your VCS:

1. Select the **Version control type** (Git, TFS, or SVN).
2. Choose the **Repository**, **Branch**, and **Credential**.
   * For an SFDX-structured repo, also select the **Package directory**. See [SFDX metadata format](../../../../arm/salesforce-dx-metadata-format.md).
3.  Optional settings:

    * **Check out and commit with user’s credentials** – Commit all changes as the selected user.
    * **Check out with user credentials and commit with actual modified user credentials** – Preserve original authors.
    * **Configuration for recordTypes picklistValues** – Choose _Replace_, _Replace all_, or _Append_. ([Learn more](../../../../arm/troubleshoot/how-tos/configure-record-types-picklist-values.md))

    <figure><img src="../../../../../.gitbook/assets/image (1222).png" alt="Auto-commit and credential options"><figcaption><p>Backup to Version Control (Auto Commit)</p></figcaption></figure>

#### Notifications <a href="#notifications" id="notifications"></a>

Send success or failure emails to selected recipients.

<figure><img src="../../../../../.gitbook/assets/image (1223).png" alt="Notification recipient list"><figcaption><p>Notifications</p></figcaption></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

Run the job automatically:

* **Daily** – Run every day at the chosen time or interval.
* **Weekly** – Run on selected day(s) and time.
* **No schedule** – Save the job and run it manually when needed.

For credential-usage details across CI job types, see the [FAQ](../../../../arm/troubleshoot/arm-faqs/ci-jobs.md).

### What’s next? <a href="#what-next" id="what-next"></a>

After saving the job, ARM redirects you to the [CI job results](../../../../arm/arm-features/automation-and-ci/ci-job-history.md) page, where you can start the first build.
