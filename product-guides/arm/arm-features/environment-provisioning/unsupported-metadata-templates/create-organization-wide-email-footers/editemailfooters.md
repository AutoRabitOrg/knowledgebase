# EditEmailFooters

The **EditEmailFooters** template is used to modify existing organization-wide email footers within your Salesforce environment.

## Steps to Create the EditEmailFooters Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Open the [**Create Unsupported Metadata Template**](https://knowledgebase.autorabit.com/docs/unsupported-metadata-templates) tab.
5. Provide a **template name** and a **short description**.
6. Select the **EditEmailFooters** checkbox under **Create Organization-Wide Email Footers**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will appear by default.
   - Click **Add** to input custom test data.
   - Fill in the following fields:
     - **Edit Footer:** Enter the footer details you wish to edit.
     - **Name:** Specify the name of the footer.
     - **Active for Single Email:** Enable this option to activate the footer for single emails.
     - **Active for Mass Email:** Enable this option to activate the footer for mass emails.
     - **Email Encoding:** Provide the desired email encoding format.
     - **Text:** Add any additional footer content or comments.
   - Click **Save** once complete.

9. Click **Save** again to finalize the template.

10. Upon successful creation, you will be redirected to the [**Environment Provisioning History**](https://knowledgebase.autorabit.com/docs/environment-provisioning) screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** from the dropdown and provide **email address(es)** for notification.
13. In **Post Deployment Steps**, select the test cases you recently created.
14. For a complete summary of the operation, visit the **View History** page.
