# ApexExceptionEmail

**ApexExceptionEmail** template sets the email addresses that will receive notifications when the Apex code encounters unhandled exceptions. Emails can be sent to the Salesforce org’s users and external email addresses. Additionally, delete the Salesforce user who no longer exists.

To create this template, follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Give the template a **name** and a **short description** of it.
6. Select the **ApexExceptionalEmail** checkbox available under **Add Apex Exception Email.**
7. Click **Add**.&#x20;
8. On the next screen, a **Test Case Name** appears automatically by default. To add the custom test data, click on **Add** button.
9.  Users can add the required details in the fields of **Salesforce User, External Email Addresses, and Delete Salesforce User.** To add further details, click on ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631619313556.png)icon.

    1. You can even add multiple pages for the above-generated test cases. Click on the **+** symbol and fill in the fields mentioned in the earlier steps.&#x20;
    2. Click **OK**.&#x20;
    3. Once done, click on the **Save** button to save this page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1632208256079.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1632208289821.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1632208328645.png" alt=""><figcaption></figcaption></figure>
10. Next, Click **Save** to save the template.
11. Once the template is successfully created, you'll be redirected to the **Environment Provisioning History** screen.
12. Click the **Run** button to run the template on your destination org.
13. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
14. In the **Post Deployment Steps**, select the test cases that you have recently created.&#x20;
15. Please check the **View History** page for a detailed summary report of the operation carried out.
