# Overview

* IZ Compliance requires the **`Compliance`** license module. When the module is not part of your subscription the menu is hidden and compliance scores are not calculated.
* In a multi-tenant installation the module is enabled per tenant by the platform administrator using **`Enable Modules`** (see [Manage Tenants](../iz-core/multi-tenancy/manage-tenants.md)).
* Users need the **`View Compliance Standard`** permission to open the screens. The built-in roles **`Compliance Admin`** and **`Compliance Viewer`** grant the required permissions.



### Introduction <a href="#introduction" id="introduction"></a>

IZ Compliance maps the quality and security rules that IZ Eye and IZ Scan already evaluate onto the controls of a compliance framework, and turns the latest scan results of your estate into a compliance percentage per control and per standard. Instead of auditing applications one by one, you can see at any time which controls of **ISO 27001** or **SOC 2** are satisfied by the code that is actually deployed, which controls are failing, and which applications are responsible.

IZ Compliance consists of:



| Concept                   | Description                                                                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Standard`**            | A compliance framework, for example ISO 27001 or SOC 2. Two standards are built in; you can add your own.                                                               |
| **`Policy Control`**      | One clause or criterion of a standard, for example `A9.4.1 Information access restriction`. Controls are organised as a tree.                                           |
| **`Standard Rule`**       | An IZ quality rule attached to a standard together with its **Likelihood** and **Impact**. Only rules attached to a standard can be mapped to that standard's controls. |
| **`Impact Measure`**      | A named axis used to score the impact of a rule, for example Confidentiality, Integrity and Availability.                                                               |
| **`Policy Rule Mapping`** | The link between a Standard Rule and a Policy Control, with the risk type, origin, action and review status of the mapping.                                             |
| **`Validation`**          | The pass/fail result of every mapped rule on the most recent scan of every application.                                                                                 |
| **`Snapshot`**            | A point-in-time copy of a standard, its controls, mappings and violations, kept under **`History`**.                                                                    |

#### Built-in Standards <a href="#built-in-standards" id="built-in-standards"></a>

| Standard      | Impact calculation      | Impact measures                          | Controls                                                                                                     |
| ------------- | ----------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **ISO 27001** | Maximum of all Measures | Confidentiality, Integrity, Availability | Annex A domains A5 to A18 with their sub-clauses                                                             |
| **SOC 2**     | Manual Selection        | None (impact is chosen directly)         | Common Criteria CC1 to CC9 plus the Availability, Confidentiality, Processing Integrity and Privacy criteria |

Both standards ship with a default mapping of the built-in Mule, API, API Manager, Azure Logic Apps, Azure API Management, Azure Function App, Salesforce Apex, C#, Python and Kubernetes rules to the relevant controls. Rules that only enforce naming or documentation conventions are intentionally not mapped, because they would lower a score without evidencing a control. The default likelihood and impact values are derived from rule severity and are intended as a starting point to be tuned for your organization.



### How the Compliance Percentage is Calculated <a href="#how-the-compliance-percentage-is-calculated" id="how-the-compliance-percentage-is-calculated"></a>

1. For every application, only the **latest scan** is considered.
2. A mapped rule is **compliant** when it passed on every application in the tenant. If it failed on any application, it counts as failed for the control it is mapped to.
3. A **Policy Control** participates in the calculation only when its status is **`Applicable`** and it has at least one mapped rule. Its percentage is `(mapped rules - failed rules) / mapped rules`.
4. A parent control's percentage is the average of its applicable children (rounded up). If the parent has no mapped rules of its own but a **`Manual Compliance`** value is recorded, that value is included in the average. Use manual compliance for controls that are satisfied by processes outside IZ Suite.
5. The **standard's** percentage is the average of its applicable top-level controls.

Percentages are recalculated:

* Automatically at midnight on the **1st and 15th of every month** for each tenant that has the module enabled.
* Whenever a scan reports results for mapped rules.
* On demand, using **`Re-calculate Compliance`** on the Standards screen. The calculation runs as a background work item; progress and the old and new percentage per standard are visible in **`Audit`** → **`Scheduler Audit Logs`** under the handler **`Compliance Validation Handler`**.

Likelihood and Impact are recorded per rule and shown on the Standard Rules screen to help prioritise remediation. They do not weight the compliance percentage.



