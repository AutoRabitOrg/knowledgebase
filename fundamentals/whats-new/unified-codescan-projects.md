# Unified CodeScan Projects

### **Overview**

ARM has enhanced its CodeScan integration to associate all version control-based scans with the same CodeScan project for a given repository.

This enhancement ensures consistent project mapping across multiple workflows and enables users to select existing baseline branches for changed-line scanning.

### **Supported Workflows**

The unified CodeScan project mapping applies to the following ARM workflows:

* EZ-Commit
* EZ-Merge
* CI Jobs
* Deployments
* Standalone CodeScan Reports

Scans performed through these workflows for the same repository are associated with the same CodeScan project.

### **Baseline Branch Selection**

Previously, baseline branches created through one workflow might not have been available in another due to differences in CodeScan project mapping.

With this enhancement, ARM retrieves baseline branches from the same CodeScan project used for the scan.

#### **Performing Changed-Line Scanning**

1. Navigate to **Reports** and initiate a CodeScan baseline scan against the required version control repository and branch.
2. Complete the baseline scan.
3. Navigate to **EZ-Commit** or **EZ-Merge**.
4. Enable CodeScan under prevalidation.
5. Select the changed-line scanning option.
6. Select the required branch from the **Baseline Branch** dropdown.
7. Proceed with the scan.

### **Important Considerations**

* Existing CodeScan project mappings are preserved.
* Org-to-Org deployment scans continue to use the Salesforce org-based CodeScan project.
* Previously generated scan history remains accessible under its original CodeScan project.
* CodeScan quality gate and quality profile configurations remain unchanged.

### **Benefits**

* Consistent CodeScan project mapping across version control workflows.
* Improved baseline branch availability.
* Centralized visibility into scan results.
* Reduced fragmentation of CodeScan projects.
