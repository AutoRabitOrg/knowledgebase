---
description: Export scan results as HTML, SARIF, JUnit, GitLab Code Quality or JSON.
---

# Reports and Export

CodeScan writes results in the formats that other tools already read, so findings can appear in your build server, your git host and your security tools.

## From the Web App

On a scan page, **`Export Report`** downloads a standalone HTML report. It needs no sign-in to open, so it works as evidence for audits or for sharing outside CodeScan.

## From the CLI

| Flag       | Format                             | Use it for                                          |
| ---------- | ---------------------------------- | --------------------------------------------------- |
| `--json`   | One JSON object on standard output | Scripts and pipeline checks                         |
| `--sarif`  | SARIF 2.1.0                        | Security tools and GitHub code scanning             |
| `--junit`  | JUnit XML, one test suite per file | Showing findings as test failures in a build server |
| `--gitlab` | GitLab Code Quality JSON           | Showing findings inline on a GitLab merge request   |
| `--html`   | Standalone HTML report             | Sharing and audit evidence                          |

Reports are written to `.codescan/reports/`. The file names change on every run, and their paths are printed and included in the JSON output. In CI, publish the folder as a build artifact.

## From VS Code

**`CodeScan: Export Scan Results`** saves the last scan as SARIF 2.1.0.

## How Likely False Positives Appear in Each Format

Findings the AI reviewer flagged are kept in every format, marked so tools don't treat them as active:

| Format              | How a likely false positive appears   |
| ------------------- | ------------------------------------- |
| SARIF               | An "under review" suppression         |
| JUnit               | A skipped test case                   |
| GitLab Code Quality | A `[Likely false positive: …]` prefix |
| HTML                | An AI-FP badge                        |

## Software Bill of Materials

For CycloneDX and SPDX SBOMs, see [Software Bill of Materials (SBOM)](/broken/pages/067fbd0d0869b1f39ab499b6e02f1ed7d442deca).

## Related Articles

* [Dashboards](/broken/pages/ea1542ce14f14c91dd60c58298eb1b6a19dcc2e1)
* [Run CodeScan in CI](/broken/pages/cfe1dcabddc18e59ed92c059096335ba2a32d2e9)
