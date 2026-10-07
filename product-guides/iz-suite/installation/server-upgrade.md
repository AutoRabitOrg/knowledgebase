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

Database migrations run automatically when the new server container starts. If a migration fails, the container stops and prints recovery instructions in its log rather than starting on a partially migrated schema. Restore the backup, resolve the reported problem and start the container again.

#### Upgrading to 26.4.1 <a href="#upgrading-to-26-4-1" id="upgrading-to-26-4-1"></a>

**Before the upgrade**

1. Generate a secrets encryption key, for example with `openssl rand -hex 32` (64 hexadecimal characters), and store it in your deployment's secret store.
2. Set it as **`SECRETS_ENCRYPTION_KEY`** on every IZ Suite server container that shares the database, including `worker` containers. Never change it afterwards: stored credentials cannot be decrypted under a different key and would have to be re-entered.
3. If you run auto-registering cloud agents, set **`AGENT_WRAPPER_SECRET`** on the server and pass the same value to each agent with `--agentWrapperSecret`.&#x20;

**During the upgrade** the following happen automatically when the new server starts:

* Existing IZ Scan security tokens are stored as one-way hashes. Existing CLI and IDE tokens keep working, but a token can no longer be displayed after it has been generated.
* Stored cloud credentials, secure settings and agent secrets are encrypted with the new key.
* The **`IZ Token Auth`** sign-in option is renamed **`IZ User Auth`** and new **`Login Settings`** entries are added. Users who signed in with an IZ token sign in once with their email and old token, then set a password. See [Sign-in and MFA](../../integral-zone/iz-suite/iz-core/sign-in-and-mfa.md).
* Agent job types are switched to the new per-platform packages. Agents download them on their next job; no agent configuration change is needed.

**After the upgrade**

1. Navigate to **`Global Settings`** → **`Seed Data`** and click **`Trigger Seed Data`** so that the language manifests, the AWS rule packs, PySpark, Java and the Python PEP 8 rules are installed.&#x20;
2. Refresh the licence so that newly licensed modules (AWS services, Java) are listed. AWS services and Java appear only once they are seeded and licensed.
3. Every existing role that holds Python scan permissions on an organization receives the matching Java permissions there on server start. Users see **`Java Apps`** after signing in again.

### Integral Zone-Managed Installation

If the installation is managed by **`Integral Zone`**, the following will be handled as part of the upgrade process:

1. A full backup of the existing database/schema will be taken before the upgrade.
2. In case of an upgrade failure, rollback and recovery will be performed by the Integral Zone team.
3. No manual intervention is required from the client side for backup or rollback if the installation is managed by Integral Zone.

### See Also

* [Server Installation](server-installation.md)
* [Prerequisites](installation-requirements.md)
* [Cluster Mode](../../integral-zone/iz-suite/installation/modes/cluster-installation.md)
