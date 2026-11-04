# Excluded Metadata Types in ARM

### Overview

This article lists the Salesforce metadata types that are currently not supported in AutoRABIT Metadata (ARM).

While these metadata types are not supported at present, our team is actively working to enable support for a subset of them in upcoming releases.

Understanding these exclusions will help you:

* Plan deployments more effectively
* Avoid gaps during metadata retrieval
* Identify metadata that may require manual handling

### 1. Planned for Support

The following metadata types are currently not supported in ARM, but they are under active evaluation and planned for future support:

* CustomIndex
* CustomObjectBinding
* DataSourceField
* EmbeddedServiceFieldService
* ExperienceContainer
* ExperiencePropertyTypeBundle
* ManagedContentTypeBundle
* ManagedTopic
* PublicKeyCertificate
* PublicKeyCertificateSet
* ReferencedDashboard
* ServiceProcess
* WorkflowFlowAutomation

These metadata types are available through Salesforce APIs, and support for them is being prioritized in ARM.

### 2. Currently Not Supported

The following metadata types are currently not supported in ARM. This includes metadata types that either do not have Salesforce API support or have limited or inconsistent behavior:

* DiscoveryStory
* ExternalAIModel
* LightningOutApp
* OmniTrackingGroup
* OmniExtTrackingDef
* SalesWorkQueueSettings
* ExperiencePropertyTypeBundle (specific scenarios)
* AccountingFieldMapping
* ActivationPlatformActvAttr
* ActivationPlatformField
* ActvPfrmDataConnectorS3
* ActvPlatformAdncIdentifier
* ActvPlatformFieldValue
* ActvPlatformOAuthConnector
* AIScoringModelDefinition
* ClaimFinancialSettings
* ExternalDataTranObject
* ExtlClntAppSamlConfigurablePolicies
* IdentityVerificationProcDtl
* IdentityVerificationProcFld
* OauthTokenExchangeHandler
* ProcessFlowMigration

### Impact

For all metadata types listed above:

* They are excluded during metadata retrieval
* They are not included in ARM deployments
* They do not appear in metadata discovery

### Recommended Actions

To avoid deployment issues, we recommend the following:

* Do not include unsupported metadata types in deployment packages
* Use manual configuration in Salesforce where necessary
* Validate metadata with limited or inconsistent support thoroughly before deployment
* Monitor ARM release updates for newly supported metadata types

### Important Note

This exclusion list applies only to **DX-based retrieval and deployment (Salesforce CLI / SF CLI)**.

For **non-DX flows using the Metadata API**, the metadata types listed above should continue to work unless otherwise noted.
