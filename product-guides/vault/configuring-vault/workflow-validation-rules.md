# Workflow/Validation Rules

### What are validation rules? <a href="#what-are-validation-rules" id="what-are-validation-rules"></a>

Salesforce allows defining several rules on objects and fields, such as validation rules, workflow rules, process builder flows, assignment rules, escalation rules, auto-response rules, and triggers.

**Validation rules** ensure that the data entered into a record meets the defined standards before the record can be saved. These rules help enforce business rules at the data-entry level.

A validation rule consists of:

- **Formula** — A logical expression to evaluate the business condition. If it returns `TRUE`, an error is triggered.
- **Error Message** — Displayed to users when the validation rule fails.
- **Location** — Defines where the error message appears (either at the top of the page or below the relevant field).

### How Salesforce processes validation rules <a href="#how-salesforce-processes-validation-rules" id="how-salesforce-processes-validation-rules"></a>

Salesforce processes rules in the following order:

1. Validation Rules  
2. Assignment Rules  
3. Auto-response Rules  
4. Workflow Rules  
5. Escalation Rules

### What are workflow rules? <a href="#what-are-workflow-rules" id="what-are-workflow-rules"></a>

Workflow rules are business logic containers that automate actions based on specific criteria. When criteria are met, predefined actions execute. If not, the record is saved with no additional action.

> **Example:** If it’s raining, then wear a raincoat.

**Structure of a Workflow Rule:**

<figure>
  <img src="../../../.gitbook/assets/image (138).png" alt="Structure of a Workflow Rule in Salesforce" width="393">
  <figcaption>Workflow Rule Components</figcaption>
</figure>

#### Workflow Components <a href="#workflows-components" id="workflows-components"></a>

1. **Criteria** — Conditions to test a record (like the `if` condition).
2. **Actions** — Events triggered when the criteria are met (like the `then` condition).

### Disabling Salesforce triggers, workflows, and validations when working with Vault <a href="#disabling-salesforce-triggers-workflows-and-validations-when-working-with-vault" id="disabling-salesforce-triggers-workflows-and-validations-when-working-with-vault"></a>

To ensure smooth backup or recovery with Vault, it may be necessary to disable certain automated Salesforce features.

#### Workflow Rules

Workflow rules can be disabled during **EZ-Restore** operations in Vault.

#### Triggers and Process Builder Flows

These must be disabled directly in Salesforce.

{% hint style="info" %}
**Note:** Workflow Rules, Validation Rules, and Triggers associated with managed packages cannot be disabled, either manually or automatically.
{% endhint %}
