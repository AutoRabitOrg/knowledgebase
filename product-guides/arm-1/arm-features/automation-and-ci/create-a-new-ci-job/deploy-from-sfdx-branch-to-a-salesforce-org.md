# Deploy from SFDX branch to a Salesforce Org

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Use ARM CI intelligence to extract and package from a [Version Control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) SFDX branch to deploy into a Salesforce Org. Additionally, you can configure the job to pick up revisions based on your ALM story status and/or run functional test cases on your Destination Org.

## Procedure <a href="#procedure" id="procedure"></a>

1. Login to your ARM account.
2. From the top navigation pane, navigate to **Create New > New CI Job**.

<figure><img src="../../../../../.gitbook/assets/image (29) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Choose the tile: **Deploy SFDX source from** [**Version Control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/)

<figure><img src="../../../../../.gitbook/assets/image (30) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections, we will cover each one of them separately.

### Build <a href="#build" id="build"></a>

Under the **Build** section, fill in the below details:

1. Select the **Version Control Systems** as **GIT**.
2. Select the **Repository** and the **Branch**.
3. Under the **'Build Using'** dropdown, there are two different options to choose from:

**Baseline Revision:** Enter the baseline revision number manually or click on the **Edit** (![](<../../../../../.gitbook/assets/image (32) (1) (1) (1) (1) (1) (1).png>)) icon to select the baseline revision from the revision list. A new pop-up window appears; from the list displayed, choose the required baseline revision number.

<figure><img src="../../../../../.gitbook/assets/image (31) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (33) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. For the first CI Job to run, you need to choose the **Baseline Revision** of your selected Version Control Repository.
2. **Get Latest HEAD** points out the last commit in the current checkout branch.
3. When you wish to perform Git Merge-operation from one branch to another, you are requested to select the correct development start revision (from source branch) since it will get all revisions from the source branch to destination branch based on the commit date and generate a new merged revision.
{% endhint %}

**Time Range:** This option allows you to create a CI job using a timeline. You need to specify the time period from where the revisions will get fetched. This improves the usability of our CI server and helps build a package based on time rather than commits.

<figure><img src="../../../../../.gitbook/assets/image (34) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Next, select the **Source Folder** under the **Package Directory** drop-down field for your SFDX Repo. However, this is optional and it will allow users to package the SFDX structure without the App folder being a necessity.

{% hint style="info" %}
**Important Note:** For the SFDX repository created outside and registered later with ARM, the source folder has to be declared in the **sfdx-project.json** file under the array named **packageDirectories**. This will allow you to pick the source folder that you have declared in the **sfdx-project.json** during the CI job operation. If you are in trouble finding the declared source folder yet, press the Refresh button to re-scan the Package Directories for the new source folder path.
{% endhint %}

#### Additional Build options <a href="#additional-build-options" id="additional-build-options"></a>

1. **Status Check API:** This allows you to check the statuses of the APIs being run for the CI job.
2. [**Pull Request**](../../../../arm/arm-features/version-control/external-pull-request/)**:** Creates a pull request for the current CI job if opted.
3. [**Merge Request**](../../../../arm/arm-features/version-control/ez-merge/merge-requests.md)**:** Creates a merge request for the current CI job if opted.
4. **Map ALM Project (Ex: Jira):** Configure work item type status in ALM type to include in the build (under the ALM section).

{% hint style="info" %}
**Important Note:** **Build Using- Baseline Revision/Time Range** and **Trigger Build on Commit** will not be available for the users if the 'Map ALM Project' option is chosen.
{% endhint %}

5. **Trigger Build on commit:** A new build is triggered when changes are committed to the mapped version control system.
   *   **Process commit revision via hook only:** This option is visible only for Version Control as GIT (Enterprise BITBUCKET, BITBUCKET, VSGIT, GITLAB, GITHUB) type. Upon selection, the build agent will read the commit revision number and generate a package from that revision number to the branch head.\
       **Let’s take the below scenario:**\
       Two developers (**Developer A** and **Developer B**) both working on the same code base.

       1. **Developer A** has committed some changes to its local repository at 10 AM this morning but did not push the changes to the remote repository.
       2. **Developer B** has also performed some changes in the code, but he pushed the changes into the remote repository by 10:05 AM this morning.\
          So, when ARM builds get triggered by webhook, **Developer B** changes will be packaged and deployed and the codes get updated with the latest revision. However, **Developer A** changes are ahead of **Developer B**, ARM will show no modifications for the build since the **Developer B** changes are in the **HEAD** position. To overcome this scenario, ARM has come with an option to **"Process commit revision via hook only"**. This will prepare the build from the revision of **Developer A** to the HEAD revision of the branch, therefore no commits are skipped through the ARM cycle.

       <figure><img src="../../../../../.gitbook/assets/image (35) (1) (1) (1) (1) (1) (1).png" alt="" width="553"><figcaption></figcaption></figure>
6. **Incremental Build:** Incremental builds are important for managing continuous builds for continuous delivery. Incremental Builds substantially decrease build times by avoiding the execution of previous metadata that is not needed. This will fetch all the metadata changes beyond the selected Baseline Revision till the successfully deployed revision to the destination org. On the next CI Job run, the previous Baseline Revision automatically gets changed to the successfully deployed revision. Hence, there will be a substantial increase in build time performance for large-project incremental builds when a change to a single file or a small number of files is performed.

{% hint style="info" %}
**Note:** Incremental Build also works to validate Deployment Jobs.
{% endhint %}

7. **Prepare Destructive Changes:** Pre-destructive changes option will allow the users to delete unwanted fields or metadata components from their destination Salesforce org before the deployments begin.
8. **Run Static Analysis Report:** This will identify potential software quality issues before code moves to production.

<figure><img src="../../../../../.gitbook/assets/image (36) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**For ApexPMD and Checkmarx:** ARM allows you to set the criteria for running the ApexPMD SCA tool. This means running for all the apex classes or stating the period from where it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.

<figure><img src="../../../../../.gitbook/assets/image (37) (1) (1) (1) (1) (1) (1).png" alt="" width="506"><figcaption></figcaption></figure>

**For CodeScan and SonarQube:** Set the criteria for running the CodeScan or SonarQube tool, whether to run on the supported metadata types from the full source or to run on the newly added components. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.

<figure><img src="../../../../../.gitbook/assets/image (38) (1) (1) (1) (1) (1) (1).png" alt="" width="345"><figcaption></figcaption></figure>

* **Run on all supported Metadata types:** Analysis is performed on all the metadata types that are supported. For example, if the build includes 2 classes and 2 triggers, then the analysis will run on all the supported components that are retrieved for these 2 classes and 2 Triggers in the build.
* **Run on Newly added supported Metadata types:** Analysis is performed only on those components which are received during build retrieval. For example, if there are added as well as modified components in the build, then the analysis runs on the newly added components, not on the modified components&#x20;
* **Run on all supported Metadata types from the Full source:** Analysis is performed on the entire branch, including all supported metadata types, regardless of any build changes.

<figure><img src="../../../../../.gitbook/assets/image (39) (1) (1) (1) (1) (1) (1).png" alt="" width="368"><figcaption></figcaption></figure>

For more information on running **Static Code Analysis in CI Jobs**, refer [HERE](../../../../arm/arm-administration/registration/static-code-analysis-in-ci-cd.md).

7. **Additional Profile Packaging Options:**
   1. **Remove login IP Ranges:** If you want to log in with a Salesforce org, you have an option to restrict IP ranges. Upon selection, login IP details will not be deployed to Salesforce Org.
   2. **Remove System and User Permissions:** System permissions control a user’s ability to perform tasks that apply to their VCS or Org. To not deploy this permission, select this option.
8. **Exclude Metadata Types:** These exclude the metadata no longer required for build/deployment. To avoid fetching unwanted metadata types during a CI job, ensure that you have excluded them. If the 'Exclude Metadata Types' checkbox is not checked, all metadata types will get chosen. That globally excluded metadata will be auto-populated if you select this option.

{% hint style="info" %}
**Note:** To set this option at a global level, go to the **'My Salesforce Settings'** section on the **My Account** page. Next, select the metadata types to exclude. This reflects in all CI jobs that get created henceforth and across other modules as well.
{% endhint %}

### Deploy <a href="#deploy" id="deploy"></a>

This section is about deploying or validating the above package onto a different Salesforce Org.\


<figure><img src="../../../../../.gitbook/assets/image (40) (1) (1) (1) (1) (1) (1).png" alt="" width="434"><figcaption></figcaption></figure>

1. Select the **Deployment org**.
2. Specify the **Apex test level** you would like to run for the CI job.

<figure><img src="../../../../../.gitbook/assets/image (42) (1) (1) (1) (1) (1) (1).png" alt="" width="407"><figcaption></figcaption></figure>

3. **Use Salesforce Defaults:** It keeps the default behavior for all tests. In the sandbox, no tests are executed. In production, all local tests are executed if it contains Apex classes or triggers. Local tests are all tests, except the ones that originate from managed packages. If the package doesn’t contain Apex components, no tests are run.
4. **No Test Run:** No apex test is run unless it is a production deployment.
5. **Run Specified Tests:** Only the tests that the user specify are run. The benefit of choosing this option is that it checks code coverage criteria at the ARM level rather than checking it at the entire org level. The executed tests must cover the classes or triggers contained with a minimum of 75% code coverage. This coverage is computed for each class or trigger individually and is different from the overall coverage percentage.

{% hint style="info" %}
**Note:** Make sure for the runTests parameter, you're specifying the test class names separated by ",". The runTests parameter will be used only when the test level is set to Run Specified Tests.
{% endhint %}

6. **Run Local Tests:** All tests in your organization are run, except the ones that originate from installed managed packages. This test level is the default for production deployments that include Apex classes or triggers.
7. **Run All Tests in Org:** In this, all tests in the organization are run, including tests of managed packages.
8. **Run Tests Based On Changes—**&#x54;his option will identify apex test classes from your source package in addition to the default configured apex classes and run the identified tests to the destination environment. Also, if you would like to include the newly identified apex classes from the packages in your [default apex test class configuration](../../../../arm/troubleshoot/how-tos/default-apex-class-configuration.md) list, please check the **"Do you want us to update the test classes"**&#x63;heckbox.

{% hint style="info" %}
**Important Notes:**

1. Only CI Jobs have the **"Do you want us to update the test classes"** checkbox enabled. This feature is yet to be implemented in other modules yet.
2. Please make sure to execute all apex tests before configuring this option. This allows you to configure the mapping between the main class and the test class.
3. If you have cleared the last run history in your destination org, again you are required to execute run all tests. If not done, the dependent test execution will fail.&#x20;
4. If you have refreshed your sandbox, then again you are required to execute run all tests. If not done, the dependent test execution will fail.
5. If the test classes do not exist in the package, the test level is configured based on the Run local Tests.
{% endhint %}

#### Additional Deploy options <a href="#additional-deploy-options" id="additional-deploy-options"></a>

<figure><img src="../../../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1) (1).png" alt="" width="378"><figcaption></figcaption></figure>

1. **Validate Only:** You can now set up validation-only CI jobs between your Salesforce Orgs or Version Control, so you can catch any problematic changes early and make sure that when the time comes to deploy, you’ll be able to release successfully. All success and error messages are displayed on the CI Job Result page.&#x20;
   * **Prevent Deployment:** With the ARM 20.1 release, ARM ensures that you do not trigger a build deployment for the validation-only CI jobs. Therefore, the **Deploy** option will either be in disabled mode or in some cases, will not be seen whenever you try to trigger a new build for the CI validate jobs.

{% hint style="info" %}
**Note:** Build triggers do not execute **Test Cases** if the **Validate Only** check box is selected.
{% endhint %}

2. **Rollback:** Keep a copy of the changes before deployment and can revert the changes later.
3. **Ignore Missing Visibility Settings, If Package Contains Profiles Or PermissionSets:** With this option, differences in visibility settings between the source and destination orgs will not cause the deployment to fail. ARM will compare the source and destination orgs and keep only the profile/permission sets settings that are common between both orgs.

{% hint style="info" %}
Note: **Standard fields** are not supported for **Ignore Missing Visible Settings**.
{% endhint %}

4. **Ignore Installed (Managed) components:** This option will exclude any **Managed packages** that the user may have installed.
   * **Ignore all manually created components:** All manually added components in the installed (managed) package will also get excluded.
5. **Ignore warnings:** These allow the metadata members to get deployed even though errors/warnings are encountered during deployment.
6. **Do not include 'Skip members' during Deployment:** This option will get displayed only if the user has configured certain metadata types for their Salesforce Org which gets skipped whenever deployment happens for the same Salesforce Org. The user can configure such metadata members in the [Salesforce Org Management](../../../../arm/registration/salesforce-org/salesforce-org-management.md) page in our application.
7. **Run Destructive Changes:** Here you can specify whether to run pre or post-destructive changes while carrying out the deployment process.
8. **Apply Search and Substitute Rules:** If you have created the SEARCH and SUBSTITUTE rules to define custom find and substitute rules that ARM applies whenever you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control or vice-versa, such rule can be found here.&#x20;
9.  **On successful Deployment**

    <figure><img src="../../../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    1. **Run Skuid Pages:** As the name suggests, this option, on selection, will let you run another skuid page.
    2. **Trigger another CI Job:** Trigger another build on successful deployment of the current build.
    3. **Run Environment Provisioning Template:** Run Environment Provisioning templates that are stored in ARM to automate manual post-deployment tasks.
    4. **Run DataLoader Process or Group:** Trigger the dataloader process once the build is successful.
    5.  **Run Merge Process:** This allows you to perform the merge operation upon successful deployment. To do so, you need to select the source and the destination Version Control branches, and other options that are necessary to perform the Merge operation. You can perform a merge from one source branch to multiple destination branches. (Do refer to the [Merge](../../../../arm/arm-features/version-control/ez-merge/) section to know more about the fields and their uses.)

        * **Add**: Click on the![](<../../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1).png>)icon to add up to **5** destination branches.
        * **Delete**: Click on the![](<../../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1).png>)icon to delete a destination branch row.\


        <figure><img src="../../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
    6. **Trigger Jenkins Job:** Triggers Jenkins jobs on successful deployment.
    7. **Configure Parallel Processor:** This is covered in a separate topic, do check out the link [ HERE](../../../../arm/arm-features/automation-and-ci/parallel-processor.md).
    8. **Set Sequence For Post Activities- On Success:** This option creates a sequencing workflow that runs a particular action after the CI Job is successfully executed. For example, you can create a workflow to run a merge process or a dataloader job once your CI job is deployed. However, in order to create a workflow sequence, a minimum of two (2) activities need to be selected.

    To have a better understanding of the post-activity sequence, let's take the below scenario: User **'XYZ'** would like to trigger one of the CI Job through ARM and parallelly would like to carry other post activities such as running an Environment Provisioning Template, dataloader job and triggering another CI Job as well. Therefore, **XYZ** user navigate to the **Deploy > On Successful Deployment** section and select the necessary post activities checkbox as shown below. The above-selected post-deployment activities will run in parallel with the initial CI job once it is successfully deployed.

    <figure><img src="../../../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1).png" alt="" width="431"><figcaption></figcaption></figure>

    However, **XYZ** would like to run the above activities in the following sequence:

    * First, the DataLoader job
    * Second, CI Job and
    * Environment Provisioning template at last.\
      Therefore, a workflow sequence is required to run the activities based on his requirement. This can be achieved using **Set Sequence For Post Activities- On Success** option. So, **XYZ** will select Dataloader as a first activity, so this will be the initial task that will get carried out. If the Dataloader operation is successfully performed, the next task will be to trigger another CI Job process. Therefore, **XYZ** will select the CI Job checkbox as the next activity. However, if the Dataloader task failed due to any reason, the post activities stop there itself and no further actions will be carried out.\
      Click to assign the sequence for the remaining activities. In the new auto-populated screen, select the CI Job option as the second activity. So, if the CI Job operation is successfully executed, the third and final task will be to run the Environment Provisioning template. Select the Environment Provisioning checkbox for the next activity. Using the above steps, the user can easily set the sequential order in which the post-deployment activities will get executed.

    <figure><img src="../../../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. Both the **CI Job** and the **Environment Provisioning** post activities are allowed to run parallel once the Dataloader job is successfully completed. This can be achieved if both the CI Job and Environment Provisioning checkboxes are selected together as the next activity.
2. However, if you select the CI Job checkbox and leave the Environment Provisioning checkbox blank, in such case:
   * CI Job will get triggered only if the Dataloader Job is successfully executed,
   * Environment Provisioning will run in parallel to the Dataloader Job.&#x20;
{% endhint %}

#### Dependency Analyzer <a href="#dependency-analyzer" id="dependency-analyzer"></a>

This section allows users to query dependency relationships between the metadata components in a Salesforce org to view and manage dependent metadata components so that your commits do not break any existing functionalities in your org. Dependency Analyzer offers a dependency check, which allows users to see what they are missing due to Salesforce specificity.

To analyze failed components in case of a failed deployment, select the **Source Org for analysis** from the drop-down. Users can view the results of this analysis in the **Dependency Analyzer** tab of the **Deployment Report**, or download it in manifest (.json) or .xls format.

#### Tests <a href="#tests" id="tests"></a>

Before proceeding with the CI Job operation, you can run the functional test cases to evaluate the functionality of the code being deployed to the Destination environment. Select the manner in which you want to fetch the test cases.

There are different ways to fetch the test cases:

* TAF Labels
* Version Control
* AccelQ (if AccelQ plugin is installed in ARM)
* Provar (if Provar plugin is installed in ARM)

<figure><img src="../../../../../.gitbook/assets/image (51) (1) (1) (1) (1) (1) (1).png" alt="" width="391"><figcaption></figcaption></figure>

1.  **TAF Labels:** The test labels that are present in the ARM TAF module get displayed. Select the test cases as per your requirement.

    * **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    * **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    * **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (52) (1) (1) (1) (1) (1).png" alt="" width="379"><figcaption></figcaption></figure>
2.  **Version Control:** The test cases committed to a branch in version control are displayed.

    * Select the **Version Control Repository** type.
    * Select the **Repository** and the **Branch**.&#x20;
    * Select the way you would like to run your test cases, i.e., TAF, Selenium Maven, or Selenium Non-Maven.
      1. For the **Selenium Maven** test type, you need to enter the test case root path in the **Test Case Root Path** field. Also, specify the goals.
      2. For the **Selenium Non-Maven** test type, you need to choose the **Execution Type**, and enter the test case root path in the **Test Case Root Path** field.

    **Additional options:**

    * **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    * **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (53) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **AccelQ:** Select the Fetch Test Cases as **'AccelQ'**.  Enter your **Project Name** and the **Test Job Name** and set the **parameter(s)** for your AccelQ test.

<figure><img src="../../../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1).png" alt="" width="467"><figcaption></figcaption></figure>

4.  **Provar:** Select Fetch Test Cases From as **'Provar'**.

    * Select your **Version Control Repository** and the **Branch** and provide the **provar test cases path**.
    * **Test Cases Root Path**: Enter the test case root path till the **.testproject** file
    * **Test Cases Execution Path:** Enter the test cases execution path here. **Ex:** tests/sample and if not specified, all the test cases from the **'tests'** folder will get executed.

    **Additional options:**

    1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    2. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. With the 19.3 release, the user will be able to proceed with the test even if the deployment gets failed.
    3. **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (55) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Callout URL <a href="#callout-url" id="callout-url"></a>

The Callout URL lets you call another service from the ARM application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly. ([LEARN MORE](../../../../arm/arm-features/automation-and-ci/configure-callout-url.md))

#### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications to selected users' emails on the success or failure of a build. However, if the number of CheckIn users is more than 50, then the notification is not sent.

<figure><img src="../../../../../.gitbook/assets/image (56) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Schedule  <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.&#x20;

#### Save <a href="#save" id="save"></a>

Finally, click **Save** to save the new CI job details.

If you want to deploy compiled objects of **FlexCard** and **OmniScript** for Vlocity, you must verify 2 things:

<figure><img src="../../../../../.gitbook/assets/image (57) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. The destination org must be registered with **OAuth**. If it is registered with **Standard**, you must register it with OAuth first and then proceed with the deployment. If the org is registered with Standard, the deployment will fail and the following message will display in the log: **`To deploy compiled versions of OmniScript and FlexCards, Please re-register your destination org with OAuth and update the Local Compilation key in the My Account section.`**
2. You must select the **Local Compilation** checkbox in the **My Account** section and enter the **Access Key**.
   * The following message will be displayed in the log if you do not select this option: **`Deployment will be performed without local compilation due to the absence of Access Key of Vlocity's Private NPM Repository.`**
   * The following message will be displayed in the log if you select this option but enter the wrong key: **`Deployment is completed without local compilation due to the incorrect Access Key of Vlocity's Private NPM Repository.`**

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](../../../../arm/troubleshoot/arm-faqs/ci-jobs/).

#### What Next? <a href="#what-next" id="what-next"></a>

Once you filled in all the details for your CI job, you will be redirected to the [CI Job Results](../../../../arm/arm-features/automation-and-ci/ci-job-history.md) page where you can trigger a build for your CI job.
