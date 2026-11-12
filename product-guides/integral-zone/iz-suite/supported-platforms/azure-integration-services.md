# Azure Integration Services

IZ Suite connects to Azure with a service principal: an app registered in Microsoft Entra ID with the Reader role on your subscriptions. The sync brings in each subscription as an organization and each resource group as an environment. Assessment jobs then check the Logic Apps, API Management policies and Function Apps in those resource groups.

{% hint style="info" %}
Requires the **Platform Analysis** licence.
{% endhint %}

## Register an App in Microsoft Entra ID

### Create the App and Its Secret

1. In the Azure portal, open **Microsoft Entra ID** → **App registrations** and click **New registration**.
2. Enter a **Name** for the app.
3. Under **Supported account types**, choose the single-tenant option.
4. Click **Register**.
5. On the app's page, click **Add a certificate or secret** under **Client credentials**.
6. On the **Client secrets** tab, click **New client secret**, enter a description and choose an expiry that follows your organization's standards.
7. Click **Add** and copy the secret's **Value**. It is shown only once.

### Give the App Read Access

Repeat for each subscription you want IZ Suite to cover:

1. Open **Subscriptions**, select the subscription and open **Access control (IAM)**.
2. Click **Add** → **Add role assignment**.
3. Choose the **Reader** role.
4. Under **Assign access to**, choose **User, group, or service principal**.
5. Click **Select members**, search for the app you registered and select it.
6. Click **Review + assign**.

### Copy the App's IDs

On the app's **Overview** page, copy:

* **Directory (tenant) ID**
* **Application (client) ID**

{% hint style="danger" %}
The client secret expires on the date you chose. Before it does, create a new secret in Entra ID and enter it in IZ Suite, or the sync and assessments stop signing in.
{% endhint %}

## Connect Azure in IZ Suite

<figure><img src="../../../../.gitbook/assets/v2-plat-azure.png" alt="Connect Azure subscriptions drawer with the Entra ID instructions, Directory (tenant) ID, Application (client) ID, Client secret and Inventory sync"><figcaption></figcaption></figure>

1. Open **Administration** → **Setup** and click **Set up** (or **Review**) on **Connect Azure subscriptions**.
2. Enter the **Directory (tenant) ID**, **Application (client) ID** and **Client secret**.
3. Leave **Inventory sync** on.
4. Click **Save**.

Saving stores the client secret encrypted and starts a one-time **Azure Integration Services Sync**; with **Inventory sync** on, the sync also runs every 12 hours. There is no test button: the first sync's run log under [Execution History](../operations/schedules/execution-history.md) says what it found, and the step turns done when subscriptions arrive.

{% hint style="warning" %}
You need a role that can change global settings to connect Azure.
{% endhint %}

The Change Assurance Azure connection is separate, though the same app can serve both. Signing in to IZ Suite with an Azure account uses a different app registration too (see [Single Sign-On](single-sign-on/)).

## What the Sync Brings In

Each **Azure Integration Services Sync** run signs in with the service principal and:

* Brings in every subscription the app can read as an IZ Suite organization (source **Azure**).
* Brings in each subscription's resource groups as that organization's environments.

A recurring sync picks up new subscriptions and resource groups. See them under **Administration** → **Organizations**: **Manage environments** lists a subscription's resource groups.

## What Is Assessed

| Assessment type                   | Assesses                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Azure Logic App Analysis**      | The Logic Apps in the selected resource groups: their workflow definitions and connections. |
| **Azure API Management Analysis** | The policies of the API Management services in the selected resource groups.                |
| **Azure Function App Analysis**   | The Function Apps in the selected resource groups: their configuration and functions.       |

### Schedule the Assessments

1. Open **Administration** → **Setup** and click **Set up** on **Turn on Azure assessments**. The step unlocks once **Connect Azure subscriptions** has brought subscriptions in.
2. Under **What to assess**, keep the assessment types you want.
3. Under **When should this work run?**, choose **One time** or **Recurring** and the interval.
4. Click **Turn on assessments**.

To set one cadence per subscription, with its own resource groups and exceptions per asset type, use **Schedule platform scan** under [All Schedules](../operations/schedules/all-schedules.md).

Logic Apps, API Management policies and Function Apps can also be scanned from source with Code Analysis (see [Supported Languages](supported-languages.md)).

## Where the Results Appear

| What                                                                                                  | Where                                                             |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Subscriptions and resource groups                                                                     | [Organizations](../administration/organizations/)                 |
| Assessed Logic Apps, API Management services and Function Apps, with their quality gates and findings | [Platform Analysis](../workspaces/platform-analysis/)             |
| Monitors on Azure resources                                                                           | [Service Health](../workspaces/service-health/monitors.md)        |
| Sync and assessment runs                                                                              | [Execution History](../operations/schedules/execution-history.md) |

## Next Steps

* [How Assessments Run](how-assessments-run.md): agents, job types and schedules.
* [Single Sign-On](single-sign-on/): let people sign in with their Azure account.
* [Amazon Web Services](amazon-web-services.md): connect your AWS accounts.
* [Supported Platforms](./): back to the platform overview.
