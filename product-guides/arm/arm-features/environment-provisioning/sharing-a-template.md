# Sharing a Template

### Environment Provisioning: Template Sharing for Subusers (Custom Admin Configuration)

#### Overview

The Environment Provisioning module now supports enhanced template sharing capabilities, enabling better collaboration and reducing dependency on Admin users.

This update allows Subusers to share templates they create, while maintaining control and governance over shared resources.

***

#### What’s New

**🔹 Subuser Template Sharing**

Subusers can now share **only the templates they own**, enabling faster collaboration without requiring Admin intervention.

**🔹 Admin Capabilities (Unchanged)**

Admins continue to have full control and can share **any template**, regardless of ownership.

***

#### How It Works

**👤 For Subusers**

* You can **share templates that you have created**.
* The **Share option will be enabled** only for your own templates.
* For templates created by other users:
  * The Share option will be **disabled or hidden**.

**👑 For Admin Users**

* You can **share any template** in the system.
* No changes have been made to existing Admin functionality.

***

#### UI Behavior

| Scenario                          | Share Option Visibility |
| --------------------------------- | ----------------------- |
| Subuser viewing own template      | Enabled                 |
| Subuser viewing others' templates | Disabled/Hidden         |
| Admin viewing any template        | Enabled                 |
