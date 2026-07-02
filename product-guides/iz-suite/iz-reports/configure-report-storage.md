# Configure Report Storage

## Report Storage Options

Reports can currently be configured to be stored in any of the following cloud storage options:

### AWS S3 Bucket

* Navigate to **`S3`**, click on **`Create Bucket`**, follow the default instructions and click on **`Create`**
* Navigate to **`IAM`** -> **`Policies`**
* Create a new policy select JSON policy editor and paste the following contents (Make sure the **`BUCKET_NAME`** keyword is replace with actual bucket name created in the previous step):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersionTagging",
                "s3:GetObjectAttributes",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::BUCKET_NAME/*"
        }
    ]
}
```

* Click on **`Next`** and enter the policy name / description
* Click on **`Create Policy`**
* Navigate to **`IAM`** -> **`Users`**
* Enter the user name and click on **`Next`**
* Select `Attach Policies Directly` and select the policy that was created in the step earlier
* Follow the instructions and create the user
* Select the newly created user and select **`Security Credentials`** tab and click on **`Create Access Key`**
* Select **`Command Line Interface (CLI)`** option and click on next
* Finally click on **`Create Access Key`** and copy the generated **`Access Key`** and **`Secret Access key`**&#x20;

1. Navigate to **`Global Settings`** -> **`Settings`**
2. Search for **`Reporting Config`** and click on **`Edit`** action item
3. Value for **`PROVIDER`** should be **`AWS S3`**
4. Value for **`REGION`** should be the value in which the bucket was created
5. Value for **`BUCKET_NAME`** should be the exact bucket name
6. Value for **`CLIENT_ID`** should be the value of **`Access Key`** generated earlier
7. Value for **`CLIENT_SECRET`** should be the value of **`Secret Access key`** generated earlier

### Google Cloud Storage Bucket

1. In Google Cloud, create a Bucket and Service Account -
   1. Navigate to **`Cloud Storage`** -> **`Buckets`**
   2. Click on **`Create`** and follow the instructions to create a new bucket.
   3. Navigate to **`IAM & Admin`** -> **`Service Accounts`**
   4. Click on **`Create Service Account`** -> Enter the name, description and click on **`Create and Continue`**
   5. Add **`Storage Object Creator`** & **`Storage Object Viewer`** roles and create the service account
   6. Click on the newly create service account and navigate to **`Keys`** tab.
   7. Click on **`Add Key`** -> **`Create New Key`** -> **`JSON`**, to download the private key Json.
2. In IZ
   1. Navigate to **`Global Settings`** -> **`Settings`**
   2. Search for **`Reporting Config`** and click on **`Edit`** action item
   3. Value for **`PROVIDER`** should be **`GCS`**
   4. Value for **`REGION`** should be the value in which the bucket was created
   5. Value for **`BUCKET_NAME`** should be the exact bucket name
   6. Value for **`SECURE_VALUE_1`** should be contents of the JSON private key file downloaded earlier

### See Also

* [Deprecations](../../integral-zone/iz-suite/iz-lens/deprecations.md)
* [Aggregated Dashboard](../iz-eye/dashboard.md)
* [Application Dashboard](../../integral-zone/iz-suite/iz-eye/anypoint-platform/application-dashboard.md)
* [Mule Projects](../../integral-zone/iz-suite/iz-eye/anypoint-platform/applications/mule-applications.md)
* [API Applications](../../integral-zone/iz-suite/iz-eye/anypoint-platform/applications/exchange-apis.md)
