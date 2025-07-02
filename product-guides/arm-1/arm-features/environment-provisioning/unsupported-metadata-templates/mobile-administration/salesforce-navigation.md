# Salesforce Navigation

The **SalesforceNavigation** template allows you to configure mobile navigation menu items within Salesforce using AutoRABIT’s Environment Provisioning.

## Steps to Create the SalesforceNavigation Template

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Click **Create New Template**.
4. Navigate to the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Provide a **template name** and a **short description**.
6. Select the **SalesforceNavigation** checkbox under **Mobile Administration**.
7. Click **Add**.
8.  On the next screen:

    * A **Test Case Name**, **Object Name**, and **Navigation Menu Items** appear by default.
    * Click **Add** to define custom test data and enter values for the available fields.

    ![Salesforce Navigation Setup](<../../../../../../.gitbook/assets/image (86).png>)

    * To add additional menu items:
      * Click the edit icon ![Edit Icon](<../../../../../../.gitbook/assets/image (87).png>)
      * Enter names such as **Task** or **People** into the **Available Member** field.
      * Use the **Add/Remove** checkboxes to control their activation.
      * To add multiple items, click the **+** symbol and repeat the above steps.
      * Click **OK**, then click **Save** to finalize the test case.
9. Click **Save** again to store the template.
10. Upon successful creation, you will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** from the dropdown and provide **email address(es)** for notifications.
13. In the **Post Deployment Steps**, select the test cases you created.
14. Refer to the **View History** page for a detailed summary of the provisioning operation.
