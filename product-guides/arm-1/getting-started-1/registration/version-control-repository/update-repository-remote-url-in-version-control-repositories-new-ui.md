# Update Repository Remote URL in Version Control Repositories (New UI)

**Product:** AutoRABIT ARM\
**Module:** Admin – Version Control Repositories\
**Availability:** New UI\
**Access:** Registered Organization Super Admin only

### Overview

AutoRABIT ARM now allows **Super Admins to update the remote URL of an existing Version Control repository** directly from the repository Details screen.

This enhancement simplifies repository management when a repository URL changes due to repository migration, organization renaming, or switching between HTTPS and SSH connections, eliminating the need to contact AutoRABIT Support for manual updates.

### What's New?

#### 1. Update Repository URL

* A new **Edit** option is available next to the Repository URL in the **Details** tab.
* Clicking Edit opens an **Update Repository URL** dialog displaying the current URL and allowing users to enter a new URL.
* ARM validates the new URL to ensure it is valid, different from the existing URL, and not already registered with another repository.

#### 2. Confirmation and Update Status

Before updating the URL, ARM displays the following confirmation message:

**"Ensure no users are performing any actions or have any pending tasks on this repository before you change its URL."**

Once confirmed:

* ARM processes the URL update in the background.
* A loading indicator appears while the update is in progress.
* Upon completion, ARM displays a **Success, Warning, or Error** message based on the outcome.
* The repository list is refreshed to display the updated URL.

#### 3. Automatic Reference Updates

ARM automatically updates the repository URL across associated configurations and records, including user mappings, Version Control settings, commit labels, CI jobs, merge history, and pull request history.

This helps maintain consistency across existing repository references.

### How to Update a Repository URL

1. Log in to AutoRABIT ARM as the **Registered Organization Super Admin**.
2. Navigate to **Admin > Version Control Repositories**.
3. Select the required repository and open the **Details** tab.
4. Click the **Edit** icon next to the Repository URL.
5. Enter the new URL in the **Update Repository URL** dialog.
6. Review the confirmation warning and ensure no active or pending operations exist for the repository.
7. Confirm the update and wait for the operation to complete.
8. Once completed, verify the updated URL in the repository details.

### Important Notes

* Only the **Registered Organization Super Admin** can update repository URLs. Standard Admins and other users cannot access this option.
* The new URL must not be empty, contain spaces, match the existing URL, or already be registered with another repository.
* Ensure there are **no active or pending operations** on the repository before initiating the update.
* Only one repository rename or URL update operation can run at a time within an organization.
* If an update is already in progress, the Edit option remains unavailable until the operation completes.
* If the repository URL has changed since the page was loaded, ARM requests that the user refresh the page before proceeding.
* If the update completes with partial failures, ARM displays a warning. The same update can be submitted again to complete the remaining changes.
* Existing local Git workspaces are not updated immediately. Subsequent checkouts use the updated repository URL.
* Repository URL update activities and outcomes are recorded under **Admin > Audit**.

### Benefits

* **Self-Service Management:** Allows Super Admins to update repository URLs without Support intervention.
* **Reduced Manual Effort:** Automatically updates associated repository references.
* **Improved Visibility:** Provides real-time progress and completion status.
* **Controlled Updates:** Includes validation, confirmation, and access restrictions.
* **Better Traceability:** Records repository URL changes in audit logs.
