# Build a Package from Salesforce

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

Create a package from a Salesforce org based on a **"Start Date"** and deploy or validate the same package onto a different [Salesforce org](../../../arm-administration/registration/salesforce-org/). Configure the job to run functional test cases from the ARM TAF library or from version control.

### Procedure <a href="#procedure" id="procedure"></a>

1. Login to your ARM account.
2.  From the top navigation pane, navigate to **Create New > New CI Job**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664540211757.png" alt="" width="563"><figcaption></figcaption></figure>
3.  Choose the tile: **Package from Salesforce**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664541040172.png" alt="" width="563"><figcaption></figcaption></figure>
4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections, we will cover each one of them separately.

#### Build <a href="#build" id="build"></a>

Under the **Build** section, fill in the below details:

1. Select the source [**Salesforce org**](../../../getting-started/salesforce-org-management.md).
2. Select the **Package type** to retrieve and bundle the changes from a source sandbox.
   1. **Unpackaged Mode:** This fetches the metadata members in your org that have got modified from the last ARM cycle. On selection, specify a date in the Start Date field from which changes in Salesforce Org will fetch. If a date is not specified, then the project creation date will become the start date and changes will get fetched.
   2. **Unmanaged packages:** These provide developers with basic building blocks for an application as application templates. The user can edit the components after installing this package in a [Salesforce Org](../../../troubleshoot/best-practices/metadata-comparison-between-two-salesforce-orgs.md).
   3.  **Managed packages:** Salesforce partners use these packages to distribute and sell applications to their users. These packages get created from a Developer Edition organization. For more information, refer to the link below:\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797603302.png" alt="" width="375"><figcaption></figcaption></figure>

**Additional Build options**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797657746.png" alt="" width="375"><figcaption></figcaption></figure>

1. **Auto switch to bulk retrieve service, if job is hitting metadata retrieving governor limit:** This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 39 MB. Using Batch Size, you can process metadata in batches to stay within platform limits. If you do not have a lot of metadata, processing records through batches are your best solution. Specify the batch size for both profile and remaining components to retrieve metadata types. 10 K is the max batch size that you can set per batch.
2. **Exclude Installed (Managed) components and changes:** This option will exclude any **Managed packages** that the user may have installed.
   * **Exclude all manually created components:** All manually added components in the installed (managed) package will also get excluded.
3. **Include Picklist modifications:** Whenever a picklist value gets altered or deleted, SF will not update the picklist's last altered date. Whether the picklist value gets altered or not, it will pull all the picklist fields into the source org. This option is available only if the source is a [Salesforce Org](deploy-a-package-from-a-salesforce-org.md).
4. **Generate Code Coverage Report:** This option generates a code overage report. This has info about the apex tests run, the classes covered, and the assertions that have failed.
5. **Run Static Analysis Report:** This will identify potential software quality issues before code moves to production.\

   1.  **For ApexPMD** and **Salesforce Scanner:** ARM allows you to set the criteria for running the ApexPMD SCA tool. This means running for all the apex classes or stating the period from where it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797779127.png" alt="" width="563"><figcaption></figcaption></figure>
   2.  **For** [**CodeScan**](https://www.codescan.io/) and **SonarQube:** Set the criteria for running the CodeScan or SonarQube tool, whether to run on the supported metadata types from the full source or to run on the newly added components. This means running for all the apex classes or stating the period from where it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797943167.png" alt="" width="375"><figcaption></figcaption></figure>

       * **Run on all supported Metadata types:** Analysis is performed on all the supported metadata types. For example, if the build includes 2 classes and 2 triggers, then the analysis will run on all the supported components that are retrieved for these 2 classes and 2 Triggers in the build.
       *   **Run on Newly added supported Metadata types:** Analysis is performed only on those components which are received during build retrieval. For example, if there are added as well as modified components in the build, then the analysis runs on the newly added components, not on the modified components.

           <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797907228.png" alt="" width="375"><figcaption></figcaption></figure>

       For more information on running **Static Code Analysis in CI Jobs**, refer [HERE](../../../arm-administration/registration/static-code-analysis-in-ci-cd.md).
6. **Additional Profile Packaging Options:**
   1. **Remove login IP Ranges:** If you want to log in with a Salesforce org, you have an option to restrict IP ranges. Upon selection, login IP details will not be deployed to Salesforce Org.
   2. **Remove System and User Permissions:** System permissions control a user’s ability to perform tasks that apply to their VCS or Org. To not deploy this permission, select this option.
7. **Exclude Metadata Types:** These exclude the metadata no longer required for build/deployment. To avoid fetching unwanted metadata types during a CI job, ensure that you have excluded them. If the **'Exclude Metadata Types'** checkbox is not checked, all metadata types will get chosen. That globally excluded metadata will be auto-populated if you select this option.

{% hint style="info" %}
**Important Note**: To set this option at a global level, go to the **'My Salesforce Settings'** section on the [**My Account**](../../../arm-administration/user-management/manage-users-account-settings/) page. Next, select the metadata types to exclude. This reflects in all CI jobs that get created henceforth and across other modules as well.
{% endhint %}

#### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications to selected users email on the success or failure of a build.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665047406818.png" alt="" width="563"><figcaption></figcaption></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.&#x20;

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](../../../../../fundamentals/faq/ci-jobs.md).

### What Next? <a href="#what-next" id="what-next"></a>

Once you filled in all the details for your CI job, you will be redirected to the [CI Job Results](../ci-job-history.md) page where you can trigger a build for your CI job.
