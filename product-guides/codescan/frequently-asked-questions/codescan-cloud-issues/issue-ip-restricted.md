# Issue "ip restricted"

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-LMO4KJOV.png)

The **ip restricted** issue can be solved by relaxing the ip restrictions for the CodeScan connected app in the org you are trying to scan.

To do this follow the below steps:

1. Log in to the org you are trying to scan.
2. Go to **Setup** and search for **Connected Apps OAuth Usage**.
3. Install the app that is making the scan (_CodeScan Cloud_ or _CodeScan Quick Reports_).
4. Click **Manage App Policies** and then **Edit Policies**.
5. Under **IP Relaxation** select **Relax IP Restrictions**.
6. Re-Run the scan.
