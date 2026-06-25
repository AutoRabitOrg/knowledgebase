# On-Prem vs. Cloud

## On-Premises vs Cloud Offering

Based on the requirements, each organization can choose between the Cloud and On-Premises versions. Table below describes the features available in each of the versions:

### On-Premises Installation

IZ Analyzer Server Plugin will be distributed through the appropriate release channel ([IZ Releases](https://support.integralzone.com)), which can be installed on the [SonarQube™](https://www.sonarqube.org) server maintained by the Organization.

A license key will be provided as part of the onboarding process, which has to be configured as part of initial setup.

{% hint style="info" %}
Systems from which the source code analysis will be invoked from should be able to communicate with IZ License Manager to validate the license (For example: a Jenkins instance).
{% endhint %}

### Features

| **`Feature`**                       | **`Cloud`**                                                                                                                             | **`On Premises`**                                                                                                                                      |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Organization                        | Segregate Projects, Quality Profiles, Quality Gates for each organization                                                               | Not Supported                                                                                                                                          |
| Private & Public Projects           | Projects can be marked as private where only the organization members will have access to. Public projects will be visible to every one | All projects are available/visible to members who have access                                                                                          |
| Maintenance & Upgrades              | No overhead of server maintenance. All upgrades/patches will be deployed automatically                                                  | Need to manage your own on-prem [SonarQube™](https://www.sonarqube.org) server and manually install patches or upgrade servers                         |
| IZ Analyzer Server Plugin           | All plugin updates will be deployed automatically                                                                                       | Plugin updates can be downloaded from [IZ Releases](https://support.integralzone.com) and deployed to [SonarQube™](https://www.sonarqube.org) instance |
| SSO Integration                     | Supports integration of any organization specific SAML/OpenID SSO apart from the default Bitbucket, GitHub, Google & Azure cloud logins | Users can use any existing opensource plugins or develop custom plugins to integrate organization specific SAML/OpenID SSO                             |
| New/Custom Rule Creation            | Supported                                                                                                                               | Supported                                                                                                                                              |
| Activate/De-activate built-in rules | Supported                                                                                                                               | Supported                                                                                                                                              |
| Anypoint Studio Plugin              | Supported                                                                                                                               | Supported                                                                                                                                              |

### See Also

* [Code Analysis In Anypoint Studio](source-code-analysis/code-analysis-in-studio.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
