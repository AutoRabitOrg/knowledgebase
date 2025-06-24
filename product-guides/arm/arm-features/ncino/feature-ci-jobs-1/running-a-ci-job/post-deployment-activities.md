# Post Deployment Activities

### Introduction

Using this feature, users can perform the deployments to the Orgs selected on the post-deployment activities.

### Feature Overview

While configuring the CI Job, users can designate up to five target orgs for post-deployment activities. This capability streamlines the deployment process by enabling simultaneous distribution of identical templates across multiple orgs, thereby eliminating the need for separate deployments to each environment.

### Step-by-Step Guide

1. **Locate the Section**:\
   Navigate to the **Post Deployment Activities** section at the bottom of the **Job Settings** screen.

<figure><img src="../../../../../../.gitbook/assets/8 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

2. **Enable Dataset Propagation**:
   1. Check the option labeled **Deploy the same dataset to**.
   2. A drop-down field will appear next to the label.
3. **Choose Target Orgs**:
   1. Click on the dropdown to view the list of available organizations.
   2. Select one or more target orgs by checking the boxes.
   3. The selected orgs will be listed below the dropdown, and the count of selected orgs will be shown.

<figure><img src="../../../../../../.gitbook/assets/8.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

4.



























1. Users can select multiple Orgs, as shown on the screenshot below, to deploy to while creating the config for CI Jobs.

<figure><img src="../../../../../../.gitbook/assets/image (23) (4).png" alt=""><figcaption></figcaption></figure>

2. Once the Job is created, users can open the job created.

<figure><img src="../../../../../../.gitbook/assets/image (24) (4).png" alt=""><figcaption></figcaption></figure>

3. Click on the ‘Build Now’ button to trigger the build.

<figure><img src="../../../../../../.gitbook/assets/image (25) (4).png" alt=""><figcaption></figcaption></figure>

4. Upon completion of the CI Job deployment, the post-deployment activities will be triggered, as shown in the following figure.

<figure><img src="../../../../../../.gitbook/assets/image (26) (4).png" alt=""><figcaption></figcaption></figure>

5. While the post-deployment activities are being deployed, the post-deployment activities will be shown in progress, as seen in the prior screenshot.
6. Upon successful deployment, the relevant status is shown under the ‘Post Deploy Details’ section.
7. As shown in the following screenshot, users can click on the ‘View Details’ section to further verify post-deployment activities.

<figure><img src="../../../../../../.gitbook/assets/image (27) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (28) (4).png" alt=""><figcaption></figcaption></figure>

8. The post-deployment Org details can also be verified by clicking open the build, as shown below.

<figure><img src="../../../../../../.gitbook/assets/image (29) (4).png" alt=""><figcaption></figcaption></figure>

9.  Upon opening the deployed build, the post-deployment Org details can be observed as listed below:

    * Click on the ‘Post Deployment Activities’ tab.
    * Click on the ‘Salesforce Org’ dropdown to see details for the Org deployed to.
    * Click on the ‘Notes’ icon to see the logs of ‘Post Deployment Activities.’

    <figure><img src="../../../../../../.gitbook/assets/image (30) (4).png" alt=""><figcaption></figcaption></figure>
