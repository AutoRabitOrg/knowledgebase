# Vlocity

Vlocity, as of June 1, 2020, is now a Salesforce company. Vlocity is a set of applications built solely on the Salesforce platform and caters to a number of industries including healthcare, energy, government, entertainment, and insurance. Vlocity is popular among many of our healthcare clients.

For best tracking and visibility, it’s recommended to set a metadata folder path for a repository. This can be completed through the use of the branch settings column in the Repository details. This will enable the metadata to be placed in the specified directory rather than the root directory. This should be completed before any baseline and commits as part of your VC Repo’s registration.

Branching baseline can also be used for periodical [metadata backups](https://www.autorabit.com/blog/how-to-back-up-your-metadata-in-salesforce/) into a separate backup repository, which can be used to track unplanned manual changes in the orgs.

Branching Baseline is one of the first steps in seeding the master branch. ARM has the ability to populate the Vlocity specific metadata into the master branch using Branching Baseline methodology. These are key metadata items that are extracted as part of the Baseline process for [Vlocity](../../../arm/integration-and-plugins/vlocity/). Branching Baseline has the ability to seed master branches for Salesforce-specific Metadata and Vlocity-specific metadata.

* Attachment
* AttributeAssignmentRule
* AttributeCategory
* CalculationMatrix
* CalculationMatrixVersion
* CalculationProcedure
* CalculationProcedureVersion
* Catalog
* ContextAction
* ContextDimension
* ContextScope
* ContractType
* DataRaptor
* Document
* DocumentClause
* DocumentTemplate
* EntityFilter
* FlexCard
* IntegrationProcedure
* InterfaceImplementation
* ItemImplementation
* ManualQueue
* ObjectClass
* ObjectContextRule
* ObjectLayout
* OmniScript
* OrchestrationDependencyDefinition
* OrchestrationItemDefinition
* OrchestrationPlanDefinition
* Pricebook2
* PriceList
* PricingPlan
* PricingVariable
* Product2
* Promotion
* QueryBuilder
* Rule
* StoryObjectConfiguration
* System
* TimePlan
* TimePolicy
* UIFacet
* UISection
* VlocityAction
* VlocityAttachment
* VlocityCard
* VlocityFunction
* VlocityPicklist
* VlocitySearchWidgetSetup
* VlocityStateModel
* VlocityUILayout
* VlocityUITemplate
* VqMachine
* VqResource

Seeding a master repository within ARM is possible for both Salesforce and Vlocity metadata as displayed below:

<figure><img src="../../../../.gitbook/assets/image (30) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="507"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)  (15).png" alt="" width="511"><figcaption></figcaption></figure>

Upon successfully executing the Branching Baseline by selecting Salesforce and Vlocity for the retrieval type all metadata is placed into the master repository.  The Salesforce metadata should be placed in the src directory within the master repository.  Additionally, a **vlocity.yaml** file is created as part of the baseline process.  Here is an example of a **vlocity.yaml** file:

**Project path:** _./autorabit\_alldefault\_vlocity\_buildmanifest_

* Attachment
* AttributeAssignmentRule
* AttributeCategory
* CalculationMatrix
* CalculationMatrixVersion
* CalculationProcedure
* CalculationProcedureVersion
* Catalog
* ContextAction
* ContextDimension
* ContextScope
* ContractType
* DataRaptor
* Document
* DocumentClause
* DocumentTemplate
* EntityFilter
* FlexCard
* IntegrationProcedure
* InterfaceImplementation
* ItemImplementation
* ManualQueue
* ObjectClass
* ObjectContextRule
* ObjectLayout
* OmniScript
* OrchestrationDependencyDefinition
* OrchestrationItemDefinition
* OrchestrationPlanDefinition
* Pricebook2
* PriceList
* PricingPlan
* PricingVariable
* Product2
* Promotion
* QueryBuilder
* Rule
* StoryObjectConfiguration
* System
* TimePlan
* TimePolicy
* UIFacet
* UISection
* VlocityAction
* VlocityAttachment
* VlocityCard
* VlocityFunction
* VlocityPicklist
* VlocitySearchWidgetSetup
* VlocityStateModel
* VlocityUILayout
* VlocityUITemplate
* VqMachine
* VqResource\
  maxDepth: -1\
  autoUpdateSettings: true\
  separateMatrixVersions: true

In addition to the **vlocity.yaml** file, the Vlocity metadata is retrieved and placed into the _autorabit\_alldefault\_vlocity\_build_ folder.
