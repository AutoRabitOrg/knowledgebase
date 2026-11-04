# MCP Server Installation

## Enabling IZ MCP Server

{% hint style="warning" %}
* MCP server feature requires IZ Suite version 1.4.0 or above
* From IZ Suite version 26.3.1 the MCP server starts automatically with the IZ Server. The steps below describe how to verify and restart it.
{% endhint %}

#### MCP Server Endpoint <a href="#mcp-server-endpoint" id="mcp-server-endpoint"></a>

1. The HTTP MCP server is available at http(s)://\<YOUR\_HOST\_NAME>/mcp as soon as the IZ Server is running.
2. In a multi-tenant installation, use the tenant's hostname. The tenant is identified from the service URL sent by the MCP client; see [HTTP MCP Server Configuration](http-mcp-server-configuration.md).
3. To check the list of available tools check available tools section



#### Restarting MCP Server <a href="#restarting-mcp-server" id="restarting-mcp-server"></a>

1. Navigate to **`Global Settings`** -> **`MCP Server Setup`**
2. Click on **`Restart MCP Server`**. The action is available to administrators of the platform tenant (or of the instance, in a single-tenant installation).
3. The MCP server also restarts automatically when the **`MCP Server Settings`** global setting is saved.



#### Upgrading from 1.4.x <a href="#upgrading-from-14x" id="upgrading-from-14x"></a>

The **`MCPServerMonitorSchedule`** entry under **`Audit`** -> **`Scheduler Audit Logs`** and its **`Enable Schedule`** / **`Disable Schedule`** actions no longer exist. No action is required after upgrading; the MCP server starts with the server.

### Enabling / Starting MCP Server (only till 1.4.2 version)

1. Navigate to **`Audit`** -> **`Scheduler Audit Logs`**
2. Click on the **`Enable Schedule`** action item against **`MCPServerMonitorSchedule`** to start the MCP Sever.
3. Once the schedule is enabled, the HTTP MCP server can be accessed at http(s)://\<YOUR\_HOT\_NAME>/mcp
4. To check the list of available tools check available tools section

### Stopping MCP Server (only till 1.4.2 version)

1. Navigate to **`Audit`** -> **`Scheduler Audit Logs`**
2. Click on the **`Disable Schedule`** action item to stop the MCP Sever.

### See Also

* [Configuring STDIO MCP Server](stdio-mcp-server-configuration.md)
* [Configuring HTTP MCP Server](http-mcp-server-configuration.md)
* [MCP Tools](mcp-tools.md)
