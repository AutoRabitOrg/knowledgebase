# NewEmailServices

The **NewEmailServices** template allows users to configure new Email Service records in a Salesforce org via AutoRABIT's Environment Provisioning.

## Steps to Create the NewEmailServices Template

1. Log in to your AutoRABIT account.
2. Go to the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Navigate to the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Enter a **template name** and a **short description**.
6. Select the **NewEmailServices** checkbox under **Manage Email Services**.
7. Click **Add**.
8.  On the next screen, a **Test Case Name** appears by default.

    * Click the **Add** button to provide custom test data.
    * Fill in the required fields with appropriate values.
    * Click **Save**.

    ![New Email Services Test Case](<../../../../../../.gitbook/assets/image (77).png>)
9. Click **Save** again to save the template.
10. After saving, you'll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your selected destination org.
12. Choose your **destination org** from the dropdown and enter the **email address(es)** for deployment notifications.
13. In the **Post Deployment Steps**, select the test cases you recently created.
14. Review the **View History** page for a comprehensive summary of the deployment operation.
