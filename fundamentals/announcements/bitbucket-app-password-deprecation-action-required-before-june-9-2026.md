# Bitbucket App Password Deprecation – Action Required Before June 9, 2026

### Overview

Atlassian is deprecating **Bitbucket Cloud App Passwords** effective **June 9, 2026**. After this date, App Passwords will no longer be supported for authentication and any integrations, automation, or API operations that rely on App Passwords may fail.

To avoid service disruptions, all users currently using Bitbucket App Passwords must migrate to **Bitbucket API Tokens** before the deadline.

***

### Who Is Impacted?

You are impacted if you use Bitbucket App Passwords for:

* API integrations
* CI/CD pipelines
* Automation scripts
* Third-party integrations
* Repository operations performed over HTTPS authentication

#### Not Impacted

Users who authenticate using **SSH keys** for Git operations are **not affected** by this change and do not need to take any action.

***

### Required Actions

#### 1. Replace App Passwords with API Tokens

If your integrations, scripts, or tools currently use Bitbucket App Passwords, update them to use **Bitbucket API Tokens**.

Review all automation, integrations, and configuration settings to identify and replace any stored App Password credentials.

#### 2. Update API Authentication Credentials

As part of this change, Bitbucket now requires the **email address associated with the Bitbucket account** for API authentication.

**Previous Behavior**

* Git Operations: Username
* API Operations: Username

**New Behavior**

* Git Operations: Username
* API Operations: Email Address (mandatory)

Any API integrations that currently use only the Bitbucket username must be updated to use the account's registered email address along with the API Token.

**User Guide(ARM)**

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/getting-started-1/registration/version-control-repository/bitbucket/configuring-bitbucket-token-authentication-and-email-support" %}

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm/registration/version-control-repository/bitbucket/configuring-bitbucket-token-authentication-and-email-support" %}
