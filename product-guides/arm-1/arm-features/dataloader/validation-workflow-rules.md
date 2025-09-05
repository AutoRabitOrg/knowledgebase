# Validation / Workflow Rules

### Validation Rules: Overview <a href="#validation-rules-overview" id="validation-rules-overview"></a>

Validation rules ensure that data entered into a Salesforce record meets specific criteria before saving. These rules are composed of a formula or expression that evaluates one or more fields and returns **True** (invalid) or **False** (valid). When a rule returns True, a specified error message is shown to the user.

***

#### Disable Validation Rules & Workflow Rules

When running a Data Loader job, both the validation rules and workflow rules can be disabled.

* **Validation Rules** – All validation rules associated with the relevant Salesforce objects are temporarily deactivated, allowing data migration without validation errors. Once migration completes, the rules are automatically reactivated.
* **Workflow Rules** – Similarly, all workflow rules are temporarily disabled to ensure smooth data transfer without unintended triggers. After migration, ARM restores these workflows to their active state.

This combined option ensures uninterrupted data migration while preserving the integrity of Salesforce configurations by reactivating both validation and workflow rules post-migration.

<figure><img src="../../../../.gitbook/assets/WorkflowValidation Rules - Validation Rules - 1.png" alt=""><figcaption></figcaption></figure>

Starting with ARM version 20.1, all validation rules are listed in the ARM UI. Users may review and manually re-enable rules as needed.

<figure><img src="../../../../.gitbook/assets/WorkflowValidation Rules - 2.png" alt=""><figcaption></figcaption></figure>

**Screen 1: Successful Validation/Workflow Rule Execution**

<figure><img src="../../../../.gitbook/assets/WorkflowValidation Rules - 3.png" alt=""><figcaption></figcaption></figure>

**Screen 2: Failed Validation/Workflow Rule Execution**

<figure><img src="../../../../.gitbook/assets/WorkflowValidation Rules - 4.png" alt=""><figcaption></figcaption></figure>

***



