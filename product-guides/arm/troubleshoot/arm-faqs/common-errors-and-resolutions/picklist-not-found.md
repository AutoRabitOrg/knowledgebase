# Picklist not found

## Error message: Picklist not found

The potential causes of _Picklist not found_ error-related Merge/Commit Prevalidation deployment failures are listed below, along with the procedures you need to follow to fix them:

* **Verify the field name:** Verify the API name or the label of the picklist field you're trying to reference and the spelling and capitalization of your source.
* **Check the object:** Verify the object you're working with has the picklist field you're looking for. Locate the proper object by going to the **Object Manager** in **Salesforce Setup**. Look for the disputed field in the **Fields & Relationships** section in the target org.
* **Validate field-level security:** Make sure the user or profile you're using can see and access the picklist field. Ensure the user has the appropriate permissions to see and update the field by checking the field-level security settings for their profile. Check the **field-level security settings** to ensure the user's profile has appropriate permissions to view and edit the field.
* **Consider record types:** If your Salesforce org utilizes record types, check to see if the picklist field is specific to a particular record type. If it is, ensure that the user or profile you're using has access to the relevant record type.
* **Consider field dependencies:** If the picklist field has any field dependencies or controlling fields, ensure that the controlling field values are set correctly. If the controlling field values are incorrect or incompatible, it can lead to the "picklist field not found" error.
