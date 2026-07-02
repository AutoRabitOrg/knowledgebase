# System Audit Logs

{% hint style="warning" %}
* **`System Audit Logs`** can only be accessed by users with appropriate permissions. Permission required to view the audit logs is **`View System Audit Log` .**
{% endhint %}

1. Navigate to **`Audit`** -> **`System Audit Logs`**&#x20;
2. Audit Logs include following information about every action in the system -
   1. **`Product`** - Product / Module in which the action was performed
   2. **`User / Agent Name`** - Name of the user if the action was performed by a user or Agent name if the action was performed by an agent
   3. **`Operation`** - Name of the operation
   4. **`Request Date`** - Date on which the action was performed
   5. **`Time Taken`** - Time taken to execute / complete the request
   6. **`Status`** - Status of the operation. It can either be **`Success`** or **`Failed`**
   7. **`Actions`** -
      1. **`Download Payload`** - Download the Request and Response of the performed event. Certain field values might be masked based on the sensitivity of the data.

### See Also

* [Creating an Agent](../../integral-zone/iz-suite/iz-core/agent/create-agent.md)
* [Updating an Agent](../../integral-zone/iz-suite/iz-core/agent/update-agent.md)
