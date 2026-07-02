# Scan Settings

### Scan Settings

Configuration to control the projects that are being scanned from CICD Pipelines

1. Navigate to **`Settings`** -> **`Global Settings`**.
2. Search for **`IZ Scan Settings`** and click on edit.
3. Updated the required pattern to exclude or include the projects -
   1. **`PROJECT_NAME_INCLUDE_PATTERN`** - By default, all the projects will be scanned
   2. **`PROJECT_NAME_EXCLUDE_PATTERN`** - By default, no projects will be excluded from scan
   3. **`ABORT_ON_PATTERN_VALIDATION_FAILURE`** - Indicates if the build should be aborted if it's not allowed based on the pattern configuration
   4. **`ALLOW_ALREADY_SCANNED_PROJECTS`** - Determines whether the build should continue or abort if the project has already been scanned once

### See Also

* [Configure IZ Scan Plugin](anypoint-studio/configuration/iz-suite-configuration.md)
* [Source Code Analysis - On The Fly Results](anypoint-studio/source-code-analysis/anypoint-studio-analysis.md)
