# Findings

**Findings** lists the open findings from the latest assessment of every application you can see, across Platform Analysis and Code Analysis, in one list grouped by rule. Use it to see which rules cause the most findings anywhere in your estate, then open a group for its occurrences or an application for its full evidence.

Open it from **Findings** in the sidebar, below **Dashboards**.

{% hint style="info" %}
Requires the **Platform Analysis** or **Code Analysis** licence. The list shows the findings of the applications your roles let you see in each of them.
{% endhint %}



<figure><img src="../../../.gitbook/assets/findings-list.png" alt=""><figcaption></figcaption></figure>

### Filters

| Filter                                            | Description                                                                                |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Product**                                       | **All products**, **Platform Analysis** or **Code Analysis**. Shown when you can see both. |
| **Asset type**                                    | The asset types of the chosen product that you can see.                                    |
| **Severity**, **Category**, **Security standard** | Narrow the list, as on the product's own **Findings** tab.                                 |

Every filter is kept in the page address, so you can share the link or save the set with **Save filters** and choose it later from **Saved filters**.

### Tiles

| Tile                               | Description                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| **Open finding occurrences**       | Every open occurrence that matches the filters, except severity.               |
| **Critical + Blocker occurrences** | The Critical and Blocker occurrences. Click it to show only those in the list. |
| **Rules with open findings**       | The number of rules with open findings: each rule is one group in the list.    |

### Open findings

The list has the same columns, grouping and finding detail as the Platform Analysis Findings tab. Each row is tagged with its product. Opening an application takes you to its dossier in the workspace it belongs to.

{% hint style="info" %}
**Time to fix** and **Exceptions** are kept per product. Use the **Findings** tab of Platform Analysis or Code Analysis for them.
{% endhint %}

### Next steps

* Platform Analysis Findings: effort estimates and the exceptions register for deployed applications.
* Code Analysis Findings: findings of branches and pull requests.
* Quality Gates: decide which findings fail an assessment.
