# Commit the Vlocity Components to a Branch

This section deals with exporting of vlocity data packs from a Salesforce Org through a YAML manifest describing your project and committing the same to a Version Control System. The primary goal is to enable Continuous Integration for vlocity metadata through source control.

### Commit Vlocity Components <a href="#commit-vlocity-components" id="commit-vlocity-components"></a>

1. Go to the **New EZ-Commit** screen,

<figure><img src="../../../../.gitbook/assets/image (61) (1) (1).png" alt="" width="479"><figcaption></figcaption></figure>

2. In the **EZ-Commit** screen, select your **Salesforce Org.**
3. Select the **Salesforce Org Author**.
4. Under **Commit To** section, select the **Version Control Repository** and the **Branch** where the commits need to be done.

<figure><img src="../../../../.gitbook/assets/image (62) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**: The selection of a branch is only available if you have enabled **'Skip Mappings'** in the **My Profile** section.  Else, the branch will automatically be selected based on the org mappings and it is not editable.
{% endhint %}

5. Under **Fetch Changes**, select the components as **'Vlocity Components'**.

<figure><img src="../../../../.gitbook/assets/image (63) (1) (1).png" alt="" width="431"><figcaption></figcaption></figure>

#### Different options for Vlocity Components <a href="#different-options-for-vlocity-components" id="different-options-for-vlocity-components"></a>

**1. Auto Draft**

This will bring all the changes which the Author has done in the Salesforce Org which have not been committed yet to Version Control (AutoRABIT does the calculation by using the last modified date in the Salesforce org and comparing against the last commit date to Version Control branch).

**2. Select Manually**

This will export vlocity components from a Salesforce Org through a YAML manifest describing your project and committing the same to a Version Control System. The primary goal is to enable continuous integration for vlocity metadata through source control.

**3. Max Depth**

Max Depth decides the level of dependencies that will be executed while fetching and committing vlocity components. The value of Max Depth that was set while configuring vlocity will be used globally

However, the user can modify the value based on his requirement.

* When Max Depth Values is set to **-1** means it will execute all-level dependencies of the selected data pack record
* When Max Depth Values is set to **0** means it will execute only selected data pack records and
* When Max Depth Values is set to **1** means it will execute only first-level dependencies of the selected data pack record.

**4. Custom YAML File**

The user also has an option to upload a custom **YAML file** (Project path and manifest/queries fields are mandatory). In such a case, the already configured Data Packs Type will have no impact on the current commit label.

**5. Compile on Build**

When checked, it compiles the data you are attempting to deploy in your branch. **However, AutoRABIT recommends that you keep this checkbox unselected.** This is because the AR tool can throw a compilation error when you're trying to commit data that doesn't have dependent components keeping the '**Compile On Build'** checkbox selected.

**6. Auto Update Settings**

This option ensures you have the latest DataPack settings before each export and deployment. This check is quick and you are advised to allow it.

**7. Separate Matrix Versions**

Add Ability to Export Matrix Versions separately.

Fill in the remaining fields as per your requirements, and proceed to the next screen. The vlocity components will get retrieved based on the difference between the Salesforce org and below mentioned retrieval path. Select the components that you would like to commit to the branch.

### Possible Retrieval Path <a href="#possible-retrieval-path" id="possible-retrieval-path"></a>

#### A. For Custom YAML file <a href="#a-for-custom-yaml-file" id="a-for-custom-yaml-file"></a>

**Scenario 1:** If the metadata folder path is not available. For such a case, the vlocity components will fetch from the _**\<repoURL>/\<yaml project path>**_ path by default.

**Example:**

<figure><img src="../../../../.gitbook/assets/image (64) (1) (1).png" alt="" width="452"><figcaption></figcaption></figure>

**Retrieval Path:**_**"\<repoURL>/\<yaml project path>"**_**Scenario 2:** The metadata folder path is available.In such case, the vlocity components will get retrieved from _r**epoURL>/\<metadata folder path>/\<yaml project path>**_.

**Example:**

<figure><img src="../../../../.gitbook/assets/image (65) (1) (1).png" alt="" width="452"><figcaption></figcaption></figure>

**Retrieval Path:**_**"\<repoURL>/\<Vlocity Component>/\<yaml project path>"**_

#### B. For Default YAML file <a href="#b-for-default-yaml-file" id="b-for-default-yaml-file"></a>

**Scenario 1:** The metadata folder path is not available. For such a case, the vlocity components will fetch from _**\<repoURL>/autorabit\_alldefault\_vlocity\_build**_ path by default.

**Example:**

<figure><img src="../../../../.gitbook/assets/image (66) (1) (1).png" alt="" width="452"><figcaption></figcaption></figure>

**Retrieval Path**: _**"\<repoURL>/\<autorabit\_alldefault\_vlocity\_build>"**_

**Scenario 2:** The metadata folder path is available.In such case, the vlocity components will get retrieved from _**\<repoURL>/\<metadata folder path>**_.

**Example:**

<figure><img src="../../../../.gitbook/assets/image (67) (1) (1).png" alt="" width="452"><figcaption></figcaption></figure>

**Retrieval Path:**_**"\<repoURL>/\<metadata folder path>"**_
