# CodeScan Rule List

The CodeScan rule list is always expanding. You can view the complete current list in the latest file below.

Our [Release Notes](../../../release-notes/release-notes/codescan-release-notes/) also have a record of when certain rules were added.

You can download the list of CodeScan rules from here (last updated 17 June 2025):&#x20;

{% file src="../../../.gitbook/assets/CodeScan Rules List 6-17-25.xlsx" %}

### Rules Not Available for On-Premises Applications

Please note that not all rules available on CodeScan Cloud are available in the Self-Hosted CodeScan version. For example, the following rules will not function on CodeScan Self-Hosted:

* Limit number of Custom Profiles with Modify All Data Permission (sfmeta:CustomProfilesPermission)
* Limit number of Page Layouts per object (sfmeta:ExcessivePageLayout)
* Limit number of Custom Fields per object (sfmeta:LimitCustomFields)
* Limit number of System Administrators(sfmeta:CheckSystemAdministrator)

These rules require a direct connection to the Salesforce environment to execute queries.

For a complete list of rules limited to CodeScan Cloud, see the file below:

{% file src="../../../.gitbook/assets/CodeScan_Cloud_Only_Rules_24_0_4 (2).xlsx" %}

{% hint style="warning" %}
**Note:** These rules do not apply to the plugin for on-prem as they will not function.
{% endhint %}
