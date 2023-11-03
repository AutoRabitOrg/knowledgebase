# Enable Enhanced Domains

## Introduction <a href="#introduction" id="introduction"></a>

Enhanced domains are the next version of My Domain. My domain replaces the standard subdomain in the URL of your Salesforce Org with your company-specific subdomain, including URLs for your Experience Cloud sites, Salesforce Sites, Visualforce pages, and content files.

## Do I need enhanced domains? <a href="#do-i-need-enhanced-domains" id="do-i-need-enhanced-domains"></a>

Salesforce requires customers to use enhanced domains by Winter ’23 release to comply with the latest browser and security standards.

## How do I enable enhanced domains? <a href="#how-do-i-enable-enhanced-domains" id="how-do-i-enable-enhanced-domains"></a>

Enhanced domains affect all application URLs; testing in a sandbox before deployment is recommended and should be done before Winter ’23 release, starting in August 2022 for sandboxes and October 2022 for production orgs.

Reference: [https://help.salesforce.com/s/articleView?id=sf.domain\_name\_enhanced.htm](https://help.salesforce.com/s/articleView?id=sf.domain\_name\_enhanced.htm)

1. Access **Setup** from Salesforce and select **My Domain**.
2. Select **Edit** under **My Domain Details**.
3. Select the checkbox: **Use enhanced domains**.
4. Click **Save**.

Your org doesn't qualify for enhanced domains if you don't see the Use enhanced domains option.

## What if I do not enable the enhanced domain? <a href="#what-if-i-do-not-enable-the-enhanced-domain" id="what-if-i-do-not-enable-the-enhanced-domain"></a>

If enhanced domains aren't deployed before the Winter ’23 release, Salesforce will automatically set one based on your org’s ID.

## Points to Consider in ARM <a href="#points-to-consider-in-arm" id="points-to-consider-in-arm"></a>

Before performing any deployment or CI activities in ARM, reauthenticate your registered org via the **Salesforce Org Management** page. Reauthentication will update the most recent org changes.

## Use Cases <a href="#use-cases" id="use-cases"></a>

**Query 1:** How is the backup request ID hitting the redirect URL successfully while deployment, on the other hand, is failing (before Salesforce Org is reauthenticated to update the URL under ARM)?

**Answer:** The deployment is carried out on the agent side based on the configured CI job, and the backup is carried out on the ARM server side with an updated refresh token. The Salesforce Org's redirection was modified during this process, and the deployment failed because the re-authentication was not yet complete.

**Solution:** Once Salesforce Org has been reauthenticated, save the job again.

***

**Query 2:** Considering the possibility of just the build package being backed up, why is the deployment log referencing the target org?

**Answer:** Backup is only packaged from the target org for the deployable components.
