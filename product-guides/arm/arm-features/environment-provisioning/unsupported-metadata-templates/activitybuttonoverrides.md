# ActivityButtonOverrides

The **ActivityButtonOverrides** template allows you to configure custom behavior for activity buttons using Visualforce pages in Salesforce via AutoRABIT.

## Steps to Create the ActivityButtonOverrides Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Open the **Create** [**Unsupported Metadata Template**](./) tab.
5. Provide a **template name** and a **short description**.
6. Select the **ActivityButtonOverrides** checkbox under **Activity Button Overrides**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will be automatically populated.
   - Click **Add** to input custom test data.
   - Fill in the following fields:
     - **Edit Standard Buttons and Links:** Enter the details for the standard buttons to override.
     - **Visualforce Page:** Specify the Visualforce page used for the override.
     - **Active Visualforce Page:** Check this box to activate the Visualforce override.
   - Click **Save** to save the configuration.

9. Click **Save** again to finalize the template.

10. After successful creation, you will be redirected to the [**Environment Provisioning**](../) **History** screen.
11. Click **Run** to execute the template on your destination org.
12. Choose your **destination org** and enter the **email address(es)** to receive notification upon completion.
13. In the **Post Deployment Steps**, select the test cases you created.
14. Review the **View History** page for a detailed summary of the deployment.
