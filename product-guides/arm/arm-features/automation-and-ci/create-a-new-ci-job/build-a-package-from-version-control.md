# Build a package from Version Control

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Convert and package your version control files to [Salesforce Metadata](https://www.autorabit.com/blog/how-salesforce-metadata-affects-compliance/) components based on a **"Start Revision."** Additionally, configure an ALM Project and Sprint to only include revisions based on a user story and its status.

## Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account.
2. From the top navigation pane, navigate to **Create New >** [**New CI Job**](../ci-job-history.md).

<figure><img src="../../../../../.gitbook/assets/image (1229).png" alt=""><figcaption></figcaption></figure>

3. Choose the tile: **Package from** [**Version Control**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/)**.**

<figure><img src="../../../../../.gitbook/assets/image (1230).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and subsequent CI jobs to a group.
7. Here, the user interface is in different sections; we will cover each one of them separately.

### Build <a href="#build" id="build"></a>

1. The first step is to choose your [**Version Control**](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) **System**. Currently, ARM supports Version Control Systems like GIT, SVN, and TFS.
2. Select the **Repository** and the **Branch**.
3. Under the **'Build Using'** dropdown, there are two different options to choose from:
   1. **Baseline Revision:** Enter the baseline revision number manually or click on the **Edit** (![](<../../../../../.gitbook/assets/image (90) (1).png>)) icon to select the baseline revision. A new pop-up window appears. From the list displayed, choose the required baseline revision number.

<figure><img src="../../../../../.gitbook/assets/image (1231).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1233).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. For the first CI Job to run, you need to choose the **Baseline Revision** of your selected Version Control Repository.
2. **Get Latest HEAD** points out the last commit in the current checkout branch.
{% endhint %}

2. **Time Range:** This option allows you to create a CI job using a timeline. You need to specify the time period from when the revisions will get fetched. This improves the usability of our CI server and helps build a package based on time rather than commits.

<figure><img src="../../../../../.gitbook/assets/image (1234).png" alt=""><figcaption></figcaption></figure>

#### **Additional options in the 'Build' section**

1. **Status Check API:** This allows you to check the status of the APIs being run for the CI job.
2. [**Pull Request**](../../version-control/external-pull-request/)**:** Creates a pull request for the current CI job if opted.
3. [**Merge Request**](../../version-control/ez-merge/merge-requests.md)**:** Creates a merge request for the current CI job if opted.
4. **Map ALM Project:** (Ex: Jira) Configure work item type status in ALM type to include in the build (under the ALM section).&#x20;

{% hint style="warning" %}
**Important Note**: **Build Using - Baseline Revision/Time Range** and **Trigger Build on Commit** is not available if the '**Map ALM Project**' option is chosen.
{% endhint %}

5. **Trigger Build on Commit:** A new build is triggered when changes are committed to the mapped version control system.

* **Process commit revision via hook only**: This option is visible only for Version Control as GIT (Enterprise BITBUCKET, BITBUCKET, VSGIT, GITLAB, GITHUB) type. Upon selection, the build agent will read the commit revision number and generate a package from that revision number to the branch head.\
  \
  Let’s take the following scenario:\
  Two developers (**Developer A** and **Developer B**) are both working on the same code base.

1. **Developer A** committed some changes to its local repository at 10 am this morning but did not push the changes to the remote repository.
2. **Developer B** also performed some changes in the code, but he pushed the changes into the remote repository by 10:05 am this morning.\
   \
   So, when ARM builds get triggered by webhook, **Developer B's** changes will be packaged and deployed, and the code gets updated with the latest revision. However, **Developer A's** changes are ahead of **Developer B's**, so ARM will show no modifications for the build, since **Developer B's** changes are in the **HEAD** position. To overcome this scenario, ARM has an option to **"Process commit revision via hook only."** This will prepare the build from the revisions of **Developer A** to the HEAD revision of the branch, thereby ensuring no commits are skipped in the ARM cycle.

{% hint style="warning" %}
**Note**: If you’re committing both _nCino Record-Based Config_ files and _Salesforce Metadata_ files to the same branch—even though they’re in separate folders—AutoRABIT may encounter an issue with certain Git-based version control systems. Specifically, AutoRABIT is unable to determine which folder's content has changed, leading to unnecessary build triggers that won't pick any changes if changes are in an irrelevant folder when the 'Build on commit' option is enabled.&#x20;
{% endhint %}

6. **Incremental Build:** Incremental builds are important for managing continuous builds for [continuous delivery](https://www.autorabit.com/blog/what-you-need-to-know-about-salesforce-continuous-delivery/). Incremental builds substantially decrease build times by avoiding the execution of previous metadata that is not needed. This will fetch all the metadata changes beyond the selected Baseline Revision till the successfully deployed revision to the destination org. On the next CI Job run, the previous Baseline Revision automatically gets changed to the successfully deployed revision. Accordingly, there will be a substantial increase in build-time performance for large-project incremental builds compared to when changes to a single file or a small number of files are performed.

{% hint style="info" %}
**Important Note:** Incremental Build also works to validate **Deployment Jobs**.
{% endhint %}

7. **Prepare Destructive Changes:** The pre-destructive changes option allows users to delete unwanted fields or metadata components from their destination [Salesforce org](../../../getting-started/salesforce-org-management.md) before the deployments begin.
8.  **Run Static Analysis Report:** This will identify potential software quality issues before code moves to production.

    <figure><img src="../../../../../.gitbook/assets/image (1228).png" alt=""><figcaption></figcaption></figure>

    **For ApexPMD** and **Checkmarx:** ARM allows you to set the criteria for running the ApexPMD static code analysis (SCA) tool. This means running for all the apex classes or stating the period when it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps in reporting the code quality of the developer team.

    <figure><img src="../../../../../.gitbook/assets/image (1227).png" alt=""><figcaption></figcaption></figure>

    **For CodeScan** and **SonarQube:** Set the criteria for running the CodeScan or SonarQube tool, whether to run on the supported metadata types from the full source or to run on the newly added components. This means running for all the apex classes or stating the period when it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps in reporting the code quality of the developer team.

    <figure><img src="../../../../../.gitbook/assets/image (1226).png" alt=""><figcaption></figcaption></figure>

    * **Run on all supported Metadata types:** Analysis is performed on all the supported metadata types. For example, if the build includes 2 classes and 2 triggers, then the analysis will run on all the supported components that are retrieved for those 2 classes and 2 Triggers in the build.
    * **Run on Newly added supported Metadata types:** Analysis is performed only on those components received during build retrieval. For example, if there are added as well as modified components in the build, then the analysis runs on the newly added components, not on the modified components.
    * **Run on all supported Metadata types from the Full source:** Analysis is performed on the entire branch, including all supported metadata types, regardless of any build changes.

    <figure><img src="../../../../../.gitbook/assets/image (1225).png" alt=""><figcaption></figcaption></figure>

    For more information on running **Static Code Analysis in CI Jobs**, refer [HERE](../../../arm-administration/registration/static-code-analysis-in-ci-cd.md).
9. **Additional Profile Packaging Options:**
   * **Remove Login IP Ranges:** If you want to log in with a [Salesforce org](../../../arm-administration/registration/salesforce-org/), you have an option to restrict IP ranges. Upon selection, login IP details will not be deployed to Salesforce Org.
   * **Remove System and User Permissions:** System permissions control a user’s ability to perform tasks that apply to their VCS or Org. To not deploy this permission, select this option.
10. **Exclude Metadata Types:** These exclude the metadata no longer required for build/deployment. To avoid fetching unwanted metadata types during a CI job, ensure that you have excluded them. If the 'Exclude Metadata Types' checkbox is not checked, all metadata types will be chosen. That globally excluded metadata will be auto populated if you select this option.

{% hint style="info" %}
**Important Note:** To set this option at a global level, go to the **'My Salesforce Settings'** section on the [**My Account**](../../../arm-administration/user-management/manage-users-account-settings.md) page. Next, select the metadata types to exclude. This is reflected in all CI jobs created from this point forward and across other modules as well.
{% endhint %}

### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications to selected users on the success or failure of a build.

<figure><img src="../../../../../.gitbook/assets/image (1224).png" alt=""><figcaption></figcaption></figure>

### Schedule <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](../../../../../fundamentals/faq/arm-faqs/ci-jobs.md).

### What Next? <a href="#what-next" id="what-next"></a>

Once you fill in all the details for your CI job, you will be redirected to the [CI Job Results](../ci-job-history.md) page, where you can trigger a build for your CI job.
