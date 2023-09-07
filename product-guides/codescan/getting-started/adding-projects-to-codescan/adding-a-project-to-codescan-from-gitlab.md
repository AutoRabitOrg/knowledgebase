# Adding a project to CodeScan from GitLab

This document guides how to add a GitLab project to your CodeScan Cloud account and run the analysis.

1. Login to your CodeScan account.
2. Once you login into your [CodeScan](https://www.codescan.io/) account, click on the (**+**) icon in the top right corner and select **Analyze new project**.![login codescan account](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634903866931.png)
3. &#x20;It takes you to a different window. Choose the **Organization** for which you'd like to create a project. Click on **Set Up**.![Analyze projects](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634904111011.png)
4. In the next screen, click on **Add Analysis Project** button. ![Add Analysis Project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1634904218482.png)
5. You will now see a new popup window; click on [**GitLab**](https://knowledgebase.autorabit.com/codescan/docs/integrating-codescan-in-gitlab) from the given options.
6. Now another popup window appears with the fields: **Choose a repository**, **Project Branch**, **Check Pull Requests**, **Key**, and **Name.**
   * Choose the repository you want to add, followed by the project branch name.
   * Make sure you select the checkbox under **Check Pull Requests**. This will add **webhooks**.
   * Next, enter the **Project Key** followed by the **Project Name**.Note:To know where to find the project key, refer to our document on how to do it by clicking [HERE](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
   * Once you fill out all the details in the popup window, click on **Add and Run Now**.
7. This triggers the project analysis and the project being added under your CodeScan organization.
8. You can view the project analysis report by clicking on **Details** from your VC repository.![VC repository](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642586013379.png)
9. &#x20;When you click the link, it will take you to the **CodeScan Project** page, where you can view your project's log report.
10. ![codescan project page](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642586282193.png)
11. Now that the webhooks have been created, every time a push or pull request is made to the tracked branch, an analysis will be triggered in CodeScan.
