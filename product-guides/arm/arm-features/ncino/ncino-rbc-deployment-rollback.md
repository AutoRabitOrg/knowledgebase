# nCino RBC Deployment Rollback

### Introduction

Rollbacks are an indispensable pillar in the realm of systems that undergo continuous evolution. They provide a safety net, enabling you to revert to a known, stable state if something goes wrong.

### Feature Overview

This feature allows users to perform a rollback of the deployments—if rollbacks were enabled when creating the deployments.

### Feature Considerations

To be able to perform rollbacks on the deployments, users must mark the deployments for rollback when configuring deployments.

### Step-by-Step Guide

1. Login to your ARM account.

<figure><img src="../../../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

2. Go to the nCino module.
3. Rollbacks can either be performed through CI Jobs or Feature Deployment.

#### CI Job Rollback

1. Once in the nCino module, click on the '**Create CI Job**' button.

<figure><img src="../../../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

2. Continue to provide the required inputs to create the configuration of the CI Job creation.
3. In the **Preview and Save** section, the user can toggle the button to enable the rollback option.

<figure><img src="../../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

4. Initially, the slider is disabled. Users must toggle the button to turn on the '**Enable rollback**' option, as shown in the following picture.

<figure><img src="../../../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

5. On enabling the '**Enable rollback**' option, users can continue to '**Save**' the job.
6. While enabling the '**Enable rollback**' option, users can click on the question mark and read the message: “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”
7. On saving the job, users are directed to the '**Job List**' page as shown.

<figure><img src="../../../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

8. On landing on the '**Job List**' page, users can continue and run the job they created by clicking on the ‘**play**’ icon.

<figure><img src="../../../../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

9. Once the build run is completed, users can see that the '**rollback**' button is available on the '**job results**' page.

<figure><img src="../../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

10. When the build is completed successfully, users can download the snapshot of the backed-up data by hovering on the list icon beside the '**Rollback**' button in the '**Job Details**' page, as highlighted in the following screenshot.

<figure><img src="../../../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

11. Users can initiate the rollback from the '**Job Results**' page directly or the '**Details'** page.
12. Users can see the '**Rollback**' button in the following screenshot on the '**Job Details**' page.

<figure><img src="../../../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

13. Upon clicking the ‘**Rollback**’ button, users are prompted to decide whether to go ahead with the '**Rollback**’ operation as shown in the image below.

<figure><img src="../../../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

14. As the '**Rollback**' build is in progress, the page looks like the following:

<figure><img src="../../../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

15. Once the '**Rollback**' is completed successfully, the '**Job Details**' page looks like the following:

<figure><img src="../../../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

16. A new build will be added to the list of the build in the following format: '**Rollback**' **- < Build No >**
17. Users can roll back the builds as often as needed.

#### Feature Deployment

1. Initiate a '**Feature Deployment**' by clicking on the '**Feature Deployment**' button.
2. Continue to input the ‘**Source**’ and ‘**Destination’** configuration details.
3. On entering all the required details, click on the '**Create Dataset & Deploy**' button.
4. On clicking the '**Create Dataset & Deploy**' button, a popup with the '**Enable Rollback**' option is displayed.
5. Select the checkbox to enable the rollback of this deployment.

<figure><img src="../../../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

6. Users can see an information icon beside the '**Enable Rollback**' button that says, “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”

<figure><img src="../../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

7. Until the deployment is completed, it is not possible to perform a '**Rollback**' on the deployment.
8. Click the '**Deploy**' button to deploy the build.

<figure><img src="../../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

9. Only upon completion of the deployment is the '**Rollback**' option available.

Observe the ‘**Rollback**’ option, both on the '**Deployment History**' page and on the '**Job Details**' page.

<figure><img src="../../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

10. Once the deployment is finished, users can download the backup snapshot of the deployment marked for ‘**Rollback**.’

<figure><img src="../../../../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

11. Click on the '**Rollback**' button to roll back the deployment.
12. Once the '**Rollback**' is completed, then the iteration number will be updated.
13. While the '**Rollback**' is in progress, the '**Re-Deploy**' and '**Rollback**' buttons are grayed out until its completion.

<figure><img src="../../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

14. Observe the ‘**Rollback**’ iteration in the logs by expanding the deployed build, as shown below.

<figure><img src="../../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

#### Additional Resources

**What happens during the rollback of the deployments on the destination Org?**

1. **Insert:** The inserted records in the destination Org are deleted.
2. **Update:** Updates to the destination Org are reverted to their original state.
