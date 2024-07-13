# Add a project to CodeScan from Salesforce

This document guides how to add a Salesforce project to your [CodeScan cloud](https://www.codescan.io/products/cloud/) account and run the analysis.

1. Login into your CodeScan account.
2. Once you log into your CodeScan account, click the **`+`** icon in the top right corner and select **`Analyze new project`**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. &#x20;It takes you to a different window. Choose the **`Organization`** for which you'd like to create a project. Click **`Set Up`**.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. In the next window, click on **`Add Analysis Project`** option.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. You will now see a new popup window; select **`Salesforce`** from the given options.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6.  Next, choose the environment from the dropdown between _**Production/Developer**, **My own domain**, and **Sandbox**_.

    * **`Production/Developer:`** Production/Developer refers authenticating users to Salesforce.com for a Developer account and/or a  Production account using the username and password at [_login.salesforce.com_](https://login.salesforce.com/)_._
    * **`Sandbox:`** Sandboxes are test environments that provide a way to copy and create metadata from a production org (above).  It is a separate environment where you can test (including seeding with data). There are four different types of sandboxes, accessed at [_test.salesforce.com_](https://test.salesforce.com/)_._
    * **`My own domain:`** Choose this if you have set up your domain or custom URL to access your Salesforce org rather than [_https://login.salesforce.com_](https://login.salesforce.com/). Next, specify the Salesforce login URL in the text box. For example, _https://mydomainname.my.salesforce.com_. Companies and admins can better manage login and authentication for their Salesforce orgs by creating a custom domain.

    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="487"><figcaption></figcaption></figure>
7. Click on **`Authorize`**. It will redirect to the Salesforce login page. Validate your credentials and click on **`Login`**.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. You will be redirected back to the CodeScan app.
9.  In **CodeScan**, on **`Add a new project`** screen, fill in the below details:

    * The **`project key`** and the **`project name`** are auto-assigned. You can edit the fields as per your need.Note:To know where to find the project key, refer to our document on how to do it by clicking [HERE](../setting-up-a-codescan-cloud-organization/finding-your-project-key.md).
    * Enter the project version under the **`Default Project Version`** field.
    * Choose the **`Unit Test Mode`** from the dropdown. This allows you to configure which unit tests are run by the analysis. Example, _Run Unit Tests, Use Previous Run, or_ keep it in _disabled_ mode
    * Under **`Scheduling`**, you can set the time frame for the analysis to run. You can run the project automatically by selecting _Daily_ or manually by selecting _Manual_. If you select _Daily_, another field named _Schedule_ has to be selected by choosing the time you want the automatic analysis to be triggered.

    <figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="406"><figcaption></figcaption></figure>
10. Click **`Add and Run Now`**. This triggers the project analysis and the added project under your [CodeScan](https://www.codescan.io/) organization.
11. You'll be redirected to the **`Project Analysis`** screen to view the status of your analysis triggered.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

12. View the log report by clicking on **`Gear`** (![](<../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon drop-down and selecting **`Logs`**.

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Troubleshooting

**"ip restricted" error:** If your scan fails with the IP restricted error, please refer to the [Troubleshooting article](https://knowledgebase.autorabit.com/codescan/docs/ip-restricted-issue).
