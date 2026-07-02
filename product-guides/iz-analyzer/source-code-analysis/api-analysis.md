# API Analysis

## API Analysis

### Overview

In an API and micro services world, quality of the deliverable becomes paramount – since a weak link can break the whole chain.

Now with API Analyzer plugin, APIs can be quality tested in an automated manner. Make sure that only the quality integration without security issues/vulnerability will make it through the quality gate. API Analyzer plugin supports scanning multiple APIs within the same project. Supported versions include:

* RAML 0.8
* RAML 1.0
* OAS / Swagger 2.0
* OAS 3.0

### Analyzing or Scanning APIs

API projects can be scanned for issues using any of the following approaches:

1. Anypoint Studio plugin - Get the results in real time as when the APIs are being developed.
2. Sonar Scanner - API projects can be scanned using sonar scanner to view the scan results in web dashboard.

### Choosing between multiple APIs

If a project contains multiple APIs, all the available APIs will be scanned. There might be certain scenarios where you need to scan specific APIs instead of all. Specific APIs can be included or excluded by using **`analyzer-apis.json`** file. Create a file called **`analyzer-apis.json`** in the project root directory and specify the required APIs to be scanned.

In the example below, only api\_1.raml and api\_2.raml will be considered during analysis.

```json
{
  "apis": [
    "relative/path/to/api_1.raml",
    "relative/path/to/api_2.raml"
  ]
}
```

### See Also

* [Code Analysis In Server](../../integral-zone/iz-analyzer/manage-server-plugin/install-server-plugin.md)
