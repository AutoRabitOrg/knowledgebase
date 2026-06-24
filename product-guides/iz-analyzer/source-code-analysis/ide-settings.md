# IDE Settings

{% hint style="warning" %}
* This feature is available only in Anypoint Studio Plugin version 5.1.3 and Anypoint Code builder version 1.0.8
{% endhint %}

Configuration to control the projects that are being scanned from the IDE

1. Navigate to **`Administration`** -> **`Mule`**.
2. Search for **`Project/Rule Settings`** and add the following settings to exclude or include the projects -
   1. **`PROJECT_NAME_INCLUDE_PATTERN`** - For example .\* to scan all projects from being scanned
   2. **`PROJECT_NAME_EXCLUDE_PATTERN`** - For example .\* to exclude all projects from being scanned
3. Multiple patterns can be configured by using "\~" as a separator.

### See Also

* [Code Analysis In Server](../install/install-iz-analyzer-server-plugin.md)
