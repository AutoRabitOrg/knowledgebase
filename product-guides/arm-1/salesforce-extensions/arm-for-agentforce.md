# ARM for Agentforce

**Overview**\
AutoRABIT ARM supports deployment and version control of Salesforce Agentforce components by treating them as standard metadata. This allows teams to manage Agentforce configurations using the same CI, version control, and deployment workflows used for Salesforce development. Agentforce assets can be moved consistently across environments with governance, traceability, and automation.

**How ARM supports Agentforce**\
Agentforce components can be committed into version control, validated through CI jobs, and deployed across environments such as Development, QA, UAT, and Production using ARM pipelines. By managing Agentforce components as metadata, teams can ensure consistency between environments and maintain complete visibility into changes.

Customers can include Agentforce components in their regular DevOps lifecycle without requiring separate deployment tools or manual steps. This ensures a unified deployment approach for both traditional Salesforce metadata and Agentforce AI components.

Supported Agentforce metadata in ARM

<table><thead><tr><th width="611.203125">Metadata Type</th></tr></thead><tbody><tr><td>AiAgentDefinition</td></tr><tr><td>AiAgentDefinitionVersion</td></tr><tr><td>AgenticCtxtDecorDefinition</td></tr><tr><td>AgentPlatformSettings</td></tr><tr><td>AgentforceAccountManagementSettings</td></tr><tr><td>AgentforceForDevelopersSettings</td></tr><tr><td>AgentforcePlatformTracingSettings</td></tr><tr><td>AiSurface</td></tr><tr><td>AiResponseFormat</td></tr><tr><td>AiTestingDefinition</td></tr><tr><td>GenAiPlugin</td></tr><tr><td>GenAiFunction</td></tr><tr><td>GenAiPlanner</td></tr><tr><td>GenAiPlannerBundle</td></tr><tr><td>GenAiPromptTemplate</td></tr><tr><td>GenAiPromptTemplateActv</td></tr></tbody></table>
