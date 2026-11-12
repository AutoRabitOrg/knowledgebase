# Metric Profiles

A metric profile is the set of metrics measured when an application of a technology is assessed. Quality gate conditions can only check metrics that the profile measures. Each technology has a supplied language default, and you can create alternatives. Use this tab to compare how metric profiles are used, review organization defaults and adapt the metrics each application uses.

Open it from **Operations** → **Quality Control** → **Metric profiles** in the sidebar.

{% hint style="warning" %}
You need a role that can view metric profiles. Creating, editing, cloning and assigning profiles need roles that can manage or clone metric profiles.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/v2-qc-metric-profiles (1).png" alt="Metric profiles tab with summary tiles, filters and the profile table"><figcaption></figcaption></figure>

## Summary Tiles

Click a tile to filter the table.

| Tile                      | Shows                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| **Profiles**              | All metric profiles in the selected technology scope.                                             |
| **Language defaults**     | The starting default profile of each technology. Organization and application choices can differ. |
| **No active definitions** | Profiles without any active metric. Review their coverage before assigning them.                  |

## Profile Adoption and Configuration

| Filter                   | Description                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Technology**           | The technology the profile applies to.                                                                               |
| **Profile status**       | **All profiles**, **Language defaults**, **Other profiles**, **Enabled**, **Disabled** or **No active definitions**. |
| **Search profile names** | Finds profiles by name.                                                                                              |

**Saved filters** and **Save filters** keep a combination of filters for later. **Refresh** reloads the table, **Columns** shows or hides columns and **Export** downloads the table.

| Column                        | Description                                                                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Profile**                   | The profile name and whether it is **Enabled** or **Disabled**. Click the name to open its details.                                           |
| **Technology**                | The technology the profile applies to.                                                                                                        |
| **Language default**          | **Default** when this is the technology's default profile.                                                                                    |
| **Active / included metrics** | Active metrics out of all included metrics. Click it to review the metrics.                                                                   |
| **Last updated**              | When the profile last changed. The list shows the most recently changed profiles first; click **Last updated** or the name column to sort.    |
| **Latest assessment use**     | How many applications used the profile in their latest assessment, and in how many organizations it is the default. Click it to review usage. |
| **Actions**                   | **Review metrics**, **Assign organization defaults** and **Clone profile**.                                                                   |

## Profile Details

Click a profile's name or usage to open its details: technology, status, whether it is the language default and when it was updated, followed by the **Applications assessed** and **Organization defaults** counts and the **Applications using this standard** table (with **Refresh**, **Columns** and **Export**). From the details you can use **Edit profile details**, **Export profile** (JSON), **Make language default**, and **Disable profile** or **Enable profile**. Organizations using a disabled profile revert to the language default; recorded assessment results stay unchanged.

## Create a Profile

1. Click **Create Profile**.
2. Enter the **Profile name**. Required.
3. Choose the **Starting point**: **Start empty**, or **Import JSON** to upload an **Exported profile** file.
4. Choose the **Technology**. Required.
5. Optionally, explain in **Purpose** which applications or policy the profile is for.
6. Click **Create profile**.

To copy an existing profile instead, click **Clone profile** on its row and enter the **New Profile Name**.

## Review the Metrics in a Profile

Click **Review metrics** to open the profile's metrics on their own page; **Back to metric profiles** returns to the list. Filter by **Origin**, **Assessment use** and **Component type**, or search by metric name or identifier. **Saved filters**, **Refresh**, **Columns** and **Export** work as on the profile list.

| Column             | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Metric**         | The metric name.                                                          |
| **Origin**         | **Supplied** or **Custom**.                                               |
| **Key**            | The stable identifier that quality gate conditions use.                   |
| **Return type**    | The type of value the metric returns, for example `NUMBER` or `STRING`.   |
| **Component**      | What the metric measures, for example `FILE`, `PROJECT` or `APPLICATION`. |
| **Assessment use** | **Active** or **Disabled** in this profile.                               |
| **Updated**        | When the metric last changed.                                             |
| **Action**         | Disables an active metric in this profile, or activates a disabled one.   |

Click **Add metrics** to choose more metrics from those available for the technology, then confirm them in **Review profile additions**.

## Assign Organization Defaults

1. Click **Assign organization defaults** on the profile's row.
2. Choose one or more organizations in **Add organization to profile**, and click **Add Organizations**.

Defaults apply to future assessments and do not rewrite earlier results.

## Next Steps

* [Metric Rules](metric-rules.md): review and create the metrics a profile measures.
* [Quality Gates](quality-gates.md): use measured values in gate conditions.
* [Quality Profiles](quality-profiles.md): choose which rules raise findings for a technology.
* [Quality Control](./): return to the Quality Control overview.
