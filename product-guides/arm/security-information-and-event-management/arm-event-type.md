# ARM Event Type

The following is a list of ARM event types:

| S. No. | Event Type             | Module Related                        | Descriptions |
|--------|------------------------|---------------------------------------|--------------|
| 1      | **LOGIN**              | Admin                                 | - Login via Username and Password: **UWP**<br>- Via APIs:<br>  1. VSCode: **apiToken**<br>  2. Channel Secure Login: **ChannelSecure**<br>  3. Modernization: **jwtToken** |
| 2      | **DEPLOYMENT**         | CI Jobs, Deployment, Version Control  | - **CI Jobs**:<br>  1. CI Job Deployment<br>  2. Quick Deployment<br>  3. Rollback Deployment<br><br>- **Deployment Module**:<br>  1. Deployment:<br>  - Custom Deployment<br>  - Profile Manager<br>  - Org Synchronization<br>  2. Quick Deployment<br>  3. Rollback<br><br>- **Version Control**:<br>  1. Commit Validation<br>  2. Merge Validation<br><br>- **Salesforce DX**:<br>  1. Scratch Org creation and deployment |
| 3      | **CIBUILD**            | CI Jobs                               | - Trigger Build<br>- Build History |
| 4      | **DATALOADER**         | Single Dataloader                     | - Extract<br>- Insert<br>- Upsert<br>- Update<br>- Delete |
| 5      | **FEATUREDEPLOYMENT**  | nCino                                 | All events related to the **Feature Deployment** module |
| 6      | **DATARETRIEVALMIGRATION** | nCino                             | All Salesforce events involving data migration and retrieval |
| 7      | **FEATURECREATION**    | nCino                                 | Events related to Feature Creation |
| 8      | **DATALOADERPRO**      | Dataloader Pro                        | - Upsert<br>- Data Masking<br>- Applied Mapping<br>- Filters |
| 9      | **DATALOADERCONFIGURATION** | Dataloader                       | All events related to Dataloader Configurations |
| 10     | **TESTENVIRONMENTSETUP** | Dataloader                          | - Upsert<br>- Applied Mappings |
| 11     | **EZCOMMIT**           | Version Control                       | Prevalidate Commit and EZ-Commit |
| 12     | **MERGE**              | Version Control                       | Dry Run, Prevalidate Merge, and Merge only |
