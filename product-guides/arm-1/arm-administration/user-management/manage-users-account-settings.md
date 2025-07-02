# Managing User Account Settings

{% hint style="info" %}
**Important Note:** This article is for the **Org Administrator** in particular. The actions discussed in this article will not be available to general users.
{% endhint %}

You can create, edit, and view user account details as an Org administrator. Admins can view their account details too.

### View User Account <a href="#view-user-account" id="view-user-account"></a>

* Hover your mouse over the **`Admin`** tile and select **`My Account`**.

<figure><img src="../../../../.gitbook/assets/image (579).png" alt="" width="243"><figcaption></figcaption></figure>

* The **`My Account`** page appears. You’ll then be presented with a screen divided into different sections, as depicted below:

<figure><img src="../../../../.gitbook/assets/image (580).png" alt=""><figcaption></figcaption></figure>

#### 1. Account Contact Details (Read only) <a href="#id-1-account-contact-details-read-only" id="id-1-account-contact-details-read-only"></a>

**`The Account Contact Details`** section contains your account's primary information and your subscription period with ARM.

<figure><img src="../../../../.gitbook/assets/image (581).png" alt=""><figcaption></figcaption></figure>

#### 2. Subscription Type (Read only) <a href="#id-2-subscription-type-read-only" id="id-2-subscription-type-read-only"></a>

**`Subscription Types`** are set up to match your organization's requirements. View the current subscription type and list of modules granted by ARM based on your subscription. Click on **`View Models`** to view the complete subscription model.

<figure><img src="../../../../.gitbook/assets/image (582).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (583).png" alt="" width="563"><figcaption></figcaption></figure>

#### 3. SSO Configuration <a href="#id-3-sso-configuration" id="id-3-sso-configuration"></a>

**Single Sign-On (SSO)** is an authentication process that allows a user to access multiple applications with only one set of credentials. ARM uses the secure and widely adopted industry-standard **Security Assertion Markup Language 2.0 (SAML 2.0)**, which means our implementation of SSO integrates easily with any large identity provider that supports SAML 2.0.

SAML-based SSO enables two-way communication between an authentication server (the Identity Provider) and an application (the Service Provider). So, your account must be set up to declare who will be the authentication server and how the communication must work.

Using the information you gathered from your IdP (the Identity Provider), fill in the below details:

* **`Entity ID:`** String that uniquely identifies your IdP (your IdP generally provides it).&#x20;
* **`Uploaded File Name:`** You must upload the XML file generated from IdP. (For more information, please refer to the Integration section on[ SSO](../../../arm/integration-and-plugins/sso/).
* **`Disable login with ARM credentials:`** When selected, passwords on ARM are no longer used once the SSO is activated. The system forces you and your sub-users to log in via SSO rather than entering their username and password on the login page. However, once disabled, all the authentication requests will go through the classic login interface.

<figure><img src="../../../../.gitbook/assets/image (584).png" alt="" width="563"><figcaption></figcaption></figure>

* How to override single sign-on (SSO)?Sub-users registered to that organization cannot log in to the ARM application using the standard (username + password) approach if the **`Disable login with AutoRABIT credentials`** checkbox is selected. If the org admin wants to override the **`SSO configuration`** for an individual user or group of users, he can do so under the **`Admin > Users`** section. Uncheck the **`Enforce SSO`** boxes after selecting the users from the list. Save the **`SSO Configuration`** by clicking **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (585).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** When the **`Disable login with AutoRABIT credentials`** option is selected, the **`Enforce SSO`** checkboxes are automatically checked for all the users.
{% endhint %}

#### 4. Mail Extensions <a href="#id-4-mail-extensions" id="id-4-mail-extensions"></a>

The admin can add different mail extensions based on the organization's requirements in this section.

<figure><img src="../../../../.gitbook/assets/image (586).png" alt="" width="563"><figcaption></figcaption></figure>

This allows new users to sign up for the ARM account by giving their mail extensions.

<figure><img src="../../../../.gitbook/assets/image (587).png" alt="" width="563"><figcaption></figcaption></figure>

#### 5. Plugins <a href="#id-5-plugins" id="id-5-plugins"></a>

This section lists various plugins that are configured in ARM. Based on the organization's requirements, admins can select the desired plugins to be used and register by giving the correct credentials.&#x20;

In addition to this, the admin can select the desired browsers to execute the selenium test cases. Selenium cannot automate desktop applications; it can only be used in browsers.&#x20;

Browsers Supported:

* Google Chrome 12+&#x20;
* Internet Explorer 7+&#x20;
* Firefox 3+

<figure><img src="../../../../.gitbook/assets/image (588).png" alt=""><figcaption></figcaption></figure>

#### 6. Configure Default SCA Baseline Branches <a href="#id-6-configure-default-sca-baseline-branches" id="id-6-configure-default-sca-baseline-branches"></a>

Developers must select the appropriate baseline branch to compare against. If they don't, a new branch will be created, which causes problems.

Admins can configure the default baseline branches for CodeScan and SonarQube SCA plugins in the **`My Account`** section. This resolves the confusion developers previously faced when selecting baseline branches for SCA and. It also helps Admins control the default baseline branches.

<figure><img src="../../../../.gitbook/assets/image (589).png" alt=""><figcaption></figcaption></figure>

**Configure the baseline branches**

* Select **`CodeScan`** or **`SonarQube`**.
* **`Select Project`** from the dropdown list.
* Click on the **`Select Default Branch`** field to display the available branches within the selected project, then click on the branch name from the list. You can choose multiple branches for each project. These branches are available for a developer to choose from during EZ-Commit.
* Other options:
  1. Click the ![](<../../../../.gitbook/assets/image (590).png>) icon to add a project.
  2. Click the![](<../../../../.gitbook/assets/image (591).png>)icon to remove a branch from a project.
  3. Click the![](<../../../../.gitbook/assets/image (592).png>)icon to delete the project completely.
* Click **`Save`** after selecting, adding, or deleting the required projects and corresponding branches.

#### 7. Validation Criteria- Static Code Analysis <a href="#id-7-validation-criteria-static-code-analysis" id="id-7-validation-criteria-static-code-analysis"></a>

With the current release, users can set the global criteria to enforce **`Static Code Analysis (SCA)`** tools across CI jobs and merge jobs. Based on the priority set, the build will be successful only if the criteria are met. The build will only succeed if the **Apex Classes**, **Triggers**, and **Visualforce** pages pass the priority set.

<figure><img src="../../../../.gitbook/assets/image (593).png" alt="" width="563"><figcaption></figcaption></figure>

#### 8. Commit Validation - Approval Settings <a href="#id-8-commit-validation-approval-settings" id="id-8-commit-validation-approval-settings"></a>

Here the admin can specify specific evaluation criteria for which the commit will get reviewed before being committed to the version control branch.

<figure><img src="../../../../.gitbook/assets/image (594).png" alt=""><figcaption></figcaption></figure>

**Auto reject commit after XX days**

Auto rejects an approval for pre-validation commit after the days mentioned here.&#x20;

**Enable criteria-based Review Process**

Select the **`Enable criteria based Review Process`** checkbox to enable the commit criteria.

<figure><img src="../../../../.gitbook/assets/image (595).png" alt=""><figcaption></figcaption></figure>

Next, choose the approval criteria based on your requirement:&#x20;

* **`Enable file comparison reports:`** When selected, this generates a code difference report upon completion of the commit operation.
*   **`Should pass validation criteria for Static Code Analysis:`** Select this option if you would like to run a static code analysis tool to identify potential software quality issues before the code moves to production.

    * Select the SCA tool according to your requirements.

    <figure><img src="../../../../.gitbook/assets/image (596).png" alt="" width="430"><figcaption></figcaption></figure>
* Select the **`Auto reject commit process if the criteria are not met`** checkbox to auto-reject the commit if the set criteria are not met.
* **`Auto approve on commit validation success:`** If all the criteria selected under **`Enable criteria based Review Process`** are successfully validated, selecting this checkbox will automatically approve the commit.

{% hint style="info" %}
**Important Note:** The user can set the commit validation criteria under the **`Validation Criteria- Static Code Analysis`** section on the **`My Account`** page.
{% endhint %}

**Auto commit on Approval**

Once the reviewer has approved the changes, or if you have opted to auto-approve upon successful validation, the commit process is automatically pushed to the destination branch.

<figure><img src="../../../../.gitbook/assets/image (597).png" alt=""><figcaption></figcaption></figure>

#### Deployment - Approval Settings

Admins are now able to configure the approvals process for the custom deployment module.&#x20;

1. By Admin → My Profile -> Deployment Approval Settings.
2.  Select the Salesforce Org from the drop-down menu, which requires approval before deployment. (This menu provides a list of Orgs that you have already configured in SF Org MGMT.)\


    <figure><img src="../../../../.gitbook/assets/image (1696).png" alt=""><figcaption><p>Deployment - Approval Settings</p></figcaption></figure>

    You can also configure the approval process for multiple Orgs.
3. Click on the drop-down menu to select the approvers for Level 1 and Level 2. The list will contain only users who can access the deployment module.\
   \
   Note : The App doesn't allow you to select the same approvers for Level 1 and Level 2.\

4. Click on Save to enable the approval process for deployments.

#### 9. Merge Settings <a href="#id-9-merge-settings" id="id-9-merge-settings"></a>

Here the administrator can specify specific evaluation criteria on which the merge will be reviewed before committing to the version control branch. The New Merge screen reflects the same option based on the criteria selected.

Select the **`Enable criteria based Review Process`** checkbox to enable the merge setting.

<figure><img src="../../../../.gitbook/assets/image (598).png" alt="" width="465"><figcaption></figcaption></figure>

**Merge Criteria**

* **`Enable file comparison reports:`** When selected, this generates a code difference report on completion of the merge operation.
* **`Should pass validation criteria for Static Code Analysis:`** Select this checkbox to run one or more SCA tools to identify potential software quality issues before the code moves to production.
* **`Should pass mock Deployment:`** This allows the users to perform a validation deployment before committing the changes. If the deployment is successful, the commit is executed. This option only permits the merge operation to proceed if the deployment is successfully validated. Here, you need to specify the code coverage percentage, beyond which allows proceeding for validation deployment, or else the deployment fails.What is a Code Coverage Report?The code coverage report details the apex tests run, the classes covered, and the failed assertions. It also provides a percentage of the code covered by the test execution.
* **`Disable Merge Self Approval:`** This option allows the Admin to prevent users who have committed to a merge request from approving it.
* **`Auto commit on Approval:`** This option allows developers to work on their feature branches, and after review (approval), it gets automatically committed to the trunk. View the commit revision information when you click the Revisions link.
* **`Enable Merge Approver:`** Enables the pprover to perform enforced code review by requiring specified people to approve a merge request before it can be unblocked for merging. Please set the number of necessary approvers before open merge requests can be merged under the **`Approval Levels`** drop-down box. The minimum approval level can be 1.
* **`Auto approve on merge validation success:`** If all the criteria selected under **`Enable criteria based Review Process`** are successfully validated, selecting this checkbox will automatically approve the merge. The merge will appear to have been approved by ARM. If the user has selected multiple approver levels, both levels will automatically be approved upon successful validation.
* **`Notify All Criteria Overwrites To:`** The email address(es) specified here will receive an overwrite email notification every time the user tries to overwrite the evaluation criteria set in the **`Merge Settings`** section and tries to merge the files to a branch.

#### 10. Salesforce Settings <a href="#id-10-salesforce-settings" id="id-10-salesforce-settings"></a>

ARM supports all the metadata types based on the **`Salesforce API Version`**. ARM now supports the Salesforce API **64.0** version, which means it can support any Salesforce standard or custom objects that require Salesforce API version 64. The newly supported Salesforce objects for each API version can be found [here](../../../arm/arm-administration/user-management/salesforce-api-version.md).

Select the API version to see the supported metadata types and avoid errors while accessing Salesforce orgs in Version Control, CI Jobs, Deployment, or SFDX modules.\


<figure><img src="../../../../.gitbook/assets/image (1687).png" alt=""><figcaption></figcaption></figure>

1. **`Configuration for recordTypes picklistValues:`** This topic is covered separately. [Click here](https://knowledgebase.autorabit.com/product-guides/arm/troubleshoot/how-tos/configure-record-types-picklist-values) to go directly to the mentioned topic.&#x20;
2. **`Configuration for Translations:`** Options to choose the configuration for the LabelTranslations, i.e., either replace or append. When selecting the _Replace_ option for the Configuration for LabelTranslations option for every EZ-commit operation, if the Label Translation has no custom label metadata type, it will override the LabelTranslations in Version Control, even if it has more than one custom label metadata type value. For the _Append_ option, instead of overriding the custom label metadata types, it keeps adding to the existing one.
3.  **`Configuration for running delta on RecordType Picklist values:`** On selection, this allows you to check delta on RecordType Picklist values during a Deployment.\


    <figure><img src="../../../../.gitbook/assets/image (1583).png" alt=""><figcaption></figcaption></figure>
4.  **Packaging and Deployment Settings:** Several options can be configured in this section:&#x20;

    1. **Manageable States**: In Salesforce, the `ManageableState` attribute indicates the status of a component within a package, reflecting its lifecycle stage and editability. The possible states are:
       * **Beta**: The component is in a managed package version marked as beta, suitable for testing but not for production use.
       * **Released**: The component is in a managed package version officially released for production use.
       * **Deleted**: The component has been deleted from the package.
       * **Deprecated**: The component is marked as deprecated, indicating it's outdated or should no longer be used.
       * **Unmanaged**: The component isn't part of a managed package, allowing full editing and deletion.
       * **Installed**: The component is part of a managed package installed in a subscriber's org, and it can't be edited or deleted by the subscriber.
       * **InstalledEditable**: The component is part of an installed managed package but can be edited by the subscriber.
       * **DeprecatedEditable**: The component is deprecated but remains editable.



    <figure><img src="../../../../.gitbook/assets/image (1578).png" alt=""><figcaption></figcaption></figure>

    &#x62;**. Include Default Apex Tests For Run Tests Based On Changes**: When selected, the default configured tests are added to the set, even if Test classes or Apex Class Apex Triggers are unavailable. Apex Test Level executes as _RunSpecifiedTests_. However, if the checkbox is unchecked, no default tests are added, and no Apex Test Level is set. Salesforce default behavior is expected in such cases.

    c. **`Enable Delta on PermissionSets:`** Per the Salesforce behavior, for _Salesforce API 40 or later_, all PermissionSets are replaced with the latest changes. However, when the _Enable Delta on PermissionSets_ checkbox is selected, the PermissionSets are retrieved from the source org and will append with the latest changes in the deployment package.

    d. **`Include/Exclude Metadata Types`**: Be sure to exclude them to avoid retrieving unwanted metadata types during the deployment or merge.

<figure><img src="../../../../.gitbook/assets/image (1580).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**&#x20;

Enabling the **`Configuration for running delta on RecordType Picklist values`** checkbox may lead to more time for the build. If you deselect it, your build cycles will be shorter.
{% endhint %}



**Rollback Settings**

Ensure you exclude them to avoid retrieving unwanted metadata types during deployment or commits rollback.

<figure><img src="../../../../.gitbook/assets/image (601).png" alt="" width="540"><figcaption></figcaption></figure>

**Profile/PermissionSets Settings**

This section pertains to granting or revoking permissions to the **`Profiles/PermissionSets`** of any org. Based on the permission granted or revoked, the same is affected after committing the custom object in the Version Control.

<figure><img src="../../../../.gitbook/assets/image (602).png" alt="" width="563"><figcaption></figcaption></figure>

**What is a Profile?**

Profiles define how users access objects and data and what they can do within the application. When you create users, you assign a profile to each one.

**What are Permission Sets?**

A permission set is a collection of settings and permissions that give users access to various tools and functions. Users can have only one profile, but they can have multiple permission sets. You can assign permission sets to different users, regardless of their profiles.

**Create a Profile or Permission Set permissions**

Create permission sets to grant access among logical groupings of users, regardless of their primary job function. For example, if you have an Inventory custom object in your org. Many users need **Read** access to this object, and fewer users need **Edit** access. You can create a permission set that grants **Read** access and assign it to the appropriate users. You can then create another permission set that gives **Edit** access to the Inventory object and assign it to the other group of users.

1. Click the **`New`** button.
2. Select the **`Salesforce Org`**.
3. Click either **`Get Profiles`** or **`Get PermissionSets`**.
   * **`Get Profiles`** will fetch all the profiles available in selected Salesforce Orgs.
   * **`Get PermissionSets`** will list all permission sets available in Salesforce Orgs.
4. Based on the above selection, choose either the **`Profile`** or **`Permission`** from the list.
5. Next, grant or revoke the permissions for the selected Profiles/Permission Sets.

**Additional configuration for "Field Permissions" and "Object Permissions" settings**

**Field Permissions** represent the field-level permission for users assigned to a profile.

| Field Name | Description                                                     |
| ---------- | --------------------------------------------------------------- |
| Editable   | Indicates whether this field is editable (true) or not (false). |
| Readable   | Indicates whether this field is readable (true) or not (false). |

**Object Permissions** represent a user's access to custom objects.&#x20;

| Field Name       | Description                                                                                                                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| allowCreate      | Indicates whether the object referenced by the object field can be created by the users assigned to this profile (true) or not (false).                                                                     |
| allowDelete      | Indicates whether the object referenced by the object field can be deleted by the users assigned to this profile (true) or not (false).                                                                     |
| allowEdit        | Indicates whether the object referenced by the object field can be edited by the users assigned to this profile (true) or not (false).                                                                      |
| allowRead        | Indicates whether the object referenced by the object field can be seen by the users assigned to this profile (true) or not (false).                                                                        |
| modifyAllRecords | Indicates whether the object referenced by the object field can be read, edited, or deleted by the users assigned to this profile (true) or not (false), regardless of the sharing settings for the object. |
| viewAllRecords   | Indicates whether the object referenced by the object field can be read by the users assigned to this profile (true) or not (false), regardless of the sharing settings for the object.                     |



#### 11. Vlocity Configuration Settings <a href="#id-11-vlocity-configuration-settings" id="id-11-vlocity-configuration-settings"></a>

Vlocity integration with ARM allows you to retrieve and deploy Vlocity metadata in the same way as for the Salesforce metadata, and commit the changes either to the repository or to a Version control branch.

Vlocity Version Supported: v1.17.1

**Integrate Vlocity as a plugin in ARM**

1. In the **`Vlocity Configuration Settings`** section, select the **`Enable Vlocity`** checkbox.
2.  Next, you must select the various parameters required to integrate Vlocity with ARM:

    * **`Compile On Build:`** When selected or set to true, the _compileonbuild_ code is modified in the YAML file, and the same gets committed to your Version Control branch during the EZ-Commit process. When you're trying to deploy to a Salesforce org using the above-configured branch, the compilation will take place before the deployment begins. **However, ARM recommends that you keep this checkbox unselected.** This is because the Vlocity tool throws compilation errors when you're trying to deploy the data that doesn't have dependent components when **`Compile On Build`** is checked.
    * **`Auto Update Settings:`** This option ensures you have the latest Data Pack settings before each export and deployment. This check is quick, and we recommend that you allow it.
    * **`Separate Matrix Versions:`** Add the ability to export matrix versions separately.
    * **`Local Compilation:`** To perform a local compilation of **`FlexCard`** and **`OmniScript`** metadata types, select this checkbox and enter the **`Access Key`** of Vlocity's private NPM repository to load the OmniStudio LWC compiler and deploy the compiled objects.\
      NoteIf you do not have the NPM repository Access Key, you can request one from your Vlocity customer representative at [_https://repo.vlocity.com/repository/vlocity-public/_](https://repo.vlocity.com/repository/vlocity-public/), by filing a support case with the subject **Request for Access Key to Vlocity's Private NPM Repository**.
    * **`MaxDepth:`** MaxDepth decides the level of dependencies that will be executed while fetching and committing vlocity components. By default, MaxDepth is set to **`-1`**.
      1. When MaxDepth Values is set to **`-1`** means, it will execute all-level dependencies of selected data pack record
      2. When MaxDepth Values is set to **`0`** means, it will execute only selected data pack record and
      3. When MaxDepth Values is set to **`1`** means, it will execute only first-level dependencies of the selected data pack record.
    * **`Data Pack Types:`** This gives you an option to choose your specific Vlocity components that will be committed to your destination org/branch.

    <figure><img src="../../../../.gitbook/assets/image (603).png" alt=""><figcaption></figcaption></figure>
3. Click **`Save`**.

#### 12. Session Settings <a href="#id-12-session-settings" id="id-12-session-settings"></a>

After logging in, a user establishes a session with the ARM platform. As an admin, you can control when an inactive user session expires. The default session timeout is 30 mins of inactivity. When the session timeout is reached, users are prompted with a dialog that allows them to log out or continue working.

<figure><img src="../../../../.gitbook/assets/image (604).png" alt="" width="374"><figcaption></figcaption></figure>

#### 13. Retention Policy <a href="#id-13-retention-policy" id="id-13-retention-policy"></a>

In this section, the admin can define the period for which data is retained by ARM in the history tables.&#x20;

Clearing historical and irrelevant data from the database helps prevent the application from lagging, resulting in better performance in all modules. The default retention period is set as **`12 months`**. Data older than 12 months will be automatically cleaned. Admins can later change it to **`6 months`** or **`3 months`**.

<figure><img src="../../../../.gitbook/assets/image (605).png" alt=""><figcaption></figcaption></figure>

This is applicable to the historical data on the following pages:

1. Deployment history
2. CI Job History
3. Org Sync History
4. Commits page
   * EZ-Commits history
   * Prevalidation commits history
   * Reverted commits history
   * Merges history
   * Prevalidation merge history
5. Merge Requests history
6. External Pull Requests page
7. Branching baseline page
8. Change the Labels page
   * Commit Labels
   * Release Labels
   * ALM Labels

{% hint style="info" %}
**Important Note:** The clean-up of the historical data will run every Saturday. To access any historical data that has already been cleaned up, contact us at **support@autorabit.com**, and we will provide the data in a CSV file format. Deleted data cannot be restored to the application.
{% endhint %}
