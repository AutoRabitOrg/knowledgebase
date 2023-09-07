# Add a project to CodeScan from GitHub

This document guides how to add a **GitHub** project to your CodeScan cloud account and run the analysis.

1. Login to your **CodeScan** account.
2. On the top right corner, click on the **'+'** icon and select **Analyze new project**.\
   ![Analyze New Project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045365564.png)
3. It takes you to a different window. Choose the **Organization** for which you'd like to create a project. Click **Set Up**.![Analyze Projects](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045425810.png)
4. On the next window, click on **Add Analysis Project**.![Add Analysis Project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045455803.png)
5. You will now see a new pop-up window; select [**GitHub**](https://knowledgebase.autorabit.com/codescan/docs/integrating-codescan-with-github-actions) from the given option.![Add New Project](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045811458.png)
6. Once you select [GitHub](https://knowledgebase.autorabit.com/codescan/docs/github-actions), it will redirect to the **GitHub login** page. Validate your credentials and click on **Login**.![GitHub Login](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1635045572121.png)
7. On the next screen, fill in the details below:
   1. Choose the **Repository** you want to add, followed by the **Project Branch** name.
   2. Make sure you select the checkbox under **Check Pull Requests**.&#x20;
   3. The **Project Key** and the **Project Name** are auto-assigned. You can edit the fields as per your requirement.
   4. Click on **Add and Run Now.**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1649142175036.png)About Project KeyTo know where to find the project key, refer to our documentation by clicking [HERE](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
8. This triggers the project analysis and the project being added under your [CodeScan](https://www.codescan.io/) organization.
9. &#x20;You can view the project analysis report by clicking on **Details** from your VC repository.![VC repository](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642586013379.png)
10. &#x20;When you click the link, it will take you to the **CodeScan Project** page, where you can view your project's log report.![CodeScan Project page](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1642590860205.png)

Now that the webhooks have been created, every time there is a push to the tracked branch or a pull request made/updated against the tracked branch, an analysis will be triggered in CodeScan.
