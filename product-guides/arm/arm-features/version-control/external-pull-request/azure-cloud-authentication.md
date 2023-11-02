# Azure Cloud Authentication

The recommended way to access your Azure DevOps project is to use personal access tokens (PAT). PAT is like a combination of a user name and a password that are valid for a certain time only and can have restricted access to your Azure DevOps resources.

To create a personal access token, you have to follow the following steps:

1. Sign in to your organization in [Azure DevOps](../../../integration-and-plugins/azure-devops.md).
2. From your home page, open your profile. Go to your **security details**.
3. Select **+ New Token**.
4. **Name** your token, select the **organization** where you want to use the token, and then choose a **lifespan** for your token.
5. Select the **scopes** for this token to authorize for your specific tasks.
6. Click **Create**.
7. When you're done, make sure to copy the token. For your security, it won't be shown again. **Use this token as your password.**

**Pre-requisites:**

If you select **Custom defined** access, then you must select the below options:

1.  &#x20;**Code**: Select at least **Read** or any other option, except status, so that we are able to enable the pull request.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1657015264704.png" alt="" width="375"><figcaption></figcaption></figure>
2.  &#x20;**Member Entitlement Management**: Select at least the **Read** option, so that we are able to fetch users, i.e. reviewers; and can perform approval-related operations.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1657015560785.png" alt="" width="375"><figcaption></figcaption></figure>

**Limitations:**

When we generate PAT with custom defined access, we won't be able to see **DIFF** of a pull request. This is because the Diff API is not supported with custom access option.

We can only see Diff if PAT is generated with **Full access**.
