# Enable Delta on PermissionSets

### Overview <a href="#overview" id="overview"></a>

As per the Salesforce behavior, for Salesforce **API 40 or later**, the entire PermissionSets will be replaced with the latest changes. However, when the **Enable Delta on PermissionSets** checkbox is selected, the PermissionSets will get retrieved from the Source org or the Source branch and will append with the latest changes in the deployment package.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617512076830.png)

#### Important Note**The "Enable Delta on PermissionSets" option is functional only in the CI Job module. It is not functional in EZ-Commit, EZ-Merge, or Deployment modules.** <a href="#important-note-the-enable-delta-on-permissionsets-option-is-functional-only-in-the-ci-job-module-it" id="important-note-the-enable-delta-on-permissionsets-option-is-functional-only-in-the-ci-job-module-it"></a>

#### Scenario 1 <a href="#scenario-1" id="scenario-1"></a>

* In **Source Org**: Deploying Permission sets with one Apex class permission
* In **Destination Org**: Same permission sets with different apex classes permission already exists

As per the Salesforce behavior, the destination org permission sets will be overridden with the newly deployed permission set. However, if the user selects the **"Enable Delta on PermissionSets"** checkbox, the destination org permission set permissions will be appended with new class permission as shown below.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623776197850.png" alt=""><figcaption></figcaption></figure>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623776224467.png)
