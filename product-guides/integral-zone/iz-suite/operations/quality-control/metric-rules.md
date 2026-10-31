# Metric Rules

A metric produces a measured value during an assessment, such as the number of blocker issues or the number of batch jobs. Quality gate conditions compare these values with required results. A metric only runs for an application when it is included in that technology's metric profile. Use this tab to review what each metric measures, the value it returns and where it runs.

Open it from **Operations** → **Quality Control** → **Metric rules** in the sidebar.

{% hint style="warning" %}
You need a role that can view metric rules. Creating, editing, cloning, deleting and activating metrics in profiles need the matching metric permissions.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/.gitbookassetsqc-metric-rules-list.png" alt="Metric rules tab with filters and the metric definitions table"><figcaption><p>Metric rules</p></figcaption></figure>

## Filters

| Filter                             | Description                                                            |
| ---------------------------------- | ---------------------------------------------------------------------- |
| **Technology**                     | The technology the metric applies to.                                  |
| **Assessment scope**               | Where the metric runs, for example `APPLICATION`, `PROJECT` or `FILE`. |
| **Output**                         | The type of value it returns, for example `NUMBER` or `STRING`.        |
| **Origin**                         | **Supplied** or **Custom**.                                            |
| **Implementation language**        | The language the metric's logic is written in.                         |
| **Search name, identifier or tag** | Finds metrics by name, identifier or tag.                              |

**Saved filters** and **Save filters** keep a combination of filters for later. **Refresh** reloads the table.

## Metric definitions

| Column                          | Description                                                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Metric**                      | The metric name. Click it to open the metric.                                                                                                                            |
| **Technology**                  | The technology the metric applies to.                                                                                                                                    |
| **Output**                      | The type of value it returns.                                                                                                                                            |
| **Assessment scope**            | Where it runs.                                                                                                                                                           |
| **Origin**                      | **Supplied** or **Custom**.                                                                                                                                              |
| **Manage / profile membership** | **Edit metric**, **Clone metric** (creates a custom copy and opens it), **Activate in profile** (adds it to metric profiles) and, for custom metrics, **Delete metric**. |

{% hint style="info" %}
A metric's presence in this library does not mean every application evaluates it. Profile membership decides which metrics are measured.
{% endhint %}

{% hint style="danger" %}
Deleting a custom metric cannot be undone.
{% endhint %}

## Create a metric

1. Click **Create metric**.
2. Fill in the fields on **Purpose & measurement**, **Customer guidance** and **Implementation**.
3. Click **Create metric**.
4. Use **Activate in profile** to include the metric in the metric profiles that need it.

<figure><img src="../../../../../.gitbook/assets/.gitbookassetsqc-metric-rules-editor.png" alt="Create metric with the Purpose and measurement tab"><figcaption><p>Creating a metric</p></figcaption></figure>

| Field                       | Description                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metric name**             | Required. A descriptive name, up to 100 characters.                                                                                                 |
| **Technology**              | Required. The technology the metric applies to.                                                                                                     |
| **Metric key**              | Required. The stable identifier that quality gate conditions use. Renaming the metric keeps this key.                                               |
| **Output type**             | Required. The type of value the metric returns.                                                                                                     |
| **Assessment scope**        | Required. Where the metric runs.                                                                                                                    |
| **Tags**                    | Type a tag and press Enter or a comma, or pick an existing tag.                                                                                     |
| **Guidance (Markdown)**     | On **Customer guidance**: what the value means, why it matters and what the application owner should do. **Guidance preview** shows how it renders. |
| **Implementation language** | On **Implementation**: required. The language of the metric's logic, together with the implementation itself.                                       |

## Open or edit a metric

Click a metric's name to open it. **Edit definition** lets you change it; click **Save definition** to keep the change, or **Cancel**. **Activate in profile** adds it to metric profiles. Supplied metrics have no **Implementation** tab; clone one to make a custom version you can change.

## Next steps

* [Metric Profiles](metric-profiles.md): include metrics in the profile for a technology.
* [Quality Gates](quality-gates.md): use a metric's value in a gate condition.
* [Quality Rules](quality-rules.md): review the rules whose findings many metrics count.
* [Quality Control](./): return to the Quality Control overview.
