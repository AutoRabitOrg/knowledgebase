# Release Notes 26.3.2.0

**Security and Bug Fixes | Public Sector Release**

**Release Date:** August 12, 2026\
**Release Type:** Security and Bug Fix Release (Maintenance)\
**Build Images:** Created and documented on Confluence\
**Previous Base:** Latest Public Sector release build prior to 26.3.2.0

***

### 1. Overview

ARMOR release 26.3.2.0 includes **security fixes** and one important **configuration change** on top of the previous Public Sector release build.

This release addresses multiple vulnerabilities across core services (primarily related to Jackson, Netty, OpenSSL, minimatch, and other dependencies).

**Important change in this release:**\
Pendo and FullStory have been **disabled**.

Apart from the above, no new functional features or major changes have been introduced in this release.

***

### 2. Scope of Changes

#### In Scope

* Security vulnerability remediation
* Disabling of Pendo and FullStory

#### Out of Scope

Any new functionality, customer-facing features, architecture changes, performance optimizations, or other non-security-related issues are explicitly excluded from this release.

***

### 3. Security Fixes Summary

A total of **26 vulnerabilities** have been addressed in this release. These primarily consist of:

* Java/Maven dependency updates (Jackson Databind, Netty components, Keycloak services)
* Red Hat Enterprise Linux package updates (OpenSSL, OpenSSL-fips-provider, unbound, expat, libtasn1)
* Node.js/npm package updates (minimatch, picomatch, protobufjs, @sigstore/core)

#### Vulnerability Count by Severity

| Severity  | Count  |
| --------- | ------ |
| Sev 2     | 1      |
| Sev 3     | 6      |
| Sev 4     | 19     |
| **TOTAL** | **26** |

***

### 4. Detailed Fixes by Component

The following tables list every vulnerability addressed in this release, grouped by the affected ARMOR service.

#### arm-api

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-2220 | 4        | Java (Maven) Security Update for io.netty:netty-resolver-dns (GHSA-676x-f7gg-47vc)                 |
| SEC-2219 | 4        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:25239)                           |
| SEC-2214 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-5hh8-q8hv-fr38) |
| SEC-2213 | 4        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-j3rv-43j4-c7qm) |
| SEC-2211 | 3        | NodeJs (Npm) Security Update for @sigstore/core (GHSA-jfc7-64v2-mr8c)                              |
| SEC-1429 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-3ppc-4f35-3m26)                                   |
| SEC-1427 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-23c5-xmqv-rm74)                                   |
| SEC-1402 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-7r86-cg39-jmmj)                                   |
| SEC-1327 | 4        | NodeJs (Npm) Security Update for picomatch (GHSA-c2c7-rcm5-vvqj)                                   |

#### arm-keycloak-service (armor-authentication)

| JIRA ID  | Severity | Vulnerability / Package Updated                                                        |
| -------- | -------- | -------------------------------------------------------------------------------------- |
| SEC-2222 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL)-fips-provider (RHSA-2026:27744) |
| SEC-2221 | 3        | Java (Maven) Security Update for org.keycloak:keycloak-services (GHSA-g8vr-x4qh-25qg)  |
| SEC-2218 | 4        | Java (Maven) Security Update for io.netty:netty-codec-haproxy (GHSA-cc37-9q2j-3hfv)    |
| SEC-2217 | 4        | Red Hat Update for expat (RHSA-2026:23230)                                             |

#### arm-scheduler-service

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-2224 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-9fxm-vc8v-hj55) |
| SEC-2223 | 4        | Red Hat Update for unbound (RHSA-2026:24369)                                                       |

#### arm-version-control

| JIRA ID  | Severity | Vulnerability / Package Updated                                                  |
| -------- | -------- | -------------------------------------------------------------------------------- |
| SEC-2216 | 3        | Java (Maven) Security Update for io.netty:netty-codec-http (GHSA-hvcg-qmg6-jm4c) |
| SEC-1967 | 4        | NodeJs (Npm) Security Update for protobufjs (GHSA-685m-2w69-288q)                |
| SEC-1511 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-3ppc-4f35-3m26)                 |
| SEC-1481 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-23c5-xmqv-rm74)                 |
| SEC-1432 | 4        | NodeJs (Npm) Security Update for picomatch (GHSA-c2c7-rcm5-vvqj)                 |
| SEC-1330 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-7r86-cg39-jmmj)                 |

#### arm-build-deploy

| JIRA ID  | Severity | Vulnerability / Package Updated                                  |
| -------- | -------- | ---------------------------------------------------------------- |
| SEC-2215 | 2        | Red Hat Update for libtasn1 (RHSA-2026:28253)                    |
| SEC-1381 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-3ppc-4f35-3m26) |
| SEC-1380 | 4        | NodeJs (Npm) Security Update for picomatch (GHSA-c2c7-rcm5-vvqj) |
| SEC-1368 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-23c5-xmqv-rm74) |
| SEC-1275 | 4        | NodeJs (Npm) Security Update for minimatch (GHSA-7r86-cg39-jmmj) |

***

**Note on Implementation:** These security updates were delivered by updating the relevant container base images and rebuilding the affected service images with patched dependency versions. No source code changes were made to ARMOR business logic or customer-facing functionality.

Pendo and FullStory have been disabled as part of this release.
