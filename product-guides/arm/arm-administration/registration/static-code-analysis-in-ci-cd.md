# Static Code Analysis in CI-CD

### 1. What is a Static Code Analysis (SCA)? <a href="#id-1-what-is-a-static-code-analysis-sca" id="id-1-what-is-a-static-code-analysis-sca"></a>

Static code analysis, also known as static analysis or source code analysis, is a method used in software development to analyze the source code of a program without actually executing it. It involves reviewing the code for potential defects, vulnerabilities, and other issues to identify and fix them before the code is compiled or executed.

Static code analysis tools analyze the code for adherence to coding standards, coding best practices, and potential coding errors. These tools can scan the source code for a wide range of issues, including syntax errors, semantic errors, unused variables, potential security vulnerabilities, performance issues, and code smells, which indicate poor coding practices.

Static code analysis helps to identify and fix issues early in the development process, reducing the likelihood of introducing bugs or vulnerabilities into the compiled or executed code. It can also improve code quality, maintainability, and reliability, as it helps developers identify and address potential issues before they become critical problems.

### 2. SCA tools supported <a href="#id-2-sca-tools-supported" id="id-2-sca-tools-supported"></a>

The SCA tools supported with ARM are:

* Apex PMD
* Checkmarx
* CodeScan
* Salesforce Scanner
* SonarQube

### 3. Integrate SCA into your build process <a href="#id-3-integrate-sca-into-your-build-process" id="id-3-integrate-sca-into-your-build-process"></a>

Incorporate the SCA tool into your build process to automatically scan the source code during the build or continuous integration (CI) process. To do so,

1. Log in to your ARM account.
2. Go to the **`Admin > Plugins`** section.
3. In the **`Static Code Analysis`** section, choose the SCA tool to include as part of the build or CI process.

#### 3.1 Integrate Apex PMD <a href="#id-31-integrate-apex-pmd" id="id-31-integrate-apex-pmd"></a>

Apex PMD comes with a comprehensive rule set. However, you can define your own rule set to silence warnings that aren't relevant or change the warning level for specific rules.

1. Select the **`Edit`** icon beside the ApexPMD checkbox.
2. Upload your custom Apex PMD rules set using the **`Choose file`** field and upload it from your local machine.
3. To use the default Apex PMD rule set, click on the **`Download`** icon to download the default rule set in .XML format. You will need to upload them again using the **`Choose file`** field.
4. Click **`Save`** to save the plugin configuration.

#### 3.2 Integrate CheckMarx <a href="#id-32-integrate-checkmarx" id="id-32-integrate-checkmarx"></a>

To integrate Checkmarx as an SCA plugin,

1. Select the **`Edit`** icon beside the Checkmarx checkbox.
2. Fill in the below details:
   1. **`CxServer:`** Checkmarx Server URL or IP address, e.g., _`http://server-name`_.
   2. **`Team Name:`** Enter the relevant team name for the project.
   3. **`Select Credential:`** Choose your user's credential from the list. If you cannot find your credentials, you must create a new one (using the + icon) and save them in ARM. Refer [Create User's Credentials](../user-management/arm-credential-manager.md).
   4. Click on **`Test Connection`** to authenticate your details.
   5. Click **`Save`**.
3. Click **`Save`** on the **My Account** page to save the plugin configuration.

#### 3.3 Integrate CodeScan <a href="#id-33-integrate-codescan" id="id-33-integrate-codescan"></a>

To integrate all the functionality in your CodeScan license with ARM, you must integrate CodeScan as a plugin with your ARM account. However, it requires some steps in CodeScan and your ARM account to get configured.

**Prerequisites:**

* [**CodeScan security token**](../../../codescan/getting-started/setting-up-a-codescan-cloud-organization/generate-a-security-token.md)**.** This token will be used instead of a password while storing your credentials inside ARM. You can generate a new token inside CodeScan by navigating to **`My Account > Security`** tab.
* [**CodeScan Organization key**](../../../codescan/getting-started/setting-up-a-codescan-cloud-organization/finding-your-organization-key.md)**.** You can always find your organization key on the top right corner of your Organization’s home page inside CodeScan.

**Integration Steps:**

1. Select the **`Edit`** icon beside the CodeScan checkbox in ARM (under the **`My Account > Plugins`** section).
2. Enter the CodeScan **`host (instance) URL`**. For the CodeScan cloud version, enter **`https://app.codescan.io/`** for the **US** region, **`https://app-eu.codescan.io/`** for the **EU** region, or **`https://app-aus.codescan.io/`** for the **AUS** region.
3. Select your CodeScan host type (cloud or on-premise).
4. Select your **`credential`** from the drop-down. If you do not have one created yet, use the **`+`** icon to register a new credential inside ARM. Make sure you enter the CodeScan token key in the **`Password`** field.
5. Enter your **`Organization key`**. This is applicable only if you are using the CodeScan cloud version.
6. Click on **`Test Connection`** to authenticate your details.
7. Click **`Save`** on the **My Account** page to save the plugin configuration.

#### 3.4 Integrate Salesforce Scanner <a href="#id-34-integrate-salesforce-scanner" id="id-34-integrate-salesforce-scanner"></a>

The Salesforce Scanner plugin aggregates the results of static analyzers most relevant to Salesforce developers by employing a unified set of rules checked by their respective rule engines, making additional configuration rules optional.

**Prerequisites**

If you want to opt to add customized rules to perform the analysis, please write your ruleset as per your requirements, and save them with the following name and format exactly as it is:

* **PMD Config:** _pmdconfig.xml_
* **eslintrc:** _.eslintrc.json_
* **tsconfig:** _tsconfig.json_

{% hint style="info" %}
**Note**:

If the config file has the wrong name or format, an error message will popup. Please change the name/format, and then upload the file again.
{% endhint %}

**To integrate Salesforce Scanner as an SCA plugin,**

1. Select the **Salesforce Scanner** checkbox.
2. To add extra configurations,
   1. Click the **`Edit`** icon beside the Salesforce Scanner checkbox.
   2. Click the **`Choose File`** button to upload one or more of the following configuration files from your local machine:
      1. **`PMD Config:`**
      2. **`eslintrc:`**
      3. **`tsconfig:`**
   3. Click **`Save`** to save the Salesforce Scanner settings
3. Click **`Save`** on the **My Account** page to save the plugin configuration.

#### 3.5 Integrate SonarQube <a href="#id-35-integrate-sonarqube" id="id-35-integrate-sonarqube"></a>

To integrate all the functionality in your SonarQube license, you must integrate SonarQube as a plugin with your ARM account. However, configuring in SonarQube and your ARM account requires additional steps.

**Prerequisites:**

1. **SonarQube Security token**. This token will be used instead of a password while storing your credentials inside ARM. You can generate a new token inside SonarQube by navigating to the **`User > My Account > Security`** tab.
2. **SonarQube Organization key**. You'll find your organization key by clicking your **user** icon in the **`top-right corner > My Account > Organizations`**. You'll see there the organization's name and its key.

**Integration Steps:**

To integrate SonarQube after completing the prerequisites:

1. Select the **`Edit`** icon beside the SonarQube checkbox in ARM (under the **`My Account > Plugins`** section).
2. Enter the SonarQube **`host URL`**. For the SonarQube cloud version, use _**`https://sonarcloud.io`**_
3. Choose the SonarQube **`host type`**, i.e., cloud or on-premise. For SonarQube hosted on the cloud, you must add the **organization key**.
4. Select your **`credential`** from the drop-down. If you do not have one created yet, use the **`+`** icon to register a new credential inside ARM. Make sure you enter the CodeScan token key in the **`Password`** field.
5. Enter your **`Organization key`**. This is applicable only if you are using the SonarQube cloud version.
6. Click on **`Test Connection`** to authenticate your details.
7. Click **`Save`**.
8. Click **`Save`** again on the **My Account** page, and you are all set with SonarQube integration.

{% hint style="info" %}
**Point to note**:

If there is no **Master Analysis** available, you will get the following message on the screen:

_You do not have a Master analysis. We recommend you to run the Master (baseline) analysis from the Static Code Analysis (hyperlink) section in the Reports module before you proceed. If you do not run the Master analysis, the analysis from this job will become your Master (baseline) analysis._

Click **Continue anyway** to proceed with the new analysis as Master.
{% endhint %}

### 4. Setting Global Criteria for SCA <a href="#id-4-setting-global-criteria-for-sca" id="id-4-setting-global-criteria-for-sca"></a>

We’ve added the feasibility where you can set the global criteria to enforce SCA tools across CI jobs, deployments, and gated commits. Based on the priority set, the build will be successful only if the criteria are met.

You can find the option to set global criteria for SCA under the **`Admin > My Account > Validation Criteria - Static Code Analysis`** section. Next, select the **`Enable Validation Criteria - SCA`** checkbox.

For example, when you use the Apex PMD rule during a scan, you have to give it Priority depending on the importance of this rule on your business needs. PMD’s default priority – 1, highest to 5, lowest. Next, you must add the desired value to the severity set. You can use the **`+`** icon to add more than one priority for apexPMD.

Other SCA tools should also follow the same procedures; however, the fields may differ from those for ApexPMD.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-TL4M8JF2.png" alt="" width="563"><figcaption></figcaption></figure>

### 5. Running SCA in CI Job <a href="#id-5-running-sca-in-ci-job" id="id-5-running-sca-in-ci-job"></a>

Continuously run SCA as part of your development process and regularly review and address the identified issues. Analyze the results and optimize your coding practices based on the feedback from the SCA tool to improve code quality over time.

When executing a CI Job, you can select the Static Code Analysis tool to run into your build or continuous integration (CI) processes.

1. Select the **`Run Static Analysis Report`** checkbox in the **`Build`** section.
2. Select the desired SCA tool from the dropdown.
3. There are different fields for each SCA that you need to fill to configure SCA for your build process.

**For 'ApexPMD' and 'Salesforce Scanner';**

* **Run On All Supported Metadata Types:** Apex PMD and Salesforce Scanner SCA supports various metadata types in Salesforce, including _Apex classes, Apex triggers, Apex pages, Lightning components, Lightning web components, Aura components,_ and more. The scan runs on the supported metadata types on your Salesforce org or version control system configured as part of the build. Supported Metadata Types:
  * **ApexPMD:** _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
  * **Salesforce Scanner:** _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle, CustomObject, Flow, Profile, PermissionSet, Settings, SharingRules, Workflow, StaticResource._
* **Run On Newly Added Supported Metadata Types:** The scan runs on the recently added/updated metadata types available on your Salesforce org or version control system configured as part of the build.
* **Mark Build As Unstable If Doesn't Meet Below Criteria:** Set the priority for your scan, which means if the priority set is not achieved, the current build will be treated as unstable. This helps in reporting the code quality of the developer team. An email is triggered to inform you that the build failed as the criteria set for static code analysis were not met.

**For 'Checkmarx';**

*   **`Run On All Apex Classes, Triggers, Apex Pages & AuraDefinitionBundles:`** Checkmarx SCA supports various metadata types in Salesforce, including _Apex classes, Apex triggers, Apex pages, Lightning components, and Aura components_. The scan runs on the supported metadata types on your Salesforce org or version control system configured as part of the build.

    Checkmarx- Supported Metadata Types:

    _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
* **`Criteria rules for the stable build:`** Set the priority for your scan, which means if the priority set is not achieved, the current build will be treated as unstable. This helps in reporting the code quality of the developer team. An email is triggered to inform you that the build failed as the criteria set for static code analysis were not met.

**For 'CodeScan' and 'SonarQube';**

*   **Run On All Supported Metadata Types:** CodeScan and SonarQube SCA supports various metadata types in Salesforce, including _Apex classes, Apex triggers, Visualforce pages, Lightning components, Lightning web components, Aura components_, and more. The scan runs on the supported metadata types on your Salesforce org or version control system configured as part of the build.

    * This will be visible on both pre-validation commits and merges.&#x20;
    * Analysis will be run on all selected respective supported components on the pre-validation commit.&#x20;
    * In merge, it runs on the entire branch irrespective of merging components.

    **Supported Metadata Types:**

    * **CodeScan:** _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle, CustomObject, Flow, Profile, PermissionSet, Settings, SharingRules, Workflow, StaticResource._
    * **SonarQube:** _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle._
* **Run On Newly Added Supported Metadata Types:** The scan runs on the recently added/updated metadata types available on your Salesforce org or version control system configured as part of the build.&#x20;
  * This will be visible on both pre-validation commits and CI Jobs.
  * Pre-validation Commits: Analysis will be run on selected respective newly added supported components.
  * CI Jobs: Analysis will be run on newly retrieved supported components in CI Jobs.
* **Run On All Supported Metadata Types from the full source:** CodeScan and SonarQube SCA analysis is performed on your entire Salesforce org or version control system for various supported metadata types in Salesforce, regardless of any build changes.&#x20;
  * This will be visible only on CI Jobs.&#x20;
  * The analysis will be run on the entire branch.

{% hint style="info" %}
**Point to note**:

This option is only available for the following CI jobs:

* Build a package from Version Control
* Deploy from Version Control to a Salesforce Org
* Deploy from SFDX branch to a Salesforce Org
{% endhint %}

* **Mark Build As Unstable If Doesn't Meet Below Criteria:** Set the priority for your scan, which means if the priority set is not achieved, the current build will be treated as unstable. This helps in reporting the code quality of the developer team. An email is triggered to inform you that the build failed as the criteria set for static code analysis were not met.

### 6. Running SCA in CI Job <a href="#id-6-running-sca-in-ci-job" id="id-6-running-sca-in-ci-job"></a>

ARM allows you to set the validation criteria to enforce SCA tools while performing EZ-Commits. You can find the option to set the commit validation criteria for your SCA under the **Admin > My Account > Commit Validation – Approval Settings** section.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-8DKTUYZ1.png" alt="" width="375"><figcaption></figcaption></figure>

Select the **Enable criteria-based review process** checkbox, and then select the **Should pass validation criteria for Static Code Analysis** checkbox to reveal all the SCA tools. You can choose one or more, or all the tools, to run your code through.

Using the **Auto reject commit process if the criteria are not met** checkbox, you can choose to reject the commit automatically if the criteria are not met, even for one of the selected tools. For example, if the criteria are met for Apex PMD, Checkmarx, and CodeScan, but not for SonarQube, then the commit is rejected. After you edit the code and run it again through the SCA tool(s) for validation, the code goes through all the selected tools again, even the ones for which the criteria were met in the previous attempt.

With the **Auto-approve on commit validation** and **Auto-commit on approval** checkboxes, you can choose to auto-approve the commit if the criteria are met, and also auto-commit once it is approved manually or automatically.

### 7. Running an SCA during Deployment <a href="#id-7-running-an-sca-during-deployment" id="id-7-running-an-sca-during-deployment"></a>

You can choose an SCA tool to detect bugs, code smells, and security vulnerabilities on the **Deployment Settings** screen before the deployment begins.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-6UF9CSWY.png" alt="" width="375"><figcaption></figcaption></figure>

ARM stores the Static Code Analysis source content for 90 days. The report is deleted automatically after 90 days. For PMD reports generated less than 90 days before, the source content files are not shown in the Static Code Analysis report.

SCA Supported Metadata Types:

* For **Apex PMD, Checkmarx, SonarQube:** _Apex Classes, Apex Triggers, Apex Pages, AuraDefinitionBundle, LightningComponentBundle_
* For **CodeScan:** _Apex Classes, Apex Pages, Apex Triggers, AuraDefinitionBundle, CustomObjects, Flow, LightningComponentBundle, PermissionSets, Profiles, Settings, SharingRules, Workflows_

Select the **Stop deployment if build doesn't meet global criteria** checkbox if you don’t want the deployment to proceed unless all criteria are met. These are the same global criteria you set for your SCA tool in **My Account > Validation Criteria – Static Code Analysis** section.\
You can also select one or more recipients to alert under the **SCA Mail Notifications** field.

### 8. Running an SCA during an EZ-Merge <a href="#id-8-running-an-sca-during-an-ezmerge" id="id-8-running-an-sca-during-an-ezmerge"></a>

You can select the static code analysis tool on the **New EZ-Merge** page as part of a pre-validation merge before merging to your target branch.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-QLX5NXCO.png" alt="" width="375"><figcaption></figcaption></figure>

**Run Static Code Analysis:** Select this checkbox if you want to run a Static Code Analysis tool to identify potential software quality issues before the code moves to production. Like **Generate Diff Report**, this checkbox is selected by default if the criteria are set globally under the **My Account > Commit Validation – Approval Settings** section.

* For **Apex PMD**, **Checkmarx**, **CodeScan**, and **SonarQube**, ARM allows you to set the criteria for running the SCA tool, whether to run on all supported metadata types from the full source or to run on the newly added components.
*   The SCA with “all supported metadata” will scan the entire target branch during the EZ merge.

    Whereas during an EZ commit, the SCA with “all supported metadata” will scan only the supported metadata that are part of the commit.

Timeout Exceptions:

* Whenever a code analysis is triggered, ARM will wait up to 5 hours for a response. If the code analysis is not completed within 5 hours, ARM will throw an error. This applies to all SCA tools, including Salesforce Scanner.
* The merge process in ARM is valid for 7 days. You must resolve merge conflicts, if any, for your merge label and commit the changes to another branch within 7 days, or the merge expires. Generated SCA reports related to such merges also expire after 7 days.
