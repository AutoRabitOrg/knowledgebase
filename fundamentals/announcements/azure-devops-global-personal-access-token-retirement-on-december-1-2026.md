# Azure DevOps Global Personal Access Token Retirement

## Microsoft Azure DevOps authentication update&#x20;

Global Personal Access Tokens (PATs) will retire on December 1, 2026. Customers using them with AutoRABIT should move to organization-scoped PATs before that date. No AutoRABIT upgrade is required for this migration.&#x20;

#### Key message for customers&#x20;

This is a Microsoft Azure DevOps platform change. Organization-scoped PATs continue to work with AutoRABIT today, so customers can complete the required migration without waiting for a product release.&#x20;

## Azure DevOps Global Personal Access Token Retirement&#x20;

**Action required before December 1, 2026**&#x20;

Microsoft is retiring Global Personal Access Tokens (PATs) in Azure DevOps Services. A Global PAT is a token whose access scope is set to **All accessible organizations**.&#x20;

**On** **December 1, 2026, existing Global PATs will stop working**. Organization-scoped PATs are not affected and can continue to be used with AutoRABIT.&#x20;

This change is part of Microsoft’s Azure DevOps authentication updates. No AutoRABIT product upgrade is required to move from a Global PAT to an organization-scoped PAT.&#x20;

#### Who should review this?&#x20;

Review your configuration if AutoRABIT connects to repositories in Azure DevOps Services using a Personal Access Token.&#x20;

You are affected only if the PAT currently used is a Global PAT with the scope **All accessible organizations**.&#x20;

#### How to check whether you use a Global PAT&#x20;

1. Sign in to your Azure DevOps organization.&#x20;
2. Open User settings and select Personal access tokens.&#x20;
3. Filter Access scope to All accessible organizations and Status to Active.&#x20;
4. Any active token shown in this view is a Global PAT and should be replaced before December 1, 2026.&#x20;

If no active Global PATs are listed, no change is required for this Microsoft retirement.&#x20;

#### What you need to do&#x20;

**1. Identify the Azure DevOps organizations used by your repositories**&#x20;

A Global PAT can be used across multiple Azure DevOps organizations. An organization-scoped PAT is limited to one organization. If your AutoRABIT repositories span multiple Azure DevOps organizations, create a separate organization-scoped PAT for each organization.&#x20;

**2. Create an organization-scoped PAT in Azure DevOps**&#x20;

Create a new PAT and select the specific Azure DevOps organization instead of All accessible organizations.&#x20;

**Recommended permissions:**&#x20;

* **Code - Read, Write and Manage** - Required for repository operations such as commits, merges, CI jobs, deployments, and pull requests.&#x20;
* **Member Entitlement Management - Read** - Required only if you select reviewers when creating pull requests from AutoRABIT.&#x20;

Set the token expiration according to your organization’s security policy and record the expiration date for future rotation.&#x20;

**3. Add the new credential in AutoRABIT**&#x20;

In AutoRABIT, go to **Admin > Credentials** and create a credential for the new organization-scoped PAT.&#x20;

**Credential type**: Username With Password&#x20;

Enter your Azure DevOps user name in the User Name field and the PAT in the Password field.&#x20;

**Tip**: Include the Azure DevOps organization name in the credential name so it is easy to identify which credential belongs to each organization.&#x20;

**4. Update the places that use the credential**&#x20;

Review the following areas and replace the Global PAT credential with the correct organization-scoped credential where applicable:&#x20;

* Admin > Repository Manager&#x20;
* Admin > ALM Management&#x20;
* Admin > User Management for any user-specific repository or ALM credentials&#x20;
* Your own user profile if you have configured a personal repository credential&#x20;

User-specific credentials are important to review because they can override the shared credential configured for a repository or ALM connection.&#x20;

**5. Validate the connection**&#x20;

After updating the credentials, validate your normal Azure DevOps workflows before December 1, 2026. We recommend testing at least one repository operation and one CI workflow for each Azure DevOps organization you use.&#x20;

If you use pull requests from AutoRABIT, also create a test pull request and confirm that the reviewer list loads correctly.&#x20;

#### What is not changing&#x20;

* Organization-scoped PATs continue to be supported.&#x20;
* Existing repositories do not need to be re-registered simply because Microsoft is retiring Global PATs.&#x20;
* No AutoRABIT upgrade is required to replace a Global PAT with an organization-scoped PAT.&#x20;
* Azure DevOps Server connections used for Azure Boards are not affected by Microsoft’s Azure DevOps Services Global PAT retirement.&#x20;

#### Future authentication direction&#x20;

AutoRABIT is also working toward Microsoft Entra ID-based authentication for Azure DevOps Services, aligned with Microsoft’s recommended direction for modern authentication. This capability will be communicated separately when available.&#x20;

**Customers should not wait for this future capability to address the December 1, 2026, Global PAT retirement. Moving to organization-scoped PATs is the supported action available today.**&#x20;

#### Need help?&#x20;

If you need help identifying which AutoRABIT repositories use each Azure DevOps organization, or assistance updating credentials, contact AutoRABIT Support or your Customer Success Manager.&#x20;

#### Reference&#x20;

Microsoft announcement: Retirement of Global Personal Access Tokens in Azure DevOps \
[https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/)&#x20;
