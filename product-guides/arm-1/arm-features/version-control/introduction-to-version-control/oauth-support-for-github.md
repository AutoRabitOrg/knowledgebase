---
description: >-
  Note: OAuth is currently supported only for GitHub Cloud repositories. GitHub
  Enterprise repositories must use Standard access type.
---

# OAuth Support for GitHub

## Register a GitHub Repository in ARM Using OAuth

### Overview

GitHub OAuth allows ARM to securely connect to GitHub repositories **without using Personal Access Tokens (PATs)**.\
This method improves security by allowing scoped access and managed authentication through GitHub.

***

## Prerequisites

Before registering a repository in ARM, configure **one of the following applications in GitHub**.

***

### Option 1 — GitHub OAuth App

1. Go to:

```
GitHub → Settings → Developer Settings → OAuth Apps → New OAuth App
```

2. Enter the following details:

* **Application Name**
* **Homepage URL**\
  Example:\
  `https://na15.autorabit.com/`
* **Authorization Callback URL**\
  (Provided by ARM during repository registration)

3. Click **Register Application**.
4. After the application is created, copy:

* **Client ID**
* **Client Secret** (generate a new client secret if required)

***

### Option 2 — GitHub App

GitHub Apps are recommended for automation and integrations.

1. Navigate to:

```
GitHub → Settings → Developer Settings → GitHub Apps → New GitHub App
```

2. Provide the following details:

* **Application Name**
* **Homepage URL**\
  Example:\
  `https://na15.autorabit.com/`
* **Authorization Callback URL** (Provided by ARM)

3. Enable:

* **Expire user authorization tokens**

4. Configure **Repository Permissions**:

| Permission    | Access         |
| ------------- | -------------- |
| Contents      | Read and Write |
| Pull Requests | Read and Write |

5. After creating the app:

* Click **Install App**
* Select your **GitHub organization**
* Complete the installation

6. Copy the following values:

* **Client ID**
* **Client Secret**

***

## Register a Repository in ARM Using OAuth

### Step 1 — Open Repository Registration

1. Log in to **ARM**.
2. Navigate to **Repository Registration**.
3. Click **Add Repository**.

***

### Step 2 — Select Git Provider

In the repository configuration form:

Select:

```
Git Type → GitHub
```

ARM displays the available connection options.

***

### Step 3 — Select OAuth Connection

Choose:

```
Connection Type → OAuth
```

The **OAuth configuration section** appears.

***

### Step 4 — Enter OAuth Configuration

Provide the following details:

| Field         | Description                          |
| ------------- | ------------------------------------ |
| Client ID     | GitHub application client identifier |
| Client Secret | GitHub application client secret     |
| OAuth URL     | Auto-generated authorization URL     |

The **OAuth URL** is generated automatically and cannot be edited.

***

### Step 5 — Validate Configuration

Click **Validate** to verify the configuration and retrieve the repository default branch.

ARM validates:

* Client ID
* Client Secret

If a value is missing, validation messages appear.

Example:

```
Client ID is required
Client Secret is required
```

***

### Step 6 — Authorize GitHub Access

After validation, ARM redirects you to the **GitHub authorization page**.

1. Review the requested permissions.
2. Click **Authorize**.

GitHub then redirects you back to ARM.

***

## Registration Confirmation

After authorization, ARM completes the repository connection.

The repository details are displayed:

| Field             | Value               |
| ----------------- | ------------------- |
| Repository Name   | Selected repository |
| Git Type          | GitHub              |
| Connection Type   | OAuth               |
| Connection Status | Connected           |

A confirmation message indicates that the repository has been **successfully registered**.

***

## Note

GitHub supports two integration methods: **OAuth Apps** Or **GitHub Apps**.

* **GitHub OAuth App**\
  The application accesses GitHub **on behalf of a user**. Permissions are granted using broader scopes such as `repo` or `user`.
* **GitHub App**\
  The application accesses GitHub **as an application** and uses **fine-grained permissions** that can be limited to specific repositories.

**Key Difference:**\
OAuth Apps access GitHub **as a user**, while GitHub Apps access GitHub **as an application with controlled repository permissions**, making them more secure for integrations and automation.
