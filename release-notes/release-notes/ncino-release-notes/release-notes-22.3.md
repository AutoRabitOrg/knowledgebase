# Release Notes 22.3

**March 2023 - Version 22.3 (nCino)**- **Key Features and Enhancements**

**Date of release:** _05 March 2023_\
**Article last updated:** _05 March 2023_\
\


### Key Features <a href="#key-features" id="key-features"></a>

#### 1. Specify baseline revision in continuous integration for version control <a href="#id-1-specify-baseline-revision-in-continuous-integration-for-version-control" id="id-1-specify-baseline-revision-in-continuous-integration-for-version-control"></a>

With this nCino release, we've added a new option called **Version Control** to facilitate deployment. The users will now be able to define a starting point from which commit needs to be picked for the range of revisions to be deployed via Continuous Integration (CI) jobs. The key features are:

* The user will be able to trigger builds for new revisions (delta deployments).
* The user will be able to select baseline revisions as a starting point for CI jobs.
* The user will be able to group all commit revisions together to run dataloader operations at once.

[**Read more →**](../../../product-guides/arm/arm-features/ncino/feature-ci-jobs/running-a-ci-job.md)

#### 2. Reuse the package from the build and deploy in multiple Salesforce environments as post-deployment success activity <a href="#id-2-reuse-the-package-from-the-build-and-deploy-in-multiple-salesforce-environments-as-postdeployment" id="id-2-reuse-the-package-from-the-build-and-deploy-in-multiple-salesforce-environments-as-postdeployment"></a>

As a post-deployment success activity, we've provided the ability to reuse a package from a single build from a single CI job to deploy the same data in various Salesforce environments.

While using the current nCino implementation, the user must create multiple CI jobs, one for each destination org, in order to build data from the same repository and branch and deploy it to multiple salesforce environments. This results in repeated effort in building from the same source and defining the same job over and over again merely to choose a different destination, making it difficult to manage several CI jobs.\
With this new functionality, the user can build once and reuse it for deploying to multiple Salesforce orgs using a single build from a CI job.

The key features are:

* Reduced effort in redefining the CI jobs with the same source multiple times.
* Reduced time to deploy to multiple environments from the same source.

[**Read more →**](../../../product-guides/arm/arm-features/ncino/feature-ci-jobs/running-a-ci-job.md)

#### 3. New 'Spreads Schedule Template' tile in _Feature Creation_ screen <a href="#id-3-new-spreads-schedule-template-tile-in-feature-creation-screen" id="id-3-new-spreads-schedule-template-tile-in-feature-creation-screen"></a>

New objects, such as _Schedules_ and _Debt Schedules_, were introduced with the latest nCino version release.

All of them are part of the _Spreads Schedules_ group. To include all these objects under a single umbrella, we added a new tile called **Spreads Schedules Template**.

The **Spreads Schedules Template** template includes the following objects:

* LLC\_BI\_\_Underwriting\_Bundle\_\_c
* LLC\_BI\_\_Spread\_Statement\_Type\_\_c
* LLC\_BI\_\_Spread\_Statement\_Record\_\_c
* LLC\_BI\_\_Debt\_\_c
* LLC\_BI\_\_Debt\_Schedule\_\_c
* LLC\_BI\_\_Schedule\_\_c
* LLC\_BI\_\_Schedule\_Section\_\_c
* LLC\_BI\_\_Schedule\_Entry\_\_c

[**Read more →**](../../../product-guides/arm/arm-features/ncino/feature-migration/create-a-feature-migration-template.md)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Salesforce Spring '23 (API version 57.0) Support <a href="#id-1-salesforce-spring-23-api-version-570-support" id="id-1-salesforce-spring-23-api-version-570-support"></a>

To keep our product up to current with the most recent Salesforce upgrades, AutoRABIT supports the most recent API 57.0 version in this release. The most recent API version is aimed for customising the metadata schema and developing tools to manage it.

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/salesforce-api-version.md)
