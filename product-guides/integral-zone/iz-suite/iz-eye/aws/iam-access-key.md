# IAM Access Key

IZ Suite connects to an AWS account with an IAM access key pair (Access Key ID and Secret Access Key). The key should belong to a dedicated IAM user with **read-only** permissions on the services you want to govern. IZ Suite never creates, changes or deletes AWS resources and never reads secret values.

{% hint style="info" %}


* Create one access key per AWS account you onboard. The key must belong to the account whose id you enter when onboarding: IZ Suite checks this on every sync and stops the sync if the key belongs to a different account.
* Services you do not license or do not want to govern can be left out of the policy. A denied call only affects that service.
{% endhint %}

#### Create the IAM policy <a href="#create-the-iam-policy" id="create-the-iam-policy"></a>



1. In the AWS console, open **`IAM`** -> **`Policies`** and click **`Create policy`**
2. Select the **`JSON`** editor and paste the policy below
3. Name the policy, for example `IZSuiteReadOnly`, and create it

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "IZSuiteDiscovery",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeRegions",
        "lambda:ListFunctions",
        "lambda:GetFunction",
        "lambda:GetPolicy",
        "lambda:ListFunctionUrlConfigs",
        "lambda:ListEventSourceMappings",
        "cloudformation:ListStacks",
        "cloudformation:DescribeStacks",
        "cloudformation:GetTemplate",
        "states:ListStateMachines",
        "states:DescribeStateMachine",
        "apigateway:GET",
        "ecs:ListClusters",
        "ecs:ListServices",
        "ecs:DescribeServices",
        "ecs:DescribeTaskDefinition",
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeDBEngineVersions",
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeLoadBalancerAttributes",
        "elasticloadbalancing:DescribeListeners",
        "elasticloadbalancing:DescribeTargetGroups",
        "elasticloadbalancing:DescribeTargetGroupAttributes",
        "secretsmanager:ListSecrets",
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetResourcePolicy",
        "cloudfront:ListDistributions",
        "cloudfront:GetDistribution",
        "dynamodb:ListTables",
        "dynamodb:DescribeTable",
        "dynamodb:DescribeContinuousBackups",
        "dynamodb:DescribeTimeToLive",
        "sqs:ListQueues",
        "sqs:GetQueueUrl",
        "sqs:GetQueueAttributes",
        "sns:ListTopics",
        "sns:GetTopicAttributes",
        "sns:ListSubscriptionsByTopic",
        "events:ListEventBuses",
        "events:DescribeEventBus",
        "events:ListRules",
        "events:DescribeRule",
        "events:ListTargetsByRule",
        "codepipeline:ListPipelines",
        "codepipeline:GetPipeline",
        "codebuild:ListProjects",
        "codebuild:BatchGetProjects",
        "codedeploy:ListApplications",
        "codedeploy:ListDeploymentGroups",
        "codedeploy:BatchGetDeploymentGroups",
        "codedeploy:GetDeploymentGroup"
      ],
      "Resource": "*"
    },
    {
      "Sid": "IZSuiteExecutionRoles",
      "Effect": "Allow",
      "Action": [
        "iam:GetRole",
        "iam:ListRolePolicies",
        "iam:GetRolePolicy",
        "iam:ListAttachedRolePolicies",
        "iam:GetPolicy",
        "iam:GetPolicyVersion"
      ],
      "Resource": "*"
    }
  ]
}

```



| Statement                   | Why it is needed                                                                                                                                                                                                                              |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`IZSuiteDiscovery`**      | Lists the resources of each service and reads the definition that is scanned. `ec2:DescribeRegions` is only used when no regions are entered on the organisation and the regions are discovered automatically.                                |
| **`IZSuiteExecutionRoles`** | Optional. Reads the IAM roles used by Lambda functions, Step Functions state machines and ECS task definitions so the IAM rules (for example over-permissive policies) can be evaluated. Without it the scan still runs, without those rules. |

{% hint style="warning" %}
The policy deliberately does not include `secretsmanager:GetSecretValue`. IZ Suite evaluates a secret's rotation, encryption and resource policy from its metadata only.
{% endhint %}



#### Create the IAM user and access key <a href="#create-the-iam-user-and-access-key" id="create-the-iam-user-and-access-key"></a>



1. Open **`IAM`** -> **`Users`** and click **`Create user`**. Do not give the user console access.
2. On **`Set permissions`**, select **`Attach policies directly`** and attach the policy created above
3. Open the new user, select the **`Security credentials`** tab and click **`Create access key`**
4. Choose **`Third-party service`** (or **`Other`**) as the use case and create the key
5. Copy the **`Access key`** and the **`Secret access key`**. The secret is shown only once.
6. Note the 12-digit **`Account ID`** shown in the account menu at the top right of the console

The Account ID, Access Key ID and Secret Access Key are entered when the AWS account is onboarded&#x20;



#### Rotating the key <a href="#rotating-the-key" id="rotating-the-key"></a>

Create a second access key for the same IAM user, update the organisation in IZ Suite with the new key, confirm the next sync succeeds, and then deactivate and delete the old key in AWS.

<br>
