# Specify Baseline Revision in Continuous Integration for Version Control

### Introduction

Now users can seamlessly specify the baseline revision from a set of revisions available from the repository.

### Feature Overview

1. Users can select the baseline revision from which the system can select all the revisions available until that date as part of the deployment.
2. Once a user specifies a the baseline revision, the system will automatically pick up all the commits available from that point forward, every time a deployment is triggered on that job.

### Step-by-Step Guide

1.  Select the ‘Version Control’ in the ‘Deployment From’ field of the ‘CI Job’ creation screen.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-BYOQQPIG.png" alt=""><figcaption></figcaption></figure>
2.  Select ‘Baseline Revision’ in the ‘Deployment Type’ field as shown in the following screenshot.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-SZV5N3W0.png" alt=""><figcaption></figcaption></figure>
3.  Select ‘Git’ in the ‘Version Control’ field as shown in the following screenshot.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ATOCL3B9.png" alt=""><figcaption></figcaption></figure>
4.  Select the required repository from the list in the ‘Repository’ field, as shown in the following screenshot.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YBETAW9P.png" alt=""><figcaption></figcaption></figure>
5.  Select the ‘Branch’ to which users can deploy through the ‘Branch’ field available.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-UIUQMDVN.png" alt=""><figcaption></figcaption></figure>
6.  Select the required revision from the list available in the ‘Revision’ field, as shown in the following screenshot.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CBEPZ8MN.png" alt=""><figcaption></figcaption></figure>
7.  Open the ‘Revision’ field by clicking on the search icon. Upon clicking the search icon, a popup opens up, as shown in the following screenshot.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-FLM444FR.png" alt=""><figcaption></figcaption></figure>
8.  Select the required commit as a baseline revision and click ‘ok’ to confirm. When you complete the selection, the selected commit is displayed on the field.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0YG0168A.png" alt=""><figcaption></figcaption></figure>
9.  Upon clicking ‘Save’ on the ‘CI Jobs’ configuration, users will be redirected to the ‘Job List’ section of the ‘CI Jobs’ page, as shown below.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-15FB7WP2.png" alt=""><figcaption></figcaption></figure>
10. Upon clicking the ‘Play’ button, users are taken to the ‘New Build’ page, where users can ‘Trigger Build’ using the button.\
    a. On the ‘New Build’ screen, users can view the ‘Baseline Revision’ selected, under the ‘Baseline Revision’, as shown below.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-39NO90K7.png" alt=""><figcaption></figcaption></figure>
