# NewQuote

The **NewQuote** template is used to create a new quote template in Salesforce via the Environment Provisioning workflow.

## Steps to Create the NewQuote Template

1. Log in to your AutoRABIT account.
2. Go to the **Env. Pro.** module.
3. Click on **Create New Template**.
4. Navigate to the **Create Unsupported Metadata Template** tab.
5. Provide a **name** and a **short description** for the template.
6. Check the **NewQuote** option under **Quote Templates**.
7. Click **Add**.

8. In the next screen:
   - A **Test Case Name** is auto-generated.
   - Click **Add** to enter custom test data and provide a name.
   - Fill in the **Existing Template** and **Template Name** fields.
   - Click **Save** to store the data for this step.

9. Click **Save** again to finalize the template.

10. Upon successful creation, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your target org.
12. Choose your **destination org** from the dropdown and enter one or more **email addresses** to receive notifications upon execution.
13. Under **Post Deployment Steps**, select the recently created test cases.
14. Review the **View History** page for a complete report of the deployment process.
