# Email Admin Settings

**Email Administration in Salesforce r**epresents an organization’s email administration settings, including email deliverability, security compliance, relay configurations, and system notifications.&#x20;

This governs how outbound emails are handled across your org. These include default behaviors like:&#x20;

* Compliance features (like bounce management and logging)&#x20;
* TLS settings&#x20;
* Mail Server Management&#x20;
* Footers, headers, and more&#x20;

With Salesforce, you will not be able to deploy this setting as part of your package.xml. It will have to be a manual deployment. To avoid this, AutoRABIT has an ‘EmailAdminSettings’ option under ‘Manage Email Administration Deliverability’ – this allows users to manage email administration settings as follows:&#x20;

**Access to Send Email** - This setting applies to production and sandboxes. The values can be one of:&#x20;

* No access—Allows only password reset emails. Prevents all other outbound email to and from users.&#x20;
* System email only—Allows only automatically generated emails, such as new user and password reset emails.&#x20;
* All email—Allows all types of outbound email. Default for new orgs that aren’t sandboxes.&#x20;

**TLS Setting** – This setting configures your TLS for outbound emails. The values include:&#x20;

* **Preferred**—If the message transfer agent (MTA) advertises TLS and a common cipher can be negotiated, TLS is used. If TLS can’t be negotiated, the email is delivered unencrypted. This setting is the default.&#x20;
* **Required**—If TLS can’t be negotiated or a common cipher can’t be agreed on, the email bounces back to the originator.&#x20;
* **Preferred Verify**—If the MTA advertises TLS, a common cipher can be negotiated, and Salesforce can verify the receiver, TLS is used. Verification means that a valid certificate authority has signed the receiver’s certificate and the hostname in the certificate matches the host to which we connected. If TLS can’t be negotiated or the verification fails, the email is delivered unencrypted.&#x20;
* **Required Verify**—If TLS can’t be negotiated, a common cipher can’t be agreed on, or the sender can’t be verified, the email bounces back to the originator. Verification means that a valid certificate authority has signed the receiver’s certificate and the hostname in the certificate matches the host to which we connected.&#x20;

&#x20;

**Restrict TLS To These Domains** - To enable this preference, you must specify a TLS Setting other than ‘Preferred’ and provide the comma-separated list of domains through Domains Name in ARM. When this field is set to true, any domains not in the list use the system default TLS Setting of ‘Preferred’.&#x20;

**Note** – With ‘TLS Setting’ set to ‘Preferred’, the option of ‘Restrict TLS to these domains’ should not be selected in ARM. If it is, ARM will throw an error during the deployment.&#x20;

&#x20;

**Domains Name** – With TLS Setting set to anything other than ‘Preferred’, you can provide a list of domains that should adhere to the TLS Setting configured from earlier.&#x20;
