# nCino RBC Deployment Rollback

### Introduction

Rollbacks are an indispensable pillar in the realm of systems that undergo continuous evolution. They provide a safety net, enabling you to revert to a known, stable state if something goes wrong.

### Feature Overview

This feature enables users to roll back deployments—provided rollback was enabled during deployment creation. Depending on the requirement, users can perform either a full rollback or a selective rollback. Selective rollback is especially useful when only a specific portion of the deployment needs to be reverted (e.g., a Template, a Feature Template, or a specific ORG from a group of deployed ORGs).

### Feature Considerations

To be able to perform rollbacks on the deployments, users must mark the deployments for rollback when configuring deployments.

### Step-by-Step Guide

1. Log in to your ARM account.

<figure><img src="../../../../../../.gitbook/assets/image (54) (3).png" alt=""><figcaption></figcaption></figure>

2. Go to the nCino module.
3. Rollbacks can either be performed through CI Jobs or Feature Deployment.

### CI Job Rollback

1. Once in the nCino module, click on the '**Create CI Job**' button.

<figure><img src="../../../../../../.gitbook/assets/image (55) (3).png" alt=""><figcaption></figcaption></figure>

2. Enter the required information to configure the CI Job creation.
3. In the **Preview and Save** section, users can toggle the button to enable the rollback option.

<figure><img src="../../../../../../.gitbook/assets/image (56) (3).png" alt=""><figcaption></figcaption></figure>

4. Initially, the slider is disabled. Users must toggle the button to turn on the '**Enable rollback**' option, as shown in the following picture.

<figure><img src="../../../../../../.gitbook/assets/image (57) (3).png" alt=""><figcaption></figcaption></figure>

5. On enabling the '**Enable rollback**' option, users can continue to '**Save**' the job.
6. While enabling the '**Enable rollback**' option, users can click on the question mark and read the message: “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”
7. Upon saving the job, users are directed to the '**Job List**' page as shown.

<figure><img src="../../../../../../.gitbook/assets/image (58) (3).png" alt=""><figcaption></figcaption></figure>

8. On landing on the '**Job List**' page, users can continue and run the job they created by clicking on the ‘**play**’ icon.

<figure><img src="../../../../../../.gitbook/assets/image (59) (3).png" alt=""><figcaption></figcaption></figure>

9. Once the build run is completed, users can see that the '**rollback**' button is available on the '**job results**' page.

<figure><img src="../../../../../../.gitbook/assets/image (60) (3).png" alt=""><figcaption></figcaption></figure>

10. When the build is completed successfully, users can download the snapshot of the backed-up data by hovering on the list icon beside the '**Rollback**' button in the '**Job Details**' page, as highlighted in the following screenshot.

<figure><img src="../../../../../../.gitbook/assets/image (61) (3).png" alt=""><figcaption></figcaption></figure>

11. Users can initiate the rollback from the '**Job Results**' page directly or the '**Details'** page.
12. Users can see the '**Rollback**' button in the following screenshot on the '**Job Details**' page.

<figure><img src="../../../../../../.gitbook/assets/image (62) (3).png" alt=""><figcaption></figcaption></figure>

13. On triggering the “RollBack” button either on the “Job Results” window or the “Job Details” page, the RollBack window will be displayed. Observe the following screenshot for reference.

<figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

14. Click on the “Salesforce Orgs” to expand and observe the ORGs available. The list of ORGs include both the direct deployment and the post-deployment ORGs.

<figure><img src="../../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

15. Click on the “Feature(s)” to observe the list of available features.

<figure><img src="../../../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

16. Any combination of ORGs and the respective features can be selected to perform the rollback.
17. On completing the required selections, continue with the ‘RollBack’ by clicking on the “RollBack” button.
18. As the '**Rollback**' build is in progress, the page looks like the following:

<figure><img src="../../../../../../.gitbook/assets/image (64) (3).png" alt=""><figcaption></figcaption></figure>

15. Once the '**Rollback**' is completed successfully, the '**Job Details**' page looks like the following:

<figure><img src="../../../../../../.gitbook/assets/image (65) (3).png" alt=""><figcaption></figcaption></figure>

16. A new build will be added to the list of the build in the following format: '**Rollback**' **- < Build No >**
17. Users can roll back the builds as often as needed.

### Feature Deployment

1. Initiate a '**Feature Deployment**' by clicking on the '**Feature Deployment**' button.
2. Continue to input the ‘**Source**’ and ‘**Destination’** configuration details.
3. On entering all the required details, click on the '**Create Dataset & Deploy**' button.
4. On clicking the '**Create Dataset & Deploy**' button, a popup with the '**Enable Rollback**' option is displayed.
5. Select the checkbox to enable the rollback of this deployment.

<figure><img src="../../../../../../.gitbook/assets/image (66) (3).png" alt=""><figcaption></figcaption></figure>

6. Users can see an information icon beside the '**Enable Rollback**' button that says, “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”

<figure><img src="../../../../../../.gitbook/assets/image (67) (3).png" alt=""><figcaption></figcaption></figure>

7. Until the deployment is completed, it is not possible to perform a '**Rollback**' on the deployment.
8. Click the '**Deploy**' button to deploy the build.

<figure><img src="../../../../../../.gitbook/assets/image (68) (3).png" alt=""><figcaption></figcaption></figure>

9. Only upon completion of the deployment is the '**Rollback**' option available.

Observe the ‘**Rollback**’ option, both on the '**Deployment History**' page and on the '**Job Details**' page.

<figure><img src="../../../../../../.gitbook/assets/image (69) (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (70) (2).png" alt=""><figcaption></figcaption></figure>

10. Once the deployment is finished, users can download the backup snapshot of the deployment marked for ‘**Rollback**.’

<figure><img src="../../../../../../.gitbook/assets/image (71) (2).png" alt=""><figcaption></figcaption></figure>

11. &#x20;On clicking the Rollback, a window will be displayed with the option to select the feature(s) intended to be rolledback.

<figure><img src="../../../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

12. After doing the required selections continue with the “ROLLBACK”, by clicking on the rollback button.
13. While the '**Rollback**' is in progress, the '**Re-Deploy**' and '**Rollback**' buttons are grayed out until its completion.
14. Once the '**Rollback**' is completed, then the iteration number will be updated.

<figure><img src="../../../../../../.gitbook/assets/image (72) (2).png" alt=""><figcaption></figcaption></figure>

14. Observe the ‘**Rollback**’ iteration in the logs by expanding the deployed build, as shown below.

<figure><img src="../../../../../../.gitbook/assets/image (73) (2).png" alt=""><figcaption></figcaption></figure>

### Rollback – Post Deployment Activities

Rollback functionality is now supported for the Orgs selected for post-deployment activities. Please choose the selected Orgs in the highlighted section of the CI job creation flow.

<figure><img src="../../../../../../.gitbook/assets/image (1490).png" alt=""><figcaption></figcaption></figure>

### Additional Resources

**What happens during the rollback of the deployments on the destination Org?**

1. **Insert:** The inserted records in the destination Org are deleted.
2. **Update:** Updates to the destination Org are reverted to their original state.
