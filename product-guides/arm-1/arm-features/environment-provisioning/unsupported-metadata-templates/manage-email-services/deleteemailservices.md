# DeleteEmailServices

The **DeleteEmailServices** template allows you to remove specific fields from existing email service configurations in Salesforce.

## Steps to Create the DeleteEmailServices Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Open the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **DeleteEmailServices** checkbox under **Manage Email Services**.
7. Click **Add**.
8. On the next screen, a **Test Case Name** and **Fields To Delete** are auto-populated. To add custom test data, click **Add**.
9. To change field names for auto-generated or custom test cases:
   * Click the ![Edit Field Icon](<../../../../../../.gitbook/assets/image (75).png>) icon.
   * Enter the new field name in the provided text box.
   * To add multiple fields, click the **+** symbol and repeat the above steps.
   * Click **OK** once done.
   * Click **Save** to finalize the configuration for this test case.
10. Click **Save** again to store the template.
11. After successful creation, you will be redirected to the **Environment Provisioning History** screen.
12. Click **Run** to apply the template to your destination org.
13. Select your **destination org** from the dropdown list and provide **email address(es)** for notification purposes.
14. In the **Post Deployment Steps**, select the test cases recently created.
15. For a comprehensive summary of the executed operation, refer to the **View History** page.
