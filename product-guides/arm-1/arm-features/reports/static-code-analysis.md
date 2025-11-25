# Static Code Analysis

### Overview <a href="#overview" id="overview"></a>

Static code analysis, or static analysis, is a software verification activity that analyzes source code for quality, reliability, and security without executing the code. Using static analysis, you can identify defects and security vulnerabilities that could compromise the safety and security of your application. Static analysis is a cost-effective approach to measuring and tracking software quality metrics without the overhead of writing test cases or instrumenting your code.

Static analysis is generally good at finding coding issues, such as:

* Programming errors
* Coding standard violations
* Undefined values
* Syntax violations
* Security vulnerabilities

### Run Static Code Analysis <a href="#run-static-code-analysis" id="run-static-code-analysis"></a>

To run a static code tool on your Salesforce Org or Version Control Branch, follow the steps below:

1.  Hover your mouse over the **Reports** module and choose the option: [**Static Code Analysis**](https://www.autorabit.com/products/codescan/)**.**<br>

    <figure><img src="../../../../.gitbook/assets/image (2156).png" alt=""><figcaption></figcaption></figure>
2.  Click on the **New Static Code Analysis** button at the top right corner of the screen.<br>

    <figure><img src="../../../../.gitbook/assets/image (2157).png" alt="" width="206"><figcaption></figcaption></figure>
3. On the next screen, enter a **Label Name**.
4. Choose **Source** as **Salesforce Org** or **Version Control**.
   *   For **Salesforce Org** selection, choose the Salesforce Org for which the SCA will be performed.<br>

       <figure><img src="../../../../.gitbook/assets/image (2158).png" alt=""><figcaption></figcaption></figure>
   *   For [**Version Control**](../../../arm/arm-features/version-control/) selection, choose your source **Repository** and **Branch**.<br>

       <figure><img src="../../../../.gitbook/assets/image (2159).png" alt=""><figcaption></figcaption></figure>
   *   Select **Source** as **Salesforce org**, then new options become available:\
       <br>

       <figure><img src="../../../../.gitbook/assets/image (2160).png" alt=""><figcaption></figcaption></figure>

* When performing a prevalidation commit with SCA analysis in DX format on the respective SF Org and package directory, consistency with previously executed analyses for this SF Org and related directory is crucial. Choosing the appropriate comparison branch is essential for accurate evaluations.
* Existing analyses lack branch tracking, limiting the effectiveness of the fix to new analyses if transitioning from a base scan in mdapi to DX, project deletion, and rerun become necessary for recreation in the DX source structure.
* Building on point #1, achieving the described outcome is unattainable with different structures but aligns seamlessly within a single structure per project.
* Depending on the need, a Salesforce or a repository must be bonded with either mdapi or DX source structure but not with both.

5.  Select the SCA tool from the dropdown list. For example, [_CodeScan_](https://www.codescan.io/), _ApexPMD, Checkmarx, Salesforce Scanner, or SonarQube_.<br>

    <figure><img src="../../../../.gitbook/assets/image (2161).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Before running the **Static Code Analysis** tool, you must enable them under the **My Account > Plugins** section.
{% endhint %}

6. The list of respective **Metadata Types** is displayed for the selected SCA tool. By default, all are selected. You can unselect certain metadata types as per your requirements.\
   Supported Metadata Types:
   * For **ApexPMD, Checkmarx, SonarQube**: _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
   * For **CodeScan, Salesforce Scanner**: _ApexClasses, ApexPages, ApexTriggers, AuraDefinitionBundle, CustomObjects, Flow, LightningComponentBundle, PermissionSets, Profiles, Settings, SharingRules, Workflows, StaticResource._
7. For **CodeScan** or **SonarQube**, choose the **Baseline Branch** if you want to run comparisons between reports.<br>

<figure><img src="../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1).png" alt="" width="432"><figcaption></figcaption></figure>

8. Select the recipients for the alert under the **Notifications** field. Multiple recipients can be added here
9.  Next, choose the frequency for the SCA to run, e.g., daily, weekly, or at any specific interval. For example, if you want the SCA tool to run daily at **10 a.m.**, select the **Daily** option and set the fixed time to 10.<br>

    <figure><img src="../../../../.gitbook/assets/image (2162).png" alt=""><figcaption></figcaption></figure>
10. Click on **Save**.
11. Upon confirmation, you'll be redirected to the home page, where you can find your recently configured SCA.<br>

    <figure><img src="../../../../.gitbook/assets/image (2163).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** When the analysis is run on a zip file, the content is not visible in the UI. But Salesforce Scanner can scan the zipped file and provide the vulnerabilities. However, the file contents for **Static Resource** metadata type are empty.
{% endhint %}

#### Additional options on this page <a href="#additional-options-on-this-page" id="additional-options-on-this-page"></a>

1. **Editing the Schedule:** Locate the edit schedule icon.\
   \
   ![](<../../../../.gitbook/assets/image (2164).png>)
2. Choose the desired report frequency (daily, weekly, monthly, etc.).
3. Specify the exact times for reports to run.
4. Please add/remove an email If you want to send/not send the notification.
5.  Click on **Update** to save and confirm the changes made to the schedule.<br>

    <figure><img src="../../../../.gitbook/assets/image (2165).png" alt=""><figcaption></figcaption></figure>
6. **Running On-Demand SCA**: To run the SCA tool before the scheduled time frame, click on the **Run (**![](<../../../../.gitbook/assets/image (34) (1) (1) (1).png>)**)** button.\
   \
   ![](<../../../../.gitbook/assets/image (2166).png>)<br>
7.  **Log**: Click on the **Log** (![](<../../../../.gitbook/assets/image (39) (1) (1) (1).png>)) icon to find the detailed log report.<br>

    <figure><img src="../../../../.gitbook/assets/image (2167).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../../../.gitbook/assets/image (2168).png" alt=""><figcaption></figcaption></figure>



1.  **SCA Result**: ARM generates a detailed SCA report whenever you run static code analysis. This report will have info about the reviewed files and the related violations. Click on each file to view its related violations at the bottom right side of the page. If you click on any violation, it will take you to the respective line (in the black screen on the right side) where the violation occurred.<br>

    <figure><img src="../../../../.gitbook/assets/image (2169).png" alt=""><figcaption></figcaption></figure>
2. **Download SCA Report**: Click on the **Download** (![](<../../../../.gitbook/assets/image (44) (1) (1) (1).png>)) icon to download the report in CSV format on your local device.
3. **Delete SCA process**: Click on the **Delete (**![](<../../../../.gitbook/assets/image (45) (1) (1) (1).png>)**)** icon to delete the SCA process configured for your org/ancestor. This cannot be undone.
4.  **View the SCA run details**: To view the list of SCA runs to date along with individual SCA results, click on the **Label Name**. The main screen shows the last details of the SCA run.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (2170).png" alt=""><figcaption></figcaption></figure>

### **Points to Note:** <a href="#points-to-note" id="points-to-note"></a>

We are utilizing **\<sforgname>** or **\<reponame>** as the project’s unique identifier, and we’re creating short-lived branches for each run. Thus, the technique builds a single project for a single Salesforce Org or Version Control Repo/branch and then executes the analysis on the short-lived branches.

The naming convention for the short-lived branches: **\<jobname\_branchname>**

The short-lived branches are active for a limited time (30 days by default, depending on _SonarQube/CodeScan_ configuration), after which they will be automatically deleted. The report will remain on ARM. However, the branch will be removed from the _SonarQube/CodeScan_ side.

Scans run only on the **source**, whether the source is **VC Repo** or **SF Org**. The scan results will then be available in the **Reports** module. Users can trace the job that is run in ARM to the scan using the unique identifier.

{% hint style="info" %}
**Important Note:**

If there is no **master analysis** available, you will get the following message on the screen:&#x20;

_You do not have a Master analysis. We recommend you run the Master (baseline) analysis from the Static Code Analysis (hyperlink) section in the Reports module before you proceed. If you do not run the Master analysis, the analysis from this job will become your Master (baseline) analysis._

Click **Continue anyway** to proceed with the new analysis as Master.
{% endhint %}
