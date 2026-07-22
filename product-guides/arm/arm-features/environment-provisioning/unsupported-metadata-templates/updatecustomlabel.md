# Update Custom Label

The **UpdateCustomLabel** template enables you to update existing custom label values within your Salesforce org via AutoRABIT.

## Steps to Create the Update Custom Label Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **UpdateCustomLabel** checkbox under **Update Custom Label**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** and **Custom Label Name** are auto-generated.
   - Click **Add** to insert custom test data.

9. To define additional custom label updates:
   - Click the edit icon ![Edit](../../../../../.gitbook/assets/image%20(1479).png).
   - Input values in the **Custom Label Name** and **New Value** fields.
   - To add multiple entries for the same test case, click the **+** symbol and repeat the process.
   - Click **OK**, then click **Save** to preserve the test case.

10. Click **Save** again to complete the template creation.

11. Upon successful save, you will be redirected to the **Environment Provisioning History** screen.
12. Click **Run** to execute the template in your destination org.
13. From the dropdown, select your **destination org** and enter the **email address(es)** for notifications.
14. In the **Post Deployment Steps**, choose the test cases you've created.
15. For a comprehensive report of the deployment, visit the **View History** page.
