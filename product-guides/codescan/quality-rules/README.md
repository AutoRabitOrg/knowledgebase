# CodeScan Rules

CodeScan has a set of metadata rules; these rules allow you to scan your settings to ensure that your org is secure and clean.

CodeScan divides the rules into 4 categories:

* Bug (reliability domain)
* Code Smell (maintainability domain)
* Vulnerability (security domain)
* Security Hotspot (security domain)

For code smells and bugs, zero false positives are expected.

For vulnerabilities, the goal is to have more than 80% of issues be true positives.

Security hotspot rules draw attention to code that is security-sensitive. It is expected that more than 80% of the issues will be quickly resolved as "reviewed" after being evaluated by a developer.

More information on Security-Related Rules can be found [here](https://knowledgebase.autorabit.com/product-guides/codescan/quality-rules/security-related-rules).

{% hint style="warning" %}
Please note that not all rules available on CodeScan Cloud are available in the Self-Hosted CodeScan version. The following rules will not function on CodeScan Self-Hosted:

* Limit number of Custom Profiles with Modify All Data Permission (sfmeta:CustomProfilesPermission)
* Limit number of Page Layouts per object (sfmeta:ExcessivePageLayout)
* Limit number of Custom Fields per object (sfmeta:LimitCustomFields)
* Limit number of System Administrators(sfmeta:CheckSystemAdministrator)



These rules require a direct connection to the Salesforce environment to execute queries.&#x20;
{% endhint %}

### Access Quality Rules <a href="#access-quality-rules" id="access-quality-rules"></a>

You can access the **Quality Rules** page from the Organization’s home page.

By default, you will see all the available rules installed on your CodeScan instance. You have the ability to review and narrow the selection based on search criteria in the left sidebar:

1. **Language:** the language to which a rule applies.
2. **Type:** bug, vulnerability, code smell, or security hotspot rules.
3. **Tag:** it is possible to add tags to rules in order to classify them and to help discover them more easily.
4. **Repository:** the engine/analyzer that contributes rules to CodeScan.
5. **Default Severity:** Filter Quality Rules based on the severity of the rule
6. **Status:** rules can have 3 different statuses:
   * **Beta:** The rule has been recently implemented, and we haven't gotten enough feedback from users yet, so there may be false positives or false negatives.
   * **Deprecated:** The rule should no longer be used because a similar, but more powerful and accurate rule exists.
   * **Ready:** The rule is ready to be used in production.
7. **Available since:** the date when a rule was first added on CodeScan. This is useful to list all the new rules since the last upgrade of a plugin, for instance.
8. **Template:** display the rules created from a template.
9. **Quality profile:** inclusion in or exclusion from a specific profile

### Viewing Quality Rules details <a href="#viewing-quality-rules-details" id="viewing-quality-rules-details"></a>

Click on the rule to see the details of a rule. Along with basic rule data, you'll also be able to see which, if any, profiles the rule is active in and how many open issues have been raised with it.

For each rule, you can:

* **Add or remove existing tags** on a rule
* You can **extend rule descriptions** to let users know how your organization is using a particular rule or to give more insight into a rule.

To make changes to the Quality Rules, users must be granted the _**Administer Quality Gates or Profile**_ permission.

### Create Custom Rules <a href="#create-custom-rules" id="create-custom-rules"></a>

Custom rules are considered like any other rule, except that you can edit or delete them. You can define your own custom rules in CodeScan using Rule templates.\
To find templates, select the **Show Templates Only** option from the **Template** dropdown menu.<br>

<figure><img src="../../../.gitbook/assets/image (7) (1) (3).png" alt="" width="375"><figcaption><p>Show Templates Only</p></figcaption></figure>

To create a custom rule from a template, select **Create** next to the **Custom rules** heading and enter the following information:<br>

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (3) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

* Name
* Key (auto-suggested)
* Type
* Severity
* Status
* Description (Markdown format is supported)
* The parameters specified by the template

### Edit or Delete Custom Rules <a href="#edit-or-delete-custom-rules" id="edit-or-delete-custom-rules"></a>

Unlike other rules, you can edit or delete custom rules. When a custom rule is deleted, it is not removed from the CodeScan Cloud instance. Instead, its status is set to "REMOVED", allowing relevant issues to continue to be displayed properly.

Click on the custom rules to view its details. Under the **Parameter** section, you have the option to edit the custom rule information or delete them.<br>

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (3) (1) (1).png" alt=""><figcaption><p>Custom Test Rule</p></figcaption></figure>
