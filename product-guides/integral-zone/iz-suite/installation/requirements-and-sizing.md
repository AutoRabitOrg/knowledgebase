---
description: >-
  Check the software and network requirements, and size IZ Suite from the number
  of assets you plan to assess.
---

# Requirements & Sizing

IZ Suite's size depends on how much you assess: how many applications and repositories, how often, and how many monitors run. AutoRABIT works out the sizing for your installation with you, from the inputs below.

## Software

| Item                         | Requirement                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Container runtime            | Docker Engine with the Docker Compose v2 plugin (single VM), or a container service such as Amazon ECS.         |
| CPU architecture             | x86-64 (Intel or AMD). The images are not built for Arm.                                                        |
| Operating system (single VM) | Ubuntu 24.04 LTS or Debian 12.                                                                                  |
| Database                     | PostgreSQL 16. The proof-of-concept setup runs it as a container; production uses a managed PostgreSQL service. |

## Inputs for Sizing

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

## Sizing

AutoRABIT sizes the virtual machine, the server, worker and agent tasks and the database for your installation from these inputs, for example the number of applications and repositories you assess.

{% hint style="info" %}
Add agents rather than making one agent larger when you have many platforms, a high monitor count or platforms in separate networks. Each agent works on its own; agents need no load balancer.
{% endhint %}

## Network

| Direction | Port    | Purpose                                                                                                                                                                                                                                                                                                                     |
| --------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound   | TCP 443 | Users and pipelines reach IZ Suite over HTTPS, through a load balancer or reverse proxy that holds your TLS certificate.                                                                                                                                                                                                    |
| Inbound   | TCP 22  | Administration of a single VM, from administrator addresses only.                                                                                                                                                                                                                                                           |
| Outbound  | TCP 443 | `public.ecr.aws` to download the images, `artifacts.integralzone.com` for content and agent updates, `license.integralzone.com` for the licence service, and the platforms and repositories IZ Suite assesses (for example MuleSoft Anypoint, AWS, Azure, GitHub or Bitbucket), and your AI provider if you use AI reviews. |

Keep PostgreSQL (TCP 5432) reachable only from the server and worker. Agents need no database access. They need HTTPS to IZ Suite, to `artifacts.integralzone.com` and to the platforms they assess, so they can run in other networks.

Choose one hostname for IZ Suite, for example `izsuite.yourcompany.com`, and a TLS certificate for it.

## Next Steps

* [Proof of Concept Installation](proof-of-concept-installation.md): run IZ Suite on one VM.
* [Production Deployment](production-deployment.md): the recommended production setup.
