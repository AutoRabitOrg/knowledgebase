# API Security

New **API Security** feature has been introduced in Guard to help customers identify and mitigate risks from third-party apps connected to Salesforce. As attacks on Salesforce orgs increase, including from unverified or over-permissive apps, this feature gives teams visibility into which apps are connected to your Salesforce, how they’re being used, and whether they pose a risk.

**API Security** tab is located under the **Risk** section. From here, users can inspect API activity for all Salesforce orgs registered in Guard:

<figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

**Value to Users:**

* **Increased Security Visibility**: Spot risky or shadow apps that might otherwise go unnoticed.
* **Proactive Defense**: Prevent over-permissive apps from giving unauthorized users access to critical data.
* **Multi-org**: Quickly assess and compare API risks across all Salesforce orgs.

### Overview

API Security dashboard aggregates all Connected Apps, Installed Packages, OAuth scopes/tokens, Named Credentials, etc.

* Correlates who/what connected, what scopes were granted, what’s actually used, and when it was last active.
* Highlights over-permissive and unverified connections

### How It Works

1. Discover & Normalize: We inventory integrations across all registered orgs and present findings in the easy-to-understand dashboard.
2. Verify Installation Status: Verified or Unverified.
3. We compare granted scopes/permissions to observed behavior (API calls, objects touched, endpoints hit) to flag potential over-privilege.
4. Review risk scores to rank items for investigation.
5. Monitor connected applications over time.

&#x20;
