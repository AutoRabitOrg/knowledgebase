# Automatic Cleanup of Deactivated Picklist Values

#### What is changing in ARM?

ARM now automatically removes references to deactivated picklist values from all impacted Record Types associated with the same Salesforce object.

#### Why is this needed?

When a picklist value is deactivated at the field level, Salesforce removes its availability from associated Record Types. However, Record Type metadata already stored in Git may continue to reference the deactivated value if those Record Types are not included in the commit.

This can result in stale metadata and potential deployment validation issues.

#### How did ARM handle this previously?

Previously, ARM removed the deactivated picklist value only from the Record Types explicitly selected as part of the commit.

Other Record Types under the same object could continue to reference the deactivated value in Git.

#### How does ARM handle this now?

When a picklist value is deactivated, ARM will:

1. Identify the parent object.
2. Scan all Record Types under that object.
3. Identify Record Types referencing the deactivated value.
4. Remove the invalid reference.
5. Automatically include the impacted Record Types in the commit.

#### Do I need to select all impacted Record Types?

No. ARM automatically scans all Record Types under the parent object, regardless of which Record Types you selected for the commit.

#### Will ARM modify unrelated Record Types or metadata?

No. Only Record Types containing references to the deactivated picklist value are updated. Active picklist values and unrelated metadata remain unchanged.

#### What is the benefit?

This enhancement keeps field and Record Type metadata synchronized in Git, reduces stale metadata references and deployment issues, and eliminates the need to manually identify and commit every affected Record Type.
