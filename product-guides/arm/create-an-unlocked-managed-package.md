# Create an Unlocked/Managed Package

### What’s a Package? <a href="#whats-a-package" id="whats-a-package"></a>

A **package** is a container of related metadata—features, customizations, and schema—that you move from one [Salesforce org](broken-reference) to another.

There are two kinds:

* **Unlocked packages** – ideal for internal development; they let you add, edit, and remove metadata across multiple orgs in a traceable way.
* **Managed packages** – created by Salesforce partners to distribute or sell apps. They bundle code and configuration into a single, versioned unit.

***

### Create a Package <a href="#create-a-package" id="create-a-package"></a>

Creating a package involves two steps:

1. **Create the package** – define static info such as the name and description.
2. **Create a package version** – the deployable artifact you install in any org.

***

#### Step 1: Create a Package <a href="#step-1-creating-a-package" id="step-1-creating-a-package"></a>

1. Hover over **Salesforce DX** and select **Packages**.
2. Click **Create Package**.
3. Enter a **Package Name** and **Package Description**.
4. Choose **Package Type:** _Unlocked_ or _Managed_.
5. Select the **Dev Hub** that owns the package.
6. Choose the **Version Control Repository** and **Branch**.
7. Pick the **Package Directory**.

<figure><img src="../../.gitbook/assets/image (1453).png" alt="Create Package form fields"><figcaption></figcaption></figure>

***

#### Step 2: Create a Package Version <a href="#step-2-create-a-package-version" id="step-2-create-a-package-version"></a>

A **package version** is an immutable snapshot of the metadata in your package. You can install it in scratch orgs, sandboxes, or production.

Fill in the **Package Version** section:

1. **Version Name** – auto-generated from the package name (editable).
2. **Version Description** – brief summary.
3.  **Version Number** – format **major.minor.patch.build** (e.g., `1.2.3.4`).

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>The version must contain <strong>four</strong> dot-separated numbers. Any other format causes an error.</p></div>
4. **Installation Key** – optional password to protect the package.
5. **Tag** – release label such as `Release 1.0.0`.

<figure><img src="../../.gitbook/assets/image (1454).png" alt="Package Version details"><figcaption></figcaption></figure>

***

**Package Dependencies**

If the Dev Hub owns other packages, they appear here.

* Move items between lists with
  * ![Add dependency](<../../.gitbook/assets/image (1445).png>) and ![Remove dependency](<../../.gitbook/assets/image (1446).png>)
* Re-order with
  * ![Move up](<../../.gitbook/assets/image (1455).png>) and ![Move down](<../../.gitbook/assets/image (1457).png>)

<figure><img src="../../.gitbook/assets/image (1458).png" alt="Package Dependencies list"><figcaption></figcaption></figure>

***

Click **View Metadata** or **Create Package**:

*   **View Metadata** – review the metadata pulled from VCS before creating.

    <figure><img src="../../.gitbook/assets/image (1459).png" alt="View Metadata list"><figcaption></figcaption></figure>
* **Create Package** – create the package with the specified data.

Progress appears on the **Unlocked Package** home screen.

<figure><img src="../../.gitbook/assets/image (1460).png" alt="Package home progress"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1461).png" alt="Package progress details"><figcaption></figcaption></figure>

***

### More Information on the Package Screen <a href="#more-information-on-the-package-screen" id="more-information-on-the-package-screen"></a>

<figure><img src="../../.gitbook/assets/image (1462).png" alt="Package management screen"><figcaption></figcaption></figure>

1. **Status** – view success/failure and download the log.
2. **Actions**
   * **Delete Package** – permanently removes the package.
   * **Create Version** ![Plus icon](<../../.gitbook/assets/image (1445).png>) – add a new version.
3. **Info** – hover for package metadata.

**View Packaged Versions** ![View versions icon](<../../.gitbook/assets/image (1463).png>) – shows each version’s details.

<figure><img src="../../.gitbook/assets/image (1464).png" alt="Packaged version details"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Notes**

1. For _unlocked_ packages, the latest promoted version is used as the ancestor.
2.  For _managed_ packages:

    * If no ancestor chosen, the latest promoted version is selected.
    * Selecting **None** creates a version without an ancestor.
    * To choose a non-latest ancestor, tick **Skip Ancestor Check**.

    <figure><img src="../../.gitbook/assets/image (1465).png" alt="Skip ancestor check option"><figcaption></figcaption></figure>
3. Non-linear versioning in the same branch is restricted.
{% endhint %}

***

#### Promote

Promote a package version to make it installable outside scratch orgs.\
You may promote only **once** per version number.

{% hint style="info" %}
* Code coverage must be **≥ 75 %** for promotion.
* Older versions created before code-coverage checks show **0 %** but remain unaffected.
{% endhint %}

***

#### Package Info Tooltip

Hover the info icon to see author, timestamps, and last-modified details.

<figure><img src="../../.gitbook/assets/image (1466).png" alt="Package information tooltip"><figcaption></figcaption></figure>
