# Release Notes 24.1

## ARM Release Notes 24.1 <a href="#arm-release-notes-23-1" id="arm-release-notes-23-1"></a>

**June 2024**

**Version 24.1 – Enhancements and Improvements**

### Enhancements

1. **Perform Validation Deployment for Multiple Orgs**\
   In this release, we're thrilled to introduce an enhanced **Validate Deployment** feature, responding to a key user request. Users can now choose multiple orgs simultaneously, enabling a forward-looking validation process as they promote from one sandbox to the next and eventually to production. This time-saving enhancement allows users to select up to three organizations from a convenient multi-picklist, and the subsequent summary screen provides a consolidated view of the deployment results for each selected organization. The implementation ensures a seamless experience by allowing users to toggle between different org validations. The introduction of this feature in the EZ-Merge and EZ-Commit options streamlines deployment validations, contributing to a more efficient and informed deployment workflow.\
   \

2. **Incorporated Checkbox to Skip Prevalidation Criteria**\
   In this release, we're excited to introduce the ability for developers to **skip all prevalidation criteria** specifically for **back merges from designated branches**. This enhancement offers a streamlined approach to the back merge process, empowering developers to improve efficiency and simplify code migration upstream. To leverage this feature, developers can configure the branch type in VC Repos → Branch settings, where a new checkbox option allows you to enable skipping prevalidation criteria for a particular branch during back merges. This capability enhances flexibility and productivity, reducing unnecessary steps in the code migration workflow. With the skip option, developers have greater control over the back merge process, ensuring a smoother and more agile development experience.\
   \

3. **Revamped Static Code Analysis View**\
   We’ve revamped our static code analysis UI to enhance the user experience. Now, errors are conveniently displayed under selected files, streamlining issue identification and resolution across various tools.\
   \

4. **Streamlined EZ-Commit Editing**\
   This release significantly enhanced the EZ-Commit workflow to empower developers. The introduction of an integrated **Compare Changes** option in the **Review Artifact** screen allows for seamless viewing, editing, and visualizing of Salesforce metadata changes in a single, user-friendly interface. Developers can now effortlessly navigate and understand their code edits with color-coded differences, eliminating the need to toggle between multiple screens. This streamlined process enhances the user experience and addresses a crucial blocker in the journey towards CI/CD, providing a more efficient and intuitive path for developers.\
   \

5. **Enhanced SCA Label Scheduling**\
   In this release, users can now enjoy enhanced control over SCA label scheduling with the introduction of the ability to edit/update schedules. This feature provides greater flexibility, allowing users to modify scheduled times for SCA labels, contributing to a more seamless and user-friendly experience in managing job schedules.\
   \

6. **New Email Templates Implementation**\
   In this release, a significant enhancement has been made by implementing new email templates that align with current visualization standards. This update reflects our commitment to maintaining high standards in user interface design and enhancing overall user engagement.\


### Improvements

This update improves the tool's efficiency and responsiveness and leverages new technologies, collectively resulting in a smoother, faster user experience.

1. In this release, we revolutionized the system by converting all JSP pages into a RESTful API, enhancing modularity, scalability, and interoperability.
2. SF CLI Version upgrade to 2.41.8
3. SOAP to REST services upgrade: Upgrading from SOAP to REST services improves performance by reducing overhead with lightweight JSON payloads and enhances security through stateless communication and simplified implementation of HTTPS.
4. By merging SalesforceDxHub into SalesforceOrg, it effectively reduces redundancy in data storage. Users can now register once from SalesforceOrg, with the added capability to specify a registered org as a Dev hub. When a production org is registered as a Dev hub, it appears on both screens, streamlining data management and enhancing user workflow. This release optimizes data storage, improves user experience, and simplifies registration processes, ultimately enhancing overall system efficiency.
5. Upgrade of third-party libraries
6. Salesforce integration credentials (Client ID & Secret) are now encrypted for improved security. Existing tokens are also migrated to the new format. This enhances protection against unauthorized access.
7. Log-leveling: Dynamically modify log levels for specific logger categories to enhance monitoring and troubleshooting.



### nCino Improvements

See the recent updates to [nCino release 24.1](../ncino-release-notes/release-notes-24.1.md) notes as well.&#x20;