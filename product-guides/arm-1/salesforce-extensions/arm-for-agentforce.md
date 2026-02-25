# ARM for Agentforce

**Overview**\
AutoRABIT ARM supports deployment and version control of Salesforce Agentforce components by treating them as standard metadata. This allows teams to manage Agentforce configurations using the same CI, version control, and deployment workflows used for Salesforce development. Agentforce assets can be moved consistently across environments with governance, traceability, and automation.

**How ARM supports Agentforce**\
Agentforce components can be committed into version control, validated through CI jobs, and deployed across environments such as Development, QA, UAT, and Production using ARM pipelines. By managing Agentforce components as metadata, teams can ensure consistency between environments and maintain complete visibility into changes.

Customers can include Agentforce components in their regular DevOps lifecycle without requiring separate deployment tools or manual steps. This ensures a unified deployment approach for both traditional Salesforce metadata and Agentforce AI components.

Supported Agentforce metadata in ARM

| Agentforce Metadata Type                   | Supported |
| ------------------------------------------ | --------- |
| GenAiPromptTemplate                        | Yes       |
| GenAiPromptTemplateActv                    | Yes       |
| GenAiPlugin                                | Yes       |
| GenAiFunction                              | Yes       |
| GenAiPlanner (API 60 to 63)                | Yes       |
| GenAiPlannerBundle (API 64 and Above)      | Yes       |
| Bot                                        | Yes       |
| BotVersion                                 | Yes       |
| Custom Apex invoked by agents (ApexClass)  | Yes       |
| Flows used by agents (Flow)                | Yes       |
| Permission Sets assigned to the Agent User | Yes       |
| CustomSite                                 | Yes       |
| Network                                    | Yes       |
| DigitalExperienceBundle                    | Yes       |
| EmbeddedServiceConfig                      | Yes       |
| MessagingChannel                           | Yes       |
| Flow (Omnichannel routing flow)            | Yes       |
| Queue                                      | Yes       |
| QueueRoutingConfig                         | Yes       |
