# DelegatedAdministrationEdit

The **DelegatedAdministrationEdit** template allows editing delegated administration settings in a Salesforce org via AutoRABIT.

To create this template, follow the steps below:

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Navigate to the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **DelegatedAdministrationEdit** checkbox under **Delegated Administration**.
7. Click **Add**.
8. On the next screen, a **Test Case Name** appears by default. Click **Add** to provide custom test data. Fill in the required fields:
    - **Delegated Group Name To Edit:** Specify the group name that is permitted to edit.
    - **Delegated Group Name:** Enter the name of the delegated group.
    - **Developer Name:** Enter the developer’s name performing the action.
9. Click **Save** to store the test data configuration.
10. Click **Save** again to finalize and create the template.
11. Upon successful creation, you’ll be redirected to the **Environment Provisioning History** screen.
12. Click the **Run** button to execute the template in your destination org.
13. Select your **destination org** from the dropdown and input **email address(es)** for notification.
14. In the **Post Deployment Steps**, select the recently created test cases.
15. To review detailed operation results, go to the **View History** page.
