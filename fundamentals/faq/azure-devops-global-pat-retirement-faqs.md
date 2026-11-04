---
hidden: true
noIndex: true
---

# Azure DevOps Global PAT Retirement FAQs

## Azure DevOps Global PAT Retirement FAQs

## Understanding the Change&#x20;

### 1. What is changing, and when?&#x20;

Microsoft is retiring Global Personal Access Tokens (PATs) in Azure DevOps Services on December 1, 2026. Global PATs provide access across all Azure DevOps organizations accessible to the token owner.&#x20;

After retirement, integrations that still authenticate with a Global PAT will stop working. Replace affected tokens before December 1, 2026, to avoid disruption. [Microsoft Dev Blogs](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/?utm_source=chatgpt.com)&#x20;

### 2. Which AutoRABIT connections should I review?&#x20;

Review both your Azure DevOps repository connections and your Azure DevOps application lifecycle management (ALM) connections, including connections used for work items.&#x20;

Check shared credentials and any user-specific credentials that override them. A working repository connection does not establish that your ALM connection has been updated. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

## Checking Your Tokens&#x20;

### 3. How can I tell whether I am using a Global PAT?&#x20;

Check the PAT in Azure DevOps and confirm whether it is scoped to “All accessible organizations” or to a specific named organization. A PAT scoped to “All accessible organizations” is a Global PAT.&#x20;

1. Sign in to your Azure DevOps organization.&#x20;
2. Open User settings > Personal access tokens.&#x20;
3. Set the Access scope filter to All accessible organizations and Status to Active.&#x20;
4. Review the listed tokens and identify any used by AutoRABIT.&#x20;

Tokens listed under that filter are Global PATs. A token scoped to a specific, named Azure DevOps organization is an organization-scoped PAT. [Microsoft Dev Blogs](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/?utm_source=chatgpt.com)&#x20;

### 4. Azure DevOps shows a single organization, but ARM shows “Global.” Do I need to change anything?&#x20;

The “Global” value shown in ARM refers to how the credential is shared within ARM. It does not indicate whether the Azure DevOps PAT itself is Global or organization-scoped.&#x20;

In Azure DevOps, the token’s organization scope determines which Azure DevOps organization or organizations it can access. In ARM, the credential scope determines whether the stored credential is shared with the team or private to its owner.&#x20;

Thus, an organization-scoped Azure DevOps PAT can be stored as a Global credential in ARM. Changing ARM’s credential scope to Private does not convert an Azure DevOps Global PAT into an organization-scoped PAT. [Microsoft Dev Blogs](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/?utm_source=chatgpt.com)&#x20;

### 5. Do I need to replace a PAT that is already organization-scoped?&#x20;

No replacement is required solely because of the Global PAT retirement. Organization-scoped PATs are not being retired by this change.&#x20;

Continue monitoring the token’s expiration, permissions, and your organization’s security policies. An organization-scoped token can still stop working if it expires, is revoked, or loses the access required by the integration. [Microsoft Dev Blogs](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/?utm_source=chatgpt.com)&#x20;

## Updating AutoRABIT ARM&#x20;

### 6. Do I need to upgrade ARM or register my repositories again?&#x20;

No. This migration does not require an ARM upgrade or repository re-registration. However, affected stored credentials must be updated. “No product change required” does not mean “no customer action required.” [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

### 7. How do I replace a Global PAT used by ARM?&#x20;

Create an organization-scoped PAT in Azure DevOps, then replace the token stored in the corresponding ARM credential.&#x20;

1. In Azure DevOps, open Personal access tokens and select New Token.&#x20;
2. Select the specific organization, rather than All accessible organizations. Set an expiration date and the permissions required for the connection.&#x20;
3. Copy the new token and store it securely.&#x20;
4. In ARM, go to Admin > Credentials and open the credential that contains the old Global PAT.&#x20;
5. Replace the old value in the Token/Password field with the new organization-scoped PAT, then save.&#x20;

For Azure DevOps credentials configured in ARM using Username with Password, the PAT is stored in the Token/Password field. Replace the existing Global PAT value with the new organization-scoped PAT. &#x20;

Keep the token out of email, chat, and screenshots. The documentation supports storing the PAT in the password field. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/azure-devops)&#x20;

### 8. Should I update repository and ALM connections separately?&#x20;

Yes. Check them independently. As clarified in the supplied thread, repository and ALM connections are configured separately and may use different credentials. Updating one does not establish that the other has been migrated.&#x20;

Review Admin > Repository Manager, Admin > ALM Management, user-specific settings in Admin > User Management, and personal repository credentials in your profile. Update every location still using an affected credential. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

### 9. What should I do if my repositories span multiple Azure DevOps organizations?&#x20;

Create a separate organization-scoped PAT for each Azure DevOps organization and associate the appropriate credential with each connection. If ARM connects to multiple Azure DevOps organizations using PAT authentication, create an organization-scoped PAT for each Azure DevOps organization and associate the appropriate credential with each connection. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

### 10. How do I confirm that the migration worked?&#x20;

After updating the credential, test the repository connection and run a normal repository operation used by your team. For ALM, use Test Connection and confirm that work-item operations continue to work. &#x20;

For Azure DevOps ALM, use Test Connection and verify that the work-item operation your team normally uses still succeeds. A successful test of one connection does not validate another independently configured connection. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/azure-devops)&#x20;

## Authentication Alternatives and Support&#x20;

### 11. Our organization prohibits all PATs. Will AutoRABIT provide another authentication method?&#x20;

AutoRABIT is working on Microsoft Entra ID–based authentication for Azure DevOps as an alternative to PAT authentication. Target delivery is mid-November 2026; availability and release details will be communicated separately.&#x20;

Contact Support or your Customer Success Manager to discuss your policy and confirm available options. Do not plan around an unconfirmed release date or assume a policy exception. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

### 12. Does this retirement affect on-premises TFS or Azure DevOps Servers?&#x20;

No. This retirement applies to the cloud-based Azure DevOps Services product. Microsoft states that it is not changing Global PATs in Azure DevOps Server as part of this retirement. [Microsoft Dev Blogs](https://devblogs.microsoft.com/devops/retirement-of-global-personal-access-tokens-in-azure-devops/?utm_source=chatgpt.com)&#x20;

### 13. Who should I contact for help?&#x20;

Contact AutoRABIT Support or your Customer Success Manager to help identify affected connections or update credentials. [AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/fundamentals/announcements/azure-devops-global-personal-access-token-retirement-on-december-1-2026)&#x20;

### 14. ARM shows “Global,” but Azure DevOps shows my organization name. Am I impacted?&#x20;

No. If Azure DevOps shows that the PAT is scoped to a specific organization, the PAT is organization-scoped and is not affected by the December 1, 2026, global PAT retirement. The “Global” value displayed in ARM refers to ARM credential sharing and is unrelated to the Azure DevOps PAT organization scope.&#x20;

&#x20;
