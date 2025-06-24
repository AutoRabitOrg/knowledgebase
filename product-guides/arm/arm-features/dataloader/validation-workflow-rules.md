# Validation / Workflow Rules

### Validation Rules: Overview <a href="#validation-rules-overview" id="validation-rules-overview"></a>

Validation rules ensure that data entered into a Salesforce record meets specific criteria before saving. These rules are composed of a formula or expression that evaluates one or more fields and returns **True** (invalid) or **False** (valid). When a rule returns True, a specified error message is shown to the user.

---

#### Disable Validation Rules <a href="#disable-validation-rules" id="disable-validation-rules"></a>

When the **Disable validation rules** checkbox is selected during a Data Loader job, all validation rules associated with the relevant Salesforce objects are temporarily deactivated. Data is then migrated to the destination sandbox. Once migration is complete, the validation rules are reactivated automatically.

<figure><img src="../../../../.gitbook/assets/image (1131).png" alt="Checkbox UI to disable validation rules in Data Loader"></figure>

Starting with ARM version 20.1, all validation rules are listed in the ARM UI. Users may review and manually re-enable rules as needed.

<figure><img src="../../../../.gitbook/assets/image (1132).png" alt="List of validation rules in ARM interface"></figure>

**Screen 1: Successful Validation Rule Execution**

<figure><img src="../../../../.gitbook/assets/image (1133).png" alt="Validation rules that executed successfully"></figure>

**Screen 2: Failed Validation Rule Execution**

<figure><img src="../../../../.gitbook/assets/image (1134).png" alt="Validation rules that failed execution"></figure>

---

### Workflow Rules: Overview <a href="#workflow-rules-overview" id="workflow-rules-overview"></a>

Workflow rules automate standard processes and procedures. They typically follow an **if/then** logic model—triggering actions when specified conditions are met.

---

#### Disable Workflow Rules <a href="#disable-workflow-rules" id="disable-workflow-rules"></a>

Selecting the **Disable workflow rules** checkbox during the [Data Loader job](https://www.autorabit.com/wp-content/uploads/2020/12/Salesforce-Data-Loader-1.pdf) will deactivate all applicable Salesforce workflow rules during data migration. After the migration is complete, ARM reactivates the workflows.

<figure><img src="../../../../.gitbook/assets/image (1135).png" alt="UI showing workflow rules disable checkbox"></figure>

Similar to validation rules, ARM also displays all workflow rules, allowing users to re-enable them if needed.

<figure><img src="../../../../.gitbook/assets/image (1136).png" alt="List of workflow rules in ARM UI"></figure>

**Screen 1: Successful Workflow Rule Execution**

<figure><img src="../../../../.gitbook/assets/image (1137).png" alt="Successfully executed workflow rules"></figure>

**Screen 2: Failed Workflow Rule Execution**

<figure><img src="../../../../.gitbook/assets/image (1138).png" alt="Workflow rules that failed execution"></figure>
