# Release Notes 24.1

## nCino Release Notes 24.1

**Release Date: 16 June 2024**

### Overview

nCino 24.1 is a major release which encompasses the following release items:&#x20;

* **nCino Compare Functionality**
* **Enhanced Data Loader Pro Job Configuration** &#x20;
* **Exclude the OwnerID from Automapping in nCino CI jobs**&#x20;
* **Data Loader Pro Job Run Options in Configuration**
* **Triggering nCino CI Jobs Using REST API**
* **Select external unique identifier During nCino Feature Deployment**

**New Features**

1.  **nCino Compare Functionality**

    **Overview:** This provides users with enhanced control and insight into the deployment of nCino Record-Based Configurations (RBC). \
    **Application:** The nCino RBC Comparison Tool allows users to effortlessly compare RBC configurations between those ready for deployment and those already existing in the target environment. This comparison ensures that users can identify discrepancies, confirm consistency, and make informed decisions before finalizing deployments. \
    **Benefit:** This tool addresses the need for a reliable method to ensure consistency and accuracy in RBC deployments, reducing the risk of configuration errors and streamlining the configuration management process.\
    **Additional Information:** For more detailed information, please refer to our Knowledge Base.\

2.  **Enhanced Data Loader Pro Job Configuration**\
    **Purpose:** To provide users with greater flexibility and control over the data loading process by allowing the users to enable and disable the validation rules, workflow rules, and triggers.

    **Overview:** Users can now enable or disable validation rules, workflow rules, and triggers as part of the Data Loader Pro job configuration. This feature allows users to leverage pre-configured selections during the scheduled execution of the job, ensuring that the data-loading process adheres to their specific requirements.

    **Resolution** Enhances flexibility and control over the data loading process, enabling users to customize job configurations to meet their unique needs and reducing the risk of unintended rule or trigger executions.

    **Further documentation:** For more detailed information, please refer to our Knowledge Base.\

3.  **Triggering nCino CI Jobs Using REST API**\
    **Purpose:** Customers can now trigger nCino CI (Continuous Integration) jobs using the provided API endpoints.

    **Describe how and/or why it works:** This enhancement simplifies and automates the Continuous Integration (CI) process for nCino users by allowing them to trigger CI jobs through REST API calls. With this capability, users can integrate CI job execution seamlessly into their existing automation workflows or CI/CD pipelines. By leveraging API endpoints, users gain greater flexibility and control over the CI process, enabling efficient and consistent integration testing and deployment.

    **Issue Resolved:** Addresses the need for streamlined and automated CI processes by providing customers with the ability to trigger nCino CI jobs via API endpoints. This enhancement improves efficiency, reduces manual intervention, and enhances the overall CI experience for users.

    **Further documentation:** For more detailed information, please refer to our Knowledge Base.\


### Enhancements

1.  **Exclude the OwnerID from Automapping in nCino CI jobs**

    **Overview:** Users can now disable the auto-mapping of ownerIDs between environments within the application.

    **Application:** This new option allows users to prevent the automatic mapping of ownerIDs during record-based configuration migration. This is particularly useful in scenarios where developers in lower environments, such as a development sandbox, have the necessary privileges to own configuration records but lack similar access in higher environments like QA or production. By disabling auto-mapping, users can manually set appropriate ownerIDs, ensuring a smoother and more controlled migration process.

    **Benefit:** Helps avoid issues encountered during record-based configuration migration due to limited access to record owners in higher environments. This enhancement ensures that migrations do not fail or cause access-related issues, improving the reliability and consistency of deployments across different environments.

    **Further documentation:** For more detailed information, please refer to our Knowledge Base. \
    &#x20;
2.  **Data Loader Pro Job Run Options in Configuration**

    **Overview:** All job run options can now be configured when creating a job in Data Loader Pro.

    **Application:** This enhancement allows users to set all desired job run options at the time of job creation, providing greater customization and control over Data Loader Pro job executions. These configurations are preserved for the scheduled execution of the jobs, ensuring that each job runs with the specified settings without the need for manual adjustments before each execution.

    **Benefit:** Enhances customization and control over Data Loader Pro job executions and ensures that job settings are consistently applied during scheduled runs, reducing the risk of errors and improving efficiency.

    **Further documentation:** For more detailed information, please refer to our Knowledge Base.\

3.  **Select External Unique Identifier During nCino Feature Deployment**

    **Overview:** Users now have the option to select the external unique identifier instead of AutoRABIT external ID for deployments.

    **Application:** This enhancement provides users with the flexibility to choose an external unique identifier for deployments, rather than relying solely on AutoRABIT's external ID. This feature ensures accurate data transfer and eliminates the risk of record duplication by allowing users to select an identifier specific to their environment or requirements, such as an external system ID or a custom unique identifier. Users can now confidently deploy data outside of AutoRABIT or in refreshed sandboxes without encountering issues related to record duplication.

    **Benefit:** Addresses the potential for record duplication when transferring data outside of AutoRABIT or deploying default data in refreshed sandboxes. By enabling users to select an external unique identifier, this enhancement mitigates the risk of duplication and ensures data integrity during deployments.

    **Further documentation:** For more detailed information, please refer to our Knowledge Base.
