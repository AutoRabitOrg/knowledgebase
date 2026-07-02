# Migrating to Version 2.0

### What’s new in 2.0

IZ Analyzer 1.5 and below had a single plugin (iz-analyzer-server-plugin-1.x) to scan both MuleSoft projects and APIs (RAML & OAS). With IZ Analyzer 2.0 and above, scanner plugin will be available in 2 flavors:

1. MuleSoft project scanner (mule-analyzer-plugin) - To scan MuleSoft configuration files & properties
2. API project scanner (api-analyzer-plugin) - To scan APIs, which include RAML & OAS

Details for migrating from 1.x version to 2.x can be found below for various deployment options -

### On-Premises Users

1. Navigate to **`SONAR_HOME/extensions/plugins`** remove the old version of plugin (iz-analyzer-server-plugin-x.x.jar)
2. Download the latest versions on Mule and API Analyzer plugins from [Releases](https://support.integralzone.com)
3. Copy the latest plugin jar files (mule-analyzer-plugin-x.x.jar & api-analyzer-plugin-x.x.jar) to **`SONAR_HOME/extensions/plugins`**
4. Restart [SonarQube™](https://www.sonarqube.org) server
5. Update Anypoint Studio plugin by following the document [here](../integral-zone/iz-analyzer/manage-anypoint-studio-plugin/update-plugin.md)

### Cloud Users

1. All migration/deployment related activities will be managed by [Integral Zone](https://integralzone.com).
2. All cloud users are only required to update the Anypoint Studio plugin by following the document [here](../integral-zone/iz-analyzer/manage-anypoint-studio-plugin/update-plugin.md)

### API Rules

All built-in API rules will now be available as part of API plugin under Quality Profile **`Analyzer API Rules`**, instead of Mule plugin. Any custom API rules have to be deactivated in Mule language profile and created in API language profile.

### See Also

* [Update IZ Analyzer Anypoint Studio Plugin](../integral-zone/iz-analyzer/manage-anypoint-studio-plugin/update-plugin.md)
* [Remove IZ Analyzer Anypoint Studio Plugin](../integral-zone/iz-analyzer/manage-anypoint-studio-plugin/remove-plugin.md)
