# Pipeline

### Pipeline: Overview <a href="#pipeline-overview" id="pipeline-overview"></a>

A pipeline is a unidirectional flow that defines how changes progress from development orgs to the Pipelines is a top-level module in ARM that helps teams automate and manage the movement of Salesforce changes across environments. Within Pipelines, **Releases** is a dedicated sub-module used to configure and execute **Release Pipelines**.\
\
A Release Pipeline defines how a built artifact is promoted from one environment to another through one or more stages. Each stage represents a deployment or validation step, typically mapped to a Salesforce org such as Development, QA, UAT, or Production.

Release Pipelines allow teams to take a single artifact generated from a build pipeline and consistently move it across multiple stages in a controlled and repeatable manner.

***

### Navigating to the Pipeline Page <a href="#navigating-to-pipeline-dashboard-page" id="navigating-to-pipeline-dashboard-page"></a>

When you navigate to Pipelines → Releases, the landing page displays **Most recent runs** by default. This view shows the latest execution for each release pipeline, allowing users to quickly understand the current state of deployments.\
<br>

<figure><img src="../../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

From this page, users can:\
\
• Monitor active and completed release executions\
• Identify failed or in-progress stages\
• Access detailed execution information using View details\
• Create new release pipelines or manage existing ones\
<br>
