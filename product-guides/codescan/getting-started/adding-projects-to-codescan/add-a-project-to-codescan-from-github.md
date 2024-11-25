# Add a project to CodeScan from GitHub

This document guides you how to add a **GitHub** project to your CodeScan cloud account and run the analysis.

1. Log in to your **CodeScan** account.
2. On the top right corner, click on the **'+'** icon and select **Analyze new project**.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. This takes you to a different window. Choose the **Organization** for which you'd like to create a project. Click **Set Up**.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next window, click on **Add Analysis Project**.

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. You will now see a new pop-up window; select [**GitHub**](https://knowledgebase.autorabit.com/codescan/docs/integrating-codescan-with-github-actions) from the given option.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Once you select [GitHub](https://knowledgebase.autorabit.com/codescan/docs/github-actions), it will redirect you to the **GitHub login** page. Validate your credentials and click on **Sign In**.

<figure><img src="../../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="267"><figcaption></figcaption></figure>

7.  On the next screen, fill in the details below:

    * Choose the **Repository** you want to add, followed by the **Project Branch** name.\
      **NOTE**: If you do not specify the Branch Name during GitHub integration, then it will take the main branch by default.
    * Make sure you select the checkbox under **Check Pull Requests**.&#x20;
    * The **Project Key** and the **Project Name** are automatically assigned. You can edit the fields per your requirements.
    * Click on **Add and Run Now.**

    <figure><img src="../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="405"><figcaption></figcaption></figure>

    * About **Project Key**: To find the project key, refer to our documentation [HERE](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key).
8. This triggers the project analysis and the project being added under your CodeScan organization.
9. &#x20;You can view the project analysis report by clicking on **Details** from your VC repository.

<figure><img src="../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

10. When you click the link, it will take you to the **CodeScan Project** page, where you can view your project's log report.

<figure><img src="../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Now that the webhooks have been created, every time there is a push to the tracked branch or a pull request made/updated against the tracked branch, an analysis will be triggered in CodeScan.

{% hint style="info" %}
**Known limitation from GitHub**: When an analysis is triggered, CodeScan requests a token to GitHub, which has a limitation of 10 tokens per hour per user per application. For more information, refer to [Token Expiration and Revocation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation#token-revoked-due-to-excess-of-tokens-for-an-oauth-app-with-the-same-scope) on GitHub Docs.
{% endhint %}



