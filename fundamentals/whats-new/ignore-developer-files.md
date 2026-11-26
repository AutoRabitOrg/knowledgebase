# Ignore Developer Files

### **Overview**

ARM introduces the **Ignore Developer Files** option to exclude files and folders defined in the repository's `.forceignore` file during Salesforce validation and deployment operations.

When enabled, ARM honors the exclusion patterns configured in the `.forceignore` file, allowing users to control which files are excluded from the package.

This option is **unchecked by default**, allowing users to enable it based on their requirements.

**Availability:** Classic and New UI.

### **Supported Workflows**

The **Ignore Developer Files** option is available in the following workflows:

| Workflow    | Configuration Step    |
| ----------- | --------------------- |
| Deployments | Deployment Settings   |
| CI Jobs     | Build                 |
| EZ-Merge    | Merge Review Settings |
| EZ-Commit   | Submit for Validation |

### **How to Use**

1. Ensure the `.forceignore` file is configured in your version control repository with the required file and folder exclusion patterns.
2. Navigate to any of the supported workflows.
3. Locate the **Ignore Developer Files** option.
4. Enable the checkbox.
5. Proceed with the build, validation, or deployment.

### **File Exclusion Behavior**

When the **Ignore Developer Files** option is enabled, ARM excludes only the files and folders matching the patterns defined in the `.forceignore` file in the version control repository.

Files not matching these patterns are not excluded by this option. When the option is disabled, ARM does not apply the `.forceignore` rules.

#### **Example**

Consider a repository containing a `.forceignore` file with the following exclusion patterns:

```
**/__tests__/**
**/*.test.js
**/*.ts
**/validationRules/**
```

When the **Ignore Developer Files** option is enabled, ARM excludes files and folders matching these patterns from the package.

Users should configure exclusion patterns carefully to avoid excluding metadata required for deployment.

### **Execution Logs**

ARM displays information about excluded developer files in the execution logs, helping users identify which files were excluded from the package.

### **Important Considerations**

* The **Ignore Developer Files** option is unchecked by default.
* Users must manually enable the option when required.
* Only files and folders matching the `.forceignore` patterns are excluded by this option.
* When the option is disabled, ARM retains its existing file-handling behavior.
* Excluded files remain unchanged in the version control repository.
* Consistent file exclusion rules are applied during validation and subsequent deployment.

### **Benefits**

* Greater control over file exclusions.
* Reduced deployment failures caused by unnecessary development files.
* Consistent file handling across supported ARM workflows.
* Improved flexibility through repository-specific exclusion patterns.
