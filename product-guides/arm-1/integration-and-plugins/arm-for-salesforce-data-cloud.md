# ARM for Salesforce Data Cloud

AutoRABIT provides CI/CD support for Salesforce Data Cloud, enabling organizations to manage and deploy supported Data Cloud metadata through automated pipelines. This document outlines the integration capabilities, supported metadata types, and deployment considerations based on what is available through Salesforce's Metadata API.&#x20;

## Integration Features&#x20;

* Automated retrieval for supported metadata types and deployment&#x20;
* Version control integration for supported metadata types (like some Data Streams, Calculated Insights, Data Model Objects, etc.)&#x20;
* CI/CD pipeline support for automated deployments&#x20;

## Supported Metadata Types&#x20;

AutoRABIT supports deployment of the following Data Cloud metadata types through the Salesforce Metadata API:&#x20;

<table><thead><tr><th width="206">Category</th><th>Supported Types</th></tr></thead><tbody><tr><td>Activation </td><td>ActivationPlatform, ActivationPlatformField, ActvPfrmDataConnectorS3, ActvPlatformAdncIdentifier, ActvPlatformFieldValue </td></tr><tr><td>Data Connectors </td><td>DataConnectorIngestApi, DataConnectorS3, ExternalDataConnector </td></tr><tr><td>Data Sources </td><td>DataSource, DataSourceField, DataSourceObject, DataSourceBundleDefinition </td></tr><tr><td>Data Streams </td><td>DataStreamDefinition, DataStreamTemplate </td></tr><tr><td>Mapping &#x26; Relations </td><td>DataSrcDataModelFieldMap, FieldSrcTrgtRelationship, ObjectSourceTargetMap </td></tr><tr><td>External Data </td><td>ExternalDataSource, ExternalDataTranObject </td></tr><tr><td>Marketing </td><td>MktCalcInsightObjectDef, MktDataTranObject </td></tr><tr><td>Other </td><td>SharingAppDefinition, DataPackageKitObject </td></tr></tbody></table>

### Currently Unsupported Types&#x20;

* MarketSegmentDefinition&#x20;
* DataPackageKitDefinition&#x20;

## Known Limitations & Manual Steps&#x20;

**Re-authentication of External Connections** \
Data connectors or authentication details (API keys, tokens, etc.) may require updating in the target environment after deployment.&#x20;

**Data Stream Activation** \
Even though Data Stream configurations can be deployed, they typically require manual activation or scheduling in the target environment.&#x20;

**Manual Recreation of Unsupported Metadata** \
Any component not currently covered by the Metadata API—for example, certain market segmentation rules—requires manual creation and configuration.&#x20;

## Environment Considerations&#x20;

Customers may operate Data Cloud in separate Production instances or within the same core Salesforce org. It is crucial to align your Data Cloud environment strategy with your overarching DevOps practices:&#x20;

**Governance & Version Control:** Track Salesforce Data Cloud metadata in the same version control repository as your Salesforce customizations whenever possible. For components not supported by the Metadata API, export definitions via the UI, store JSON in Git, and deploy using API calls or custom scripts with manual validation in the target org.&#x20;

**Release Pipelines:** Use AutoRABIT’s CI/CD pipelines to automate build and deployment processes, even if some post-deployment re-authentication steps are manual.&#x20;

## Best Practices & Recommendations&#x20;

**Combine Deployments** \
Deploy Data Cloud metadata alongside standard Salesforce metadata to maintain consistency and reduce dependency issues.&#x20;

**Document Manual Steps** \
Clearly document post-deployment tasks such as re-authentication or Data Stream activation. Assign these tasks to the appropriate team members as part of your release process.&#x20;

**Leverage CI/CD Pipelines** \
Use AutoRABIT’s pipelines to automatically retrieve Data Cloud metadata changes from your version control system. While you may still have to handle certain manual tasks, automation of metadata retrieval and deployment reduces errors and speeds up delivery.&#x20;

**Plan for Unsupported Metadata** \
Because certain Data Cloud components (like MarketSegmentDefinition, DataPackageKitDefinition) remain unsupported by the Metadata API, account for any manual effort needed in each environment. Keep a checklist of these tasks for streamlined release management.&#x20;

**Coordinate with Salesforce Roadmap** \
Salesforce continues to evolve Data Cloud capabilities and metadata coverage. Stay in touch with your Salesforce contacts and AutoRABIT support for updates on new metadata types or changes that may simplify your deployments.&#x20;

**Future Updates**&#x20;

AutoRABIT continuously expands its Data Cloud support as Salesforce releases new features and metadata types. Contact your Customer Success Manager for the latest updates on supported features.&#x20;

&#x20;

&#x20;
