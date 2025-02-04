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

This error may occur for projects having huge metadata.

1. Increase the Project's Java heap memory size to analyze the project sources.&#x20;
   * On the CodeScan Project page, navigate to **`Project Settings > Project Analysis`**.
   * Click on the **`Edit Project`** button.
   * Update the **`Project Memory`** by selecting the required memory from the dropdown. _The memory size can be overridden and increased at the organization level._
2. Check for the rule **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`** in your default quality profile. If available, please deactivate it. Use the steps below:
   * Create a new quality profile for Apex language.
   * Deactivate the **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`** rule.
   * Set the newly created profile as **default**.

For detailed steps, please refer to [Customizing Quality Profiles](https://knowledgebase.autorabit.com/codescan/docs/customizing-quality-profiles).

#### Error: Background Tasks Failing

This error either occurs if it’s out of memory or when multiple analyses have been triggered at the same time. The one triggered last gets completed first.

#### Error: Not Able to Download Code from SF in the Project Analysis Page

Check to see whether CodeScan is blocked in Salesforce (Setup > Connected Apps > CodeScan). If it's blocked, unblocked it. If it's already unblocked, yet you are still seeing the error, uninstall then reinstall, block it, and then unblock it.

## Copado Integration <a href="#faqs" id="faqs"></a>

#### **Should the user add a new analysis project after the CodeScan-Copado integration is complete? If the user creates one, how does CodeScan understand it's the same project as the Copado connection?**

Adding a new analysis project is not required. The project in CodeScan is automatically created in Copado Integration using the organization key and security token provided by CodeScan.

#### **Why am I unable to see the results in CodeScan using the Copado integration?**

Check if the specific user has permission to access the 'Result Record' in Copado.

