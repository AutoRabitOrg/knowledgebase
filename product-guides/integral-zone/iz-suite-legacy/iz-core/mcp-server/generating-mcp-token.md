# Generating MCP Token

## Configuring Access Token for IZ MCP Server

To configure the IZ MCP Server, you must generate a valid access token. Follow the steps below:

### 1. Create a Role

1. Navigate to **`Organization`** → **`Roles`**
2. Click **`Create Role`**
3. Name the role as **`MCP Role`** or any meaningful equivalent\
   (skip this step if the role already exists)

### 2. Assign Permissions

1. Assign the appropriate permissions to the role based on the tools being used
2. For details on permissions required for each tool, refer to:\
   MCP Server Tools

### 3. Generate Access Token

1. Navigate to **`Organization`** → **`Tokens`**
2. Click **`Generate Token`**
3. Select the role created earlier
4. Provide a token name
5. Click **`Submit`**
6. Copy the generated access token — **it will be shown only once**

### See Also

* [Enabling MCP Server](mcp-server-installation.md)
* [Configuring STDIO MCP Server](stdio-mcp-server-configuration.md)
* [Configuring HTTP MCP Server](http-mcp-server-configuration.md)
* [MCP Tools](mcp-tools.md)
