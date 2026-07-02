# Teams(WorkFlows)

## Configure Microsoft Teams Workflows Webhook for ARM Notifications

***

## Overview

Microsoft is deprecating **Office 365 Connectors** and **Incoming Webhooks** in Microsoft Teams. To continue receiving ARM notifications in Microsoft Teams, customers must migrate to the new **Microsoft Teams Workflows** webhook integration.

This guide explains how to:

* Create a Microsoft Teams Workflow webhook
* Generate the Workflows webhook URL
* Configure the webhook in ARM
* Map notification events to Teams channels

***

## Prerequisites

Before configuring the integration, ensure the following:

* Microsoft Teams desktop or web application
* Permission to install Microsoft Teams apps (or Workflows app already installed)
* ARM Administrator access
* A Microsoft Teams Team and Channel where notifications will be posted

***

## Step 1: Install the Microsoft Teams Workflows App

1. Open **Microsoft Teams**.
2. Click **Apps** from the left navigation.
3. Search for **Workflows**.
4. Click **Install**.

> **Note:** If the Workflows app is already installed, you can skip this step.

***

## Step 2: Create or Select a Teams Channel

Create a new Team/Channel where ARM notifications should be posted.

If you already have an existing channel, you can use it directly.

***

## Step 3: Open Workflows from the Channel

1. Navigate to the required Teams channel.
2. Click the **More options (⋯)** menu.
3. Select **Workflows**.

<figure><img src="../../../../.gitbook/assets/image (2561).png" alt=""><figcaption></figcaption></figure>

***

## Step 4: Create a Webhook Workflow

From the available templates:

Select:

**Send webhook alerts to a channel**

<figure><img src="../../../../.gitbook/assets/image (2562).png" alt=""><figcaption></figcaption></figure>

This template creates a webhook endpoint that external applications (such as ARM) can use to send notifications.

***

## Step 5: Select Team and Channel

Choose:

* **Team**
* **Channel**

where notifications should be delivered.

Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (2563).png" alt=""><figcaption></figcaption></figure>

***

## Step 6: Copy the Webhook URL

After saving the workflow:

1. Open the newly created workflow.
2. Click **Copy webhook link**.
3. Save the generated URL.

<figure><img src="../../../../.gitbook/assets/image (2564).png" alt=""><figcaption></figcaption></figure>

This URL will be required while configuring ARM.

***

## Step 7: Configure Microsoft Teams in ARM

Navigate to:

**ARM → Settings → Notifications**

Expand:

**Teams/Slack Settings**

Select the **Microsoft Teams** tab.

<figure><img src="../../../../.gitbook/assets/image (2567).png" alt=""><figcaption></figcaption></figure>

***

### Add Notification Channel

**Add Channel**

Provide:

| Field                   | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| Channel Name            | Friendly name for identification (Example: Production Notifications) |
| Webhook Integration URL | Paste the Microsoft Teams Workflows webhook URL copied earlier       |

Click **Test Connection**.

If the test succeeds, click **Save**.

***

## Step 8: Configure Notification Events

After adding the Teams channel:

Navigate to:

**Configure Notification Channels**

Choose which ARM events should send notifications to Microsoft Teams.

Examples include:

### CI Jobs

* CI Job Failed Report
* CI Job Success Report

### EZ-Commit

* Gated Check-ins
* Pre-Validation Approval
* Pre-Validation Rejection
* Mentioned Comments

### Environment

* Environment Provision

### Merge

* Merge Expiration Report

> Select the Teams channel created in the previous step for each required notification.

Click **Save**.

Sample Notifications:

<figure><img src="../../../../.gitbook/assets/image (2566).png" alt=""><figcaption></figcaption></figure>

<br>
