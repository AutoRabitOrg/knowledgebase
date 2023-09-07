# Import an Unlocked/Managed Package

In this article, we would be discussing about how to import a packages (unlocked/managed) into the ARM application. For more information related to packages, refer to the article: [Create an Unlocked/Managed Package](create-an-unlocked-managed-package.md)

### Step 1: Importing a Package <a href="#step-1-importing-a-package" id="step-1-importing-a-package"></a>

1. Hover your mouse over the **Salesforce DX** module and select the option: **Packages**
2.  Click **Import Package**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-N7JAPIZY.png" alt=""><figcaption></figcaption></figure>
3. Select your version control **Repository** and **Branch**.
4. This list down all the **packages** and **package versions** (if any) available in your branch.
5.  Select the **packages** to import.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-PJ42RA5L.png" alt=""><figcaption></figcaption></figure>
6.  To view the dependent packages for the selected packages, click on **View Dependency Packages**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-OAS1UWTE.png" alt=""><figcaption></figcaption></figure>
7. To validate the selected package with your devhub, select the devhub from the drop down list and click on **Validate Package** button. The _green_ tick beside **Validate Package** denotes the packages and devhub are rightly matched.
8.  Click **Save**. A confirmation window appears with the details of the package.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CZUSMCU6.png" alt="" width="563"><figcaption></figcaption></figure>
9.  Click **IMPORT**. The **Import Packages Log** window appears.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GPDQ8HMS.png" alt="" width="563"><figcaption></figcaption></figure>
10. Click **CLOSE**, and you'll be redirected to the **Packages** homepage where you can find your package recently imported.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-WP0X13YG.png" alt=""><figcaption></figcaption></figure>

Important Note

You can import multiple packages with the same name as long as they are from different repositories or different branches.

### Step 2: Create a Package Version <a href="#step-2-create-a-package-version" id="step-2-create-a-package-version"></a>

#### What is a Package Version? <a href="#what-is-a-package-version" id="what-is-a-package-version"></a>

A package is a container for Salesforce metadata. It represents a distinct deployable unit of functionality that is iterated over time. You can add metadata to a package and take a snapshot of it, anytime. This snapshot is called a package version. You can create package versions any number of times. Each package version, once created, is immutable and is associated with a single package. You can install a package version in any Salesforce environment - scratch orgs, sandbox orgs, or production orgs. Installing a package version deploys the metadata that was specified when the package version was created.

1.  Click on the **+** icon under the **Actions** tab to create a version for your package.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-IU1LB5DV.png" alt=""><figcaption></figcaption></figure>
2. Next, fill in the below details:
   * **Version Name**: Version name gets auto-generated based on the package name. However, you can edit the name and enter your desired name. It is really up to you.
   * **Version Number**: Version numbers are formatted as "major.minor.patch.build". _**For ex-**_ _1.2.1.8_.
   * **Installation Key**: Enter the installation key that protects your package from being installed by unauthorized individuals.
   * **Tag**: Enter the tag that is required to release the package. _**For ex-** Release 1.0.0_
   * **Version Description**: Brief description of your package version.
3. Click **Create**.
4.  Verify the log status in the **Package Log** screen.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZOQFMTLR.png" alt="" width="563"><figcaption></figcaption></figure>
