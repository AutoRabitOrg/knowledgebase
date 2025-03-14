# Release Notes 4.4

### CodeScan 4.4 <a href="#codescan-44" id="codescan-44"></a>

#### New Features <a href="#new-features" id="new-features"></a>

**New Cloud Features**

* **Salesforce Project Branch Types**: when adding a sandbox to your Salesforce project as a branch, you are now able to specify the type of branch you would like to add (Long or Short). Find out more here about branches here.

**New Metadata Rules**

* **BETA metadata ruleset added**: our beta metadata ruleset has been added to this release. Currently, you will find rules covering security settings, custom fields, permissions, and record type ID's. This edition also includes a setting to define the metadata types to be downloaded. Find out more here for CodeScan Cloud and here for a Self Hosted package.xml file.

**New Apex Rules**

* **Aura Controller Naming**: Aura Controllers should adhere to certain naming conventions. Only classes linked to a page as a controller or extension are considered.
* **Track Usage of @SuppressWarnings**: overuse of the @SupressWarnings annotation can mean issues in your code are not picked up. This rule flags each usage to make sure it is needed.
* **Track Usage of //NOSONAR**: overuse of the //NOSONAR rule suppression can mean issues in your code are not picked up. This rule flags each usage to make sure it is needed.
* **Static can not be used in Inner Class (v4.4.5**): Static can only be used on fields, properties, and methods of top-level classes only.
* **Avoid using Tab Characters Check (v4.4.5)**: Checks that there are no tab characters ('\t') in the source code.

**New Visualforce Rules**

* **Avoid using Tab Characters Check (v4.4.5)**: checks that there are no tab characters ('\t') in the source code.

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* Field Level Security now specifies the field it is failing on.
* Old Page API Version now specifies the API version in the message (**v4.4.4**).
* Metadata parsing was improved to fix memory errors caused by larger types (**v4.4.5**).

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* Excessive Method Length no longer counts comments as lines.
* Use Singleton now ignores Aura controllers.
* NPath Complexity now calculates correctly around ternary statements.
* False-positive fixed in Unnecessary Boolean Assertion.
* Avoid Public Fields now ignores Aura fields.
* False positive fixed in InlineStyleAttributesCheck for lightning:formattedNumber tag (**v4.4.4**).
* Field Level Security no longer detects WITH\_SECURITY\_ENFORCED (**v4.4.4**).
* Edge cases of DML parsing fixed (**v4.4.4**).
* Edge cases of Copado parsing fixed (**v4.4.4**).
* Classes extending nested classes parsing fixed (**v4.4.4**).
* General Parser fixes and improvements (**v4.4.4**).
* InsecureEndpointRule throws StackOverflowError while analyzing the attached Apex class (**v4.4.5**).
* Parsing error caused by using "Sharing" as Enum name fixed (**v4.4.5**).
* Parsing error caused by using "import" (Javascript) fixed. BREAKING CHANGE - This will cause new errors to be created on previously unparsed files (**v4.4.6**).
* Error caused by custom fields in SFDX projects fixed (**v4.4.6**).
