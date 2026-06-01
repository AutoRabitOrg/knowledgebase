---
hidden: true
---

# Upgrading the Node Runtime for Azure DevOps

{% hint style="info" %}
**This change applies to all CodeScan customers running scans through the Azure DevOps extension.** If you use Microsoft-hosted (default) agents, no action is required. If you run your pipelines on custom (self-hosted) agents, please review the _Custom (Self-Hosted) Agents_ section below.
{% endhint %}

#### **Overview**

As part of our ongoing commitment to platform security and maintenance, CodeScan is upgrading the Node runtime used by our Azure DevOps extension to **Node 24** on **August 1, 2026**. To support a smooth transition, **Node 20 will remain available as a fallback** alongside Node 24, ensuring uninterrupted operation while customers validate compatibility with the new runtime.

Your scan functionality remains the same — this is a runtime update only.

#### Key Date

1. **August 1, 2026** — CodeScan's Azure DevOps extension upgrades to Node 24. Node 20 remains available as a fallback.

#### Actions Required

**If you use Microsoft-hosted (default) agents**, no action is required. Microsoft-hosted agents are already compatible with both Node 20 and Node 24, and your pipelines will continue to run without changes.

**If you use custom (self-hosted) agents**, please ensure your agents are compatible with at least Node 20 ahead of the upgrade date. Agents that meet this requirement will continue to operate without interruption when the upgrade takes effect.

#### Custom (Self-Hosted) Agents

To confirm your self-hosted agents are ready for the upgrade:

1. Verify that each agent machine has a supported Node runtime installed (Node 20 or later).
2. Confirm operating system and architecture compatibility with your installed Node version.
3. Where possible, we recommend upgrading agents to Node 24 to align with the new default runtime and benefit from the latest security and performance updates.

#### Need Help?

1. Contact AutoRABIT Support ([support@autorabit.com](mailto:support@autorabit.com)).
2. Refer to Microsoft's [Azure Pipelines agents documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents) for guidance on managing self-hosted agents.

#### Additional Resources

For more information on Node.js release schedules and supported versions, refer to the [Node.js release documentation](https://nodejs.org/en/about/previous-releases).
