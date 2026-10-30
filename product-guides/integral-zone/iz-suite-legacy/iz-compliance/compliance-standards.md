# Compliance Standards

### Standards <a href="#standards" id="standards"></a>

Navigate to **`IZ Compliance`** → **`Standards`**.

| Column             | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| **`Name`**         | Name of the standard. Click to open its Policy Controls.        |
| **`Enabled?`**     | Whether the standard is included in calculations and snapshots. |
| **`Compliance %`** | Current compliance percentage of the standard.                  |
| **`Created`**      | When the standard was created.                                  |

Use **`Search Standards`** to filter by name.



Toolbar actions:

* **`Configure Standard`** creates a new standard (requires **`Create Compliance Standard`**).
* **`Re-calculate Compliance`** recalculates every enabled standard for your tenant.

\
Row actions:

* **`Rule Impact Measures`** opens the Standard Rules of the standard.
* **`Control Policies`** opens the Policy Controls tree.
* **`Edit Standard`** (requires **`Edit Compliance Standard`**).
* **`Initiate Snapshot`** stores the current state of the standard under **`History`**.
* **`Subscribe To Updates`** subscribes you to the **`On Compliance Snapshot`** notification for the standard (Email or Slack).
* **`Delete Compliance Standard`** is available for standards you created (requires **`Delete Compliance Standard`**). Built-in standards cannot be deleted.



#### Create or Edit a Standard <a href="#create-or-edit-a-standard" id="create-or-edit-a-standard"></a>



1. Click **`Configure Standard`**.
2. Enter the details:
   1. **`Standard Name`** - Name of the standard
   2. **`Description`** - Description of the standard
   3. **`Score Calculation Type`** - **`Multiply all Measures`**
   4. **`Impact Measure Calculation Type`** - **`Maximum of all Measures`** to score rules on several impact measures and take the highest as the rule's impact, or **`Manual Selection`** to pick the impact of each rule directly
   5. **`Add Impact Measures`** - Shown for **`Maximum of all Measures`**. Add one entry per measure, for example `Confidentiality`, `Integrity`, `Availability`. At least one measure is required.
   6. **`Status`** - **`Enabled`** or **`Disabled`**
3. Click **`Submit`**.
