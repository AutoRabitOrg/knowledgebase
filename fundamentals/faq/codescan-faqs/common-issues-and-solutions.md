# Common Issues and Solutions

## Errors <a href="#error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml" id="error-salesforceforceappmaindefaultapplicationschatterdeleteblockerappmetaxml"></a>

1. **Why am I getting the following error:&#x20;**_**Salesforce\force-app\main\default\applications\Chatter\_Delete\_Blocker.app-meta.xml**_**&#x20;when writing a custom SonarQube rules using the Xpath Template rule for Salesforce Metadata (sfmeta:XPathRule)?**\
   The analysis is looking for a match with a file name and the suffix entered in the field, but it cannot find any, which is why the above error is thrown. This is expected behavior because CodeScan cannot decide which rules to apply to the files. To remove file patterns listed for sonar.lang.patterns.xml, navigate to **`Project Settings > General Settings > Language.`**
2.  **Why is my CodeScan analysis failing with the error&#x20;**_**`"Job took long. We will attempt to rerun with more memory."`**_**`?`**\
    This error may occur for projects having huge metadata.

    1. Increase the Project's Java heap memory size to analyze the project sources.&#x20;
       * On the CodeScan's Project page, navigate to **`Project Settings > Project Analysis`**.
       * Click on the **`Edit Project`** button.
       * Update the **`Project Memory`** by selecting the required memory from the dropdown. _The memory size can be overridden and increased at the organization level._
    2. Check for the rule **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`**&#x69;n your default quality profile. If available, please deactivate it. Use the steps mentioned below:
       * Create a new quality profile for Apex language.
       * Deactivate the **`"Avoid Cleartext Transmission of Sensitive Information in the default quality profile"`** rule.
       * Set the newly created profile as **default**.

    For detailed steps, please refer to [Customizing Quality Profiles](https://knowledgebase.autorabit.com/codescan/docs/customizing-quality-profiles).

## Copado Integration <a href="#faqs" id="faqs"></a>

1. **Should the user add a new analysis project after the CodeScan-Copado integration is complete? If the user creates one, how does CodeScan understand it's the same project as the Copado connection?**\
   Not required. The project in CodeScan is automatically created in Copado Integration using the organization key and security token provided by CodeScan.
2. **I am unable to see the results in CodeScan using the Copado integration.**\
   Check if the specific user has permission to access the 'Result Record' in Copado.

