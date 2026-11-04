# Ensure Complete Record Type XML Retrieval from Salesforce

### Overview

When retrieving **Record Type metadata from Salesforce**, the complete XML definition may sometimes be missing—particularly when **custom picklist fields are associated with the Record Type**.

This can cause discrepancies between environments (for example, **Dev vs. UAT**) during retrieval or deployment. This behavior is typically related to **Salesforce metadata dependencies**, not the AutoRABIT platform.

***

### Symptoms

You may encounter one or more of the following:

* Retrieved **Record Type XML is incomplete**
* Metadata differences between **two Salesforce orgs** (e.g., Dev and UAT)
* **Deployment failures or validation errors** related to picklist value dependencies
* Missing **picklist value mappings** within the Record Type metadata

***

### Cause

Record Types depend on **picklist value definitions from custom fields**.

If a Record Type references a **custom picklist field**, but that field is **not included in the same retrieval or deployment operation**, Salesforce may return **incomplete Record Type metadata**.

***

### Solution

Always retrieve or deploy **dependent metadata together**.

Include the following components in the **same deployment package**:

* **Custom Picklist Field**
* **Associated Record Type**

Doing so ensures that:

* Picklist values are correctly mapped
* Salesforce dependency checks pass
* Deployment errors are avoided

***

### Workaround

If the Record Type XML has already been retrieved incompletely:

1. Identify the **custom picklist fields referenced by the Record Type**
2. Add those fields to the **same commit or deployment package**
3. Retrieve or deploy **both components together**

***

### Additional Notes

* This behavior is related to **Salesforce metadata configuration**, not an AutoRABIT platform issue.
* Similar dependency-related retrieval gaps have been observed in other metadata types, such as **Profiles**.
* AutoRABIT relies on metadata returned by **Salesforce APIs** and cannot supplement metadata that Salesforce does not provide.

***

### When to Contact Support

Contact **AutoRABIT Support** if:

* Including the **picklist field and Record Type together** does not resolve the issue
* Metadata still differs between environments after following the recommended steps
* Deployment errors persist despite including all known dependencies
