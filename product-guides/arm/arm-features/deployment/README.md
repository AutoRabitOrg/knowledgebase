# Deployment

### What is Deployment? <a href="#what-is-deployment" id="what-is-deployment"></a>

The Deployment process allows you to transfer new developments easily and safely from your sandbox instance to a production instance. Using the deployment process, you will be able to transfer validation rules, custom objects, new fields, apex codes, and many other components from your development environment to a live production environment.

### Deployment Methods <a href="#deployment-methods" id="deployment-methods"></a>

Once you are done with your development, you need to migrate your code from your development organization to the organization where business users can use your code. So, in this section, we will learn different methods of deploying the changes to a target/production org:

* **Deploy from Salesforce Org:** Deploys the latest changes made in your source sandbox to a destination sandbox, using either a selective deployment of only the metadata types you’ve chosen or full deployment of all the objects in a build.
* **Deploy from AutoRABIT Build:** Deploys from AutoRABIT build to your target org.
* **Deploy from Package.xml:** A package .xml file controls which metadata types and members are retrieved and deployed from the source org to the destination org. This type of file is also known as a project manifest. Using this type of control file allows you to initiate a deployment without manually selecting metadata components to be included in the deployment.
* **Deploy from Metadata Zip:** Upload the zip file and deploy to the [sandbox](https://www.autorabit.com/blog/the-impact-of-automation-in-salesforce-sandbox-management/) using the Metadata Zip facility
* **Deploy from Version Control (Full Profiles):** Deploy the latest changes made in your version control repository to a destination sandbox, using either a selective deployment of only the metadata types you’ve chosen or full deployment of all the objects in a build.
* **Deploy from Single Revision:** Deploy the changes using [version control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) revision.
* **Deploy from Revision Range:** Deployment based on a range of committed revisions
* **Deploy from Commit Label:** Deploy the EZ-Commit labels to your target sandbox
* **Deploy from Release label:** Deploy using the Release Labels. A release label is nothing but a group of single revisions combined.
* **Deploy from Validate & Commit Label:** Deploy using the validate commit labels
* **Deploy from Previous Deployment Labels:** Re-deploy a previously used deployment label to your destination org
* **Deploy from Unlocked Package:** Deploy using the Salesforce DX unlocked package
* **Deploy from Tag:** Deploy using the version control GIT tags
* **Deploy from Vlocity Components:** Deploy the vlocity components to your target org

### Types of Deployment <a href="#types-of-deployment" id="types-of-deployment"></a>

#### InQueue Deployment <a href="#inqueue-deployment" id="inqueue-deployment"></a>

You can initiate multiple deployments, but only one deployment can run at a time. The other deployments will remain in the queue waiting to be executed after the current deployment finishes.

#### Selective Deployment <a href="#selective-deployment" id="selective-deployment"></a>

Selective Deployment is a deployment in which only the metadata types you’ve selected are deployed from the source to your destination environment.

#### Full Deployment <a href="#full-deployment" id="full-deployment"></a>

A full deployment transfers all [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) in the source org to the destination org. However, there are a few metadata types, such as dynamic package XML files, which cannot be retrieved in this process. In this case, the unretrievable data types will generate warnings during the deployment process, but ARM will continue the deployment and transfer the retrievable metadata types.

#### Deployment Validations <a href="#deployment-validations" id="deployment-validations"></a>

A deployment validation is a deployment that is used only to check the results of deploying components and is rolled back. Validation doesn't save any deployed components or change the [Salesforce Org](../salesforce-org-management.md) in any way. If validation is completed successfully, and all the tests are passed with sufficient code coverage, you can perform a **Quick Deployment** by deploying this validation to production without running tests.

#### Rollback Deployment <a href="#rollback-deployment" id="rollback-deployment"></a>

Sometimes you may want to roll back a deployment — for example, when the deployment is not stable. By default, all of the deployment’s rollout history is kept in the system, so you can roll back anytime you want.

#### Quick Deployment <a href="#quick-deployment" id="quick-deployment"></a>

As part of a deployment, all Apex tests are run in production. If the production org contains many Apex tests, executing the tests can be time-consuming and can delay your deployment. To reduce deployment time to production, you can perform a quick deployment by skipping the execution of tests. Quick deployments are available when the following requirements are met:

* The components have been validated successfully for the target environment within the last 10 days.
* Code coverage requirements are met.
  * If all tests in the org or all **Local tests** are run, overall code coverage is at least 75%, and Apex triggers have some coverage.
  * If specific tests are run with the **Run specified tests** test level, each class and trigger that was deployed is covered by at least 75% individually.

A validation enables you to view the success or failure messages that you would receive with an actual deployment.

**Performing a Quick Deployment**

In the Deployment Status page, deploy a recent validation by clicking **Quick Deploy**. This button appears only for qualifying validations. On the next screen, you need to:

1. Give the deployment a **label name**.
2. Select the **destination environment**.
3. AutoRABIT creates a random Asynchronous Id for every validation and deployment in the destination environment. However, Asynchronous Id which is older than 4 days (96 hours) cannot be used for Quick deployment. Under the **Asynchronous Id** field, you have two options to choose from:
   1. **AutoRABIT generated:** You can select the Asynchronous Id from the drop-down that was generated for the target environment.
   2. **Custom:** As the name suggests, you can manually enter the Asynchronous Id of your choice.
4. Select the **Take Backup** checkbox, if you would like to preserve the snapshot of members before deployment to ensure roll backing the deployment if any issues arise.
5. Next, before running the quick deployment, you may like to run the functional test cases in order to test the functionality of the code being deployed to the destination environment. For example, If you would like to fetch the test cases from [AccelQ](https://www.autorabit.com/blog/autorabit-and-accelq-partner-to-achieve-a-complete-continuous-delivery-solution/), select **AccelQ** under **Fetch Test Cases From** drop-down.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoperformQuickDeploymentcustom7.png" alt="" width="375"><figcaption></figcaption></figure>

6. To fetch the test cases, you'll need to enter the **Project Name**, **Test Job Name**, and set the **parameters** for your AccelQ test cases.
7. Click **Deploy.** You will be again redirected to the **Deployment History** screen where the progress of your deployment can be seen.
