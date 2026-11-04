# AI Interfaces for AutoRABIT Guard: Technical Specification

### Overview

Release 26.1.6 has introduced the first AI interfaces for Guard, giving AI agents consistent, standards-aligned access to Guard capabilities through a Machine Control Protocol (MCP) server.

With this release, AI platforms and automation tools can discover and invoke Guard operations programmatically. The MCP server exposes Guard features as structured tools with defined input and output contracts, designed for LLM-centric workflows and orchestration.

### Goals

* Provide an MCP-compliant server interface so AI agents can discover and invoke Guard capabilities programmatically.
* Expose Guard functions as tools with metadata suited to LLM-centric workflows and orchestration.
* Deliver a Guard skill for integrating Guard-powered capabilities into AI platforms.
* Lay the foundation for a Guard CLI with AI-specific commands, planned for a future release.

### Scope

#### MCP Server

The MCP server provides a standards-aligned interface for AI agents to list, inspect, and invoke Guard tools.

* MCP-compliant server that exposes Guard features as invocable tools, registered via Spring AI's tool callback provider.
* Tool discovery is handled natively by the MCP protocol — clients can list and inspect all available tools without a separate search endpoint.
* Structured tool descriptors with descriptions and typed input parameters, optimised for LLM consumption.

#### Allowed Origins Management

Administrators can control which MCP clients are permitted to connect to the Guard MCP server.

* GraphQL API for creating, listing, and managing custom allowed origins.
* Frontend UI in the management console for origin configuration.
* Supports both predefined and custom origin types.

#### Guard Skill

The Guard skill bundles tool wiring and contextual guidance for use in AI platforms.

* Skill definition format for Guard-powered AI flows.
* Local execution support for testing skills before connecting to external AI agents.

### Architecture and Technical Design

#### High-Level Components

* **MCP Server Core**: handles protocol negotiation, request routing, and tool dispatch. Implemented as a Spring Boot service with Spring AI's MCP server support.
* **Tool Registry**: tools are registered declaratively using Spring AI's @Tool annotations and exposed to the MCP protocol via a ToolCallbackProvider. There is no separate runtime search or ranking layer; the MCP protocol itself handles tool listing and inspection.
* **Guard Adapter Layer**: each tool class bridges MCP invocations to the underlying Guard services. Tool groups are separated by access level and functional area.
* **Skill Runtime**: loads the Guard skill definition, resolves tools, and executes flows, returning structured results to callers.
* **OAuth Metadata Endpoints**: public endpoints that expose RFC 8414 and RFC 7591 metadata for MCP client auto-discovery of the OAuth 2.0 authorization server.

#### MCP Server Design

The server is implemented as a stateless Spring Boot service that delegates execution to Guard service beans.

* **Transport layer**: HTTP endpoint at /api/mcp. Handles request/response framing and translates errors into MCP-compliant responses.
* **Protocol layer**: Spring AI enforces the MCP protocol contract, validates tool calls, and normalises inputs and outputs.
* **Execution layer**: each tool invocation is dispatched to the relevant Guard service. Read operations return results directly. Operations that trigger background jobs (classification analysis, data scans, changelog import, policy deviation analysis) return immediately with a confirmation; the underlying job runs asynchronously.

### API and Endpoints

#### MCP Endpoint

The MCP server is exposed at /api/mcp. All tool discovery and invocation goes through this single endpoint using the MCP protocol.

* **Tool listing**: MCP clients can list all available tools and their input schemas natively through the protocol.
* **Tool invocation**: clients invoke tools by name, passing typed inputs as defined in the tool descriptor.

#### OAuth Metadata Endpoints

The following public endpoints support MCP client auto-discovery of the authorization server. They require no authentication.

* /.well-known/oauth-protected-resource: RFC 8707 protected resource metadata, including the resource URL and supported scopes. Returned in the WWW-Authenticate header on 401 responses so clients can locate the authorization server automatically.
* /.well-known/openid-configuration: OIDC discovery metadata.
* /oauth/register: RFC 7591 dynamic client registration.

#### Allowed Origins API

A GraphQL API manages which origins are permitted to connect to the MCP server.

* Query allowed origins and their types.
* Create or update custom origin entries.

### Authentication and Security

The MCP server uses OAuth 2.0 Bearer token authentication backed by Keycloak as the OpenID Connect provider.

* **Bearer token requirement**: all requests to /api/mcp must include a valid Bearer token in the Authorization header. Unauthenticated requests receive a 401 response with a WWW-Authenticate header pointing to the protected resource metadata URL, allowing MCP clients to auto-discover the authorization server and initiate the OAuth flow without manual configuration.
* **Supported grant types**: authorization\_code (with PKCE), refresh\_token, and client\_credentials. Scopes include openid, profile, and email by default, configurable per deployment.
* **Role-based access**: tool access is enforced by Guard's method-level security. Callers can only discover and invoke tools they are authorised to use based on their identity and tenant context.
* **Allowed origins**: administrators configure which MCP client origins are permitted to connect via the management console or GraphQL API. Requests from unconfigured origins are rejected.
* **Audit logging**: all tool invocations are logged with caller identity, tool name, parameters (redacted where sensitive), and outcome for audit and troubleshooting.
* **Input validation**: all tool inputs are validated against typed schemas before dispatch to Guard services.

#### Public Endpoints

The following paths are permitted without authentication to support OAuth discovery and platform integrations:

/.well-known/\*\*, /oauth/register, /oauth/\_callback, /actuator/\*\*

### Configuration

Configuration is layered across environment variables, configuration files, and command-line flags with a defined precedence order.

* **MCP server options**: base URL, endpoint path (/api/mcp by default), and OAuth issuer and client ID are configured under the app.mcp property namespace.
* **OAuth / Keycloak**: issuer URL, client ID, and scopes are required for the protected resource metadata to be generated correctly.
* **Allowed origins**: managed at runtime via the management console or GraphQL API rather than static configuration.
* **Tool availability**: all registered tool groups are active by default. Individual tools can be excluded by removing or conditionally registering the relevant Spring component.

### Tool Reference

Tools are organised into five groups by access level and functional area. All groups are registered together via a single ToolCallbackProvider bean.

#### Read Tools (guard-read)

Core read-only access to org data, risk, permissions, and connected apps.

| Tool                   | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| list\_orgs             | List all registered Salesforce orgs                          |
| get\_org               | Get a Salesforce org by UUID                                 |
| get\_risk\_assessment  | Get risk assessment results for an org                       |
| get\_risk\_scores      | Get risk scores for one or more orgs                         |
| list\_connected\_apps  | List all connected apps across all orgs                      |
| get\_connected\_app    | Get details for a connected app by name                      |
| get\_permissions       | Get user permissions for specific permission names in an org |
| list\_permission\_sets | List permission sets for one or more orgs                    |

#### Policy Tools (guard-policy)

Reads for baseline policies, policy intents, and classification data.

| Tool                              | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ |
| list\_baseline\_policies          | List all baseline authorization policies                     |
| get\_baseline\_policy             | Get a baseline policy by ID including its deviations summary |
| list\_policy\_intents             | List all policy-as-intent rules                              |
| get\_policy\_intent               | Get a policy intent by ID with deviations                    |
| list\_classification\_regulations | List all data classification regulations                     |
| get\_classification\_analysis     | Get classification analysis results for an org               |
| list\_classification\_analyses    | List classification analysis overview for all orgs           |

#### Ops Tools (guard-ops)

Execution workflows that trigger background jobs or long-running operations.

| Tool                             | Description                                              |
| -------------------------------- | -------------------------------------------------------- |
| run\_classification\_analysis    | Start a classification analysis job for an org           |
| run\_data\_scan                  | Run an AI data scan on a specific Salesforce field       |
| run\_policy\_deviation\_analysis | Run deviation analysis for a policy intent               |
| import\_changelog                | Import changelog data for all orgs in the current tenant |

#### Admin Tools (guard-admin)

Privileged mutations — delete and update operations that modify state. Requires stronger approval; not mixed with read tools.

| Tool                            | Description                                  |
| ------------------------------- | -------------------------------------------- |
| delete\_baseline\_policy        | Delete a baseline authorization policy by ID |
| delete\_policy\_intent          | Delete a policy-as-intent rule by ID         |
| delete\_permissions\_query      | Delete a saved permissions query by ID       |
| delete\_changelog\_notification | Delete a changelog notification rule by ID   |
| update\_data\_scan\_settings    | Update classification data scan settings     |

#### Reporting Tools (guard-reporting)

Reporting and inspection data — changelog stats, user security, permission history, saved queries, notifications, and scan settings.

| Tool                           | Description                                          |
| ------------------------------ | ---------------------------------------------------- |
| list\_changelog\_stats         | List changelog statistics for all orgs               |
| get\_changelog\_stat           | Get changelog statistics for a specific org          |
| list\_changelog\_notifications | List all changelog notification rules                |
| get\_changelog\_notification   | Get a changelog notification rule by ID              |
| get\_user\_login\_history      | Get login history for a Salesforce user              |
| get\_user\_oauth\_tokens       | Get OAuth tokens for a Salesforce user               |
| get\_user\_permission\_sets    | Get permission set assignments for a Salesforce user |
| get\_permission\_history       | Get permission change history for an org             |
| list\_permissions\_queries     | List all saved permissions queries                   |
| get\_permissions\_query        | Get a saved permissions query by ID                  |
| get\_data\_scan\_settings      | Get current data scan settings                       |
| get\_risk\_assessment\_goals   | Get risk assessment goals and thresholds             |

### Known Issues and Limitations

* **Partial feature coverage**: not all Guard capabilities are surfaced as MCP tools in this initial release. Additional tools will be added in subsequent iterations based on demand and security reviews.
* **Ops tools are fire-and-forget**: tools that trigger background jobs return immediately with a confirmation. There is no built-in polling mechanism in this release; callers should use Guard's existing reporting tools to check job outcomes.
