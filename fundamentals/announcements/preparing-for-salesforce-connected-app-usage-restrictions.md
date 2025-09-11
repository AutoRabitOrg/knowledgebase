# Preparing for Salesforce Connected App Usage Restrictions

### **Overview**

Salesforce has announced changes to how uninstalled connected apps function in customer orgs, effective September 2025. These changes impact AutoRABIT products that connect to your Salesforce environments using the OAuth 2.0 Client Credentials Flow.

### What’s Changing in Salesforce

1. Uninstalled connected apps restricted — New authorizations will be blocked unless specific permissions are granted.

> **Note:** The existing connections between AutoRABIT and Salesforce are not going to be impacted by this change

2. OAuth 2.0 Device Flow blocked — Not used by AutoRABIT.
3. New permissions introduced:
   1. Approve Uninstalled Connected Apps
   2. Use Any API Client

### Impact on AutoRABIT Products

1. Vault, ARM, and CodeScan Cloud connect to Salesforce via Client Credentials Flow, which creates an uninstalled connected app.
2. Existing connections (before September 2025): Will continue to work.
3. New connections (after September 2025): May fail unless permissions are updated by your Salesforce admin.

### Actions Required

_For existing customers with an already connected Org/s to AutoRABIT_\
No action is required.

Recommended configuration:\
&#xNAN;_&#x46;or existing customers, adding net new Salesforce Sandbox Orgs_

**Install Connected App**

1. In your Salesforce Org, Navigate to Setup → type Connected Apps OAuth Usage in the Quick Find box.
2. Find the AutoRABIT connected app in the list. If it’s not installed, there will be an Install button next to it.
3. Click Install, then confirm on the subsequent page.

**Optional Configuration:**\
&#xNAN;_&#x41;pplies to initial authentications with AutoRABIT made after the connected apps security change made by Salesforce, or net new production orgs (this will be updated, as more information becomes available from Salesforce)_

Actions Required

1. Identify AutoRABIT Connected Apps:
   1. Go to Setup → Connected Apps OAuth Usage in Salesforce.
   2. Locate entries linked to AutoRABIT.
2. Update User Permissions:
   1. If API Access Control is enabled: Assign “Use Any API Client.”
   2. If API Access Control is not enabled: Assign either “Approve Uninstalled Connected Apps” or “Use Any API Client.”

Grant these permissions only to trusted integration users.

### Best Practices

1. Use a dedicated integration user for AutoRABIT.
2. Grant only minimum required permissions.
3. Review unused connected apps regularly and remove them.

### Need Help?

1. Contact AutoRABIT Support (support@autorabit.com).
2. Refer to Salesforce’s announcement: Prepare for Connected App Usage Restrictions Change.

### Additional Resources

Refer to the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=005132365\&type=1) below for additional details.

### FAQ

**Will my existing AutoRABIT connections stop working?** No. If you connected AutoRABIT products (Vault, ARM, CodeScan Cloud) to Salesforce before the enforcement date in September 2025, your existing integrations will continue to work.

**What happens if I try to create a new connection after September 2025?** New connections may fail unless your Salesforce administrator assigns the new permissions introduced by Salesforce (Approve Uninstalled Connected Apps or Use Any API Client).

**Which Salesforce permission should be used?** If API Access Control is enabled in your org, assign 'Use Any API Client'. If it is not enabled, you may assign either 'Approve Uninstalled Connected Apps' or 'Use Any API Client'. These should be granted only to trusted integration users.

**Does AutoRABIT use the OAuth Device Flow?** No. AutoRABIT uses the OAuth 2.0 Client Credentials Flow, which creates an uninstalled connected app in your Salesforce org. The blocked device flow is not used by AutoRABIT.

**Is there a long-term solution beyond permissions?** Yes. AutoRABIT is actively working on enhancements to move towards installed connected apps for greater security and compliance. Updates will be shared in future product releases.

**Do I need to reinstall AutoRABIT in my Salesforce org?** No reinstallation is required. You only need to ensure the correct Salesforce permissions are assigned to your integration user for new connections after September 2025.

**Where can I read Salesforce’s official announcement?** You can view Salesforce’s official article here: https://help.salesforce.com/s/articleView?id=005132365\&type;=1

**Who should I contact if I face issues?** Please contact AutoRABIT Support (support@autorabit.com) for assistance with setup, permissions, or troubleshooting.
