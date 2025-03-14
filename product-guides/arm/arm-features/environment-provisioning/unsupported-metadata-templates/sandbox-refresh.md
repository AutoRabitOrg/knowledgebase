# Sandbox Refresh

To create this template, follow the steps below:

1. Log in to your ARM account.
2. Click on **Env. Pro.** module.

<figure><img src="../../../../../.gitbook/assets/image (34).png" alt="" width="215"><figcaption></figcaption></figure>

3. Click on **Create New Template**.

<figure><img src="../../../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

4. Click on the **Create** [**Unsupported Metadata Template**](./) tab.

<figure><img src="../../../../../.gitbook/assets/image (36).png" alt="" width="563"><figcaption></figcaption></figure>

5. Enter the **Template Name** and a short **Description**.
6. Select the **Sandbox Refresh** checkbox, then click on **Add**.
7. On the next screen, a **Test Case Name** appears by default. To refresh multiple sandboxes, enter the custom test data, click **Add**, then enter a name.
8. In ARM, enter the same name in the **Sandbox Name** field as the name in the **Sandbox Information** section of the production org. Provide the source name from the same production org in the **Source Sandbox**.

<figure><img src="../../../../../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

Refer to the following Salesforce screens to update the details under **Deploy > Sandboxes**, click **Refresh** for the Sandbox to view the **Sandbox Information** section.

<figure><img src="../../../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

9. To refresh a sandbox, select **Production Org** in the **Source Sandbox** field or, to clone an existing sandbox, select the name of the sandbox as selected in the **Create From** dropdown in the **Sandbox Information** section.&#x20;
10. Click **Save** to save this page.&#x20;
11. Next, click **Save** to save the template.&#x20;
12. Once the template is created successfully, you'll be redirected to the **Environment Provisioning History** screen.
13. Click on the **Run** button to run the current template on your destination org.

<figure><img src="../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

14. From the dropdown, select the **Production Org in which the selected Sandbox** exists.

{% hint style="info" %}
**Note:** Production must be registered in AutoRABIT.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/image (41).png" alt="" width="563"><figcaption></figcaption></figure>

15. Enter the **email address(es)** to receive an email notification when the template is run.
16. In the **Post Deployment Steps**, select the test cases you recently **created**.&#x20;
17. For a detailed summary report of the operation carried out, see the **View History** page.
