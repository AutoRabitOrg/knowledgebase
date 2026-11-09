---
description: >-
  Choose how to run IZ Suite on your own infrastructure, from a single-VM proof
  of concept to a resilient production deployment
---

# Installation

IZ Suite runs as a set of containers next to a PostgreSQL database. You can run it on a single virtual machine for a proof of concept, or spread it across managed services for production. Both use the same container images and the same configuration.

{% hint style="info" %}
**HINT (info):** IZ Suite is also available as a service managed by AutoRABIT. When AutoRABIT hosts your workspace, you can skip this section and start with [Sign In](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/getting-started/sign-in).
{% endhint %}

### Components

| Component    | Image                                       | What it does                                                                                            |
| ------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Server**   | `iz-suite-server` with `FALCON_MODE=all`    | The web interface and the API. Applies database updates when it starts.                                 |
| **Worker**   | `iz-suite-server` with `FALCON_MODE=worker` | Background processing: assessment lifecycles, risk matching, reports, notifications and scheduled work. |
| **Agent**    | `iz-suite-agent`                            | Runs scans and connector jobs against your platforms and repositories, and Service Health checks.       |
| **Database** | PostgreSQL 16                               | Holds all IZ Suite data.                                                                                |

The images are published at `public.ecr.aws/h0h7r7j4/iz-suite-server` and `public.ecr.aws/h0h7r7j4/iz-suite-agent`, tagged with the release, for example `26.4.2`.

### Choose a Path

| Path                              | Use it for                                                                                                                  | Page                                                                                                                                                  |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single VM with Docker Compose** | Proofs of concept, trials and small teams. Everything, including PostgreSQL, runs on one VM.                                | [Proof of Concept Installation](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/proof-of-concept-installation) |
| **Managed services**              | Production: two or more servers behind a load balancer, a managed PostgreSQL database with backups, and workers that scale. | [Production Deployment](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/production-deployment)                 |

Whichever you choose, size it from the number of assets you plan to assess; see [Requirements & Sizing](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/requirements-and-sizing).

### Next steps

* [Requirements & Sizing](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/requirements-and-sizing): work out the machines and database you need.
* [Proof of Concept Installation](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/proof-of-concept-installation): run IZ Suite on one VM.
* [Production Deployment](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/production-deployment): the recommended production setup.
* [First Start](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/first-start): apply the licence and sign in.
