# SSO

<h2 align="center">Single Sign-On (SSO)</h2>

Single Sign-On (SSO) allows your organization to streamline and secure access to Guard by integrating with your corporate identity provider (IdP), such as Microsoft Entra ID. With SSO, users log in using their existing corporate credentials, reducing the need for multiple passwords and centralizing access control.

&#x20;

### Benefits of Using SSO

* Enhanced Security: Centralized authentication through your IdP ensures strong password policies, MFA, and compliance with your security standards.
* Simplified User Experience: Users log in once with their corporate account and gain access without needing separate Guard credentials.
* Centralized User Management: Control user access through your IdP groups instead of managing accounts manually in Guard.
* Improved Compliance & Auditing: Authentication and authorization are handled through a single, auditable system.

&#x20;

### How SSO Works with Guard

Currently, Guard manages SSO through Keycloak. To set up SSO for your tenant:

1. Submit a Support ticket requesting SSO enablement support.
2. Our team will help configure the integration with your IdP (e.g., Microsoft Entra ID).
3. Once configured, users assigned to the proper IdP groups will automatically be granted access to Guard (recommended default is Standard User privileges). Admins retain their permissions as defined in Guard.

&#x20;

### SSO-Only Authentication

Guard supports a tenant setting called Only SSO Authentication. When this option is enabled:

* Local tenant-manager users are automatically disabled.
* The User Management section is hidden in the Guard app.
* API-based user management is disabled.
* Only SSO-authenticated users can log in.

This mode ensures Guard access is exclusively controlled through your IdP, providing maximum security and centralized account lifecycle management.

&#x20;

### Best Practices

* Coordinate with your IT/IdP administrators when enabling SSO.
* Assign Guard access through IdP groups instead of creating users manually.
* Enable Only SSO Authentication once you’re confident your IdP is fully managing user access.
* Maintain at least two Admins in Guard during the transition to prevent lockouts.

&#x20;

SSO in Guard provides a secure and scalable way to manage authentication, while shifting User Management to your organization’s IdP.

&#x20;
