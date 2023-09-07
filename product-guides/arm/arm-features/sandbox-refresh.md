# Sandbox Refresh

To create this template, follow the steps below:

1. Log in to your ARM account.
2. Click on **Env. Pro.** module.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689932268762.png)
3. Click on **Create New Template**.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689932369120.png)
4. Click on the **Create** [**Unsupported Metadata Template**](https://knowledgebase.autorabit.com/docs/unsupported-metadata-templates) tab.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689932583705.png)
5. Enter the **Template Name** and a short **Description**.
6. Select the **Sandbox Refresh** checkbox, then click on **Add**.
7. On the next screen, a **Test Case Name** appears by default. To refresh multiple sandboxes, enter the custom test data, click **Add**, then enter a name.
8. In ARM, enter the same name in the **Sandbox Name** field as the name in the **Sandbox Information** section of the production org.

&#x20;![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689941650217.png)

Provide the source name from the same production org in the **Source Sandbox**.

Refer to the following Salesforce screens to update the details under **Deploy>Sandboxes**, click **Refresh** for the Sandbox to view the **Sandbox Information** section.\
![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1691088066826.png)\
\
![A screenshot of a software program&#x20;
Description automatically generated](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1691088146878.png)

9. To refresh a sandbox, select **Production Org** in the **Source Sandbox** field. Or, to clone an existing sandbox, select the name of the sandbox as selected in the **Create From** dropdown in the **Sandbox Information** section.&#x20;
10. Click **Save** to save this page.&#x20;
11. Next, click **Save** to save the template.&#x20;
12. Once the template is created successfully, you'll be redirected to the [**Environment Provisioning**](https://knowledgebase.autorabit.com/docs/environment-provisioning) **History** screen.
13. Click on the **Run** button to run the current template on your destination org.\
    ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689936743383.png)
14. From the dropdown, select the **Production Org in which the selected Sandbox** exists.\
    _**Note: Production must be registered in AutoRABIT.**_\
    ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689936882637.png)
15. Enter the **email address(es)** to receive an email notification when the template is run.
16. In the **Post Deployment Steps**, select the test cases you recently **created**.&#x20;
17. For a detailed summary report of the operation carried out, see the **View History** page.
