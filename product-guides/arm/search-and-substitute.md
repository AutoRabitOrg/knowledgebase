# Search and Substitute

This article is for **Org Administrators** in particular. The actions discussed in the article are not available to general users.

### Overview <a href="#overview" id="overview"></a>

The Search and Substitute rules feature allows you to define custom find and substitute rules that ARM applies whene you commit and deploy files from one sandbox to another sandbox, one sandbox to Version Control, or vice-versa.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account.
2.  Hover your mouse over the **`Admin`** module and click on the **`Search and Substitute`** option.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667886922752.png" alt="" width="375"><figcaption></figcaption></figure>
3.  Click on **`Create Rule`**. A rule consists of a rule label and several rule parameters.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667886980268.png" alt=""><figcaption></figcaption></figure>

#### Rule Parameters <a href="#rule-parameters" id="rule-parameters"></a>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667887074828.png)

**1. Metadata Type**

Until now, Search and Substitute could only be used to select a metadata type and then perform the search for substrings across all members in that type. Now, however, you can choose specific metadata members in a type and substitute values for the member(s).

**Use Cases:**

* If you have a **custom label** in one of your orgs with identical values across multiple labels, but you only want to change one of those values, then having the ability to search for a specific label and apply substitution rules will help.
* Suppose you need to add a few object permissions, but only to the Production environment and not the lower sandboxes. In that case, you can now do so instead of manually commenting out some metadata in the **Permission Set** file during **sandbox deployments** and then uncommenting them before a Production deployment.
* The rules can be created and used in **CI Jobs** to make the replacements automatically, depending on the **deployment settings** in the CI Job.

Supported Metadata TypesBelow is an updated list of all the metadata types compatible with the enhanced Search and Substitute functionality.

* AutoResponseRule
* CustomLabel
* CustomMetadata
* CustomObject
* CustomSite
* Dashboard
* DashboardFolderShare
* Network
* NamedCredential
* PermissionSet
* Portal
* Queue
* RemoteSiteSettings
* Report
* ReportFolderShare
* SamlSsoConfig
* SharingCriteriaRule
* SharingOwnerRule
* Workflow

**2. Sub Element**

The element for which you want to substitute the character.

**3. Criteria**

The text you want to replace.

**4. Substitute**

The value that will replace the text.

To substitute multiple values, click on the '+' icon to add more field parameters. Note that you can only add up to **5 parameters** for a rule; anything beyond that, the application won’t allow you. Also, ensure the parameters are not duplicated, which may fail in search and substitute functionality.

**Example:**

The **'Formatchange'** rule will be applied to the **'CustomObject'** metadata type in the following example. The sub-element is **'Fields.displayFormat',** and the value to be replaced is **'a-{000}'**. The value to replace this with is **'a-{001}'**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402453624.png" alt=""><figcaption></figcaption></figure>

Once you're done creating the rule, click on the **`Save`** button.

The rule will be displayed on the Search and Substitute home screen with an option to edit, delete, or create a new rule to add to the existing rules using the **`clone`** icon.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667887667345.png" alt=""><figcaption></figcaption></figure>

### What's Next? <a href="#whats-next" id="whats-next"></a>

You have successfully created a new rule. The next step is to specify the newly created rule whenever you perform a CI, deployment, or commit operation in ARM.

#### Deploying the changes to a Sandbox with a new rule assigned <a href="#deploying-the-changes-to-a-sandbox-with-a-new-rule-assigned" id="deploying-the-changes-to-a-sandbox-with-a-new-rule-assigned"></a>

While deploying the changes from one sandbox to another sandbox, you can apply the Search and Substitute rule on the **`Deployment Settings`** screen.

From the **`Apply Search and Substitute Rules`** list, select the rule that will be associated with the current deployment process. Use the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402857647.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402882169.png) button to add or remove the rule and use the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402900576.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402922812.png) button to move the rules list up and down. Based on the selection, the top rule is deployed initially, and the process continues for the remaining rules.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402780152.png" alt=""><figcaption></figcaption></figure>

#### Committing the changes from one Salesforce org to a Version Control branch with new rules assigned <a href="#committing-the-changes-from-one-salesforce-org-to-a-version-control-branch-with-new-rules-assigned" id="committing-the-changes-from-one-salesforce-org-to-a-version-control-branch-with-new-rules-assigned"></a>

While committing the metadata component changes to a Version Control Branch, you can apply the Search and Substitute rule on the **Commit** or **Submit for Validation** screen. Refer to the Commit topic for the detailed commit process.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613416059664.png" alt=""><figcaption></figcaption></figure>

#### Performing CI Job with new rule assigned <a href="#performing-ci-job-with-new-rule-assigned" id="performing-ci-job-with-new-rule-assigned"></a>

While committing the metadata component changes from a Salesforce org to a Version Control branch using CI job, you can apply the Search and Substitute rule in the **`Create CI Job`** screen under the **`Deploy`** section.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613416165848.png" alt=""><figcaption></figcaption></figure>
