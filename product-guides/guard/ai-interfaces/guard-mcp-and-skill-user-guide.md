# Guard MCP & Skill: User Guide

## Executive Overview

#### What this enables

AutoRABIT Guard can now be operated directly from your AI coding assistant of choice, so you can skip the browser altogether. The Guard **MCP** (Model Context Protocol server) and **Skill** give tools like Claude Code and Codex a direct connection to the Guard platform, so your team can do things like:

* Ask questions in plain English and get back live security data from your Salesforce orgs
* Run classification analyses, risk assessments and permission audits from a terminal
* Export or script Guard data for reporting and reviews without leaving your terminal

#### How we keep your credentials safe

* **No credentials leave your machine.** Authentication is handled automatically via OAuth when you connect, using the same identity provider your team already uses. No tokens are stored in config files or passed manually.
* **Permissions are your Guard permissions.** The AI assistant can only do what your logged-in user is allowed to do in Guard. No privilege escalation is possible.

## Compatible tools

Guard's MCP works with any AI coding assistant that supports MCP over HTTPS and can complete the OAuth login flow. The table below lists the tools we have tested and the level of support each offers.

| Tool                                       | Support    | Best for                                                                                        |
| ------------------------------------------ | ---------- | ----------------------------------------------------------------------------------------------- |
| Claude Code (desktop)                      | ✓ Full     | Day-to-day use; the Skill gives the assistant built-in Guard knowledge so you can ask naturally |
| Codex (OpenAI CLI or app)                  | ✓ Full     | Terminal-first teams who want the same depth of Guard integration as Claude Code                |
| Claude web ([claude.ai](http://claude.ai)) | ✓ MCP only | Fastest setup; occasional use or less technical users                                           |
| Cursor                                     | ✓ Full     | Teams already using Cursor as their primary IDE                                                 |
| GitHub Copilot Chat                        | ✗          | —                                                                                               |
| ChatGPT (web or app)                       | ✗          | —                                                                                               |

Any tool not listed here that supports MCP over a custom HTTPS endpoint may also work.

***

## Quickstart

Follow the path for the tool you are using.

### Claude

**Step 1: Add the MCP connector**

1. Go to **Settings → Connectors** and select **Add custom connector**.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-04-28 143405.png" alt="" width="563"><figcaption></figcaption></figure>

2. Enter a name (e.g. guard) and _your instance_ URL: https://your-instance.autorabit.com/api/mcp (**replace "your-instance"**)
3. Click **Add**.

**Step 2: Connect and authenticate**

The connector will appear in your list. Click **Connect** and complete the OAuth login. Authentication is handled automatically in the browser.

**Step 3: Add the Skill file - Desktop app only**

1. In Guard, go to **Help → AI Integration** and download the Skill package.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-04-29 111441.png" alt="" width="382"><figcaption></figcaption></figure>

2. In Claude Code go to **Customise** → **Skills**. Click + → Create skill → Upload a skill. Select the downloaded guard-skill folder.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-04-28 143709.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2026-04-28 143733.png" alt="" width="563"><figcaption></figcaption></figure>

**Step 4: Verify**

Ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. You may need to explicitly ask Claude to use Guard in your prompt, for example: _"use the guard connector to list my orgs"_. Cross-check one org ID against the Guard web UI to confirm.

***

### Codex

**Step 1: Add the MCP server**

Open \~/.codex/config.toml (create it if it does not exist) and add:

```
[mcp_servers.guard]
url = "https://your-instance.autorabit.com/api/mcp"
enabled = true
```

**Step 2: Authenticate**

Run the following in your terminal:

```
codex mcp login guard
```

This opens a browser and completes the OAuth login. Your session is stored automatically.

**Step 3: Add the Skill**

1. In Guard, go to **Help → AI Integration** and download the Skill package.
2. Move the downloaded guard-skill folder somewhere permanent on your machine, for example \~/tools/guard-skill.
3. Add the Skill to the same \~/.codex/config.toml file:

```
[[skills.config]]
path = "/Users/your-name/tools/guard-skill"
enabled = true
```

Replace /Users/your-name/tools/guard-skill with wherever you saved the folder.

4. Restart Codex.

**Step 4: Verify**

Ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. Cross-check one org ID against the Guard web UI to confirm.

***

### Cursor

**Step 1: Add the MCP server**

In the root of your project, create or edit .cursor/mcp.json (or \~/.cursor/mcp.json to apply across all projects):

```
{
  "mcpServers": {
    "guard": {
      "url": "https://your-instance.autorabit.com/api/mcp"
    }
  }
}
```

**Step 2: Reload and authenticate**

Reload Cursor (Cmd+Shift+P → **Developer: Reload Window**). If Cursor prompts for OAuth, complete the login in the browser.

**Step 3: Confirm the connection**

Go to **Settings** (Cmd+Shift+J) → **Features** → **Model Context Protocol** and check that guard shows as healthy. If you see an error, open **Output** (Cmd+Shift+U) and select **MCP Logs** from the dropdown for details.

**Step 4: Verify**

In an Agent chat, ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. Cross-check one org ID against the Guard web UI to confirm.

***

## Authentication

#### How authentication works

When you connect the Guard MCP, you are taken through an OAuth login flow. This is fully automatic. Guard authenticates you using the same credentials you use to log in to Guard normally, and your session is maintained by the connector.

**You do not need to run any commands, enter tokens manually, or manage config files for normal use.**

#### Authentication for CI and scripted use

If you are running Guard commands in a CI pipeline or another automated context where a browser login is not possible, use the GUARD\_API\_TOKEN environment variable:

```
export GUARD_API_TOKEN=your-token-here
```

When this is set and non-empty, Guard skips the OAuth flow entirely and uses the token directly. Store this as a secured secret in your CI platform. Never commit it to source control.

Other supported overrides for advanced use:

| Method                                      | When to use                                              |
| ------------------------------------------- | -------------------------------------------------------- |
| GUARD\_API\_TOKEN environment variable      | CI pipelines, shared environments                        |
| GUARD\_GRAPHQL\_BEARER environment variable | When you already have a bearer token from another source |
| --bearer flag                               | One-off overrides on a single command                    |

#### Common failure modes

| Error                                         | What it means                                             | Fix                                              |
| --------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| Connector shows "Disconnected" or "Reconnect" | Your OAuth session has expired                            | Click Connect again in Settings > Connectors     |
| GUARD\_API\_TOKEN set but getting 401         | Token is expired or has insufficient permissions          | Rotate the token in Guard and update your secret |
| Method not found or Unknown tool              | The connector is connected but something is misconfigured | Remove and re-add the connector                  |

## JSON Output Contract

You only need to understand this section if you're building tooling around the MCP server directly. Your AI assistant will handle all of this for you in normal use.

#### The runCmd tool

The MCP server exposes a single tool:

```
{
  "name": "runCmd",
  "inputSchema": {
    "type": "object",
    "properties": {
      "command": {
        "type": "string",
        "description": "Guard CLI arguments after the binary name, e.g. 'get orgs'"
      }
    },
    "required": ["command"]
  }
}
```

#### Successful response

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "...Guard CLI output here..."
      }
    ],
    "isError": false
  }
}
```

#### Error response (Guard command failed)

When the Guard CLI itself returns a non-zero exit code, isError is set to true but the response is still a valid MCP result (not a JSON-RPC error):

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Authentication is required to access Guard"
      }
    ],
    "isError": true
  }
}
```

#### Protocol error (malformed request)

If the request itself is invalid (wrong method name, missing parameters, unparseable JSON), you'll receive a JSON-RPC error instead:

```
{
  "jsonrpc": "2.0",
  "id": null,
  "error": {
    "code": -32602,
    "message": "Parameter 'command' is required and must not be empty."
  }
}
```

#### Retry behaviour

The MCP server does not retry automatically. If a command fails with isError: true:

1. Check the text field for a human-readable error message.
2. For authentication errors, reconnect the connector in Settings > Connectors, then retry.
3. For transient network errors, a simple retry of the same runCmd call is safe. Guard read commands (get) are idempotent.
4. For write commands (run, admin), check the Guard UI before retrying to avoid duplicate operations.

## Troubleshooting Runbooks

#### "I don't have access to Guard" / no Guard tools appearing

1. Confirm the Guard MCP is connected in your tool's settings.
2. For Claude Code and Claude web: go to **Settings > Connectors** and check the Guard connector shows as connected. If disconnected, click **Connect**.
3. For Codex: run codex mcp login guard to re-authenticate.
4. For Cursor: check **Settings → Features → Model Context Protocol** and confirm guard is green. Check **Output → MCP Logs** for errors.
5. For Claude Code and Codex, also check that the Skill is loaded.

***

#### "Authentication is required to access Guard"

Your session has expired. Re-authenticate using the same method you used to set up:

* **Claude / Cursor**: go to Settings > Connectors, find Guard, and click **Connect**.
* **Codex**: run codex mcp login guard.

***

#### Commands time out or hang

1. Check your network connection to your Guard instance URL.
2. Confirm your Guard instance is reachable by opening it directly in a browser.
3. Disconnect and reconnect, then retry.

***

#### "Unknown tool: runCmd" in logs

This usually means the Guard Skill file is not loaded. Check that the Skill is present in your assistant's Skills section (Claude) or that \[\[skills.config]] points to the correct path (Codex), then restart your assistant.

***

#### CI pipeline: 401 Unauthorized

1. Confirm GUARD\_API\_TOKEN is set: echo $GUARD\_API\_TOKEN | cut -c1-4 (prints the first four characters without exposing the full token).
2. Check the token has not expired. Rotate it in Guard and update your pipeline secret if needed.
3. Verify the instance URL is correct and does not have a trailing slash.

***

#### Still stuck?

Contact the AutoRABIT support team with:

* The Guard instance URL you are connecting to
* The AI assistant you are using
* A description of the error or unexpected behaviour
* Any error text shown in the connector or assistant logs
