# ReplaceContactRoles

**ReplaceContactRoles** template allows replacement of existing picklist value with the new picklist value and automatically deletes a value to the picklist.

To create this template, follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create** [**Unsupported Metadata Template**](../) tab.
5. Give the template a **name** and a **short description** of it.
6. Select the **ReplaceContactRoles** checkbox available under [**Case Contact Roles**](./)**.**
7. Click **Add**.
8.  On the next screen, you will find a **Test case name** appear automatically by default. To add the custom test data, click on **Add** button. You will have the following options to check:

    * Click on![](<../../../../../../.gitbook/assets/image (42).png>)icon.
    * **Exact Value**: Enter the existing picklist value to be fetched
    * **Select Value:** Enter the new picklist value to be changed
    * **Blank Values:** If selected, it will replace all the blank values from the ‘**Exact Value**’ field. Make sure to keep the ‘Exact Value’ field blank when using this option.
    * You can even add multiple values for the above-generated test case. Click on the **+** symbol and fill in the fields as mentioned in the steps earlier.&#x20;
    * Click **OK**. Once you are finished, click on **Save** to save this page.

    <figure><img src="../../../../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>
9. Next, Click **Save** to save the template.
10. Once the template is successfully created, you'll be redirected to the [**Environment Provisioning**](../../) **History** screen.
11. Click on the **Run** button to run the current template on your destination org.
12. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
13. In the **Post Deployment Steps**, select the test cases that you have recently created.&#x20;
14. For a detailed summary report of the operation carried out, please check the **View History** page.
