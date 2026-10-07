# Schedule Configuration

{% hint style="info" %}


* The AWS account must be onboarded before configuring the schedules - [Onboard an AWS Account](onboard-an-aws-account.md)
* Repeatedly creating a schedule for the same organization and environment will simply overwrite the pre-existing schedule.
* Only the job types of the AWS services granted on your licence are listed.&#x20;
{% endhint %}

#### Configuring the initial Schedule <a href="#configuring-the-initial-schedule" id="configuring-the-initial-schedule"></a>

The **`AWS Sync`** schedule creates the environments of every onboarded AWS account (one per region plus **`global`**). Creating a recurring schedule picks up new accounts, new regions and rotated credentials automatically.

1. Navigate to **`Schedules`** -> **`Schedules`** and click on **`Configure Schedule`**
2. Select **`AWS Sync`** job type and proceed
3. Select the appropriate schedule based on the requirement (Either **`OneTime`** or **`Recurring`**)
4. Once the schedule completes successfully, the regions are listed as environments of the AWS organisation under the **`Organization`** main menu. Click on **`View Environments`** to see them.

#### Configuring schedule for continuous scans <a href="#configuring-schedule-for-continuous-scans" id="configuring-schedule-for-continuous-scans"></a>

Each AWS service has its own analysis job type. A job discovers the resources of its service in the selected environments and scans them against the service rule pack.

1. Navigate to **`Schedules`** -> **`Schedules`** and click on **`Configure Schedule`**
2. Select the job type of the service to scan:

| Job type                           | Discovers and scans                        |
| ---------------------------------- | ------------------------------------------ |
| **`AWS Lambda Analysis`**          | Lambda functions                           |
| **`AWS CloudFormation Analysis`**  | CloudFormation stacks                      |
| **`AWS Step Functions Analysis`**  | Step Functions state machines              |
| **`AWS API Gateway Analysis`**     | API Gateway REST, HTTP and WebSocket APIs  |
| **`AWS ECS Analysis`**             | ECS task definitions used by ECS services  |
| **`AWS RDS Analysis`**             | RDS instances and Aurora clusters          |
| **`AWS Load Balancer Analysis`**   | Elastic Load Balancing (v2) load balancers |
| **`AWS Secrets Manager Analysis`** | Secrets Manager secrets (metadata only)    |
| **`AWS CloudFront Analysis`**      | CloudFront distributions                   |
| **`AWS DynamoDB Analysis`**        | DynamoDB tables                            |
| **`AWS SQS Analysis`**             | SQS queues                                 |
| **`AWS SNS Analysis`**             | SNS topics                                 |
| **`AWS EventBridge Analysis`**     | EventBridge event buses and their rules    |
| **`AWS CodePipeline Analysis`**    | CodePipeline pipelines                     |
| **`AWS CodeBuild Analysis`**       | CodeBuild projects                         |
| **`AWS CodeDeploy Analysis`**      | CodeDeploy deployment groups               |

3. On **`Choose Organization`**, select the AWS organisations and the environments (regions) to scan. For **`AWS CloudFront Analysis`**, select the **`global`** environment.
4. Select the schedule/frequency at which the analysis should be performed
5. Click on **`Submit`** to configure the schedule

#### Excluding resources (Pattern Matchers) <a href="#excluding-resources-pattern-matchers" id="excluding-resources-pattern-matchers"></a>

By default every resource of a service is scanned. Each service has a pattern matcher setting that includes or excludes resources by name, which keeps test or temporary resources out of the inventory.

1. Navigate to main menu **`Global Settings`** -> **`Settings`** and search for **`AWS <Service> Pattern Matcher`**, for example **`AWS Lambda Pattern Matcher`**
2. Click on edit action item and update the `includePattern` / `excludePattern` regular expressions:

```
{
  "config": {
    "name": {
      "includePattern": [".*"],
      "excludePattern": ["^test-.*", ".*-sandbox$"]
    }
  }
}

```

3. Click on save. The pattern is applied from the next run of the analysis job.

| Service            | Attributes that can be matched                                                 |
| ------------------ | ------------------------------------------------------------------------------ |
| Lambda             | `name`, `runtime` (for example `python3.12`), `packageType` (`Zip` or `Image`) |
| CloudFormation     | `name`, `status` (stack status, for example `CREATE_COMPLETE`)                 |
| All other services | `name`                                                                         |

The pattern format is the same as for the other IZ Eye pattern matchers - see [IZ Eye Scan Patterns](../../iz-core/settings/iz-eye-scan-patterns.md).



#### Per-application schedules <a href="#per-application-schedules" id="per-application-schedules"></a>

Individual resources can also be included in or excluded from scheduled scans:

* From the application's version row in IZ Eye, use **`Include in Scan Schedule`** / **`Exclude from Scan Schedule`**
* Or navigate to **`Schedules`** -> **`IZ Eye Apps`** and select the AWS service, for example **`AWS Lambda`**
