# ReorderContactRoles

The **ReorderContactRoles** template is used to change the sequence of values in the list for Case Contact Roles in Salesforce.

## Steps to Create the ReorderContactRoles Template

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Click **Create New Template**.
4. Navigate to the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **ReorderContactRoles** checkbox under **Case Contact Roles**.
7. Click **Add**.
8. On the next screen:
   * A **Test Case Name** will appear by default.
   * Click **Add** to define your custom test data.
   * Configure the following fields:
     * **Values** – List the values to include.
     * **Default Value** – Specify the default selected value.
     * **Sort Alphabetically** – Enable to sort the list alphabetically.
   * Click **Save** to confirm.
9. Click **Save** again to finalize the template.
10. You will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Choose the **destination org** from the dropdown and provide **email address(es)** for notification.
13. In **Post-Deployment Steps**, select the test cases created.
14. Visit the **View History** page to review a detailed summary report of the operation.
