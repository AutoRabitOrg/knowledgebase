# Server Upgrade

## Upgrading IZ Suite Server

{% hint style="warning" %}
Before installing, make sure you have a **valid database backup**:

* Proceeding without a valid database backup can lead to data loss or inability to recover in case of upgrade failure.
{% endhint %}

### Client-Managed Installation

If the IZ Suite installation is managed by the client, please follow the steps below _**before performing the upgrade**_:

1. Take a complete backup of the existing database or schema.
2. This backup is **`critical`** to enable rollback in case the upgrade process fails or encounters issues.
3. Ensure that the backup is _**verified and stored securely**_ before proceeding with the upgrade.
4. Upgrade IZ Suite by following the steps that match your installation method, making sure to increment the IZ suite version.

### Integral Zone-Managed Installation

If the installation is managed by **`Integral Zone`**, the following will be handled as part of the upgrade process:

1. A full backup of the existing database/schema will be taken before the upgrade.
2. In case of an upgrade failure, rollback and recovery will be performed by the Integral Zone team.
3. No manual intervention is required from the client side for backup or rollback if the installation is managed by Integral Zone.

### See Also

* Server Installation
* Prerequisites
* Cluster Mode
