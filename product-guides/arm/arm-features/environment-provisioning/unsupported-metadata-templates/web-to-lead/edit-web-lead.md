# Edit Web Lead

The **EditWebLead** template allows you to configure or update Web-to-Lead settings in your Salesforce org via AutoRABIT's Environment Provisioning module.

## Steps to Create the EditWebLead Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Open the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **EditWebLead** checkbox under **Web to Lead**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will be displayed by default.
   - Click **Add** to input custom test data.
   - Fill in the following fields:
     - **Enabled:** Enable Web-to-Lead functionality for your organization.
     - **Default Lead Creator:** Specify the username that will be assigned as the creator of online leads.
     - **Default Response Template:** Provide a default email template to be used if no auto-response rule is matched.
   - Click **Save** to save the configuration.

   ![Edit Web Lead Settings](../../../../../../.gitbook/assets/image%20(1481).png)

9. Click **Save** again to finalize the template.

10. You will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** and enter the **email address(es)** to receive run notifications.
13. In the **Post Deployment Steps**, select the test cases you created.
14. Visit the **View History** page to review a detailed summary of the operation.
