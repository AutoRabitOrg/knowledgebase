# Guard MCP & Skill: User Guide

## Executive Overview

#### What this enables

AutoRABIT Guard can be used directly from supported AI assistants. The Guard **MCP** (Model Context Protocol server) gives those assistants secure access to Guard tools, while the **Skill** gives the assistant Guard-specific guidance so you can ask questions naturally.

With the Guard MCP and Skill, your team can:

* Ask questions in plain English and get back live security data from your Salesforce orgs
* Run classification analyses, risk assessments and permission audits from a terminal or AI assistant
* Export or script Guard data for reporting and reviews without leaving your workflow

#### How we keep your credentials safe

* **OAuth keeps passwords out of configuration files.** When you connect the MCP server in an AI assistant, authentication is handled through the browser using the same identity provider your team already uses.
* **Local auth material still needs to be protected.** The Guard Skill and command-line flows may cache authentication details locally under `~/.guard/configuration`, and API key mode relies on environment variables or command flags. Treat these as sensitive secrets.
* **Permissions follow the authentication method.** OAuth uses your Guard user permissions. API keys use tenant-bound standard access for the key, so they should be scoped and stored carefully.

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

## Decision guide

Use this guide when you are not sure which Guard interface fits the job.

| What you want to do                                             | Use                                    | Why                                                                                          |
| --------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------- |
| Review dashboards, filter tables or make admin changes          | Guard web UI                           | Best for visual review, setup tasks and actions that need careful confirmation               |
| Ask live questions about Guard data from an assistant           | Guard MCP                              | Best for natural-language questions, quick lookups and guided investigation                  |
| Help an AI assistant understand Guard terminology and workflows | Guard Skill + Guard MCP                | The Skill gives context; the MCP provides live data and tools                                |
| Run scripted checks in CI or another headless environment       | Guard API key mode                     | Works without browser-based OAuth                                                            |
| Build a custom automation around Guard data                     | Direct MCP integration                 | Lets your code discover typed Guard tools and call them through the MCP protocol             |
| Prepare audit notes or review evidence                          | Guard MCP, then Guard web UI if needed | The assistant can summarise findings; the UI is better for final evidence review and exports |

***

## Quickstart

Follow the path for the tool you are using.

### Claude

**Step 1: Add the MCP connector**

1. Go to **Customize → Connectors** and select **Add custom connector**.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2Fulqpz5nUTFp3Pd4oW6e4%2FScreenshot%202026-04-28%20143405.png?alt=media&#x26;token=0085f6fa-eadd-49d3-817a-60dfb76fe934" alt="" width="563"><figcaption></figcaption></figure>

2. Enter a name, for example `guard`, and your instance URL: `https://your-instance.autorabit.com/api/mcp` (**replace `your-instance`**).
3. Click **Add**.

**Step 2: Connect and authenticate**

The connector will appear in your list. Click **Connect** and complete the OAuth login in the browser.

**Step 3: Add the Skill file - Desktop app only**

1. In Guard, go to **Help → AI Integration** and download the Skill package.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FVWaRfrvgkRaXagvE6bJY%2FScreenshot%202026-04-29%20111441.png?alt=media&#x26;token=04f89aff-51d9-4111-aa1e-e25d32670e0c" alt="" width="382"><figcaption></figcaption></figure>

2. In Claude Code, go to **Customise** → **Skills**. Click **+** → **Create skill** → **Upload a skill**. Select the downloaded `guard-skill` folder.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FX27PO38zGspKGjkkQuX9%2FScreenshot%202026-04-28%20143709.png?alt=media&#x26;token=8bcf93b0-0d9e-47f2-bef3-11c6ce3d2044" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FLGQDPOTIYDwQrqrlix8C%2FScreenshot%202026-04-28%20143733.png?alt=media&#x26;token=a1703672-c60f-4578-b202-be92e394fba5" alt="" width="563"><figcaption></figcaption></figure>

**Step 4: Verify**

Ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. You may need to explicitly ask Claude to use Guard in your prompt, for example: _"use the Guard connector to list my orgs"_. Cross-check one org ID against the Guard web UI to confirm.

***

### Codex

**Step 1: Add the MCP server**

Open `~/.codex/config.toml` (create it if it does not exist) and add:

```toml
[mcp_servers.guard]
url = "https://your-instance.autorabit.com/api/mcp"
enabled = true
```

**Step 2: Authenticate**

Run the following in your terminal:

```bash
codex mcp login guard
```

This opens a browser and completes the OAuth login. Your session is stored automatically by Codex.

**Step 3: Add the Skill**

1. In Guard, go to **Help → AI Integration** and download the Skill package.
2. Move the downloaded `guard-skill` folder somewhere permanent on your machine, for example `~/tools/guard-skill`.
3. Add the Skill to the same `~/.codex/config.toml` file:

```toml
[[skills.config]]
path = "/Users/your-name/tools/guard-skill"
enabled = true
```

Replace `/Users/your-name/tools/guard-skill` with wherever you saved the folder.

4. Restart Codex.

**Step 4: Verify**

Ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. Cross-check one org ID against the Guard web UI to confirm.

***

### Cursor

**Step 1: Add the MCP server**

In the root of your project, create or edit `.cursor/mcp.json` (or `~/.cursor/mcp.json` to apply across all projects):

```json
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

Go to **Settings** (Cmd+Shift+J) → **Features** → **Model Context Protocol** and check that `guard` shows as healthy. If you see an error, open **Output** (Cmd+Shift+U) and select **MCP Logs** from the dropdown for details.

**Step 4: Verify**

In an Agent chat, ask: _"List all the Salesforce orgs connected to Guard"_

If you see org names and IDs returned, everything is working. Cross-check one org ID against the Guard web UI to confirm.

***

## Authentication

#### How authentication works

When you connect the Guard MCP, you are taken through an OAuth login flow. Guard authenticates you using the same credentials you use to log in to Guard normally, and your session is maintained by the MCP client.

You do not need to enter tokens manually for normal interactive use.

#### Skill and command-line authentication

The Guard Skill is separate from the MCP connection. If your assistant uses the Skill for local Guard commands, it may ask you to sign in separately or provide an API key. Local Skill authentication is cached under `~/.guard/configuration`.

#### Authentication for CI and scripted use

If you are running Guard from a CI pipeline or another automated context where a browser login is not possible, use a Guard API key.

```bash
export GUARD_API_KEY=your-api-key-here
```

The API key is sent to Guard as an `X-API-Key` header. Store it as a secured secret in your CI platform and never commit it to source control.

Other supported overrides for advanced use:

| Method                               | When to use                                                             |
| ------------------------------------ | ----------------------------------------------------------------------- |
| OAuth login                          | Normal interactive use in Claude, Cursor or Codex                       |
| `GUARD_API_KEY` environment variable | CI pipelines and shared automation environments                         |
| `--api-key` flag                     | One-off command-line use where an environment variable is not practical |

#### Common failure modes

| Error                                         | What it means                                                                   | Fix                                                             |
| --------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Connector shows "Disconnected" or "Reconnect" | Your OAuth session has expired                                                  | Click **Connect** again in the tool's MCP settings              |
| `GUARD_API_KEY` is set but you get a 401      | The key is expired, invalid or does not have access to the tenant               | Rotate the key in Guard and update your secret                  |
| Guard tools do not appear                     | The MCP connection is not healthy or the client has not refreshed its tool list | Reconnect the MCP server, reload the client and check MCP logs  |
| Skill commands fail but MCP tools work        | The Skill has a separate local authentication state                             | Sign in through the Skill flow again or provide `GUARD_API_KEY` |

## MCP tool contract

You only need this section if you are building tooling around the MCP server directly. AI assistants handle this discovery and tool calling for you in normal use.

The Guard MCP server exposes typed Guard tools. It does not expose a single generic command tool. MCP clients should discover the available tools through the MCP protocol, inspect each tool's description and input schema, then call the specific tool they need.

Typical tool categories include:

* Organisation and Salesforce org lookup
* Risk, classification and permission review
* Policy, monitoring and compliance data
* Export or reporting actions where supported

Tool responses are returned through the MCP protocol. Read tools return the requested Guard data directly. Some actions may return a confirmation while Guard continues work asynchronously in the background. For any tool that changes data or starts a job, review the action in the assistant before approving it.

#### Retry behaviour

The MCP server does not retry automatically. If a tool call fails:

1. Check the error text returned by the assistant or MCP client.
2. For authentication errors, reconnect the MCP server or refresh the Skill login, depending on which flow failed.
3. For transient network errors, retry read-only calls after confirming the Guard instance is reachable.
4. For write or job-starting tools, check Guard before retrying so you do not start the same action twice.

## Real prompt examples

Use these examples to confirm the connection and learn the kinds of questions Guard can answer.

| Prompt                                                           | Output                                                                                             |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| "List all Salesforce orgs connected to Guard."                   | Org names, org IDs, environment type and connection status.                                        |
| "Show the latest risk assessment for my production org."         | Overall risk status, highest-risk settings, last assessment time and suggested next review steps.  |
| "Which users have risky permissions in the EU production org?"   | Users, permission names, why each permission matters and where to review them in Guard.            |
| "Show public file exposure findings for this org."               | Exposed files, severity, owner or context where available and recommended remediation.             |
| "Summarise API security risks for this org."                     | API risk areas, affected users or connected apps where available and recommended follow-up checks. |
| "Prepare a 30-day audit summary for user activity monitoring."   | Key user activity events, unusual patterns, review notes and evidence to collect from Guard.       |
| "Compare the current risk posture with the previous assessment." | Important changes, newly introduced risks, resolved risks and items that still need review.        |

## Real workflows

#### 1. Security review

Use this when you want a quick read on an org's current security posture.

1. Ask Guard to list connected Salesforce orgs.
2. Choose the production or sandbox org you want to review.
3. Ask for the latest risk assessment and top risk categories.
4. Ask follow-up questions about the highest-risk users, settings or exposed data.
5. Use the Guard web UI for final review, exports or remediation actions.

Example prompt:

> List my connected Salesforce orgs, then help me review the highest risks for the production org.

Output:

A short security review with the selected org, current risk posture, top issues, recommended follow-up and any items that need manual review in Guard.

#### 2. Compliance check

Use this when you need evidence for an internal review or recurring audit.

1. Ask Guard for recent user activity, change monitoring and compliance policy signals.
2. Ask the assistant to summarise unusual activity, high-impact changes and unresolved policy deviations.
3. Ask for a review checklist that separates evidence already available in Guard from items that need manual confirmation.
4. Use the Guard web UI to validate the evidence and export anything required for the audit file.

Example prompt:

> Prepare a compliance review summary for the last 30 days using user activity monitoring, change monitoring and authorization policy data.

Output:

A review summary with notable events, policy deviations, suggested evidence, open questions and a checklist for the compliance owner.

## Troubleshooting Runbooks

#### "I don't have access to Guard" / no Guard tools appearing

1. Confirm the Guard MCP is connected in your tool's settings.
2. For Claude Code and Claude web: go to **Settings > Connectors** and check the Guard connector shows as connected. If disconnected, click **Connect**.
3. For Codex: run `codex mcp login guard` to re-authenticate.
4. For Cursor: check **Settings → Features → Model Context Protocol** and confirm `guard` is green. Check **Output → MCP Logs** for errors.
5. For Claude Code and Codex, also check that the Skill is loaded if you expect Skill-specific behaviour.

***

#### "Authentication is required to access Guard"

Your session has expired or the configured API key is not valid. Re-authenticate using the same method you used to set up:

* **Claude / Cursor**: go to the MCP settings, find Guard and click **Connect**.
* **Codex**: run `codex mcp login guard`.
* **API key mode**: rotate the key in Guard and update `GUARD_API_KEY` or the `--api-key` value.

***

#### Commands time out or hang

1. Check your network connection to your Guard instance URL.
2. Confirm your Guard instance is reachable by opening it directly in a browser.
3. Disconnect and reconnect, then retry.

***

#### Guard tools are missing or look outdated

1. Reload the AI client so it refreshes the MCP tool list.
2. Confirm the MCP server URL is `https://your-instance.autorabit.com/api/mcp`.
3. Check the client MCP logs for connection or authentication errors.
4. Reconnect the Guard MCP server if the session has expired.

***

#### Skill commands fail but MCP tools work

The Skill has its own local authentication state. Sign in again through the Skill flow or provide `GUARD_API_KEY`. If you recently moved the Skill folder, update the Skill path in your assistant configuration and restart the assistant.

***

#### CI pipeline: 401 Unauthorized

1. Confirm `GUARD_API_KEY` is set: `echo $GUARD_API_KEY | cut -c1-4` prints the first four characters without exposing the full key.
2. Check the key has not expired and has access to the tenant you are querying.
3. Verify the instance URL is correct and does not have a trailing slash.

***

#### Still stuck?

Contact the AutoRABIT support team with:

* The Guard instance URL you are connecting to
* The AI assistant you are using
* A description of the error or unexpected behaviour
* Any error text shown in the connector, assistant or MCP logs
