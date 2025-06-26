# Search Settings

The **SearchSetting** template enables users to configure and schedule search interface settings in Salesforce using AutoRABIT. It allows setting up enhanced lookups, auto-completion, and customizing search result limits.

## Steps to Create the Search Settings Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Go to the **Create** [**Unsupported Metadata Template**](./) tab.
5. Provide a **template name** and a **short description**.
6. Select the **SearchSetting** checkbox under **Search Settings**.
7. Click **Add**.

8. On the next screen:
   - A **Test Case Name** will appear by default.
   - Click **Add** to enter custom test data.
   - Fill in the required fields:
     - **Search Setting:** Enter the desired search interface configuration and check the **Active** box.
     - **Search Results:** Specify the number of records to display per object on the search results page (value must be between 5 and 50).
     - **Lookup Settings:** Select the relevant objects and enable:
       - **Enhanced Lookups** for advanced filtering, sorting, paging, and customizable columns.
       - **Lookup Auto-completion** for predictive suggestions from the Recent Items list.
   - Click **Save** to finalize the test case.

9. Click **Save** again to save the overall template.

10. Once saved, you’ll be redirected to the [**Environment Provisioning History**](../) screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** and enter **email address(es)** to receive notifications.
13. In the **Post Deployment Steps**, select the test cases you have recently created.
14. Visit the **View History** page for a detailed summary of the operation.
