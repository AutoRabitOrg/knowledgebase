---
description: >-
  Choose how to run IZ Suite on your own infrastructure, from a single-VM proof
  of concept to a resilient production deployment
---

# Installation

IZ Suite runs as a set of containers next to a PostgreSQL database. You can run it on a single virtual machine for a proof of concept, or spread it across managed services for production. Both use the same container images.

## Components

| Component    | Image                                       | What it does                                                                                            |
| ------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Server**   | `iz-suite-server` with `FALCON_MODE=api`    | The web interface and the API. Applies database updates when it starts.                                 |
| **Worker**   | `iz-suite-server` with `FALCON_MODE=worker` | Background processing: assessment lifecycles, risk matching, reports, notifications and scheduled work. |
| **Agent**    | `iz-suite-agent`                            | Runs scans and connector jobs against your platforms and repositories, and Service Health checks.       |
| **Database** | PostgreSQL 16                               | Holds all IZ Suite data.                                                                                |

The images are published at `public.ecr.aws/h0h7r7j4/iz-suite-server` and `public.ecr.aws/h0h7r7j4/iz-suite-agent`, tagged with the release.

## Choose a Path

| Path                              | Use it for                                                                                                                  | Page                                                              |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Single VM with Docker Compose** | Proofs of concept, trials and small teams. Everything, including PostgreSQL, runs on one VM.                                | [Proof of Concept Installation](proof-of-concept-installation.md) |
| **Managed services**              | Production: two or more servers behind a load balancer, a managed PostgreSQL database with backups, and workers that scale. | [Production Deployment](production-deployment.md)                 |

Whichever you choose, size it from the number of assets you plan to assess; see [Requirements & Sizing](requirements-and-sizing.md).

## Next Steps

* [Requirements & Sizing](requirements-and-sizing.md): work out the machines and database you need.
* [Proof of Concept Installation](proof-of-concept-installation.md): run IZ Suite on one VM.
* [Production Deployment](production-deployment.md): the recommended production setup.
* [First Start](first-start.md): apply the licence and sign in.
