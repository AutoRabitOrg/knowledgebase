# Salesforce API version

ARM's ability to support Salesforce Standard and Custom Objects is determined by the Salesforce API version used. ARM now supports the **Salesforce API 59.0 version**, which means it can support any Salesforce standard or custom object that requires Salesforce API version **59.0** or earlier.

{% hint style="info" %}
Important: Only users on an ARM shared instance will see the changes since the Salesforce API version is being updated to **59.0** as part of weekly hotfixes to shared instances only.
{% endhint %}

**Troubleshooting:**

Ensure your Salesforce API version in ARM matches the API version of the Salesforce org. Failure to match the version may result in metadata object commit/deployment failure in your target environment. Use Case:

* **API version set in ARM: 59.0**
* **Salesforce Org API version: 59.0**

To identify which Salesforce API version you are on, please refer to the article: [Find Salesforce Edition and API version](https://help.salesforce.com/s/articleView?id=000334996\&type=1).

#### Salesforce API Supported Metadata Types

The following tables highlight the newly supported metadata types for each API version.

Metadata types added as part of the **API 59** upgrade:

| MetadataType                         | Extension     | FolderName                 |
| ------------------------------------ | ------------- | -------------------------- |
| ExternalClientApplication            | .eca          | externalClientApps         |
| ExtlClntAppGlobalOauthSettings       | .ecaGlblOauth | extlClntAppGlobalOauthSets |
| ExtlClntAppOauthConfigurablePolicies | .ecaOauthPlcy | extlClntAppOauthPolicies   |
| ExtlClntAppOauthSettings             | .ecaOauth     | extlClntAppOauthSettings   |
| FlowTransform                        | NA            | NA                         |

Below is the List of Metadata types support added as part of **API 58** Release -

| MetadataType                   | Extension                   | FolderName                      |
| ------------------------------ | --------------------------- | ------------------------------- |
| `AccountingFieldMapping`       | `.accountingFieldMapping`   | `accountingFieldMappings`       |
| `AIScoringModelDefinition`     | `.aiScoringModelDefinition` | `aiScoringModelDefinitions`     |
| `DataWeaveResource`            | `.dwl`                      | `dw`                            |
| `PlatformEventSettings`        | `.settings`                 | `settings`                      |
| `ExperiencePropertyTypeBundle` | NR                          | `experiencePropertyTypeBundles` |
| ProcessFlowMigration           | NA                          | NA                              |

{% hint style="warning" %}
*
{% endhint %}

**Troubleshooting**:

Ensure your Salesforce API version in ARM matches the API version of the Salesforce org. Failure to match the version may result in metadata object commit/deployment failure in your target environment.\
\
**Use Case:**

* API version set in ARM: **56.0**
* Salesforce Org API version: **57.0**

When you use ARM to perform an EZ-Commit and choose the **Flow** and **Flow Definition** components from a Salesforce org, the properties **'triggerOrder'** and **'Overridable'** do not reflect in your target branch.

It fails when you try to deploy using the above revision after changing the API version to 57.0 in ARM.\
\
You'll need to retrigger the commit and deployment process to make the deployment successful.\


The below tables highlight the supported metadata types for each API version.&#x20;

**API 57.0 newly Supported Metadata Types**

| OmniSupervisorConfig      | PipelineInspMetricConfig | DataImportManagementSettings |
| ------------------------- | ------------------------ | ---------------------------- |
| HighVelocitySalesSettings | Territory2AccessLevel    | AdvAccountForecastSet        |

Important Note:**OmniSupervisorConfig** metadata type is not supported in **Unlocked Package** creation, but is working as expected in **Commits** and **Deployments**.

**API 56.0 newly Supported Metadata Types**

| **S. No.** | **Metadata Type**       | **Folder Name**          | **File Extension**       |
| ---------- | ----------------------- | ------------------------ | ------------------------ |
| 1          | AIUsecaseDefinition     | aiUsecaseDefinitions     | .aiUsecaseDefinitions    |
| 2          | DigitalExperienceBundle | digitalExperiences       | .digitalExperience       |
| 3          | DigitalExperienceConfig | digitalExperienceConfigs | .digitalExperienceConfig |
| 4          | EventRelayConfig        | eventRelays              | .eventRelay              |
| 5          | OauthOidcSettings       | settings                 | .settings                |

TroubleshootingEnsure that your Salesforce API version in ARM matches the API version of the Salesforce org. Failure to match the version may result in errors while accessing the Salesforce org in Version Control, CI Jobs, Deployment, or SFDX modules.Important Note:

The following fields have been deprecated on the **NamedCredential** metadata type in API version 56.0. These fields are valid only when **namedCredentialType** is **null** or set to **Legacy**.

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

| S. No. | Metadata Type       | Folder Name           | File Extension       |
| ------ | ------------------- | --------------------- | -------------------- |
| 1      | LoyaltyProgramSetup | loyaltyProgramSetups  | .loyaltyProgramSetup |
| 2      | RecordAlertCategory | recordAlertCategories | .recordAlertCategory |

**API 53.0 Supported Metadata Types**

Please refer [here](https://help.salesforce.com/s/articleView?id=release-notes.rn\_api\_objects.htm\&type=5\&release=234) to find the list of supported Salesforce objects supported on Salesforce API 53.0 version.

**API 52.0 newly Supported Metadata Types**

| S. No. | Metadata Type                 | File Extension                 | Folder Name                  |
| ------ | ----------------------------- | ------------------------------ | ---------------------------- |
| 1      | EinsteinAgentSettings         | EinsteinAgent.settings         | settings                     |
| 2      | FieldRestrictionRule          | .rule                          | fieldRestrictionRules        |
| 3      | ForecastingObjectListSettings | ForecastingObjectList.settings | settings                     |
| 4      | ForecastingSourceDefinition   | .forecastingSourceDefinition   | forecastingSourceDefinitions |
| 5      | ForecastingType               | .forecastingType               | forecastingTypes             |
| 6      | ForecastingTypeSource         | .forecastingTypeSource         | ForecastingTypeSources       |
| 7      | FunctionReference(Beta)       | .functions                     | functions                    |
| 8      | MktCalcInsightObjectDef       | .mktCalcInsightObjectDef       | mktCalcInsightObjectDefs     |
| 9      | OcrSampleDocument             | .ocrSampleDocument             | ocrSampleDocuments           |
| 10     | OcrTemplate                   | .ocrTemplate                   | ocrTemplates                 |
| 11     | RestrictionRule               | .rule                          | restrictionRules             |
| 12     | ServiceCloudVoiceSettings     | ServiceCloudVoice.settings     | settings                     |
| 13     | WorkforceEngagementSettings   | WorkforceEngagement.settings   | settings                     |

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

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-317\(1\).png)

For versions **48.0 and earlier**, please refer [here](https://developer.salesforce.com/docs/atlas.en-us.object\_reference.meta/object\_reference/sforce\_api\_objects\_list.htm) to find the list of Salesforce objects and their supported API versions.
