# Install an Unlocked Package from Version Control Branch

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

Use ARM CI intelligence to build using SFDX project structure in a Version Control Branch and install the same in the Destination Org of your choice.

### About Unlocked Packages  <a href="#about-unlocked-packages" id="about-unlocked-packages"></a>

Salesforce offers different types of packages (unmanaged, managed, and Unlocked). Unlocked packages are especially suited for internal business apps and allows you to do modular application development. The unlocked package is the right package type for most use cases unless you plan to distribute an app on AppExchange. You can use unlocked packages to organize your existing metadata, package an app, extend an app that you’ve purchased from AppExchange, or package new metadata.&#x20;

Unlocked packages help you add, edit, and remove metadata in your org in a trackable way. You can install an unlocked package to multiple orgs, and upgrade your Salesforce apps easier and faster. Metadata in unlocked packages can be modified in a production org.

### How to install an unlocked package from a branch? <a href="#how-to-install-an-unlocked-package-from-a-branch" id="how-to-install-an-unlocked-package-from-a-branch"></a>

1. Login to your AutoRABIT account.
2. From the top navigation pane, navigate to **Create New > New CI Job**.

<figure><img src="../../../../../.gitbook/assets/image (68) (1).png" alt=""><figcaption></figcaption></figure>

3. Choose the tile: **Install an Unlocked Package from a Version Control Branch**

<figure><img src="../../../../../.gitbook/assets/image (69).png" alt="" width="563"><figcaption></figcaption></figure>

4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections, we will cover each one of them separately.

#### Build <a href="#build" id="build"></a>

This section deals with retrieving the [SFDX](https://knowledgebase.autorabit.com/docs/deploy-from-sfdx-branch-to-a-salesforce-org) project JSON file from your version control branch.

1. Select the [**Version Control**](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) **Systems** as **GIT**.
2. Select the **Repository** and the **Branch**.
3. Under the **'Build Using'** dropdown, there are two different options to choose from:

**Baseline Revision:** Enter the baseline revision number manually or click on the **Edit** (![](<../../../../../.gitbook/assets/image (70).png>)) icon to select the baseline revision from the revision list. A new pop-up window appears; from the list displayed, choose the required baseline revision number.

<figure><img src="../../../../../.gitbook/assets/image (71).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (72).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. For the first CI Job to run, you need to choose the **Baseline Revision** of your selected Version Control Repository.
2. **Get Latest HEAD** points out the last commit in the current checkout branch.
3. When you wish to perform Git Merge-operation from one branch to another, you are requested to select the correct development start revision (from source branch) since it will get all revisions from the source branch to destination branch based on the commit date and generate a new merged revision.
{% endhint %}

**Time Range:** This option allows you to create a CI job using a timeline. You need to specify the time period from where the revisions will get fetched. This improves the usability of our CI server and helps build a package based on time rather than commits.

<figure><img src="../../../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

4. Next, select the **Source Folder** under the **Package Directory** drop-down field for your SFDX Repo. However, this is optional and it will allow users to package the SFDX structure without the App folder being a necessity.

{% hint style="info" %}
**Important Note:** For the SFDX repository created outside and registered later with AutoRABIT, the source folder has to be declared in the **sfdx-project.json** file under the array named **packageDirectories**. This will allow you to pick the source folder that you have declared in the **sfdx-project.json** during the CI job operation. If you are in trouble finding the declared source folder yet, press the Refresh button to re-scan the Package Directories for the new source folder path.
{% endhint %}

**Additional options in the 'Build' section**

<figure><img src="../../../../../.gitbook/assets/image (74).png" alt="" width="398"><figcaption></figcaption></figure>

1. **Status Check API:** This allows you to check the statuses of the APIs being run for the CI job.
2. [**Pull Request**](https://knowledgebase.autorabit.com/arm/docs/external-pull-request)**:** Creates a pull request for the current CI job if opted.
3. [**Merge Request**](https://knowledgebase.autorabit.com/arm/docs/merge-requests)**:** Creates a merge request for the current CI job if opted.
4.  **Map ALM Project (Ex: Jira):** Configure work item type status in ALM type to include in the build (under the ALM section).

    <figure><img src="../../../../../.gitbook/assets/image (75).png" alt="" width="563"><figcaption></figcaption></figure>

    * Select your **ALM type**. Currently, AutoRABIT supports ALM types such as JIRA, IBMRTC, Version One, CA Agile Central, and Azure DevOps.
    * Select the **ALM Label** and its related **Projects**.
    * The active sprint(s) for the above selected Project will be available in the **Sprint** drop-down. AutoRABIT has given provision to you to update multiple sprints related to tasks or bugs and update the status at ongoing when running the CI Job. You can select either one of Sprint or if you wish to update the status for all the sprints, leave as default i.e., keep **'All Active Sprints'** in the selected mode.
    * Select the **Work Item type**. Here you can select multiple work items that you like the update the status in your ALM. To use all the work item types, keep the 'All Work Item Type' option selected by default.

    <figure><img src="../../../../../.gitbook/assets/image (76).png" alt="" width="563"><figcaption></figcaption></figure>

    * Based on the above work Item selected, you need to update the status for each work item type. Important Note:**Build Using- Baseline Revision/Time Range** and **Trigger Build on Commit** will not be available for the users if the 'Map ALM Project' option is chosen.
5. **Trigger Build on commit:** A new build is triggered when changes are committed to the mapped version control system.
   *   **Process commit revision via hook only:** This option is visible only for Version Control as GIT (Enterprise BITBUCKET, BITBUCKET, VSGIT, GITLAB, GITHUB) type. Upon selection, the build agent will read the commit revision number and generate a package from that revision number to the branch head.\
       Let’s take the below scenario:\
       Two developers (Developer A and Developer B ) both working on the same code base.

       1. **Developer A** has committed some changes to its local repository at 10 AM this morning but did not push the changes to the remote repository.
       2. **Developer B** has also performed some changes in the code, but he pushed the changes into the remote repository by 10:05 AM this morning.\
          So, when AutoRABIT builds get triggered by webhook, **Developer B** changes will be packaged and deployed and the codes get updated with the latest revision. However, **Developer A** changes are ahead of **Developer B**, AutoRABIT will show no modifications for the build since the **Developer B** changes are in the **HEAD** position. To overcome this scenario, AutoRABIT has come with an option to **"Process commit revision via hook only"**. This will prepare the build from the revision of **Developer A** to the HEAD revision of the branch, therefore no commits are skipped through the AutoRABIT cycle.

       <figure><img src="../../../../../.gitbook/assets/image (77).png" alt="" width="553"><figcaption></figcaption></figure>
6. **Incremental Build:** Incremental builds are important for managing continuous builds for continuous delivery. Incremental Builds substantially decrease build times by avoiding the execution of previous metadata that is not needed. This will fetch all the metadata changes beyond the selected Baseline Revision till the successfully deployed revision to the destination org. On the next CI Job run, the previous Baseline Revision automatically gets changed to the successfully deployed revision. Hence, there will be a substantial increase in build time performance for large-project incremental builds when a change to a single file or a small number of files is performed.

{% hint style="info" %}
**Important Note:** Incremental Build also works to validate **Deployment Jobs**.
{% endhint %}

#### Deploy <a href="#deploy" id="deploy"></a>

This section is all about deploying the above package onto a target Salesforce Org or you can create a new scratch org and install the unlocked packages to it.

<figure><img src="../../../../../.gitbook/assets/image (78).png" alt="" width="555"><figcaption></figcaption></figure>

**1. Deploy only the latest version of each package**

Select this checkbox to install only the latest version of each package.

<figure><img src="../../../../../.gitbook/assets/image (79).png" alt="" width="485"><figcaption></figcaption></figure>

**2. Run Apex Compile**

Select this checkbox to compile the Apex classes in your organization. Based on your choice, you can either compile all the Apex classes in your organization or only those available in your managed packages.

**3. Security Type**

Enables you to choose the user (admin or for all users) to have full access to your organization.

**4. Upgrade Type**

You can upgrade the installed package if there is a newer version of the package available. You can publish an upgrade for an installed package and notify installers that the new version is available.

**5. Publish Wait**

Publish Wait defines the maximum number of minutes can AutoRABIT waits for the package version to be available in the target org. The default is 0. If the package is not available in the target org in this time frame, the install is terminated.

**6. Installation Key**

To ensure the security of the metadata in your package, you must specify an installation key when creating a package version. The key ensures that no package information, such as the name or components, is disclosed until the correct installation key is supplied.

**7. Rollback**

Keep a copy of the changes before deployment and can revert the changes later.&#x20;

**8. On Successful Deployment**

List of actions to perform once the build is successfully deployed.

<figure><img src="../../../../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

1. **Run Skuid Pages:** As the name suggests, this option, on selection, will let you run another skuid page.
2. **Trigger another CI Job:** Trigger another build on successful deployment of the current build.
3. **Run Environment Provisioning Template:** Run Environment Provisioning templates that are stored in AutoRABIT to automate manual post-deployment tasks.
4. **Run DataLoader Process or Group:** Trigger the [ dataloader ](https://www.autorabit.com/blog/9-ways-a-salesforce-data-loader-assists-compliance/) process once the build is successful.
5. **Run Merge Process:** This allows you to perform the merge operation upon successful deployment. To do so, you need to select the source and destination Version Control branch and other options that are necessary to perform Merge operation. (Do refer to the [Merge](https://knowledgebase.autorabit.com/arm/docs/ez-merge) section to know more about the fields and their uses.)
6. **Trigger Jenkins Job:** Triggers Jenkins jobs on successful deployment.
7. **Configure Parallel Processor:** This is covered in a separate topic, do check out the link  [ HERE ](https://knowledgebase.autorabit.com/arm/docs/parallel-processor) .
8. **Set Sequence For Post Activities- On Success:** This option creates a sequencing workflow that runs a particular action after the CI Job is successfully executed. For example, you can create a workflow to run a merge process or a dataloader job once your CI job is deployed. However, in order to create a workflow sequence, a minimum of two (2) activities need to be selected.\
   \
   To have a better understanding of the post-activity sequence, let's take the below scenario: User **'XYZ'** would like to trigger one of the CI Job through AutoRABIT and parallelly would like to carry other post activities such as running an Environment Provisioning Template, dataloader job and triggering another CI Job as well. Therefore, the **XYZ** user navigates to the **Deploy > On Successful Deployment** section and selects the necessary post activities checkbox as shown below. The above-selected post-deployment activities will run in parallel with the initial CI job once it is successfully deployed.

<figure><img src="../../../../../.gitbook/assets/image (81).png" alt="" width="431"><figcaption></figcaption></figure>

However, **XYZ** would like to run the above activities in the following sequence:

1. First, the DataLoader job
2. Second, CI Job and
3. Environment Provisioning template at last.\
   Therefore, a workflow sequence is required to run the activities based on his requirement. This can be achieved using **Set Sequence For Post Activities- On Success** option. So, **XYZ** will select Dataloader as a first activity, so this will be the initial task that will get carried out. If the Dataloader operation is successfully performed, the next task will be to trigger another CI Job process. Therefore, **XYZ** will select the CI Job checkbox as the next activity. However, if the Dataloader task failed due to any reason, the post activities stop there itself and no further actions will be carried out.\
   Click to assign the sequence for the remaining activities. In the new auto-populated screen, select the CI Job option as the second activity. So, if the CI Job operation is successfully executed, the third and final task will be to run the Environment Provisioning template. Select the Environment Provisioning checkbox for the next activity. Using the above steps, the user can easily set the sequential order in which the post-deployment activities will get executed.

<figure><img src="../../../../../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. Both the **CI Job** and the **Environment Provisioning** post activities are allowed to run parallel once the Dataloader job is successfully completed. This can be achieved if both the CI Job and Environment Provisioning checkboxes are selected together as the next activity.
2. However, if you select the CI Job checkbox and leave the Environment Provisioning checkbox blank, in such case:
   * CI Job will get triggered only if the Dataloader Job is successfully executed,
   * Environment Provisioning will run in parallel to the Dataloader Job.&#x20;
{% endhint %}

#### Dependency Analyzer <a href="#dependency-analyzer" id="dependency-analyzer"></a>

This section allows users to query dependency relationships between the metadata components in a Salesforce org to view and manage dependent metadata components so that your commits do not break any existing functionalities in your org. Dependency Analyzer offers a dependency check, which allows users to see what they are missing due to Salesforce specificity.

<figure><img src="../../../../../.gitbook/assets/image (83).png" alt="" width="470"><figcaption></figcaption></figure>

To analyze failed components in case of a failed deployment, select the **Source Org for analysis** from the drop-down. Users can view the results of this analysis in the **Dependency Analyzer** tab of the **Deployment Report**, or download it in manifest (.json) or .xls format.

#### Tests <a href="#tests" id="tests"></a>

Before proceeding with the CI Job operation, you can run the functional test cases to evaluate the functionality of the code being deployed to the Destination environment. Select the manner in which you want to fetch the test cases.

There are different ways to fetch the test cases:

* TAF Labels
* Version Control
* AccelQ (if AccelQ plugin is installed in AutoRABIT)
* Provar (if Provar plugin is installed in AutoRABIT)

<figure><img src="../../../../../.gitbook/assets/image (84).png" alt="" width="391"><figcaption></figcaption></figure>

1.  **TAF Labels:** The test labels that are present in the AutoRABIT TAF module get displayed. Select the test cases as per your requirement.

    * **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    * **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    * **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (85).png" alt="" width="379"><figcaption></figcaption></figure>
2.  **Version Control:** The test cases committed to a branch in version control are displayed.

    * Select the  [ **Version Control Repository** ](https://knowledgebase.autorabit.com/docs/version-control-repository)  type.
    * Select the **Repository** and the **Branch**.&#x20;
    * Select the way you would like to run your test cases, i.e., TAF, Selenium Maven, or Selenium Non-Maven.
      1. For the **Selenium Maven** test type, you need to enter the test case root path in the **Test Case Root Path** field. Also, specify the goals.
      2. For the **Selenium Non-Maven** test type, you need to choose the **Execution Type**, and enter the test case root path in the **Test Case Root Path** field.

    **Additional options:**

    * **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    * **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (86).png" alt="" width="547"><figcaption></figcaption></figure>
3. **AccelQ:** Select the Fetch Test Cases as **'AccelQ'**.  Enter your **Project Name** and the **Test Job Name** and set the **parameter(s)** for your AccelQ test.

<figure><img src="../../../../../.gitbook/assets/image (87).png" alt="" width="467"><figcaption></figcaption></figure>

4.  **Provar:** Select Fetch Test Cases From as **'Provar'**.

    * Select your **Version Control Repository** and the **Branch** and provide the **provar test cases path**.
    * **Test Cases Root Path**: Enter the test case root path till the **.testproject** file
    * **Test Cases Execution Path:** Enter the test cases execution path here. **Ex:** tests/sample and if not specified, all the test cases from the **'tests'** folder will get executed.

    **Additional options:**

    1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    2. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. With the 19.3 release, the user will be able to proceed with the test even if the deployment gets failed.
    3. **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (88).png" alt="" width="542"><figcaption></figcaption></figure>

#### Callout URL <a href="#callout-url" id="callout-url"></a>

The Callout URL lets you call another service from the AutoRABIT application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly. ([LEARN MORE](https://knowledgebase.autorabit.com/arm/docs/configure-callout-url))

#### Notifications <a href="#notifications" id="notifications"></a>

Send email notifications to selected users email on the success or failure of a build.

<figure><img src="../../../../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

#### Schedule <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.&#x20;

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](https://knowledgebase.autorabit.com/docs/ci-faq#8-how-does-the-user-credentials-impact-different-types-of-ci-jobs).
