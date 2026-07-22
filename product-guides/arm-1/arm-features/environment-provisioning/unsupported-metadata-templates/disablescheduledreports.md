# Disable Scheduled Reports

The **DisableScheduledReports** template allows users to delete scheduled report jobs from Salesforce using AutoRABIT.

## Steps to Create the Disable Scheduled Reports Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **DisableScheduledReports** checkbox under **Disable Scheduled Reports**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** is auto-generated.
   * Click **Add** to insert custom test data.
   * To define the scheduled report(s) for deletion:
     * Click the add icon (![Add Icon](<../../../../../.gitbook/assets/image (64).png>)).
     * Enter the report job in the **Job Name** field under **Deleting Schedule**.
     * To add multiple schedules, click the **+** symbol and repeat the steps above.
     * Click **OK**.
     * Click **Save** to save this page.
9. Click **Save** again to finalize the template.
10. Once saved, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** and enter **email address(es)** to receive execution notifications.
13. Under **Post Deployment Steps**, select the test cases you recently created.
14. Visit the **View History** page for a detailed summary report of the operation.
