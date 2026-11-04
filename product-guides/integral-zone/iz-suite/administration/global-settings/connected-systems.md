# Connected Systems

A connected system groups work and agent assignments. When a job has to run on a particular agent, for example one installed next to a specific platform, you assign that agent and the work to the same system. Use this tab to register systems and check their agent coverage.

Open it from **Administration** → **Global Settings** → **Connected systems** in the sidebar.

<figure><img src="../../../../../.gitbook/assets/.gitbookassetsgs-connected-systems-list.png" alt="Connected systems tab with summary tiles and the system inventory"><figcaption><p>Connected systems</p></figcaption></figure>

{% hint style="warning" %}
You need a role that can view systems to open this tab. Registering, editing and deleting systems each need their own system permission.
{% endhint %}

{% hint style="info" %}
Registering a system does not connect to it or check its health. Assignments describe collection scope; check agent heartbeats and execution results to see whether work is actually running.
{% endhint %}

## Summary tiles

| Tile                      | Shows                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **Registered systems**    | Systems matching the current search.                                                   |
| **Assigned to agents**    | Systems with at least one agent assigned.                                              |
| **Without an assignment** | Systems no agent is assigned to. Review whether that is the intended collection scope. |

## System inventory

Use **Search system names or keys** to filter the table. **Reset filters** clears the search, and **Refresh** reloads the list. **Export this page** at the top of the tab downloads the systems on the current page as a CSV file.

| Column                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| **System**            | The system's name (click it to open **System evidence**) and key. |
| **Agent assignments** | How many agents are assigned, or **No explicit assignment**.      |
| **Last updated**      | When the system last changed.                                     |
| **Review**            | **Review system** opens **System evidence**.                      |

**System evidence** shows the system's name, key, registration and update dates, number of agent assignments and identity, and the **Assigned agents** with their recorded state. From there you can:

* Edit the system.
* Click **System executions** to open the execution history filtered to this system.
* Click **Delete system** to delete the registration after typing its exact name.

{% hint style="danger" %}
Deleting a system also deletes its agent assignments and can affect configuration that uses it. Review the linked agents and executions first.
{% endhint %}

## Register a system

1. Click **Register system**.
2. Enter the **System name** and **System key**.
3. Click **Save changes**.

<figure><img src="../../../../../.gitbook/assets/.gitbookassetsgs-connected-systems-register.png" alt="Register system form with System name and System key"><figcaption><p>Register system</p></figcaption></figure>

| Field           | Description                                                                         |
| --------------- | ----------------------------------------------------------------------------------- |
| **System name** | **Required.**                                                                       |
| **System key**  | **Required.** Use the stable key that your configuration and integrations refer to. |

{% hint style="warning" %}
Changing the key of an existing system can affect configuration that refers to it by key.
{% endhint %}

To assign an agent to a system, edit the agent and add the system under **Assigned systems**.

## Next steps

* [Agents](agents.md): assign agents to a system.
* Execution History: follow the work recorded against a system.
* [Global Settings](./): the other configuration screens.
