# CodeScan and Flosum Integration

### About Flosum <a href="#about-flosum" id="about-flosum"></a>

**Flosum** is a release management tool for the Salesforce platform. Flosum users can now integrate CodeScan in their deployments to achieve error-free and secure releases.

### How to Integrate Flosum with CodeScan? <a href="#how-to-integrate-flosum-with-codescan" id="how-to-integrate-flosum-with-codescan"></a>

1. Install the **`CodeScan package`** in your **Flosum org**. Package URL to be provided by the **Flosum Customer Success Manager**.
2. After installation, click on **`App launcher`** and open **`Flosum-Codescan`**.

<figure><img src="../../../../.gitbook/assets/image (509).png" alt=""><figcaption></figcaption></figure>

3.  There are few settings which we need to enable in Flosum-CodeScan Package.

    * **Activate CodeScan:** Click on **`Activation`** tab and select **`Enable Synchronization`** option for Flosum-CodeScan.

    <figure><img src="../../../../.gitbook/assets/image (510).png" alt="" width="563"><figcaption></figcaption></figure>

    * **Authorize CodeScan:** To authenticate CodeScan account you need to have an **`Organization Key`** as well as **`Access Token`** from CodeScan Server.

    <figure><img src="../../../../.gitbook/assets/image (511).png" alt="" width="563"><figcaption></figcaption></figure>

    * **Select Component Types:** We support six metadata components as shown in the below image and you must select the branch in order to perform static code analysis. So, you have to select a **branch** and click on **`Save`**.

    <figure><img src="../../../../.gitbook/assets/image (512).png" alt="" width="563"><figcaption></figcaption></figure>

    * **Create new project from existing branch:** You can select an existing Flosum branch and click on **`Create`** button to create a new project in CodeScan which you can analyze.

    <figure><img src="../../../../.gitbook/assets/image (513).png" alt="" width="563"><figcaption></figcaption></figure>

Now you have done your complete setup with respect to Flosum-CodeScan.

### How Does Flosum-CodeScan Work <a href="#how-does-flosumcodescan-work" id="how-does-flosumcodescan-work"></a>

#### Case 1: Create a new branch and add all metadata components <a href="#case-1-create-a-new-branch-and-add-all-metadata-components" id="case-1-create-a-new-branch-and-add-all-metadata-components"></a>

In this use case we will create a new branch in Flosum and add all new metadata components and do a [static code analysis](https://www.codescan.io/) on a CodeScan server.

1. Go to **Flosum**, Create a **new branch** and attach it to existing repository and click on **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (514).png" alt="" width="563"><figcaption></figcaption></figure>

2. Now go to **`Flosum-CodeScan Package`**, click on **`component type`** and select all the component types and associate branch and click **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (515).png" alt="" width="563"><figcaption></figcaption></figure>

3. Navigate to your instance's URL, for example, [_https://app.codescan.io/_](https://app.codescan.io/) for **US** region, [_https://app-eu.codescan.io/_](https://app.codescan.io/) for **EU** region or [_https://app-aus.codescan.io/_](https://app.codescan.io/) for **AUS** region.
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

3. Navigate to your instance's URL, for example, [_https://app.codescan.io/_](https://app.codescan.io/) for **US** region, [_https://app-eu.codescan.io/_](https://app.codescan.io/) for **EU** region or [_https://app-aus.codescan.io/_](https://app.codescan.io/) for **AUS** region.
4. Login to your CodeScan account, and you will notice that the branch is populated in the CodeScan Server.

<figure><img src="../../../../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure>

5. Click on the **`branch`** and attach analysis as webhook.
6. Now you can deploy [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) components like **`Apex Class`**, **`Triggers`** to your branch and CodeScan will trigger static code analysis on the fly.

{% hint style="info" %}
**Note:** Step 4, 5, and 6 have similar functionality as Case 1.
{% endhint %}
