# Overview

### IZ Suite for AWS <a href="#iz-suite-for-aws" id="iz-suite-for-aws"></a>

IZ Suite for AWS brings the inventory, configuration scanning and governance used for MuleSoft, Azure and Salesforce to Amazon Web Services. An AWS account is onboarded as an organisation, each governed region becomes an environment, and every discovered resource is evaluated against a built-in rule pack for its service.

#### AWS Governance Challenges <a href="#aws-governance-challenges" id="aws-governance-challenges"></a>

AWS makes it easy to create resources, but teams often face key challenges:

* Limited visibility into what is deployed across accounts and regions.
* Configuration drift and insecure defaults (public endpoints, missing encryption, over-permissive IAM roles, unrotated secrets).
* Runtimes and database engines that reach end of support without anyone noticing.
* Stacks left in failed states that still hold live, billed resources.

#### Solution: Visibility and Governance <a href="#solution-visibility-and-governance" id="solution-visibility-and-governance"></a>

IZ Suite discovers the resources of 16 AWS services on a schedule, scans each resource's definition against its service rule pack, and reports the findings in the same issue views, quality gates and reports used for every other application type.

#### Supported Services <a href="#supported-services" id="supported-services"></a>

| Service         | IZ Eye menu               | Built-in rules |
| --------------- | ------------------------- | -------------- |
| Lambda          | **`AWS Lambda`**          | 61             |
| CloudFormation  | **`AWS CloudFormation`**  | 69             |
| Step Functions  | **`AWS Step Functions`**  | 51             |
| API Gateway     | **`AWS API Gateway`**     | 51             |
| ECS             | **`AWS ECS`**             | 57             |
| RDS / Aurora    | **`AWS RDS`**             | 51             |
| Load Balancer   | **`AWS Load Balancer`**   | 50             |
| Secrets Manager | **`AWS Secrets Manager`** | 50             |
| CloudFront      | **`AWS CloudFront`**      | 49             |
| DynamoDB        | **`AWS DynamoDB`**        | 36             |
| SQS             | **`AWS SQS`**             | 34             |
| SNS             | **`AWS SNS`**             | 34             |
| EventBridge     | **`AWS EventBridge`**     | 43             |
| CodePipeline    | **`AWS CodePipeline`**    | 37             |
| CodeBuild       | **`AWS CodeBuild`**       | 50             |
| CodeDeploy      | **`AWS CodeDeploy`**      | 42             |



#### Key Benefits <a href="#key-benefits" id="key-benefits"></a>

* **`Clear Visibility`** - One inventory of the governed resources of every onboarded account and region.
* **`Stronger Governance`** - Consistent rules and quality gates across AWS and the rest of the integration estate.
* **`Reduced Risk`** - Insecure configuration, failed stacks and end-of-support runtimes surface before they cause an incident.
* **`Read-only by design`** - IZ Suite reads resource metadata only. It never changes a resource and never reads secret values.

#### Core Capabilities <a href="#core-capabilities" id="core-capabilities"></a>

* **`Automated Discovery & Inventory`** - Recurring sync jobs discover the resources of each service, with per-service pattern matchers to exclude noisy resources.
* **`Configuration Scanning`** - Each resource's definition is scanned against its service rule pack. Lambda rules carry auto-fix suggestions.
* **`Code Scanning`** - Lambda functions on Python runtimes have their deployment package scanned with the Python rules as part of the same scan.
* **`Infrastructure as Code`** - CloudFormation and SAM templates are scanned both as deployed stacks (IZ Eye) and from source before deployment (IZ Scan and the IZ Scan CLI).
* **`Relationships`** - Lambda functions, queues, topics, event buses, state machines, secrets and databases are linked, so IZ Lens can show what depends on what.

#### Licensing and Permissions <a href="#licensing-and-permissions" id="licensing-and-permissions"></a>

* Each AWS service is a separate licence module. A service's menus, job types and applications appear only when the service is granted on the tenant's licence.
* Two permission categories, **`Falcon Eye AWS`** and **`Falcon Scan AWS`**, control access per service in **`Roles`**. Onboarding an AWS organisation grants its administrator the AWS permissions automatically.

#### Who It's Designed For <a href="#who-its-designed-for" id="who-its-designed-for"></a>

IZ Suite for AWS is aimed at:

* Cloud and Platform Architects
* DevOps and Site Reliability Engineers
* Security and Compliance Teams responsible for cloud posture
* Integration Leaders who run workloads across AWS, MuleSoft and Azure
