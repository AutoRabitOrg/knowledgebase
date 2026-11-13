# Feature Controls

### Overview

Feature Controls let tenant managers turn selected Guard features on or off for their tenant, straight from the Guard UI. You no longer need to raise a support request to change these settings.

### Navigation path

`Guard → Settings → Feature Controls`

Only tenant managers can see Feature Controls. Other users do not see it in Settings and cannot open the page by direct link.

### Features you can control

| Feature                       | What it does                                                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated Data Classification | Classifies custom fields against major regulations. See [Data Classification](../features/governance/data-classification.md).                            |
| Ask AutoRABIT                 | The in-app AI assistant.                                                                                                                                 |
| Guard CLI and MCP access      | Lets users connect Guard to AI assistants and the command line. See [Guard MCP & Skill: User Guide](../ai-interfaces/guard-mcp-and-skill-user-guide.md). |
| Risk Auto Resolve             | Allows auto-resolution of identified org risks, where available.                                                                                         |
| AI notification summaries     | Adds a short AI summary to each notification. See [Notification Center](../features/notification-center.md).                                             |

If AI is not enabled for your tenant, the AI features (Automated Data Classification, Ask AutoRABIT and AI notification summaries) are hidden. Speak to AutoRABIT if you want AI turned on.

### How to turn a feature on or off

1. Open Settings, then Feature Controls.
2. Find the feature.
3. Switch the toggle.
4. Confirm the change. If you cancel, the setting stays as it was.

Every change is recorded in the audit log, with the setting, the old and new values, who made the change and when.

### Upgrading

When your tenant is upgraded, each feature keeps the setting it had before, so nothing changes until you choose to change it.
