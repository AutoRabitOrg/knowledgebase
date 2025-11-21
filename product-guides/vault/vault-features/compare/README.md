# Vault Compare

## Introduction

The Compare feature in AutoRABIT Vault offers a streamlined method for identifying differences between two data snapshots or between a snapshot and a live Salesforce org. It enables administrators and developers to evaluate record-level variations across objects, supporting accurate assessment of data consistency between backup sets or between a backup and the source environment. This capability is essential for validating data integrity, detecting configuration drift, and confirming that recent updates have been accurately captured and reflected in backups or deployments.

## Overview

The **Compare operation** in AutoRABIT Vault enables comprehensive analysis between two data sources—either **two backup snapshots** or a **backup and a live Salesforce environment**. It helps in identifying record-level and field-level discrepancies, ensuring that data across environments remains synchronized and reliable.

This functionality serves as a powerful validation mechanism for teams managing frequent data changes, releases, or environment refreshes. By visually presenting differences between data sets, Vault empowers administrators to assess impacts, troubleshoot issues, and maintain data consistency across the Salesforce landscape.

#### Key highlights include:

1. **Flexible Comparison Options:**\
   Supports both _Backup Compare_ (snapshot-to-snapshot) and _Live Compare_ (snapshot-to-live org), allowing teams to choose the best approach for their verification needs.
2. **Record-Level Insights:**\
   Displays additions, deletions, and modifications between compared datasets, ensuring complete visibility into what has changed.
3. **Interactive Result Visualization:**\
   Comparison results are displayed in an intuitive, tabular format that allows sorting, filtering, and detailed inspection of individual records.
4. **Compare History Tracking:**\
   Every compare operation is logged in the _Compare History_ section, providing auditability and the ability to re-run previous comparisons when needed.
5. **Configurable Retention Period:**\
   Comparison results are retained for a defined duration (default: 7 days), with an option to modify retention as per organizational requirements.
6. **Re-run Capability:**\
   Enables users to re-execute previous comparisons without redefining configuration parameters, saving time and effort during repeated validation cycles.

#### Use Case Example

For instance, when comparing "**two snapshot versions of Salesforce Accounts data, or comparing the backedup data against the live org"** Vault will highlight all record-level changes such as:

* New records added in the latest snapshot.
* Modified fields in existing records.
* Deleted records that were present in the earlier snapshot.

This helps teams identify discrepancies introduced during deployments or data imports and maintain alignment across their Salesforce environments.
