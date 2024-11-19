# Workflow/Validation Rules

### What are validation rules? <a href="#what-are-validation-rules" id="what-are-validation-rules"></a>

Salesforce has a bunch of rules that can be defined on objects and fields. For example, you can define validation rules, workflow rules, process builder, flows, assignment rules, escalation rules, auto-response rules, triggers etc.

Validation rules verify that the data a user enters in a record meets the standards you specify before the user can save the record. These validation rules help ensure that any record being created or updated qualifies to defined business rules. If not, then developers/ administrators can display required error message.

Validation rule constitutes of:

* **Formula** — formula to evaluate business rule. If formula evaluates to **TRUE**, validation error is thrown, else it’s considered as validation success
* **Error message** — error message to be displayed on validation failure
* **Location** — Enables admin/ developer to define location to display validation error. In standard page layouts, it’ll allow user to show error either at page top or beneath the selected field.

### How Salesforce processes validation rules? <a href="#how-salesforce-processes-validation-rules" id="how-salesforce-processes-validation-rules"></a>

There are five types of rules in salesforce and the priority of each rule is according to their order.\
Salesforce processes rules in the following order.

1. Validation Rules
2. Assignment Rules
3. Auto-response Rules
4. Workflow Rules
5. Escalation Rules

### What are workflow rules? <a href="#what-are-workflow-rules" id="what-are-workflow-rules"></a>

Workflow rules is basically a container or business logic engine which automates certain actions based on particular criteria. If the criteria are met, the actions get executed. When they are not met, records will get saved but no action will get executed.

> **For example:** If it’s raining, then wear a raincoat.

Below is the basic structure of a workflow rule in Salesforce:

<figure><img src="../../../.gitbook/assets/image (138).png" alt="" width="393"><figcaption></figcaption></figure>

#### Workflow Components <a href="#workflows-components" id="workflows-components"></a>

Workflow rules can be broken down into two main components:

1. **Criteria:** Criteria are conditions you are supposed to put in order to test a record. For example, if you’re from a technical background, what the if statement does in an if/then condition is what criteria mean in a workflow.
2. **Actions:** Actions occur after a record meets the criteria. Again, what the then statement does in the if/then condition is what an action means in the workflow.

### Disabling Salesforce triggers, workflows and validations when working with Vault <a href="#disabling-salesforce-triggers-workflows-and-validations-when-working-with-vault" id="disabling-salesforce-triggers-workflows-and-validations-when-working-with-vault"></a>

When working with Vault, you may want to disable any automated processes or validation rules you have in place to guarantee a successful backup or recovery operation.

#### Validation Rules <a href="#validation-rules" id="validation-rules"></a>

You can disable validation rules while working with [EZ-Restore](../vault-features/restore/restoring-the-metadata-data-to-the-salesforce-org.md) operation in Vault. During EZ-Restore, select the data and metadata that contains the rule you want to disable and then turn off the validation rules.

During this operation, all the validation rules of the Salesforce components are deactivated, and the data gets transferred from the source to the destination sandbox. Once the restore is completed, validation rules will be activated automatically.

#### Workflow Rules <a href="#workflow-rules" id="workflow-rules"></a>

Similar to validation rules, you can disable workflow rules while working with an **EZ-Restore** operation in Vault.

{% hint style="info" %}
**Important Note:** Workflow / Validation rules are not supported for **managed packages** at this time.
{% endhint %}

#### Triggers and Process Builder Flow <a href="#triggers-and-process-builder-flow" id="triggers-and-process-builder-flow"></a>

Triggers and Process Builders Flows must be controlled directly from the Salesforce environment.
