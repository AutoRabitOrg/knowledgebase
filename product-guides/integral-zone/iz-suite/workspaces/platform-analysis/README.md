# Platform Analysis

Platform Analysis shows the configuration and code posture of the applications deployed on your connected platforms (for example MuleSoft, AWS or Azure): their quality gate results, open findings and the evidence behind each verdict. Use it to decide which applications to fix first and to follow an application from one assessment to the next.

Open it from **Workspaces** → **Platform Analysis** in the sidebar.

{% hint style="info" %}
Requires the **Platform Analysis** licence.
{% endhint %}

{% hint style="warning" %}
You need a role that can view the applications of at least one licensed platform. The workspace shows only the organizations and platforms your role covers.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/.gitbookassetspa-overview-workspace.png" alt="Platform Analysis workspace with its Overview, Applications and Findings tabs"><figcaption><p>Platform Analysis workspace</p></figcaption></figure>

## Tabs

| Tab                             | Use it to                                                                                |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| [Overview](overview.md)         | See gate results, evidence coverage, defect trends and the applications to review first. |
| [Applications](applications.md) | List application versions, open an application's dossier and manage it.                  |
| [Findings](findings.md)         | Investigate open findings, estimate the time to fix them and review exceptions.          |

## Header actions

| Action                | Description                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Copy link**         | Copies the address of the current tab and filters.                                                                                                                                                                               |
| **Prepare AI review** | Opens the **AI review · connected evidence** drawer, where you prepare an AI review of an application or of the whole workspace. See [Overview](overview.md#prepare-an-ai-review). Shown only when your role can run AI reviews. |

The filters, saved filters and table tools work as described in Workspaces.

## Next steps

* [Overview](overview.md): start with the applications that need a gate review.
* [Applications](applications.md): open an application's dossier.
* [Findings](findings.md): investigate findings across applications.
