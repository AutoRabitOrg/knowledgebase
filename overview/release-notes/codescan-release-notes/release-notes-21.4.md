# Release Notes 21.4

### CodeScan 21.4 <a href="#codescan-214" id="codescan-214"></a>

**Released Date: 01 July 2021**

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* **Enhanced Reports**: CodeScan's weekly reports have been improved, with more scheduling choices, insights into project issue patterns, logs of project configuration changes, and false positives logged.
* **Enhanced Metadata Ruleset**: Before deploying from the developer environment, Salesforce metadata components can now be scanned to ensure that they have an associated description, improving the clarity around their purpose and function.
* **Rulesets for nCino**: In this release, nCino-specific rules have been added. CodeScan can now limit the number of sharing rules, as well as active and inactive workflow rules created on an object in order to prevent performance impact due to system overload caused by extensive calculations when a record is created or updated. Users may customize these rules for their own purposes.
* **Improved AutoRABIT integration**: CodeScan reports generated from AutoRABIT for a project or Salesforce org are now consolidated as individual branches under their respective CodeScan projects rather than in a separate new project. This allows the user to show continuity in the reports and retain history tracking, making the integration more helpful and intuitive.
