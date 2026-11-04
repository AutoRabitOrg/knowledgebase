# Flows in Salesforce

### What is a Flow?

In Salesforce, a flow is an application that automates complex business processes. It collects data and performs actions with it—helping users save time, avoid errors, and streamline tasks. Flows are an essential tool for automating manual processes and ensuring consistency across the platform.

### Different Categories of Flows

Salesforce flows fall into five main categories:

1. **Screen Flows** – Include user interface elements; require user input. They can be launched via actions or embedded in Lightning pages.
2. **Schedule-Triggered Flows** – Run in the background at specified intervals for each record in a batch.
3. **Autolaunched Flows** – Perform tasks without user interaction. These can be triggered from Process Builder, Apex, schedules, record changes, or platform events.
4. **Record-Triggered Flows** – Automatically triggered in the background when a record is created, updated, or deleted.
5. **Platform Event-Triggered Flows** – Triggered when a platform event message is received.

### When and Why Should I Use a Flow?

* Flows can create, edit, and delete records passed into them—even unrelated records.
* Flows can be scheduled to run at set intervals for collections of records.
* Unlike workflow rules, which can only update related records, flows offer more flexibility and broader actions.
* Compared to Process Builder, flows can also delete records and provide UI elements.

### Flows vs. Process Builder vs. Workflows vs. Apex

| Feature          | Flows                                                                                                | Process Builder                                                     | Workflows                                                         | Apex                                         |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| **Capabilities** | Automate complex logic, manipulate records, interact with external systems, offer UIs (Screen Flows) | Automate record changes and external interactions (background only) | Automate field updates, limited interaction with external systems | Automate any business logic programmatically |
| **Interface**    | Flow Builder (UI)                                                                                    | Process Builder (UI)                                                | Wizard-style setup                                                | Code (Developer Console or IDE)              |
| **Flexibility**  | High                                                                                                 | Moderate                                                            | Limited                                                           | Unlimited                                    |
| **Execution**    | Foreground and background                                                                            | Background only                                                     | Background only                                                   | Background or UI via LWC/Visualforce         |

### Activate or Deactivate a Flow

Only one version of a flow can be active at a time. When a new version is activated, any previously active version is deactivated automatically.

**Deployment Note:** The flow and its latest definition must be included in the deployment package to deactivate it in Salesforce.

### What is a Flow Interview in Salesforce?

A flow interview is a running instance of a flow. For example, a flow may serve as a call script for customer support. As the user interacts with it, Salesforce captures the input and executes the defined actions. Whether accessed via a link, button, or tab, a flow interview represents a single execution of that flow logic.



## **Common Salesforce Flow Deployment Failures and Resolutions**

### Overview

Salesforce Flow deployments frequently fail due to versioning, activation, or dependency-related issues. Most errors occur during validation when Salesforce attempts to activate Flows or resolve references that are missing in the target org.

This article outlines the most common Flow deployment errors, their causes, and recommended resolutions.

#### 1. Issue: Salesforce deployment fails with **“Invalid version number** `<x>`**”** for the `FlowDefinition` metadata type.

**Cause:** `FlowDefinition` controls Flow activation and references a specific Flow version. This error occurs when the referenced version does not exist in the target org, commonly due to mismatched Flow version histories, partial deployments, or CI/CD pipelines attempting to activate Flows before all dependencies are available.<br>

**Resolution (Recommended):** Exclude the `FlowDefinition` file from deployment. Deploy the Flow metadata (`Flow`) as inactive and activate the Flow separately after deployment.\
**Why This Works:** `FlowDefinition` is not required to deploy Flow logic. Excluding it avoids version mismatch and activation-related validation errors, making deployments more reliable across environments.

#### 2. Issue: Salesforce deployment fails with **“Cannot activate flow.”**

**Cause:** Salesforce attempts to activate the Flow during deployment, but required dependencies such as objects, fields, Apex actions, subflows, permissions, or settings are missing in the target org.\
**Resolution (Recommended):** Deploy the Flow as inactive and activate it only after all dependent metadata has been deployed.\
**Why This Works:** Activation triggers runtime validation. Delaying activation ensures all dependencies are available, preventing validation failures.

#### 3. Issue: Salesforce deployment fails with **“The flow failed to compile.”**

**Cause:** The Flow contains invalid or unresolved references, often due to missing fields, renamed objects, or unsupported elements in the target org.\
**Resolution (Recommended):** Verify that all referenced metadata exists in the target org and redeploy after correcting missing dependencies.\
**Why This Works:** Flow compilation requires all references to be valid at deployment time.

#### 4. Issue: Salesforce deployment fails with **“Flow references an invalid element.”**

**Cause:** One or more Flow elements reference metadata that has been deleted, renamed, or is unavailable in the target org.\
**Resolution (Recommended):** Open and re-save the Flow in the source org to refresh references, then redeploy.\
**Why This Works:** Re-saving updates internal references and removes stale metadata links.

#### 5. Issue: Salesforce deployment fails with **“Apex action not found”** or **“Apex class does not exist.”**

**Cause:** The Flow references an invocable Apex method that is missing or not yet deployed in the target org.\
**Resolution (Recommended):** Deploy Apex classes before deploying or activating Flows.\
**Why This Works:** Flow validation checks for the presence of referenced Apex actions.

#### 6. Issue: Salesforce deployment fails with **“Flow type not supported.”**

**Cause:** The target org does not have the required feature, license, or setting enabled for the Flow type (e.g., platform event flows or specialized screen components).\
**Resolution (Recommended):** Enable required features or deploy the Flow inactive and activate it after configuration.\
**Why This Works:** Flow types are validated against org capabilities during activation.

#### Key Takeaway

Most Flow deployment failures are caused by **activation timing or missing dependencies**.\
Deploying Flows inactive and activating them after deployment resolves the majority of issues.

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;
