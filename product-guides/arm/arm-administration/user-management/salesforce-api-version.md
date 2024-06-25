# Salesforce API version

ARM's ability to support Salesforce standard and custom objects is determined by the Salesforce API version used. ARM now supports **Salesforce API version 61**, which means it can support any Salesforce standard or custom object that requires Salesforce API version 61 or earlier.

{% hint style="info" %}
**Important Note:** Only users on an ARM shared instance will see the changes since the Salesforce API version is being updated to **61** as part of weekly hotfixes to shared instances only.
{% endhint %}

**Troubleshooting:**

Ensure your Salesforce API version in ARM matches the API version of the Salesforce org. Failure to match the version may result in metadata object commit/deployment failure in your target environment.&#x20;

Use case:

* **API version set in ARM: 61.0**
* **Salesforce Org API version: 61.0**

To identify which Salesforce API version you are using, please refer to [Find Salesforce Edition and API version](https://help.salesforce.com/s/articleView?id=000334996\&type=1).

#### Salesforce API Supported Metadata Types

The following sections highlight the newly supported metadata types for each API version.

Metadata types added as part of the **API 61** upgrade:

* EnablementMeasureDefinition
* EnablementProgramDefinition



Metadata types added as part of the **API 59** upgrade:

| MetadataType                         | Extension     | FolderName                 |
| ------------------------------------ | ------------- | -------------------------- |
| ExternalClientApplication            | .eca          | externalClientApps         |
| ExtlClntAppGlobalOauthSettings       | .ecaGlblOauth | extlClntAppGlobalOauthSets |
| ExtlClntAppOauthConfigurablePolicies | .ecaOauthPlcy | extlClntAppOauthPolicies   |
| ExtlClntAppOauthSettings             | .ecaOauth     | extlClntAppOauthSettings   |
| FlowTransform                        | NA            | NA                         |

Below is a list of the Metadata types supported, which were added as part of **API 58** release -

| MetadataType                   | Extension                   | FolderName                      |
| ------------------------------ | --------------------------- | ------------------------------- |
| `AccountingFieldMapping`       | `.accountingFieldMapping`   | `accountingFieldMappings`       |
| `AIScoringModelDefinition`     | `.aiScoringModelDefinition` | `aiScoringModelDefinitions`     |
| `DataWeaveResource`            | `.dwl`                      | `dw`                            |
| `PlatformEventSettings`        | `.settings`                 | `settings`                      |
| `ExperiencePropertyTypeBundle` | NR                          | `experiencePropertyTypeBundles` |
| ProcessFlowMigration           | NA                          | NA                              |



**API 57.0 newly Supported Metadata Types**

| OmniSupervisorConfig      | PipelineInspMetricConfig | DataImportManagementSettings |
| ------------------------- | ------------------------ | ---------------------------- |
| HighVelocitySalesSettings | Territory2AccessLevel    | AdvAccountForecastSet        |

{% hint style="info" %}
**Important Note:** **OmniSupervisorConfig** metadata type is not supported in **Unlocked Package** creation, but is working as expected in **Commits** and **Deployments**.
{% endhint %}

**API 56.0 newly Supported Metadata Types**

<table data-header-hidden><thead><tr><th width="94"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>S. No.</strong></td><td><strong>Metadata Type</strong></td><td><strong>Folder Name</strong></td><td><strong>File Extension</strong></td></tr><tr><td>1</td><td>AIUsecaseDefinition</td><td>aiUsecaseDefinitions</td><td>.aiUsecaseDefinitions</td></tr><tr><td>2</td><td>DigitalExperienceBundle</td><td>digitalExperiences</td><td>.digitalExperience</td></tr><tr><td>3</td><td>DigitalExperienceConfig</td><td>digitalExperienceConfigs</td><td>.digitalExperienceConfig</td></tr><tr><td>4</td><td>EventRelayConfig</td><td>eventRelays</td><td>.eventRelay</td></tr><tr><td>5</td><td>OauthOidcSettings</td><td>settings</td><td>.settings</td></tr></tbody></table>

{% hint style="info" %}
**Important Note:** The following fields have been deprecated on the NamedCredential metadata type in API version 56.0. These fields are valid only when namedCredentialType is null or set to Legacy.
{% endhint %}

* authProvider
* authTokenEndpointUrl
* awsAccessKey
* awsAccessSecret
* awsRegion
* awsService
* certificate
* endpoint
* jwtAudience
* jwtFormulaSubject
* jwtIssuer
* jwtSigningCertificate
* jwtTextSubject
* jwtValidityPeriodSeconds
* oauthRefreshToken
* oathScope
* oathToken
* outboundNetworkConnection
* password
* principalType
* protocol
* username

**API 55.0 newly Supported Metadata Types**

The newly supported metadata types are available on the Salesforce website, link: [https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages\_intro\_whats\_new.htm](https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages\_intro\_whats\_new.htm)

Troubleshooting:Below is the list of the metadata types in the _API 55.0 version_ that are not picked up during deployment or CI job operation:

* ARMAssessmentQuestion
* AssessmentQuestionSet
* ForecastingFilterConditions
* ForecastingFilters
* ForecastingSourceDefinitions
* ForecastingTypes
* ForecastingTypeSources

**API 54.0 newly Supported Metadata Types**

<table><thead><tr><th width="83">S. No.</th><th>Metadata Type</th><th>Folder Name</th><th>File Extension</th></tr></thead><tbody><tr><td>1</td><td>LoyaltyProgramSetup</td><td>loyaltyProgramSetups</td><td>.loyaltyProgramSetup</td></tr><tr><td>2</td><td>RecordAlertCategory</td><td>recordAlertCategories</td><td>.recordAlertCategory</td></tr></tbody></table>

**API 53.0 Supported Metadata Types**

Please refer [here](https://help.salesforce.com/s/articleView?id=release-notes.rn\_api\_objects.htm\&type=5\&release=234) to find the list of supported Salesforce objects supported on Salesforce API 53.0 version.

**API 52.0 newly Supported Metadata Types**

<table><thead><tr><th width="78">S. No.</th><th>Metadata Type</th><th>File Extension</th><th>Folder Name</th></tr></thead><tbody><tr><td>1</td><td>EinsteinAgentSettings</td><td>EinsteinAgent.settings</td><td>settings</td></tr><tr><td>2</td><td>FieldRestrictionRule</td><td>.rule</td><td>fieldRestrictionRules</td></tr><tr><td>3</td><td>ForecastingObjectListSettings</td><td>ForecastingObjectList.settings</td><td>settings</td></tr><tr><td>4</td><td>ForecastingSourceDefinition</td><td>.forecastingSourceDefinition</td><td>forecastingSourceDefinitions</td></tr><tr><td>5</td><td>ForecastingType</td><td>.forecastingType</td><td>forecastingTypes</td></tr><tr><td>6</td><td>ForecastingTypeSource</td><td>.forecastingTypeSource</td><td>ForecastingTypeSources</td></tr><tr><td>7</td><td>FunctionReference(Beta)</td><td>.functions</td><td>functions</td></tr><tr><td>8</td><td>MktCalcInsightObjectDef</td><td>.mktCalcInsightObjectDef</td><td>mktCalcInsightObjectDefs</td></tr><tr><td>9</td><td>OcrSampleDocument</td><td>.ocrSampleDocument</td><td>ocrSampleDocuments</td></tr><tr><td>10</td><td>OcrTemplate</td><td>.ocrTemplate</td><td>ocrTemplates</td></tr><tr><td>11</td><td>RestrictionRule</td><td>.rule</td><td>restrictionRules</td></tr><tr><td>12</td><td>ServiceCloudVoiceSettings</td><td>ServiceCloudVoice.settings</td><td>settings</td></tr><tr><td>13</td><td>WorkforceEngagementSettings</td><td>WorkforceEngagement.settings</td><td>settings</td></tr></tbody></table>

**API 51.0 newly  Supported Metadata Types**

| S. No | Metadata Type                 | File Sufix                     | Folder Name                    |
| ----- | ----------------------------- | ------------------------------ | ------------------------------ |
| 1     | BatchCalcJobDefinition        | .batchCalcJobDefinition        | batchCalcJobDefinitions        |
| 2     | BatchProcessJobDefinition     | .batchProcessJobDefinition     | batchProcessJobDefinitions     |
| 3     | CleanDataService              | .cleanDataService              | cleanDataServices              |
| 4     | DecisionTable                 | .decisionTable                 | decisionTables                 |
| 5     | DecisionTableDatasetLink      | .decisionTableDatasetLink      | decisionTableDatasetLinks      |
| 6     | DuplicateRule                 | .duplicateRule                 | duplicateRules                 |
| 7     | FieldSrcTrgtRelationship      | .fieldSrcTrgtRelationship      | fieldSrcTrgtRelationship       |
| 8     | ObjectSourceTargetMap         | .objectSourceTargetMap         | objectSourceTargetMaps         |
| 9     | PlatformEventSubscriberConfig | .platformEventSubscriberConfig | PlatformEventSubscriberConfigs |
| 10    | ServiceAISetupDefinition      | .serviceAISetupDescription     | serviceAISetupDescriptions     |
| 11    | ServiceAISetupField           | .serviceAiSetupField           | serviceAiSetupFields           |

**API 49.0 newly Supported Metadata Types**

Below is the list of **API 49.0** metadata types supported for both **Salesforce DX** and **non-DX platforms**:

<figure><img src="../../../../.gitbook/assets/image (638).png" alt=""><figcaption></figcaption></figure>

For versions **48.0 and earlier**, please refer [here](https://developer.salesforce.com/docs/atlas.en-us.object\_reference.meta/object\_reference/sforce\_api\_objects\_list.htm) to find the list of Salesforce objects and their supported API versions.
