# Add a Project to CodeScan from Bitbucket

This document is a guide on how to add a Bitbucket project to your CodeScan cloud account and run the analysis.

1. Login to your CodeScan account.
2. Once you login into your [CodeScan](https://www.codescan.io/) account, on the top right corner, click on the (**+**) icon and select **Analyze new project**.

<figure><img src="../../../../.gitbook/assets/image (22) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. It takes you to a different window. Choose the **Organization** for which you'd like to create a project.

<figure><img src="../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. In the next window, click on **Add Analysis Project** option.

<figure><img src="../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. You will now see a new popup window, select [**Bitbucket**](https://knowledgebase.autorabit.com/codescan/docs/integrating-codescan-in-bitbucket-pipelines) from the given options.

<figure><img src="../../../../.gitbook/assets/image (25) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Once you select **Bitbucket**, it will redirect you to the **Bitbucket login** page. Validate your credentials and click on **Login**.

<figure><img src="../../../../.gitbook/assets/image (26) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="328"><figcaption></figcaption></figure>

7.  Enter the necessary information in the below fields and then click on **Add and Run Now.**

    <figure><img src="../../../../.gitbook/assets/image (30) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="450"><figcaption></figcaption></figure>

    * Choose the repository you want to add followed by the **Project Branch** name.
    * Make sure you select the checkbox under **Check Pull Requests**.
    * Now, enter the **project key** followed by the **project name**.
    * Once you fill out all the details in the popup window, select **Add and Run Now**.

{% hint style="info" %}
**Note:** To know where to find the project key, refer to our document on how to do it by clicking [HERE](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
{% endhint %}

8. This triggers the project analysis along with the project being added under your CodeScan organization.
9. You can view the project analysis report by clicking on **Details** from your VC repository.

<figure><img src="../../../../.gitbook/assets/image (28) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

10. When you click the link, it will take you to the **CodeScan Project** page, where you can view your project's log report.

<figure><img src="../../../../.gitbook/assets/image (29) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Now that the webhooks have been created, every time there is a push to the tracked branch or a pull request made/updated against the tracked branch, an analysis will be triggered in CodeScan.
