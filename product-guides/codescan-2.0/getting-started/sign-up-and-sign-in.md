---
description: >-
  How to create a CodeScan account and sign in to the web app, the CLI and VS
  Code.
---

# Sign Up and Sign In

**Step 2 of Getting Started.**

This article explains how to create a CodeScan account and sign in to the web app, the CodeScan CLI and the VS Code extension.

{% hint style="danger" %}
**\[TO CONFIRM before publishing]** The sign-up flow is not yet documented. Confirm:

* Where customers sign up (trial landing pages, or an invitation from AutoRABIT)
* The fields on the sign-up form, and the terms customers accept
* Whether multi-factor authentication or single sign-on is available
* How an administrator invites other users and assigns roles
{% endhint %}

### Signing Up

1. Go to <mark style="color:red;">**\[TO CONFIRM: sign-up URL]**</mark>.
2. <mark style="color:red;">**\[TO CONFIRM: sign-up steps]**</mark>

<mark style="color:red;">**\[SCREENSHOT: sign-up form]**</mark>

### Signing In to the Web App

1. Go to your CodeScan URL, `https://<your-codescan-url>`.
2. Enter your CodeScan username and password. <mark style="color:red;">**\[TO CONFIRM: exact field labels and button name]**</mark>

After you sign in, CodeScan opens on your project cards. Each card shows the last scan, open issues, and counts for Security, Structure and Code Analysis.

<mark style="color:red;">**\[SCREENSHOT: project cards after sign-in]**</mark>

### Inviting Users

<mark style="color:red;">**\[TO CONFIRM: how an administrator adds users and assigns roles]**</mark>

For what each role can do, see Users, Roles and Permissions.

### Signing In to the CLI and VS Code

The CodeScan CLI and the VS Code extension sign in with an API key, or with your CodeScan username and password. They share the same stored sign-in on your computer, so signing in to one also signs in the other.

* **CLI:** run `codescan config` and follow the prompts. See Connect the CLI.
* **VS Code:** open the Command Palette and run **`CodeScan: Sign In`**. See Using the VS Code Extension.

{% hint style="info" %}
**Note:** Only administrators can create API keys. If you need one, ask your CodeScan administrator. See Create and Manage API Keys.
{% endhint %}

### Next Step

Register a Repository

### Related Articles

* Getting Started
* Users, Roles and Permissions
* Create and Manage API Keys
