# Edit Lead

The **EditLead** template allows users to modify lead ownership and conversion settings in Salesforce using AutoRABIT.

## Steps to Create the Edit Lead Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **EditLead** checkbox under **Lead Settings**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** is auto-generated.
   * Click **Add** to insert custom test data.
   *   Fill in the following fields:

       * **Lead Type:** Specify a queue or user to assign the lead if assignment rules fail.
       * **Lead Owner:** Enter the designated lead owner.
       * **Lead Conversion Setting:** Click the configuration icon ![icon](<../../../../../.gitbook/assets/image (71).png>) to open the settings panel and configure:
         * **Require Validation for Converted Leads:** Enforces field-level validations, workflow actions, and triggers on conversion.
         * **Preserve Lead Status:** Retains the lead's original status instead of using the new owner’s default.
         * **Enable Conversions for Salesforce Mobile:** Allows lead conversion from the Salesforce mobile app.

       ![Lead Conversion Settings](<../../../../../.gitbook/assets/image (70).png>)
   * Activate the settings using the **Active** checkbox.
   * Click **Save** to finalize the data entry.
9. Click **Save** again to create the template.
10. You’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Choose your **destination org** and enter **email address(es)** for execution notifications.
13. In the **Post Deployment Steps**, select the test cases you created.
14. Visit the **View History** page for a comprehensive execution summary.
