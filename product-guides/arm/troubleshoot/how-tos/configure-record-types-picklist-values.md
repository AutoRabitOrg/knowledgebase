# Configure Record Types Picklist Values

### Overview <a href="#overview" id="overview"></a>

The Record Type node contains certain picklist fields and their corresponding picklist values that are assigned to Record Type.

<figure><img src="../../../../.gitbook/assets/image (68) (1) (1) (1) (1) (1) (1).png" alt="" width="389"><figcaption></figcaption></figure>

As per the behavior of Salesforce, if a user likes to retrieve a certain picklist field along with the Record type, only those picklist values in the Record Type Node get retrieved.

* **RecordTypes PicklistValues** configuration as **Replace**: For every EZ-Commit operation, if the Record Type has no picklist values, it will override the Record Type node in the version control even it has more than one picklist field value.
* **RecordTypes PicklistValues** configuration as **Replace All**: This is the same as **'Replace,'** the only difference is it will replace the entire existing picklist values.
* **RecordTypes PicklistValues** configuration as **Append**: Instead of overriding the entire record type picklist values, it adds to the existing picklist values.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) ( (2).png" alt=""><figcaption></figcaption></figure>

The below table highlights the expected behavior on **Picklist Fields** and **Picklist Values** of Record Type node for **Append**, **Replace** and **Replace All** configuration.

| ITEM                                           | OPERATION                                                                                                                                                                                                                                                                                                                                              | ACTION _(Performed in your CustomObject file in Version Control)_                                                                                                                                                                                                                                                           |             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| <p><br><br>Picklist Field/Value Assignment</p> | <p><br></p>                                                                                                                                                                                                                                                                                                                                            | **Added/Modified**                                                                                                                                                                                                                                                                                                          | **Deleted** |
| Append (No Overwrite)                          | <ol><li><strong>Added/Modified:</strong> Reads the CustomObject file and appends the CHANGE ( PicklistField/ PicklistValue) to the RecordType Assignment irrespective of the existing data.</li></ol>                                                                                                                                                  | No Action                                                                                                                                                                                                                                                                                                                   |             |
| Replace (Partial Overwrite)                    | <ol><li><strong>Modified:</strong> Reads the existing Picklist fields in the CustomObject file and overwrites it with the newly introduced CHANGE in the RecordType Assignment.</li><li><strong>Added:</strong> Reads the existing Picklist fields in the CustomObject file and adds the  CHANGE into the RecordType Assignment. </li></ol><p><br></p> | Deleted Picklist Fields/Values will be permanently removed from the Version Control system.                                                                                                                                                                                                                                 |             |
| Replace All (Complete Overwrite)               | <ol><li><strong>Modified/Added:</strong> Overrides the entire RecordType in the CustomObject file with the CHANGE</li></ol>                                                                                                                                                                                                                            | <p>Deletes the entire Picklist Fields/Values as the action will overwrite the entire RecordType Picklist Assignment.<br><strong>Note:</strong> To delete a Picklist field assignment from RecordType node in your VCS, select the entire Picklist fields and its corresponding Record type in your EZ-Commit operation.</p> |             |

| **Added**    | A new Picklist Field/value has been introduced in the Salesforce Org    |
| ------------ | ----------------------------------------------------------------------- |
| **Modified** | An existing Picklist Field/value has been changed in the Salesforce Org |
| **Deleted**  | A Picklist Field/Value has been deleted in the Salesforce Org           |
| **Change**   | Difference pulled from the Salesforce Org                               |

#### Example: <a href="#example" id="example"></a>

**A. Configuration for recordTypes picklistValues as 'Replace'**

**Scenario 1-** **Picklist field exists in the Record Type:** If the Picklist field exists in the Record Type, it overrides its corresponding Picklist values.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Before:** Search Picklist field 1

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After:** Picklist field 1 being available, it overrides the existing values for Picklist field 1



**Scenario 2- Picklist field does not exist in the Record Type:** It searches for the Picklist field availability in the Record Type and if the Picklist field is not present, it gets added to the Record Type. Refer to the screenshot attached below:

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Before:** Search Picklist field 2

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After:** Picklist field 2 not being available, it gets added to the Record Type thereby acting as an append operation

**B. Configuration for recordTypes picklistValues as 'Replace ALL'**

Replaces the entire Picklist fields and its corresponding Picklist values for the Record type.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Before**

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After**

**C. Configuration for recordTypes picklistValues as 'Append'**

There can also be two possible scenarios:

**Scenario 1-** Picklist field exists in the Record Type: If the Picklist field exists in the Record Type, it updates the existing Picklist values and adds the new ones.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Before:** Search Picklist field 1

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After:** Picklist field 1 being available, new Picklist Values gets added



**Scenario 2- Picklist Field does not exist in the Record Type:** Its searches for the Picklist Field availability in the Record Type and if the Picklist Field is not present, it gets added to the Record Type. Refer to the screenshot attached below:

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Before:** Search Picklist field 2

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After:** Picklist Field 2 not being available, it gets added to the Record Type

See our FAQ: [Can I Update or Remove Picklist Values with CI Job?](https://knowledgebase.autorabit.com/fundamentals/faq/ci-jobs#id-19.-can-i-update-or-remove-picklist-values-with-ci-job)
