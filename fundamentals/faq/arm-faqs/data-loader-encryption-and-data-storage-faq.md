# Data Loader

## Encryption

### **Is there any encryption for Data Loader files? We don't want our data or upload files (e.g., CSV files) to be accessible by AutoRABIT or any other party.**

AutoRABIT does not encrypt CSV files. However, the EBS volumes are encrypted using AWS KMS keys.

### **Can a customer's own key be used to encrypt their data? Is this possible?**

Currently, AutoRABIT does not support customer encryption keys for data encryption. This feature is not supported at the moment.

## Data Storage

### **Where is the result data (including exported data) physically stored, and can it be moved to a specific location (e.g., another country)? Can we ensure this data is not stored in AutoRABIT?**

AutoRABIT does not delete data in the Data Loader functionality until the customer deletes it.  For example, the ap5.autorabit.com instance is hosted in an AWS Singapore data center, and the data is stored in EBS volumes with AWS KMS keys in the same region.

## Error Messages

### Why does my Data Loader Pro job fail with an "Invalid ID" error message when the parent object is not selected?

An Invalid ID error occurs while running the Data Loader Pro job from release 23.1.26.

This is a known issue in the Data Loader Pro module. There is an invalid ID error while not selecting the parent object and keeping as null. A fix is available in the ARM 23.1.28 build version.

The customer has a Data Loader Pro job and has two queries:

1. They had to select the ancestor object whenever they ran the Data Loader Pro job.
2. They have tried a few records with null values, and it resulted in multiple object record failure with the error message Invalid ID.

## Feature Overview

### Why does the record fail when trying to update with "null" values?&#x20;

For this to happen, you must choose "Insert/Update with null values" while running the Data Loader Pro job.

_There are instances when you do not want to include ancestor records that haven't changed._ For example: If there are no changes on ancestors, then it is not required to include that Parent object in the job unless it is a Master-Detail relation.

## Feature Considerations

### Why does the current Data Loader setup require parent objects to be included without the Limit 0 option?

The current Data Loader setup in AutoRABIT requires parent objects to be included without the Limit 0 option for the records, causing some records to fail. A code fix has resolved this issue, available in the ARM 23.1.28 build version.&#x20;

## Is AutoRABIT compatible with the deployment of CPQ data? <a href="#is-autorabit-compatible-with-the-deployment-of-cpq-data" id="is-autorabit-compatible-with-the-deployment-of-cpq-data"></a>

Currently, we are supporting CPQ data deployment through Data Loader Pro only. We plan to release a beta version exclusively for CPQ deployments in the coming months.
