# Deploy a package from a Salesforce Org

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### <mark style="color:blue;">1,000,000 customers have moved to SF CLI. Are you ready?</mark>

[Why does Salesforce recommend moving from SFDX to SFCLI?](https://app.gitbook.com/o/vIHQCTOOUDcNoPic3AQi/s/9vAxMuDrkUkB4OXlH9CL/product-guides/arm/troubleshoot/salesforce-known-limitations#why-does-salesforce-recommend-moving-from-sfdx-to-sfcli) Click [here](../../../troubleshoot/known-issues-limitations/salesforce-known-limitations.md#why-does-salesforce-recommend-moving-from-sfdx-to-sfcli) for more info.

### Overview <a href="#overview" id="overview"></a>

Backup your Salesforce metadata to version control and trigger a deployment to a Salesforce org based on a '**Start Date**'. This job can be further customized to run functional test cases from the ARM TAF library or from version control.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account.
2.  From the top navigation pane, navigate to **Create New > New CI Job**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664540215589.png" alt="" width="563"><figcaption></figcaption></figure>
3.  Choose the tile: **Deploy from Salesforce Org**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664540869139.png" alt="" width="563"><figcaption></figcaption></figure>
4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections, we will cover each one of them separately.

#### Build <a href="#build" id="build"></a>

Under the **Build** section, fill in the below details:

1. Select the source [**Salesforce org**](../../../arm-administration/registration/salesforce-org/).
2. Select the **Package type** to retrieve and bundle the changes from a source sandbox.
   1. **Unpackaged Mode:** This fetches the metadata members in your org that have got modified from the last ARM cycle. On selection, specify a date in the Start Date field from which changes in Salesforce Org will fetch. If a date is not specified, then the project creation date will become the start date and changes will get fetched.
   2. **Unmanaged packages:** These provide developers with basic building blocks for an application as application templates. The user can edit the components after installing this package in a Salesforce Org.
   3. **Managed packages:** Salesforce partners use these packages to distribute and sell applications to their users. These packages get created from a **Developer Edition** organization.\
      For more information, refer to the link below:\
      [https://help.salesforce.com/HTViewHelpDoc?id=sharing\_apps.htm\&language=en\_US](https://help.salesforce.com/HTViewHelpDoc?id=sharing\_apps.htm\&language=en\_US)\


**Additional options in the Build section**\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658400880100.png" alt="" width="375"><figcaption></figcaption></figure>

1. **Auto switch to bulk retrieve service, if job is hitting metadata retrieving governor limit:** This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 39 MB. Using Batch Size, you can process metadata in batches to stay within platform limits. If you do not have a lot of metadata, processing records through batches are your best solution. Specify the batch size for both profile and remaining components to retrieve metadata types. 10 K is the max batch size that you can set per batch.
2. **Exclude Installed (Managed) components and changes:** This option will exclude any **Managed packages** that the user may have installed.
   * **Exclude all manually created components:** All manually added components in the installed (managed) package will also get excluded.
3. **Incremental Build:** Incremental builds are important for managing continuous builds for continuous delivery. Incremental Builds substantially decrease build times by avoiding the execution of previous metadata that is not needed. This will fetch all the metadata changes beyond the selected Baseline Revision till the successfully deployed revision to the destination org. On the next CI Job run, the previous Baseline Revision automatically gets changed to the successfully deployed revision. Hence, there will be a substantial increase in build time performance for large-project incremental builds when a change to a single file or a small number of files is performed.
4. **Include Picklist modifications:** Whenever a picklist value gets altered or deleted, SF will not update the picklist's last altered date. Whether the picklist value gets altered or not, it will pull all the picklist fields into the source org. This option is available only if the source is a Salesforce Org.
5. **Prepare Destructive Changes:** Pre-destructive changes option will allow the users to delete unwanted fields or metadata components from their destination Salesforce org before the deployments begin.
6. **Generate Code Coverage Report:** This option generates a code overage report. This has info about the apex tests run, the classes covered, and the assertions that have failed.
7. **Run Static Analysis Report:** This will identify potential software quality issues before code moves to production.

&#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665048328756.png" alt="" width="375"><figcaption></figcaption></figure>

1.  **For ApexPMD** and **Checkmarx**: ARM allows you to set the criteria for running the ApexPMD SCA tool. This means running for all the apex classes or stating the period from where it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053647906.png" alt="" width="563"><figcaption></figcaption></figure>
2.  **For CodeScan** and **SonarQube:** Set the criteria for running the [CodeScan](https://www.codescan.io/) or SonarQube tool, whether to run on the supported metadata types from the full source or to run on the newly added components. This means running for all the apex classes or stating the period from where it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.

    * **Run on all supported Metadata types:** Analysis is performed on all the metadata types that are supported. For example, if the build includes 2 classes and 2 triggers, then the analysis will run on all the supported components that are retrieved for these 2 classes and 2 Triggers in the build.
    *   **Run on Newly added supported Metadata types:** Analysis is performed only on those components which are received during build retrieval. For example, if there are added as well as modified components in the build, then the analysis runs on the newly added components, not on the modified components.\


        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797907228.png" alt=""><figcaption></figcaption></figure>
    * For more information on running **Static Code Analysis in CI Jobs**, refer [HERE](https://knowledgebase.autorabit.com/docs/static-code-analysis-in-ci-cd#5-running-sca-in-ci-job).

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797943167.png" alt=""><figcaption></figcaption></figure>
3. **Additional Profile Packaging Options:**
   1. **Remove login IP Ranges:** If you want to log in with a Salesforce org, you have an option to restrict IP ranges. Upon selection, login IP details will not be deployed to Salesforce Org.
   2. **Remove System and User Permissions:** System permissions control a user’s ability to perform tasks that apply to their VCS or Org. To not deploy this permission, select this option.
4. **Exclude Metadata Types:** These exclude the metadata no longer required for build/deployment. To avoid fetching unwanted metadata types during a CI job, ensure that you have excluded them. If the 'Exclude Metadata Types' checkbox is not checked, all metadata types will get chosen. That globally excluded metadata will be auto-populated if you select this option.Important Note:To set this option at a global level, go to the **'My Salesforce Settings'** section on the [**My Account**](../../../arm-administration/user-management/manage-users-account-settings/) page. Next, select the metadata types to exclude. This reflects in all CI jobs that get created henceforth and across other modules as well.

#### Deploy <a href="#deploy" id="deploy"></a>

This section is all about either deploying or validating the above package onto a different Salesforce Org.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053710641.png" alt="" width="375"><figcaption></figcaption></figure>

1. Select the **Deployment org**.
2.  Specify the **Apex test level** you would like to run for the CI job.\


    <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **Use Salesforce Defaults:** It keeps the default behavior for all tests. In the sandbox, no tests are executed. In production, all local tests are executed if it contains Apex classes or triggers. Local tests are all tests, except the ones that originate from managed packages. If the package doesn’t contain Apex components, no tests are run.
   1. **No Test Run:** No apex test is run unless it is a production deployment.
   2. **Run Specified Tests:** Only the tests that the user specifies are run. The benefit of choosing this option is that it checks code coverage criteria at the ARM level rather than checking it at the entire org level. The executed tests must cover the classes or triggers contained with a minimum of 75% code coverage. This coverage is computed for each class or trigger individually and is different from the overall coverage percentage.Important Note:Make sure for the runTests parameter, you're specifying the test class names separated by ",". The runTests parameter will be used only when the test level is set to Run Specified Tests.
   3. **Run Local Tests:** All tests in your organization are run, except the ones that originate from installed managed packages. This test level is the default for production deployments that include Apex classes or triggers.
   4. **Run All Tests in Org:** In this, all tests in the organization are run, including tests of managed packages.
   5. **Run Tests Based On Changes—**This option will identify apex test classes from your source package in addition to the default configured apex classes and run the identified tests to the destination environment. Also, if you would like to include the newly identified apex classes from the packages in your [default apex test class configuration](../../../troubleshoot/how-tos/default-apex-class-configuration.md) list, please check the **"Do you want us to update the test classes"** checkbox.Important Notes:
      1. Only CI Jobs have the **"Do you want us to update the test classes"** checkbox enabled. This feature is yet to be implemented in other modules yet.
      2. Please make sure to execute all apex tests before configuring this option. This allows you to configure the mapping between the main class and the test class.
      3. If you have cleared the last run history in your destination org, again you are required to execute run all tests. If not done, the dependent test execution will fail.&#x20;
      4. If you have refreshed your sandbox, then again you are required to execute run all tests. If not done, the dependent test execution will fail.
      5. If the test classes do not exist in the package, the test level is configured based on the Run local Tests.

**Additional Deployment Options**\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658402446213.png" alt="" width="375"><figcaption></figcaption></figure>

1. **Validate Only:** With ARM, you can set up validation-only CI jobs between your Salesforce Orgs or Version Control, so you can catch any problematic changes early and make sure that when the time comes to deploy, you’ll be able to release successfully. All success and error messages are displayed on the CI Job Result page.&#x20;
   * **Prevent Deployment:** With AR 20.1 release onward, ARM will make sure that you do not trigger a build deployment for the validation-only CI jobs. Therefore, the **Deploy** option will either be in disabled mode or in some cases, will not be seen to the user whenever trying to trigger a new build for the validation-only CI jobs.Important NoteBuild triggers do not execute **Test Cases** if the **Validate Only** check box is selected.
2. **Rollback:** Keep a copy of the changes before deployment and can revert the changes later.
3. **Ignore Missing Visibility Settings, If Package Contains Profiles Or PermissionSets:** With this option, differences in visibility settings between the source and destination orgs will not cause the deployment to fail. ARM will compare the source and destination orgs and keep only the profile/permission sets settings that are common between both orgs. **Please Note:**
   * **Deploying Standard Objects:** AutoRabit does not ignore Standard Objects like Cases during the deployment phase when layout assignments and RecordType permissions are provided in profiles. Ensure that the necessary layouts and record types are deployed to the target sandbox before handling Field-Level Security (FLS) permissions.
   * **Limitation with FLS Permissions:** Note that the "Ignore Missing Visibility" option in AutoRABIT cannot be used to ignore FLS permissions for Standard Objects. FLS permissions for Standard Objects cannot be ignored, and it is important to follow the recommended process of deploying layouts and record types first.&#x20;
4. **Ignore Installed (Managed) components:** This option will exclude any **Managed packages** that the user may have installed.
   * **Ignore all manually created components:** All manually added components in the installed (managed) package will also get excluded.
5. **Ignore warnings:** These allow the metadata members to get deployed even though errors/warnings are encountered during deployment.&#x20;
6. **Do not include 'Skip members' during Deployment:** This option will get displayed only if the user has configured certain metadata types for their Salesforce Org which gets skipped whenever deployment happens for the same Salesforce Org. The user can configure such metadata members in the [Salesforce Org Management](../../../getting-started/salesforce-org-management.md) page in our application.
7. **Run Destructive Changes:** Here you can specify whether to run pre or post-destructive changes while carrying out the deployment process.
8. **Apply Search and Substitute Rules:** If you have created the SEARCH and SUBSTITUTE rules to define custom find and substitute rules that ARM applies whenever you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control or vice-versa, such rule can be found here.&#x20;
9. **On successful Deployment**\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665054574032.png)

**Options available:**

1. **Run Skuid Pages:** As the name suggests, this option, on selection, will let you run another skuid page.
2. **Trigger another CI Job:** Trigger another build on successful deployment of the current build.
3. **Run Environment Provisioning Template:** Run Environment Provisioning templates that are stored in ARM to automate manual post-deployment tasks.
4. **Run DataLoader Process or Group:** Trigger the dataloader process once the build is successful.
5. **Run Merge Process:** This allows you to perform the merge operation upon successful deployment. To do so, you need to select the source and destination Version Control branch and other options that are necessary to perform Merge operation. (Do refer to the [Merge](../../version-control/ez-merge/) section to know more about the fields and their uses.)
6. **Trigger Jenkins Job:** Triggers Jenkins jobs on successful deployment.
7. **Configure Parallel Processor:** This is covered in a separate topic, do check out the link [ HERE ](../parallel-processor.md) .
8.  **Set Sequence For Post Activities- On Success:** This option creates a sequencing workflow that runs a particular action after the CI Job is successfully executed. For example, you can create a workflow to run a merge process or a dataloader job once your CI job is deployed. However, in order to create a workflow sequence, a minimum of two (2) activities need to be selected.\
    To have a better understanding of the post-activity sequence, let's take the below scenario: User **'XYZ'** would like to trigger one of the CI Job through ARM and parallelly would like to carry other post activities such as running an Environment Provisioning Template, dataloader job and triggering another CI Job as well. Therefore, **XYZ** user navigate to the **Deploy > On Successful Deployment** section and select the necessary post activities checkbox as shown below. The above-selected post-deployment activities will run in parallel with the initial CI job once it is successfully deployed.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053092797.png" alt="" width="375"><figcaption></figcaption></figure>
9.  However, **XYZ** would like to run the above activities in the following sequence:

    1. First, the DataLoader job
    2. Second, CI Job and
    3.  Environment Provisioning template at last.\
        Therefore, a workflow sequence is required to run the activities based on his requirement. This can be achieved using **Set Sequence For Post Activities- On Success** option. So, **XYZ** will select Dataloader as a first activity, so this will be the initial task that will get carried out. If the Dataloader operation is successfully performed, the next task will be to trigger another CI Job process. Therefore, **XYZ** will select the CI Job checkbox as the next activity. However, if the Dataloader task failed due to any reason, the post activities stop there itself and no further actions will be carried out.\
        Click to assign the sequence for the remaining activities. In the new auto-populated screen, select the CI Job option as the second activity. So, if the CI Job operation is successfully executed, the third and final task will be to run the Environment Provisioning template. Select the Environment Provisioning checkbox for the next activity. Using the above steps, the user can easily set the sequential order in which the post-deployment activities will get executed.\


        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053178364.png" alt="" width="563"><figcaption></figcaption></figure>

    **Important Note:**

    1. Both the CI Job and the Environment Provisioning post activities are allowed to run parallel once the Dataloader job is successfully completed. This can be achieved if both the CI Job and Environment Provisioning checkboxes are selected together as the next activity.
    2. However, if you select the CI Job checkbox and leave the Environment Provisioning checkbox blank, in such case:
       1. CI Job will get triggered only if the Dataloader Job is successfully executed,
       2. Environment Provisioning will run in parallel to the Dataloader Job.&#x20;

#### Dependency Analyzer <a href="#dependency-analyzer" id="dependency-analyzer"></a>

This section allows users to query dependency relationships between the metadata components in a Salesforce org to view and manage dependent metadata components so that your commits do not break any existing functionalities in your org. Dependency Analyzer offers a dependency check, which allows users to see what they are missing due to Salesforce specificity.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1683701620054.png)

To analyze failed components in case of a failed deployment, select the **Source Org for analysis** from the drop-down. Users can view the results of this analysis in the **Dependency Analyzer** tab of the **Deployment Report**, or download it in manifest (.json) or .xls format.

#### Tests <a href="#tests" id="tests"></a>

Before proceeding with the CI Job operation, you can run the functional test cases to evaluate the functionality of the code being deployed to the Destination environment. Select the manner in which you want to fetch the test cases.

There are different ways to fetch the test cases:

1. TAF Labels
2. [Version Control](../../version-control/)
3. AccelQ (if AccelQ plugin is installed in ARM)
4.  Provar (if Provar plugin is installed in ARM)\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046383131.png" alt=""><figcaption></figcaption></figure>
5. **TAF Labels:** The test labels that are present in the ARM TAF module get displayed. Select the test cases as per your requirement.
   1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
   2. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
   3.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046491598.png" alt="" width="375"><figcaption></figcaption></figure>
6. **Version Control:** The test cases committed to a branch in version control are displayed.
   1. Select the **Version Control Repository** type.
   2. Select the **Repository** and the **Branch**.&#x20;
   3. Select the way you would like to run your test cases, i.e., TAF, Selenium Maven, or Selenium Non-Maven.
      1. For the **Selenium Maven** test type, you need to enter the test case root path in the **Test Case Root Path** field. Also, specify the goals.
      2. For the **Selenium Non-Maven** test type, you need to choose the **Execution Type**, and enter the test case root path in the **Test Case Root Path** field.
   4. **Additional options:**
      1. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
      2.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046646306.png" alt="" width="563"><figcaption></figcaption></figure>
7.  **AccelQ:** Select the Fetch Test Cases as **'AccelQ'**.  Enter your **Project Name** and the **Test Job Name** and set the **parameter(s)** for your AccelQ test.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046710823.png" alt="" width="563"><figcaption></figcaption></figure>
8. **Provar:** Select Fetch Test Cases From as **'Provar'**.
   1. Select your **Version Control Repository** and the **Branch** and provide the **provar test cases path**.
   2. **Test Cases Root Path**: Enter the test case root path till the **.testproject** file
   3. **Test Cases Execution Path:** Enter the test cases execution path here. **Ex:** tests/sample and if not specified, all the test cases from the **'tests'** folder will get executed.
   4. **Additional options:**
      1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
      2. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. With the 19.3 release, the user will be able to proceed with the test even if the deployment gets failed.
      3.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046980511.png" alt="" width="563"><figcaption></figcaption></figure>

#### Callout URL <a href="#callout-url" id="callout-url"></a>

The Callout URL lets you call another service from the ARM application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly. ([LEARN MORE](../configure-callout-url.md))

#### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications to selected users email on the success or failure of a build.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665047406818.png" alt="" width="563"><figcaption></figcaption></figure>

#### Schedule  <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.&#x20;

#### Save <a href="#save" id="save"></a>

Finally, click **Save** to save the new CI job details.\
If you want to deploy compiled objects of **FlexCard** and **OmniScript** for Vlocity, you must verify 2 things:\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1681473879014.png" alt="" width="563"><figcaption></figcaption></figure>

* The destination org must be registered with **OAuth**. If it is registered with **Standard**, you must register it with OAuth first and then proceed with the deployment. If the org is registered with Standard, the deployment will fail and the following message will display in the log: **`To deploy compiled versions of OmniScript and FlexCards, Please re-register your destination org with OAuth and update the Local Compilation key in the My Account section`**.
* You must select the **Local Compilation** checkbox in the **My Account** section and enter the **Access Key**.
  * The following message will be displayed in the log if you do not select this option: **`Deployment will be performed without local compilation due to the absence of Access Key of Vlocity's Private NPM Repository`**.&#x20;
  * The following message will be displayed in the log if you select this option but enter the wrong key: **`Deployment is completed without local compilation due to the incorrect Access Key of Vlocity's Private NPM Repository`**.

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](../../../../../fundamentals/faq/ci-jobs.md).
