# Public File Exposure

### Overview

The **Public Links – File Exposure** feature in AutoRABIT Guard provides visibility into Salesforce files that are publicly accessible through shared links. This feature helps organizations identify potential data exposure risks by highlighting files that can be accessed outside their Salesforce environment.

With this capability, administrators can quickly review files that have public links enabled and determine whether those links should remain active.

### Key Benefits

* **Improved Data Security:** Identify Salesforce files that are publicly accessible through shared links.
* **Risk Visibility:** Detect files that may expose sensitive data outside the organization.
* **Better Governance:** Monitor public links that may lack expiration controls.
* **Faster Risk Remediation:** Quickly review and manage exposed files.

### Navigation Path

`Guard → Risk → Public File Exposure`

### How It Works

Guard scans Salesforce file-sharing settings and identifies files that have been shared via **public links**. These links allow access to files without requiring authentication.

The **Public File Exposure** view displays a list of such files along with key details that help administrators evaluate the risk associated with each file.

### Information Displayed

For each exposed file, Guard provides the following details:

* **File Name** – Name of the Salesforce file.
* **Public Link** – The external URL that provides public access to the file.
* **Expiration Date** – The date when the public link will expire (if configured).
* **Creator** – The user who created the file or public link.

This information helps administrators quickly determine whether a link has appropriate controls or has remained active longer than intended.

### Example Use Case

An administrator reviews the **Public File Exposure** view and notices a file containing internal documentation with a public link that does not have an expiration date set.

Using this information, the administrator can:

* Investigate the file and its purpose.
* Determine whether the link is still required.
* Remove or restrict the public link if it presents a security risk.

### Best Practices

To minimize the risk of unintended data exposure:

* Regularly review the **Public File Exposure** view.
* Ensure public links include expiration dates when possible.
* Remove links that are no longer needed.
* Review files shared publicly to confirm they do not contain sensitive information.
