# ComplianceBCCEmail

The **ComplianceBCCEmail** template enables automatic copying of all outgoing emails to a designated compliance email address in Salesforce using AutoRABIT.

## Steps to Create the ComplianceBCCEmail Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Select the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Check the **ComplianceBCCEmail** option under **Add Compliance BCC Email**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** is auto-generated.
   * Click **Add** to insert custom test data.
   * Fill in the **Compliance BCC Email** field with the desired email address.
   * Select the **Enable Email** checkbox to activate the BCC functionality.
   * Click **Save** to finalize this page.
9. Click **Save** again to complete the template creation.
10. After saving, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Choose your **destination org** and specify **email address(es)** to receive notifications upon completion.
13. Under **Post Deployment Steps**, select the test cases that you recently created.
14. Visit the **View History** page for a comprehensive summary of the execution.
