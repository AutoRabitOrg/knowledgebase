# IZ-Core Rules

## Custom Rule Registry Keywords

{% hint style="info" %}
* Rule definitions for all built-in rules, including Mule, API, and API Instance, will be accessible on the support portal at [Support Portal](https://support.integralzone.com/) after the onboarding process is complete.
* Mule components/configurations stored are GPathResult and NodeChilds from Groovy XML parser. Visit [Groovy XMLSlurper](https://groovy-lang.org/processing-xml.html) for more information.
{% endhint %}

### Registry Keywords - Mule, API

Keywords available for Groovy style rules execution.

| Variable                                                                                                    | Description                                                                                                                                             | Structure .2+                                                 |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| DOCUMENTS .2+                                                                                               | Contains list of all parsed mule xml configuration files                                                                                                | **`Map<String, groovy.util.slurpersupport.GPathResult>`**     |
| COMPONENTS .2+                                                                                              | Contains list of all components/elements across all mule configuration files                                                                            | **`Map<String, List<groovy.xml.slurpersupport.NodeChild> >`** |
| MUNIT\_DOCUMENTS .2+                                                                                        | Contains list of all parsed mule munit xml configuration files                                                                                          | **`Map<String, groovy.xml.slurpersupport.GPathResult>`**      |
| MUNIT\_COMPONENTS .2+                                                                                       | Contains list of all munit components accross all mule munit configuration files                                                                        | **`Map<String, List<groovy.xml.slurpersupport.NodeChild> >`** |
| CONFIGURATIONS .6+                                                                                          | Contains list of all Property/YAML files with their object representation used in the application.                                                      |                                                               |
| **CONFIGURATIONS.get(propertyKey)** - will return values defined for the property key in all property files | **`List<java.lang.Object>`**                                                                                                                            | Eg: **`List<Property Values>`** .2+                           |
| PROJECT\_HANDLE .2+                                                                                         | Contains the default project level file which can be used to mark project/directory level errors. Eg: Project is not mavenized                          | **`File Root Object`**                                        |
| API\_CONFIGURATIONS                                                                                         | Contains the web api instance of the parsed RAML/OAS                                                                                                    | **`Map<MainAPIFilePath, WebAPI>`**                            |
| ANALYSIS                                                                                                    | Can be used to get the project root directory. Eg: ANALYSIS.projectDir would return a java.io.File instance to project directory which is being scanned |                                                               |

### Registry Keywords - API Instance

| Variable               | Description                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API.TIERS              | Json structure representing the tiers information for a specific API Instance     | **`[ { "masterOrganizationId": "xxx", "organizationId": "xxx", "id": 2075526, "name": "Tier 1", "description": null, "limits": [ { "maximumRequests": 1, "timePeriodInMilliseconds": 10000, "visible": true }, { "maximumRequests": 2, "timePeriodInMilliseconds": 45000, "visible": true } ], "status": "ACTIVE", "autoApprove": false, "applicationCount": 0, "apiId": 20070196 } ]`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| API.POLICIES           | Json structure representing the policies information for a specific API Instance  | **`[ { "policyTemplateId": "386072", "order": 1, "pointcutData": null, "type": "system", "policyId": 6198311, "configuration": { "scopeValidationCriteria": "AND", "tokenUrl": "sdasf", "secureTrustStore": false, "exposeHeaders": false, "skipClientIdValidation": false, "authenticationTimeout": 10000 }, "template": { "groupId": "68ef9520-24e9-4cf2-b2f5-620025690913", "assetId": "external-oauth2-access-token-enforcement", "assetVersion": "1.6.0" }, "version": 1733730272393 } ]`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| API.CONFIG             | Json structure representing the API Instance information                          | **`{ "masterOrganizationId": "xxx", "organizationId": "xxx", "id": 20070196, "instanceLabel": null, "groupId": "xxx", "assetId": "shipment-eapi", "assetVersion": "2.0.0", "productVersion": "v1", "description": null, "tags": [], "order": 1, "providerId": null, "deprecated": false, "lastActiveDate": null, "endpointUri": null, "environmentId": "xxx", "isPublic": false, "stage": "release", "technology": "mule4", "status": "unregistered", "endpoint": { "audit": { "created": {}, "updated": {} }, "id": 4605251, "type": "rest", "uri": null, "apiGatewayVersion": null, "proxyUri": null, "proxyRegistrationUri": null, "lastActiveDate": null, "isCloudHub": null, "deploymentType": "CH", "policiesVersion": null, "referencesUserDomain": null, "responseTimeout": null, "wsdlConfig": null, "tlsContexts": null, "muleVersion4OrAbove": true, "apiVersionId": 20070196, "tlsContexts.outbound": null }, "deployment": null, "autodiscoveryInstanceName": "v1:20070196" }`** |
| API.CONTRACTS          | Json structure representing the contracts information for a specific API Instance | **`[ { "masterOrganizationId": "xxx", "organizationId": "xxx", "id": 24, "status": "APPROVED", "approvedDate": "2017-07-19T20:46:22.520Z", "rejectedDate": null, "revokedDate": null, "applicationId": 1, "application": { "audit": { "created": { "date": "2017-07-19T20:46:19.307Z" }, "updated": {} }, "id": 1, "name": "dolor 1", "description": "", "coreServicesId": "xxx", "url": "http://sample-app.com/1" }, "tierId": 48, "tier": { "audit": { "created": { "date": "2017-07-19T20:46:22.197Z" }, "updated": {} }, "id": 48, "name": "magni 48", "description": "xxx", "limits": [ { "maximumRequests": 1000000, "timePeriodInMilliseconds": 1000, "visible": true } ], "status": "DEPRECATED", "autoApprove": true }, "requestedTierId": null, "requestedTier": null, "terms": null, "partyId": null, "partyName": null, "apiId": 25, "api": { "audit": { "created": {}, "updated": {} }, "id": 25 } } ]`**                                                                        |
| API.ALERTS             | Json structure representing the alerts information for a specific API Instance    | **`[ { "apiAlertsVersion": "1.0.0", "api": { "id": 24, "name": "ad 24" }, "condition": { "aggregate": "COUNT", "operator": "GREATER_THAN", "value": 90, "resourceType": "api" }, "createdAt": 1501526157101, "enabled": true, "environmentId": "xxx", "id": "xxx", "lastModified": 1501526157101, "name": "REQUEST COUNT ALERT", "organizationId": "xxx", "period": { "repeat": 5, "duration": { "count": 5, "weight": "DAYS" } }, "recipients": [ { "type": "user", "value": "xxx", "lastName": "Owner", "firstName": "Organization" } ], "severity": "CRITICAL", "type": "api-request-count" } ]`**                                                                                                                                                                                                                                                                                                                                                                                         |
| API.UPSTREAMS          | Json structure representing the upstream information for a specific API Instance  | **`{ "total": 1, "upstreams": [ { "id": "xx", "label": null, "uri": "http://upstream-test.com" } ] }`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| API.GROUP-TIERS        | Json structure representing the alerts information for a specific API Instance    | **`[ { "masterOrganizationId": "xxx", "organizationId": "xxx", "id": 2075526, "name": "Tier 1", "description": null, "limits": [ { "maximumRequests": 1, "timePeriodInMilliseconds": 10000, "visible": true }, { "maximumRequests": 2, "timePeriodInMilliseconds": 45000, "visible": true } ], "status": "ACTIVE", "autoApprove": false, "applicationCount": 0, "apiId": 20070196 } ]`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| API.GROUP-CONTRACTS    | Json structure representing the alerts information for a specific API Instance    | **`{ "total": 2, "contracts": [ { "masterOrganizationId": "xxx", "organizationId": "xxx", "id": 24, "status": "APPROVED", "approvedDate": "2017-07-19T20:46:22.520Z", "rejectedDate": null, "revokedDate": null, "applicationId": 1, "application": { "audit": { "created": { "date": "2017-07-19T20:46:19.307Z" }, "updated": {} }, "id": 1, "name": "dolor 1", "description": "", "coreServicesId": "xxx", "url": "http://sample-app.com/1" }, "tierId": 48, "tier": { "audit": { "created": { "date": "2017-07-19T20:46:22.197Z" }, "updated": {} }, "id": 48, "name": "magni 48", "description": "xxx", "limits": [ { "maximumRequests": 1000000, "timePeriodInMilliseconds": 1000, "visible": true } ], "status": "DEPRECATED", "autoApprove": true }, "requestedTierId": null, "requestedTier": null, "terms": null, "partyId": null, "partyName": null, "apiId": 25, "api": { "audit": { "created": {}, "updated": {} }, "id": 25 } } ] }`**                                           |
| API.AUTOMATED-POLICIES | Json structure representing the alerts information for a specific API Instance    | **`{ "automatedPolicies": [ { "audit": { "created": { "date": "2018-11-23T14:37:08.953Z" }, "updated": {} }, "id": 11, "ruleOfApplication": { "organizationId": "xxx", "environmentId": "xxx", "range": { "from": "4.1.1", "to": "4.3.x" } }, "policyTemplateId": "2", "groupId": "xxx", "assetId": "rate-limiting", "assetVersion": "1.0.0", "configurationData": { "rateLimits": [ { "timePeriodInMilliseconds": 60000, "maximumRequests": 3 } ], "clusterizable": true, "exposeHeaders": true }, "pointcutData": null, "order": null, "disabled": false } ], "total": 1 }`**                                                                                                                                                                                                                                                                                                                                                                                                               |

### Custom Mule Rule Example

* **`Name:`** DATABASE - DB queries SHOULD be externalized
* **`Custom Rule definition:`**

```groovy
def list =[] 
COMPONENTS.get('select')?.each {  
        it.'*'.each { sql -> 
            if(sql.name() == 'sql' && !sql.text().startsWith('${')) { 
                list.add(sql) 
            } 
        } 
    }
return list 
```

### Custom property / YAML Rule Example

* **`Name:`** PROPERTY/YAML FILE - Sensitive data NOT encrypted
* **`Custom Rule definition:`**

```groovy
def response = [:]
def propFiles = [:]
CONFIGURATIONS.getAll().keySet().each { filePath ->
  def list = []
  def props = CONFIGURATIONS.getProps(filePath)
  props.keySet().each { key ->
    if( (key.toLowerCase().contains('pass') ||  key.toLowerCase().contains('secure')) && !props.get(key).startsWith('![')) {
      list.add(key)
    }
  }

    if(!list.isEmpty()) {
     propFiles[filePath] = list
    }
}
response['PROPERTY'] = propFiles
return response
```

### Custom API Rule Example

* **`Name:`** API RESOURCE - Health API NOT defined
* **`Custom Rule definition:`**

```groovy
def response = [:]
def apiErrors = [:]
String healthEndpoint = '/health'

API_CONFIGURATIONS.getResolved().each { filePath, webApi->
  def isDefined = false

    webApi.endPoints().each { endpoint ->
	String name = endpoint.path().value()
	if(name == healthEndpoint) {
		isDefined = true
	}
  }

    if(!isDefined) {
	apiErrors[filePath] = webApi
  }
  
}
response['API'] = apiErrors
return response
```

### Custom API Instance Rule Example

* **`Name:`** API Instance should have atleast 1 SLA Tier defined
* **`Custom Rule definition:`**

```groovy
def response = []

if(API.TIERS == null || API.TIERS?.size() == 0)
    response.add("API should have at least one SLA tier defined")

return response
```

### Debugging Custom Rules

When developing custom rules, there may be scenarios where debugging the values of certain components is required. The following section outlines how to add logs to custom rules to print the desired values.

{% hint style="info" %}
This approach should only be used for debugging purposes. Debug logs must be removed before publishing the rule to the server.
{% endhint %}

Example: Debugging a Custom Rule to Print SQL Query Values

* Assume we need to debug the following custom rule to print the value of an SQL query:

```groovy
def list =[] 
COMPONENTS.get('select')?.each {  
        it.'*'.each { sql -> 
            if(sql.name() == 'sql' && !sql.text().startsWith('${')) { 
                list.add(sql) 
            } 
        } 
    }
return list 
```

* **`Create a Log File:`** Create a file anywhere on the file system for logging. In this example, a log file is created at **`/tmp/iz_custom_rule.log`**
* **`Write Logs:`** Log the required details such as SQL query values.

```groovy
def list =[] 

File logs = new File("/tmp/iz_custom_rule.log")
logs.write('Begin debug\n')

COMPONENTS.get('select')?.each {  
        it.'*'.each { sql -> 
            // 3. Write the configured SQL query to file
            logs &lt;&lt; "SQL text::" + sql.text() + "\n"
            if(sql.name() == 'sql' && !sql.text().startsWith('${')) { 
                list.add(sql) 
            } 
        } 
    }
logs &lt;&lt; "End debug\n"
return list 
```

* **`Checking Logs:`** After adding the debug logs, click on **`Evaluate Rule`**. Review the generated logs in the configured file (e.g., /tmp/iz\_custom\_rule.log).

### See Also

* On The Fly Results
* Rules Playground
