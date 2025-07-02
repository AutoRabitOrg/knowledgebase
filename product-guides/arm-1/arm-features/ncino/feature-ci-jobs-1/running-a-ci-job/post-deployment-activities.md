# Post Deployment Activities

Introduction

Using this feature, users can perform the deployments to the Orgs selected on the post-deployment activities.

### Feature Overview

While configuring the CI Job, users can designate up to five target orgs for post-deployment activities. This capability streamlines the deployment process by enabling simultaneous distribution of identical templates across multiple orgs, thereby eliminating the need for separate deployments to each environment.

### Step-by-Step Guide

1. **Locate the Section**:\
   Navigate to the **Post Deployment Activities** section at the bottom of the **Job Settings** screen.

<figure><img src="../../../../../../.gitbook/assets/8 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

2. **Enable Dataset Propagation**:
   1. Check the option labeled **Deploy the same dataset to**.
   2. A drop-down field will appear next to the label.
3. **Choose Target Orgs**:
   1. Click on the dropdown to view the list of available organizations.
   2. Select one or more target orgs by checking the boxes.
   3. The selected orgs will be listed below the dropdown, and the count of selected orgs will be shown.

<figure><img src="../../../../../../.gitbook/assets/8.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

4. Continue to the preview screen after completing the selections on the "Post Deployment" activities
5.  **Preview**: The preview screen provides a holistic view of the configurations selected for the deployment.

    <figure><img src="../../../../../../.gitbook/assets/5- Post Deployment (1).png" alt=""><figcaption></figcaption></figure>
6. Click **Save** to create a CI Job. On clicking "Save", the interface will navigate to the "CI Job List" page.
7. Initiate the job build by clicking on the "Play" icon available at the job level.
8.  After verifying all the details of the build, the post-deployment selected can be observed here, click on the "Trigger build" to initiate the job build.



    <figure><img src="../../../../../../.gitbook/assets/6.1- Post Deployment.png" alt=""><figcaption></figcaption></figure>
9.  Once the job run is completed, the post-deployment details and logs can be observed here.

    <figure><img src="../../../../../../.gitbook/assets/7- Post Deployment.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/8- Post Deployment.png" alt=""><figcaption></figcaption></figure>
10. The post-deploymnt logs can be downloaded using the logs icon.

    <figure><img src="../../../../../../.gitbook/assets/9- Post Deployment.png" alt=""><figcaption></figcaption></figure>
11. Clicking on "View Logs" will redirect the user to the "Feature Logs" section.

    <figure><img src="../../../../../../.gitbook/assets/10- Post Deployment.png" alt=""><figcaption></figcaption></figure>
