---
description: 26.4.8 build
---

# Enhanced Template Execution Logs

### **Overview**

ARM has enhanced Environment Provisioning Template execution logs to provide more detailed and actionable error information. This enhancement helps users identify migration failures, understand their causes, and take corrective action.

Additionally, a new execution status, **Partially Successful**, has been introduced to provide better visibility into the overall migration outcome.

### **Improved Execution Logs**

When an Environment Provisioning Template execution encounters a failure, ARM now provides detailed error information, including:

* Affected execution step.
* Relevant configuration details.
* Underlying error messages.

Users can review these details to troubleshoot issues, make necessary corrections, and retry the execution.

![](<../../.gitbook/assets/image (647).png>)

### **Execution Statuses**

ARM now supports the following three execution statuses:

| Status               | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| Successful           | All records are migrated successfully.                      |
| Partially Successful | Some records are migrated successfully, while others fail.  |
| Failed               | The execution fails without successfully migrating records. |

Previously, even if a single record migration failed, the entire execution was marked as **Failed**. With this enhancement, ARM displays **Partially Successful** when only some records fail to migrate.

<figure><img src="../../.gitbook/assets/image (649).png" alt=""><figcaption></figcaption></figure>

### **Benefits**

* Improved visibility into migration outcomes.
* Easier troubleshooting with detailed error messages.
* Clear distinction between partial and complete execution failures.
