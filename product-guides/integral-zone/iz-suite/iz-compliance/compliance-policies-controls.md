# Compliance Policies Controls

Navigate to **`IZ Compliance`** → **`Standards`** and click a standard name, or use the **`Control Policies`** action.

Controls are displayed as an expandable tree. Each node shows:

* The control as **`<Control Name> - <Name>`**, for example `A12.6.1 - Management of technical vulnerabilities`. Click it to open the control.
* A badge with the **count of rules mapped** to the control. A red badge means no rule is mapped yet, so the control does not contribute to the score.
* The control's compliance percentage. Controls marked **`Not Applicable`** show `n/a`.

Click **`Create Policy Control`** to add a control (requires **`Create Compliance Standard`**):

1. **`Control Name`** - Short identifier, for example `A1.1`
2. **`Name`** - Title of the control
3. **`Control Description`** - Full text of the control in Markdown
4. **`Order`** - Position among its siblings
5. **`Status`** - **`Applicable`** or **`Not Applicable`**
6. **`Select Parent`** - Search for the parent control. Leave empty for a top-level control.
7. **`Manual Compliance`** (optional) - A **`Compliance`** value from 0 to 100 and **`Notes`** describing how the manual compliance is evidenced. Used only when the control has no mapped rules.



#### Policy Control Details <a href="#policy-control-details" id="policy-control-details"></a>



Opening a control shows three tabs:

1. **`Basic Info`** - The control description. Users with **`Edit Compliance Standard`** can click **`Edit`** to change it or delete the control.
2. **`Mapped Rules`** - The rules mapped to this control. Columns include **`Name`**, **`Risk type`**, **`Status`**, **`Origin`**, **`Action`**, and optionally **`Potential Consequence`**, **`Remediation`** and **`Created`**. Use **`Search Compliance Policy Rules`** to filter by rule name, rule id or tag.
3. **`Violations`** - Applications that currently fail at least one rule mapped to this control, with **`Total Failed Rules`** and the application's **`Compliance %`** for this control. Expand a row to see **`Rule Name`** and **`Total Violations`**. **`View Application Issues`** opens the application's issue list.

#### Map a Rule to a Control <a href="#map-a-rule-to-a-control" id="map-a-rule-to-a-control"></a>



Rules must first be attached to the standard (see Standard Rules below).

1. In the **`Mapped Rules`** tab click **`Map Policy Control Rule`**.
2. Enter the details:
   1. **`Select Rule`** - Search among the rules attached to the standard
   2. **`Risk Type`** - For example **`Threat`**
   3. **`Origin`** - **`Internal`** or **`External`**
   4. **`Status`** - **`Applicable`** or **`Not Applicable`**
   5. **`Action`** - **`Tolerate: Residual risk`**, **`Transfer`**, **`Combination of actions`**, **`Treat`** or **`Monitor`**
   6. **`Potential Consequence`**, **`Remediation`**, **`Notes`** - Free text
3. Click **`Submit`**. A rule can be mapped to a control only once.



### Standard Rules <a href="#standard-rules" id="standard-rules"></a>



Navigate to **`IZ Compliance`** → **`Standards`** and click **`Rule Impact Measures`** on a standard.

| Column           | Description                          |
| ---------------- | ------------------------------------ |
| **`Rule`**       | Name of the IZ quality rule          |
| **`Impact`**     | Impact of a violation of the rule    |
| **`Likelihood`** | Likelihood that the rule is violated |

Use **`Search Compliance Rules`** to filter by rule name, rule id or tag. Expand a row to see the policy controls the rule is mapped to.



#### Add a Rule to a Standard <a href="#add-a-rule-to-a-standard" id="add-a-rule-to-a-standard"></a>



1. Click **`Add Compliance Rule`**.
2. **`Select Rule`** - Search for the rule by name.
3. **`Set Impact Measures`** - For standards using **`Maximum of all Measures`**, pick a value for every measure. The **`Impact`** field is filled automatically with the highest value.
4. **`Impact`** - For standards using **`Manual Selection`**, pick **`Severe`**, **`High`**, **`Moderate`**, **`Low`** or **`None`**.
5. **`Likelihood`** - **`Severe`**, **`Medium`**, **`Low`** or **`None`**.
6. **`Notes`** - Optional.
7. Click **`Submit`**. A rule can be attached to a standard only once.

Row actions on a Standard Rule:

* **`Edit Standard Rule`** changes its impact and likelihood.
* **`Attach Policy`** maps the rule to a policy control (same fields as _Map a Rule to a Control_).
* **`Delete`** removes the rule from the standard together with its control mappings.



### Compliance Settings <a href="#compliance-settings" id="compliance-settings"></a>



Navigate to **`IZ Compliance`** → **`Settings`**. This screen holds the pick-lists used throughout the module.

| Setting type              | Built-in values                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **`IMPACT_MEASURES`**     | Severe (5), High (4), Moderate (3), Low (2), None (1)                     |
| **`LIKELIHOOD_MEASURES`** | Severe (5), Medium (3), Low (2), None (0)                                 |
| **`RISK_TYPES`**          | Threat                                                                    |
| **`ORIGIN_TYPES`**        | Internal, External                                                        |
| **`ACTION_TYPES`**        | Tolerate: Residual risk, Transfer, Combination of actions, Treat, Monitor |
| **`REVIEW_STATUS_TYPES`** | Applicable, Not Applicable                                                |



Click **`Configure Setting`** to add a value: **`Name`**, **`Value`**, **`Value Type`** (`INTEGER` or `STRING`), **`Setting Type`** and **`Status`**. Built-in values can be edited or disabled but not deleted.



### Compliance History <a href="#compliance-history" id="compliance-history"></a>



Navigate to **`IZ Compliance`** → **`History`**.

A snapshot preserves a standard's percentage, every control's percentage, all rule mappings and every failing validation at that moment. Use snapshots as audit evidence and to track progress over time.



| Column              | Description                                        |
| ------------------- | -------------------------------------------------- |
| **`Standard Name`** | Click to open the snapshot                         |
| **`Compliance %`**  | Percentage of the standard at the time of snapshot |
| **`Created`**       | When the snapshot was taken                        |

* **`Initiate Compliance Snapshot`** (toolbar) snapshots all enabled standards. **`Initiate Snapshot`** on the Standards screen snapshots a single standard.
* Opening a snapshot shows the same Policy Controls tree, control details, mapped rules and violations as the live standard, read-only, labelled with the standard name and snapshot time.
* When a snapshot is created, subscribers of **`On Compliance Snapshot`** receive a notification titled **`<Standard> | Compliance Report`**.
* **`Delete Compliance History`** removes a snapshot.



### Roles and Permissions <a href="#roles-and-permissions" id="roles-and-permissions"></a>



| Permission                       | Allows                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------- |
| **`View Compliance Standard`**   | Open all IZ Compliance screens                                                |
| **`Create Compliance Standard`** | Create standards, policy controls, rule mappings and settings                 |
| **`Edit Compliance Standard`**   | Edit standards, controls, mappings and settings; re-calculate; take snapshots |
| **`Delete Compliance Standard`** | Delete custom standards, controls, mappings, settings and snapshots           |



### Multi-Tenancy Notes <a href="#multi-tenancy-notes" id="multi-tenancy-notes"></a>



* Standards, controls, rule mappings and snapshots are private to each tenant.
* When the platform administrator enables **`Compliance`** for a tenant, the tenant receives a copy of the built-in standards, controls, impact measures and default rule mappings. Changes the tenant makes afterwards are never overwritten by upgrades; upgrades only add new built-in items.
* Compliance Settings pick-lists are shared with the platform defaults; a tenant can add its own values.

<br>
