# Create New Branch During Deployment

## 1. Introduction

This document explains the process of creating a new branch directly from the nCino application Deployment workflow. It covers how to configure repository details, define branch attributes, and create credentials if required. This functionality enables seamless branch creation without leaving the deployment setup flow.

## 2. Use Case

Deploy metadata changes to a new branch that does not yet exist in the repository. Rather than leaving the deployment flow to update version control settings, the branch can be created directly from the nCino application during deployment configuration, helping maintain context and improve efficiency.

## 3. Feature Overview

The Create Branch feature in the nCino application allows branch creation within the Deployment > Destination stage. It provides options to:

·       Define a new branch name

·       Select a parent branch

·       Assign branch type (for example, QA, UAT, or Production)

·       Configure repository credentials

·       Immediately use the created branch in deployment

This reduces context switching and accelerates release workflows.

## 4. Feature Considerations

·       Repository access must be configured prior to branch creation.

·       Valid credentials are required to authenticate branch creation.

·       Parent branch selection is mandatory.

·       Branch type must align with the organization’s branching strategy.

·       Permissions must allow branch creation in the selected repository.

## 5. Step-by-Step Guide

### Step 1: Navigate to Destination Stage

·       Access the Deployment workflow.

·       Move to Step 3: Destination.

·       Enable the Commit to toggle.

·       Select the required Repository.

### Step 2: Initiate Branch Creation

·       Click the + (Create new branch) icon next to the Branch field.

<figure><img src="../../../../../.gitbook/assets/image (2503).png" alt=""><figcaption></figcaption></figure>

·       The Create Branch panel opens on the right side of the screen.

<figure><img src="../../../../../.gitbook/assets/image (2504).png" alt=""><figcaption></figcaption></figure>

### Step 3: Enter Branch Details

·       Provide a Display Name, such as QA\_New\_Branch.

·       Select a Parent Branch from the dropdown, such as ST-1.

### Step 4: Select Branch Type

Choose the appropriate Branch Type from the available options:

·       Development

·       Integration

·       QA

·       UAT

·       Production

<figure><img src="../../../../../.gitbook/assets/image (2505).png" alt=""><figcaption></figcaption></figure>

### Step 5: Configure Credentials

Select an existing Credential from the dropdown.

<figure><img src="../../../../../.gitbook/assets/image (2506).png" alt=""><figcaption></figcaption></figure>

OR

Click the + (Add Credential) icon to create a new credential.

<figure><img src="../../../../../.gitbook/assets/image (2507).png" alt=""><figcaption></figcaption></figure>

#### Credential Creation

·       Enter the credential Name.

<figure><img src="../../../../../.gitbook/assets/image (2508).png" alt=""><figcaption></figcaption></figure>

·       Select the credential Type, such as Username with Password, SSH, CA, HashiCorp Vault, SSH Certificate, or Application Token.

·       Choose the Scope as Global or Private.

<figure><img src="../../../../../.gitbook/assets/image (2509).png" alt=""><figcaption></figcaption></figure>

·       Provide the required authentication details, such as Username and Token/Password.

<figure><img src="../../../../../.gitbook/assets/image (2510).png" alt=""><figcaption></figcaption></figure>

·       Click Save.

### Step 6: Create the Branch

·       After completing all required fields, click Create.

<figure><img src="../../../../../.gitbook/assets/image (2511).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2512).png" alt=""><figcaption></figcaption></figure>

·       A success message appears: Branch created successfully.

<figure><img src="../../../../../.gitbook/assets/image (2513).png" alt=""><figcaption></figcaption></figure>

### Step 7: Verify Branch Selection

·       The newly created branch is automatically populated in the Branch dropdown.

·       Add a Commit Comment if required.

### Step 8: Proceed with Deployment

·       Click Next to continue to the next stage.

## 6. Prerequisites

·       Repository must be integrated with the nCino application.

·       Valid credentials must exist or be created.

·       Appropriate permissions to create branches must be available.

## 7. Conclusion

The Create Branch feature in the nCino application streamlines deployment workflows by enabling in-context branch creation. It eliminates dependency on external tools, ensures faster setup, and maintains continuity within the deployment process.







