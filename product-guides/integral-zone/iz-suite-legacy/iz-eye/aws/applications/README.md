---
description: >-
  Each AWS service has its own applications page in IZ Eye. All of them work the
  same way; Lambda Functions and CloudFormation Stacks have additional behaviour
  described on their own pages.
---

# Applications

{% hint style="warning" %}


* Resources are listed only after the analysis schedule of the service has run - [Schedule Configuration](../schedule-configuration.md)
* A service is listed only when it is granted on your licence and your role has the matching **`Falcon Eye AWS`** permission
{% endhint %}

#### To view the resources of a service <a href="#to-view-the-resources-of-a-service" id="to-view-the-resources-of-a-service"></a>

1. Navigate to **`IZ Eye`** -> **`AWS`** and select the service:

| Menu                      | Each application is                       | Documents scanned (file names shown in issues)                                                                                                                                                  |
| ------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`AWS Lambda`**          | A Lambda function                         | `lambda-function-definition.json`, `lambda-policy.json`, `lambda-url-configs.json`, `lambda-event-source-mappings.json`, `lambda-iam-role.json`, plus the Python code of the deployment package |
| **`AWS CloudFormation`**  | A CloudFormation stack                    | The stack's template                                                                                                                                                                            |
| **`AWS Step Functions`**  | A state machine                           | `sfn-state-machine-definition.json`, `sfn-iam-role.json`                                                                                                                                        |
| **`AWS API Gateway`**     | A REST, HTTP or WebSocket API             | `apigw-api-definition.json`                                                                                                                                                                     |
| **`AWS ECS`**             | A task definition used by an ECS service  | `ecs-task-definition.json`, `ecs-service.json`, `ecs-iam-role.json`                                                                                                                             |
| **`AWS RDS`**             | An RDS instance or Aurora cluster         | `rds-instance.json` or `rds-cluster.json`, `rds-engine-support.json`                                                                                                                            |
| **`AWS Load Balancer`**   | A load balancer                           | `elb-load-balancer.json`, `elb-listeners.json`, `elb-target-groups.json`                                                                                                                        |
| **`AWS Secrets Manager`** | A secret (metadata only, never the value) | `secrets-secret.json`, `secrets-resource-policy.json`                                                                                                                                           |
| **`AWS CloudFront`**      | A distribution (environment **`global`**) | `cloudfront-distribution.json`                                                                                                                                                                  |
| **`AWS DynamoDB`**        | A table                                   | `dynamodb-table.json`                                                                                                                                                                           |
| **`AWS SQS`**             | A queue                                   | `sqs-queue.json`                                                                                                                                                                                |
| **`AWS SNS`**             | A topic                                   | `sns-topic.json`                                                                                                                                                                                |
| **`AWS EventBridge`**     | An event bus                              | `eventbridge-bus.json`, `eventbridge-rules.json`                                                                                                                                                |
| **`AWS CodePipeline`**    | A pipeline                                | `codepipeline-pipeline.json`                                                                                                                                                                    |
| **`AWS CodeBuild`**       | A build project                           | `codebuild-project.json`                                                                                                                                                                        |
| **`AWS CodeDeploy`**      | A deployment group                        | `codedeploy-deployment-group.json`                                                                                                                                                              |

2. Overview includes -
   1. **`Name`** - Name of the resource
   2. **`Organization`** - The AWS account to which the resource belongs
   3. **`Environment`** - The region to which the resource belongs (or **`global`**)
3. Click on the **`Plus`** icon to view the details. AWS resources have a single version, named **`default`**, which is rescanned whenever the analysis job runs.
4. Summary details include -
   1. **`Total Issues`** - Indicates total number of issues once the resource is scanned
   2. **`Status`** - Status of the resource reported by AWS, for example the Lambda function state or the CloudFormation stack status
   3. **`Last Scan`** - Time since the last scan was performed
5. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues with file names and line numbers. See [Application Issues](../../application-issues.md).
   3. **`View Metrics`** - Metrics collected for the resource, including its relationships to other resources.
   4. **`View Previous Scans`** - Scan history of the resource.
   5. **`Trigger Force Scan`** - Scan the resource now.
   6. **`Include in Scan Schedule`** / **`Exclude from Scan Schedule`** - Include or exclude the resource from scheduled scans.

