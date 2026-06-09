# Deployment

### What is Deployment? <a href="#what-is-deployment" id="what-is-deployment"></a>

“Deployment” allows teams to transfer metadata changes from one Salesforce environment to another in a controlled and secure manner. It is typically used to move configurations and customizations—such as validation rules, custom objects, fields, Apex classes, and other components—from a Sandbox (development/testing environment) to Production (live environment).

Example: A developer creates a new custom object and validation rule in a Sandbox. After testing is completed successfully, the release manager deploys these changes to the Production org. This ensures that only tested and approved components are introduced into the live environment, minimizing risk to business operations.

Deployment is useful in the following scenarios:

* Moving tested developments from Sandbox to Production.
* Promoting changes across multiple environments (Dev → QA → UAT → Prod).
* Releasing new features or enhancements to end users.
* Migrating configuration updates without manual rework.
* Implementing controlled and auditable change management processes.

### Deployment Methods <a href="#deployment-methods" id="deployment-methods"></a>

Once you are done with your development, you need to migrate your code from your development organization to the organization where business users can use your code. So, in this section, we will learn different methods of deploying the changes to a target/production org:

* **Deploy from Salesforce Org:** Deploys the latest changes made in your source sandbox to a destination sandbox, using either a selective deployment of only the metadata types you’ve chosen or full deployment of all the objects in a build.
*   **Deploy from AutoRABIT Build:** Deploy from AutoRABIT Build allows teams to reuse a previously generated CI build and deploy it to any environment manually without running the CI job again. Instead of running the CI job again, you can reuse an existing successful build.

    Example: A CI job generates Build #45 after developers commit code. QA tests this build successfully. Later, the release manager selects Build #45 from the Deployment module and deploys it to the UAT org. This ensures the same tested build is promoted across environments without rebuilding. This option is useful in following scenarios:

    * You have multiple builds in the CI job history and need to deploy a specific successful build.
    * The target environment (QA/UAT/Sandbox) was not available when the CI build completed.
    * A hotfix build is created to fix a critical production issue.
    * You want to reuse the same build artifact across environments.
    * A deployment fails due to environment configuration issues.
* **Deploy from Package.xml:** A package .xml file controls which metadata types and members are retrieved and deployed from the source org to the destination org. This type of file is also known as a project manifest. Using this type of control file allows you to initiate a deployment without manually selecting metadata components to be included in the deployment.
* **Deploy from Metadata Zip:** Upload the zip file and deploy to the [sandbox](https://www.autorabit.com/blog/the-impact-of-automation-in-salesforce-sandbox-management/) using the Metadata Zip facility.
*   **Deploy from Version Control (Full Profiles):** Allows users to deploy complete Salesforce profile metadata directly from the version control repository to a target org. It retrieves the entire profile, including permissions, object access, field permissions, app visibility, and related settings, instead of deploying only selected profile components. This ensures the profile is deployed exactly as it exists in the repository.

    Example Scenario: Suppose a new profile called "Sales\_User\_Profile" is created in the repository with multiple permissions, including object access, field permissions, and app visibility settings. When deploying to a QA or UAT org, users can select Deploy from Version Control (Full Profiles) to ensure the complete profile and all its associated settings are deployed together.

    This option is best used when creating new profiles or when the full profile configuration must remain consistent across environments.
* **Deploy from Single Revision:** Deploy the changes using [version control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) revision.
* **Deploy from Revision Range:** Deployment based on a range of committed revisions.
* **Deploy from Release label:** Deploy using the Release Labels. A release label is simply a group of single revisions combined.
* **Deploy from Commit Label:** Deploy the EZ-Commit labels to your target sandbox. The commit label will send the entire file from the latest commit, rather than utilizing a delta approach.
*   **Deploy from Validate & Commit Label:** Allows teams to deploy commit labels that have already been successfully validated against a target org. Instead of validating the same changes again, users can directly promote a pre-validated commit label to the destination environment.

    Example: A developer creates a commit label for a set of changes and runs validation against the UAT org. The validation completes successfully without errors. Later, the release manager selects the validated commit label from the Deployment module and deploys it to Production. This ensures that only pre-validated and approved changes are promoted.

    This option is useful in the following scenarios:

    * When you want to deploy only changes that have already passed validation.
    * When multiple commit labels exist and you need to promote a specific validated label.
    * When you want to reduce deployment risk by avoiding re-validation errors.
    * When the release process requires validation approval before Production deployment.
    * When you need controlled promotion of tested changes across environments.
* **Deploy from Previous Deployment Labels:** Redeploy a previously used deployment label to your destination org.
* **Deploy from Unlocked Package:** Deploy using the Salesforce DX unlocked package.
* **Deploy from Tag:** Deploy using the version control GIT tags.
* **Deploy from Vlocity Components:** Deploy the Vlocity components to your target org.

### Types of Deployment <a href="#types-of-deployment" id="types-of-deployment"></a>

#### InQueue Deployment <a href="#inqueue-deployment" id="inqueue-deployment"></a>

You can initiate multiple deployments, but only one deployment can run at a time. The other deployments will remain in the queue waiting to be executed after the current deployment finishes.

#### Selective Deployment <a href="#selective-deployment" id="selective-deployment"></a>

Selective Deployment is a deployment in which only the metadata types you’ve selected are deployed from the source to your destination environment.

#### Full Deployment <a href="#full-deployment" id="full-deployment"></a>

A full deployment transfers all [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) in the source org to the destination org. However, there are a few metadata types, such as dynamic package XML files, which cannot be retrieved in this process. In this case, the unretrievable data types will generate warnings during the deployment process, but ARM will continue the deployment and transfer the retrievable metadata types.

#### Deployment Validations <a href="#deployment-validations" id="deployment-validations"></a>

A deployment validation is a deployment that is used only to check the results of deploying components and is rolled back. Validation doesn't save any deployed components or change the [Salesforce Org](../../registration/salesforce-org/salesforce-org-management.md) in any way. If validation is completed successfully, and all the tests are passed with sufficient code coverage, you can perform a **Quick Deployment** by deploying this validation to production without running tests.

#### Rollback Deployment <a href="#rollback-deployment" id="rollback-deployment"></a>

Sometimes you may want to roll back a deployment — for example, when the deployment is not stable. By default, all of the deployment’s rollout history is kept in the system, so you can roll back anytime you want.

#### Quick Deployment <a href="#quick-deployment" id="quick-deployment"></a>

As part of a deployment, all Apex tests are run in production. If the production org contains many Apex tests, executing the tests can be time-consuming and can delay your deployment. To reduce deployment time to production, you can perform a quick deployment by skipping the execution of tests. Quick deployments are available when the following requirements are met:

1. The components have been validated successfully for the target environment within the last 10 days.
2. Code coverage requirements are met.
   * If all tests in the org or all **Local tests** are run, overall code coverage is at least 75%, and Apex triggers have some coverage.
   * If specific tests are run with the **Run specified tests** test level, each class and trigger that was deployed is covered by at least 75% individually.

A validation enables you to view the success or failure messages that you would receive with an actual deployment.

**Performing a Quick Deployment**

In the Deployment Status page, deploy a recent validation by clicking **Quick Deploy**. This button appears only for qualifying validations. On the next screen, you need to:

1. Give the deployment a **label name**.
2. Select the **destination environment**.
3. AutoRABIT creates a random Asynchronous Id for every validation and deployment in the destination environment. However, Asynchronous Id which is older than 4 days (96 hours) cannot be used for Quick deployment. Under the **Asynchronous Id** field, you have two options to choose from:
   * **AutoRABIT generated:** You can select the Asynchronous Id from the drop-down that was generated for the target environment.
   * **Custom:** As the name suggests, you can manually enter the Asynchronous Id of your choice.
4. Select the **Take Backup** checkbox, if you would like to preserve the snapshot of members before deployment to ensure roll backing the deployment if any issues arise.
5. Next, before running the quick deployment, you may like to run the functional test cases in order to test the functionality of the code being deployed to the destination environment. For example, If you would like to fetch the test cases from [AccelQ](https://www.autorabit.com/blog/autorabit-and-accelq-partner-to-achieve-a-complete-continuous-delivery-solution/), select **AccelQ** under **Fetch Test Cases From** drop-down.

<figure><img src="../../../../.gitbook/assets/image (65) (1).png" alt="" width="473"><figcaption></figcaption></figure>

6. To fetch the test cases, you'll need to enter the **Project Name**, **Test Job Name**, and set the **parameters** for your AccelQ test cases.
7. Click **Deploy.** You will be again redirected to the **Deployment History** screen where the progress of your deployment can be seen.
