# Feature Migration Templates

## What is a Feature Migration Template?&#x20;

A Feature Migration Template in AutoRABIT is essentially a blueprint that helps you manage and automate the process of moving features from one environment to another. It’s like a checklist that defines exactly what should be moved, how it should be transferred, and in what order — ensuring everything gets to the new environment correctly, without missing any critical steps.&#x20;

A template saves time and effort by letting you set up migration rules once and use them repeatedly for consistent, error-free deployments. Whether you're moving configurations, customizations, or entire features, a template streamlines the whole process, making it much smoother and more predictable.&#x20;

## Standard vs Community Templates&#x20;

**Standard Feature Templates**: These are templates that are pre-defined and ready to be used by customers/partners. Such templates are updated regularly as nCino releases changes to any configurations. AutoRABIT provides several default templates to be directly used by our community for migrating Record-Based Configurations (RBCs). &#x20;

**Community Feature Templates**: Community templates are non-standard templates. In other words, users can define their own migration templates that are not already published by AutoRABIT. Community templates are useful if there are any customizations in nCino users want to migrate that are not listed as part of the default Standard templates. &#x20;

Community templates, just like the Standard ones, are designed to be long-lasting. They can be created once, then used multiple times as a template.&#x20;

## Record Configurations <a href="#record-configuration" id="record-configuration"></a>

This section allows users to configure nCino records. The nCino platform that will be available to your end users solely depends on how the records are configured. Every record of nCino that the end user interacts with, you can configure a different outcome for the same. The entire platform’s behavior lies on these Record-Based Configurations (RBCs).&#x20;

1.  **Selected List**&#x20;

    This list shows the objects that you have explicitly picked to include in your migration. These are the features or configurations you actually want to move, like specific custom objects that are part of the change you're working on.&#x20;
2.  **Related List**&#x20;

    Objects in this list are automatically identified by AutoRABIT as being related to your selected objects. For example, if your selected object has lookup relationships or dependencies, those related objects will appear here. This ensures all necessary dependent data is considered during migration.&#x20;
3.  **Required List**&#x20;

    These are objects that AutoRABIT identifies as essential for the integrity of the migration. They are mandatory and cannot be removed from the template. This typically includes standard Salesforce objects or configurations that are foundational to the selected features.&#x20;
4.  **Excluded List**&#x20;

    This list comprises objects that are not required and have been explicitly excluded from the migration. You might place objects here to prevent unnecessary data from being migrated, especially if it's irrelevant to the current feature or could cause conflicts in the target environment. Note that such objects in the excluded list are still available for user selection (case-by-case basis).&#x20;

AutoRABIT automatically groups related objects into different buckets based on how they’re connected. While it’s not required, you’ll need to apply at least one filter to each bucket. By default, AutoRABIT marks one object in each bucket as the "entry point" — that’s the object the filter will apply to. Although you can choose any object, it’s generally a best practice to apply the filter to the entry point itself, since that helps keep things clean and consistent.&#x20;

