# Share Settings

The **ShareSettings** template allows you to configure sharing settings for report and dashboard folders in Salesforce via AutoRABIT's Environment Provisioning module.

## Steps to Create the ShareSettings Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Provide a **name** and a **short description** for the template.
6. Select the **ShareSettings** checkbox under **Report Dashboards Create Manage Folders**.
7. Click **Add**.
8.  On the next screen:

    * A **Test Case Name** appears automatically by default.
    * Click **Add** to input custom test data.
    * Enter the required values in the fields displayed.
    * Click **Save** to confirm the data.

    ![Share Settings Configuration](<../../../../../../.gitbook/assets/image (33) (1).png>)
9. Click **Save** to save the template.
10. After the template is successfully created, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to deploy the template to the selected destination org.
12. Select your **destination org** from the dropdown menu and enter the **email address(es)** to receive notifications.
13. Under **Post Deployment Steps**, select the recently created test cases.
14. Visit the **View History** page to review the detailed operation summary.
