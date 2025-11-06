# Preparing the CSV file for ARM DataLoader

When creating the CSV file, follow the considerations below to ensure compatibility and efficiency with ARM DataLoader.

***

### File Format and General Recommendations <a href="#file-format-and-general-recommendations" id="file-format-and-general-recommendations"></a>

1. Files must be in **CSV (Comma-Separated Values)** format. Use Microsoft Excel or a similar spreadsheet program to create your file.
2. Ensure the file is **UTF-8 encoded**.
3. Do **not include duplicated or empty headers**.
4. Remove **empty columns** and **duplicate header names**, as these can disrupt field mapping.
5. Include **column headers and data rows** for all **required system fields** (e.g., _Account Name_, _Contact Last Name_).
6. **Match column headers to Salesforce API field names** for easier mapping.
7. Use Excel’s **conditional formatting** to highlight duplicate values in fields that must be unique before saving.
8. File size must not exceed **10MB**.
9. For files with **more than 200 rows**, enable **"Use Bulk API"** during **Run Configuration** for better performance.
10. **Concatenate fields** before upload—DataLoader does not merge multiple columns into one Salesforce field.

***

### Field Type Format Supported <a href="#field-type-format-supported" id="field-type-format-supported"></a>

#### ID Field

* **Format:** 15-character alphanumeric, case-sensitive (e.g., `003D000000yUbCD`)

#### Number

* Accepts **only numbers and decimal points**. Text values are not allowed.

#### Text

* Accepts **all characters**, including letters, numbers, and symbols.

#### Currency

* Accepts **numbers and decimal points only**.
* **Remove** currency symbols and commas.

#### Date

* Format: `MM-DD-YYYY` or `YYYY-MM-DD`\
  Refer to [Salesforce Date Formatting](https://help.salesforce.com/s/articleView?language=en_US\&mode=1\&type=1\&id=000325035) for alternatives.

#### Date/Time

* Format: `MM-DD-YYYYThh:mm:ss-hh:mm` or `YYYY-MM-DDThh:mm:ss-hh:mm`

#### Email

* Must include `@` and a valid domain suffix (e.g., `.com`, `.org`, `.uk`)

#### Checkbox

* Use **TRUE/FALSE** or **1/0**

#### Zip Code

* Excel may strip **leading zeros**. Format cells as _text_ and reapply after conversion to CSV.

#### RecordTypeID

* Provide the **record type ID** for each relevant entry.

#### Lookup Fields

* Must contain a **valid record ID** from an existing ARM record.

***

### Sample CSV File <a href="#sample-csv-file" id="sample-csv-file"></a>

Below is a sample CSV containing 11 records for the **Account** object. Each row includes six fields. You may include additional fields based on your data needs. Fields omitted from the CSV will not be updated.

<figure><img src="../../../../.gitbook/assets/image (1139).png" alt="Sample CSV file with 11 account records and corresponding field headers"><figcaption></figcaption></figure>
