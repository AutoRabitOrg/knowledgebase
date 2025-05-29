# Import an Unlocked/Managed Package

Learn how to bring an existing unlocked or managed package into AutoRABIT for further management.  
(Need a refresher on packages? See [Create an Unlocked/Managed Package](create-an-unlocked-managed-package.md).)

---

### Step 1: Import a Package <a href="#step-1-importing-a-package" id="step-1-importing-a-package"></a>

1. **Open Packages**  
   Hover over **Salesforce DX** and select **Packages**.

2. **Click Import Package**

   <figure><img src="../../.gitbook/assets/image (1467).png" alt="Import Package button"></figure>

3. Choose the **Repository** and **Branch** that contain the package manifest.  
4. All available **packages** and **package versions** in that branch appear.  
5. Select the packages you want to import.

   <figure><img src="../../.gitbook/assets/image (1468).png" alt="List of packages and versions"></figure>

6. **View dependencies** – click **View Dependency Packages** to see related packages.

   <figure><img src="../../.gitbook/assets/image (1469).png" alt="Dependency Packages dialog"></figure>

7. **Validate** – pick the **Dev Hub** and click **Validate Package**. A green tick confirms a match.  
8. Click **Save** to review the summary.

   <figure><img src="../../.gitbook/assets/image (1470).png" alt="Save confirmation window" width="559"></figure>

9. Click **IMPORT** to begin. The **Import Packages Log** opens.

   <figure><img src="../../.gitbook/assets/image (1471).png" alt="Import Packages Log dialog" width="496"></figure>

10. Click **CLOSE**. You return to the **Packages** home page, where the newly imported package appears.

    <figure><img src="../../.gitbook/assets/image (1472).png" alt="Packages home showing imported package"></figure>

{% hint style="info" %}
**Note:** You can import multiple packages with the same name if they come from different repositories or branches.
{% endhint %}

---

### Step 2: Create a Package Version <a href="#step-2-create-a-package-version" id="step-2-create-a-package-version"></a>

#### What Is a Package Version? <a href="#what-is-a-package-version" id="what-is-a-package-version"></a>

A **package version** is an immutable snapshot of metadata. You can install it in any org (scratch, sandbox, production) to deploy that exact set of components.

1. Click the **+** icon in the **Actions** column to add a version.

   <figure><img src="../../.gitbook/assets/image (1473).png" alt="Create Package Version plus icon"></figure>

2. Fill in the details:

   * **Version Name** – auto-filled from the package name; editable.  
   * **Version Number** – format `major.minor.patch.build` (e.g., `1.2.1.8`).  
   * **Installation Key** – optional password to restrict installs.  
   * **Tag** – release label (e.g., `Release 1.0.0`).  
   * **Version Description** – brief notes.

3. Click **Create**.  
4. Watch progress on the **Package Log** screen.

   <figure><img src="../../.gitbook/assets/image (1474).png" alt="Package Log showing version creation"></figure>
