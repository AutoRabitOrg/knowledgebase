# How to Include Network Settings in Commit or Deployment

## Overview

This guide outlines the steps to include network settings during a commit or deployment in AutoRABIT. Following these steps ensures that network access configurations are properly managed and deployed.

### Steps to Include Network Settings

1. **Metadata Retrieval in EZ-Commit / Deployment**
   * During the **metadata retrieval stage** of an EZ-Commit or Deployment job, ensure the **`security`** metadata is included under the **`settings`** section.
   * This step ensures that network-related configurations, including IP ranges and login IPs, are captured for commit or deployment.
2. **Compare Changes Stage**
   * In the **Compare Changes** stage, review all **Network Access** changes included in the commit. This is particularly important for **existing commits** (ex commits).
   * Use this stage to validate that all required network settings have been accurately captured.

***

> **Important Note:**\
> For secure and efficient deployments, it is **recommended to grant IP access based on the deployment profile**. This ensures that only the necessary IP ranges are permitted, maintaining both compliance and security standards.
