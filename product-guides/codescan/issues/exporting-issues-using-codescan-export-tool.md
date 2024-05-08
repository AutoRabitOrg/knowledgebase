# Exporting Issues using CodeScan-Export Tool

This guide will walk you through the steps necessary to export a **.CSV** report of your project's issues.

#### Requirements: <a href="#requirements" id="requirements"></a>

* A Bash terminal (such as Git Bash)
* The [codescan-export tool](https://www.npmjs.com/package/codescan-export) (This can be acquired through Node.JS or git)
* Your CodeScan credentials:
  * [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)
  * [Project Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)
  * [Security Token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)

The plug-in can be used by simply calling it from the CLI and feeding it with the required parameters.

Enter the following command to see a list of options.

```
codescan-export -h
```

**Example, usage of the plugin to pull all issues:**

{% code overflow="wrap" fullWidth="false" %}
```
codescan-export MyOrganizationKey MyProjectKey --token=MyToken -f C:/MyDirectory/MyFileName.csv
```
{% endcode %}

**Example, usage of the plugin to pull all issues with the severity of blocker or critical:**

{% code overflow="wrap" %}
```
codescan-export MyOrganizationKey MyProjectKey --token=MyToken --types=BUG --severities=BLOCKER,CRITICAL -f C:/MyDirectory/MyFileName.csv
```
{% endcode %}

**The following video will provide you with step-by-step instructions for exporting issues:**

{% file src="../../../.gitbook/assets/Codescan_exporttool.mp4" %}
