# Control Access to the Salesforce Organization

Vault allows administrators to restrict user access to specific Salesforce orgs registered within the account. Based on access permissions, users can perform Vault operations such as **backup**, **restore**, **replication**, **comparison**, and **archival** on authorized Salesforce orgs only.

## Org Access Control Overview

The **Enable Org. Access Control** toggle on the **Manage Users** page is **enabled by default**. This setting grants the administrator the ability to define which users can access specific Salesforce orgs.

If this toggle is **disabled**, all users in the Vault account will have **unrestricted access** to all registered Salesforce orgs.

<figure><img src="../../../.gitbook/assets/image (86) (1) (1) (1) (1) (1).png" alt="Enable Org Access Control Toggle" /></figure>

---

## When "Enable Org. Access Control" Is Turned **On** <a href="#enable-org-access-control-is-turned-on" id="enable-org-access-control-is-turned-on"></a>

1. On the **Add User** screen, the **Salesforce Orgs** field becomes active.
2. The administrator must select one or more Salesforce orgs for the new user.
3. Users will have **access only to the Salesforce orgs explicitly granted** by the administrator.
4. Users are limited to performing Vault operations within those assigned orgs.

---

## When "Enable Org. Access Control" Is Turned **Off** <a href="#enable-org-access-control-is-turned-off" id="enable-org-access-control-is-turned-off"></a>

1. All users in the Vault account can access **all registered Salesforce orgs**.
2. Users can perform Vault operations on **any org**, regardless of who registered it.
3. The **Salesforce Orgs List** will display **every org** currently registered in Vault for all users.
