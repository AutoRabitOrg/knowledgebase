# Release Notes 22.0

## Vault 22.2 Release Notes <a href="#vault-222" id="vault-222"></a>

#### What's New <a href="#whats-new1" id="whats-new1"></a>

**Support for Serial Backups**

With this release, we have added the flexibility to enable your backup configs to run in serial mode. This prevents overlap of backups triggered under the same config and helps reduce redundant data storage caused due to overlapping backups.

[Read more →](../../../product-guides/vault/vault-features/backup/schedule-a-vault-backup.md)

**Access restriction through SSO for non-registered users**

We’ve added the capability to Vault administrator to prevent the auto-creation of new users in Vault from SSO ID providers like OKTA and Microsoft Azure AD.

[Read more →](../../../product-guides/vault/configuring-vault/sso-configuration/sso-for-okta.md)

**Notifications for Restore/Replicate operations**

With this release, we have enhanced the capability of how the users get notified once an operation is performed inside Vault. You will now have a field to add multiple recipients who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be enabled to receive the notifications.

[Read more →](../../../product-guides/vault/vault-features/restore/restoring-the-metadata-data-to-the-salesforce-org.md)
