---
description: Let Claude Code run CodeScan before every commit and pull request.
---

# AI Coding Agents

AI coding agents write code quickly, so it needs checking just as quickly. The CodeScan skill teaches Claude Code to scan its own work before it commits and before it opens a pull request.

### What the Skill Does

* Before a commit, the agent runs `codescan review --local --json` and reports findings by severity.
* Before a pull request, it runs `codescan review --pr --json`.
* It adds a `/codescan` command.
* It adds a safety check: the agent cannot run `git push`, `gh pr create` or `bkt pr create` until the current commit has a clean branch review. The check reads the last result. It does not run a scan itself.

### Installing the Skill

You need the CodeScan CLI installed and signed in. See Connect the CLI.

For the current project:

```bash
codescan install skill
```

For every project on your computer:

```bash
codescan install skill --global
```

The skill is written to the project's `.claude/` folder, or to your home folder with `--global`. The command then checks your credential.

| Option        | Effect                    |
| ------------- | ------------------------- |
| `--force`     | Replace an existing skill |
| `--no-verify` | Skip the credential check |

### Related Articles

* Connect the CLI
* CLI Reference
