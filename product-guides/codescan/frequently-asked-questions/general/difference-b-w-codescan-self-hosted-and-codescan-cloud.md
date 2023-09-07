# Difference b/w CodeScan Self-Hosted and CodeScan Cloud

Most of the differences between CodeScan Cloud and Self Hosted lie in the integration types and scanning options available.

<table data-full-width="false"><thead><tr><th>Feature</th><th>CodeScan Self-Hosted</th><th>CodeScan Cloud</th></tr></thead><tbody><tr><td><strong>Requirements</strong></td><td>Hosted SonarQube™ server</td><td>None</td></tr><tr><td><strong>Branch Analysis</strong></td><td>Requires SonarQube™ Developer edition</td><td>Yes</td></tr><tr><td><strong>Reporting</strong></td><td>Requires SonarQube™ Enterprise edition</td><td>Yes</td></tr><tr><td><strong>GitHub Integration</strong></td><td>Requires ARM/ Salesforce CLI and other CI tools</td><td>Yes</td></tr><tr><td><strong>Bitbucket Integration</strong></td><td>Requires ARM/ Salesforce CLI and other CI tools</td><td>Yes</td></tr><tr><td><strong>Salesforce Integration</strong></td><td>Requires ARM/ Salesforce CLI and other CI tools</td><td>Yes</td></tr><tr><td><strong>Generic Git Integration</strong></td><td>Requires ARM/ Salesforce CLI and other CI tools</td><td>Yes</td></tr><tr><td><strong>480+ Included Rules for Salesforce</strong></td><td>Yes</td><td>Yes</td></tr><tr><td><strong>Custom Rules</strong></td><td>Yes</td><td>Yes</td></tr><tr><td><strong>VS Code/IntelliJ Plugin</strong></td><td>Yes</td><td>Yes</td></tr></tbody></table>

On CodeScan Cloud, all scanning are done from the GUI. The tool integrates with your version control/Salesforce orgs to pull the metadata and scan it on our server.

On Self-hosted, the metadata collection and scanning are completed by an external scanner and pushed to the SonarQube™ dashboard. This can be accomplished with **AutoRABIT's ARM**, **CodeScan’s Salesforce CLI** plugin or **SonarQube™’s own SonarScanner**.

Your edition of SonarQube™ also limits the features. SonarQube™ provides a free and open-source version and multiple tiers of paid versions. Please ensure that the version you choose to use has the features you need.

Platform API endpoints are very similar but are also subject to the version and the edition of SonarQube™ you are using.

Note:

**SonarQube™** documentation can be found at [https://docs.sonarqube.org](https://docs.sonarqube.org/) and has information on current integrations and analysis options with a self-hosted installation.
