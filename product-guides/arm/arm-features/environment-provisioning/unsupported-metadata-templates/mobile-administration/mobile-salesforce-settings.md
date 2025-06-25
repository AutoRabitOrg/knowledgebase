# Mobile Salesforce Settings

The **MobileSalesforceSettings** template allows the configuration of mobile-specific Salesforce settings via AutoRABIT’s Environment Provisioning.

## Steps to Create the MobileSalesforceSettings Template

1. Log in to your AutoRABIT account.
2. Click on the **Env. Pro.** module.
3. Select **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **MobileSalesforceSettings** checkbox under **Mobile Administration**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will appear by default.
   - Click **Add** to create custom test data and assign a name.

9. Check the following settings:
   - **Mobile Browser App Settings**
   - **Device Access Settings**

   Then click **Save** to confirm and store the configuration.

   ![Mobile Salesforce Settings Configuration](../../../../../../.gitbook/assets/image%20(85).png)

10. Click **Save** again to save the template.
11. Once saved, you will be redirected to the **Environment Provisioning History** screen.
12. Click **Run** to execute the template on the selected destination org.
13. Choose your **destination org** from the dropdown and specify **email address(es)** for notifications.
14. In the **Post Deployment Steps**, select the test cases that were just created.
15. Visit the **View History** page for a comprehensive summary of the deployment activity.
