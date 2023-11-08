# Amazon AWS S3 Storage Environment

The following article deals with configuring the AWS S3 bucket as a storage environment in your Vault account. To begin with, you will need an S3 bucket created in your AWS account.&#x20;

### How to create and configure AWS S3 bucket <a href="#how-to-create-and-configure-aws-s3-bucket" id="how-to-create-and-configure-aws-s3-bucket"></a>

1. Log in to the AWS Console at [https://aws.amazon.com/console/](https://aws.amazon.com/console/)
2. From the storage service, click on **S3**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235583015.png" alt=""><figcaption></figcaption></figure>

3.  Click on **Create Bucket**. The **Create bucket** page opens.&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235593679.png" alt=""><figcaption></figcaption></figure>
4. Enter the **Bucket name**.The Bucket name must:
   * Should be unique across the globe
   * Be between 3 and 63 characters long.
   * Not contain uppercase characters.
   * Start with a lowercase letter or number.
5. In **Region**, choose the AWS Region where you want the bucket to reside (keep a note of the AWS region chosen by you. _For ex- us-east-2_). This will come in handy when you configure the bucket in Vault.
6. Choose **Create bucket**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235608993.png" alt="" width="563"><figcaption></figcaption></figure>

7. Once you're done creating the bucket, go to the **Properties** tab.
8. Click on **Default Encryption** and choose the second option i.e., **AES-256**.
9. Click on the **Save** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235620241.png" alt="" width="375"><figcaption></figcaption></figure>

10. Next, search for **IAM** from the **AWS Management console** homepage.
11. Click on **Policies > Create policy**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235629842.png" alt="" width="563"><figcaption></figcaption></figure>

12. Switch to the **JSON** tab and paste the below text by replacing '**bucket\_name'** with the name of the bucket that was created in previous steps.

```
{ 
    "Version": "2012-10-17", 
    "Statement": [
        { 
            "Action": [ 
                "s3:ListAllMyBuckets" 
            ], 
            "Effect": "Allow", 
            "Resource": [ 
                "arn:aws:s3:::*" 
            ] 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "s3:*", 
            "Resource": [ 
                "arn:aws:s3:::bucket_name", 
                "arn:aws:s3:::bucket_name/*" 
            ] 
        }, 
        { 
            "Effect": "Deny", 
            "NotAction": "s3:*", 
            "NotResource": [ 
                "arn:aws:s3:::bucket_name", 
            "arn:aws:s3:::bucket_name/*" 
            ] 
        } 
    ] 
}
```

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235652798.png" alt="" width="563"><figcaption></figcaption></figure>

13. Click on **Review policy** and provide a name to the policy.
14. Click on **Create policy**.
15. After the policy is created, go to the **Users** tab, and click on **Add user**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235679656.png" alt="" width="563"><figcaption></figcaption></figure>
16. Enter an IAM username specific for Vault integration.&#x20;
17. Select the **AWS access type** as **Programmatic access.**
18. Click on **Next: Permissions** to go to the next page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235688422.png" alt="" width="563"><figcaption></figcaption></figure>

19. Click on **Attach existing policies directly.**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235705771.png" alt=""><figcaption></figcaption></figure>

20. Search for the policy created in _Steps 10-14._&#x20;
21. Select the policy and click on **Next: Tags.**&#x20;
22. Skip to the last screen and click on **Create user**.&#x20;
23. Click on **Download .CSV file** for downloading the credentials (access key and secret key) to be configured in Vault.&#x20;

### Configuring in Vault <a href="#configuring-in-vault" id="configuring-in-vault"></a>

1. Log in to your Vault account.
2. Go to **Settings > Backup Environment.**
3. Select **AWS S3** as the **Storage Type**.
4. Provide a **label** of your choice (Need not be the same as your S3 Bucket name).
5. Enter the name of your s3 bucket in the **Bucket Name** field.
6. Provide the **Access key** and **Secret key** by copying from the CSV file downloaded earlier (mentioned in _Step 23_).
7. Select the region to be the same as the region provided for the bucket while creating in _Step 5_.
8. Enable the checkbox: **AES-256 Encryption**
9. Click on **Save Settings**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623235724406.png" alt="" width="563"><figcaption></figcaption></figure>



\
