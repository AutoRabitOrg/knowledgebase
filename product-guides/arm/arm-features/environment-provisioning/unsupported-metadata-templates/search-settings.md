# Search Settings

The user can schedule an Apex class that implements the 'Schedulable' interface to be automatically executed on a weekly interval using this template.

To create this template, follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create** [**Unsupported Metadata Template**](./) tab.
5. Give the template a **name** and a **short description** of it.
6. Select the **SearchSetting** checkbox available under **Search Settings**.
7. Click **Add**.
8. On the next screen, you'll notice that a **Test Case Name** appears by default. Click the **Add** button to add the custom test data. Fill the required information in the fields below, then click the **Save** button.
   * **Search Setting field:** Enter the desired search interface settings in this fields, mark it active by selecting the Active box.
   * **Search Results:** Specify the number of records to display for each object on the Search Results page. To make changes, select one or more objects, enter the new number of results per page, and click Save. The new value must be between 5 and 50.
   * **Lookup Settings:** Select the objects for which you want to enable the following features and click Save:
   * Enhanced lookups provide an updated lookup dialog interface that gives users the ability to filter, sort, and page through results as well as customize columns.
   * Lookup auto-completion displays suggestions from the Recent Items list as you type.
9. Click **Save** to save the template.
10. Once the template is successfully created, you'll be redirected to the [**Environment Provisioning**](../) **History** screen.
11. Click on the **Run** button to run the current template on your destination org.
12. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
13. In the **Post Deployment Steps**, select the test cases that you have recently created.&#x20;
14. For a detailed summary report of the operation carried out, please check the **View History** page.
