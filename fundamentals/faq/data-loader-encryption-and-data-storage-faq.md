# Data Loader Encryption and Data Storage - FAQ

#### Frequently Asked Questions

**1. Is there any encryption for Data Loader files? We don't want our data or upload files (e.g., CSV files) to be accessible by AutoRABIT or any other party.**

**Answer:** AutoRABIT does not encrypt CSV files. However, the EBS volumes are encrypted using AWS KMS keys.

**2. Can a customer's own key be used to encrypt their data? Is this possible?**

**Answer:** Currently, AutoRABIT does not support customer encryption keys for data encryption. This feature is not supported at the moment as confirmed by our product team.

**3. Where is the result data (including exported data) physically stored, and can it be moved to a specific location (e.g., Another country)? Can we ensure this data is not stored in AutoRABIT?**

**Answer:** AutoRABIT does not delete data in the Data Loader functionality until the customer deletes it.  For example, The ap5.autorabit.com instance is hosted in an AWS Singapore data centre, and the data is stored in EBS volumes with AWS KMS keys in the same region.

For any further questions on this topic, please respond to this email. For new issues, kindly open a new ticket.
