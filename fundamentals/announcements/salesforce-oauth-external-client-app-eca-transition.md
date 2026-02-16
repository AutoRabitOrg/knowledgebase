# Salesforce OAuth External Client App (ECA) Transition

### Overview

Salesforce is transitioning from the legacy Connected App model to External Client Apps (ECA) for new OAuth integrations. This change affects how new integrations are registered within Salesforce orgs and is tied to the Salesforce Spring ’26 release. For more details from Salesforce, see their official announcement: [https://help.salesforce.com/s/articleView?id=005228017\&type=1](https://help.salesforce.com/s/articleView?id=005228017\&type=1).

AutoRABIT is actively updating its products to support this new Salesforce framework. This article addresses common questions and clarifies what this means for your existing and future Salesforce integrations.

### Does this impact my existing Salesforce integration?

No. Existing Salesforce connections in AutoRABIT’s products will continue to work as they do today.

If your Salesforce org is already connected to AutoRABIT’s products using a Connected App, no action is required. There is no expected downtime and no disruption to current integrations.

This change only affects new Salesforce org registrations.

### What exactly is changing in Salesforce?

Salesforce is replacing Connected Apps with External Client Apps for new OAuth-based integrations. In upcoming Salesforce releases, customers will no longer be able to create new Connected Apps and must instead use the External Client App framework.

This is a Salesforce platform change intended to modernize the integration and authentication model. For more information, refer to Salesforce’s documentation: [https://help.salesforce.com/s/articleView?id=005228017\&type=1](https://help.salesforce.com/s/articleView?id=005228017\&type=1).

### Who is affected by this change?

You may be impacted if:

* You are registering a new Salesforce org in AutoRABIT’s products.
* You recently created or refreshed a Salesforce sandbox.
* You are onboarding AutoRABIT’s products for the first time.

If your Salesforce org is already connected to AutoRABIT’s products, you are not impacted.

### What happens if I try to register a new org today?

Until AutoRABIT’s support for External Client Apps is released, new Salesforce org registrations using the updated Salesforce framework may not complete successfully.

Salesforce has indicated the following regarding continued use of connected apps as part of the Spring ’26 release:

> If you need to continue using existing connected apps, you can do so. However, no new connected apps can be created with the Spring ‘26 release unless enabled by Salesforce Support. In future releases, Salesforce Support won’t be able to enable the creation of new connected apps.

**Workaround:**\
If you must register a new Salesforce org with AutoRABIT before our ECA support is available, you can open a case with Salesforce Support and request that they temporarily enable the creation of new connected apps for your org (where applicable, per Salesforce policy). Once enabled, you can complete the org registration using a Connected App as before.

We are actively working on full compatibility with External Client Apps and will notify customers as soon as support is available.

### Will I need to reconnect my existing Salesforce orgs?

No. Existing integrations will continue functioning normally.

Reconnection would only be required if:

* The existing OAuth connection is manually revoked.
* The Connected App is deleted in Salesforce.
* Credentials are invalidated for another administrative reason.

Otherwise, no migration or reconfiguration is required at this time.

### Why is Salesforce making this change?

Salesforce is modernizing its integration model to improve security, modularize authentication plugins, and provide clearer lifecycle management for external integrations.

This change applies across the Salesforce ecosystem and is not specific to AutoRABIT. Additional details are available in Salesforce’s release documentation: [https://help.salesforce.com/s/articleView?id=005228017\&type=1](https://help.salesforce.com/s/articleView?id=005228017\&type=1).

### What about Salesforce sandboxes?

Salesforce sandboxes require separate app registrations.

If you create or refresh a sandbox, you may need to register it again once AutoRABIT’s ECA support is released. Existing connected sandboxes will continue to function as expected.

### Is there any security impact?

There is no negative security impact.

Existing AutoRABIT integrations remain secure. AutoRABIT continues to use OAuth 2.0 best practices and encrypted token storage. The Salesforce platform change does not weaken or expose existing integrations.

### What is AutoRABIT doing?

AutoRABIT is updating its products to support Salesforce External Client Apps using OAuth 2.0 Web Server Flow.

The update will include:

* A guided Salesforce registration workflow
* Clear setup instructions
* Live validation during connection
* Improved error handling
* Enhanced visibility into integration health

We will announce availability as soon as the update is released.

### When will support be available?

Support for Salesforce External Client Apps is planned to be available by the end of February 2026. Customers will be notified through in-app messaging and updated documentation when the feature is released.

### Additional Questions

If you have further questions about how this change affects your organization, please reach out to AutoRABIT Support. Our team is available to assist and provide clarity on your specific environment.
