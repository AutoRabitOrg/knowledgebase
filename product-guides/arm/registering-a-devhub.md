# Registering a DevHub

### Introduction <a href="#introduction" id="introduction"></a>

Dev Hub is the main Salesforce Org that you and your team use to create, delete and manage your Salesforce Scratch Orgs. A [Scratch Org](create-a-scratch-org.md) is a temporary deployment of Salesforce source code and metadata. Any number of Salesforce Scratch Orgs can be created to start a new project, to start a new feature branch, to test a new feature, start automated testing, perform development tasks directly in an Org, and start from scratch with a fresh new org.

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

To register a Dev Hub, you must **enable Dev Hub**, and configure **Salesforce Dev Hub** set up in your Salesforce Organization.

### To enable Dev Hub in an org <a href="#to-enable-dev-hub-in-an-org" id="to-enable-dev-hub-in-an-org"></a>

1. Log in as system administrator to your developer edition, production org, or business org.
2.  Navigate to **Develop > Dev Hub** or enter **Dev Hub** in the **Quick Find** box. If you don't see Dev Hub in the **Setup** menu, make sure your org is one of the supported editions.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613886976294.png" alt=""><figcaption></figcaption></figure>
3. To enable Dev Hub, click **Enable**. Also, enable unlocked packages and second-generation managed packages to develop 2GP packages. Once you enable Dev Hub, you can no longer disable it.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613887013857.png" alt=""><figcaption></figcaption></figure>

### Procedure to register a Dev Hub <a href="#procedure-to-register-a-dev-hub" id="procedure-to-register-a-dev-hub"></a>

1.  Hover your mouse over the **SFDX** module and select the option: **Hub Management**

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613887593614.png" alt="" width="188"><figcaption></figcaption></figure>
2. Click **REGISTER DEV HUB**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646405561728.png" alt=""><figcaption></figcaption></figure>

3. &#x20;In the **Register Dev HUB** screen, enter the **Dev Hub** name.
4. Select the **Environment**.
5.  The remaining fields are populated by default. Click **Register Dev Hub**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1685107415302.png" alt="" width="375"><figcaption></figcaption></figure>
6. It will redirect to the **Salesforce** login page where you need to click **Allow** to allow access to your Salesforce Org.&#x20;
7. When your **Dev Hub** is ready, it will appear on the **HUB MANAGEMENT** page.
8. Now, user with owner or admin access to the dev Hub, can limit activity to certain users and restrict all other users from interacting with it. This can be achieved using the **HUB LEVEL PERMISSIONS** option.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646405634939.png" alt=""><figcaption></figcaption></figure>

9. Under the **Hub Level Permissions** screen, select the users to whom you want to grant permissions to access the dev hub org. Click **Save**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613887830241.png" alt="" width="375"><figcaption></figcaption></figure>

10. In order to view your org’s limits and how close you are to reaching them, you can view such information using View Org's API Limits. Click on the **VIEW ORG's API LIMITS** button and it will display the remaining and maximum calls and events for your org.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646405707165.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613887899992.png" alt="" width="563"><figcaption></figcaption></figure>

### View Packages <a href="#view-packages" id="view-packages"></a>

To view the managed/unlocked packages for your dev hub, click on the **VIEW PACKAGES** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646405938411.png" alt=""><figcaption></figcaption></figure>

This lists down all the packages available in your dev hub in the record view. Click on the **expand** arrow for each package to view the version of the package in chronological order along with package details.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646406176765.png" alt=""><figcaption></figcaption></figure>

Scroll to the right side of the screen to view the **Anchestors** for your managed packages only.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646406329560.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646406411467.png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Ancestors are visible only for managed packages.
{% endhint %}

### What's Next? <a href="#whats-next" id="whats-next"></a>

The next topic will be Scratch Orgs, their advantages, and the procedures to create and register them with your dev hub in [ARM](https://www.autorabit.com/). To navigate directly to the Scratch Org section, [click here](create-a-scratch-org.md).
