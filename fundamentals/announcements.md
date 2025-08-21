# Announcements

Preparing for Salesforce Connected App Usage

## Preparing for Salesforce Connected App Usage Restrictions

### Guidance for AutoRABIT Customers

**Overview**

Salesforce has announced changes to how uninstalled connected apps function in customer orgs,

effective September 2025. These changes impact AutoRABIT products that connect to your Salesforce

environments using the OAuth 2.0 Client Credentials Flow.

### What’s Changing in Salesforce

1. Uninstalled connected apps restricted — New authorizations will be blocked unless specific permissions are granted.
2. OAuth 2.0 Device Flow blocked — Not used by AutoRABIT.
3. New permissions introduced:
   1. Approve Uninstalled Connected Apps
   2. Use Any API Client

### Impact on AutoRABIT Products

1. Vault, ARM, and CodeScan Cloud connect to Salesforce via Client Credentials Flow, which creates an uninstalled connected app.
2. Existing connections (before September 2025): Will continue to work.
3. New connections (after September 2025): May fail unless permissions are updated by your Salesforce admin.

### Actions Required

1. Identify AutoRABIT Connected Apps:
   1. Go to Setup → Connected Apps OAuth Usage in Salesforce.
   2. Locate entries linked to AutoRABIT.
2. Update User Permissions:
   1. If API Access Control is enabled: Assign “Use Any API Client.”
   2. If API Access Control is not enabled: Assign either “Approve Uninstalled Connected Apps” or “Use Any API Client.”

> Grant these permissions only to trusted integration users.

3. Plan for Future Stability:
   1. AutoRABIT is preparing enhancements to support installed connected apps for long-term compliance.

### Best Practices

1. Use a dedicated integration user for AutoRABIT.
2. Grant only minimum required permissions.
3. Review unused connected apps regularly and remove them.

### Need Help?

1. Contact AutoRABIT Support (support@autorabit.com).
2. Refer to Salesforce’s announcement: Prepare for Connected App Usage Restrictions Change.

### Additional Resources

Refer to the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=005132365\&type=1) below for additional details.
