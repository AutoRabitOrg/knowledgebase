# Release Notes 26.3.1.0



## Release Notes 26.3.1.0

**Security and Bug Fixes | Public Sector Release**

**Release Date:** July 8, 2026\
**Release Type:** Security and Bug Fix Release (Maintenance)\
**Build Images:** Created and documented on Confluence\
**Previous Base:** Latest Public Sector release build prior to 26.3.1.0

***

### 1. Overview

ARMOR release 26.3.1.0 includes **security fixes** and one important **bug fix** on top of the previous Public Sector release build.

This release addresses **6 vulnerabilities** across multiple services, primarily related to the Bouncy Castle FIPS cryptographic library and Red Hat base packages.

Additionally, plain-text passwords have been removed from emails and replaced with a secure **Update Password** link (ARMOR-2945). This improves security and prevents accidental exposure of credentials.

No other new functional features or major changes have been introduced in this release.

***

### 2. Scope of Changes

#### In Scope

* Security vulnerability remediation
* Bug fix: Removal of plain-text passwords from emails (replaced with Update Password link)

#### Out of Scope

Any new functionality, customer-facing features, architecture changes, performance optimizations, or non-security-related issues are explicitly excluded from this release.

***

### 3. Security Fixes Summary

A total of **6 vulnerabilities** have been addressed in this release. These primarily consist of:

* Java/Maven dependency updates for the Bouncy Castle FIPS library (`org.bouncycastle:bc-fips`)
* Red Hat Enterprise Linux package update (libcap)
* Java/Maven dependency update for Netty (`io.netty:netty-codec-http`)

#### Vulnerability Count by Severity

| Severity  | Count |
| --------- | ----- |
| Sev 3     | 5     |
| Sev 4     | 1     |
| **TOTAL** | **6** |

***

### 4. Detailed Fixes by Component

The following tables list every vulnerability addressed in this release, grouped by the affected ARMOR service. Each entry corresponds to a tracked JIRA issue.

#### arm-keycloak-service

**3 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                  |
| -------- | -------- | -------------------------------------------------------------------------------- |
| SEC-2178 | 3        | Java (Maven) Security Update for org.bouncycastle:bc-fips (GHSA-mx76-r943-rf8g)  |
| SEC-2171 | 4        | Red Hat Update for libcap (RHSA-2026:19346)                                      |
| SEC-1888 | 3        | Java (Maven) Security Update for io.netty:netty-codec-http (GHSA-38f8-5428-x5cv) |

#### arm-worker

**1 vulnerability addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                 |
| -------- | -------- | ------------------------------------------------------------------------------- |
| SEC-2165 | 3        | Java (Maven) Security Update for org.bouncycastle:bc-fips (GHSA-mx76-r943-rf8g) |

#### arm-version-control

**1 vulnerability addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                 |
| -------- | -------- | ------------------------------------------------------------------------------- |
| SEC-2149 | 3        | Java (Maven) Security Update for org.bouncycastle:bc-fips (GHSA-mx76-r943-rf8g) |

#### arm-api

**1 vulnerability addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                 |
| -------- | -------- | ------------------------------------------------------------------------------- |
| SEC-2102 | 3        | Java (Maven) Security Update for org.bouncycastle:bc-fips (GHSA-mx76-r943-rf8g) |

***

[**Note on Implementation:** These updates were delivered by updating the relevant container base images and rebuilding the affected service images with patched dependency versions. No source code changes were made to ARMOR business logic or customer-facing functionality. The bug fix for email password handling was implemented as part of this release.](#user-content-fn-1)[^1]

[^1]: 
