# Backup your project to Version Control

{% hint style="info" %}
The **CI JOBS** screen is easiest to read at **80 %** zoom in Chrome or Firefox.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

Use ARM to back up changes from your Salesforce org to your [version-control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) system. You can also map commits to specific Salesforce users.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to ARM.  
2. From the top navigation bar, select **`Create New > New CI Job`**.

   <figure><img src="../../../../../.gitbook/assets/image (1216).png" alt="Create New > New CI Job menu option"></figure>

3. Click the **Backup to Version Control** tile.

   <figure><img src="../../../../../.gitbook/assets/image (1217).png" alt="Backup to Version Control job tile"></figure>

4. Enter a descriptive **Job name**.  
5. Add a short **Description**.  
6. (Optional) Assign the job to a **Group** for easier filtering, or click **`+`** to create a new group.  
7. The configuration page is divided into several sections. The key sections are explained below.

#### Build <a href="#build" id="build"></a>

Under **Build**, provide:

1. **Source Salesforce org** – the org to back up.  
2. **Package type** – how ARM collects metadata:

   * **Unpackaged mode** – retrieves metadata changed since the last ARM cycle (or since **Start date**, if specified).  
   * **Unmanaged package** – retrieves components from an unmanaged package so you can edit them.  
   * **Managed package** – retrieves components from a managed package created in a partner dev org.

   <figure><img src="../../../../../.gitbook/assets/image (1218).png" alt="Package type selection list"></figure>

##### Additional build options

1. **Auto switch to bulk retrieve service if job hits metadata governor limit** – automatically switches to batch retrieval if the job exceeds Salesforce limits. Specify **Batch size** (up to 10 000 items).  
2. **Exclude installed (managed) components and changes** – skip all managed-package components.  
   * **Exclude all manually created components** – also skip custom components inside managed packages.  
3. **Incremental build** – fetch only the metadata changed since the last successful deployment, greatly reducing build time.  
4. **Include picklist modifications** – always include picklist fields, even if Salesforce did not update their “last modified” date. (Source = Salesforce org only.)  
5. **Generate code coverage report** – include Apex test coverage details.  
6. **Run static analysis report** – run an SCA tool before committing.

   * **Apex PMD / Checkmarx** – choose whether to scan all Apex classes or only those modified after a given date, and set a **Priority** threshold that causes the build to be marked unstable if not met.

     <figure><img src="../../../../../.gitbook/assets/image (1219).png" alt="Apex PMD and Checkmarx criteria configuration"></figure>

   * **CodeScan / SonarQube** – choose to scan all supported metadata types or only newly added ones, and set a **Priority** threshold.

     <figure><img src="../../../../../.gitbook/assets/image (1220).png" alt="CodeScan and SonarQube criteria configuration"></figure>

     * **Run on all supported metadata types** – scan every retrieved component.  
     * **Run on newly added supported metadata types** – scan only components added in the current retrieval.

       <figure><img src="../../../../../.gitbook/assets/image (1221).png" alt="Run-scope options for supported metadata types"></figure>

7. **Additional profile packaging options**  
   * **Remove login IP ranges** – omit IP range settings from profiles.  
   * **Remove system and user permissions** – omit profile permissions from deployment.  
8. **Exclude metadata types** – globally omit specific metadata types from all CI jobs.

{% hint style="info" %}
To set global exclusions in advance, open **My Account > My Salesforce Settings**, choose **Exclude metadata types**, and select the types to skip. These settings apply to all future CI jobs.
{% endhint %}

#### Backup to Version Control (auto-commit) <a href="#backup-to-version-control-auto-commit" id="backup-to-version-control-auto-commit"></a>

Enable **Auto commit** to push changes directly to your VCS:

1. Select the **Version control type** (Git, TFS, or SVN).  
2. Choose the **Repository**, **Branch**, and **Credential**.  
   * For an SFDX-structured repo, also select the **Package directory**. See [SFDX metadata format](../../../salesforce-dx-metadata-format.md).  
3. Optional settings:  
   * **Check out and commit with user’s credentials** – commit all changes as the selected user.  
   * **Check out with user credentials and commit with actual modified user credentials** – preserve original authors.  
   * **Configuration for recordTypes picklistValues** – choose *Replace*, *Replace all*, or *Append*. ([Learn more](../../../troubleshoot/how-tos/configure-record-types-picklist-values.md))

   <figure><img src="../../../../../.gitbook/assets/image (1222).png" alt="Auto-commit and credential options"></figure>

#### Notifications <a href="#notifications" id="notifications"></a>

Send success or failure emails to selected recipients.

<figure><img src="../../../../../.gitbook/assets/image (1223).png" alt="Notification recipient list"></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

Run the job automatically:

* **Daily** – run every day at the chosen time or interval.  
* **Weekly** – run on selected day(s) and time.  
* **No schedule** – save the job and run it manually when needed.

For credential-usage details across CI job types, see the [FAQ](../../../../../fundamentals/faq/arm-faqs/ci-jobs.md).

### What’s next? <a href="#what-next" id="what-next"></a>

After saving the job, ARM redirects you to the [CI job results](../ci-job-history.md) page, where you can start the first build.
