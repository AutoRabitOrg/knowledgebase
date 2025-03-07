# Release Notes 25.1

## nCino + Data Loader 25.1.2 Release Notes

**Release Date: 9 March 2025**

#### **Data Loader Performance Improvement**

**Optimized Field Extraction:** nCino introduced an enhancement that optimizes the field extraction process during data retrieval. Previously, Data Loader Pro fetched all available fields from an object during extraction, which could lead to unnecessary data processing and performance inefficiencies. Data Loader Pro now retrieves only the fields explicitly mapped by the user.

**Key Benefits:**

* **Improved Performance** – Reduces processing time by extracting only the necessary fields.
* **Optimized Data Handling** – Prevents retrieval of unneeded data, leading to a more streamlined extraction process.
* **Greater Control** – Users can now ensure that only relevant fields are included in the extraction, enhancing data accuracy and efficiency.

This enhancement ensures a more efficient and user-centric data extraction experience in [Data Loader Pro](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/dataloader/dataloader-pro).

## nCino + Data Loader 25.1.0 Release Notes

**Release Date: 23 February 2025**

* **Increased Unit Coverage for Data Loader & Data Loader Pro:** Expanded unit test coverage to enhance efficiency in nCino & Data Loader.
* **Data Loader API Migration: SOAP to REST:** Converted Data Loader APIs from SOAP to REST for improved performance and maintainability.
* **Performance Optimization:** Enhanced job execution performance for faster processing.
* **Data Consistency Fix:** Resolved an issue to ensure reliable and consistent data transfers.
