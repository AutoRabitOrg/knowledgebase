# Working with Translations in ARM

Translation feature can help you translate almost everything in your organization ranging from Salesforce custom objects, fields, labels, etc. This provides users with different languages to interact with Salesforce.

### A. Commit and deploy 'Custom Object' translations with ARM <a href="#a-commit-and-deploy-custom-object-translations-with-arm" id="a-commit-and-deploy-custom-object-translations-with-arm"></a>

In order to translate custom objects for a variety of languages, you need to commit the following components.

1. Select the `CustomObject` metadata type and select the specific custom objects that you want to move the translation.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Select the `CustomObjectTranslation` metadata type and select the translations associated with the custom object.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Point to Note:**

* The translation will not take place and nothing will be retrieved if you merely use the `CustomObjectTranslation` metadata type and leave out the `Custom Object`.
* The translation should be activated for the custom object in the destination org.

### B. Commit and deploy 'Custom Field' Translations with ARM <a href="#b-commit-and-deploy-custom-field-translations-with-arm" id="b-commit-and-deploy-custom-field-translations-with-arm"></a>

To commit and deploy custom field translations with ARM, you need to commit the following components.

1. Select the `CustomField` metadata type and select the specific custom fields that you want to move the translation.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Select the metadata type `CustomObjectTranslation` and select the members associated with the custom object.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Troubleshooting:**

In some circumstances, the `CustomObjectTranslation` might just have the opening and closing xml tags. In this situation, we advise you to do a commit while selecting the **Review Artifacts** option, allowing you to inspect the contents of the files before committing them.

### C. Commit and Deploy 'Custom Label' Translations with ARM <a href="#c-commit-and-deploy-custom-label-translations-with-arm" id="c-commit-and-deploy-custom-label-translations-with-arm"></a>

Translations for custom labels determine what text to display for the label’s value when a user’s default language is the translation language.

To commit or deploy custom label translations with ARM, you need to commit the following components.

1. Select the name of the custom label you want to translate available under the `CustomLabel` metadata type.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Look for the `Translation` metadata type and select the language from the list.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### D. Commit and Deploy 'Field Set' Translations with ARM <a href="#d-commit-and-deploy-field-set-translations-with-arm" id="d-commit-and-deploy-field-set-translations-with-arm"></a>

A field set is a group of different fields. For example, a field set that contains fields describing a user's first name, last name, occupation, etc.

In order to commit and deploy field set translations with ARM, you need to commit the following components.

1. Select the `FieldSet` metadata type and select the specific field set(s) that you want to move the translation.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Select the metadata type `Translations` and select the language you want the translations to be moved. This deploy the field sets along with the translations for the language selected.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### E. Commit and Deploy 'Standard Value Set' Translations with ARM <a href="#e-commit-and-deploy-standard-value-set-translations-with-arm" id="e-commit-and-deploy-standard-value-set-translations-with-arm"></a>

In order to commit and deploy standard value set translations with [ARM](https://www.autorabit.com/products/automated-release-management/), you need to commit the following components.

1. Select the `StandardValueSet` metadata type and select the specific standard value sets that you want to move the translation.
2. Select the `StandardValuesetTranslation` metadata type and select the respective metadata members from the list.
3. Select the metadata type `Translations` and select the language you want the translations to be moved. This deploy the standard value sets along with the translations for the language selected.

### F. Commit and Deploy 'Global Value Set' Translations with ARM <a href="#f-commit-and-deploy-global-value-set-translations-with-arm" id="f-commit-and-deploy-global-value-set-translations-with-arm"></a>

In order to commit and deploy global value set translations with ARM, you need to commit the following components.

1. Select the `GlobalValueSet` metadata type and select the specific global value sets that you want to move the translation.
2. Select the `GlobalValuesetTranslation` metadata type and select the global value set translations metadata members from the list.
3. Select the metadata type `Translations` and select the language you want the translations to be moved. This deploy the global value sets along with the translations for the language selected to the Version Control branch.
