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

- Flows can create, edit, and delete records passed into them—even unrelated records.
- Flows can be scheduled to run at set intervals for collections of records.
- Unlike workflow rules, which can only update related records, flows offer more flexibility and broader actions.
- Compared to Process Builder, flows can also delete records and provide UI elements.

### Flows vs. Process Builder vs. Workflows vs. Apex

| Feature | Flows | Process Builder | Workflows | Apex |
|--------|-------|------------------|-----------|------|
| **Capabilities** | Automate complex logic, manipulate records, interact with external systems, offer UIs (Screen Flows) | Automate record changes and external interactions (background only) | Automate field updates, limited interaction with external systems | Automate any business logic programmatically |
| **Interface** | Flow Builder (UI) | Process Builder (UI) | Wizard-style setup | Code (Developer Console or IDE) |
| **Flexibility** | High | Moderate | Limited | Unlimited |
| **Execution** | Foreground and background | Background only | Background only | Background or UI via LWC/Visualforce |

### Activate or Deactivate a Flow

Only one version of a flow can be active at a time. When a new version is activated, any previously active version is deactivated automatically.

**Deployment Note:** The flow and its latest definition must be included in the deployment package to deactivate it in Salesforce.

### What is a Flow Interview in Salesforce?

A flow interview is a running instance of a flow. For example, a flow may serve as a call script for customer support. As the user interacts with it, Salesforce captures the input and executes the defined actions. Whether accessed via a link, button, or tab, a flow interview represents a single execution of that flow logic.
