# Multi-Tenancy Overview

* Multi-tenancy is available from IZ Suite version **26.3.1**.
* Multi-tenancy is a licensed capability. When the **`Multi Tenant`** license module is not part of your subscription, IZ Suite behaves exactly as a single-tenant installation and none of the tenant screens described in this section are shown

### What is a Tenant?

A **tenant** is a fully isolated workspace inside one IZ Suite installation. Each tenant has its own:



* Organizations, environments and applications
* Users, roles, permissions and security tokens
* Quality rules, quality and metric profiles, quality gates
* Schedules, job executions and agents
* Global settings (with a small set of platform-managed exceptions, see below)
* License, license modules and license usage
* Notifications, subscriptions and audit logs
* Dashboards, automation tasks and MCP tools



Data never crosses tenant boundaries. A user signed in to one tenant cannot see or search another tenant's data, and reports, dashboards and MCP tools only return data for the tenant that the user belongs to.



### Platform Tenant and Customer Tenants



Every multi-tenant installation has exactly one **platform tenant**. This is the tenant that exists after a fresh installation and that holds the platform operator's license. Platform administrators use it to:



* Onboard, edit, suspend and delete customer tenants
* Enable optional modules for a tenant
* Decide which settings a tenant may manage on its own
* Push a setting value to many tenants at once
* Monitor all tenants from the **Tenant Ops** console



When multi-tenancy is enabled, the platform tenant's home page and menu show only **`Manage Tenants`** and **`Global Settings`**. Product areas such as IZ Eye, IZ Scan, IZ Pulse and Quality Control are hidden on the platform tenant and are used from within customer tenants.

**Customer tenants** are created by the platform administrator using Onboard Tenant. Each customer tenant gets its own administrator, its own login URL and its own license key.<br>

### What a New Tenant Starts With

When a tenant is onboarded it receives a copy of the platform baseline:



| Copied to the new tenant                                                        | Not copied (platform-managed)                                                      |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Built-in permissions and roles                                                  | **`Manage Tenants`** permission                                                    |
| Built-in quality rules, metric rules, quality/metric profiles and quality gates | **`Job Types`** and **`Seed Data`** administration                                 |
| Job types and default schedules                                                 | **`Worker Node Configuration`** setting                                            |
| Global settings, with single sign-on providers cleared and disabled             | **`MCP Server Settings`** setting                                                  |
| Notification events and channel events                                          | **`Email Settings`** (mail is always sent using the platform's mail configuration) |
| Automation tasks and MCP tools                                                  | **`Multi Tenant`** license module                                                  |
| An organization named after the tenant with a **`Production`** environment      | Server audit logs and scheduler audit logs                                         |

Built-in rules, profiles and dashboards that are added in later IZ Suite releases are automatically added to every tenant when the server is upgraded.

### Tenant Status

| Status          | Effect                                             |
| --------------- | -------------------------------------------------- |
| **`ACTIVE`**    | Normal operation.                                  |
| **`TRIAL`**     | Same as Active. Use it to mark evaluation tenants. |
| **`SUSPENDED`** | No operations allowed. All data is retained.       |

\
The platform tenant is always Active and cannot be deleted. To stop users of a tenant from working, disable the tenant's sign-in options in the tenant's **`Global Settings`** → **`Settings`** (for example set **`Is Enabled`** to `false` on the tenant's auth settings) or deactivate the users.



### How Users Reach the Tenant <a href="#how-users-reach-their-tenant" id="how-users-reach-their-tenant"></a>

Each tenant is reached through its own URL, either a subdomain of the IZ Suite host (for example `acme.izsuite.example.com`) or a dedicated hostname configured as the tenant's **`External Link`**. The tenant is identified from the hostname of the request, so single sign-on, security tokens and MCP clients must all use the tenant's own URL



### Licensing <a href="#licensing" id="licensing"></a>

* Each tenant has its own license key. A license key can be applied to only one tenant.
* Quotas (for example the number of applications or developer keys) are counted per tenant and shown in that tenant's **`Global Settings`** → **`License`** screen.
* Optional modules such as **`Compliance`** are enabled per tenant by the platform administrator through **`Enable Modules`**.



### Agents and Schedules <a href="#agents-and-schedules" id="agents-and-schedules"></a>

Agents and workers are shared infrastructure. A schedule created in any tenant is executed by the pool of agent workers, and work is allocated fairly so that one tenant with a large backlog cannot starve the others. Each job execution runs in the context of the tenant that owns the schedule; agents never mix data between tenants. Self-hosted agents can also be started for a single tenant by using that tenant's agent credentials.



### Settings Managed by the Platform <a href="#settings-managed-by-the-platform" id="settings-managed-by-the-platform"></a>

Some settings are sensitive or affect the whole installation. For these, the platform administrator decides per tenant which entries a tenant administrator can see and edit. By default:



| Setting                 | Tenant administrators can edit                                                                              |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| **`AI Agent Settings`** | `AI_AGENT_API_KEY`, `VECTOR_DB_TOKEN`, `AI_PROVIDER`, `AI_MODEL`, `VECTOR_DB_URL`, `VECTOR_DB_SEARCH_TOKEN` |
| **`Reporting Config`**  | `PROVIDER`, `REGION`, `CLIENT_ID`, `CLIENT_SECRET`, `BUCKET_NAME`, `SECURE_VALUE_1`                         |
| **`Email Settings`**    | Nothing. Mail is sent using the platform configuration.                                                     |

Entries that are not tenant-managed are hidden from the tenant's settings screens, and secure values are always masked.

