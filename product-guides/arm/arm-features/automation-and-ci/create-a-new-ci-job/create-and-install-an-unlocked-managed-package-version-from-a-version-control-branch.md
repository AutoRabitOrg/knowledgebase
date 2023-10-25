# Create and Install an Unlocked/Managed Package Version from a Version Control Branch

### Overview

Use ARM CI intelligence to create a package version, build using the SFDX project structure in a Version Control branch, and install the same in the destination org of your choice.

### About Unlocked Packages&#x20;

Salesforce offers different packages (unmanaged, managed, and unlocked). Unlocked packages are especially suited for internal business apps and allow you to do modular application development. The unlocked package is the right package type for most use cases unless you plan to distribute an app on the AppExchange. You can use unlocked packages to organize your existing metadata, package an app, extend an app you’ve purchased from the AppExchange, or package new metadata.&#x20;

Unlocked packages help you add, edit, and remove metadata in your org in a trackable way. You can install an unlocked package to multiple orgs and upgrade your Salesforce apps more easily and faster. Metadata in unlocked packages can be modified in a production org.

### How to create and install an unlocked package version from a branch

1. Log in to your ARM account.
2.  From the top navigation pane, navigate to **Create New > New CI Job**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664540211757.png" alt=""><figcaption></figcaption></figure>
3.  Choose the tile: **Create and Install an Unlocked/Managed Package Version from a Version Control Branch**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678344915227.png" alt=""><figcaption></figcaption></figure>
4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. Choose the group from the dropdown to group your CI job for easier identification. You can create a new group using the **+** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections. We will cover each one of them separately.

Important Notes:

* The logs for package versions created through the CI Job module are not available under the respective package screen in the SFDX Module.
* The package version cannot be created simultaneously in SFDX and CI jobs. If a package version creation is in progress in either one, then it will fail in the other.

#### Build

This section pertains to creating a new package version for packages that are already created in or imported to ARM.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678441449536.png)

1. Select the **Version Control Type** as **GIT**.
2. Select the **Repository** and the **Branch**.
3. Under the **Build Using** dropdown, there are two different options to choose from:
   1.  **Baseline Revision:** Enter the baseline revision number manually or click on the **Edit** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619411284981.png)) icon to select the baseline revision from the revision list. A new pop-up window appears; choose the required baseline revision number from the list displayed.\
       Important Note:

       1. For the first CI Job to run, you must choose the **Baseline Revision** of your selected Version Control Repository.
       2. **Get Latest HEAD** indicates the last commit in the current checkout branch.
       3. To perform a Git Merge operation from one branch to another, you must select the correct development start revision (from the source branch) since it will get all revisions from the source branch to the destination branch based on the commit date and generate a new merged revision.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665055663919.png" alt="" width="563"><figcaption></figcaption></figure>
   2.  **Time Range:** This option allows you to create a CI job using a timeline. You must specify the period during which the revisions will be fetched. This improves the usability of our CI server and helps build a package based on time rather than commits.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678440682085.png" alt=""><figcaption></figcaption></figure>
4. Select the source folder under the **Package Directory** drop-down field for your SFDX Repo. However, this is optional and will allow users to package the SFDX structure without the App folder.Important Note:For the SFDX repository created outside and registered later with ARM, the source folder has to be declared in the **sfdx-project.json** file under the array named **packageDirectories**. This will allow you to pick the source folder you declared in the **sfdx-project.json** during the CI job operation. If you have trouble finding the declared source folder, press the **Refresh** button to re-scan the **Package Directories** for the new source folder path.
5. The **Package** drop-down is populated with successfully created packages in ARM with the selected combination of repo, branch, and package directory. Select the package for which you want to create a new version when the CI job is triggered.
6. **Choose Incremental Value:** Select the value you want to increment in the new version number.Important Note:All values following the one you choose to increment in the new version number will be **0**. For example, if the current version number is 2.1.9.0, and you choose to increment **Minor**, the new version number will be 2.2.0.0. Similarly, if the current version number is 1.9.2.6, and you choose to increment **Major**, the new version number will be 2.0.0.0.&#x20;
7. &#x20;**Trigger Build on commit:** A new build is triggered when changes are committed to the mapped version control system.
   1. **Process commit revision via hook only:** This option is visible only for Version Control as GIT (Enterprise BitBucket, VSGit, GitLab, GitHub) type. Upon selection, the build agent will read the commit revision number and generate a package from that revision number to the branch head.\
      Take the following scenario:\
      Two developers (Developer A and Developer B ) are working on the same code base.
      1. **Developer A** committed some changes to a local repository at 10 a.m. this morning but did not push the changes to the remote repository.
      2. **Developer B** made some code changes and pushed the changes to the remote repository by 10:05 a.m. this morning.\
         So, when ARM builds get triggered by webhook, **Developer B's** changes will be packaged and deployed, and the codes will be updated with the latest revision. However, **Developer A's** changes are ahead of **Developer B**, ARM will show no modifications for the build since the **Developer B** changes are in the **HEAD** position. To overcome this scenario, ARM has come up with an option to **Process commit revision via hook only**. This will prepare the build from the revision of **Developer A** to the HEAD revision of the branch, so no commits are skipped through the ARM cycle.

#### Deploy

This section is all about deploying the above package onto a target Salesforce Org, or you can create a new scratch org and install the unlocked packages to it.\
![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678441569077.png)

**1. Deploy only the latest version of each package**

This checkbox is selected by default because the latest version is created whenever the CI job is triggered, and the same is installed.

**2. Run Apex Compile**

Select this checkbox to compile the Apex classes in your organization. Based on your choice, you can either compile all the Apex classes in your organization or only those available in your managed packages.

**3. Security Type**

Enables you to choose the user (admin or all users) to have full access to your organization.

**4. Upgrade Type**

You can upgrade the installed package if there is a newer version of the package available. You can publish an upgrade for an installed package and notify installers that the new version is available.

**5. Publish Wait**

Publish Wait defines the maximum number of minutes ARM will wait for the package version to be available in the target org. The default is 0. If the package is not available in the target org in this time frame, the install is terminated.

**6. Installation Key**

To ensure the security of the metadata in your package, you must specify an installation key when creating a package version. The key ensures that no package information, such as the name or components, is disclosed until the correct installation key is supplied.

**7. Rollback**

After a successful rollback, the latest package version deployed to the target org does not roll back to the previous package version's state. Instead, the complete package version is deleted.&#x20;

**8. On Successful Deployment**

List of actions to perform once the build is successfully deployed.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665054681578.png)

1. **Run Skuid Pages:** This option will let you run another skuid page.
2. **Trigger another CI Job:** Trigger another build on successful deployment of the current build.
3. **Run Environment Provisioning Template:** Run Environment Provisioning templates stored in ARM to automate manual post-deployment tasks.
4. **Run Dataloader Process or Group:** Trigger the [dataloader](https://www.autorabit.com/blog/9-ways-a-salesforce-data-loader-assists-compliance/) process once the build is successful.
5. **Run Merge Process:** This allows you to perform the merge operation upon successful deployment. To do so, you need to select the source and destination Version Control branch and other options that are necessary to perform the Merge operation. (Refer to the [Merge](https://portal.document360.io/arm/docs/ez-merge) section to learn more about the fields and their uses.)
6. **Trigger Jenkins Job:** Triggers Jenkins jobs on successful deployment.
7. **Configure Parallel Processor:** This is covered in a separate topic; check out the link [HERE](https://portal.document360.io/arm/docs/parallel-processor).
8. **Set Sequence For Post Activities - On Success:** This option creates a sequencing workflow that runs a particular action after the CI Job is successfully executed. For example, you can create a workflow to run a merge process or a dataloader job once your CI job is deployed. However, in order to create a workflow sequence, a minimum of two (2) activities need to be selected.\
   \
   To have a better understanding of the post-activity sequence, take the following scenario: User **'XYZ'** would like to trigger one of the CI Jobs through ARM and parallelly would like to carry other post activities such as running an Environment Provisioning Template, dataloader job and triggering another CI Job as well. Therefore, the **XYZ** user navigates to the **Deploy > On Successful Deployment** section and selects the necessary post activities checkbox as shown below. The above-selected post-deployment activities will run in parallel with the initial CI job once it is successfully deployed.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053092797.png)
9. However, **XYZ** would like to run the above activities in the following sequence:
   1. First, the Dataloader job;
   2. Second, CI Job; and
   3.  Environment Provisioning template last.\
       Therefore, a workflow sequence is required to run the activities based on this requirement. This can be achieved using **Set Sequence For Post Activities - On Success** option. So, **XYZ** will select Dataloader as the first activity, so this will be the initial task that will be carried out. If the Dataloader operation is successfully performed, the next task will be to trigger another CI Job process. Therefore, **XYZ** will select the CI Job checkbox as the next activity. However, if the Dataloader task fails due to any reason, the post activities stop there and no further actions are carried out.\
       Click to assign the sequence for the remaining activities. In the new auto-populated screen, select the CI Job option as the second activity. So, if the CI Job operation is successfully executed, the third and final task will be to run the Environment Provisioning template. Select the Environment Provisioning checkbox for the next activity. Using the above steps, the user can easily set the sequential order in which the post-deployment activities will be executed.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665053178364.png" alt="" width="563"><figcaption></figcaption></figure>
   4. Important Note:
      1. Both the **CI Job** and the **Environment Provisioning** post activities are allowed to run in parallel once the Dataloader job is successfully completed. This can be achieved if both the CI Job and Environment Provisioning checkboxes are selected together as the next activity.
      2. However, if you select the CI Job checkbox and leave the Environment Provisioning checkbox blank, in such case:
         1. The CI Job will be triggered only if the Dataloader job is successfully executed,
         2. Environment Provisioning will run in parallel to the Dataloader job.&#x20;

#### Tests

Before proceeding with the CI Job operation, you may wish to run the functional test cases in order to test the functionality of the code being deployed to the Destination Environment. Therefore, select the manner in which you would like to fetch the test cases.

There are different ways to fetch the test cases:

1. TAF Labels
2. Version Control
3. AccelQ (if AccelQ plugin is installed in ARM)
4.  Provar (if Provar plugin is installed in ARM)\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046383131.png" alt="" width="375"><figcaption></figcaption></figure>
5. **TAF Labels:** The test labels present in the ARM TAF module are displayed. Select the test cases as per your requirements.
   1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment from proceeding if any errors/warnings occur while running the test cases.
   2. **Run Test even when the Deployment fails:** Until now, users were able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage was successful. This leads to failure of the deployment if the test cases fail in the 'test' stage. In the recent release, users will still be able to proceed with the test even if the deployment fails.
   3.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046491598.png" alt="" width="375"><figcaption></figcaption></figure>
6. **Version Control:** The test cases committed to a branch in version control are displayed.
   1. Select the [ **Version Control Repository** ](https://knowledgebase.autorabit.com/docs/version-control-repository) type.
   2. Select the **Repository** and the **Branch**.&#x20;
   3. Select the way you would like to run your test cases, i.e., TAF, Selenium Maven, or Selenium Non-Maven.
      1. For the **Selenium Maven** test type, you need to enter the test case root path in the **Test Case Root Path** field. Also, specify the goals.
      2. For the **Selenium Non-Maven** test type, you need to choose the **Execution Type**, and enter the test case root path in the **Test Case Root Path** field.
   4. **Additional options:**
      1. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
      2.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046646306.png" alt="" width="563"><figcaption></figcaption></figure>
7.  **AccelQ:** Select the Fetch Test Cases as **'AccelQ'**. Enter your **Project Name** and the **Test Job Name** and set the **parameter(s)** for your AccelQ test.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046710823.png" alt="" width="563"><figcaption></figcaption></figure>
8. **Provar:** Select Fetch Test Cases from **'Provar.'**
   1. Select your **Version Control Repository** and the **Branch** and provide the **Provar test cases path**.
   2. **Test Cases Root Path**: Enter the test case root path to the **.testproject** file
   3. **Test Cases Execution Path:** Enter the test case's execution path here. **Ex:** tests/samples and if not specified, all the test cases from the **'tests'** folder will be executed.
   4. **Additional options:**
      1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment from proceeding if any errors/warnings occur while running the test cases.
      2. **Run Test even when the Deployment fails:** Until now, users were able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage was successful. This leads to failure of the deployment if the test cases fail in the 'test' stage. With the 19.3 release, users will still be able to proceed with the test even if the deployment fails.
      3.  **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.\


          <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665046980511.png" alt="" width="563"><figcaption></figcaption></figure>

#### Callout URL

The Callout URL lets you call another service from the ARM application via an HTTP request. For an HTTP callout to work correctly, all the HTTP callout parameters and the entities associated with the callout must be configured correctly. ([Learn more](https://portal.document360.io/arm/docs/configure-callout-url))

#### Notifications

Send email notifications to selected users' emails upon the success or failure of a build.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1665047406818.png" alt=""><figcaption></figcaption></figure>

#### Schedule&#x20;

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only be saved, and you can run it when required.&#x20;

Limitation

If the new package version is in the format **2.0.0-0**, then when the CI job runs, the new package version created will be in the format **2.0.0.0** instead.
