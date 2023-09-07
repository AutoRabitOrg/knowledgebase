# Preparing the CSV file for ARM Dataloader

When creating the CSV file, you will have to take into the below considerations:

### File format and general recommendations <a href="#file-format-and-general-recommendations" id="file-format-and-general-recommendations"></a>

* ARM dataloader accepts CSV (comma separated values) files. Use a spreadsheet program such as Microsoft Excel to create your CSV file.
* The file must be UTF-8 encoded
* Make sure you don't have any duplicated or empty headers.
* Ensure you do not have any empty columns or any columns with the same header names as this can cause field mapping issues.
* Ensure you have a column header and rows of data populated for all system required fields such as Account Name or Contact Last Name
* Try to name your column headers with the same names as your Salesforce id fields to make mapping easier.
* In your Excel file prior to saving it as a CSV, leverage conditional formatting functionality to highlight cells with duplicate values in columns that should not have duplicates
* Keep your files at a maximum size of 10MB.
* When dealing with files that are larger than **200 rows**, pick the **Use Bulk API** option in the **Run Configuration** dialog box. This will give you optimum performance for large files.
* Data Loader does not allow importing multiple columns into one field in Salesforce. You will need to concatenate these fields before uploading.

### Field type format supported <a href="#field-type-format-supported" id="field-type-format-supported"></a>

#### ID Field <a href="#id-field" id="id-field"></a>

Case-sensitive 15-character alphanumeric string that uniquely identifies a particular record (ex. 003D000000yUbCD)

#### Number <a href="#number" id="number"></a>

Can only contain numbers and decimal spaces. ARM dataloader will not accept text in number fields

#### Text <a href="#text" id="text"></a>

Can support all characters

#### Currency <a href="#currency" id="currency"></a>

Can only contain numbers and decimal spaces

Remove all currency symbols and commas from the number and currency columns.

#### Date <a href="#date" id="date"></a>

Must be in the format: MM-DD-YYYY or YYYY-MM-DD. Please see the Salesforce Help Topic “[Data Loader Date Values](https://help.salesforce.com/s/articleView?language=en\_US\&mode=1\&type=1\&id=000325035)” for other options

#### Date/Time <a href="#datetime" id="datetime"></a>

Must be in the format: MM-DD-YYYYThh:mm:ss-hh:mm or YYYY-MM-DDThh:mm:ss-hh:mm

#### Email <a href="#email" id="email"></a>

Must contain @ sign and dot some type of text at the end (.com, .uk, .org, etc.)

#### Checkbox <a href="#checkbox" id="checkbox"></a>

Must contain TRUE or FALSE / 1 or 0 values

#### Zip Code <a href="#zip-code" id="zip-code"></a>

If you’re working with Zip Code data that has leading zeros, Excel will remove these zeros. Leverage the Zip Code cell format to put them back. Remember, you will need to do this formatting again if you convert from Excel to CSV.

#### RecordTypeID <a href="#recordtypeid" id="recordtypeid"></a>

ID used to designate which type of record type the record will be

#### Lookup Fields <a href="#lookup-fields" id="lookup-fields"></a>

Must contain record ID from an existing record in ARM.

### Sample CSV file <a href="#sample-csv-file" id="sample-csv-file"></a>

The following CSV sample includes 11 records for the Account object. Each record contains six fields. You can include any field for an object that you're processing. If you use this file to update existing accounts, any fields that aren't defined in the CSV file are ignored during the update.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JPSF51D7.png" alt=""><figcaption></figcaption></figure>
