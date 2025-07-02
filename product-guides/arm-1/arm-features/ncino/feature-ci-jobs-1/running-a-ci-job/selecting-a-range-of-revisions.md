# Selecting a Range of Revisions

### Introduction

Now it is easier to select a range of revisions through Version Control.

### Feature Overview

The **Revision Range** defines the span of version control commits from which templates are selected for deployment. By specifying a **From Revision** and a **To Revision**, the system includes all templates committed within that range—starting just above the _From Revision_ and up to and including the _To Revision_.

This method provides controlled, incremental deployments by targeting a precise subset of changes from the version control history. It ensures that only relevant template updates are deployed to the destination environment, helping to maintain alignment between development and release cycles.

### Step-by-Step Guide

1.  Select "Deploy From Version Control" from the "Source Type"&#x20;

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Deploy From Version Control (3).png" alt=""><figcaption></figcaption></figure>
2.  On selecting "Source Type", the interface will navigate to the "Source" selection of the flow

    <figure><img src="../../../../../../.gitbook/assets/1 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
3. On this page, select the following required fields and input the necessary values:
   1. **Label Name**: Enter the preferred label to identify the CI job.
   2. **Description**: Provide a relevant description outlining the purpose of the deployment.
   3. **Repository**: Select the appropriate repository from the available list.
   4. **Branch**: Choose the required branch associated with the selected repository.
   5. **VC Fetch Type**: Select the required "Fetch Type" from the available list.
   6. **From Revision**: Select the starting revision to define the lower boundary of the revision range.
   7. **To Revision**: Select the ending revision to define the upper boundary of the revision range.
4. **VC Fetch Type:** Select the Revision Range as the option to select the range commits required for the commits
5.  Select the "From Revision" in this field

    <figure><img src="../../../../../../.gitbook/assets/2 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/3 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/3.1 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
6.  Select the "To Revisions" in this field

    <figure><img src="../../../../../../.gitbook/assets/4 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/5 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
7.  The "Feature Versions" from the selected revision range can be observed under the "Selected Feature Version(s)".

    <figure><img src="../../../../../../.gitbook/assets/6 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
8.  Select the required "Destination ORG" at the "Deploy To" field

    <figure><img src="../../../../../../.gitbook/assets/7 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
9.  Preview: At this section the selections made for the "CI Job" configuration can be reviewed here

    <figure><img src="../../../../../../.gitbook/assets/8 - Range of Revisions.png" alt=""><figcaption></figcaption></figure>
