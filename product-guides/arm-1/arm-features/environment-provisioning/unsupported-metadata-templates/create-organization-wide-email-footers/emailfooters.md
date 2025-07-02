# EmailFooters

The **EmailFooters** template allows you to create organization-wide email footers used in messages sent from Salesforce.

## Steps to Create the EmailFooters Template

1. Log in to your AutoRABIT account.
2. Go to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Navigate to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **EmailFooters** checkbox under **Create Organization-Wide Email Footers**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** will be generated automatically.
   * Click **Add** to input custom test data.
   * Fill in the following fields:
     * **Name:** Enter the name for the email footer.
     * **Active for Single Email:** Check to activate for single email messages.
     * **Active for Mass Email:** Check to activate for bulk/mass emails.
     * **Email Encoding:** Specify the encoding (e.g., UTF-8).
     * **Text:** Add any footer message or custom note.
   * Click **Save** when complete.
9. Click **Save** again to finalize the template.
10. Once the template is created, you will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** from the dropdown and provide **email address(es)** for notifications.
13. Under **Post Deployment Steps**, select the recently created test cases.
14. For a detailed report of the deployment, visit the **View History** page.
