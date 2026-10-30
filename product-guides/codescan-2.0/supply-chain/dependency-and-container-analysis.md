---
description: >-
  How CodeScan checks third-party packages, supply-chain risks and container
  base images.
---

# Dependency and Container Analysis

Your own source code is only half of what you ship. The other half is code someone else wrote: dependencies and container images. CodeScan checks both in the same scan as your source code, with no separate setup.

### What Is Read

Dependencies are read from `package.json` and its lockfiles, `pom.xml`, Gradle version catalogs, `requirements.txt`, `pyproject.toml`, `Pipfile.lock`, `poetry.lock`, `pdm.lock` and `uv.lock`. For Maven and Gradle, the full tree of indirect dependencies is resolved too.

Helm charts are rendered and scanned with the rest, if `helm` is installed where the scan runs.

### Known Vulnerabilities

Every package is checked against the OSV.dev advisory database. Each finding shows, where available:

| Information                    | What it tells you                                                                                               |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Known Exploited** (CISA KEV) | Attackers are exploiting this vulnerability now. Fix it first.                                                  |
| EPSS                           | The probability that it will be exploited                                                                       |
| Reachability                   | Whether your code actually imports the vulnerable package. Unreachable findings are deprioritised, not deleted. |
| CVSS and CWE                   | Standard severity score and weakness type                                                                       |

### Supply-Chain Risks

Beyond known vulnerabilities, CodeScan looks for signs of an attack on your supply chain:

| Risk                                 | What CodeScan checks                                                                                                                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Malicious packages and typosquatting | Known-bad packages, and names that imitate popular ones. Shown with a red **Malicious Package — Remove, Do Not Upgrade** badge. Remove the package: don't upgrade it in place. |
| Build provenance                     | High-risk npm versions published without provenance, or built below your required SLSA level                                                                                   |
| Lockfile integrity                   | Whether the package in your lockfile still matches what the registry publishes. A mismatch means the package changed after you locked it.                                      |
| Dependency confusion                 | An internal-looking package name that resolves from a public registry                                                                                                          |
| Maintainer changes                   | A release published right after a package changed hands                                                                                                                        |
| Suspicious install scripts           | Install steps that run commands typical of malicious code                                                                                                                      |
| SBOM drift and unpinned versions     | A committed SBOM that disagrees with your manifests, and dependencies on floating version ranges                                                                               |
| Copied libraries                     | Libraries pasted into your repository, matched to a known version                                                                                                              |

### Licences and Project Health

Licences are identified using standard SPDX names and checked against an allow and deny policy. CodeScan also catches restrictive licences pulled in indirectly under a permissive direct dependency, and licence combinations that conflict. <mark style="color:red;">**\[TO CONFIRM: where customers set the licence allow/deny policy]**</mark>

Allowed Licenses: MIT, Apache-2.0, BSD and similar.\
Denied Licenses: GPL, AGPL, SSPL, EUPL\
Recognised licences not in the list are flagged for review.\
Unrecognised licences are denied.

Project health uses the OpenSSF Scorecard of each dependency's source repository, and flags deprecated packages and packages with no recent release that still have open advisories.

### Container Base Images

For every `FROM` line in a Dockerfile, CodeScan downloads the base image and checks its operating-system packages and libraries for known vulnerabilities. A Dockerfile pinned to an old distribution is not reported as clean.

No container is started and nothing from the image is run. The image is read as data only.

### Vendor Statements (VEX)

If a vendor has formally stated that a vulnerability does not affect their product (in OpenVEX or CSAF format), CodeScan reads that statement and suppresses the finding, so you don't dismiss it again on every scan. These findings never count toward the quality gate and cannot be restored.

### Fixing Vulnerable Dependencies

For a vulnerable dependency, CodeScan works out the version upgrade that fixes it, from your dependency tree, and shows the resulting change. This is calculated, not written by AI.

### Related Articles

* Software Bill of Materials (SBOM)
* Understanding a Finding
