# Delete Outbound Messages

The **OutboundMessages** template enables users to delete existing outbound messages in Salesforce using AutoRABIT.

## Steps to Create the OutboundMessages Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **OutboundMessages** checkbox under **Delete Outbound Messages**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** is auto-generated.
   * Click **Add** to insert custom test data.
9. To add more outbound messages to your test case:
   * Click the ![Add Icon](<../../../../../.gitbook/assets/image (58).png>) icon.
   * In the **Delete Outbound Message** field, enter the name of the message you want to delete.
   * To add multiple messages for the same test case, click the **+** symbol and complete the additional fields.
   * Click **OK** and then **Save** to complete this step.
10. Click **Save** to finalize the template creation.
11. After saving, you’ll be redirected to the **Environment Provisioning History** screen.
12. Click **Run** to execute the template on your destination org.
13. Choose your **destination org** and provide **email address(es)** to receive execution notifications.
14. In the **Post Deployment Steps**, select the test cases that were recently created.
15. Visit the **View History** page for a detailed summary report of the operation.
