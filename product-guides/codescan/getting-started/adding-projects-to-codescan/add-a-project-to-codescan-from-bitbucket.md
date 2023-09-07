# Add a Project to CodeScan from Bitbucket

This document is a guide on how to add a Bitbucket project to your CodeScan cloud account and run the analysis.

1. Login to your CodeScan account.
2. Once you login into your [CodeScan](https://www.codescan.io/) account, on the top right corner, click on the (**+**) icon and select **Analyze new project**.<img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635044236805.png" alt="CodeScan account" data-size="original">
3. It takes you to a different window. Choose the **Organization** for which you'd like to create a project.![Analyze projects](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635044284970.png)
4. In the next window, click on **Add Analysis Project** option.![Add Analysis Project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635044314783.png)
5. You will now see a new popup window, select [**Bitbucket**](https://knowledgebase.autorabit.com/codescan/docs/integrating-codescan-in-bitbucket-pipelines) from the given options.![Bitbucket](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045969225.png)
6. &#x20;Once you select **Bitbucket**, it will redirect you to the **Bitbucket login** page. Validate your credentials and click on **Login**.![Bitbucket](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045088451.png)
7. Enter the necessary information in the below fields and then click on **Add and Run Now.**\
   ![add a new project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(132\).png)
   * Choose the repository you want to add followed by the **Project Branch** name.
   * Make sure you select the checkbox under **Check Pull Requests**.
   * Now, enter the **project key** followed by the **project name**.\
     Note:To know where to find the project key, refer to our document on how to do it by clicking [HERE](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
   * Once you fill out all the details in the popup window, select **Add and Run Now**.
8. This triggers the project analysis along with the project being added under your CodeScan organization.
9. You can view the project analysis report by clicking on **Details** from your VC repository.![VC repository](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642586013379.png)
10. &#x20;When you click the link, it will take you to the **CodeScan Project** page, where you can view your project's log report.![codescan project page](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642586282193.png)

Now that the webhooks have been created, every time there is a push to the tracked branch or a pull request made/updated against the tracked branch, an analysis will be triggered in CodeScan.

\
