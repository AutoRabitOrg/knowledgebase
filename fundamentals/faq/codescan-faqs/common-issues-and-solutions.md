# Common Issues and Solutions

## Errors <a href="#error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml" id="error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml"></a>

#### **Why am I getting the following error:&#x20;**_**Salesforce\force-app\main\default\applications\Chatter\_Delete\_Blocker.app-meta.xml**_**&#x20;when writing a custom SonarQube rules using the Xpath Template rule for Salesforce Metadata (sfmeta:XPathRule)?** <a href="#error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml" id="error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml"></a>

The analysis is looking for a match with a file name and the suffix entered in the field, but it cannot find any, which is why the above error is thrown. This is expected behavior because CodeScan cannot decide which rules to apply to the files. To remove file patterns listed for sonar.lang.patterns.xml, navigate to **`Project Settings > General Settings > Language.`**

#### **Why is my CodeScan analysis failing with the error&#x20;**_**`"Job took long. We will attempt to rerun with more memory."`**_?

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

#### 'Background Tasks Failing'

This error occurs either if it’s Out of Memory, or if multiple analysis has been triggered at the same time and the one which got triggered later gets completed before the first triggered analysis

#### **Why is the Add & Run Scan tab grayed out?**

If a user does not have approval/permission to run a scan, when they try to add a project for analysis, the **Add & Run Scan** tab will be grayed out.

#### Why am I getting the following error message: "Not Able to Download Code from SF in the Project Analysis Page"?

Check to see whether CodeScan is blocked in Salesforce (Setup > Connected Apps > CodeScan). If it's blocked, unblocked it. If it's already unblocked, yet you are still seeing the error, uninstall then reinstall, block it, and then unblock it.

## Copado Integration <a href="#faqs" id="faqs"></a>

#### **Should the user add a new analysis project after the CodeScan-Copado integration is complete? If the user creates one, how does CodeScan understand it's the same project as the Copado connection?**

Adding a new analysis project is not required. The project in CodeScan is automatically created in Copado Integration using the organization key and security token provided by CodeScan.

#### **Why am I unable to see the results in CodeScan using the Copado integration?**

Check if the specific user has permission to access the 'Result Record' in Copado.

