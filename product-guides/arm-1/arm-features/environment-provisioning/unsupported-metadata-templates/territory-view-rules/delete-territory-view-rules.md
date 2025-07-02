# Delete Territory View Rules

The **DeleteTerritoryViewRules** template enables deletion of specific Territory View Rules from Salesforce using AutoRABIT’s Environment Provisioning feature.

## Steps to Create the DeleteTerritoryViewRules Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Open the **Create** [**Unsupported Metadata Template**](../../../../../arm/arm-features/environment-provisioning/unsupported-metadata-templates/) tab.
5. Provide a **name** and a **short description** for the template.
6. Select the **DeleteTerritoryViewRules** checkbox under **Territory View Rules**.
7. Click **Add**.
8.  On the next screen:

    * A **Test Case Name** appears automatically.
    * Click **Add** to input custom test data.
    * Complete the following fields:
      * **Territory Name**: Specify the territory associated with the rule.
      * **Rule Name**: Provide the name of the rule to delete.
    * Click **Save** to store the test data.

    ![Delete Territory View Rules - Example](<../../../../../../.gitbook/assets/image (1475).png>)
9. Click **Save** again to save the template.
10. After the template is successfully created, you’ll be redirected to the [**Environment Provisioning**](https://knowledgebase.autorabit.com/docs/environment-provisioning) **History** screen.
11. Click the **Run** button to execute the template on your destination org.
12. Choose your **destination org** from the dropdown and enter the **email address(es)** to receive notifications.
13. In the **Post Deployment Steps**, select the test cases you have recently created.
14. Visit the **View History** page for a detailed summary of the operation.
