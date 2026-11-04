# Kiro Extension - Install and Run

This guide explains how to install the AutoRABIT CodeScan 2.0 extension in Kiro and run a scan from the editor. Findings show up in the CodeScan view, on the lines they belong to, and in Kiro’s Problems panel, before the code reaches a pull request.

Kiro uses the same extension package as Visual Studio Code. Download `codescan-vscode.vsix` and install it into Kiro. Kiro’s extension search uses Open VSX, and this package is not listed there. An install in Kiro is separate from an install in VS Code or Cursor.

The editor command is `kiro`. That is separate from `kiro-cli`, which is Kiro’s terminal assistant and does not install editor extensions.

## Before you start

Please check prerequisites:

* **Kiro** built on VS Code 1.128 or newer. Open Help → About and read the VS Code version. Recent Kiro 0.12 builds, including 0.12.200 and 0.12.301, report VS Code 1.107.1. On that base Kiro refuses this package. Upgrade Kiro when a release reports 1.128 or newer, then install.
* **The `kiro` command on your PATH**, if you install from a terminal. On macOS, open the Command Palette and run **Shell Command: Install 'kiro' command in PATH**.
* **A CodeScan API key**, or a CodeScan username and password. An administrator creates a key under API Keys. Ask an admin if that page is not in your account.
* **A git repository** opened as the workspace. Only git-tracked files are scanned.
* **The CodeScan CLI**, only if you choose the CLI install path below. If you already ran `codescan config`, the extension can use that URL and credential and you can skip Set up the endpoint and Sign in.

## Install the extension

Use either the manual VSIX install or the CodeScan CLI. You only need one of them. The download needs no sign-in. The extension is published as AutoRABIT CodeScan.

### Option 1: Manual install

Download the package from CodeScan Help → Download VS Code extension. The file is named `codescan-vscode.vsix`.

Install it from a terminal in the folder that contains the file:

kiro --install-extension codescan-vscode.vsix

Or in Kiro: open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run Extensions: Install from VSIX…. You can also open the Extensions view, open the … menu (Views and More Actions), and choose Install from VSIX.... Select `codescan-vscode.vsix`.

Reload the window if Kiro asks you to. The Activity Bar shows a shield icon. Open it to reach the CodeScan view.

### Option 2: Install with the CodeScan CLI

With the CodeScan CLI already installed and able to reach the instance, run:

codescan install vscode --url CUSTOM\_URL --binary kiro

Replace `CUSTOM_URL` with your instance URL. The command name stays `install vscode` because the package is the VS Code extension. `--binary kiro` installs it with the Kiro editor command.

The command downloads the VSIX that instance serves and installs it with the `kiro` CLI.

Omit `--url` when `~/.codescan/configuration` already points at that instance. The file stores the URL only. No secrets are written there.

codescan install vscode --binary kiro

If the `kiro` command is not on your PATH, or the install fails, the command keeps the downloaded `.vsix` and tells you where it is, so you can install it by hand with Extensions: Install from VSIX….

## Set up the endpoint

Skip this section if you already ran `codescan config` or `codescan auth login`. The extension shares that URL.

Open Kiro Settings (`Ctrl+,` / `Cmd+,`) and search for AutoRABIT CodeScan.

Set AutoRABIT CodeScan: Endpoint (`autorabit.codescan.endpoint`) to the application origin:

CUSTOM\_URL

Replace `CUSTOM_URL` with your instance URL. Leave Web App URL empty unless the web app is hosted on a different host from the endpoint. Use only the scheme and host, with no path.

The status bar item changes from CodeScan: no endpoint to CodeScan: not connected. If Endpoint is left empty, the extension uses the URL saved by the CLI in `~/.codescan/configuration`.

## Sign in

Create an API key under API Keys → Create API Key. Creating a key requires an admin account. The key is shown once.

Then sign in from Kiro. The command name in the palette is CodeScan: Sign In. The same command is behind the Sign In link in the CodeScan view and behind the CodeScan: not connected status bar item.

1. Open the Command Palette: `Ctrl+Shift+P` on Windows and Linux, or `Cmd+Shift+P` on macOS.
2. Run CodeScan: Sign In.
3. Choose one:
   * API key. Paste the key.
   * Username and password. Your CodeScan account. The extension refreshes the session in the background.

On success you see CodeScan: signed in. and the status bar item reads CodeScan.

The credential is stored in the operating-system secret store: macOS Keychain, Windows credential store, or Linux libsecret. It is not written to settings, workspace files, or `~/.codescan/configuration`. The extension and the CodeScan CLI share that store, so a sign-in in one is picked up by the other. CodeScan: Sign Out signs both out.

The same sign-in from a terminal, which prompts for the key:

codescan auth login --api-key

Interactive setup in the terminal is `codescan config`.

On Remote SSH, WSL, and containers there is no system keyring. There the extension keeps the key in Kiro Secret Storage, and the CLI uses the `CODESCAN_API_KEY` environment variable. Those two stores are separate, so sign in inside the environment where you run the scan.

## Run a scan

Open the git repository you want analysed. Save your editors first. `git add` new files before Scan Changed Files: an unsaved edit is uploaded as context but not judged, and a file you never added is invisible to git.

Start a scan from the Command Palette or from the CodeScan view:

| Command                       | What it analyses                                                                          | Same in CLI               |
| ----------------------------- | ----------------------------------------------------------------------------------------- | ------------------------- |
| CodeScan: Scan Workspace      | The open workspace                                                                        | `codescan review`         |
| CodeScan: Scan Changed Files  | Files that differ from HEAD, staged and unstaged                                          | `codescan review --local` |
| CodeScan: Scan Branch Changes | Commits on this branch since it forked from its base. Uncommitted edits are not included. | `codescan review --pr`    |

Each scan runs the AI reviewer and spends scan credits. A second scan stays disabled until the current one finishes or you cancel it.

Scan Branch Changes looks for the base branch in this order: the `autorabit.codescan.baseBranch` setting, the project’s comparison base branch in CodeScan, the clone’s `origin/HEAD`, the remote’s `origin/HEAD`, then `origin/main`, then `origin/master`. If none answers, it tells you what it tried.

The whole workspace is uploaded even for a narrowed scan, so rules that look across files keep their context. Only the files reported on are narrowed. If nothing differs, or everything that differs is excluded, the extension says so. That is not a clean result.

Progress is written to the extension log. CodeScan: Show Output opens it. If a scan outlives `autorabit.codescan.publishTimeoutSeconds` (default 3600), the notification closes but the status bar keeps watching, and the findings load when it finishes.

## Read the results

When the scan finishes:

* The CodeScan view groups findings by severity. Accepted findings and Likely false positives have their own groups. Click a row to open that file at the reported line.
* The same findings are underlined in the editor and listed in the Problems panel.
* The status bar shows the outcome by severity, for example CodeScan: B7 C10 M20 m11 (blocker, critical, major, minor). CodeScan: 0 is a clean scan. CodeScan: stale means you edited a scanned file; click it to rescan.
* The scan is saved under Agentic Code Analysis as SCA-n, the same kind of record a CI run produces.

Each finding row offers:

| Action                        | What it does                                                                                                                                                                       |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Show Rule Description         | Opens what the rule checks, and the suggested fix when there is one.                                                                                                               |
| CodeScan: Apply Suggested Fix | Lightbulb on the squiggle, or `Ctrl+.` / `Cmd+.`. CodeScan re-checks the fix against the file as it is now. If the code has moved, nothing is changed, and you are told to rescan. |
| Accept Finding                | Marks the finding as an accepted false positive or an acceptable risk for this repository. It loses its squiggle and stays accepted on later scans, including CI.                  |
| Restore Finding               | Reverses an acceptance.                                                                                                                                                            |

Accepting needs a git remote, so CodeScan knows which repository the decision belongs to.

On each scan the extension sends your git remote so CodeScan can apply that repository’s settings:

| Result          | Meaning                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| Registered      | The repository’s settings were applied. Results match CI.                                                     |
| Unregistered    | A remote exists, but the repository is not registered, so default rules were used. Click Register Repository. |
| No remote found | Scanned on defaults and recorded under the folder name. How to Connect explains the steps.                    |

If the AI reviewer is off, fails, or credits run out, deterministic findings are still shown. The scan does not fail only because AI was unavailable.

Editing a scanned file withdraws that file’s squiggles, so they never point at the wrong line. The finding stays in the CodeScan view, marked stale, until you scan again.

CodeScan: Export Scan Results saves the last scan as a SARIF 2.1.0 file.

## Troubleshooting

#### Install from VSIX does nothing, or `kiro` is not recognized

Confirm Help → About shows a VS Code version of 1.128 or newer, and that `kiro` is on your PATH. Use the editor command `kiro`, not `kiro-cli`. From inside Kiro, run Extensions: Install from VSIX… and select the downloaded file. If `codescan install vscode --binary kiro` could not find the editor command, it keeps the `.vsix` and prints the path.

#### The extension is not compatible with this version of the editor

Kiro’s VS Code base is older than 1.128. Help → About shows the version it is built on. Update Kiro, then install the VSIX again.

#### CodeScan: Sign In is missing

The extension is not enabled for this window. Reload the window, then open the Command Palette and type CodeScan: Sign In.

#### The scan reports authentication required, or CodeScan rejected the API key

The key is missing, wrong, expired, or revoked. Sign in again in the same environment where you run the scan. On a normal desktop, CodeScan: Sign In and `codescan auth login --api-key` write the same OS secret. On Remote SSH, WSL, or a container, set `CODESCAN_API_KEY` for the CLI and sign in again inside that Kiro window for the extension.

#### Your CodeScan session has expired

Run CodeScan: Sign In again.

#### The endpoint is rejected, or the extension cannot reach the host

Set AutoRABIT CodeScan: Endpoint to `CUSTOM_URL` with no path, and leave Web App URL empty unless the web app is on another host. For a dev certificate this machine does not trust, enable `autorabit.codescan.allowUnauthorizedCertificate` only if you trust that host.

#### API Keys is not in the web app

The signed-in user is not an admin. Ask an administrator to create the key and send it to you. Paste that key into CodeScan: Sign In.
