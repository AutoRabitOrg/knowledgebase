# CodeScan and Flosum Integration

## About Flosum <a href="#about-flosum" id="about-flosum"></a>

**Flosum** is a release management tool for the Salesforce platform. Flosum users can now integrate CodeScan in their deployments to achieve secure, error-free releases.

## How to Integrate Flosum with CodeScan <a href="#how-to-integrate-flosum-with-codescan" id="how-to-integrate-flosum-with-codescan"></a>

1. **Install CodeScan.**&#x20;
   1. Obtain the CodeScan package URL from your Customer Success Manager.&#x20;
   2. Install the CodeScan package in your Flosum organization.&#x20;
   3. After installation, click on the app launcher and open Flosum-CodeScan.

<figure><img src="../../../../.gitbook/assets/image (509).png" alt=""><figcaption></figcaption></figure>

2.  **Authorize** CodeScan.

    *   Go to the **Authorization** tab in Flosum-CodeScan.\


        <figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>



    * Enter the following details to sync CodeScan with your Flosum organization.
      * **CodeScan URL**: Use the appropriate URL for your CodeScan instance:
        * **US** region: [_https://app.codescan.io_](https://app.codescan.io)
        * **EU** region: [_https://app-eu.codescan.io_](https://app-eu.codescan.io)
        * **AUS** region: [_https://app-aus.codescan.io_](https://app-aus.codescan.io)
      * **Organization Key**: Obtain this key from your hosted CodeScan instance.
      *   **Token**: Generate a token by navigating to **User > My Account > Security** in CodeScan. Set the token expiration or choose "no expiration."\


          <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **Flosum Branch Configuration**:
   1. On the **Branch Configuration** tab, choose the branch you want to scan.
      * Select all or specific component types from the six supported profiles:
        * Aura
        * Lightning
        * Apex Class
        * Apex Triggers
        * Apex Page
        * Component
      *   Check the boxes for the components you want to scan and click **Save**.\


          <figure><img src="../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. **Finalize Setup**:&#x20;
   *   Log in to CodeScan and confirm that your branch is populated in the CodeScan server. \


       <figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
   *   Select the branch, click **Add Analysis Project**, and attach it as a webhook.\


       <figure><img src="../../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

       <figure><img src="../../../../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Initiating a Scan on the Flosum Branch

1. **Branch Sync**:
   * Add the **Branch Sync** lightning component to your branch's Lightning record page.
   *   Click the **Branch Sync** button to trigger the static code analysis.\


       <figure><img src="../../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>
2. **View Project Analysis**:
   *   Go to the **Project Analysis** page to see the analysis in progress.\


       <figure><img src="../../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

Your Flosum-CodeScan integration is complete!

## How Does Flosum-CodeScan Work? <a href="#how-does-flosumcodescan-work" id="how-does-flosumcodescan-work"></a>

#### Case 1: Create a new branch and add all metadata components <a href="#case-1-create-a-new-branch-and-add-all-metadata-components" id="case-1-create-a-new-branch-and-add-all-metadata-components"></a>

In this use case, we will create a new branch in Flosum, add all new metadata components, and perform a [static code analysis](https://www.codescan.io/) on a CodeScan server.

1. Go to **Flosum**, create a **new branch** and attach it to existing repository and click on **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (514).png" alt="" width="563"><figcaption></figcaption></figure>

2. Now go to **`Flosum-CodeScan Package`**, click on **`component type`** and select all the component types and associate branch and click **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (515).png" alt="" width="563"><figcaption></figcaption></figure>

3. Navigate to your instance's URL, for example, [_https://app.codescan.io_](https://app.codescan.io) for **US** region, [_https://app-eu.codescan.io_](https://app-eu.codescan.io) for **EU** region or [_https://app-aus.codescan.io_](https://app-aus.codescan.io) for **AUS** region.
4. Login to your CodeScan account, and you will notice that the branch is populated in the CodeScan Server with your project.

<figure><img src="../../../../.gitbook/assets/image (516).png" alt=""><figcaption></figcaption></figure>

5. Select the **`branch`** and click on **`Add Analysis Project`** button and attach it as a webhook.

<figure><img src="../../../../.gitbook/assets/image (517).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

6. Now you deploy metadata components like **`Apex Class`**, **`triggers`** to your branch and CodeScan will trigger static code analysis on the fly.

#### Case 2: For an existing branch create a new project <a href="#case-2-for-an-existing-branch-create-a-new-project" id="case-2-for-an-existing-branch-create-a-new-project"></a>

In this use case we will authorize existing branch in Flosum and add all new metadata components and do a static code analysis on a CodeScan server.

{% hint style="info" %}
**Note:** This case is very similar to case 1, only step 1 is added as an extra functionality.
{% endhint %}

1. Go to **`Flosum-CodeScan Package`** and click on **`Create project`** from a branch, select the **`branch`** and click on **`Create`**.

<figure><img src="../../../../.gitbook/assets/image (519).png" alt=""><figcaption></figcaption></figure>

2. Click on **`component type`** and select all the component types and associate branch and click **`save`**.

<figure><img src="../../../../.gitbook/assets/image (520).png" alt=""><figcaption></figcaption></figure>

3. Navigate to your instance's URL, for example, [_https://app.codescan.io_](https://app.codescan.io) for **US** region, [_https://app-eu.codescan.io_](https://app-eu.codescan.io) for **EU** region or [_https://app-aus.codescan.io_](https://app-aus.codescan.io) for **AUS** region.
4. Login to your CodeScan account, and you will notice that the branch is populated in the CodeScan Server.

<figure><img src="../../../../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure>

5. Click on the **`branch`** and attach analysis as webhook.
6. Now you can deploy [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) components like **`Apex Class`**, **`Triggers`** to your branch and CodeScan will trigger static code analysis on the fly.

{% hint style="info" %}
**Note:** Steps 4, 5, and 6 have similar functionality as Case 1.
{% endhint %}
