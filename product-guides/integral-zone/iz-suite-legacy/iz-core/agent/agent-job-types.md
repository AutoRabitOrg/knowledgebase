# Agent Job Types

{% hint style="warning" %}
Each Agent is capable of running/handling multiple job types. For example - Scanning Anypoint Runtime Applications, Performing health checks for configured endpoints
{% endhint %}

The status of each **`Job Type`** supported by the Agent can administered by following the below steps -

1. Navigate to **`Global Settings`** -> **`Agents`**&#x20;
2. Expand the details by clicking on the **`Plus`** icon&#x20;
3. Each Job Type can have different status associated with it -
   1. **`RUNNING`** - Running without any issues
   2. **`INVALID CREDENTIALS`** - Running, but with missing configurations. E.g.: Client Id and Secret for a specific job type is not configured
   3. **`STOPPED`** - Not Running
4. The **`IS MASTER`** column indicates if the current instance is the **Master**
   1. **Master** instance is the once responsible for creating the jobs based on the configured schedules



#### Job Type Packages <a href="#job-type-packages" id="job-type-packages"></a>

From 26.4.1 the job types are packaged per platform: **Anypoint Platform**, **Azure Integration Services**, **Salesforce Platform** and **AWS Platform**. An agent downloads one package per platform on its next job instead of one per job type, and a new job type on an existing platform needs no additional download. Existing job types are updated automatically during the server upgrade; no agent configuration change is needed.



#### Anypoint Platform Job Types <a href="#anypoint-platform-job-types" id="anypoint-platform-job-types"></a>

These job types run from the **Anypoint Platform** package. Each is available only when its product is enabled on the tenant's licence.

| Job Type                              | Discovers                                                    |
| ------------------------------------- | ------------------------------------------------------------ |
| **`Anypoint Mule Runtime Analysis`**  | Mule applications deployed in Anypoint **`Runtime Manager`** |
| **`Anypoint API Instance Analysis`**  | API instances in Anypoint **`API Manager`**                  |
| **`Anypoint Exchange APIs Analysis`** | APIs published in Anypoint **`Exchange`**                    |
| **`Anypoint Sync`**                   | Anypoint organizations, environments and Teams users         |

Schedules are configured under **`Schedules`** → **`IZ Eye Apps`** → **`Runtime Applications`**, **`API Manager Applications`** or **`Exchange Assets`**

#### Azure Job Types <a href="#azure-job-types" id="azure-job-types"></a>

These job types run from the **Azure Integration Services** package. Each is available only when its product is enabled on the tenant's licence.

| Job Type                              | Discovers                                                                                                                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`Azure Integration Services Sync`** | Azure subscriptions and resource groups, using the Microsoft Entra ID app registration from **`Azure Integration Services Sync`** in _Global Settings_ |
| **`Azure Logic App Analysis`**        | Logic Apps                                                                                                                                             |
| **`Azure API Management Analysis`**   | API Management instances and their APIs                                                                                                                |
| **`Azure Function App Analysis`**     | Function Apps                                                                                                                                          |
| **`Azure Service Bus Analysis`**      | Service Bus namespaces. Not run by the 26.4.1 agent and has no schedule menu entry.                                                                    |

Schedules are configured under **`Schedules`** → **`IZ Eye Apps`** → **`Azure Logic Apps`**, **`Azure API Management`** or **`Azure Function Apps`**

#### AWS Job Types <a href="#aws-job-types" id="aws-job-types"></a>

26.4.1 adds one job type per AWS service. Each discovers the service's resources in every AWS organization and region it is scheduled for, and is available only when the service is enabled on the tenant's licence.

| Job Type                           | Discovers                                       |
| ---------------------------------- | ----------------------------------------------- |
| **`AWS Lambda Analysis`**          | Lambda functions                                |
| **`AWS CloudFormation Analysis`**  | CloudFormation stacks (including failed stacks) |
| **`AWS Step Functions Analysis`**  | Step Functions state machines                   |
| **`AWS API Gateway Analysis`**     | API Gateway APIs                                |
| **`AWS ECS Analysis`**             | ECS task definitions                            |
| **`AWS RDS Analysis`**             | RDS and Aurora databases                        |
| **`AWS Load Balancer Analysis`**   | Load balancers                                  |
| **`AWS Secrets Manager Analysis`** | Secrets Manager secrets                         |
| **`AWS CloudFront Analysis`**      | CloudFront distributions                        |
| **`AWS DynamoDB Analysis`**        | DynamoDB tables                                 |
| **`AWS SQS Analysis`**             | SQS queues                                      |
| **`AWS SNS Analysis`**             | SNS topics                                      |
| **`AWS EventBridge Analysis`**     | EventBridge event buses                         |
| **`AWS CodePipeline Analysis`**    | CodePipeline pipelines                          |
| **`AWS CodeBuild Analysis`**       | CodeBuild projects                              |
| **`AWS CodeDeploy Analysis`**      | CodeDeploy applications                         |
| **`AWS Sync`**                     | AWS account and region onboarding               |

The AWS credential is taken from the AWS organization (see [Organizations](../organization/organizations.md)); no client id or secret is configured on the job type. Schedules are configured under **`Schedules`** → **`IZ Eye Apps`**, which has one entry per licensed AWS service, for example **`AWS Lambda`**.





### See Also

* [Creating an Agent](create-agent.md)
* [Updating an Agent](update-agent.md)
