---
description: >-
  Check the software and network requirements, and size IZ Suite from the number
  of assets you plan to assess.
---

# Requirements & Sizing

IZ Suite's size depends on how much you assess: how many applications and repositories, how often, and how many monitors run. AutoRABIT confirms the sizing for your installation from the inputs below. The figures on this page are starting points.

### Software

| Item                         | Requirement                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Container runtime            | Docker Engine 24 or later with the Docker Compose v2 plugin (single VM), or a container service such as Amazon ECS, Azure Container Apps or Kubernetes. |
| CPU architecture             | x86-64 (Intel or AMD). The images are not built for Arm.                                                                                                |
| Operating system (single VM) | Ubuntu 24.04 LTS or Debian 12.                                                                                                                          |
| Database                     | PostgreSQL 16. The proof-of-concept setup runs it as a container; production uses a managed PostgreSQL service.                                         |

### Inputs for Sizing

Send these to AutoRABIT with your installation request:

| Input                                                                         | Why it matters                                                            |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Number of deployed applications to assess (by platform: MuleSoft, AWS, Azure) | Platform assessments run on the agent; their evidence fills the database. |
| Number of repositories and active branches, and pull requests per day         | Code assessments and pull request scans drive agent and worker load.      |
| How often assessments run (for example nightly, or on every change)           | Sets the peak number of jobs running at once.                             |
| Number of Service Health monitors and their check interval                    | Monitors run continuously on the agent.                                   |
| Number of users working at the same time                                      | Sets the number of server tasks.                                          |
| Whether AI reviews and source storage are used                                | AI reviews add agent work; stored source adds database or storage space.  |
| How long evidence must be kept                                                | Sets database storage and backup size.                                    |

### Starting Points

| Size         | Typical estate                                                                                  | Single VM                      | Production (per task)                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Trial**    | A few dozen applications or repositories, light scanning                                        | 4 vCPU, 16 GB RAM, 100 GB disk | —                                                                                                                 |
| **Standard** | Up to a few hundred applications or repositories, nightly assessments                           | 8 vCPU, 32 GB RAM, 150 GB disk | Server 2 × (2 vCPU, 4 GB); worker 1–4 × (2 vCPU, 4 GB); agent 1 × (2 vCPU, 4 GB); PostgreSQL with 2 vCPU and 8 GB |
| **Large**    | Many hundreds of applications or repositories, frequent or pull-request scanning, many monitors | Not recommended                | As Standard with more agents and workers, and a larger PostgreSQL instance, sized by AutoRABIT from your inputs   |

On a single VM the four components need about 8 vCPU and 20 GB together; the rest of a 32 GB machine is left for the operating system and growth.

> **HINT (info):** Add agents rather than making one agent larger when you have many platforms, a high monitor count or platforms in separate networks. Each agent works on its own; agents need no load balancer.

### Network

| Direction | Port    | Purpose                                                                                                                                                                                                     |
| --------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound   | TCP 443 | Users and pipelines reach IZ Suite over HTTPS, through a load balancer or reverse proxy that holds your TLS certificate.                                                                                    |
| Inbound   | TCP 80  | Optional; only to redirect to HTTPS.                                                                                                                                                                        |
| Inbound   | TCP 22  | Administration of a single VM, from administrator addresses only.                                                                                                                                           |
| Outbound  | TCP 443 | `public.ecr.aws` to download the images, and the platforms and repositories IZ Suite assesses (for example MuleSoft Anypoint, AWS, Azure, GitHub or Bitbucket), and your AI provider if you use AI reviews. |

Keep PostgreSQL (TCP 5432) reachable only from the server and worker. Agents talk to the server only, so they can run in other networks as long as they reach IZ Suite over HTTPS.

Choose one hostname for IZ Suite, for example `izsuite.yourcompany.com`, and a TLS certificate for it.

### Next steps

* [Proof of Concept Installation](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/proof-of-concept-installation): run IZ Suite on one VM.
* [Production Deployment](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/installation/production-deployment): the recommended production setup.
