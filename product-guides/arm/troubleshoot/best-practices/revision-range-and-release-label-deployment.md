# Revision Range & Release Label Deployment

## What is a Deployment? <a href="#what-is-deployment" id="what-is-deployment"></a>

The Deployment process allows you to easily and safely transfer new developments from your sandbox instance to a production instance. Using the deployment process, you will be able to transfer validation rules, custom objects, new fields, Apex codes, and many other components from your development environment to a live production environment.

## Different Deployment Methods <a href="#different-deployment-methods" id="different-deployment-methods"></a>

Once you are done with your development, you need to migrate your code from your development organization to the organization where business users can use your code. There are different methods of deploying the changes to a target/production org in AutoRABIT, such as deployment via Salesforce Org/Version Control, Revision Range, Release Label, etc.

### Deployment via Revision Range <a href="#deployment-via-revision-range" id="deployment-via-revision-range"></a>

Deployment via revision range is all about deploying the codes based on a range of committed revisions. Multiple revisions can be a part of this deployment based on the from and to revision selection.

**For example,** to deploy the below-mentioned commit revisions to your target org;

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Choose the **From Revision Date** as **a1022af** and the **To Date** as **d86165a** while you're carrying out the deployment via revision range.

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **Changes on Custom Object**

Let’s take a look at the changes when, for instance, a custom object is selected and deployed using the Revision Range operation:

1. The **custom object** is a part of the initial revision but gets deleted in the revision ranges selection.
   * The custom object becomes part of the **Destructive Items** list.
   * Custom object-related fields become part of the **Destructive Items** list.
2. The **custom object** is a part of the revision ranges selection
   * The custom object is added in one of the revisions and deleted in other revisions. In this scenario, the custom object is not considered a **Destructive Items** or in the **Added/Modified** list.
   * The custom object is modified in between the revision ranges. In this scenario, the custom objects will be treated as a **Modified Items** list.
3. The **custom object** is not a part of the initial revision, but is newly added in the revision ranges selection
   * The custom object will be treated as an **Added Item** list and will get deployed to the target org.

#### **Changes on Profile**

The profile is a collection of settings and permissions that define how a user access records. Let’s take a look at the changes when, for instance, a profile object is selected and deployed using the Revision Range operation:

1. The **profile** is a part of the revision ranges selection.
   * The recent settings and the permissions changes allocated to the Profiles for the revision ranges are deployed.
2. The **profile** is a part of the initial revision but gets deleted in the revision ranges selection.
   * The profile becomes part of the **Destructive Items** list.
   * The profile-related settings and permissions become part of the **Destructive Items** list too.

#### **Changes on Apex Class**

Looking at the changes when, for instance, an Apex class is selected and deployed using the Revision Range operation:

1. The apex class is a part of the initial revision, but is deleted in the revision ranges selection
   * The apex class becomes part of the **Destructive Items** list.
   * The apex class-related fields become part of the **Destructive Items** list.
2. The **Apex class** is a part of the revision ranges selection
   * The apex class is added in one of the revisions and deleted in other revisions. In this scenario, the apex class is not considered a **Destructive Items** or **Added/Modified** list.
   * The apex class is modified in between the revision ranges. In this scenario, the Apex class is treated as a **Modified Items** list.
3. The **Apex class** is not a part of the initial revision, but is newly added in the revision ranges selection.
   * The Apex class will be treated as an **Added Item** list and deployed to the target org.

### Deployment via Release Labels <a href="#deployment-via-release-labels" id="deployment-via-release-labels"></a>

This deploys the changes that are available in your release labels. A release label is simply a group of single revisions combined.

#### **Changes on Custom Object**

Let’s take a look at the changes when, for instance, a custom object is selected and deployed using the Release Label operation:

1. The **custom object** is a part of the release label:
   * The custom object, along with its related fields, will be part of the deployment.
2. The **custom object** is not part of the release label:
   * The custom object will not be deployed to the target org.

#### **Changes on Profile**

The profile is a collection of settings and permissions that define how a user access records. Let’s take a look at the changes when, for instance, a profile object is selected and deployed using the Release Label operation:

1. The **profile** is part of the release label:
   * The entire settings and the permissions allocated to the Profiles will be deployed.
2. The **profile** is not part of the Release Label:
   * The profile and its related settings and permissions will not be deployed.

#### **Changes on Apex Class**

Let’s take a look at the changes when, for instance, an Apex class is selected and deployed using the Release Label:

1. The **Apex class** is a part of the release label:
   * The Apex class along with its related fields will be part of the deployment.
2. The **Apex class** is not part of the release label:
   * The Apex class will not get deployed to the target org.

#### Delta Metadata Generation for Release Label Deployments

**NOTE**: For **Release Label Deployments**, ARM generates delta metadata only for the components listed below.

For **DX Repo Release Labels**, the supported components are:

* autoResponseRules
* bot
* escalationRules
* matchingRule
* labels
* object
* sharingRules
* workflow

For **Non-DX Repo Release Labels**, the supported components are:

* autoResponseRules
* bot
* matchingRule
* labels
* object
* translation
* sharingRules
* workflow

At this time, delta generation is limited to these components, and no other metadata is supported when utilizing Release Label Deployments.

We're exploring a solution to support Release Label delta components, and it’s currently being considered in our product backlog. While we don’t have a confirmed timeline yet, we’ll keep you informed as more information becomes available.

### Release Label Deployment Behavior

Note: If you skip some in-between revisions while creating a Release Label and include a later revision, AutoRABIT will still pick up changes from the skipped revisions in the Release Label Deployments, but only if those changes are related to the same metadata component as the selected revisions.

<figure><img src="../../../../.gitbook/assets/image (1) (10).png" alt=""><figcaption><p>Release Labels</p></figcaption></figure>

For example, if we create a **Release Label** by including **Commits 1, 2, and 4** as shown in the screenshot above, and then deploy using that Release Label to a target Salesforce org, the deployment will **still include the changes from Commit 3**, even though it was skipped in the Release Label.&#x20;
