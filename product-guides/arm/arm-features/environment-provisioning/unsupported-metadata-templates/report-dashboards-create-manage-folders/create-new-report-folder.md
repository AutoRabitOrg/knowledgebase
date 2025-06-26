# Create New Report Folder

The **CreateNewReportFolder** template is used to create new report folders within Salesforce through the Environment Provisioning module.

## Steps to Create the CreateNewReportFolder Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **name** and a **short description** for the template.
6. Select the **CreateNewReportFolder** checkbox under **Report Dashboards Create Manage Folders**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will appear by default.
   - Click **Add** to input custom test data.
   - Provide values for the **Report Folder Label** and **Folder Unique Name** fields.
   - Click **Save** to store the test case.

9. Click **Save** again to finalize and save the template.

10. After successful creation, you'll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on the target org.
12. Select your **destination org** from the dropdown and provide the **email address(es)** to receive status notifications.
13. Under **Post Deployment Steps**, choose the recently created test cases.
14. Visit the **View History** page for a detailed deployment summary.
