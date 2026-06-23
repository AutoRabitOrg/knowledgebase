# Connected Application Scopes

## Connected App Scopes

{% hint style="info" %}
Appropriate permissions might be required to create Connect App in Anypoint Platform.
{% endhint %}

### Creating Connected App

1. Log in to https://anypoint.mulesoft.com/
2. Navigate to **`Access Management`** -> **`Connected Apps`**
3. Click on **`Create App`** and select the following details
   1. Name - IZ Suite Agent
   2. Type - App acts on its own behalf
4. Click on **`Add Scopes`** and add the applicable scopes. Table below can be used as a reference.
5. Click on Save
6. Note the **`Client Id`** and **`Client Secret`** which will be used in the next step

### Connected App Scopes

| Job Type                                          | Required Scope                                           | Description .2+                                                              |
| ------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Anypoint Mule Runtime Analysis                    | **`Read Applications`**                                  | View Applications deployed on CloudHub                                       |
| **`Read Runtime Fabrics`**                        | View Applications deployed on CloudHub 2.0               | Anypoint Exchange APIs Analysis                                              |
| **`Exchange Viewer`**                             | View assets published to Exchange .4+                    | Anypoint API Instance Analysis                                               |
| **`Manage API Alerts`**                           | Read alerts defined for the API Instance                 | **`View Contracts`**                                                         |
| View contracts defined for the API Instance       | **`Manage Policies`**                                    | View policies defined for the API Instance                                   |
| **`API Group Administrator`**                     | View SLA Tiers defined for the API Instance .5+          | Anypoint Sync                                                                |
| **`View Organization`**                           | View organizations the Connected App has access to       | **`View Environment`**                                                       |
| View environments the Connected App has access to | **`View Environments in a particular organization`**     | View environments the Connected App has access to in a specific organization |
| **`View Users in a particular organization`**     | Required if Anypoint Teams Sync is enabled to sync users | **`Access Controls Viewer`**                                                 |

### Applying Client ID and Secret

1. Navigate to **`Global Settings`** -> **`Job types`**
2. Search for **`Anypoint Sync`** job type and click on edit&#x20;
3. Update the value of **`Client ID`** key with the Connected App’s Client ID
4. Update the value of **`Client Secret`** key to the Connected App’s Client Secret&#x20;
5. Click on **`Ok`**
6. The **`Anypoint Sync`** scheduler will now automatically sync the appropriate Organizations/Business Groups and Environments which it has access to

### See Also

* Aggregated Dashboard
* Application Dashboard
* Agent Job Types
* Mule Projects
* API Applications
