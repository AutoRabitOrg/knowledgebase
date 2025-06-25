# Destructive Changes

> **Note:** The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.

### About Destructive Changes <a href="#destructive-changes" id="destructive-changes"></a>

Removing dead code is an important software development aspect that is often neglected. In the world of Salesforce and Apex development, removing dead code promotes a cleaner code base, improves test coverage, and helps reduce deployment time. Unused code will slow you down in both the speed of your application and the speed of your developers in their ability to improve the application. Regularly cleaning up unused code is a good practice.

#### Types of Destructive Changes <a href="#types-of-destructive-changes" id="types-of-destructive-changes"></a>

1. **Post Destructive Changes:** Deletes unwanted fields or metadata components from your destination Salesforce org **after** a successful deployment.
2. **Pre Destructive Changes:** Deletes unwanted fields or metadata components from your destination Salesforce org **before** the deployment begins.

### Deploying Destructive Changes <a href="#deploying-destructive-changes" id="deploying-destructive-changes"></a>

After selecting the components to deploy to the target Salesforce org, navigate to the **Destructive Items** tab.

![Destructive Items Tab](../../../../.gitbook/assets/image (65) (1) (1).png)

You’ll see metadata components in your target org that are absent in your source under the **Post-Destructive Changes** tab. Select the checkboxes next to components you wish to delete—these will be removed upon deployment.

You can also delete components via **Modify**, selecting them and defining their destructive nature.

![Modify Components](../../../../.gitbook/assets/image (66) (1).png)
![Component Options](../../../../.gitbook/assets/image (67) (1).png)

- **Clear All:** Clears all selected components for pre- and post-destructive changes.
- **Reset:** Resets selection to default auto-populated components.

ARM applies test level and validation behavior to destructive deployments. It performs compilation checks and enforces code coverage for production deployments.

### Destructive Changes on a Custom Object <a href="#destructive-changes-on-a-custom-object" id="destructive-changes-on-a-custom-object"></a>

Deleting a custom object triggers deletion of:
- Custom object file
- Translation, layout, workflow files
- Sharing, matching, assignment, auto-response, escalation rules
- Trigger files
- Object and field permissions in profiles and permission sets

Note: To delete these from the **source org**, manual deletion is required.

### Destructive Changes on a Custom Field <a href="#destructive-changes-on-a-custom-field" id="destructive-changes-on-a-custom-field"></a>

Deleting a custom field removes:
- The field from the object, page layouts, reports, record types, and list views
- Field permissions in profiles and permission sets
"""

# Create directory and save Markdown
output_dir = Path("/mnt/data/destructive_changes_doc")
output_dir.mkdir(parents=True, exist_ok=True)
markdown_path = output_dir / "destructive_changes.md"
markdown_path.write_text(markdown_content)

# Create a ZIP archive
zip_path = "/mnt/data/destructive_changes_package.zip"
with ZipFile(zip_path, 'w') as zipf:
    zipf.write(markdown_path, arcname="destructive_changes.md")

zip_path
