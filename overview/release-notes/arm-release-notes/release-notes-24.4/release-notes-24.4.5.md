# Release Notes 24.4.5

## ARM Release Notes 24.4.5

**Release Date: 19 January 2025**

With this release, we have implemented the following enhancements and support fixes to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

**Email and Username Validation**

Registration processes now enforce unique email addresses and usernames, ensuring each email is linked to only one active account. Added email verification confirms ownership, enhancing security and preventing duplication. _Impacted Modules: Admin - User Registration, Subscription Management._

**Optimized Merge File Processing**

The VALIDATINGSALESFORCEXML performs a single file check during branch-to-branch merges. Merged file data is stored uniquely, improving performance by preventing duplicate validations. _Impacted Modules: EZ-Merge._

**Enhanced XSS Protection**

Implemented robust measures to prevent XSS risks, including validation of untrusted data, HTML sanitization, and Content Security Policy (CSP). These updates safeguard data and prevent script-based attacks. _Impacted Modules: All Modules._

### Support <a href="#support" id="support"></a>

**Improved Remote Site Settings Updates**

URL updates now run seamlessly in the destination org, regardless of sorting preferences. A new mechanism ensures tests proceed smoothly, even if individual cases fail. _Impacted Modules: Environment Provisioning. Support Case: #129418._

**Consistent Merge Validation**

The merge validation process now handles internal folder references accurately. Files in helper folders are fully validated, ensuring consistent results across merges and deployments. _Impacted Modules: EZ-Merge with validate deployment. Support Case: #124974._

**SharingRules Metadata Visibility**

SharingRules metadata is now visible and selectable for deployment and commit operations. Child metadata exclusions were adjusted to ensure proper visibility. _Impacted Modules: All Modules. Support Case: #126615._

**Support for GenAiPromptTemplate**

ARM now supports the GenAiPromptTemplate component, ensuring compatibility with Salesforce updates and enhancing functionality. _Impacted Modules: VC, Deployment, CI Jobs. Support Case: #126142._

**Aligned Branching Baseline Behavior**

Branching Baseline now matches EZ-commit behavior for Default manageable state metadata. Excluded Default metadata, such as Account.object-meta.xml, is no longer committed. _Impacted Modules: Branching Baseline. Support Case: #126634._

**Faster CI Job Assignment**

Agent assignment during CI jobs has been optimized, and a new feature flag allows streamlined verification using repository and username data, reducing delays. _Impacted Modules: CI Jobs using Version Control._

**Reliable Backup CI Jobs**

Backup CI jobs now handle DX metadata exclusions and dashboard queries correctly, ensuring successful scheduled backups. _Impacted Modules: CI Jobs, Deployments, EZ-Commits. Support Case: #128621._

**Merge Validation for Short Metadata Names**

Merge validation now properly handles metadata names shorter than 9 characters. Improved logic ensures accurate validations without failures. _Impacted Modules: EZ-Merge, EZ-Commit with validate deployment. Support Case: #128764._

**Commit Label Preservation**

Commit labels are now retained even when associated pre-validation labels are removed, ensuring labels remain accessible and visible. _Impacted Modules: EZ-Commit, Commit Label EZ-Merge, Commit Label Deployment. Support Case: #128102._
