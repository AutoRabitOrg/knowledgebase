# Release Notes 4.3

### CodeScan 4.3 <a href="#codescan-43" id="codescan-43"></a>

#### New Features <a href="#new-features" id="new-features"></a>

**New Apex Security Hotspots**

* **Deserializing JSON Is Security-Sensitive**: Deserializing an object from an untrusted source is security-sensitive. An attacker could modify the content of the data.
* **Encrypting Data Is Security-Sensitive**: Encrypting data is security-sensitive. Although most encryption problems are solved or managed by Salesforce, care must be taken when relying on encryption.
* **Type Reflection Is Security Sensitive**: Dynamically executing code is security-sensitive. If the code comes from an untrusted source, the untrusted source may be able to choose which code to run.
* **Using Cookies Is Security-Sensitive**: Attackers can use widely available tools to view the cookie and read the sensitive information. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.
* **Using UserInfo.GetSessionId() Is Security-Sensitive**: The use of UserInfo.GetSessionId() is security-sensitive. Ensure that you need to do this.

**New Visualforce Security Hotspots**

* **Using GETSESSIONID() and $API.Session\_Id is security-sensitive**: The use of GETSESSIONID() and $API.Session\_Id is security-sensitive. Ensure that you need to do this.

**Quality Profiles**

* Removed Unescaped Source rule from default Apex profile (**v4.3.12**).
* Removed deprecated rule javascript: S2228 from Salesforce Lightning Quality Profile (**v4.3.9**).

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* SonarQube™ Ant task has been updated to **2.6.0.1**
* SOQL Injection Rule updated and improved.(**v4.3.11**)
* Open Redirect Rule updated and improved. (**v4.3.11, v4.3.12**)

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* Bug fixed in RightLineBracesPositions rule.
* Bug fixed in Field Level Security Vulnerabilities rule. (**v4.3.10**)
* Bug fixed in Preserve Stack Trace Rule (**v4.3.12**)
* Bug fixed in Unescaped Source Rule (**v4.3.12**)
