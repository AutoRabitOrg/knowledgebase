# Create an Unlocked/Managed Package

### What’s a Package? <a href="#whats-a-package" id="whats-a-package"></a>

If you’re new to packaging, you can think about a package as a container that you fill with metadata. It contains a set of related features, customizations, and schema. You use packages to move metadata from one [Salesforce org](arm-administration/registration/salesforce-org.md) to another.

There are two kinds of packages - _managed_ and _unlocked packages_.

#### Unlocked Packages <a href="#unlocked-packages" id="unlocked-packages"></a>

Unlocked packages allow the users a means to organize their metadata into a package and then deploy the metadata (via packages) to different org. Unlocked packages will help the users to add, edit, and remove metadata in their org in a traceable way. The users can apply their source and metadata to multiple org, and upgrade their Salesforce apps easier and faster.

#### Managed Packages <a href="#managed-packages" id="managed-packages"></a>

Managed packages are created by Salesforce partners to distribute and sell apps to their customers. The main purpose of a managed package is to bind code and configuration elements into a single entity. Those can be logical functional modules, re-usable code libraries, or entire sub-systems containing the functionality of a business channel.

The key benefits of managed packages are the following:&#x20;

* Intellectual property protection is automatically included in certain components, e.g., in obfuscating Apex code.
* API accessible components have integrated versioning support.&#x20;
* A previous version of the app can be branched and patched.&#x20;
* You can seamlessly provide subscribers with patch updates.&#x20;
* You can give unique names to components to avoid conflicts when installing the app.
* You can select the desired ancestor while creating a package version.

### Create a Package <a href="#create-a-package" id="create-a-package"></a>

There are two steps to follow:

1. The first step is to create a **package**, specifying information that is unlikely to change, like the package name and description.
2. The second step is to create a **package version** of the package. This package version is the artifact that is installed in various orgs. As you update your app, you create new package versions containing the updated source.

#### Step 1: Creating a Package <a href="#step-1-creating-a-package" id="step-1-creating-a-package"></a>

1. Hover your mouse over the [Salesforce DX](https://www.autorabit.com/blog/the-basics-of-salesforce-dx/) module and select the option: **Packages**
2. Click **Create Package**.
3. On the next screen, give the **Package Name** and the **Package Description**.
4. Select the **Package Type: Unlocked** or **Managed**.
5. Select the **Dev Hub** for which the package will be associated.
6. Under Version Control, enter the [**Version Control Repository**](arm-features/version-control/version-control-repositories-summary.md) and its related **Branch**.
7.  Select the **Package Directory** from the dropdown. (For more information about **Package Directory**, refer to the article: [Salesforce DX Metadata Format](salesforce-dx-metadata-format.md))\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658922976011.png" alt=""><figcaption></figcaption></figure>

#### Step 2: Create a Package Version <a href="#step-2-create-a-package-version" id="step-2-create-a-package-version"></a>

**What is a Package Version?**

A package is a container for [Salesforce metadata](https://www.autorabit.com/blog/why-do-i-need-to-protect-my-salesforce-metadata/). It represents a distinct deployable unit of functionality that is iterated over time. You can add metadata to a package and take a snapshot of it, anytime. This snapshot is called a package version. You can create package versions any number of times. Each package version, once created, is immutable and is associated with a single package. You can install a package version in any Salesforce environment - scratch orgs, sandbox orgs, or production orgs. Installing a package version deploys the metadata that was specified when the package version was created.

Under the **Package Version** section, do the following:

1. **Version Name:** Version name gets auto-generated based on the package name. However, you can edit the name and enter your desired name. It is really up to you.
2. **Version Description:** Brief description of your Package version.
3. **Version Number:** Version numbers are formatted as **major.minor.patch.build**. **For ex-** 1.2.1.8.
4. **Installation Key:** Enter the installation key that protects your package from being installed by unauthorized individuals.
5.  **Tag:** Enter the tag that is required to release the package. **For ex-** Release 1.0.0\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658923698967.png" alt=""><figcaption></figcaption></figure>

**Package Dependencies:** The Dev Hub org can own multiple packages that are created in AutoRABIT. Such dependent packages will get displayed in this section.&#x20;

From the **Available Packages** list, select the dependent packages that will be associated with the current module. Use the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402857647.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402882169.png) button to add/remove the dependent packages to the module and using the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402900576.png)/![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613402922812.png) button, move the package list up and down. Based on the selection, the top package will be deployed in the beginning and the process continues for the remaining dependent packages.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658923720319.png)

Click either **View Metadata** or **Create Package**.

1.  **View Metadata:** This option will allow the users to view the metadata types and their members that get pulled out from the Version control repository and review the same before creating a package.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658924214669.png" alt=""><figcaption></figcaption></figure>
2. **Create Package:** This will allow you to create the package for the data that you've filled above.

Upon confirmation, the package gets created and the progress status gets displayed on the **Unlocked Package** home screen.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658924274420.png)

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658924440742.png)

### More Information on the 'Package' screen  <a href="#more-information-on-the-package-screen" id="more-information-on-the-package-screen"></a>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1658924558565.png" alt=""><figcaption></figcaption></figure>

1. **Status:** View the status of the Package i.e., success or failed along with the Package Log report.
2. **Actions:**&#x20;
   1. **Delete a Package:** Delete a package and its related version details. This process cannot be undone!!
   2. **Create a Version:** Using the **+** icon to create a new package version for the current package. On the next screen, fill in the basic details such as version name, version number, installation key, tag, and description and click **Create**.
3.  **Info:**

    1. **View Packaged versions (**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613896513485.png)**):** You can click on this icon to view the version details (package version name, version number, percentage of code coverage covered, etc.,) of an unlocked or managed package. Alternatively, you can click on the package name on the **Packages** screen to view the version details. The installation URL for the package version gets auto-generated and used in creating a package. You can add a new version to the current package by clicking **Create Package Version**.

    \
    \


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1646407711517.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Important Notes:

* For **Unlocked Packages**, when a new package version is created, the latest promoted version of the package will be considered as an ancestor.\

* For **Managed Packages**, if you do not choose any ancestor then the latest promoted version will be selected as an ancestor by default. If you choose **None**, the package version will be created without an ancestor. If you want to choose an ancestor other than the latest promoted version then select the **Skip Ancestor Check** check box.

<img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1671801329383.png" alt="" data-size="original">

* Creating non-linear package versions in the same branch is restricted as it might cause issues during build and deployment.
{% endhint %}

**Promote:** With this option, you promote your package versions to be released. A version number uses the format _major.minor.patch.build_. When you promote a package version, you cannot promote the same package again unless you increment the minor or major number. _**For example-**_ if you created and promoted package _1.0.0.2_, you can create packages _1.0.0.3_, _1.0.0.4_, and so on. However, you cannot promote more packages with the 1.0.0 scheme. To promote another package, create a new package with an incremented major or minor version number.

{% hint style="info" %}
**Important Notes:**

1. The package version can only be promoted and deployed to the production orgs if the code coverage is greater than **75 percent**.
2. The previously created package version would display **0 percent** of the code coverage, and you won't have an option to promote the version of the package to deployment orgs.
3. The already promoted package version without any code coverage will not have any impact.
4. You can promote once for each package version number, and you can’t undo the change to the package status.
{% endhint %}

**Package info:** Hover your mouse over the info icon to view the package information such as package author name, date and time stamp of the package created, package last modified date/time, and the author who did the last modification.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1659000005751.png" alt=""><figcaption></figcaption></figure>
