# Commit Templates

### What are Commit Templates?

Commit Templates are predefined collections of metadata that you use regularly to commit, saving you time and eliminating the need to pick metadata each time you pull together. **For example-** If you frequently pull the two picklist fields Standard Case Reason field and the Custom Case Sub Reason field. Instead of having to search through each metadata type individually, it would be good if they were pre-bundled into a commit suite that included the standard value set, standard field, custom field, and common record type.

### How do I create a new Commit Template?

To create a fresh commit template:

1. Sign in to your AutoRABIT account.
2. Click **Create New > New Commit Template** from the top navigation bar or hover your mouse over the **Version Control** tab and select **Commit Templates**.&#x20;
3. Click on **New Commit Template**. The **Commit Templates** screen is best viewed when the zoom setting is set to **75%** on your chrome/firefox browser.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Give the template a **Label Name**.&#x20;
5. Choose the **Source Org**. All available metadata will be fetched based on the source org selection.

{% hint style="info" %}
**Important Note:** The templates aren't dependent on the Source Org you choose. This means you can use this template to add/modify metadata components from different Salesforce Organizations.
{% endhint %}

6. **Optional:** Enter a description of the template.
7. Click **Next**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

8. Choose the **metadata components (including their members)** that should be included in the template. Use the **search** filter to quickly find and add any particular metadata member.
9. The **Selected** tab will show you all of the metadata you've chosen and are ready to use in the template.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. Click **Next**.
11. The next screen will allow viewing the components you're going to use in the template one more time before you save it. You can also go back to the previous screen and add any metadata components that were overlooked.
12. Finally, click on **Save Template**.&#x20;
13. You'll be redirected to the **Commit Templates Summary** page after confirmation, where you'll see your freshly created commit template at the top of the list.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For each commit template, you can find the below details:

| Attribute              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Template Name          | Name of the template.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Created By             | The author who created the template                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Created Date/Timestamp | Date and Timestamp when the template was created                                                                                                                                                                                                                                                                                                                                                                                                          |
| Description            | The template's description. If nothing appears, it means that no description was given at the time the template was created.                                                                                                                                                                                                                                                                                                                              |
| Last Used              | <p>Timestamp when the template was last used.<br></p><p><strong>Note:</strong> The templates used for the commit process will be color-coded in GREEN for easier differentiation, while the unused templates will be color-coded in ORANGE.</p>                                                                                                                                                                                                           |
| Share Template         | <p>Share your template with the rest of your team.</p><p></p><p><strong>Note:</strong> The text will appear as <strong>Shared Template</strong> if your org admin or sub-users shared their commit templates with you.</p>                                                                                                                                                                                                                                |
| Actions                | <p>Additional actions for each template:</p><ul><li><strong>Edit</strong>: Add/modify/delete the components included in the template</li><li><strong>Clone</strong>: Create a duplicate template with all the data from the parent template</li><li><strong>Download</strong>: Download the template in your local system. The file format is Package.XML</li><li><strong>Delete</strong>: Deletes the template. This process cannot be undone.</li></ul> |

### Filtering Commit Templates

You can search for commit templates within a particular **salesforce organization** or view the templates that are created by yourself. To see all your teammates commit, simply turn **Created By Me** toggle bar to the left side, and all the commits templates will be shown there.

It is also possible to search for templates based on the **content**. To filter the exact result, you need to enter the commit template label or title in the search field.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

It's always a good idea to break data into multiple pages when dealing with multiple templates records. You can browse 25, 50, 75, or 100 records on a single page, or you can navigate to the previous or next page using the **Previous** and **Next** buttons.

### Using a Commit Template during EZ-Commit

You can use the predefined components included in the template for your commit operation. To do so,

1. Go to the **New EZ-Commit** screen.
2. Select your **Source Org** and its related **Author**.
3. Select your **Version Control Repository** and **Branch**.
4. On the **Fetch Changes** tab, select the Components as **Metadata Components**.
5. Select the **Use Commit Template** option and choose your template from the drop-down list.
6. Under the  **Perform** tab, select the commit process (_prevalidate commit_ or _commit_ only).
7. Leave the rest of the field as default and proceed to the next screen. Click **Next**.
8. The next screen will be divided into 3-4 different  tabs:
   * **Added/Modified Metadata Components:** On this page, you'll notice that some of the components are selected by default, while others are disabled. The auto-selected components are a part of both the commit template and your source org. The disabled components mean that they are part of the commit template, but they are missing from your source org.
   * **Deleted:** AutoRABIT compares the change with the source org and the version control branch and lists all the components that are available in the branch. If you like to delete those components from the branch while committing, you can select those components in this tab.&#x20;
   * **All Metadata Components:** All of the metadata components that are available for your source org will be listed here. Select the components you like to commit to the Version Control branch.
   * **Selected:** Total components that you have selected will get displayed in this tab. The metadata components that will be newly added or updated in the destination branch will be shown as A/M (Added/ Modified) and the components that will get deleted from the destination branch will be shown as D (Deleted) under the **Action** tab.
9. Click **Next**.
10. On the final screen, fill in with the necessary **Commit Setting** details.
11. To create a fresh template using the selected metadata components, select the checkbox: **Use Selected Metadata and Create a Commit Template**
12. Give the template a unique **name** and a short **description** of it. Adding a description is optional.
13. Click on **Save and Commit**.&#x20;
14. You'll be taken to the **Commits** screen, where you can monitor the progress of the most recent commit. The newly generated template will appear at the top of the **Commit Templates** screen.
