# Delete Time Based Workflow

The **TimeBasedWorkflow** template enables users to delete time-based workflow actions in Salesforce using AutoRABIT.

## Steps to Create the Delete Time-Based Workflow Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create** [**Unsupported Metadata Template**](../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Provide a **template name** and a **short description**.
6. Select the **TimeBasedWorkflow** checkbox under **Delete Time Based Workflow**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** is auto-generated.
   * Click **Add** to insert custom test data.
   *   Under the **Monitoring Queue**, enter the **Field Name**, **Operator Name**, and **Monitoring Value**, then click **OK**.

       ![Monitoring Queue](<../../../../../.gitbook/assets/image (62).png>)
   *   Under the **Record To Delete** section, enter the specific records to be deleted, then click **OK**.

       ![Record To Delete](<../../../../../.gitbook/assets/image (63).png>)
9. Click **Save** to save the test case.
10. Click **Save** again to finalize the template.
11. Once saved, you'll be redirected to the [**Environment Provisioning History**](https://knowledgebase.autorabit.com/docs/environment-provisioning) screen.
12. Click **Run** to execute the template on your destination org.
13. Choose your **destination org** and specify **email address(es)** to receive execution notifications.
14. Under **Post Deployment Steps**, select the test cases you recently created.
15. Visit the **View History** page for a detailed summary report of the execution.
