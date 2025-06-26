# Fiscal Year

The **FiscalYear** template allows the configuration of fiscal year settings in Salesforce using AutoRABIT.

## Steps to Create the Fiscal Year Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **FiscalYear** checkbox under **Fiscal Year**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will appear automatically.
   - Click **Add** to input custom test data.
   - Enter the following details:
     - **Standard Fiscal Year:** Enable this checkbox to use the standard fiscal year.
     - **Fiscal Year Start Month Type:** Specify the starting month of the fiscal year.
     - **Based on Ending Month:** Check this box if applicable.
     - **Based on Starting Month:** Check this box if applicable.
   - Click **Save** to finalize the test data entry.

9. Click **Save** again to save the template.

10. After saving, you'll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** and enter the **email address(es)** to receive notification upon execution.
13. Under **Post Deployment Steps**, select the test cases you recently created.
14. Refer to the **View History** page for a comprehensive summary of the execution.
