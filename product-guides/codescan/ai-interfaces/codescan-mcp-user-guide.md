# CodeScan MCP: User Guide

## Executive Overview

**Bring CodeScan into your AI assistant**

CodeScan's analysis has always lived in the web app. With the CodeScan MCP (Model Context Protocol) server, that same analysis data becomes something you can query conversationally from the AI coding assistant you already use — no dashboard-hopping, no re-authenticating in a browser tab mid-task.

Once connected, you can stay in your editor and simply ask for what you need:

* Check which projects are passing or failing their quality gate, in plain language
* Drill into issues, security hotspots, rules, and measures without opening the web UI
* Look up organizations, projects, branches, pull requests, and analysis-job details as you code
* Pull CodeScan data into your own reporting or review workflow on demand

Because it's a hosted, streamable endpoint, there's no local server to install or maintain. You add the CodeScan MCP URL to your assistant's configuration, provide your instance URL and a personal token, and you're ready to go.

**Security and access model**

* **Requests are scoped to your instance.** Each call includes your CodeScan instance URL, so the assistant only ever reads from the tenant you specify.
* **Your token, your identity.** Authentication relies on a token you generate inside CodeScan and store locally in your assistant's config. The AI vendor never issues, sees, or holds your token.
* **Access mirrors your CodeScan role.** The assistant is limited to exactly what your user account can already view in CodeScan — nothing is unlocked or elevated.
* **Revocable at any time.** Delete or rotate the token in CodeScan and the connection is cut off immediately.

{% hint style="info" %}
Treat the token like any other credential. Keep it in your local MCP configuration or a secrets manager, and never check it into Version Control.
{% endhint %}

**Where it works**

The CodeScan MCP server connects to any AI assistant that speaks remote MCP over HTTPS and can send custom request headers. Here's where we've confirmed it and what each option suits best:

* **GitHub Copilot (VS Code)** — Fully tested. The go-to setup for most CodeScan users.
* **GitHub Copilot (IntelliJ IDEA)** — Fully tested. Ideal for JetBrains teams on Community or Ultimate.
* **Cursor** — Expected to work. A natural fit if Cursor is already your primary IDE.
* **Claude Desktop** — Expected to work. Great for open-ended, conversational exploration of your data.

Other MCP-capable clients that support custom HTTPS endpoints with headers should work as well.

## Quickstart

Follow the path below for the tool you are using. Every path needs three values:

* \<MCP-URL> — the remote MCP endpoint:

US:

```
https://mcp-us.codescan.io/mcp
```

EU:

```
 https://mcp-eu.codescan.io/mcp
```

AUS:

```
https://mcp-aus.codescan.io/mcp
```

* \<CODESCAN-URL> — the URL of your CodeScan instance (for example, [https://app.codescan.io](https://app.codescan.io/)).
* \<CODESCAN-TOKEN> — a user token generated from your CodeScan account (see "Generating your CodeScan token").

### GitHub Copilot in VS Code

**Step 1:** Install and sign in to GitHub Copilot.

Open Visual Studio Code, open the Extensions view (Ctrl+Shift+X on Windows/Linux, Cmd+Shift+X on macOS), and search for GitHub Copilot. Install the GitHub Copilot extension published by GitHub. Sign in by opening the Command Palette (Ctrl+Shift+P / Cmd+Shift+P), running GitHub Copilot: Sign in, and completing the GitHub authorization in your browser.

**Step 2:** Add the CodeScan MCP server to your Copilot MCP configuration.

Click on **Configure tools** → **Add MCP Server** → **Connect to a remote MCP Server** and provide the MCP URL.

Replace the script in the _mcp.json_ with the following:

```
{
  "servers": {
    "cs-ai-mcp-streamable": {
      "url": "<MCP-URL>",
      "type": "http",
      "headers": {
        "CODESCAN-URL": "<CODESCAN-URL>",
        "CODESCAN-TOKEN": "<CODESCAN-TOKEN>"
      }
    }
  }
}
```

{% hint style="info" %}
Replace \<MCP-URL> with the remote MCP endpoint, \<CODESCAN-URL> with your CodeScan instance URL, and \<CODESCAN-TOKEN> with your user token.
{% endhint %}

**Step 3:** Reload and verify.&#x20;

Reload VS Code, then open Copilot Chat and ask: "List all the organizations in CodeScan." If you see your organizations returned, everything is working. Cross-check one organization against the CodeScan web UI to confirm.

{% hint style="info" %}
You can also find a recorded step-by-step guide for installing our MCP in VS Code in the Demos section of this page.
{% endhint %}

### GitHub Copilot in IntelliJ IDEA

**Step 1:** Install and sign in to GitHub Copilot.&#x20;

Open IntelliJ IDEA (Community or Ultimate), go to Settings/Preferences → Plugins → Marketplace, search for GitHub Copilot, click Install, and restart the IDE. After the restart, open Settings/Preferences → GitHub Copilot, click Sign in with GitHub, and complete the browser login and authorization. Back in Settings/Preferences → GitHub Copilot, make sure Enable GitHub Copilot is turned on.

**Step 2:** Add the CodeScan MCP server to your Copilot MCP configuration:

```
{
  "servers": {
    "cs-ai-mcp-streamable": {
      "url": "<MCP-URL>",
      "requestInit": {
        "headers": {
          "CODESCAN-URL": "<CODESCAN-URL>",
          "CODESCAN-TOKEN": "<CODESCAN-TOKEN>"
        }
      }
    }
  }
}
```

{% hint style="info" %}
Replace \<MCP-URL> with the remote MCP endpoint, \<CODESCAN-URL> with your CodeScan instance URL, and \<CODESCAN-TOKEN> with your user token. Note that IntelliJ nests the headers inside a requestInit block, whereas VS Code uses headers directly.
{% endhint %}

**Step 3:** Reload and verify.&#x20;

Restart IntelliJ, then open the Copilot chat and ask: "List all the organizations in CodeScan." If you see your organizations returned, everything is working. Cross-check one organization against the CodeScan web UI to confirm.

{% hint style="info" %}
You can also find a recorded step-by-step guide for installing our MCP in IntelliJ in the Demos section of this page.
{% endhint %}

### Cursor

**Step 1:** Add the MCP server.&#x20;

In the root of your project, create or edit _.cursor/mcp.json_ (or _\~/.cursor/mcp.json_ to apply across all projects):

```
{
  "mcpServers": {
    "cs-ai-mcp-streamable": {
      "url": "<MCP-URL>",
      "type": "http",
      "headers": {
        "CODESCAN-URL": "<CODESCAN-URL>",
        "CODESCAN-TOKEN": "<CODESCAN-TOKEN>"
      }
    }
  }
}
```

{% hint style="info" %}
Replace \<MCP-URL> with the remote MCP endpoint, \<CODESCAN-URL> with your CodeScan instance URL, and \<CODESCAN-TOKEN> with your user token.
{% endhint %}

**Step 2:** Reload and confirm the connection.&#x20;

Reload Cursor (Cmd/Ctrl+Shift+P → Developer: Reload Window). Then open Settings → Features → Model Context Protocol and check that cs-ai-mcp-streamable shows as healthy. If you see an error, open Output and select MCP Logs from the dropdown for details.

**Step 3:** Verify.&#x20;

In an Agent chat, ask: "List all the organizations in CodeScan." If you see your organizations returned, everything is working.

### Claude Desktop / other MCP clients

Hypothetically, any MCP client that supports a remote HTTPS endpoint with custom request headers can connect. Point it at our remote MCP endpoint and supply the two headers CODESCAN-URL and CODESCAN-TOKEN with your instance URL and user token. Then verify by asking the client to "list all the organizations in CodeScan."

## Authentication

**How authentication works**

The CodeScan MCP server authenticates each request using two values that you place in your AI assistant's MCP configuration:

* CODESCAN-URL — the URL of your CodeScan instance.
* CODESCAN-TOKEN — a user token generated from your CodeScan account.

Every tool call the assistant makes is sent with these headers, so the server knows which CodeScan instance to talk to and authenticates as your user. There is no separate login step or session to manage — as long as the token is valid, the connection works.

**Generating your CodeScan token**

1. Log in to your CodeScan instance in a browser.
2. Open your account menu and go to My Account → Security (Tokens).
3. Enter a name (for example, mcp), generate the token, and copy it immediately — it is shown only once.
4. Paste it into your MCP configuration as the value for CODESCAN-TOKEN.

To revoke access, return to the same page and delete the token; the MCP connection stops working immediately.

## Available Tools

The CodeScan MCP server exposes 32 tools, grouped into the functional areas below. In normal use, your AI assistant selects the right tool automatically based on your question; you don't need to name a tool directly.

| #  | Functional Area          | Tools                                                                                                                     |
| -- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 1  | Organizations            | listOrganizations, getOrganization, checkOrganizationExists                                                               |
| 2  | Projects                 | searchProjects                                                                                                            |
| 3  | Branches & Pull Requests | listProjectBranches, listPullRequests                                                                                     |
| 4  | Components               | showComponent, getComponentTree                                                                                           |
| 5  | Issues                   | searchIssues, getIssueChangelog, listIssueTags                                                                            |
| 6  | Security Hotspots        | searchSecurityHotspots, showSecurityHotspot                                                                               |
| 7  | Measures & Metrics       | getMeasuresForComponent, getMeasureComponentTree, getMeasureHistory                                                       |
| 8  | Quality Gates            | getQualityGateProjectStatus, getQualityGateByProject, listQualityGates, showQualityGateDetails, searchQualityGateProjects |
| 9  | Quality Profiles         | searchQualityProfiles, getQualityProfileChangelog, getQualityProfileInheritance, getQualityProfileProjects                |
| 10 | Rules                    | searchRules, showRuleDetails                                                                                              |
| 11 | Languages                | listLanguages                                                                                                             |
| 12 | Analysis Jobs            | searchAnalysisJobs, getJobDetails                                                                                         |
| 13 | Integrations             | listIntegrations, getIntegration                                                                                          |

Example questions you can ask:

* "Which projects in my organization are failing their quality gate?"
* "Show me the open blockers and critical issues for project X."
* "List the security hotspots in the latest analysis and explain the top one."
* "What rules are in the quality profile applied to project Y?"
* "Show the coverage and code-smell trend for this project over time."

### Troubleshooting runbooks

#### **No CodeScan tools appear / assistant says it can't reach CodeScan**

1: Confirm the MCP server is configured and enabled in your tool's settings:

For GitHub Copilot (VS Code / IntelliJ), confirm the cs-ai-mcp-streamable entry exists in your MCP configuration and that Copilot is signed in and enabled, and reload/restart the IDE after any change.&#x20;

For Cursor, check Settings → Features → Model Context Protocol and confirm cs-ai-mcp-streamable is green, and check Output → MCP Logs for errors.&#x20;

2. Verify the MCP endpoint URL

***

#### **Authentication or 401 errors**

1. Confirm CODESCAN-TOKEN is set and has not been revoked or expired. You can generate a new token in My Account → Security and update your configuration.&#x20;
2. Confirm the token's user has permission to view the organizations and projects you are asking about: the MCP server can only return what your user can see in CodeScan.&#x20;
3. Confirm CODESCAN-URL points to the correct instance and has no trailing slash.

***

#### **Commands time out or hang**

1. Check your network connection to the MCP endpoint and to your CodeScan instance.&#x20;
2. Confirm your CodeScan instance is reachable by opening its URL directly in a browser.&#x20;
3. Reload/restart your assistant, then retry.

***

#### **Wrong or empty results**

1. Double-check CODESCAN-URL; pointing at the wrong instance is the most common cause of "missing" data.&#x20;
2. Cross-check one result against the CodeScan web UI to confirm you are connected to the expected tenant.
