# Email Admin Settings

To create this template, follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Give the template a **name** and a **short description** of it.
6. Select the **EditLead** checkbox available under **Lead Settings.**
7. Click **Add**.
8.  On the next screen, you'll notice that a **Test Case Name** appears by default. Click the **Add** button to add the custom test data. Fill in the required information in the fields below, then click the **Save** button.

    * **Lead Type:** Enter either queue or a user that will own a lead when assignment rules fail to locate an owner.
    * **Lead Owner:** Enter the owner's name in this field.
    * **Lead Conversion Setting:** Click on![](<../../../../../.gitbook/assets/image (72).png>)icon to add the required setting details here. Activate the settings by selecting the **Active** checkbox.\
      i. **Require Validation for Converted Leads:** When users convert leads, enforce required field settings, field validation rules, workflow actions, and Apex triggers.\
      ii. **Preserve Lead Status:** Prevent the lead status from changing to the new lead owner's default value during lead conversion.\
      iii. **Enable Conversions for Salesforce Mobile:** Let users convert leads on the mobile app.

    <figure><img src="../../../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>
9. Click **Save** to save the template.
10. Once the template is successfully created, you'll be redirected to the **Environment Provisioning History** screen.
11. Click the **Run** button to run the template on your destination org.
12. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
13. In the **Post Deployment Steps**, select the test cases that you have recently created.&#x20;
14. Please check the **View History** page for a detailed summary report of the operation carried out.
