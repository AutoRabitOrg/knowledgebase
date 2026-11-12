# Updates & Maintenance

**Updates & maintenance** keeps the lifecycle and maintenance rules for this workspace. A rule tells affected teams what changed, what action is needed and what evidence closes the work. Assigned work appears in the shared work queue next to upgrade waves.

Open it from **Workspaces** → **Dependency Insights** → **Updates & maintenance** in the sidebar.

The view has two tabs: **Maintenance rules** (this page) and [Actions](actions.md), which tracks upgrade waves and saved risk review notes.

{% hint style="info" %}
Requires the **Dependency Insights** licence.
{% endhint %}

<figure><img src="../../../../../../.gitbook/assets/v2-di-maint-rules.png" alt="Update and maintenance rules list"><figcaption></figcaption></figure>

## Maintenance rules

A rule is visible when at least one affected application is in your scope.

| Filter                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| Search                    | **Search by title or target**.                                                              |
| **Intent**                | **All intents** or one of the intents below. You can save the filter with **Save filters**. |
| **Active** / **Archived** | Show active or archived rules.                                                              |

| Column       | Description                                                                           |
| ------------ | ------------------------------------------------------------------------------------- |
| **Rule**     | Title and target.                                                                     |
| **Intent**   | **Update notice**, **Acknowledgment**, **Required maintenance** or **Change review**. |
| **Progress** | Closed items out of the total.                                                        |
| **Owner**    | Who owns the work, or **No assignee** for a notice.                                   |
| **Due**      | The due date, or **No due date**.                                                     |

**Refresh** reloads the list, **Columns** chooses the visible columns and **Export** downloads it.

**Assigned work** opens the shared work queue ([Assigned Work](../../../assigned-work.md)) with upgrades, maintenance, change reviews, acknowledgments and notices.

### Open a rule

Select a rule to see its intent, target, status, owner, due date, affected applications, what changed and the completion evidence. **Applications in this work** lists each application with its own status and assignee; use **Add to this work** to add applications on any platform, or remove an application from the work.

{% hint style="danger" %}
**Archive rule** cancels the rule's open items. Completed and acknowledged work stays as history.
{% endhint %}

## Create a rule

1. Select **Create rule**.
2. Under **What do you need from the affected teams?**, choose the intent:
   * **Update notice**: tell the owners of affected applications about a change in their notification bell. No work is assigned.
   * **Acknowledgment**: ask the owning team to confirm they have read and accepted the change.
   * **Required maintenance**: assign work with a due date and the evidence that completes it, for example a secret rotation or API version adoption.
   * **Change review**: ask an owner to review a proposed change with every affected application before it is made.
3. Under **What is it about?**, choose **An application version**, **Several applications** or **A shared dependency or component**, then select the target.
4. Complete the fields below.
5. Select **Save rule**.

| Field                                | Description                                                                                                                                                                                                                      |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title**                            | For example "Rotate the payments API client secret". **Required.**                                                                                                                                                               |
| **What changed and why it matters**  | The change and its reason. **Required.**                                                                                                                                                                                         |
| **Evidence that completes the work** | Shown for **Required maintenance** and **Change review**. The assignee records this evidence when completing the work. **Required.**                                                                                             |
| **Assign to**                        | A person or a team who owns the work; not used for an update notice. A person needs Dependency Insights, lifecycle and application access for every affected application; with a team, any member works the items. **Required.** |
| **Due date**                         | When the work is due.                                                                                                                                                                                                            |

<figure><img src="../../../../../../.gitbook/assets/v2-di-maint-create (1).png" alt="Create an update or maintenance rule form"><figcaption></figcaption></figure>

{% hint style="info" %}
To tell teams to stop using a component, create a deprecation instead. See [Asset Exposure](../asset-exposure.md).
{% endhint %}

## Next Steps

* [Actions](actions.md): follow upgrade waves next to maintenance work.
* [Risk & Lifecycle](../risk-and-lifecycle.md): create tracked work from the priority matrix.
* [Change Assurance](../../change-assurance/): review change before it reaches production.
