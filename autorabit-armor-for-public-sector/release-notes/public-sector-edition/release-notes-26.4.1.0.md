# Release Notes 26.4.1.0

### Overview

ARMOR release 26.4.1.0 is a **security-only patch release** focused exclusively on addressing identified vulnerabilities in the Public Sector environment.

No new features, functional enhancements, UI changes, or non-security bug fixes have been included.

This release applies targeted updates to Java/Maven dependencies and Red Hat Enterprise Linux packages across core platform services. The goal is to maintain a strong security posture and support ongoing compliance requirements for Public Sector customers.

### Scope of Changes

#### In Scope

Security vulnerability remediation only:

* `arm-worker`
* `arm-version-control`
* `keycloak-service` (armor-authentication)
* `arm-api`
* `arm-build-deploy`
* `arm-scheduler-service`

#### Out of Scope

Any new functionality, customer-facing features, architecture changes, performance optimizations, or non-security-related issues are explicitly excluded from this release.

### Security Fixes Summary

The release filter contains **99** tracked vulnerability items. The extract used for these notes contains **26** items. Those 26 primarily consist of:

* Java/Maven dependency updates (Jackson Databind, Netty HTTP codec, FreeMarker)
* Red Hat Enterprise Linux package updates (libxml2, unbound)

#### Vulnerability Count by Severity

Counts below are for the 26 items in the extract.

| Severity  | Count  |
| --------- | ------ |
| Sev 3     | 9      |
| Sev 4     | 7      |
| Sev 5     | 10     |
| **TOTAL** | **26** |

### Detailed Fixes by Component

The following tables list the vulnerabilities included in the extract, grouped by the affected ARMOR service.

**arm-worker**

**7 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3593 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-gx83-3vf8-gh7j) |
| SEC-3594 | 4        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-q4xh-88c3-wmh7) |
| SEC-3596 | 3        | Java (Maven) Security Update for io.netty:netty-codec-http (GHSA-hcvj-94mj-jp5c)                   |
| SEC-3597 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-wjgm-6hv5-3cvf) |
| SEC-3650 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3651 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |
| SEC-3652 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |

**arm-version-control**

**4 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3605 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3606 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |
| SEC-3607 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |
| SEC-3608 | 5        | Java (Maven) Security Update for org.freemarker:freemarker (GHSA-27j2-h3m2-8237)                   |

**keycloak-service (armor-authentication)**

**4 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3640 | 5        | Java (Maven) Security Update for org.freemarker:freemarker (GHSA-27j2-h3m2-8237)                   |
| SEC-3641 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |
| SEC-3657 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3658 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |

**arm-api**

**4 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3642 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3643 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |
| SEC-3644 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |
| SEC-3645 | 5        | Java (Maven) Security Update for org.freemarker:freemarker (GHSA-27j2-h3m2-8237)                   |

**arm-build-deploy**

**4 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3646 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3647 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |
| SEC-3648 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |
| SEC-3649 | 5        | Java (Maven) Security Update for org.freemarker:freemarker (GHSA-27j2-h3m2-8237)                   |

**arm-scheduler-service**

**3 vulnerabilities addressed**

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                    |
| -------- | -------- | -------------------------------------------------------------------------------------------------- |
| SEC-3659 | 4        | Red Hat Update for libxml2 (RHSA-2026:71585)                                                       |
| SEC-3660 | 5        | Red Hat Update for unbound (RHSA-2026:71487)                                                       |
| SEC-3661 | 3        | Java (Maven) Security Update for com.fasterxml.jackson.core:jackson-databind (GHSA-vvgp-rfg2-7rr6) |

**Note on Implementation:** These security updates were delivered by updating the relevant container base images and rebuilding the affected service images with patched dependency versions. No source code changes were made to ARMOR business logic or customer-facing functionality.
