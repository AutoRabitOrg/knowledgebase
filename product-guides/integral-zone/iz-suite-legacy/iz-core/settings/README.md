# Settings

Global settings are maintained under **`Global Settings`** -> **`Settings`**. Search for the setting by name and click **`Edit`** to change its values. Settings marked as secure are masked after saving.

{% hint style="info" %}
In a multi-tenant installation every tenant has its own copy of the settings. A small number of settings are managed by the platform operator and are either hidden from tenants or shown read-only; see [Multi-Tenancy Overview](../multi-tenancy/multi-tenancy-overview.md)
{% endhint %}

#### Settings Reference <a href="#settings-reference" id="settings-reference"></a>

| Setting                                                                                                        | Purpose                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **`IZ Token Auth`**, **`Anypoint Auth`**, **`Google Auth`**, **`Azure Auth`**                                  | Sign-in options and their client credentials.                                                                                  |
| **`Login Settings`**                                                                                           | Automatic user creation on first single sign-on and session timeout.                                                           |
| **`Agent Settings`**                                                                                           | Agent defaults, including **`Default Workers Count`** (12) for new agents and the stale worker check interval.                 |
| **`Anypoint Sync Settings`**                                                                                   | Anypoint Connected App **`Client Id`** and **`Client Secret`** used by the AI agent to resolve Anypoint Exchange dependencies. |
| **`Anypoint Team Sync`**, **`Anypoint Teams Role Mapping`**                                                    | Synchronise Anypoint Teams users and map their permissions.                                                                    |
| **`Azure Integration Services Sync`**                                                                          | Microsoft Entra ID app registration used to discover Azure resources.                                                          |
| **`IZ Scan Settings`**                                                                                         | Include and exclude patterns for CI/CD scans.                                                                                  |
| **`Language Identifier Settings`**                                                                             | How project types are detected.                                                                                                |
| **`BitBucket Repo Sync Settings`**, **`GitHub Repo Sync Settings`**, **`Design Center Project Sync Settings`** | External repository sources.                                                                                                   |
| **`Reporting Config`**                                                                                         | Report storage and templates.                                                                                                  |
| **`AI Agent Settings`**                                                                                        | AI provider, model, vector database and Maven settings for IZ AI.                                                              |
| **`Archival Policies`**                                                                                        | Retention rules for scans, job executions, audit logs, notifications and server work items.                                    |
| **`Dashboard Filters`**                                                                                        | Custom dashboard filters.                                                                                                      |
| **`Email Settings`**                                                                                           | Mail server used for notifications. Platform-managed in multi-tenant installations.                                            |
| **`MCP Server Settings`**                                                                                      | Port of the MCP server. Platform tenant only.                                                                                  |
| **`Worker Node Configuration`**                                                                                | Concurrency and timeouts of background workers. Platform tenant only.                                                          |
