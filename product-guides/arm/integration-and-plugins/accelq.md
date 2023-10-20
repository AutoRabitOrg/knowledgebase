# AccelQ

### AccelQ: Overview

With every release, AutoRABIT is looking to improve its application quality, achieve in-sprint automation to align with continuous delivery.&#x20;

AccelQs Quality Driven Development (QDD) implements an innovative Agile Quality Life Cycle approach, integrating the usual test silos into an end-to-end automated process. AccelQ is built on a cognitive core engine bringing the power of predictive analytics in scenario design, autonomics in test automation, and adaptive change management in traceability.

### Integrating AccelQ as a Plugin into AutoRABIT

To integrate AccelQ as a plugin with AutoRABIT, it does require some steps in AutoRABIT to get it configured. The below section will help you out to get AccelQ configured in AutoRABIT in easy steps.

Important Note:AccelQ status polds only for 10 minutes.&#x20;

#### Step 1: Store your user's AccelQ credential in AutoRABIT

This is an initial step where the user's AccelQ credential such as username and password is stored in AutoRABIT.

1. Log in to your AutoRABIT account.
2. Go to the **Credentials** tab.
3. Click on **Create Credential** button from the right navigation bar.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664787844015.png)
4. On the next pop-up screen, give a **credential name**.
5. Choose the **Credential Type** as **"User name with Password."**
6. Enter your username and **AccelQ API token** in the **Password** field.
7. Please double-check that you use your AccelQ username instead of the email address that you use to log in to AccelQ.
8. Click **Save**.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664787907361.png)

#### Step 2: Integrate AccelQ with AutoRABIT

1. Go to the **My Account** page.
2. In the **Plugins** section, select **AccelQ** under **Test Types**.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664787987814.png)
3. Fill in the below details to integrate AccelQ:
   * **URL:** Enter the AccelQ registered endpoint URL. For ex- poc.accelq.io
   * **Tenant Code:** Enter the Tenant code received from AccelQ. If you're not aware of this, you can retrieve your Tenant code from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623653800579.png)
   * **Select Credential:** Select the user's credential registered as mentioned in Step 1.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623653699013.png)
4. Once you're done filling the AccelQ fields, click on **Save** to complete the integration process.&#x20;

### Adding AccelQ configuration in CI Job

1. Go to the **New CI Job** screen.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664788025887.png)
2. Select any one of the below criteria for your CI job:
   * _Deploy from Salesforce Org_
   * _Deploy from Version Control_
   * _Deploy from Salesforce Org with a Version Control backup_
   * _Deploy SFDX source from Version Control_
   * _Run Test Automation Scripts_
   * _Install an Unlocked Package from a Version Control Branch_\
     ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664788056610.png)
3. Give the job a descriptive name in the **CI Job Name** field.
4. Go to the **Test** section. Here you will need to select _AccelQ_ to run the functional test cases to test the functionality of the code being deployed to production.
5. Select **Fetch Test Cases From** as **AccelQ**.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664788123572.png)
6. Enter your **Project Name** and the **Test Job Name.**\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664792384631.png)\
   You can find your project name from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ. Similarly, the test job name will be available in the Job section on AccelQ.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623654299743.png)![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623654317366.png)
7. Set the **parameter(s)** for your AccelQ test cases as shown below.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664793490838.png)
8. Click **Save**.
9. So, once the configured CI job is run and the build is triggered, AccelQ will review the code changes and functional review information can be found in the **CI Job Result** under the **Functional Tests** section. Here, you can find the status of the functional test done along with other details such as the number of components that successfully got reviewed, the number of components failed to review, components that are about to get reviewed or are in the queue.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623656334993.png)
10. To view the detailed success or failure report, click on the link available under Functional Tests.
    1. **Success Report:**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623656374785.png)
    2. **Failure Report:**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623656390400.png)
11. Click on **Error Details** for each test case being reviewed to view the error report.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623656400467.png)

### Adding AccelQ configuration in the 'Deployment Setting' screen

In the **Deployment Setting** screen, while performing a new deployment, you need to select **AccelQ** to fetch the test cases.\
![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664793409825.png)

Enter your **Project Name** and the **Test Job Name**.\
![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664793498293.png)

You can find your project name from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623666430357.png)

Similarly, the test job name will be available in the Job section on AccelQ. ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623666463817.png)

Click **Save**.

When the deployment is executed, you can find the AccelQ test cases report in the **Deployment History** screen.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623666702078.png)Click on the **Test Results** button for the detailed AccelQ report.![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623666486469.png)
