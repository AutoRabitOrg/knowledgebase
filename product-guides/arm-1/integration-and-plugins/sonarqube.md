# SonarQube

## Overview

SonarQube is an automated code review tool that helps detect bugs, security vulnerabilities, and maintainability issues (code smells). It integrates with your development workflows, enabling continuous inspection of your project branches and pull requests.

***

## SonarQube Concepts

### Architecture

| Concept  | Definition                                                            |
| -------- | --------------------------------------------------------------------- |
| Analyzer | A client that analyzes source code and computes snapshots.            |
| Database | Stores configuration and snapshots.                                   |
| Server   | Web interface for browsing snapshot data and managing configurations. |

### Quality

| Concept          | Definition                                                          |
| ---------------- | ------------------------------------------------------------------- |
| Clean Code       | Reliable, secure, maintainable code adhering to defined attributes. |
| Bug              | A code issue that may cause a failure. Needs immediate fixing.      |
| Code Smell       | A maintainability issue. Increases developer confusion and risk.    |
| Technical Debt   | Estimated time to fix code smells.                                  |
| Issue            | A violation of a coding rule in source or test files.               |
| Measure          | Metric value for a file/project at a given time.                    |
| Metric           | A type of measurement (e.g., LOC, complexity).                      |
| Quality Profile  | Set of rules used in a project.                                     |
| Remediation Cost | Estimated time to fix reliability/security issues.                  |
| Snapshot         | A project’s analysis result at a given time.                        |
| Security Hotspot | Code that needs manual review for potential vulnerabilities.        |
| Rule             | Coding standards to avoid issues and vulnerabilities.               |

***

## Setting Up SonarQube in AutoRABIT

### Step 1: Generate a SonarQube Token

1. Log in to your SonarQube instance.
2. Navigate to **User > My Account > Security**.
3. Generate a new token and **copy it** immediately.
4. Use this token when storing credentials in AutoRABIT.

### Step 2: Store SonarQube Credential in AutoRABIT

1. In AutoRABIT, go to **Admin > Credentials**.
2. Click **Create Credential**.
3. Enter:
   * **Credential Name**
   * **Credential Type**: "User name with Password"
   * **Scope**: Global or Private
   * **Username**: SonarQube username (not email)
   * **Password**: Paste the token from Step 1
4. Click **Save**.

![Credential Setup](<../../../.gitbook/assets/image (873).png>)

***

### Step 3: Integrate SonarQube with AutoRABIT

1. Go to **Admin > My Account > Plugins**.
2. Check **SonarQube** under **Static Code Analysis**.
3. Provide:
   * **SonarQube URL** (e.g., `https://sonarcloud.io`)
   * **Host Type**: Cloud or On-premise
   * **Organization Key** (if using SonarCloud)
   * **Select Credential**
4. Click **Test Connection**, then **Save**.

![Plugin Setup](<../../../.gitbook/assets/image (875).png>)

***

### Step 4: Configure SonarQube Quality Gate Criteria

1. Go to **Admin > My Account**.
2. Under **Validation Criteria - Static Code Analysis**:
   * Enable **SonarQube**
   * Set the **Quality Gate** status (default: ERROR)
   * Click **Save**

![Validation Setup](<../../../.gitbook/assets/image (876).png>)

***

### Step 5: Commit Validation Approval Settings

1. Under **Commit Validation - Approval Settings**:
   * Enable **criteria-based Review Process**
   * Enable:
     * **Should pass validation criteria for Static Code Analysis**
     * **SonarQube**
     * **Auto reject commit process if criteria are not met**
2. Click **Save**

![Commit Validation](<../../../.gitbook/assets/image (877).png>)

***

### Step 6: Merge Settings (Optional)

1. Under **Merge Settings**:
   * Enable **criteria-based Review Process**
   * Enable **SonarQube**
2. Click **Save**

***

Once configured, SonarQube will be enforced during commits, CI builds, and merges within AutoRABIT, ensuring only clean and secure code progresses through the pipeline.
