# How Do I Commit?

### How do I commit? <a href="#how-do-i-commit" id="how-do-i-commit"></a>

The article below discusses performing an EZ-Commit in ARM and committing the necessary code changes to a target branch.

The **New EZ-Commit** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.

#### Step 1: Initial Phase <a href="#step-1-initial-phase" id="step-1-initial-phase"></a>

1. Log in to your ARM account.
2. Hover your mouse over the [**`Version Control`**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) module and select **`Commits`**.

<figure><img src="../../../../../.gitbook/assets/image (1041).png" alt="" width="348"><figcaption></figcaption></figure>

3. Click on the **`New EZ-Commit`** button.

<figure><img src="../../../../../.gitbook/assets/image (1042).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, select the source [**`Salesforce Org`**](https://knowledgebase.autorabit.com/docs/salesforce-org) from which the changes will be retrieved.
5. Select the user registered for the above Salesforce org.
6. Select the version control **`Repository`** and the **`Branch`** where the changes will be committed. For Version Control as GIT type, the user can create a new branch from the EZ-Commit user interface.

<figure><img src="../../../../../.gitbook/assets/image (1043).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Notes:**

1. There is a provision to choose **`All`** in the **`Salesforce Org Author`** field. Upon selection, this commits changes across the org irrespective of the user registered to that Salesforce org.&#x20;
2. In addition to the ALL provision, any Salesforce Org Authors who have access to create, edit, or delete data through either profile or permission-set assignments will be listed and can be selected individually.
3. These options are accessible only to ARM administrators or users who have permission to commit on behalf of others.&#x20;
4. When **Skip Mapping** is set to false, users cannot choose associated child branches of a mapped branch. In the recent release, ARM reads the mapped branch for your version control repository and displays the related child branches during commit, even if skip mapping is disabled.
{% endhint %}

7. Under the **`Fetch Changes`** tab, select how the components are to be fetched from the above-selected source org.\

8.  Under the **`Fetch Changes`** tab, select how the components are to be fetched from the above-selected source org.

    <figure><img src="../../../../../.gitbook/assets/image (1045).png" alt=""><figcaption></figcaption></figure>

    *   **`Metadata Components:`** When selected, this retrieves all the metadata components available in the source Salesforce Org. Different ways to fetch the [**`Metadata Components`**](https://www.autorabit.com/blog/7-salesforce-security-concerns-relating-to-metadata/)are:

        1. **`Auto Draft:`** This brings all the changes the author has made in the Salesforce org that is not yet committed to the Version Control (ARM does the calculation by using the last modified date in the Salesforce Org and comparing it against the last commit date to Version Control branch).

        <figure><img src="../../../../../.gitbook/assets/image (1047).png" alt="" width="443"><figcaption></figcaption></figure>

        1. **`Select Manually:`** Choose the metadata components individually to be committed to the destination branch.
        2. **`Package Manifest:`** A package .xml file controls which metadata types and members are retrieved and deployed from the source org to the destination org. This type of file is also known as the project manifest. This control file allows you to initiate a commit process without manually selecting individual metadata components.

        <figure><img src="../../../../../.gitbook/assets/image (1048).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**&#x20;

Under the **`Package Manifest`** option, you can find the checkbox **`Apply Auto Draft`**.&#x20;

* If you click the checkbox above, the metadata components in the uploaded XML file will be compared to your source control and Salesforce, and any modified/added components will be displayed on the next Commits screen.
* If left unchecked, the components will be compared only with Salesforce, and any changed or newly added components will be shown on the next screen.
{% endhint %}

* **`Re-use Previous Validated Commit Label:`** If you placed changes related to a user story or task, etc., under a specific commit label, you can choose the same in this field. The main advantage of creating a commit label is to reuse the labels and perform multiple commits under a given label.

<figure><img src="../../../../../.gitbook/assets/image (1049).png" alt=""><figcaption></figcaption></figure>

* **`Vlocity Components:`** This option exports Vlocity data packs from a Salesforce org through a YAML manifest describing your project and committing the same to a VCS. The primary goal is to enable [Continuous Integration](https://www.autorabit.com/ebooks/how-banks-benefit-from-continuous-integration-and-delivery/) for Vlocity metadata through source control.

<figure><img src="../../../../../.gitbook/assets/image (1050).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note about Review Artifact:**&#x20;

* You can create a review of selected artifacts or a module or collection.&#x20;
* You can designate other team members as participants in the review. Depending on their assigned role in the review, participants receive requests and can approve, disapprove, or abstain from reviewing each artifact.
* When you download the file through Review Artifact and edit the changes locally, you must upload the zip file with the same name if you have hit the previous button on the commit screen; otherwise, you will encounter the error below: \
  ![](<../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)
{% endhint %}

To view changes to Salesforce metadata, edit them, and see the impact to ensure that your changes are correct, follow these steps:

1. Select the Review Artifact option while performing an EZ commit.
2. The Review Artifact screen will contain a **compare changes icon** that you can click on to view and edit any discrepancies that were identified with the artifacts:

<figure><img src="../../../../../.gitbook/assets/image (1051).png" alt=""><figcaption></figcaption></figure>

3. When you edit any of the code in the integrated development environment (IDE) and save the changes, the 'Compare Changes' screen should automatically reflect the current changes, highlighting the modifications with a color difference to distinguish between what has been changed and what has not.

<figure><img src="../../../../../.gitbook/assets/image (1052).png" alt=""><figcaption></figcaption></figure>

4. If you open the 'Compare Changes' screen and perform edits on any of the artifacts and then click on the close button, the system will navigate back to the 'Review Artifact' screen, and any new changes made will be reflected in the 'Compare Changes' screen.
5. If you are in the 'Review Artifact' screen and perform additional changes, once the changes are saved, the 'Compare Changes' screen will pick up the new changes and update the screen to reflect the most recent modifications.

If you check the **Review Artifact** box and choose only commit options for Profile/PermissionSet, the artifacts option will be ignored. The flow will continue with only commit options for Profile/PermissionSet.

*   Under the **`Perform`**&#x73;ection, you have different options:

    1. **`Validation of Changes (Before Commit):`** ARM allows performing a validation deployment before committing the changes. This command creates the validation deployment without committing any changes to the repository. If the deployment is successful, the commit is executed.
    2. **`Commit (Without Validation):`** Directly commit to your Version Control System without extra validations.
    3. **`Create a Pull Request:`** Create a pull request to propose and collaborate on changes to a repository. These changes are proposed in a branch, which ensures the master branch only contains finished and approved work.

    <figure><img src="../../../../../.gitbook/assets/image (1053).png" alt=""><figcaption></figcaption></figure>
* Under the **`Post Commit`** section, you can invoke certain processes after the commit is completed.
  1.  **`Create/Append Revision to existing Label`**

      * **`Commit Label:`** Commit Label helps to label a commit. For example, for changes related to a user story or task, etc., under a specific label, you can reuse the labels and perform multiple commits under a given label. Select the label from the dropdown or create a new one by clicking the + icon.
      * **`Release Label:`** A Release Label is created by grouping multiple EZ-Commit labels as a singular release label.

      <figure><img src="../../../../../.gitbook/assets/image (1054).png" alt=""><figcaption></figcaption></figure>

      * **ALM Label:** Users have the option to commit using solely the ALM Label or by choosing "None." This is applicable when the ALM item has been mapped in the Salesforce Org Management mappings section and the skip mappings option is not enabled. As part of this process, an ALM Label is generated post-commit and is visible under "Change labels" in the ALM Labels panel.

6. Click **`Next`**.

#### Step 2: Selecting the Components <a href="#step-2-selecting-the-components" id="step-2-selecting-the-components"></a>

The next screen will list the metadata types and their corresponding members. You will find 3-4 tabs as detailed below:

1. **`All Metadata Components:`** All metadata components available for your source org are listed here. Select the components you want to commit to the Version Control Branch.
2. **`Deleted:`**&#x41;RM compares the change with the Source Org and the Version Control Branch and lists all the available components. If you want to delete those components from the branch while committing, you can select those components in this tab.

{% hint style="info" %}
**Important Consideration:** If you delete any metadata with permissions on any profile/permissionsets, then all the profiles and permissionsets associated with that metadata are also updated.
{% endhint %}

3. **`Selected:`** Total selected components are displayed in this tab. The metadata components newly added or updated in the destination branch are shown as A/M (Added/ Modified), and the components to be deleted from the destination branch are shown as D (Deleted) under the **Action** tab.

<figure><img src="../../../../../.gitbook/assets/image (1055).png" alt=""><figcaption></figcaption></figure>

The next screen is displayed based on your commit process selection (prevalidate commit or commit only).

#### Step 3: Commit Settings <a href="#step-3-commit-settings" id="step-3-commit-settings"></a>

**A. For Validation of Changes (Before Commit)**

ARM allows performing a validation deployment before actually committing the changes.

1. Under the **`Validation Report`** section, you can:
   1. **`Generate Diff Report at current Head:`**&#x53;elect this option to auto-generate a code difference report upon commit completion.Important Note:In some scenarios, this option is selected by default. This usually occurs if you set the criteria for the commit process globally, which enables you to generate a Diff Report by default. Your commit criteria are under the **`My Account > Commit Validation - Approval Settings`** section. However, remember that once the criteria is set, the commit is automatically rejected if you deselect the **`Generate Diff Report`** checkbox.
   2. **`Run Static Code Analysis:`** You can initiate a [Static Code Analysis tool](https://www.autorabit.com/products/codescan/) to identify potential software quality issues before the code moves to production. Like **`Generate Diff Report at current HEAD`**, this option is auto-selected by default if the criteria are set globally (under the **`My Account > Commit Validation - Approval Settings`** section).
      *   For _ApexPMD_, _Checkmarx_, _CodeScan_, and _SonarQube_: ARM allows you to set the criteria for running the SCA tool, whether to run on all supported metadata types from the full source or to run on the newly added components:

          * **All Supported Metadata Types:** This option executes a comprehensive security analysis across all selected metadata components, irrespective of their creation or modification timestamps. This approach is recommended for complete security audits.
          * **Only Newly Added Supported Metadata Types:** This option performs a targeted analysis, focusing solely on metadata components created on a specific date. It is designed to evaluate recent additions efficiently.



          * Furthermore, for _CodeScan_ and _SonarQube_, ARM allows you to **`Select Baseline Branch`** from the drop-down list.

          <figure><img src="../../../../../.gitbook/assets/image (1056).png" alt=""><figcaption></figcaption></figure>

          <figure><img src="../../../../../.gitbook/assets/image (1057).png" alt="" width="375"><figcaption></figcaption></figure>
   3.  **`Validate Deployment:`** This feature allows you to validate code across multiple Salesforce orgs simultaneously, with independent Apex test class selection and skip member options for each org. \


       #### Selecting Salesforce Orgs for Validation

       * Click on the option to select Salesforce orgs for validation.
       * A dropdown will appear, displaying your available Salesforce orgs.
       * Choose up to 3 orgs by clicking the checkbox next to each desired org.

       #### Setting Apex Test Levels (Individual)

       * Select the option within each org section and locate the option to set the Apex test level.
       * Choose the desired test level (e.g., Class, Suite, Organization) for each org independently.

       #### Skip Members Option

       * The "Skip Members" checkbox will only be visible if any of the selected Salesforce orgs are configured to skip members during validation.
       * If enabled, you can choose to skip specific members from the validation process for each org where skipping is configured.

       #### Selecting Test Classes

       * You'll find a dedicated section for each chosen Salesforce org to select test classes. This section is labeled "Test Classes."
       * Within each org section, browse or search for the available test classes associated with that specific org.
       * To select the desired test classes for each org, click the checkbox next to each class you want to include in the validation.

       <figure><img src="../../../../../.gitbook/assets/image (1058).png" alt=""><figcaption></figcaption></figure>
2. Under the **`Validation Settings`**, users are prompted to enter the commit label, commit message (if any), and reviewer email ID(s) to send an email notification of the commit process performed and the difference reports. Additionally, there are various options you can configure:
   1. **`Commit WaveXMD Components:`** Upon selection, this checkbox allows you to choose the respective Wave XMD files belonging to the Wave dashboard metadata. This checkbox is hidden if the 'WaveDashboard' metadata type or its corresponding members are not picked.
   2. **`Commit Options for Profile:`** This option lets you choose to commit settings for a full profile operation.
      * **`Commit Access Settings for selected metadata (Profiles ONLY):`** This allows you to perform the commit operation based only on the profiles available for the selected metadata.
      * **`Commit Full Profiles:`** Commits the profiles irrespective of the selected Metadata.
   3. **`Commit Options for PermissionSets:`** This option allows you to choose to commit settings for permission set operation.
      * **`Commit Access Settings for selected metadata (PermissionSets ONLY):`** Commits the permission of the metadata members for permission set metadata you have worked on or modified.
   4. **`Remove IP Ranges:`** This removes the IP range from your profile/permissionsets when committing them.
   5. **`Remove User Permissions:`** This removes the user permissions from your profile or permissionsets when committing them. By default, it applies to profiles and not permissionsets.\
      \
      **Important Points to Note:**
      * Only if both the profile and permissionsets files are selected for commit will the **`Remove User Permissions`** checkbox appear.
      * By default, **`Remove User Permissions`** only applies to profiles, not permissionsets.
      * If you choose the **`Commit Options for PermissionSet`** option, the **`Remove User Permissions`** checkbox is accessible.
      * If you check the **`Remove User Permissions`** checkbox without selecting the **`Commit Options for PermissionSets`** checkbox, the Remove User Permissions only applies to profiles, not permissionsets.
   6. **`Ignore Missing Visibility Settings:`** With this option, differences in visibility settings between the source and destination orgs will not cause the deployment to fail. ARM will compare the source and destination orgs and keep only the common settings between both orgs.\
      \
      **Important Note:**\
      **Standard fields** are not supported for **Ignore Missing Visible Settings**.\

   7. **`Ignore installed components:`** When selected, ARM will scan for the components that are deployed, and if there are any managed package components located in the destination branch, these components will be excluded from the metadata.zip files when the remaining components are deployed.
3. **`Apply Search and Substitute Rules:`** If you created search and substitute rules to define custom find and replace rules which ARM applies whenever you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control, or vice-versa, that rule can be found here.

<figure><img src="../../../../../.gitbook/assets/image (1059).png" alt="" width="283"><figcaption></figcaption></figure>

4. Click **`Finish`**. View your recently created EZ-Commit in the [Commits](commits-summary.md) screen.

**B. For Commit Only (Without Validation)**

Directly commit to your Version Control System without extra validations. Different options to choose from include:

1. **`Commit WaveXMD Components:`** When selected, this checkbox allows you to choose the respective WaveXMD files belonging to the wave dashboard metadata type and commit them to the target branch. This checkbox is hidden if the **'WaveDashboard'** metadata type or its corresponding members are not picked.
2. **`Commit Options for Profile:`**&#x54;his option lets you choose to commit settings for a full profile operation.
   * **`Commit Access Settings for selected metadata(Profiles Only): This allows`** you to perform the commit operation based on the profiles available only for the selected metadata.
   * **`Commit Full Profiles:`** Commit the profiles irrespective of the selected metadata.
3. **`Commit Options For PermissionSets:`**&#x54;his option allows you to choose to commit settings for a permission set operation.
   * **`Commit Access Settings for selected metadata (PermissionSets Only):`** Commits the permissions of the metadata members for permission sets metadata you have worked on or modified.
4. **`Remove IP Ranges:`** This removes the IP range from your profile/permissionsets when committing them.
5. **`Remove User Permissions:`** This removes the user permissions from your profile or permissionsets when committing them. By default, it applies to profiles and not permissionsets.Important Point to Note:
   * The **`Remove User Permissions`** checkbox appears the profile and permissionsets files are selected for commit.
   * By default, **`Remove User Permissions`** only applies to profiles, not permissionsets.
   * If you choose the **`Commit Options for PermissionSet`** option, the **`Remove User Permissions`** checkbox will be accessible.
   * If you check the **`Remove User Permissions`** checkbox without selecting the **`Commit Options for PermissionSets`** checkbox, the Remove User Permissions will only apply to profiles, not permissionsets.
6. **`Apply Search and Substitute Rules:`** If you created search and substitute rules to define custom find and replace rules, which ARM applies when you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control, or vice-versa, that rule can be found here.
7. **`Commit Comment:`** Comment or add additional information, if any.
8. Click **`Finish`**. View your recently created EZ-Commit in the [Commits](commits-summary.md) screen.

<figure><img src="../../../../../.gitbook/assets/image (1060).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** For Non-DX Branches, if you wish to commit only the minimal metadata structure of a custom object, you can use the following XML template. This can be achieved by enabling the review artifact feature in AutoRABIT EZ-Commit. Use the inline IDE editor to adjust the XML as needed (ensure the XML is valid and remains deployable before committing).

**Sample Minimal XML Format for a Custom Object:**

\<?xml version="1.0" encoding="UTF-8"?>\
\<CustomObject xmlns="[http://soap.sforce.com/2006/04/metadata](http://soap.sforce.com/2006/04/metadata)">\
\<deploymentStatus>Deployed\</deploymentStatus>\
\<label>Book\</label>\
\<nameField>\
\<label>Book Name\</label>\
\<type>Text\</type>\
\</nameField>\
\<pluralLabel>Books\</pluralLabel>\
\<sharingModel>ReadWrite\</sharingModel>\
\</CustomObject>

If the same object already exists in the target branch or org and you attempt to edit it, you may encounter a "no modifications" popup. This approach is applicable only for creating brand-new objects.
{% endhint %}

