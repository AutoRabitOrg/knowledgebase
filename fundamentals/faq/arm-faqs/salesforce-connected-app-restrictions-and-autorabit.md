# Salesforce Connected App Restrictions & AutoRABIT

**Will my existing AutoRABIT connections stop working?**\
No. If you connected AutoRABIT products (Vault, ARM, CodeScan Cloud) to Salesforce before the\
enforcement date in September 2025, your existing integrations will continue to work.

\
**What happens if I try to create a new connection after September 2025?**\
New connections may fail unless your Salesforce administrator assigns the new permissions\
introduced by Salesforce (Approve Uninstalled Connected Apps or Use Any API Client).

\
**Which Salesforce permission should be used?**\
If API Access Control is enabled in your org, assign 'Use Any API Client'. If it is not enabled, you may\
assign either 'Approve Uninstalled Connected Apps' or 'Use Any API Client'. These should be granted\
only to trusted integration users.

\
**Does AutoRABIT use the OAuth Device Flow?**\
No. AutoRABIT uses the OAuth 2.0 Client Credentials Flow, which creates an uninstalled connected\
app in your Salesforce org. The blocked device flow is not used by AutoRABIT.

\
**Is there a long-term solution beyond permissions?**\
Yes. AutoRABIT is actively working on enhancements to move towards installed connected apps for\
greater security and compliance. Updates will be shared in future product releases.

\
**Do I need to reinstall AutoRABIT in my Salesforce org?**\
No reinstallation is required. You only need to ensure the correct Salesforce permissions are assigned\
to your integration user for new connections after September 2025.

\
**Where can I read Salesforce’s official announcement?**\
You can view Salesforce’s official article here:\
https://help.salesforce.com/s/articleView?id=005132365\&type;=1

\
**Who should I contact if I face issues?**\
Please contact AutoRABIT Support (support@autorabit.com) for assistance with setup, permissions, or\
troubleshooting.
