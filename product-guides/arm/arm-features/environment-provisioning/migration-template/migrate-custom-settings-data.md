# Migrate Custom Settings Data

When migrating a large number of Custom Settings from one sandbox to another and then to Production, use this template.

To migrate custom setting data from one Salesforce Org to another, follow the steps below:

1. In the **Create Migration Template** screen, select the checkbox: **Migrate Custom Setting Data.**
2.  Give a Name to the **template** and as well as add a **short description**. Choose the **source Salesforce Org** from the drop-down menu and then click on **Select Objects**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631610534763.png" alt=""><figcaption></figcaption></figure>
3. On the next screen, choose the required objects fields from the list of objects available in the source org. Use the quick search option to further filter the options.
4. Next, click on the **Fetch Fields** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631610608728.png" alt=""><figcaption></figcaption></figure>

5. The next screen will fetch the fields available in the selected objects. The non-customizable objects will remain un-highlighted and you won’t be able to select that object.
6.  Click on the **Show Fields** to display the list of fields available in the object.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631609807905.png" alt=""><figcaption></figcaption></figure>
7.  Select the desired fields and then click on the **Get Records** button.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631609603513.png" alt=""><figcaption></figcaption></figure>
8. Next, click the **Save** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631610035994.png" alt=""><figcaption></figcaption></figure>

9. See your Summary report to validate once again and then click **Save**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631610179941.png" alt="" width="375"><figcaption></figcaption></figure>

10. Next, you'll be taken to the **Create Template** page. At the bottom of the template screen, click the **Save** button. The template is created successfully and appears on the **Env Provisioning** homepage.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631610434329.png" alt="" width="563"><figcaption></figcaption></figure>

11. Click on the **Run** button to run the current template on your destination org.
12. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
13. To use the current template as the post-deployment during [CI/CD](https://www.autorabit.com/blog/drive-your-business-faster-why-automated-ci-cd-matters/), select the **Migrate Custom Setting Data** checkbox under the **Post Deployment Steps** section. This is optional.
14. Click **Run**. For a detailed summary report of the operation carried out, please check the **View History** page**.**
