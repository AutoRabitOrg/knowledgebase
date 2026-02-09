# Sharing Settings for Custom Objects

**Sharing Settings (OWD) for Custom Objects are part of the** `CustomObject` **metadata** and cannot be deployed or committed as a separate component. This behavior is consistent with how the Salesforce **Metadata API** manages object-level sharing settings.

When committing **only the Custom Object** (for example, to update OWD), Salesforce requires the following **mandatory XML nodes** to be present in the `CustomObject.object-meta.xml` file for a successful deployment across orgs:

* `<label>` – User-visible object name
* `<pluralLabel>` – Required for UI usage
* `<nameField>` – Primary record identifier (must include `<label>` and `<type>`: Text or AutoNumber)
* `<deploymentStatus>` – `Deployed` or `InDevelopment`
* `<sharingModel>` – Record-level access (`ReadWrite`, `ReadOnly`, or `Private`)

If any of these nodes are missing or invalid, the deployment will fail in the target org.

Currently, the **only safe and supported approach** to commit _only_ the OWD change is the following controlled method:

* Download the package from the **Review Artifact** screen
* Navigate to the **Objects** folder
* Retain only the required `CustomObject.object` file
* Remove other subfolders (fields, listViews, recordTypes, layouts, etc.)
* Review the CustomObject XML and keep only the required nodes (including the OWD update)
* Re-upload the updated `.zip` file and proceed with the commit

<figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

This ensures that **only the intended Sharing Settings change** is committed, without promoting any unintended metadata.

<figure><img src="../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
