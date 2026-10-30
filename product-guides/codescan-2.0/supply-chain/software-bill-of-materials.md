---
description: >-
  Produce a CycloneDX or SPDX software bill of materials, and send it to
  Dependency-Track.
---

# Software Bill of Materials

A software bill of materials (SBOM) lists every third-party component in your software. Customers, auditors and regulators increasingly ask for one. CodeScan produces SBOMs in the two standard formats.

### Creating an SBOM From the CLI

| Format                  | Command                                              |
| ----------------------- | ---------------------------------------------------- |
| CycloneDX 1.6 (default) | `codescan sbom --output bom.json`                    |
| SPDX 2.3                | `codescan sbom --output bom.spdx.json --format spdx` |

The SBOM is produced by a scan on CodeScan, so CodeScan must be reachable. If the folder has no git remote, pass `--repo-url` so the scan uses your connected repository's settings.

A result of zero components is valid when the repository has no dependency manifests.

### Sending It to Dependency-Track

```bash
codescan sbom --output bom.json \
  --dtrack-url https://dtrack.example.com \
  --dtrack-api-key "$DT_API_KEY" \
  --dtrack-project my-app \
  --dtrack-version 1.0.0
```

All four `--dtrack-*` options are required together, and Dependency-Track upload works with CycloneDX only.

### Related Articles

* Dependency, Supply-Chain and Container Analysis
* CLI Reference
