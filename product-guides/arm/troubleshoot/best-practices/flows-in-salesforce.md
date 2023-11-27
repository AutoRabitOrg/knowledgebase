# Flows in Salesforce

### What is a flow? <a href="#what-is-a-flow" id="what-is-a-flow"></a>

In Salesforce, a flow is an application that automates complex business processes. Simply put, it collects data and then does something with that data. Flows help you automate complex business processes and manual data entry. Flows let you work smarter, not harder, by saving your users time and making sure the required tasks are accomplished correctly.

### Different Categories of Flows <a href="#different-categories-of-flows" id="different-categories-of-flows"></a>

Flows fall into five categories:&#x20;

1. **Screen Flows:** These are flows that have a UI element and require input from users. These types of flows are either launched as an action or embedded as an element on a Lightning page.
2. **Schedule-Triggered Flows:** These auto-launched flows launch at a specified time and frequency for each record in a batch, and they run in the background.
3. **Autolaunched Flows:** Run automated tasks with this flow type. Auto-launched flows can be invoked from a process builder, from within an Apex class, from a set schedule, from record changes, or from platform events.
4. **Record-Triggered Flows:** These auto-launched flows run in the background when a record is created, updated, or deleted.
5. **Platform Event-Triggered Flows:** When a platform event message is received, these auto-launched flows run in the background.

### When and why should I use a flow? <a href="#when-and-why-should-i-use-a-flow" id="when-and-why-should-i-use-a-flow"></a>

* Flows are able to create, edit, and delete any record passed into the flow. Records do not have to be related in order to pass data in a flow. Flows can also be scheduled to run at a set interval with a collection of records.
* The workflow field update can write data to the same record that invoked the workflow rule, or to the master record of a master-detail relationship on the record that invoked the rule. Workflow rules are not able to create, edit, or delete records.
* Processes, created in the Process Builder, can write data to the same record that invoked the process, or to records related by either lookup or master-detail relationships. Processes can also create records, but they cannot delete them.

### Flows vs Process Builder vs Workflows vs Apex <a href="#flows-vs-process-builder-vs-workflows-vs-apex" id="flows-vs-process-builder-vs-workflows-vs-apex"></a>

| Flows                                                                                                                                                                                                                                                                                                                                                                                          | Process Builder                                                                                                                                                                                                                                                                                                                                            | Workflows                                                                                                                                                                                                                                                                 | Apex                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flows** automate business processes to collect, update, edit, create, or delete Salesforce records as well as interact with external systems. Flows can either run in the background( autolaunched flows) or provide a user interface( screen flows). Flows offer great flexibility and are managed in the declarative and interactive Flow Builder UI. Flows are powered by Lightning Flow. | **Process Builder** automates business processes to collect, update, edit or create delete Salesforce records as well as interact with external systems. Processes always run in the background. Processes offer moderate flexibility and are managed in the declarative and interactive Process Builder UI. Process Builder is powered by Lightning Flow. | **Workflows** automate business processes to update Salesforce records as well as interact with external systems in a limited manner. Workflows always run in the background. Workflows offer limited flexibility and are managed in a declarative wizard-like interface. | **Apex** automates any imaginable business processes within Salesforce and can interact with external systems in various ways. Apex runs in the background and can offer user interfaces via Lightning (Web) Components or Visualforce Pages. Apex offers unlimited flexibility due to its programmatic manner and is managed within the Developer Console or any IDE. |

### Activate or Deactivate a Flow <a href="#activate-or-deactivate-a-flow" id="activate-or-deactivate-a-flow"></a>

You can have multiple versions of a flow in Salesforce, but only one version of each flow can be active at a time. When you activate a flow version, the previously activated version (if one exists) is deactivated.

**Deactivate a flow:** The last flow definitions, as well as the flow, should be included in the deployment package when deactivating a flow in Salesforce.

### What is a flow interview in Salesforce? <a href="#what-is-a-flow-interview-in-salesforce" id="what-is-a-flow-interview-in-salesforce"></a>

While a flow is an application built by your administrator that asks you for inputs and does something in Salesforce based on those inputs, a flow interview is a running instance of a flow. For example, a flow could provide a call script for customer support calls using the information you provided to create a case. What the flow does with the information you provide is entirely up to your administrator. When you run a flow interview, whether, through a link, button, or tab, you’re running a single instance of a flow.