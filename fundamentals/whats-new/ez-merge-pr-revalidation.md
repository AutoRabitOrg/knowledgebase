# EZ-Merge PR Revalidation

### **Overview**

ARM enhances the **EZ-Merge** workflow to support iterative changes and automatic revalidation of existing pull requests.

Users can now configure ARM to create a pull request before executing deployment validation and Static Code Analysis (SCA). Additional commits pushed to the temporary branch are automatically detected, triggering the configured validations again without requiring users to restart the EZ-Merge process.

ARM also provides an option to automatically synchronize changes from the temporary branch back to the original source branch.

**Availability:** New UI only.

### **1. Enable Pull Request Creation Before Validation**

To enable the enhanced workflow:

1. Navigate to **Settings → My Account → Merge Settings**.
2. Enable the **Create Pull Request Before Merge Validations** option.
3. Save the settings.

Once enabled, ARM creates the temporary branch and raises the pull request before executing the configured deployment validation and SCA checks.

![](<../../.gitbook/assets/image (689).png>)

### **2. Enable Back Sync Changes to Source Branch**

While initiating an EZ-Merge operation:

1. Select the required repository, source branch, and destination branch.
2. Configure the external pull request and required validation settings.
3. Enable the **Back Sync Changes to Source Branch** option.
4. Submit the EZ-Merge request.

When this option is enabled, ARM automatically synchronizes additional changes committed to the temporary branch back to the original source branch.

<figure><img src="../../.gitbook/assets/image (714).png" alt=""><figcaption></figcaption></figure>

### **3. Review and Update the Pull Request**

Once the EZ-Merge request is submitted:

1. ARM creates a temporary branch from the original source branch.
2. ARM raises a pull request and updates the merge status to **PR Raised**.
3. ARM executes the configured deployment validation and SCA checks.
4. Users can review the pull request directly in their Git repository.
5. If additional changes are required, users can commit and push changes directly to the temporary branch.

ARM retains the existing pull request throughout the review process, eliminating the need to initiate a new EZ-Merge request for every change.

### **4. Automatic Revalidation**

When additional commits are pushed to the temporary branch, ARM automatically:

* Detects the newly committed changes.
* Synchronizes changes to the original source branch if **Back Sync Changes to Source Branch** is enabled.
* Reruns the configured deployment validation and SCA checks against the latest changes.
* Retains previous validation logs and results.
* Updates the existing EZ-Merge request with the latest validation results.

Users can repeat this process multiple times until the pull request is ready to merge.

### **Workflow Comparison**

**Previous Workflow**

Initiate EZ-Merge

Deployment Validation + SCA

Create Temporary Branch + PR

Review Pull Request

Restart EZ-Merge for additional changes

**Enhanced Workflow**

Initiate EZ-Merge

Create Temporary Branch + PR

Deployment Validation + SCA

Review PR and Commit Changes

Back Sync Source Branch (Optional)

Automatic Revalidation

Repeat as required

Complete Pull Request

### **Important Considerations**

* This enhancement is available only in the **New UI**.
* The existing EZ-Merge workflow in the Classic UI remains unchanged.
* The **Create Pull Request Before Merge Validations** option must be enabled under Merge Settings to use the enhanced workflow.
* Additional changes must be committed to the temporary branch associated with the existing pull request.
* Automatic source branch synchronization occurs only when **Back Sync Changes to Source Branch** is enabled.
* Deployment validation and SCA are rerun based on the configured validation settings.
* Previous validation results and execution logs are retained.
* Users do not need to create a new EZ-Merge request or pull request for additional changes.

### **Benefits**

* Supports multiple rounds of pull request review and changes.
* Eliminates repetitive EZ-Merge operations.
* Automates deployment validation and SCA revalidation.
* Enables automatic source branch synchronization.
* Maintains validation history within the same EZ-Merge request.
* Improves collaboration and reduces manual effort.
