# Enable Delta on PermissionSets

## Overview

Starting with Salesforce **API version 40**, deploying PermissionSets by default replaces the entire set in the destination org with the incoming metadata. This can result in the loss of existing permissions if not managed carefully.

By selecting the **Enable Delta on PermissionSets** option, AutoRABIT retrieves the existing PermissionSets from the Source Org or Source Branch and **appends only the new changes** to the deployment package—preserving existing permissions in the destination org.

![Enable Delta on PermissionSets UI](../../../../.gitbook/assets/image%20(766).png)

{% hint style="info" %}
**Important Note:**  
The **Enable Delta on PermissionSets** feature is available **only** in the **CI Job module**. It is **not supported** in EZ-Commit, EZ-Merge, or standalone Deployment modules.
{% endhint %}

---

## Scenario 1

- **Source Org:** A PermissionSet contains a permission to an **Apex class A**.
- **Destination Org:** The same PermissionSet already includes **Apex class B**.

### Behavior:

- **Without Delta Enabled:** The PermissionSet in the destination org is **replaced**, and only **Apex class A** remains.
- **With Delta Enabled:** The PermissionSet in the destination org is **appended**, so both **Apex class A** and **Apex class B** permissions exist post-deployment.

![Permission Set Behavior with Delta](../../../../.gitbook/assets/image%20(767).png)
![Resulting Permission Set with Delta Enabled](../../../../.gitbook/assets/image%20(768).png)
