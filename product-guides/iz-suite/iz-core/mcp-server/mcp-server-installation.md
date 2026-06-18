# MCP Server Installation

## Enabling IZ MCP Server

{% hint style="warning" %}
* MCP server feature requires IZ Suite version 1.4.0 or above
{% endhint %}

The following section describes the steps required to enable and start the IZ MCP server.

### Enabling / Starting MCP Server

1. Navigate to **`Audit`** -> **`Scheduler Audit Logs`**
2. Click on the **`Enable Schedule`** action item against **`MCPServerMonitorSchedule`** to start the MCP Sever.
3. Once the schedule is enabled, the HTTP MCP server can be accessed at http(s)://\<YOUR\_HOT\_NAME>/mcp
4. To check the list of available tools check available tools section

### Stopping MCP Server

1. Navigate to **`Audit`** -> **`Scheduler Audit Logs`**
2. Click on the **`Disable Schedule`** action item to stop the MCP Sever.

### See Also

* [Configuring STDIO MCP Server](stdio-mcp-server-configuration.md)
* [Configuring HTTP MCP Server](http-mcp-server-configuration.md)
* [MCP Tools](mcp-tools.md)
