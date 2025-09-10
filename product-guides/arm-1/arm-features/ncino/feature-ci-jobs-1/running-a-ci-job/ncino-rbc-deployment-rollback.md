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

1.  Once in the nCino module, click on the '**Create Feature CI Job**' button.



    <figure><img src="../../../../../../.gitbook/assets/Rollback - 1.png" alt=""><figcaption></figcaption></figure>
2. Enter the required information to configure the CI Job creation.
3.  In the **JOb Settings** section, toggle the button to enable the rollback option.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 4.png" alt=""><figcaption></figcaption></figure>
4. By default, the slider will remain disabled. It should be enabled to make sure the rollback is enabled
5.  If the "Postdeployment" ORGs are seleted during the deployment and the "Rollback" is enabled for that deployment. Then the "Postdeployment" ORGs will be available during the rollback.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 5.png" alt=""><figcaption></figcaption></figure>
6.  On enabling the '**Enable rollback**' option, continue to '**Save**' the job.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 6.png" alt=""><figcaption></figcaption></figure>
7. While enabling the '**Enable rollback**' option, observe the info icon with the message: “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”
8. Upon saving the job, the flow will be redirected to the 'CI **Job List**' screen.
9.  On landing on the '**Job List**' page, continue to run the job created by clicking on the ‘**play**’ icon.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 7.png" alt=""><figcaption></figcaption></figure>
10. Once the play icon is clicked, the "Trigger Build" page will be opened

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 8.png" alt=""><figcaption></figcaption></figure>
11. Once the build run is completed, the '**rollback**' button will be available at the '**job results**' page.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 11.png" alt=""><figcaption></figcaption></figure>
12. When the build is completed successfully, the snapshot of the backed-up data can be downloaded by clicking the "Download Backup Snapshot" option in the job menu.
13. The "Rollback" can be initiated either from the '**CI Job History - Job Results**' page directly or from the '**CI Job Builds'** page.
14. Click "Build List" to access the '**CI Job Builds'** page.
15. Observe the "Rollback" option in the job menu at the "CI Job Builds" page.



    <figure><img src="../../../../../../.gitbook/assets/Rollback - 12.png" alt=""><figcaption></figcaption></figure>
16. On triggering the “RollBack” button either on the **“CI Job History - Job Results”** window or the “**CI Job Builds**” page, the RollBack window will be displayed. Observe the following screenshot for reference.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 13.png" alt=""><figcaption></figcaption></figure>
17. Click on the “Salesforce Orgs” to expand and observe the ORGs available. The list of ORGs include both the direct deployment and the post-deployment ORGs.

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 13 (1).png" alt=""><figcaption></figcaption></figure>
18. Observe the details under tje "Rollback From" & "Rollback Deployed Templates"
    1.  Rollback From

        <figure><img src="../../../../../../.gitbook/assets/Rollback - 14.png" alt=""><figcaption></figcaption></figure>
    2.  Rollback Deployed Templates

        <figure><img src="../../../../../../.gitbook/assets/Rollback - 15.png" alt=""><figcaption></figcaption></figure>
19. Any combination of ORGs and the respective features can be selected to perform the rollback.
20. On completing the required selections, continue with the ‘RollBack’ by clicking on the “RollBack” button.
21. As the '**Rollback**' build is in progress, the page looks like the following:

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 16.png" alt=""><figcaption></figcaption></figure>
22. Once the '**Rollback**' is completed successfully, the '**CI Job Builds**' page looks like the following:

    <figure><img src="../../../../../../.gitbook/assets/Rollback - 19 (1).png" alt=""><figcaption></figcaption></figure>
23. A new build will be added to the list of builds in the following format: '**Rollback**' **- < Build No >**
24. The rollback can be done on the builds as required.

### Feature Deployment

1. Initiate a '**Feature Deployment**' by clicking on the '**Feature Deployment**' button.
2. Continue to input the ‘**Source**’ and ‘**Destination’** configuration details.
3. On entering all the details, click on the '**Create Dataset & Deploy**' button.
4.  On the "Job Settings" section of the flow enable the "Rollback" option to opt for the Rollback.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-05 at 9.13.50 PM (1).png" alt=""><figcaption></figcaption></figure>
5.  Observe the information icon beside the '**Enable Rollback**' button that says, “Please note that the data of this rollback will be retained for a period of 30 days and will be deleted as the retention period elapses.”

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-05 at 9.13.50 PM (2).png" alt=""><figcaption></figcaption></figure>
6. Until the deployment is completed, it is not possible to perform a '**Rollback**' on the deployment.
7.  Click the '**Deploy**' button to deploy the build.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-05 at 9.14.13 PM.png" alt=""><figcaption></figcaption></figure>
8. Once the "Deployment" is completed, the "Rollback" option will be available.
9.  Observe the ‘**Rollback**’ option, both on the '**Deployment History**' page and on the '**Job Details**' page.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.42.20 PM.png" alt=""><figcaption></figcaption></figure>


10. Once the deployment is finished, the backup snapshot marked for deployment can be dowbloaded.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.44.13 PM.png" alt=""><figcaption></figcaption></figure>
11. &#x20;On clicking the Rollback, a window will be displayed with the option to select the feature(s) intended to be rolledback.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.46.14 PM.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.46.30 PM.png" alt=""><figcaption></figcaption></figure>
12. After doing the required selections continue with the “ROLLBACK”, by clicking on the rollback button.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.49.00 PM.png" alt=""><figcaption></figcaption></figure>
13. While the '**Rollback**' is in progress, the '**Re-Deploy**' and '**Rollback**' buttons are grayed out until its completion.
14. Once the '**Rollback**' is completed, then the iteration number will be updated.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.49.41 PM.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2025-09-08 at 4.50.39 PM.png" alt=""><figcaption></figcaption></figure>
15. Observe the ‘**Rollback**’ iteration in the logs by expanding the deployed build, as shown below.

<figure><img src="../../../../../../.gitbook/assets/image (73) (2).png" alt=""><figcaption></figcaption></figure>

### Rollback – Post Deployment Activities

Rollback functionality is now supported for the Orgs selected for post-deployment activities. Please choose the selected Orgs in the highlighted section of the CI job creation flow.

<figure><img src="../../../../../../.gitbook/assets/image (1490).png" alt=""><figcaption></figcaption></figure>

### Additional Resources

**What happens during the rollback of the deployments on the destination Org?**

1. **Insert:** The inserted records in the destination Org are deleted.
2. **Update:** Updates to the destination Org are reverted to their original state.

