# Vault Connect Salesforce Administrator User Guide

Vault Connect Setup Guide for Salesforce Administrators

### Overview

Setting up Vault Connect in a Salesforce org takes two parts, done in order: install the AuthHub package first, then configure Vault Connect. When you finish, the org is connected to AutoRABIT Vault and the objects to protect are configured.

| **Part**               | **What you do**                                                                          | **Where it's documented**                              |
| ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 1. AuthHub package     | Install and configure the AuthHub package                                                | AuthHub Package Installation Guide (PDF, linked below) |
| 2. Vault Connect setup | Assign access, connect using the API Token from the Vault Application, configure objects | This page                                              |

This guide is for Salesforce administrators who set up Vault Connect in a customer or internal org.

### Before you begin

Check that you have these before you start Part 1.

* System Administrator access to the target Salesforce org, so you can install packages and assign permission sets
* A login to the AutoRABIT Vault application, so you can generate the API Token
* The name of the Salesforce user who will administer Vault Connect

### Part 1: Install the AuthHub package

Vault Connect depends on AuthHub, so install and configure AuthHub before anything else.

1\. Open the **AuthHub Package Installation Guide:** [https://autora-my.sharepoint.com//g/personal/harshit%5Fkumar%5Fautorabit%5Fcom/IQDc4XFjjKq2RpASpz8IHFaqAbhw1GSbpMEaV%5FSLzaliiHA?e=uSbEmo](https://autora-my.sharepoint.com/:b:/g/personal/harshit_kumar_autorabit_com/IQDc4XFjjKq2RpASpz8IHFaqAbhw1GSbpMEaV_SLzaliiHA?e=uSbEmo) Restricted content

2\. Complete every step in that guide, including the configuration steps after installation.

3\. Return to this page and continue with Part 2.

**Note:** Don't start Part 2 until AuthHub is fully configured. The Vault Connect steps assume the AuthHub package is already in place.

## Part 2: Set up Vault Connect

With AuthHub installed, give an admin user access to Vault Connect, connect the org with an API token, and choose the objects to protect.

### Step 1: Assign the Vault Connect Admin permission set

The **Vault Connect Admin** permission set lets the user see the Vault Connect app and set up the connection.

1\. In Salesforce, go to **Setup > Users > Users**.

2\. Click the name of the user who will administer Vault Connect.

3\. In the **Permission Set Assignments** related list, click **Edit Assignments**.

<figure><img src="../../../../.gitbook/assets/image (3258).png" alt=""><figcaption></figcaption></figure>

&#x20;                                       Permission Set Assignments on the Salesforce user record

4\. Under **Available Permission Sets**, select **Vault Connect Admin** and click **Add**.

5\. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (3259).png" alt=""><figcaption></figcaption></figure>

&#x20;                                       Vault Connect Admin in Available Permission Sets

**Access levels:** Vault Connect has two permission sets. Assign **Vault Connect Admin** only to the people who set up and maintain the connection.

| **Permission set**  | **Can do**                                                                                     | **Cannot do**                                                         |
| ------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Vault Connect Admin | Connect the org with an API token, configure objects and their fields, view configured objects | Nothing in Vault Connect is restricted                                |
| Vault Connect User  | View the objects that have been configured                                                     | Connect the org, add or remove objects, or change field configuration |

### Step 2: Open Vault Connect

1\. Log in to Salesforce as the user from Step 1.

2\. Click the **App Launcher** (the grid icon at the top left).

3\. Search for **Vault Connect** and open it.

<figure><img src="../../../../.gitbook/assets/image (3260).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Vault Connect in the App Launcher

### Step 3: Get the API Token from the Vault Application

1\. Log in to the **AutoRABIT Vault** application.

2\. Go to the Vault Connect Tab.

3\. Select token management tab and click Generate API Token.

4\. Generate the API Token for this Salesforce org and copy it.

<figure><img src="../../../../.gitbook/assets/image (3261).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Vault Connect navigation in AutoRABIT Vault

<figure><img src="../../../../.gitbook/assets/image (3262).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Generate Connection Token

<figure><img src="../../../../.gitbook/assets/image (3263).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Token Generated Successfully

**Important:** Treat the API token like a password. Don't share it over email or chat, and don't store it in plain text. Each token works for one Salesforce org only.

### Step 4: Connect the org to AutoRABIT Vault

1\. Back in Vault Connect, on the welcome screen, click **Have an API Token**.

<figure><img src="../../../../.gitbook/assets/image (3264).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Vault Connect welcome screen

2\. On the **Connect AutoRABIT Vault** screen, paste the API Token you copied from the Vault Application into the **API Token** field.

3\. Click **Connect**.

<figure><img src="../../../../.gitbook/assets/image (3265).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Connect AutoRABIT Vault

4\. Wait for the message **Connected securely to AutoRABIT Vault**.

<figure><img src="../../../../.gitbook/assets/image (3266).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Connected securely to AutoRABIT Vault

### Step 5: Configure objects

1\. Click **Next Step: Object Discovery**.

2\. Select the Salesforce object and click the **Configure Fields..**

<figure><img src="../../../../.gitbook/assets/image (3267).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Object Discovery and Configure Fields

3\. Select the fields from the **Available Fields** tab and click **Save Changes**.

<figure><img src="../../../../.gitbook/assets/image (3268).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Available Fields and Save Changes

4\. After the configuration done for the desired objects click **Go to Configured Objects** to see the configured object list.

<figure><img src="../../../../.gitbook/assets/image (3269).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Go to Configured Objects

<figure><img src="../../../../.gitbook/assets/image (3270).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                            Configured objects list

### Troubleshooting

| **Problem**                                      | **What to check**                                                                                                                            |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Vault Connect is missing from the App Launcher   | Confirm the user has the Vault Connect Admin permission set (Step 1), then log out and back in.                                              |
| Connecting fails with an invalid-token error     | Make sure the token was generated for this Salesforce org and copied in full, with no extra spaces. If it still fails, generate a new token. |
| Vault Connect setup steps don't work as expected | Confirm the AuthHub package from Part 1 is installed and fully configured.                                                                   |

Once setup is done, give view-only access by assigning the **Vault Connect User** permission set to anyone who needs to see the configured objects without changing them.
