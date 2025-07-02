# DelegatedAdministrationNew

The **DelegatedAdministrationNew** template allows you to create new delegated administration groups within a Salesforce org using AutoRABIT.

To create this template, follow the steps below:

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Navigate to the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Enter a **template name** and a **short description**.
6. Select the **DelegatedAdministrationNew** checkbox under **Delegated Administration**.
7. Click **Add**.
8. On the next screen, a **Test Case Name** appears by default. Click **Add** to enter custom test data. Provide the following details:
   * **Delegated Group Name:** Enter the name of the delegated group.
   * **Developer Name:** Specify the developer responsible for the action.
9. Click **Save** to store the test data.
10. Click **Save** again to finalize and create the template.
11. Upon successful creation, you’ll be redirected to the **Environment Provisioning History** screen.
12. Click the **Run** button to execute the template in your destination org.
13. Select your **destination org** from the dropdown and enter **email address(es)** to receive notifications.
14. In the **Post Deployment Steps**, select the test cases you recently created.
15. To view a detailed summary report of the executed operation, go to the **View History** page.
