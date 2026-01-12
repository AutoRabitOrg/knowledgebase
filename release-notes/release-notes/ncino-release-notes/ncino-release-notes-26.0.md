# nCino Release Notes 26.0

## nCino + DL - Release 26.1.2

**Release Date: 11 January 2026**

**Clone Version – Bucket Filter Retention**

Fixed an issue where filters applied to entry objects were not retained when switching between buckets in a cloned version, ensuring filter configurations persist consistently across buckets.

**Create Version – Entry Object Query Not Retained Across Object Sets**

Fixed an issue where entry object filter queries from the original version were not fully populated when creating a new version of a multi-bucket feature template. The filter queries are now consistently carried forward for all object sets during version creation.

## nCino + DataLoader - Release 26.1.1

**Release Date: 04 January 2026**

### **Version Control Source Reset in CI Jobs** <a href="#version-control-source-reset-in-ci-jobs" id="version-control-source-reset-in-ci-jobs"></a>

Resolved an issue where source details were not refreshed when changing the source type or repository during CI Job editing. The source configuration now resets correctly, ensuring accurate and consistent setup.

### **Single DataLoader – Limit Value Persistence Issue** <a href="#single-dataloader-limit-value-persistence-issue" id="single-dataloader-limit-value-persistence-issue"></a>

Fixed an issue where an unintended record limit was applied to subsequent Single DataLoader jobs. The system now correctly resets and applies record counts and limits when running jobs again or switching between extract, insert, and update operations with new CSV files.

### **DataLoader Extract – Download Performance Improvement** <a href="#dataloader-extract-download-performance-improvement" id="dataloader-extract-download-performance-improvement"></a>

Improved the performance of the DataLoader Extract file download process. The download now initiates promptly upon user action, reducing extended pending time and ensuring faster response and file availability compared to earlier behavior.

### **nCino Object Migration with Rollback – Stability Fix** <a href="#ncino-object-migration-with-rollback-stability-fix" id="ncino-object-migration-with-rollback-stability-fix"></a>

Resolved an issue where nCino object migrations failed during rollback-enabled feature deployments. The rollback process has been stabilized to prevent errors and ensure successful execution during rollback builds.



















