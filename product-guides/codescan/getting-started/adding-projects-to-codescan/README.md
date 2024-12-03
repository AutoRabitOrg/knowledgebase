# Adding Projects to CodeScan

This document provides a description about how to create a project in CodeScan.

### Salesforce Permissions

The minimum permissions required in the Salesforce profile to add a Salesforce project in CodeScan are listed below:

1. API Enabled (mandatory)
2. Modify Metadata Through Metadata API Functions (mandatory)
3. View All Data
4. Author Apex (Needed when IncludeContentsOfPackages is enabled)

You can find all these permissions under Profile > Administrative Permissions in Salesforce.

### Prerequisites <a href="#prerequisities" id="prerequisities"></a>

You will need a CodeScan organization to add a project to it. When signing up with [CodeScan Cloud](https://www.codescan.io/products/cloud/), an organization is created automatically under your username. New organizations can be created at any time using the '**+**' icon at the top-right corner of the screen.

<figure><img src="../../../../.gitbook/assets/image (90) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Adding a Project into CodeScan <a href="#adding-a-project-into-codescan" id="adding-a-project-into-codescan"></a>

To be able to analyze code in CodeScan, you need to add a project first. This can easily be done by following the procedures below.

1. Log in to the CodeScan account.
2. On the top-right corner, click on the **`+`** icon and select **`Analyze new project`**.
3. Choose the **`Organization`** for which you'd like to create a project. Click **`Set Up`**.
4. In the next window, click on **`Add Analysis Project`**.
5. On the next screen, select from the applications displayed to add a new analysis project. You will be redirected to an authentication page to authorize CodeScan to access your source code.

> CodeScan allows adding projects from:
>
> 1. [Salesforce](https://knowledgebase.autorabit.com/codescan/docs/adding-new-salesforce-project-to-codescan)
> 2. [GitHub](https://knowledgebase.autorabit.com/codescan/docs/add-a-project-to-codescan-from-github)
> 3. [Atlassian Bitbucket](https://knowledgebase.autorabit.com/codescan/docs/add-a-project-to-codescan-from-bitbucket)
> 4. [Gitlab](https://knowledgebase.autorabit.com/codescan/docs/add-a-project-to-codescan-from-gitlab)
> 5. [Git](https://knowledgebase.autorabit.com/codescan/docs/add-a-project-to-codescan-from-git)
> 6. [Webhooks](https://knowledgebase.autorabit.com/codescan/docs/codescan-webhooks)

The detailed instructions to add a project from each of the above-mentioned applications are covered separately. [\[Learn More](https://knowledgebase.autorabit.com/codescan/docs/adding-projects)]

{% hint style="info" %}
**NOTE**: Issues across projects cannot be compared.
{% endhint %}
