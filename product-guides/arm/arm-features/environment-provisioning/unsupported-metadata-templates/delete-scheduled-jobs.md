# Delete Scheduled Jobs

The **DeleteScheduledJobs** template enables users to remove scheduled jobs in Salesforce using AutoRABIT.

## Steps to Create the DeleteScheduledJobs Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **DeleteScheduledjobs** checkbox under **Delete Scheduled Jobs**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** is auto-generated.
   - Click **Add** to insert custom test data.

9. To include a **Report Name** for your test cases:
   - Click the ![Add Icon](../../../../../.gitbook/assets/image%20(59).png) icon.
   - Enter the report name in the **Report Name** field.
   - To add multiple reports for the same test case, click the **+** symbol and complete the additional fields.
   - Click **OK**, then **Save** to complete this step.

10. Click **Save** again to finalize the template creation.

11. After saving, you’ll be redirected to the **Environment Provisioning History** screen.
12. Click **Run** to execute the template on your destination org.
13. Choose your **destination org** and specify **email address(es)** to receive execution notifications.
14. In the **Post Deployment Steps**, select the test cases that were recently created.
15. Visit the **View History** page for a comprehensive summary of the execution.
