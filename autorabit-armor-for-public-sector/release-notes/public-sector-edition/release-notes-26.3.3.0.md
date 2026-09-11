# Release Notes 26.3.3.0

### Overview

ARMOR release 26.3.3.0 is a **security-only patch release** focused exclusively on addressing identified vulnerabilities in the Public Sector environment.

No new features, functional enhancements, UI changes, or non-security bug fixes have been included.

This release applies targeted updates to Java/Maven and Node.js dependencies across core platform services. The goal is to maintain a strong security posture and support ongoing compliance requirements for Public Sector customers.

***

### Scope of Changes

#### In Scope

Security vulnerability remediation only:

* `arm-keycloak-service` (armor-authentication)
* `arm-version-control`
* `arm-build-deploy`
* `arm-api`

#### Out of Scope

Any new functionality, customer-facing features, architecture changes, performance optimizations, or non-security-related issues are explicitly excluded from this release.

***

### Security Fixes Summary

A total of **34 vulnerabilities** have been addressed in this release. These primarily consist of:

* Java/Maven dependency updates (Jackson Databind, Netty HTTP codec, PostgreSQL driver) in Keycloak
* Node.js/npm package updates (`tar`, `undici`, `brace-expansion`) across API, version-control, and build-deploy services

#### Vulnerability Count by Severity

| Severity  | Count  |
| --------- | ------ |
| Sev 2     | 4      |
| Sev 3     | 13     |
| Sev 4     | 14     |
| Sev 5     | 3      |
| **TOTAL** | **34** |

***

### Detailed Fixes by Component

The following tables list every vulnerability addressed in this release, grouped by the affected ARMOR service.

#### arm-keycloak-service (armor-authentication)

**10 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-2584 | 4        | Java (Maven) Security Update for io.netty:netty-codec-http (GHSA-mvh2-crg5-v77c)                   |
| SEC-2580 | 4        | Java (Maven) Security Update for io.netty:netty-codec-http (GHSA-6jqx-86gh-f27w)                   |
| SEC-2579 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-5gvw-p9qm-jgwh) |
| SEC-2578 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-3pjw-73gf-8qr5) |
| SEC-2577 | 4        | Java (Maven) Security Update for org.postgresql:postgresql (GHSA-j92g-9f8w-j867)                   |
| SEC-2573 | 4        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-rmj7-2vxq-3g9f) |
| SEC-2572 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-rcqc-6cw3-h962) |
| SEC-2571 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-5jmj-h7xm-6q6v) |
| SEC-2570 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-5hh8-q8hv-fr38) |
| SEC-2569 | 4        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-j3rv-43j4-c7qm) |

#### arm-version-control

**8 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                        |
| -------- | -------- | ---------------------------------------------------------------------- |
| SEC-2535 | 5        | NodeJs (Npm) Security Update for tar (GHSA-23hp-3jrh-7fpw)             |
| SEC-2533 | 3        | NodeJs (Npm) Security Update for tar (GHSA-gvwx-54wh-qm9j)             |
| SEC-2531 | 4        | NodeJs (Npm) Security Update for brace-expansion (GHSA-3jxr-9vmj-r5cp) |
| SEC-2529 | 4        | NodeJs (Npm) Security Update for tar (GHSA-8x88-c5mf-7j5w)             |
| SEC-2528 | 3        | NodeJs (Npm) Security Update for tar (GHSA-w8wr-v893-vjvp)             |
| SEC-2518 | 4        | NodeJs (Npm) Security Update for undici (GHSA-vxpw-j846-p89q)          |
| SEC-2517 | 2        | NodeJs (Npm) Security Update for undici (GHSA-35p6-xmwp-9g52)          |
| SEC-2242 | 3        | NodeJs (Npm) Security Update for undici (GHSA-p88m-4jfj-68fv)          |

#### arm-build-deploy

**7 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                        |
| -------- | -------- | ---------------------------------------------------------------------- |
| SEC-2505 | 5        | NodeJs (Npm) Security Update for tar (GHSA-23hp-3jrh-7fpw)             |
| SEC-2503 | 3        | NodeJs (Npm) Security Update for tar (GHSA-gvwx-54wh-qm9j)             |
| SEC-2501 | 4        | NodeJs (Npm) Security Update for brace-expansion (GHSA-3jxr-9vmj-r5cp) |
| SEC-2499 | 4        | NodeJs (Npm) Security Update for tar (GHSA-8x88-c5mf-7j5w)             |
| SEC-2498 | 3        | NodeJs (Npm) Security Update for tar (GHSA-w8wr-v893-vjvp)             |
| SEC-2490 | 4        | NodeJs (Npm) Security Update for undici (GHSA-vxpw-j846-p89q)          |
| SEC-2489 | 2        | NodeJs (Npm) Security Update for undici (GHSA-35p6-xmwp-9g52)          |

#### arm-api

**9 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                        |
| -------- | -------- | ---------------------------------------------------------------------- |
| SEC-2467 | 5        | NodeJs (Npm) Security Update for tar (GHSA-23hp-3jrh-7fpw)             |
| SEC-2465 | 3        | NodeJs (Npm) Security Update for tar (GHSA-gvwx-54wh-qm9j)             |
| SEC-2463 | 4        | NodeJs (Npm) Security Update for brace-expansion (GHSA-3jxr-9vmj-r5cp) |
| SEC-2461 | 4        | NodeJs (Npm) Security Update for tar (GHSA-8x88-c5mf-7j5w)             |
| SEC-2460 | 3        | NodeJs (Npm) Security Update for tar (GHSA-w8wr-v893-vjvp)             |
| SEC-2444 | 4        | NodeJs (Npm) Security Update for undici (GHSA-vxpw-j846-p89q)          |
| SEC-2442 | 2        | NodeJs (Npm) Security Update for undici (GHSA-35p6-xmwp-9g52)          |
| SEC-2441 | 2        | NodeJs (Npm) Security Update for undici (GHSA-g8m3-5g58-fq7m)          |
| SEC-2212 | 3        | NodeJs (Npm) Security Update for undici (GHSA-p88m-4jfj-68fv)          |

***

**Note on Implementation:** These security updates were delivered by updating the relevant container base images and rebuilding the affected service images with patched dependency versions. No source code changes were made to ARMOR business logic or customer-facing functionality.
