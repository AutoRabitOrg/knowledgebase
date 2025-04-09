# Release Notes 25.1

## **nCino + Data Loader 25.1.3 Release Notes**

**Release Date: 6 April 2025**

* **Enhanced Job Prioritization in Queue:** The queue functionality has been enhanced to allow users to **prioritize jobs** effectively. Users can now **rearrange jobs based on priority**, and the updated job order will be **saved persistently in the queue**, ensuring execution follows the defined priority.
* **VC Code Performance Optimization:** Refactored the **VC code** to enhance **performance and efficiency**, ensuring smoother execution and improved system responsiveness.
* **Improved Circular Reference Handling:** Fixed an issue to ensure **circular references are correctly identified and not ignored** during processing, improving data integrity and system stability.
* **Source ID Column Visibility Fix:** Resolved an issue where the **"Source ID" column was not visible** on the results screen. The column is now correctly displayed to ensure complete data visibility.

## nCino + Data Loader 25.1.2 Release Notes

**Release Date: 9 March 2025**

* **Optimized Field Extraction:** nCino introduced an enhancement that optimizes the field extraction process during data retrieval. Previously, Data Loader Pro fetched all available fields from an object during extraction, which could lead to unnecessary data processing and performance inefficiencies. Data Loader Pro now retrieves only the fields explicitly mapped by the user.
* **Data Loader Performance Improvement**
  * **Enhanced Object Selection**: Newly identified objects during job execution are now included only if the selected child objects have Master-Detail parents apart from the master object, preventing unintended inclusion of lookup relation parents.
  * **Database Persistence**: Any newly identified objects during job execution are now saved to the database for future reference.
  * **Improved Error Handling**: If an exception occurs, the job status is now set to "Failed" instead of "No Records," ensuring accurate job execution tracking.
  * **AutorabitExtId\_\_c Validation**: The system now verifies whether `AutorabitExtId__c` exists and ensures it is marked as "External Id" and "Unique," automatically setting it to true if necessary.

## nCino + Data Loader 25.1.0 Release Notes

**Release Date: 23 February 2025**

* **Increased Unit Coverage for Data Loader & Data Loader Pro:** Expanded unit test coverage to enhance efficiency in nCino & Data Loader.
* **Data Loader API Migration: SOAP to REST:** Converted Data Loader APIs from SOAP to REST for improved performance and maintainability.
* **Performance Optimization:** Enhanced job execution performance for faster processing.
* **Data Consistency Fix:** Resolved an issue to ensure reliable and consistent data transfers.
