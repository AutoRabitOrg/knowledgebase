# Manage Libraries

The **Libraries** template in AutoRABIT allows users to manage Salesforce content libraries by configuring filters, permissions, and membership settings.

## Steps to Create the Manage Libraries Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **Libraries** checkbox under **Manage Libraries**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** and **My Libraries** section will appear by default.
   - Click **Add** to enter custom test data.
   - Click the icon to open the library configuration dialog.
   - Provide values for:
     - **Libraries**
     - **Filter**
     - **Members**
     - **Permission settings**
   - Enable the **Add** checkbox to activate the settings.
   - To include multiple library configurations, click the **+** symbol and repeat the steps.
   - Click **OK**, then **Save** to finalize the test data.

   ![Library Configuration Example](../../../../../.gitbook/assets/image%20(78).png)

9. Click **Save** to save the template.

10. Once saved, you will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** and enter **email address(es)** for notification upon execution.
13. Under **Post Deployment Steps**, choose the test cases you have recently created.
14. Refer to the **View History** page for a complete summary of the operation.
