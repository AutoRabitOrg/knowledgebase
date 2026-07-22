# Salesforce Offline

The **SalesforceOffline** template allows the configuration of offline settings for Salesforce Mobile applications using AutoRABIT’s Environment Provisioning module.

## Steps to Create the SalesforceOffline Template

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Click **Create New Template**.
4. Navigate to the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Provide a **template name** and a **short description**.
6. Select the **SalesforceOffline** checkbox under **Mobile Administration**.
7. Click **Add**.
8.  On the next screen:

    * A **Test Case Name**, **Object Name**, and **Offline Settings** appear by default.
    * Click **Add** to input custom test data.

    ![Salesforce Offline Setup](<../../../../../../.gitbook/assets/image (89).png>)

    * To add more settings:
      * Click the edit icon ![Edit Icon](<../../../../../../.gitbook/assets/image (90).png>)
      * Enter the **Setting Name**.
      * Use the **Enable/Disable** checkboxes as needed.
      * For additional settings, click the **+** symbol and complete the new entry.
      * Click **OK**, then **Save** to finalize this screen.
9. Click **Save** again to store the template.
10. Once the template is successfully created, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** from the dropdown and provide **email address(es)** for run notifications.
13. Under **Post Deployment Steps**, select the test cases you created.
14. Review the **View History** page for a detailed summary of the provisioning operation.
