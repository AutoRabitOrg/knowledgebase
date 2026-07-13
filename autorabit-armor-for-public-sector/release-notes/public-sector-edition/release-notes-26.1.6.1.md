# Release Notes 26.1.6.1

**Security Vulnerability Fixes | Public Sector Release**

**No Functional Changes**

**Release Date:** June 26, 2026\
**Release Type:** Security Patch Release (Maintenance)\
**Build Images:** Created and documented on Confluence\
**Previous Base:** Latest Public Sector release build prior to 26.1.6.1

***

### 1. Overview

ARMOR release 26.1.6.1 is a **security-only patch release** focused exclusively on addressing identified vulnerabilities in the Public Sector environment.

No new features, functional enhancements, UI changes, or non-security bug fixes have been included.

This release applies targeted updates to underlying Red Hat Enterprise Linux packages within container images and specific Java/Node.js dependencies across four core platform services. The goal is to maintain a strong security posture and support ongoing compliance requirements for Public Sector customers.

***

### 2. Scope of Changes

#### In Scope

Security vulnerability remediation only:

* `arm-build-deploy` service
* `arm-version-control` service
* `arm-worker` service
* `arm-keycloak-service`

#### Out of Scope

Any new functionality, customer-facing features, architecture changes, performance optimizations, or non-security-related issues are explicitly excluded from this release.

***

### 3. Security Fixes Summary

A total of **36 individual vulnerability fixes** have been applied. These primarily consist of:

* Red Hat Enterprise Linux package updates (libpng, glib2, OpenSSL, glibc, p11-kit, krb5, libcap, systemd, python3.9) delivered via official RHSA advisories
* Java/Maven dependency updates (OpenTelemetry API and multiple Tomcat Embedded Core security advisories)
* Node.js/npm package update (`ws` websocket library)

#### Vulnerability Count by Severity

| Severity     | Count  |
| ------------ | ------ |
| Sev 2 (High) | 1      |
| Sev 3        | 23     |
| Sev 4        | 9      |
| Sev 5 (Low)  | 3      |
| **TOTAL**    | **36** |

***

### 4. Detailed Fixes by Component

The following tables list every vulnerability addressed in this release, grouped by the affected ARMOR service. Each entry corresponds to a tracked JIRA issue under the `PubSec-Vulns` label set.

#### arm-build-deploy

**1 vulnerability addressed** – OpenTelemetry Java client library update.

| JIRA ID  | Severity | Vulnerability / Package Updated                                                           |
| -------- | -------- | ----------------------------------------------------------------------------------------- |
| SEC-2132 | 3        | Java (Maven) Security Update for io.opentelemetry:opentelemetry-api (GHSA-rcgg-9c38-7xpx) |

#### arm-version-control

**11 vulnerabilities addressed** – Mix of Red Hat OS package updates and one Node.js `ws` library fix.

| JIRA ID  | Severity | Vulnerability / Package Updated                                          |
| -------- | -------- | ------------------------------------------------------------------------ |
| SEC-2133 | 3        | Red Hat Update for libpng (RHSA-2026:18028)                              |
| SEC-2134 | 4        | Red Hat Update for libcap (RHSA-2026:19346)                              |
| SEC-2135 | 3        | Red Hat Update for glib2 (RHSA-2026:19361)                               |
| SEC-2136 | 4        | Red Hat Update for krb5 (RHSA-2026:19357)                                |
| SEC-2141 | 3        | Red Hat Update for python3.9 (RHSA-2026:18693)                           |
| SEC-2142 | 3        | NodeJs (Npm) Security Update for ws (GHSA-58qx-3vcg-4xpx)                |
| SEC-2143 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:22312) |
| SEC-2145 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:19218) |
| SEC-2146 | 3        | Red Hat Update for systemd (RHSA-2026:19213)                             |
| SEC-2147 | 3        | Red Hat Update for glibc (RHSA-2026:20597)                               |
| SEC-2148 | 3        | Red Hat Update for p11-kit (RHSA-2026:18599)                             |

#### arm-worker

**15 vulnerabilities addressed** – Includes the single Sev 2 Tomcat Embedded Core issue plus multiple Red Hat package and additional Tomcat GHSAs.

| JIRA ID  | Severity | Vulnerability / Package Updated                                                                  |
| -------- | -------- | ------------------------------------------------------------------------------------------------ |
| SEC-2150 | 3        | Red Hat Update for libpng (RHSA-2026:18028)                                                      |
| SEC-2151 | 4        | Red Hat Update for libcap (RHSA-2026:19346)                                                      |
| SEC-2152 | 2        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-9m89-8frq-c98c) |
| SEC-2153 | 3        | Red Hat Update for glib2 (RHSA-2026:19361)                                                       |
| SEC-2156 | 5        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-5m62-pw8w-7w9f) |
| SEC-2158 | 3        | Red Hat Update for p11-kit (RHSA-2026:18599)                                                     |
| SEC-2159 | 4        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-fv25-8xcx-gqjc) |
| SEC-2160 | 5        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-r29c-68gh-xp6x) |
| SEC-2162 | 5        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-h6fc-48rj-7qqh) |
| SEC-2163 | 4        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-gx5v-xp9w-j4cg) |
| SEC-2164 | 4        | Java (Maven) Security Update for org.apache.tomcat.embed:tomcat-embed-core (GHSA-5mp6-jrq3-r938) |
| SEC-2166 | 3        | Red Hat Update for python3.9 (RHSA-2026:18693)                                                   |
| SEC-2167 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:22312)                         |
| SEC-2168 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:19218)                         |
| SEC-2169 | 3        | Red Hat Update for systemd (RHSA-2026:19213)                                                     |

#### arm-keycloak-service

**9 vulnerabilities addressed** – Red Hat OS package updates (including a python3.9 update specific to this service).

| JIRA ID  | Severity | Vulnerability / Package Updated                                          |
| -------- | -------- | ------------------------------------------------------------------------ |
| SEC-2170 | 3        | Red Hat Update for libpng (RHSA-2026:18028)                              |
| SEC-2171 | 4        | Red Hat Update for libcap (RHSA-2026:19346)                              |
| SEC-2173 | 4        | Red Hat Update for krb5 (RHSA-2026:19357)                                |
| SEC-2175 | 4        | Red Hat Update for python3.9 (RHSA-2026:19216)                           |
| SEC-2176 | 3        | Red Hat Update for p11-kit (RHSA-2026:18599)                             |
| SEC-2180 | 3        | Red Hat Update for python3.9 (RHSA-2026:18693)                           |
| SEC-2181 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:22312) |
| SEC-2182 | 3        | Red Hat Update for Open Secure Sockets Layer (OpenSSL) (RHSA-2026:19218) |
| SEC-2183 | 3        | Red Hat Update for systemd (RHSA-2026:19213)                             |

> **Note on Implementation:** These security updates were delivered by updating the relevant container base images and rebuilding the affected service images with patched dependency versions. No source code changes were made to ARMOR business logic or customer-facing functionality.
