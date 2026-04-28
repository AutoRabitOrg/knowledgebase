# Permissions Explorer

### Overview

AutoRABIT Guard’s Permissions Explorer is a hub for answering who has which Salesforce permissions, how those grants are wired (Profiles, Permission sets, and Permission set groups), and how access has changed over time.&#x20;

### Explore User Permissions

Find users (or permission containers) that match general org permissions (such as Author Apex or API Enabled) and inspect how those permissions were granted.

#### Key capabilities

* Quick Explorer:

Use predefined templates to answer critical questions such as:

1. Who can access everything without restriction?
2. Who can deploy code directly to production?
3. Who can take over user accounts?
4. Who can grant elevated access to themselves or others?
5. Who can move large volumes of data in and out?
6. Who can weaken password policies?

These templates accelerate common security investigations and reduce manual query building.

<figure><img src="../../.gitbook/assets/image (2495).png" alt=""><figcaption></figcaption></figure>

* Saved Queries:

Any custom queries you’ve created are saved and easily accessible from the Permission Explorer homepage.

* Custom Explorer:

For deeper analysis, create your own queries by selecting permissions grouped into categories such as:

1. Access Control
2. Custom Code
3. Data Export / Data Input
4. Integration
5. Password Management
6. Super Admin Permissions (full permissions reserved for only a few trusted users)
7. User Management
8. Other permissions

Once permissions are selected, the tool shows:

* Which users hold the permissions
* The **source of access** (profile or permission set)
* A **User Detail Page** with account status, creator, and activity insights

#### Why it matters

It connects risky permission combinations to real users and granting paths, which supports least-privilege reviews, SOX-style access controls, and faster answers to “who can do X in production?”

#### Getting started (User permissions)

1. Open Permissions Explorer.
2. Choose Explore User Permissions.
3. Select a Salesforce org.
4. Use Quick Explorer or Custom Explorer, add optional user criteria, then run the exploration.
5. Pick an entity type on the left, select a row, and use Diagram / Tree (for users) or the users' view (for profiles and permission sets).

### Explore Object Access

Understand which users have access to which objects and at what leve, again with optional user scoping and grant-path style analysis in the shared results UI.

#### Key capabilities

* Object + access selection:&#x20;

A tree control lets you multi-select object access entries (object type paired with permission type).&#x20;

* Same user criteria builder:

Include frozen users and up to four criteria rows (Profile, Role, Company, Domain) with operators and org-resolved values, matching the permission explorer filter model.

* Saved queries:

Object-access queries are stored and listed separately so teams can reuse common object-access reviews.

#### Why it matters

Object permissions drive data exposure and bulk data operations. Exploring by object and access level makes data-governance and segmentation reviews practical without manual SOQL and setup digging.

#### Getting started (Object access)

1. From the hub, choose Explore Object Access.
2. Select Salesforce org and object access in the tree (one or more object/permission combinations).
3. Optionally configure user criteria and Include frozen users.
4. Click Explore and interpret results using the entity selector on the left.

### Explore Permission History

Review audit-style changes for selected user permissions: when something changed, which permission, who made the change, and a change detail label.

#### Key capabilities

* Permission + org selection:

Pick one or more permissions via the shared permission selector (scoped to the org) and an org, then Explore.

* History table:

Columns include Date, Permission (with category icon when available), Changed by, and Change detail.

#### Why it matters

Knowing who changed what permission and when supports investigations, change control, and proving that remediations actually landed in the org.

#### Getting started (History)

1. Choose Explore Permission History.
2. Select the Salesforce org and one or more permissions.
3. Click Explore to load the history grid.
4. Use Back to adjust permissions or return to the hub.

### Explore Agentforce

Surface permissions for Agentforce agents and related users in the selected org: a focused slice of the same “who has what and how” model as user-permission exploration, without manually assembling Agentforce-related permission lists.

#### Why it matters

Agent and automation identities often accumulate broad API and data permissions.&#x20;

A dedicated entry point speeds security and compliance review of those identities.

#### Getting started (Agentforce)

1. Choose Explore Agentforce.
2. Select Salesforce org.
3. Click Explore, then review users and grant paths.

### Benefits

* Visibility

Clear answers across users, profiles, permission sets, and permission set groups.

* Traceability

Grant paths and history reduce guesswork about how access appeared.

* Efficiency

Quick Explorer and saved queries shorten recurring audits.

* Risk focus

Object access and high-risk permission bundles align reviews with data exposure and privileged actions.

### Conclusion

Permissions Explorer bundles user-level permission analysis, object-level access exploration, Agentforce-focused reviews, and permission change history into one Guard module. Used together, these views help teams find over-privileged access, prove how it was granted, and track how it changes, supporting both operational security and compliance workflows.



&#x20;
