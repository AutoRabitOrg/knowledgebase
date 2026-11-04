# User Security Overview

### Overview

AutoRABIT Guard’s User Security Overview offers a single place to inspect Salesforce users, what they can access, and how they have been authenticating. By combining profile-level context with effective object and field permissions, permission set assignments, OAuth usage, and login history, Guard supports access reviews, incident response, and day-to-day security operations without jumping between multiple Salesforce setup screens.

### Key Capabilities

#### User-centric workspace

Select a registered Salesforce org and a user (searchable list with name and username). Content is organized into tabs so you can move from identity to access to session evidence in a consistent layout.

#### User Info

View core Salesforce user attributes in one grid: User ID, Username, Email, Alias, Profile, Role, User Type, org fields such as Title, Department, Company, Manager, Phone, Federation ID, Created and Last Login dates, Time Zone, Locale, Language, and active status.

#### Object and Field Access

Review effective object permissions across the org: Create, Read, Update, Delete, View All, and Modify All (shown as compact badges). Use built-in filters to narrow by Object and by Access type so you can quickly find over-privileged or sensitive combinations. Click a row to open a detail dialog for that object.

#### Permission Sets

See permission sets assigned to the user (excluding the profile-owned permission set), with expiration dates highlighted so expired or soon-to-expire assignments are easy to spot.

#### Active OAuth Tokens

List connected applications that have active OAuth tokens for the user, including last used time (with relative context) and token count, helping you spot stale integrations or unexpected third-party access.

#### Login History

Browse paginated login events with status, application, login type / subtype, source IP, country, browser, platform, login URL, and TLS protocol. Use View Login Map to visualize login coordinates for geographic patterns.

#### Object and field drill-down

From the object access table, the detail dialog provides:

* Field Permissions — Effective read and edit per field, with a field name filter and expandable panels that load which profiles and permission sets contribute field-level access.
* Object Permissions — For eligible administrators, which profiles and permission sets grant object-level CRUD and View All / Modify All (see note on roles below).

### Why It Matters?

* Access reviews and least privilege:

Seeing effective permissions in one view makes it practical to validate whether a user still needs broad object or “View All / Modify All” rights.

* Faster investigations:&#x20;

Login history, IP, application, and TLS details support questions about where and how a user signed in; the login map adds location context when coordinates are available.

* Integration and session risk:

OAuth token summaries surface which connected apps hold tokens and whether they are still in use, complementing object-level reviews.

* Traceability of grants:

Field-level expansion shows Profile vs. Permission Set sources for read/edit, so you can plan remediation (remove assignment, adjust permission set, or profile change) with less guesswork.

### Getting Started

1. Open Guard and go to User Security Overview.
2. Salesforce org: Choose one of your orgs registered in Guard.
3. User: Pick the user to review (the list loads from the org; you can filter the dropdown).
4. Work through the tabs: User Info → Object and Field Access → Permission Sets → Active OAuth Tokens → Login History as needed.
5. On Object and Field Access, use Object and Access filters, then click an object to open Object Permissions and Field Permissions for deeper analysis.

### Benefits

* Increased visibility:

One screen ties together identity, permissions, integrations, and sign-in evidence for a chosen user and org.

* Operational efficiency:

Reduces time spent correlating Setup, permission sets, and login reports manually.

* Stronger governance:

Supports periodic access reviews and validation of permission set expirations.

* Risk awareness:

Surfaces broad object rights, OAuth usage, and login anomalies in a structured way.

### Conclusion

User Security Overview helps organizations understand and audit Salesforce user access and activity in context: from profile and role through effective permissions and field-level sources, to permission sets, OAuth-connected apps, and login history with optional map visualization. Used as part of Guard’s broader access and compliance tools, it makes user-level security review practical and repeatable.
