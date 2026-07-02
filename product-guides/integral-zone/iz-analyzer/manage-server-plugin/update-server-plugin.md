# Update Server Plugin

{% hint style="warning" %}
Taking a backup of the current database before upgrading plugins is strongly advised.
{% endhint %}

### Update Plugin:

1. Go to **`SONAR_HOME/extensions/plugins`** to remove the old version of plugins. Either api-analyzer-plugin-x.x.jar or mule-analyzer-plugin-x.x.jar.
2. Copy the latest plugin jar files (either api-analyzer-plugin-x.x.jar or mule-analyzer-plugin-x.x.jar) to **`SONAR_HOME/extensions/plugins` .**
3. Restart [SonarQube™](https://www.sonarqube.org) server.

{% hint style="info" %}
* **`SONAR_HOME`** refers to [SonarQube™](https://www.sonarqube.org) server installation path
{% endhint %}

### See Also

* [Install IZ Analyzer Server Plugin](../../iz-suite/iz-scan/anypoint-studio/installation/install-plugin.md)
* [Remove IZ Analyzer Server Plugin](../../iz-suite/iz-scan/anypoint-studio/installation/remove-plugin.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
