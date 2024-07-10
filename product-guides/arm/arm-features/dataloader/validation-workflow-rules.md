# Validation / Workflow Rules

### Validation Rules: Overview <a href="#validation-rules-overview" id="validation-rules-overview"></a>

Validation rules verify that the data a user enters in a record meets the specified standards before the user can save the record. A validation rule can contain a formula or expression that evaluates the data in one or more fields and returns a value of **True** or **False**. Validation rules also include an error message to display to the user when the rule returns a True value due to an invalid value.&#x20;

#### Disable Validation Rules <a href="#disable-validation-rules" id="disable-validation-rules"></a>

When you select the **`Disable validation rules`** checkbox during the dataloader job, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are activated automatically.

<figure><img src="../../../../.gitbook/assets/image (1131).png" alt=""><figcaption></figcaption></figure>

From ARM version 20.1 onwards, ARM lists all the validation rules set. The ARM user interface (UI) lists all the validation rules, and users must enable them for the disabled validation rules (if required).

<figure><img src="../../../../.gitbook/assets/image (1132).png" alt=""><figcaption></figcaption></figure>

**Screen 1: Succeed Validation Rules**

<figure><img src="../../../../.gitbook/assets/image (1133).png" alt=""><figcaption></figcaption></figure>

**Screen 2: Failed Validation Rules**

<figure><img src="../../../../.gitbook/assets/image (1134).png" alt=""><figcaption></figcaption></figure>

### Workflow Rules: Overview <a href="#workflow-rules-overview" id="workflow-rules-overview"></a>

Workflow lets you automate standard internal procedures and processes to save time across your org. A workflow rule is the main container for a set of workflow instructions. These instructions can always be summed up in an if/then statement.&#x20;

#### Disable Workflow rules <a href="#disable-workflow-rules" id="disable-workflow-rules"></a>

When you select the **`Disable workflow rules`** checkbox during the [dataloader](https://www.autorabit.com/wp-content/uploads/2020/12/Salesforce-Data-Loader-1.pdf) job, all the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.

<figure><img src="../../../../.gitbook/assets/image (1135).png" alt=""><figcaption></figcaption></figure>

Similar to **`Disable validation rules`**, ARM has options to list the set workflow rules. The UI lists all the workflow rules, and users must enable them for the disabled workflow rules.

<figure><img src="../../../../.gitbook/assets/image (1136).png" alt=""><figcaption></figcaption></figure>

**Screen 1: Succeed Validation Rules**

<figure><img src="../../../../.gitbook/assets/image (1137).png" alt=""><figcaption></figcaption></figure>

**Screen 2: Failed Validation Rules**

<figure><img src="../../../../.gitbook/assets/image (1138).png" alt=""><figcaption></figcaption></figure>
