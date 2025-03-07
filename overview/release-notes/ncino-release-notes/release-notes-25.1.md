# Release Notes 25.1

## nCino + Data Loader 25.1.2 Release Notes

**Release Date: 9 March 2025**

### **nCino Improvements**

**Optimized Field Extraction**: The system now fetches only the fields mapped by the user, reducing unnecessary data extraction and improving efficiency.

### **Data Loader Performance Improvements**

* Any new object identified during job execution should be included in the job only if the selected child objects have Master-Detail relationships with the parent, apart from the master object. However, lookup relationship parents are also being included in the job.
* Any such new objects should be saved to the database.
* If an exception occurs, the status should be marked as "Failed" instead of "No Records."
* When checking for the existence of `AutorabitExtId__c`, if it exists, verify whether it is marked as "External Id" and "Unique." If not, set it to `true` as required.

## nCino + Data Loader 25.1.0 Release Notes

**Release Date: 23 February 2025**

* **Increased JUnit Coverage for Data Loader & Data Loader Pro:** Expanded unit test coverage to enhance efficiency in nCino & Data Loader.
* **Data Loader API Migration: SOAP to REST:** Converted Data Loader APIs from SOAP to REST for improved performance and maintainability.
* **Performance Optimization:** Enhanced job execution performance for faster processing.
* **Data Consistency Fix:** Resolved an issue to ensure reliable and consistent data transfers.
