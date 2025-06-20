# Deploy from version control & Deploy using salesforce and version control

Follow the following flow to create a CI Job.

1.  Click on the **"Create"** drop-down to select the "Feature CI Job" option

    <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
2.  Either select the **"Create feature CI job"**, to initiate a CI job from the **"CI Job List"**.

    <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
3.  Initiating the  "Feature CI Job" creation will land on the following **"CI Jobs - Source Type"** page.

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4. **CI Jobs "Source Type" page will have the following options:**
   1. **Deployment from, template configuration**: The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control.
   2. **Deploy using salesforce template**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, and based on the configurations, the data is pulled from the source org and later deployed to the destination environment.
   3. **Deploy from version control**: The only difference between this and the Feature Migration template deployment is that here the template is picked up, which is part of version control. Such data is pulled from the version control and deployed to the destination.
   4. **Deploy using Salesforce and version control**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.
5.  **Prerequisites:**

    To be able to access the CI Jobs, the following permissions are required:

    1. Edit, Clone, and Delete permissions are needed to access the nCino CI jobs.
    2. The administrator can provide the required permissions by going to the Users and Roles section of the application.
    3.  The administrator can assign the permissions through this flow Admin > Users > Roles > Feature Migration > Edit, Clone and Delete.

        <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (2).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

**Step-By-Step Guide:**

The following provides a detailed flow on creating the **"Feature CI Jobs"**:

1. The Feature CI Job can be created through the following options:
   1.  Click on the "Feature CI Job" option on the create drop-down

       <figure><img src="../../../../../../.gitbook/assets/3 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
   2.  Click on the "Create feature CI Job" button on the CI Jobs List page to initiate the job creation

       <figure><img src="../../../../../../.gitbook/assets/3.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
   3.  Access to the complete history of CI Jobs is available through the **CI Jobs History** page. New Feature CI Jobs can also be configured from this screen using the **Create Feature CI Job** button..

       <figure><img src="../../../../../../.gitbook/assets/3.2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

### Deploy From Version Control

1.  Initiating the "Feature CI Job" creation will navigate to the "Source Type" page


2.





































































