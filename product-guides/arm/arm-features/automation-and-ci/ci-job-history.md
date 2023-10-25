# CI Job History

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

The **CI Job History** is the page where you can:

* create a new CI job
* trigger a new build for your CI job
* find the build/deployment details, SCA report, etc., for your CI builds

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1683708353919.png)

### Deployment Workspace <a href="#deployment-workspace" id="deployment-workspace"></a>

View the builds in the deployment queue and why they're in the queue on the **Deployment Workspace** on the right side of the page.\
\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1683708442299.png" alt=""><figcaption></figcaption></figure>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682665491798.png)

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682665552969.png)

Important Notes:Different reasons why the queued build is displayed in the Deployment Workspace and the required action:

* The limit for parallel processing has been reached. Please wait.
* The agent is currently unable to process the request. Please check the agent's connection.
* Another CI job deployment to the same destination is currently in progress. Please wait.
* The previous CI job build is still in progress. Please wait.
* The previous CI job build is still in the queue. Please wait.

### Build Details <a href="#build-details" id="build-details"></a>

For each **Build**, the following information is displayed:

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1683708672680.png)

* **Build Label**: Displays the names of the build that has been created.
* **Build Date**: This shows the date and time the process was created and run.
* **Build Number**: Build numbers for each Job in reverse chronological order.&#x20;
* **Abort (if the build is in progress)**: Abort the ongoing CI job deployment and test case execution. This option will be available only if the build is in progress.
* **Build Information (**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624801572677.png)**)**: View the complete build information or download them to your local machine. The file downloads in ZIP format.
* **Build Status:** View the status of the build triggered (success/in progress/failed). There is a provision to **download** the build log report from the log screen.

#### Warnings, Changes, Check-ins, and SCA <a href="#warnings-changes-checkins-and-sca" id="warnings-changes-checkins-and-sca"></a>

Hover your mouse over the (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624801827611.png)) icon under the **Build Details** to find out two to three choices depending on your configured job:

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624801953533.png" alt=""><figcaption></figcaption></figure>

**Warning**

View the warnings that occurred when builds were deployed. The '**No Warnings Found**' popup will appear if no warnings are found.

**Changes**

The Changes screen will display the following info:

*   **Metadata Changes:** This tab will include all metadata changes made in the current build.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659521211281.png" alt="" width="563"><figcaption></figcaption></figure>
*   **Destructive Changes:** The destructive changes components will get listed on this tab ([Learn More](../destructive-changes.md))\
    \


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659521375210.png" alt="" width="563"><figcaption></figcaption></figure>
*   **File Changes:** This tab will list all newly added/modified metadata files. The number of lines being added or deleted will be highlighted appropriately. The lines highlighted in red color indicate those deleted from the metadata files, and those in green color indicate newly added/updated.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659521832074.png" alt="" width="563"><figcaption></figcaption></figure>
*   Also, the user can download individual metadata file change reports using the **Download** icon.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659522126862.png" alt="" width="375"><figcaption></figcaption></figure>
*   **Check-ins:** The user can get a comprehensive check-in summary for their CI job in this tab. This displays all the revisions that are included in the build cycle.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659538685027.png" alt="" width="563"><figcaption></figcaption></figure>
* **Points to Remember:**
  * For the files with huge content, the differences in the metadata files will not be shown on UI. However, the user can download the diff on their local machine and view them.
  * Excluded metadata members are too not shown under the **File Changes** tab. Also, for the SFDX Jobs build with a single source folder, the **File Changes** tab will not show other folder files even if exists in the revisions.
  * For builds triggered earlier, the user may not find the **File Changes** tab.
  * Recently triggered builds will now have **File Changes** along with **Check-Ins** view.
  * For Version Control as GIT, the delta is generated with git diff to pick all the required changes (in case of lazy commits created using gated merge). So, there could be a chance of a discrepancy in the files with **Metadata Changes** and **Check-Ins**.
  * For Version Control as **GIT**, the delta generates with git diff to pick all the required changes (in case of lazy commits created using gated merge). However, there may be a slight chance of discrepancies in the files with metadata changes and Check-Ins.
  * Builds triggered with the GIT repository between the two weekly fixes will not show all the revision details in the Check-Ins. Instead, all the changed files are bounded to a single **HEAD** revision of that build.
  * **Parent Revisions** in the **Check-ins** tab will be blank for the jobs run before version **22.1.18-RELEASE**.

**SCA (Static Code Analysis)**

Static Code Analysis is usually performed as part of a Code Review and is carried out at the Implementation phase of a Security Development Lifecycle (SDL). [Static Analysis tools](https://www.codescan.io/) such as **ApexPMD** and **Checkmarx** continuously detect and report on data flow problems, software defects, language implementation errors, inconsistencies, dangerous usage, coding standard violations, and security vulnerabilities.

SCA will have information for the PMD report. This report will have info about the files that were reviewed and the related violations that occurred. Click on each file to view related violations that will appear at the bottom right side of the page. If you click on any violation, it will take you to the respective line (in the black screen on the right side) where such a violation occurred.&#x20;

![Static code analysis](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-53\(1\).png)

![Apex class](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-413.png)

![Link report](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-659\(1\).png)

### Deployment Details <a href="#deployment-details" id="deployment-details"></a>

Under the **Deployment details**, you can view the below information:

![Deployment details](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624805604251.png)

1.  **Deployment Status:** View the status of the deployment triggered.

    | Icon                                                                                                         | Status                            |
    | ------------------------------------------------------------------------------------------------------------ | --------------------------------- |
    | ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-148\(1\).png) | Validate deployment is successful |
    | ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-114.png)      | Validate deployment is failed     |
    | ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-785.png)      | Deployment is successful          |
    | ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-197.png)      | Deployment is failed              |
2. **Deployment Log:** View the detailed deployment log report on UI or download them to your local machine.
3. **Quick Deploy:** View the status of the quick deployment performed or re-run the quick deployment again
4. **Rollback:** The rollback feature is handy to roll back a deployment when you realize something went wrong with the CI job or accidentally deploy something unwanted. (Learn more)Rollback Prerequisites:Enable the **Rollback** checkbox while creating a CI Job (in the **Deploy** section).
   * The **Rollback Validation** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-441.png)) icon denotes the rollback is successfully validated, and rollback can be triggered once again. This icon can be seen only if the **Validate Rollback** option is chosen during rollback.
   * **Re-run Rollback**: You can choose the metadata members you want to perform the rollback while rerunning the rollback. If there are any metadata members that you no longer require and would like to delete from your org, you can perform the destructive changes (pre/post) to such components. The selected components, i.e., excluded components details, can be found in the **Rollback Log**.

### Deployment Reports <a href="#deployment-reports" id="deployment-reports"></a>

You can download the deployment, quick deployment, or rollback reports for your build by hovering the mouse over the (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624801827611.png)) icon under the **Deployment Details** section.

* **Deployment Reports:** Displays the detailed deployment report. A sample screenshot is attached below.
  *   **Dependency Analyzer:** For failed deployments, download the analysis results of failed components in the source org selected while creating the CI job. You can download it in **Manifest (JSON)** or in **XLS** format.\


      <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1683877709628.png" alt=""><figcaption></figcaption></figure>
  * For CI job builds older than **30 days**, deployment, quick deployment, or rollback reports are not accessible.
*   **Quick Deployment Report**: Enables you to view the quick deployment report.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1599807054893.png" alt=""><figcaption></figcaption></figure>
* **Rollback History**: View the detailed rollback history report here. The user can also view the rollback log and report on this screen.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624806683005.png" alt=""><figcaption></figcaption></figure>

### Post Activities <a href="#post-activities" id="post-activities"></a>

View the activities triggered post-deployment, log report, and post-activity status, i.e., success or failure.

| Post Activity Status | CI Job                                | Environment Provisioning            | Data Loader                           | Merge                              | Jenkins Job                                     |
| -------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------- | ---------------------------------- | ----------------------------------------------- |
| **Success**          | Completed                             | Success                             | Completed                             | Merged                             | Success or unstable                             |
| **Failed**           | Any other status except for completed | Any other status except for success | Any other status except for completed | Any other status except for merged | Any other status except for Success or unstable |

### Functional Tests <a href="#functional-tests" id="functional-tests"></a>

View the success and failure test percentage report for your build triggered.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624806975504.png" alt="" width="375"><figcaption></figcaption></figure>

### Apex Tests (Coverage) <a href="#apex-tests-coverage" id="apex-tests-coverage"></a>

Under the **Apex Tests (Coverage)** tab, you can view the code coverage report here. The code coverage report provides information about the apex tests that are run, the classes that are covered, and the assertions that have failed and provides a percentage of the code that is covered by the test execution for an org.
