# AWS IAM Permissions Setup for Athena, Glue, and KMS (Vault Integration)

#### 1) Purpose <a href="#id-1-purpose" id="id-1-purpose"></a>

Provide **required permissions** for a user/role to run queries in **Amazon Athena**, manage required **AWS Glue Data Catalog** objects (DB/Table), and use **KMS** where S3 buckets are encrypted with SSE-KMS.

***

### 2) Scope <a href="#id-2-scope" id="id-2-scope"></a>

This applies to:

* AWS Account: **\<account-id / name>**
* IAM Entity to grant access:
  * **IAM Role**
  * IAM User

***

### 3) Prerequisites (Must Confirm/Collect) <a href="#id-3-prerequisites-must-confirm-collect" id="id-3-prerequisites-must-confirm-collect"></a>

Before applying policy, confirm these values (replace placeholders later):

* **Athena WorkGroup name(s)** (example: `primary` or `vault-athena-wg`)
* **Athena query results S3 bucket & prefix**
  * Example: `s3://<athena-results-bucket>/athena/results/`
* **S3 data bucket(s)** Athena queries will read from
  * Example: `s3://<data-bucket>/path/`
* If using SSE-KMS:
  * **KMS key ARN(s)** used by those buckets

> Note: Athena always needs access to **S3 query results location** usually needs **S3 read** access.

***

### 4) IAM Policy (Corrected JSON) <a href="#id-4-iam-policy-corrected-json" id="id-4-iam-policy-corrected-json"></a>

#### 4.1 Minimal functional policy for Athena + Glue + KMS (+ S3) <a href="#id-4.1-minimal-functional-policy-for-athena--glue--kms--s3" id="id-4.1-minimal-functional-policy-for-athena--glue--kms--s3"></a>

Use the following as the baseline. Replace placeholders where needed.

`{ "Version": "2012-10-17", "Statement": [ { "Sid": "Athena", "Effect": "Allow", "Action": [ "athena:StartQueryExecution", "athena:GetQueryExecution", "athena:GetQueryResults", "athena:StopQueryExecution", "athena:GetWorkGroup" ], "Resource": [ "arn:aws:athena:<Region1>:<Account Id>:workgroup/primary", "arn:aws:athena:<Region2>:<Account Id>:workgroup/primary", "arn:aws:athena:<Region3>:<Account Id>:workgroup/primary" ] }, { "Sid": "Glue", "Effect": "Allow", "Action": [ "glue:GetDatabase", "glue:GetDatabases", "glue:GetTable", "glue:GetTables", "glue:GetPartition", "glue:GetPartitions", "glue:CreateTable", "glue:UpdateTable", "glue:CreateDatabase", "glue:DeleteTable" ], "Resource": [ "arn:aws:glue:<Region1>:<Account Id>:catalog", "arn:aws:glue:<Region1>:<Account Id>:database/vault_db", "arn:aws:glue:<Region1>:<Account Id>:table/vault_db/*", "arn:aws:glue:<Region2>:<Account Id>:catalog", "arn:aws:glue:<Region2>:<Account Id>:database/vault_db", "arn:aws:glue:<Region2>:<Account Id>:table/vault_db/*" ] } ] }`

\
Note:

1. The regions list should get form instance database and specify each region in this police
