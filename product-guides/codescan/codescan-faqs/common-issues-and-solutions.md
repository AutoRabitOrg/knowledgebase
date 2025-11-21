# Common Issues and Solutions

## Common Issues

#### **Why is the Add & Run Scan tab grayed out?**

If a user does not have approval/permission to run a scan, when they try to add a project for analysis, the **Add & Run Scan** tab will be grayed out.

## Errors <a href="#error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml" id="error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml"></a>

#### Error: Project reports are not available for branches created outside the CodeScan Cloud.

For branches created outside the CodeScan Cloud, such as ARM, Flosum, or Copado, project reports are not yet accessible. Only the branch chosen during the initial integration setup with CodeScan Cloud can have reports fetched in CodeScan.&#x20;

Solution: In the Edit Project section, select “Attach Analysis Project,” and choose project type as “Webhook.” After this step, project reports will be accessible.

#### **Error: `Salesforce\force-app\main\default\applications\Chatter_Delete_Blocker.app-meta.xml` when writing a custom SonarQube rules using the Xpath Template rule for Salesforce Metadata (sfmeta:XPathRule)** <a href="#error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml" id="error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml"></a>

The analysis is looking for a match with a file name and the suffix entered in the field, but it cannot find any, which is why the above error is thrown. This is expected behavior because CodeScan cannot decide which rules to apply to the files. To remove file patterns listed for sonar.lang.patterns.xml, navigate to **`Project Settings > General Settings > Language.`**

#### **Error: `"Job took long. We will attempt to rerun with more memory."`**?

This error may occur when analyzing projects with very large amounts of metadata. It means the analysis job ran out of available memory.

1.  To resolve this issue:

    * Action Required: Please file a support ticket with the CodeScan support team.
    * Provide details about the project, including the project name and any relevant context about the size or complexity.
    * The support team will assist in increasing the memory allocation at the organization level to ensure your project can be analyzed successfully.

    If you continue to encounter this error after the memory has been increased, contact support for further troubleshooting.
2. Check for the rule **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`** in your default quality profile. If available, please deactivate it. Use the steps below:
   * Create a new quality profile for Apex language.
   * Deactivate the **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`** rule.
   * Set the newly created profile as **default**.

For detailed steps, please refer to [Customizing Quality Profiles](../quality-profiles/customizing-quality-profiles.md).

#### Error: Background Tasks Failing

This error either occurs if it’s out of memory or when multiple analyses have been triggered at the same time. The one triggered last gets completed first.

#### Error: Not Able to Download Code from SF in the Project Analysis Page

Check to see whether CodeScan is blocked in Salesforce (Setup > Connected Apps > CodeScan). If it's blocked, unblocked it. If it's already unblocked, yet you are still seeing the error, uninstall then reinstall, block it, and then unblock it.

#### Error(s): Expired Access/Refresh Token or Authentication Failure

Following a sandbox refresh, you may encounter issues scanning your environment. In most cases, an “expired access/refresh token” or “authentication failure” error shows under the Project Analysis tab.

To resolve these issues, simply reauthenticate your environment. Follow these steps:

1. Select Project -> Project Analysis tab
2.  Click Delete Analysis<br>

    <figure><img src="../../../.gitbook/assets/image (8) (1) (3).png" alt=""><figcaption><p>Delete Project Analysis</p></figcaption></figure>
3.  Make sure you DO NOT select the checkbox to Delete the Project Also (as you just want to reattach it while maintaining the same project and its history).

    <figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>DO NOT select the checkbox to Delete the Project Also</p></figcaption></figure>



{% hint style="danger" %}
Selecting the checkbox and deleting the entire project is irreversible and leads to the complete loss of historical analysis data.
{% endhint %}

4.  Then select Attach Analysis Project.<br>

    <figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>Attach Analysis Project</p></figcaption></figure>
5.  Select Salesforce.<br>

    <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>Choose Salesforce Analysis Project</p></figcaption></figure>
6.  It will redirect you to the authorization page. Enter your credentials.<br>

    <figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>Salesforce Credentials Authorization</p></figcaption></figure>


7. After successful authentication, you will be redirected to CodeScan, and a new analysis will kick off.

## Copado Integration <a href="#faqs" id="faqs"></a>

#### **Should the user add a new analysis project after the CodeScan-Copado integration is complete? If the user creates one, how does CodeScan understand it's the same project as the Copado connection?**

Adding a new analysis project is not required. The project in CodeScan is automatically created in Copado Integration using the organization key and security token provided by CodeScan.

#### **Why am I unable to see the results in CodeScan using the Copado integration?**

Check if the specific user has permission to access the 'Result Record' in Copado.

