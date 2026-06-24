# Manage Rules

## About Managing Rules

IZ Analyzer manages all the rules centrally in the server, which in turn will be accessed by:

1. **`On The Fly Results`** in Anypoint Studio Plugin
2. Project analysis using **`Scanner Plugin`** or **`Maven Plugin`**

Users with appropriate access can activate or deactivate the rules.

Some of the key benefits are:

* Centralized management of rules for the whole organization
* Automatic rule synchronization in Anypoint Studio from server
* Rules can also be synced manually in Anypoint Studio using **`Sync Rules From Server`** option in **`On The Fly Results Pane`** tab pane

### Activating Rules

At any point in time, deactivated rules can be activated from [SonarQube™](https://www.sonarqube.org) server. All the new activated rules will be synced by Anypoint Studio plugin at regular intervals.&#x20;

### Deactivating Rules

At any point in time, an activated rule can be deactivated from [SonarQube™](https://www.sonarqube.org) server. Deactivated rules will not be applied while scanning the project.

### Custom Rules

Custom rules can be created using simple groovy scripts to add additional rules complying with organizational standards.

### See Also

* [Activate Rules](activate-rules.md)
* [Deactivate Rules](deactivate-rules.md)
* [Custom Rules](custom-rules.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
