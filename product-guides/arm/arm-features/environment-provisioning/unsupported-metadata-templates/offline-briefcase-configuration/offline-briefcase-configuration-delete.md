# Offline Briefcase Configuration Delete

The **OfflineBriefcaseConfigurationDelete** template allows users to remove existing offline briefcase configuration records from their Salesforce org through AutoRABIT’s Environment Provisioning module.

## Steps to Create the OfflineBriefcaseConfigurationDelete Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Enter a **template name** and a **short description**.
6. Select the **OfflineBriefcaseConfigurationDelete** checkbox under the **Offline Briefcase Configuration** section.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** and **Record Name** appear by default.
   - Click the **Add** button to enter custom test data.
   - Click **Save** to store the test case.

9. Click **Save** again to finalize and save the template.

10. After creation, you’ll be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select the **destination org** from the dropdown and specify **email address(es)** to receive run notifications.
13. In the **Post Deployment Steps**, select the test cases you created.
14. Visit the **View History** page to review a detailed report of the operation.
