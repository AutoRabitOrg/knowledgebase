# Enable Enhanced Domains

## Introduction <a href="#introduction" id="introduction"></a>

Enhanced domains are the next iteration of My Domain in Salesforce. They replace the default Salesforce subdomain with a company-specific one across all URLs, including Experience Cloud sites, Salesforce sites, Visualforce pages, and content files.

## Do I Need Enhanced Domains? <a href="#do-i-need-enhanced-domains" id="do-i-need-enhanced-domains"></a>

Yes. Salesforce requires all customers to enable enhanced domains by the **Winter ’23** release to comply with modern browser and security standards.

## How to Enable Enhanced Domains <a href="#how-do-i-enable-enhanced-domains" id="how-do-i-enable-enhanced-domains"></a>

Enabling enhanced domains impacts all application URLs. **Testing in a sandbox** is highly recommended and should be completed before rollout deadlines: **August 2022 for sandboxes** and **October 2022 for production orgs**.

**Reference:** [Salesforce Help: Enhanced Domains](https://help.salesforce.com/s/articleView?id=sf.domain_name_enhanced.htm)

### Steps:

1. Go to **Setup** in Salesforce and select **My Domain**.
2. Click **Edit** under **My Domain Details**.
3. Select the checkbox **Use enhanced domains**.
4. Click **Save**.

> If the **Use enhanced domains** option is not available, your org may not qualify yet.

## What If I Don’t Enable Enhanced Domains? <a href="#what-if-i-do-not-enable-the-enhanced-domain" id="what-if-i-do-not-enable-the-enhanced-domain"></a>

If enhanced domains are not enabled before the Winter ’23 release, Salesforce will automatically assign one based on your org’s ID.

## Points to Consider in ARM <a href="#points-to-consider-in-arm" id="points-to-consider-in-arm"></a>

Before executing any deployment or CI activities in ARM, you must **reauthenticate** the Salesforce org through the **Salesforce Org Management** page. This updates the ARM system with the org’s most recent domain changes.

## Use Cases <a href="#use-cases" id="use-cases"></a>

### Query 1:

**Q:** How is the backup request ID hitting the redirect URL successfully while deployment fails (prior to Salesforce Org reauthentication)?

**A:** Deployment runs on the agent side based on the CI job configuration, while backup is performed on the ARM server side using a refreshed token. If the Salesforce Org's redirection URL changed and reauthentication has not been completed, deployment fails due to outdated redirect configurations.

**Solution:** Reauthenticate the Salesforce Org and then re-save the job in ARM.

***

### Query 2:

**Q:** If only the build package is backed up, why does the deployment log reference the target org?

**A:** Backup packaging pulls deployable components from the **target org**, which is why the deployment log reflects the target org's context.
