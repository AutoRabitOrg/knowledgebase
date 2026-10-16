---
description: >-
  Install the AutoRABIT CodeScan extension, sign in and run your first scan from
  the editor.
---

# VS Code Connection

The **AutoRABIT CodeScan** extension shows CodeScan findings inside VS Code, on the lines they belong to, so you can fix them before you open a pull request. This article takes you from installing it to your first scan.

### Before You Start

You need:

* **VS Code 1.134 or later.** Check in **`Help`** → **`About`**.
* **An API key**, or a CodeScan username and password. Ask your administrator for a key. See Create and Manage API Keys.
* **A registered repository**, opened as your VS Code workspace. See Register a Repository.

{% hint style="info" %}
**Note:** If you've already set up the CodeScan CLI with `codescan config`, the extension uses the same URL and sign-in. You can skip step 2.
{% endhint %}

### Step 1: Install the Extension

Choose one option.

#### Option A: From the Web App

1. In CodeScan, open **`Help`** → **`Download VS Code extension`**. The file is `codescan-vscode.vsix`.
2. In VS Code, open the Command Palette (**Ctrl+Shift+P** on Windows and Linux, **Cmd+Shift+P** on macOS).
3. Run **`Extensions: Install from VSIX…`** and select the file.

You can also install from a terminal, in the folder with the file:

```bash
code --install-extension codescan-vscode.vsix
```

On macOS, if `code` is not recognised, run **`Shell Command: Install 'code' command in PATH`** from the Command Palette first.

#### Option B: With the CodeScan CLI

```bash
codescan install vscode --url https://<your-codescan-url>
```

Leave out `--url` if you've already run `codescan config`.

Reload the window if VS Code asks you to. A shield icon appears in the Activity Bar. It opens the CodeScan view.

### Step 2: Connect and Sign In

1. Open **Settings** (**Ctrl+,** or **Cmd+,**) and search for **AutoRABIT CodeScan**.
2.  In **`Settings`**, set **`AutoRABIT CodeScan: Endpoint`** to your CodeScan URL, with no path after the host. Leave **`Web App URL`** empty unless your administrator tells you otherwise.

    The status bar changes from **CodeScan: no endpoint** to **CodeScan: not connected**.
3. Open the Command Palette and run **`CodeScan: Sign In`**. You can also select **CodeScan: not connected** in the status bar.
4. Choose how to sign in:
   * **`API key`**: paste your key.
   * **Username and password**: your CodeScan account.

You see _CodeScan: signed in._ and the status bar shows **CodeScan**.

Your sign-in is stored in your operating system's keychain, not in VS Code settings or your workspace. The CLI uses the same sign-in.

{% hint style="info" %}
**Note:** On Remote SSH, WSL and containers there is no system keychain. Sign in inside that environment, where you run the scan.
{% endhint %}

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 15.11.06.png" alt="" width="563"><figcaption></figcaption></figure>

### Step 3: Run Your First Scan

1. Save your files, and `git add` any new ones.
2. Open the Command Palette and run **`CodeScan: Scan Workspace`**.
3. When the scan finishes, check the repository result in the CodeScan view:

| Result          | What to do                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Registered      | Nothing. Your team's settings were applied, so your results match CI.                                                     |
| Unregistered    | The repository isn't registered, so default rules were used. Select **`Register Repository`**, or ask your administrator. |
| No remote found | The folder has no git remote. Open the repository folder rather than a subfolder or a copy.                               |

Findings now appear:

* in the **CodeScan view**, grouped by severity
* underlined in the editor
* in the **Problems** panel
* as a count in the status bar, for example **CodeScan: B1 C3 M12 m5** (Blocker, Critical, Major, Minor)

### Next Steps

* Scan only your changes, apply fixes and accept findings: Using the VS Code Extension
* Back to Getting Started, step 9

### Related Articles

* Connect the CLI
* Suggested Fixes and Patches
