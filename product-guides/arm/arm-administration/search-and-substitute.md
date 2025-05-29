# Search and Substitute

> **Audience:** Org Administrators only – general users don’t see these controls.

---

## Why Use Search & Substitute? <a href="#overview" id="overview"></a>

When you move metadata between environments, small but critical differences can break deployments:

* Hard-coded URLs that point to Production instead of Sandbox.  
* Object-level permissions that should exist only in lower tiers.  
* Label values that need slight tweaks per org.

**Search & Substitute** lets you define _rules_ that automatically find and replace text inside selected metadata _before_ the deployment or commit occurs. The rules run when you:

* Deploy sandbox → sandbox  
* Deploy sandbox → Version Control  
* Commit Version Control → sandbox (CI jobs)

That means fewer manual edits, fewer post-deployment fixes, and more predictable pipelines.

---

## Creating a Rule <a href="#procedure" id="procedure"></a>

1. Log in to ARM.  
2. Go to **Admin › Search and Substitute**.

   <figure><img src="../../../.gitbook/assets/image (729).png" alt="Admin menu showing the Search and Substitute option" width="283"></figure>

3. Click **Create Rule**.

   <figure><img src="../../../.gitbook/assets/image (730).png" alt="Create Rule button on the Search and Substitute page"></figure>

Each rule has a **label** plus one or more **parameters**.

---

### Rule Parameters Explained <a href="#rule-parameters" id="rule-parameters"></a>

<figure><img src="../../../.gitbook/assets/image (731).png" alt="Rule parameter fields: Metadata Type, Sub Element, Criteria, Substitute" width="563"></figure>

| # | Field | Purpose |
| - | ----- | ------- |
| **1** | **Metadata Type** | Choose a metadata type – _or an individual member_ – where the replacement should occur. |
| **2** | **Sub Element** | The XML path / JSON key holding the text you want to change. |
| **3** | **Criteria** | The exact string (or pattern) to search for. |
| **4** | **Substitute** | The replacement value. |

Click **+** to add up to **5** parameter sets per rule. Duplicate rows are not allowed.

#### Supported Metadata Types

`AutoResponseRule`, `CustomLabel`, `CustomMetadata`, `CustomObject`, `CustomSite`, `Dashboard`, `DashboardFolderShare`, `Network`, `NamedCredential`, `PermissionSet`, `Portal`, `Queue`, `RemoteSiteSettings`, `Report`, `ReportFolderShare`, `SamlSsoConfig`, `SharingCriteriaRule`, `SharingOwnerRule`, `Workflow`

> **Tip:** Combining Search & Substitute with **CI Job** deployment settings lets you adjust the same package differently for each target org.

---

### Example <a href="#example" id="example"></a>

Need to change an invoice number format in one org only? Create a rule like this:

* **Metadata Type:** `CustomObject › Invoice__c`  
* **Sub Element:** `Fields.displayFormat`  
* **Criteria:** `a-{000}`  
* **Substitute:** `a-{001}`

<figure><img src="../../../.gitbook/assets/image (732).png" alt="Example rule that changes displayFormat from a-{000} to a-{001} for a CustomObject"></figure>

Click **Save** to store the rule. It appears in the list with **Edit**, **Delete**, and **Clone** icons.

<figure><img src="../../../.gitbook/assets/image (733).png" alt="Rule list with edit, delete, and clone actions"></figure>

---

## Using a Rule in Deployments & Commits <a href="#whats-next" id="whats-next"></a>

### Sandbox → Sandbox Deployment <a href="#deploying-the-changes-to-a-sandbox-with-a-new-rule-assigned" id="deploying-the-changes-to-a-sandbox-with-a-new-rule-assigned"></a>

On the **Deployment Settings** screen:

1. Open **Apply Search and Substitute Rules**.  
2. Move rules to **Selected** with ![](../../../.gitbook/assets/image%20(734).png) / ![](../../../.gitbook/assets/image%20(735).png).  
3. Use the arrows to order execution (top rule runs first).

<figure><img src="../../../.gitbook/assets/image (736).png" alt="Deployment Settings with Search and Substitute rules selected"></figure>

### Commit to Version Control <a href="#committing-the-changes-from-one-salesforce-org-to-a-version-control-branch-with-new-rules-assigned" id="committing-the-changes-from-one-salesforce-org-to-a-version-control-branch-with-new-rules-assigned"></a>

During **Commit** or **Submit for Validation**, pick your rule under **Search and Substitute**.

<figure><img src="../../../.gitbook/assets/image (737).png" alt="Commit screen showing Search and Substitute rule selection"></figure>

### CI Job <a href="#performing-ci-job-with-new-rule-assigned" id="performing-ci-job-with-new-rule-assigned"></a>

When creating a **CI Job**, expand the **Deploy** section and choose the rule.

<figure><img src="../../../.gitbook/assets/image (738).png" alt="CI Job creation with Search and Substitute rule dropdown"></figure>

---

## Best Practices

* **Granularity first** – target specific metadata members when possible to avoid false replacements.  
* **Limit to five** – ARM enforces a max of 5 parameters; combine similar changes into one rule.  
* **Test in Sandbox** – run a dry-run deployment to validate your substitutions before Production.  
* **Clone, don’t copy-paste** – use the **Clone** icon to reuse rule logic with small tweaks.

With Search & Substitute configured, your deployments self-adjust to each environment—no manual XML edits required.
